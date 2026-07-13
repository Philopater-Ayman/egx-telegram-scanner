# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-13T08:40:34.614467+00:00
Generated Cairo: 2026-07-13 11:40
Run timing: target 08:45 Cairo | generated Cairo 2026-07-13 11:40 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-13 11:35

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 76
- Data quality issues: 1
- Tradeable price/liquidity tickers: 182/189
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 13
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 65.0% / above MA50 55.0%
- EGX70 regime: BULLISH / above MA20 82.5% / above MA50 72.5%
- Sector breadth: 57.14%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- CCAP.CA: liquidity=484055008.0 spike=0.74 score=27.9
- ZMID.CA: liquidity=151282192.0 spike=0.69 score=28.9
- AREH.CA: liquidity=107658224.0 spike=3.03 score=33.96
- RAYA.CA: liquidity=102567512.0 spike=0.89 score=30.9
- ZEOT.CA: liquidity=95883032.0 spike=2.45 score=13.8

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlights ELEC.CA as the top priority buy‑ready ticket, followed by GDWA.CA and RAYA.CA. All three sit above their 20‑day MA, show modest RSI, and have clear support‑resistance zones. EGX30 and EGX70 are both in a bullish regime with strong breadth, placing the market in a BROAD_RISK_ON mode, but confidence remains low and short‑term outlook carries uncertainty.
- ELEC.CA: price 2.19 EGP, support 2.04, resistance 2.18, liquidity spike 4.1×, RSI 51.9 – aligns with bullish macro trend.
- GDWA.CA: price 0.84 EGP, support 0.76, resistance 0.82, liquidity spike 4.9×, sector not leading but meets technical criteria.
- RAYA.CA: price 8.36 EGP, support 6.80, resistance 8.29, RSI 63.8 – momentum extended, watch for pull‑back near resistance.
- EGX30/EGX70 bullish breadth (65‑83% above MA20) supports risk‑on stance, yet low confidence flags potential volatility.
- Uncertainty: low confidence scores, sector‑lead concerns, and possible short‑term reversals; verify price action on Thndr before acting.

## Top Liquidity Spikes
- RACC.CA: spike=8.52 liquidity=89090880.0 outlook=BULLISH_WATCH score=77.4 buy_ready=True
- MOSC.CA: spike=5.86 liquidity=53680396.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GDWA.CA: spike=4.92 liquidity=79895968.0 outlook=BULLISH_WATCH score=92.4 buy_ready=True
- ELEC.CA: spike=4.11 liquidity=77833776.0 outlook=BULLISH_WATCH score=100 buy_ready=True
- AREH.CA: spike=3.03 liquidity=107658224.0 outlook=BULLISH_WATCH score=91.4 buy_ready=True

## Sector Leaderboard
- #1 Technology & Distribution: score=12.84 5d=4.42% 20d=18.68% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=11.04 5d=2.41% 20d=4.51% aboveMA50=100.0%
- #3 Real Estate: score=10.16 5d=3.68% 20d=14.76% aboveMA50=100.0%
- #4 Telecommunications: score=10.07 5d=5.07% 20d=6.67% aboveMA50=100.0%
- #5 Transportation & Logistics: score=9.98 5d=3.01% 20d=7.21% aboveMA50=100.0%
- #6 Automotive & Distribution: score=8.53 5d=-0.72% 20d=9.65% aboveMA50=100.0%
- #7 Fintech & Payments: score=8.39 5d=4.38% 20d=9.24% aboveMA50=50.0%
- #8 Textiles: score=8.0 5d=3.17% 20d=5.0% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY ELEC.CA
  - Entry: 2.19 | Take profit: 2.37 | Stop loss: 2.1
  - Confidence: LOW | score=35.9 | outlook=BULLISH_WATCH 100
  - Reason: BUY SETUP: ELEC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 51.85, support 2.04, resistance 2.18, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY GDWA.CA
  - Entry: 0.84 | Take profit: 0.9 | Stop loss: 0.81
  - Confidence: LOW | score=33.9 | outlook=BULLISH_WATCH 92.4
  - Reason: BUY SETUP: GDWA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 51.8, support 0.76, resistance 0.82, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY RAYA.CA
  - Entry: 8.36 | Take profit: 9.02 | Stop loss: 8.03
  - Confidence: LOW | score=30.9 | outlook=BULLISH_WATCH 77
  - Reason: BUY SETUP: RAYA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 63.79, support 6.8, resistance 8.29, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELEC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ALCN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- MENA.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EGAS.CA: BULLISH_WATCH score=93.12 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- GDWA.CA: BULLISH_WATCH score=92.4 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- AREH.CA: BULLISH_WATCH score=91.4 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- TMGH.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORHD.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SWDY.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MOED.CA: BULLISH_WATCH score=86.4 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- ELEC.CA: rank=35.9 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=2.19 support=2.04 resistance=2.18 liquidity=77833776.0
- AREH.CA: rank=33.96 outlook=BULLISH_WATCH outlook_score=91.4 sector_rank=9 price=1.72 support=1.51 resistance=1.76 liquidity=107658224.0
- GDWA.CA: rank=33.9 outlook=BULLISH_WATCH outlook_score=92.4 sector_rank=9 price=0.84 support=0.76 resistance=0.82 liquidity=79895968.0
- RACC.CA: rank=32.9 outlook=BULLISH_WATCH outlook_score=77.4 sector_rank=9 price=10.55 support=9.36 resistance=10.57 liquidity=89090880.0
- RAYA.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=77 sector_rank=1 price=8.36 support=6.8 resistance=8.29 liquidity=102567512.0
- ETEL.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=80 sector_rank=4 price=97.83 support=89.01 resistance=101.5 liquidity=40495644.0
- ACGC.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=80.0 sector_rank=8 price=10.09 support=8.92 resistance=9.88 liquidity=21237502.0
- COSG.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=79.4 sector_rank=9 price=1.67 support=1.47 resistance=1.66 liquidity=34291436.0
- ELSH.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=62.4 sector_rank=9 price=14.69 support=11.1 resistance=15.11 liquidity=32134194.0
- MASR.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=62.4 sector_rank=9 price=8.12 support=6.71 resistance=7.95 liquidity=42830728.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=23.6 buy_ready=False sector_rank=9 price=239.11 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=5698232.0 spike=0.38
- ABUK.CA: score=21.48 buy_ready=False sector_rank=19 price=69.9 support=66.66 resistance=77.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=31992674.0 spike=0.22
- ACAMD.CA: score=27.9 buy_ready=True sector_rank=9 price=2.36 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=20274748.0 spike=0.21
- ACGC.CA: score=29.9 buy_ready=True sector_rank=8 price=10.09 support=8.92 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=21237502.0 spike=0.97
- ADCI.CA: score=14.87 buy_ready=False sector_rank=9 price=232.38 support=223.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=967065.63 spike=0.08
- ADIB.CA: score=27.61 buy_ready=True sector_rank=12 price=46.83 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=49.79 liquidity=14044354.0 spike=0.15
- ADPC.CA: score=29.64 buy_ready=True sector_rank=9 price=3.79 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=29884970.0 spike=1.87
- AFDI.CA: score=26.12 buy_ready=True sector_rank=9 price=47.13 support=40.8 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=59.42 liquidity=6215645.5 spike=0.46
- AFMC.CA: score=24.8 buy_ready=True sector_rank=9 price=75.48 support=66.0 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=5597770.0 spike=1.65
- AJWA.CA: score=17.47 buy_ready=True sector_rank=9 price=182.98 support=150.51 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=57.66 liquidity=1574219.13 spike=0.06
- ALCN.CA: score=29.3 buy_ready=True sector_rank=5 price=30.44 support=27.7 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=28182862.0 spike=1.7
- ALUM.CA: score=15.73 buy_ready=False sector_rank=9 price=22.93 support=20.55 resistance=24.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=826464.31 spike=0.11
- AMER.CA: score=25.9 buy_ready=False sector_rank=3 price=3.14 support=2.28 resistance=3.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=22088432.0 spike=0.27
- AMES.CA: score=11.74 buy_ready=False sector_rank=9 price=93.97 support=83.13 resistance=94.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58153488.0 spike=1.42
- AMIA.CA: score=14.45 buy_ready=False sector_rank=9 price=8.9 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=552143.0 spike=0.06
- AMOC.CA: score=24.55 buy_ready=False sector_rank=13 price=8.05 support=7.42 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=27407570.0 spike=0.53
- APSW.CA: score=13.82 buy_ready=False sector_rank=9 price=8.3 support=8.0 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=45.6 liquidity=1198308.25 spike=1.36
- ARAB.CA: score=28.98 buy_ready=False sector_rank=3 price=0.24 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=94225760.0 spike=1.04
- ARCC.CA: score=13.8 buy_ready=False sector_rank=18 price=55.18 support=53.0 resistance=57.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=46.04 liquidity=3941423.0 spike=0.19
- AREH.CA: score=33.96 buy_ready=True sector_rank=9 price=1.72 support=1.51 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 July 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=107658224.0 spike=3.03
- ARVA.CA: score=15.37 buy_ready=False sector_rank=9 price=10.83 support=10.5 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=46.12 liquidity=1473667.38 spike=0.07
- ASCM.CA: score=25.9 buy_ready=True sector_rank=9 price=62.61 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=32953022.0 spike=0.4
- ASPI.CA: score=18.72 buy_ready=False sector_rank=9 price=0.32 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=39.06 liquidity=4823156.0 spike=0.17
- ATLC.CA: score=16.58 buy_ready=True sector_rank=17 price=5.22 support=4.77 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=1376703.25 spike=0.2
- ATQA.CA: score=16.5 buy_ready=False sector_rank=19 price=9.59 support=9.21 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=4021867.0 spike=0.12
- AXPH.CA: score=18.57 buy_ready=False sector_rank=9 price=1191.55 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=670742.44 spike=0.23
- BINV.CA: score=16.25 buy_ready=False sector_rank=11 price=48.96 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=346181.19 spike=0.05
- BIOC.CA: score=20.27 buy_ready=False sector_rank=9 price=73.82 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=52.12 liquidity=365561.66 spike=0.11
- BTFH.CA: score=23.21 buy_ready=True sector_rank=17 price=3.07 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=19820250.0 spike=0.1
- CAED.CA: score=22.89 buy_ready=True sector_rank=9 price=74.36 support=68.0 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=51.31 liquidity=2987633.25 spike=0.46
- CANA.CA: score=17.41 buy_ready=False sector_rank=12 price=36.49 support=34.7 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=41.44 liquidity=805933.75 spike=0.08
- CCAP.CA: score=27.9 buy_ready=True sector_rank=11 price=5.36 support=4.65 resistance=5.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=59.41 liquidity=484055008.0 spike=0.74
- CCRS.CA: score=24.42 buy_ready=True sector_rank=9 price=2.44 support=2.18 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=8515550.0 spike=0.76
- CEFM.CA: score=16.9 buy_ready=False sector_rank=9 price=104.39 support=95.75 resistance=110.5 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=55.4 liquidity=2002200.19 spike=1.0
- CERA.CA: score=20.56 buy_ready=True sector_rank=9 price=1.31 support=1.17 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=2664496.75 spike=0.13
- CFGH.CA: score=9.93 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12 July 01:25 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=9605.83 spike=1.51
- CICH.CA: score=16.4 buy_ready=False sector_rank=17 price=11.99 support=11.36 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=7336145.0 spike=1.93
- CIEB.CA: score=18.1 buy_ready=False sector_rank=12 price=24.28 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=490063.94 spike=0.07
- CIRA.CA: score=27.21 buy_ready=False sector_rank=16 price=30.91 support=26.0 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=70.57 liquidity=18341298.0 spike=0.79
- CLHO.CA: score=16.67 buy_ready=True sector_rank=14 price=16.37 support=14.85 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=55.59 liquidity=1219474.5 spike=0.03
- CNFN.CA: score=21.59 buy_ready=True sector_rank=17 price=4.83 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=4383897.5 spike=0.1
- COMI.CA: score=27.61 buy_ready=True sector_rank=12 price=135.51 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=47513116.0 spike=0.11
- COPR.CA: score=18.84 buy_ready=False sector_rank=9 price=0.37 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=32.73 liquidity=8935710.0 spike=0.43
- COSG.CA: score=29.9 buy_ready=True sector_rank=9 price=1.67 support=1.47 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=34291436.0 spike=0.85
- CPCI.CA: score=16.7 buy_ready=False sector_rank=9 price=401.79 support=355.5 resistance=434.99 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=74.79 liquidity=798758.54 spike=0.35
- CSAG.CA: score=19.17 buy_ready=True sector_rank=5 price=32.49 support=30.85 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=1271746.88 spike=0.08
- DAPH.CA: score=23.89 buy_ready=True sector_rank=9 price=85.08 support=77.12 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=59.99 liquidity=3991089.25 spike=0.45
- DEIN.CA: score=0.9 buy_ready=False sector_rank=9 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=17.93 buy_ready=False sector_rank=15 price=27.01 support=24.21 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=60.17 liquidity=537098.19 spike=0.1
- DSCW.CA: score=28.64 buy_ready=True sector_rank=9 price=1.85 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=51776152.0 spike=1.87
- DTPP.CA: score=23.03 buy_ready=False sector_rank=9 price=210.0 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=89.03 liquidity=8133233.0 spike=0.22
- EALR.CA: score=26.65 buy_ready=True sector_rank=9 price=377.8 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=57.03 liquidity=8747221.0 spike=0.74
- EASB.CA: score=16.22 buy_ready=False sector_rank=9 price=7.24 support=5.06 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=36.74 liquidity=2318294.75 spike=0.13
- EAST.CA: score=9.74 buy_ready=False sector_rank=15 price=36.67 support=36.6 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=29.64 liquidity=5347002.5 spike=0.12
- EBSC.CA: score=20.29 buy_ready=True sector_rank=9 price=1.94 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=2391174.75 spike=0.42
- ECAP.CA: score=15.15 buy_ready=False sector_rank=9 price=32.73 support=31.15 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=1250098.88 spike=0.14
- EDFM.CA: score=18.62 buy_ready=False sector_rank=9 price=349.09 support=310.2 resistance=349.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:50 AM market time freshness=DELAYED_CURRENT RSI=66.15 liquidity=724564.56 spike=0.97
- EEII.CA: score=19.03 buy_ready=True sector_rank=9 price=2.78 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=3129882.75 spike=0.14
- EFIC.CA: score=7.62 buy_ready=False sector_rank=19 price=183.0 support=180.02 resistance=207.75 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=19.85 liquidity=2826252.0 spike=1.66
- EFID.CA: score=21.38 buy_ready=True sector_rank=15 price=28.32 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=52.8 liquidity=3996182.75 spike=0.08
- EFIH.CA: score=27.9 buy_ready=True sector_rank=7 price=22.36 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=60.96 liquidity=11133138.0 spike=0.25
- EGAL.CA: score=20.31 buy_ready=False sector_rank=19 price=291.17 support=272.28 resistance=314.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=8837926.0 spike=0.18
- EGAS.CA: score=26.79 buy_ready=True sector_rank=13 price=51.36 support=46.51 resistance=54.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=41.76 liquidity=13178035.0 spike=1.62
- EGBE.CA: score=15.63 buy_ready=False sector_rank=12 price=0.45 support=0.43 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=17183.81 spike=1.0
- EGCH.CA: score=23.48 buy_ready=False sector_rank=19 price=13.3 support=12.13 resistance=14.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=29752918.0 spike=0.67
- EGSA.CA: score=14.9 buy_ready=False sector_rank=4 price=9.08 support=8.67 resistance=9.13 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=91.67 liquidity=1979.44 spike=0.39
- EGTS.CA: score=23.06 buy_ready=True sector_rank=3 price=18.41 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=4159383.0 spike=0.07
- EHDR.CA: score=27.9 buy_ready=True sector_rank=9 price=2.69 support=2.37 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=51.76 liquidity=11020860.0 spike=0.26
- EKHO.CA: score=9.55 buy_ready=False sector_rank=13 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=35.9 buy_ready=True sector_rank=2 price=2.19 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=77833776.0 spike=4.11
- ELKA.CA: score=27.9 buy_ready=False sector_rank=9 price=1.65 support=1.19 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=10599395.0 spike=0.21
- ELNA.CA: score=18.44 buy_ready=False sector_rank=9 price=39.89 support=35.55 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:49 AM market time freshness=DELAYED_CURRENT RSI=46.25 liquidity=535014.56 spike=0.86
- ELSH.CA: score=29.9 buy_ready=True sector_rank=9 price=14.69 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=64.31 liquidity=32134194.0 spike=0.18
- ELWA.CA: score=17.42 buy_ready=True sector_rank=9 price=2.07 support=1.87 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=1523347.5 spike=0.87
- EMFD.CA: score=19.49 buy_ready=False sector_rank=3 price=11.77 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=43.69 liquidity=4590013.0 spike=0.03
- ENGC.CA: score=27.9 buy_ready=False sector_rank=9 price=42.01 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=17726650.0 spike=0.75
- EOSB.CA: score=15.94 buy_ready=False sector_rank=9 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=35839.68 spike=0.47
- EPCO.CA: score=19.37 buy_ready=True sector_rank=9 price=9.26 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1470713.13 spike=0.22
- EPPK.CA: score=16.36 buy_ready=False sector_rank=9 price=14.29 support=11.72 resistance=15.25 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=69.3 liquidity=455879.58 spike=0.48
- ETEL.CA: score=29.9 buy_ready=True sector_rank=4 price=97.83 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=64.17 liquidity=40495644.0 spike=0.55
- ETRS.CA: score=20.15 buy_ready=True sector_rank=9 price=10.9 support=9.15 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=4254165.0 spike=0.05
- EXPA.CA: score=22.65 buy_ready=True sector_rank=12 price=18.75 support=18.03 resistance=18.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=56.44 liquidity=3046440.75 spike=0.12
- FAIT.CA: score=18.02 buy_ready=False sector_rank=12 price=37.09 support=35.06 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=414478.19 spike=0.16
- FAITA.CA: score=10.62 buy_ready=False sector_rank=12 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=44.83 liquidity=9466.08 spike=0.32
- FERC.CA: score=13.5 buy_ready=False sector_rank=19 price=75.65 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=48.71 liquidity=1026753.19 spike=0.26
- FWRY.CA: score=24.9 buy_ready=False sector_rank=7 price=19.22 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=23594510.0 spike=0.13
- GBCO.CA: score=25.9 buy_ready=True sector_rank=6 price=32.02 support=27.77 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=31945576.0 spike=0.38
- GDWA.CA: score=33.9 buy_ready=True sector_rank=9 price=0.84 support=0.76 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=79895968.0 spike=4.92
- GGCC.CA: score=18.04 buy_ready=False sector_rank=9 price=0.56 support=0.41 resistance=0.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=92.74 liquidity=3141509.0 spike=0.18
- GIHD.CA: score=26.36 buy_ready=True sector_rank=9 price=51.01 support=40.0 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=69.42 liquidity=26660620.0 spike=1.23
- GMCI.CA: score=16.45 buy_ready=False sector_rank=9 price=2.03 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=65.28 liquidity=552178.25 spike=0.51
- GRCA.CA: score=3.15 buy_ready=False sector_rank=9 price=53.48 support=48.74 resistance=53.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2253643.25 spike=0.73
- GSSC.CA: score=19.19 buy_ready=True sector_rank=9 price=261.55 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=65.51 liquidity=1292451.63 spike=0.29
- GTWL.CA: score=22.9 buy_ready=False sector_rank=9 price=111.36 support=46.0 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=89.45 liquidity=48073076.0 spike=0.51
- HDBK.CA: score=13.37 buy_ready=False sector_rank=12 price=77.81 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=10.6 liquidity=8760863.0 spike=0.22
- HELI.CA: score=25.9 buy_ready=False sector_rank=3 price=7.42 support=6.34 resistance=7.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=75.72 liquidity=49383836.0 spike=0.31
- HRHO.CA: score=19.21 buy_ready=False sector_rank=17 price=26.55 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=34909428.0 spike=0.27
- ICID.CA: score=19.62 buy_ready=True sector_rank=9 price=8.3 support=6.55 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=59.95 liquidity=3717115.5 spike=0.34
- IDRE.CA: score=23.54 buy_ready=True sector_rank=9 price=46.43 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=57.98 liquidity=3643884.5 spike=0.28
- IFAP.CA: score=17.2 buy_ready=False sector_rank=10 price=19.57 support=18.47 resistance=20.0 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=57.21 liquidity=2304269.61 spike=0.57
- INFI.CA: score=21.77 buy_ready=False sector_rank=9 price=103.5 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=71.89 liquidity=4870203.0 spike=0.5
- IRON.CA: score=14.62 buy_ready=False sector_rank=19 price=32.48 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=49.19 liquidity=2142842.25 spike=0.27
- ISMA.CA: score=10.37 buy_ready=False sector_rank=9 price=27.21 support=26.54 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=16.02 liquidity=1474098.88 spike=0.05
- ISMQ.CA: score=24.48 buy_ready=False sector_rank=19 price=9.72 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=72.31 liquidity=27191608.0 spike=0.19
- ISPH.CA: score=15.45 buy_ready=False sector_rank=14 price=11.38 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=13062040.0 spike=0.22
- JUFO.CA: score=16.0 buy_ready=False sector_rank=15 price=30.47 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=40.22 liquidity=2609915.5 spike=0.1
- KABO.CA: score=24.9 buy_ready=False sector_rank=8 price=7.65 support=6.04 resistance=7.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=88.76 liquidity=11089314.0 spike=0.38
- KWIN.CA: score=7.5 buy_ready=False sector_rank=9 price=68.23 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=33.96 liquidity=1604923.5 spike=0.12
- KZPC.CA: score=14.38 buy_ready=False sector_rank=9 price=8.7 support=8.26 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=7280287.0 spike=1.1
- LCSW.CA: score=22.96 buy_ready=True sector_rank=18 price=31.74 support=26.41 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=67.42 liquidity=6106791.5 spike=0.1
- LUTS.CA: score=23.9 buy_ready=False sector_rank=9 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=42.08 liquidity=10063903.0 spike=0.2
- MAAL.CA: score=17.36 buy_ready=False sector_rank=9 price=8.11 support=5.72 resistance=8.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=98.01 liquidity=4463719.0 spike=0.27
- MASR.CA: score=29.9 buy_ready=True sector_rank=9 price=8.12 support=6.71 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=62.67 liquidity=42830728.0 spike=0.5
- MBSC.CA: score=14.28 buy_ready=False sector_rank=18 price=241.37 support=222.66 resistance=256.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=2420088.75 spike=0.1
- MCQE.CA: score=15.81 buy_ready=False sector_rank=18 price=175.57 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=1955412.75 spike=0.13
- MCRO.CA: score=27.08 buy_ready=True sector_rank=9 price=1.31 support=1.17 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=37095560.0 spike=1.09
- MENA.CA: score=27.77 buy_ready=True sector_rank=3 price=7.1 support=6.41 resistance=7.59 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=58.06 liquidity=8433330.19 spike=1.22
- MEPA.CA: score=25.56 buy_ready=False sector_rank=9 price=1.67 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=44.74 liquidity=14396345.0 spike=1.33
- MFPC.CA: score=23.48 buy_ready=False sector_rank=19 price=37.35 support=34.22 resistance=40.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=49.84 liquidity=20210214.0 spike=0.2
- MFSC.CA: score=13.24 buy_ready=False sector_rank=9 price=46.22 support=44.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=51.37 liquidity=2343480.5 spike=0.3
- MHOT.CA: score=3.37 buy_ready=False sector_rank=21 price=16.42 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=15.69 liquidity=2469971.5 spike=0.16
- MICH.CA: score=16.7 buy_ready=False sector_rank=9 price=37.81 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=797973.38 spike=0.05
- MILS.CA: score=21.73 buy_ready=True sector_rank=9 price=139.9 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=5833545.0 spike=0.52
- MIPH.CA: score=18.42 buy_ready=False sector_rank=14 price=703.43 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=971843.88 spike=0.46
- MOED.CA: score=28.68 buy_ready=True sector_rank=9 price=0.73 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=25568158.0 spike=2.39
- MOIL.CA: score=15.68 buy_ready=False sector_rank=13 price=0.53 support=0.46 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=69.47 liquidity=131678.94 spike=0.45
- MOIN.CA: score=14.32 buy_ready=False sector_rank=9 price=23.95 support=22.6 resistance=25.25 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=48.18 liquidity=418933.41 spike=0.55
- MOSC.CA: score=15.9 buy_ready=False sector_rank=9 price=316.42 support=275.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53680396.0 spike=5.86
- MPCI.CA: score=18.48 buy_ready=True sector_rank=9 price=238.95 support=215.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=49.77 liquidity=2584123.0 spike=0.03
- MPCO.CA: score=25.9 buy_ready=True sector_rank=10 price=1.89 support=1.7 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=28171544.0 spike=0.34
- MPRC.CA: score=24.9 buy_ready=False sector_rank=9 price=42.97 support=31.72 resistance=43.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=89.47 liquidity=11347321.0 spike=0.24
- MTIE.CA: score=27.9 buy_ready=True sector_rank=6 price=9.59 support=8.75 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=55.23 liquidity=16340571.0 spike=0.8
- NAHO.CA: score=14.11 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=48426.17 spike=2.08
- NCCW.CA: score=25.9 buy_ready=True sector_rank=9 price=6.56 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=24429572.0 spike=0.98
- NEDA.CA: score=18.73 buy_ready=False sector_rank=9 price=2.8 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=386822.79 spike=1.22
- NHPS.CA: score=27.42 buy_ready=False sector_rank=9 price=80.0 support=61.55 resistance=83.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=75.67 liquidity=71851056.0 spike=2.26
- NINH.CA: score=18.26 buy_ready=False sector_rank=9 price=17.89 support=16.82 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=5363493.5 spike=0.73
- NIPH.CA: score=21.49 buy_ready=True sector_rank=14 price=176.16 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=4033545.75 spike=0.05
- OBRI.CA: score=25.37 buy_ready=True sector_rank=9 price=36.61 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=7469790.5 spike=0.22
- OCDI.CA: score=19.41 buy_ready=False sector_rank=3 price=26.89 support=20.24 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=78.6 liquidity=5512470.5 spike=0.06
- OCPH.CA: score=13.82 buy_ready=False sector_rank=9 price=353.28 support=337.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=65.84 liquidity=921301.44 spike=0.15
- ODIN.CA: score=11.02 buy_ready=False sector_rank=9 price=2.53 support=2.36 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15077933.0 spike=1.06
- OFH.CA: score=24.71 buy_ready=True sector_rank=9 price=0.63 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=61.46 liquidity=6810179.5 spike=0.32
- OIH.CA: score=22.21 buy_ready=False sector_rank=11 price=1.41 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=9311590.0 spike=0.13
- OLFI.CA: score=27.39 buy_ready=True sector_rank=15 price=23.1 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=58.56 liquidity=13658435.0 spike=0.41
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=687.43 support=681.14 resistance=691.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17012470.0 spike=1.0
- ORHD.CA: score=26.9 buy_ready=True sector_rank=3 price=38.9 support=36.92 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=47.12 liquidity=12933639.0 spike=0.08
- ORWE.CA: score=17.11 buy_ready=False sector_rank=8 price=22.71 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=37.21 liquidity=3207790.25 spike=0.17
- PHAR.CA: score=16.71 buy_ready=True sector_rank=14 price=86.93 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=1256641.5 spike=0.06
- PHDC.CA: score=19.9 buy_ready=False sector_rank=3 price=14.9 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=41687984.0 spike=0.13
- PHTV.CA: score=15.58 buy_ready=False sector_rank=9 price=298.45 support=204.03 resistance=304.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=89.79 liquidity=680652.56 spike=0.05
- POUL.CA: score=25.39 buy_ready=True sector_rank=15 price=40.38 support=34.99 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=69.01 liquidity=10237157.0 spike=0.24
- PRCL.CA: score=16.85 buy_ready=False sector_rank=18 price=34.92 support=24.14 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=75.45 liquidity=4989454.0 spike=0.1
- PRDC.CA: score=28.9 buy_ready=True sector_rank=3 price=8.48 support=6.2 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=16110546.0 spike=0.11
- PRMH.CA: score=25.9 buy_ready=True sector_rank=9 price=2.74 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=46.24 liquidity=10140718.0 spike=0.32
- RACC.CA: score=32.9 buy_ready=True sector_rank=9 price=10.55 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=89090880.0 spike=8.52
- RAKT.CA: score=15.05 buy_ready=False sector_rank=9 price=23.1 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=57.11 liquidity=352090.21 spike=1.4
- RAYA.CA: score=30.9 buy_ready=True sector_rank=1 price=8.36 support=6.8 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=63.79 liquidity=102567512.0 spike=0.89
- RMDA.CA: score=14.41 buy_ready=False sector_rank=14 price=4.98 support=4.81 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=3962813.25 spike=0.18
- ROTO.CA: score=23.51 buy_ready=True sector_rank=9 price=44.13 support=33.7 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=54.28 liquidity=5612188.5 spike=0.17
- RREI.CA: score=25.86 buy_ready=True sector_rank=9 price=3.85 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=5960806.0 spike=0.3
- RTVC.CA: score=15.91 buy_ready=False sector_rank=9 price=3.83 support=3.55 resistance=3.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=1013316.44 spike=0.23
- RUBX.CA: score=22.9 buy_ready=False sector_rank=9 price=13.37 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=80.15 liquidity=16036124.0 spike=0.29
- SAUD.CA: score=15.47 buy_ready=False sector_rank=12 price=21.52 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=862250.5 spike=0.13
- SCEM.CA: score=15.09 buy_ready=False sector_rank=18 price=62.28 support=60.14 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=3230548.75 spike=0.19
- SCFM.CA: score=22.54 buy_ready=True sector_rank=9 price=260.89 support=226.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=2638662.0 spike=0.49
- SCTS.CA: score=17.75 buy_ready=False sector_rank=16 price=616.22 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=544024.94 spike=0.1
- SDTI.CA: score=16.53 buy_ready=False sector_rank=9 price=47.1 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=631871.0 spike=0.08
- SEIG.CA: score=24.9 buy_ready=False sector_rank=9 price=269.99 support=180.6 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=85.04 liquidity=11035386.0 spike=0.57
- SIPC.CA: score=19.83 buy_ready=True sector_rank=9 price=3.53 support=3.25 resistance=3.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=46.75 liquidity=1934343.25 spike=0.23
- SKPC.CA: score=19.31 buy_ready=False sector_rank=19 price=16.44 support=15.58 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=6830902.5 spike=0.21
- SMFR.CA: score=18.28 buy_ready=False sector_rank=9 price=204.36 support=187.01 resistance=209.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=376770.53 spike=0.2
- SNFC.CA: score=11.84 buy_ready=False sector_rank=9 price=11.83 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=940446.0 spike=0.08
- SPIN.CA: score=15.38 buy_ready=False sector_rank=8 price=14.62 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=2482425.75 spike=0.27
- SPMD.CA: score=19.77 buy_ready=True sector_rank=9 price=0.45 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=1874765.75 spike=0.11
- SUGR.CA: score=6.36 buy_ready=False sector_rank=15 price=46.95 support=45.31 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=1967998.5 spike=0.41
- SVCE.CA: score=23.14 buy_ready=True sector_rank=9 price=9.47 support=8.35 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=5236636.0 spike=0.07
- SWDY.CA: score=21.61 buy_ready=True sector_rank=2 price=88.33 support=84.3 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=1709904.0 spike=0.13
- TALM.CA: score=6.23 buy_ready=False sector_rank=16 price=15.49 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=30.07 liquidity=1020362.06 spike=0.09
- TMGH.CA: score=28.9 buy_ready=True sector_rank=3 price=97.09 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=43509808.0 spike=0.12
- TRTO.CA: score=14.86 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=751.23 spike=2.48
- UEFM.CA: score=18.77 buy_ready=False sector_rank=9 price=505.62 support=460.0 resistance=529.0 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=60.58 liquidity=871183.25 spike=0.59
- UEGC.CA: score=24.9 buy_ready=False sector_rank=9 price=1.91 support=1.33 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=80.3 liquidity=11245943.0 spike=0.49
- UNIP.CA: score=25.5 buy_ready=True sector_rank=9 price=0.34 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=5602393.0 spike=0.31
- UNIT.CA: score=17.73 buy_ready=False sector_rank=3 price=19.37 support=12.0 resistance=20.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=76.24 liquidity=3832789.75 spike=0.18
- WCDF.CA: score=14.07 buy_ready=False sector_rank=9 price=515.94 support=450.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-11T21:00:00+00:00 freshness=FRESH RSI=39.17 liquidity=767718.72 spike=2.2
- WKOL.CA: score=22.09 buy_ready=True sector_rank=9 price=323.98 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=4193993.0 spike=0.57
- ZEOT.CA: score=13.8 buy_ready=False sector_rank=9 price=11.96 support=11.22 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=95883032.0 spike=2.45
- ZMID.CA: score=28.9 buy_ready=True sector_rank=3 price=7.16 support=6.11 resistance=7.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=151282192.0 spike=0.69

## Backtesting Lite
- ELEC.CA: 180d return=-25.35%, max drawdown=-35.96%, MA20>MA50 days last20=0, as_of=2026-07-11T21:00:00+00:00
- AREH.CA: 180d return=48.7%, max drawdown=-37.58%, MA20>MA50 days last20=20, as_of=2026-07-11T21:00:00+00:00
- GDWA.CA: 180d return=-30.17%, max drawdown=-39.84%, MA20>MA50 days last20=13, as_of=2026-07-11T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ELEC.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=193 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt (ELEC.CA) has reported recent financial performance, including a decrease in revenue and earnings in 2025, and a net loss in the latest quarter of 2026. The company is listed on the Egyptian Exchange (EGX) and specializes in the manufacture and export of power and telecommunication cables and wires.
  - Electro Cable Egypt (EGX:ELEC) Stock Price & Overview (2025 Financial Performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXMYqZMqod6U4y4bQCSUogauA_lJFtZP92fUiWG20a1Jp7srsFFwiPhH16HnLu67I0C6M9bp2t1b7DO1AcaE0Ak1TyCqla6m1rs2VmKLOTEEpVHoVGjB10B3n2w3oXCEuRKAU
  - Electro Cable Egypt (EGX:ELEC) Financials & Income Statement - Stock Analysis (as of December 31, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFRN6ll1YGtOsQT5FBTCwm5aUG2wKd1kE0wzhE6TSNbVwnuc3zbWdrEe9i8ebt7QmLKt6uq0whtDY3p2y-Msl4VIEOX3rRpWKO3Y7J_tlsJV5jxSRIV2DrnkJuOL48oH7WN6ov_G0HVbvUC4gDpw==
  - EGX:ELEC Financials | Electro Cable - Investing.com (Latest Quarter Performance, July 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH17_6wiSfhEueGE7vRFNhU2da2FZCK6MsUMPDtBaT_Nqjo0xUJ3_atQ5G_jdzDSr46-mEWOUX_9QTSh82hVI6aXhDJeKkCid93PcpPMydHSHMV_45_cejS6BakphJZ5JQFbrdqF7OlXi6KlHXEJfXb-wxk6mFO65t25E-R
- AREH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25; Shareholder ups stake in Real Estate Egyptian; Target for Real Estate Investment cuts stake in Real Estate Egyptian Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25: https://english.mubasher.info/news/4528467/Real-Estate-Egyptian-Consortium-s-net-profits-approach-EGP-2m-in-9M-25/
  - Shareholder ups stake in Real Estate Egyptian: https://english.mubasher.info/news/4026301/Shareholder-ups-stake-in-Real-Estate-Egyptian/
  - Target for Real Estate Investment cuts stake in Real Estate Egyptian: https://english.mubasher.info/news/4010821/Target-for-Real-Estate-Investment-cuts-stake-in-Real-Estate-Egyptian/
- GDWA.CA: status=RECENT_ACCEPTED latest=2026-07-09 age_days=4 sources=3 expected=Gadwa for Industrial Development summary=Gadwa for Industrial Development (GDWA.CA) has released its consolidated financial results for Q1 2026, reporting revenues of approximately EGP 3.26 billion. The company also announced a net loss for Q1 2026 and a share nominal value split. Financial metrics for the last 12 months indicate significant revenue but also losses.
  - Gadwa for Industrial Development (EGX:GDWA) Statistics & Valuation Metrics (Last 12 months, July 9, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG90EZVcBsSz26eqv0Wzc2gtD8KBs6i5Bj40K8pxpDPsSGgHMPio-y0Dmeljqibt0pnvJERsPumZTnuenmCnkmBC3nTxQfI0b0i9ay7ekxwjWlIuoC6dz8pHzeqp0T28PjyaGNW21b7pt66NRoZMw==
  - GADWA for Industrial Development Announces its Consolidated Results for Q1 2026 (March 31, 2026, released June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFet5Yk7-765YdUmR26l3vMSy2dY32DzTPoXVsYSxezhp5g_cCTncQnMwpkYASaIOyoAxahQuEKt6TLjoEjFf93pw1wK5rEPqkaUgagzNCoVH7HMx3e2eYacJBYk2Q9heQyRNDr_Dgp7rhXddn4
  - Gadwa for Industrial Development (GDWA) - Mubasher Info (Q1 2026 Financial Results, June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW_B7rRUaPLKnV3Bapaadhy1FkW4gieG7fLiTOUxgcq0C4HKw2jC3DKudKG7RjsV4HbnzxVjmjoqDclVFo9hxfHjZPkPC7o1DckETMmVaotMSa-cRRql1oL_MaoPZuA478Yb-JfA4J3OgSgQWPV7ef
- RACC.CA: status=RECENT_ACCEPTED latest=2026-05-11 age_days=63 sources=3 expected=Raya Customer Experience summary=Raya Customer Experience (RACC.CA) has reported strong financial results for Q1 2026, with significant increases in revenues, gross profit, EBITDA, and net profit. The company also released its full-year 2025 results, showing growth in revenue and EBITDA. Raya Customer Experience operates in business process outsourcing (BPO) and contact center outsourcing (CCO) services.
  - Raya Customer Experience Reports Q1 2026 Results (May 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGavPzGng0kbQH9-K-SdAcVcyUlZh2pSGuBSD_me2Gt-D0UxY5eN8lYeOv-rvQoDDZFcdGdPhHNAK1c65ZI24bHVKRyn3S0v4MmTXpqDJnmamu8mo1RDkqcbS-6EblCg6cI41w2oW35eqhG40Fz
  - Raya Customer Experience (EGX:RACC) Revenue - Stock Analysis (as of March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBZ_J5jxndGZyhB5AFvZ_c1kaCFcQxpYzoNpGcZu8-aPIV3meGDtIOs8Y92EuSWGreCMxV7t0XJR4moeYy2cEwOC1e4_Rk-D4nSxsX7r4BA_NryUcLENtUprtasrliHP7LXhh9iALGHrPm6w==
  - Raya Customer Experience Reports FY2025 Results (March 4, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8IDYd3iKyjnGv0-K8IfidOyxlCB8xs7fxc6Xe99-mbuwxLh2Hw8rM7pWzcpI25ryY65fRHJ9qei4Xl5dTeVQJphXRDMx1UQUpABFD87O-Hfadm7FuCwKDVpjDTGWBDr3PRytYSgLPmmN3ET56
- RAYA.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=6 sources=3 expected=Raya Holding summary=Raya Holding (RAYA.CA) has shown strong financial performance in 2025, with increased revenue and earnings. Recent market announcements include Q1 2026 financial results, board decisions, and an MOU signing. The company is a diversified investment conglomerate listed on the EGX.
  - Raya Holding Company for Financial Investments (S.A.E) (EGX:RAYA) Statistics & Valuation Metrics (Last 12 months, July 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvkvVEo0QWn1O_vMC8keJaTVfpCqgEse_K7NN0cReAwcijCQDaKP3DhwXFtYVVDNRsvPCL6Z9qET8mfzLvQRluMqeHgDWjRVrwCWNehlmgx_yBpg5o17FzBFIiFG_wXCQExar58hGqBbQZqSlz5Q==
  - Raya Holding for Financial Investments SAE Price: Quote, Forecast, Charts & News (RAYA.CA) (2024 Financial Results): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtaDltuypU6R8O8P7dOwos3oLzUuWXF0-ipL1F_LFuCVDg9m1xMgEdGS6XSTrF-lJFaIch-Q1AcrILayimNOvr_ppppJPRGq88kTEMypI4aTQMo7e14O6QgpY3qImitsWQjsg=
  - EGX:RAYA Financials | Raya Hld - Investing.com (Latest Quarter Performance, May 28, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWkr1o80pUOSMxNMHOaNejOeVntOL2kwzaSrH5j9CiZJCX-b3Vxk4xnk67zexfyoAaO1_8GnMqK-7NNPs6YOBW2B6HLiBX0OJCq8UHwpYIa475Hb3IjGNEUoCy8mx19obQ_VdVV1kWmQ2aZEGgcvQ1uo2Z3XEbLhd691y2YQ==
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=6 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) has reported its Q1 2026 earnings, with revenue increasing by 14% from Q1 2025, despite a decrease in net income and profit margin. The company's revenue for the last 12 months reached EGP 110.17 billion, with profits of EGP 19.30 billion.
  - Telecom Egypt Company (EGX:ETEL) Statistics & Valuation Metrics (Last 12 months, July 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQaUEfGgTHv_kmwxr3rJ63TzqSQSVT8kXGxU6NVpgHauQWj5lex2DZfqMg5OYdcsG67islPlTU3rRBz9T5KbmdMuQQVVEkDmuVQfie2pBh1tFkUgrIMLEp7tYvJO9E6As5ufOvKUIfxKcs9WlOXg==
  - Telecom Egypt Company (EGX:ETEL) Financials & Income Statement - Stock Analysis (as of March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsfU8uJ0semuUOKd4wBQ9o5otMnoNFNpbtVaMCxhcjGdyilogShprAZojreNvyJU5iHTSdwVXrOGoe8Wvu5zEBZw8i7BNdxievtkW6zo2T6i__vaBsAg_EXgC7uq9QhkVWSVnYxBsnBh4wUTm_sg==
  - Telecom Egypt - EGX:ETEL Financials - Investing.com (Latest Quarter Performance, May 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeaLiez0QaLGoZdbxzBOmeYzvlxorerseCljNcZKmgeUZbZZ8WpdzVnw06FKfQvPARrl8DZlBG36gWtdTeL3wBBiMNAbFIvS-jpcgkwtCxooBzClk_RBIwPNVcym2VzNCpDfZiBr3lFIh7Q0WGgLZ89BC3DBgEHQe2LuRX
- ACGC.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=6 sources=3 expected=Arab Cotton Ginning summary=Arab Cotton Ginning (ACGC.CA) reported a decrease in revenue and earnings in fiscal year 2025. The company's latest quarter revenue was 705.155 million EGP. Arab Cotton Ginning specializes in the textiles industry, including ginning, pressing, spinning, weaving, knitting, and marketing of cotton.
  - Arabia Cotton Ginning Company (EGX:ACGC) Stock Price & Overview (Fiscal Year 2025 Financial Performance, July 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBfPJQsxQF_ZQ_76M6gk139o-tJaHnlC8kbQrNomXHqGl5R4FS1xOZbf-bC8AnoeDgv-N4d9j3zOMx-eD6XRkWHtGXbKmZ0cCqAN-z6zgr40aK5GY-REh7kyUJm2Hq2hGXbvs=
  - Arab Cotton Ginning - EGX:ACGC Financials - Investing.com (Latest Quarter Revenue, TTM Gross Margin): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPPYwaL-73UcyIr66ghplF4vSQ344PhiSJAoOsITv4fcgWmlIWarAyip4t0pKrZbyFkBjfUNGOnJgw3vRSOOumXxuZGhgZtFde75poSEYxRhHWwFcppH9UtRzYyAyuPuD4tZGf2Omz1v5eyWEY2Zh90At2dy1FoUUnhyzHDQ==
  - Arabia Cotton Ginning Company (EGX:ACGC) Financials & Income Statement - Stock Analysis (as of September 30, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv0l5PC2bVKDUInUcPcPuHInS4N-2F6VV8fCu4HcCzB7SM7FSYRxVWaXEuclsjgDszMuGO2pMKeYYD_YRE3lpZ9qzp_bZmTKbL4ChcZPONYbQv3RGj0-uOlJ-eeP_fpKhHXwBnV5VIfoQuuOBOeg==
- COSG.CA: status=RECENT_ACCEPTED latest=2026-07-01 age_days=12 sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oil & Soap Company (COSG.CA) reported revenue of EGP 802.09 million and losses of EGP 60.34 million in the last 12 months. The company's latest quarter performance shows an increase in revenue and a shift from net loss to net income. Cairo Oil & Soap Company manufactures and distributes edible oil, ghee, soap, and animal feed.
  - Cairo Oil & Soap Company (EGX:COSG) Statistics & Valuation Metrics - Stock Analysis (Last 12 months, July 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9EQ5ETdfPsFkOZDR1YMWPJVPgluHB3fIs3UbLBc33j_quy5jrL2rGz8diLEv7ue8CQZL1idJ28a593-8gwPAqXVVOd5uE9uT-DCRWqeJ6Qhk-xJrLYkYavc0zLe0s1P-XwBLln0pf6qGV33VMbw==
  - Cairo Oil & Soap Company (EGX:COSG) Balance Sheet - Stock Analysis (as of March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyLUepvP1oI7hBFwtx1L3DxAF7PNJmUn4_MKpFFuNs1wMCpFCHsq6WIJdyBy8huTgq7ZcJzM-dgIVVVVhWmI5FEEHjiEWjW3nxNiqVB_LzheNamXPBs9eucKzND60gg00JUFQE4AnW7rwY7Xmdhm320aVxW4a6BcrVgB9E
  - Cairo Oils & Soap - EGX:COSG Financials - Investing.com (Latest Quarter Performance, May 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEstAYFQf4PxiwcUXI1d9mpc7UIIgaVZi59w-gPJjpB7AcLRzWCQyAhClmvIn4gwdudqa7o9vYgpJ5T8J3Ejywv_PIkwH_U4LzEITZutc2GApf2n2BWPtdMbgRYq-tSkFU6Ir1hfr_3sRKoAd8CinkRckVIzlNwQRsNFUAUew==

## Warnings
- Evidence for AREH.CA matches the company but no source/report date was detected.
