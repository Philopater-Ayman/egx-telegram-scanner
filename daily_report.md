# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-28T10:35:04.186704+00:00
Generated Cairo: 2026-07-28 13:35
Run timing: target 11:00 Cairo | generated Cairo 2026-07-28 13:35 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-28 13:29

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 67
- Data quality issues: 1
- Tradeable price/liquidity tickers: 181/189
- Top sector: Textiles

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, July 28
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 60.0% / above MA50 50.0%
- EGX70 regime: BULLISH / above MA20 71.79% / above MA50 82.05%
- Sector breadth: 57.14%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- COMI.CA: liquidity=393225888.0 spike=0.95 score=30.9
- CCAP.CA: liquidity=290855680.0 spike=0.42 score=25.76
- BTFH.CA: liquidity=279171008.0 spike=1.34 score=28.17
- BIOC.CA: liquidity=223585968.0 spike=6.21 score=15.9
- ZMID.CA: liquidity=176528336.0 spike=0.71 score=27.9

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner prioritized NCCW.CA, AJWA.CA, and COMI.CA as BUY setups under a BROAD_RISK_ON regime, citing price above MA20/MA50, adequate liquidity spikes, bullish watch outlooks, and supportive sector breadth.
- NCCW.CA: price above MA20/MA50, RSI 66.9, liquidity accumulation spike, but momentum extended and far above support, limiting near‑term upside.

## Top Liquidity Spikes
- SDTI.CA: spike=12.03 liquidity=94240184.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPMD.CA: spike=7.48 liquidity=135795712.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BIOC.CA: spike=6.21 liquidity=223585968.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NCCW.CA: spike=4.36 liquidity=96004096.0 outlook=BULLISH_WATCH score=85.46 buy_ready=True
- AFMC.CA: spike=4.14 liquidity=158635792.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=13.53 5d=8.21% 20d=15.77% aboveMA50=100.0%
- #2 Building Materials: score=10.59 5d=2.99% 20d=16.21% aboveMA50=83.33%
- #3 Banking & Financials: score=8.46 5d=4.54% 20d=4.08% aboveMA50=80.0%
- #4 General / Verified EGX Expansion: score=8.46 5d=1.28% 20d=11.36% aboveMA50=80.58%
- #5 Industrial Goods & Cables: score=8.35 5d=0.67% 20d=7.76% aboveMA50=100.0%
- #6 Telecommunications: score=8.2 5d=1.88% 20d=6.23% aboveMA50=100.0%
- #7 Healthcare: score=8.06 5d=1.75% 20d=6.08% aboveMA50=83.33%
- #8 Education: score=7.94 5d=0.13% 20d=0.0% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- Priority #1: BUY NCCW.CA
  - Entry: 7.09 | Take profit: 7.65 | Stop loss: 6.81
  - Confidence: LOW | score=32.9 | outlook=BULLISH_WATCH 85.46
  - Reason: WATCH/BUY SETUP: NCCW.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 66.87, support 5.82, resistance 6.91, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY AJWA.CA
  - Entry: 187.0 | Take profit: 208.95 | Stop loss: 179.52
  - Confidence: LOW | score=32.78 | outlook=BULLISH_WATCH 100
  - Reason: BUY SETUP: AJWA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 56.97, support 161.0, resistance 210.0, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY COMI.CA
  - Entry: 141.75 | Take profit: 153.09 | Stop loss: 136.08
  - Confidence: LOW | score=30.9 | outlook=BULLISH_WATCH 95.46
  - Reason: BUY SETUP: COMI.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 61.34, support 126.21, resistance 141.4, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- AJWA.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- COMI.CA: BULLISH_WATCH score=95.46 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- PHAR.CA: BULLISH_WATCH score=95.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- SPIN.CA: BULLISH_WATCH score=93 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- ARCC.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PRCL.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- RACC.CA: BULLISH_WATCH score=89.46 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- RTVC.CA: BULLISH_WATCH score=89.46 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- RMDA.CA: BULLISH_WATCH score=89.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; close to resistance

## BUY-Ready Candidates
- NCCW.CA: rank=32.9 outlook=BULLISH_WATCH outlook_score=85.46 sector_rank=4 price=7.09 support=5.82 resistance=6.91 liquidity=96004096.0
- AJWA.CA: rank=32.78 outlook=BULLISH_WATCH outlook_score=100 sector_rank=4 price=187.0 support=161.0 resistance=210.0 liquidity=72383096.0
- TALM.CA: rank=31.08 outlook=BULLISH_WATCH outlook_score=83.94 sector_rank=8 price=16.18 support=15.27 resistance=16.42 liquidity=36955292.0
- COMI.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=95.46 sector_rank=3 price=141.75 support=126.21 resistance=141.4 liquidity=393225888.0
- ARCC.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=90 sector_rank=2 price=56.69 support=53.5 resistance=58.5 liquidity=14655501.0
- ORHD.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=66.64 sector_rank=9 price=40.24 support=37.0 resistance=40.8 liquidity=97599104.0
- AALR.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=68.46 sector_rank=4 price=245.0 support=196.0 resistance=255.0 liquidity=14751508.0
- ORWE.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=90 sector_rank=1 price=23.01 support=21.95 resistance=23.47 liquidity=8504377.0
- RMDA.CA: rank=29.04 outlook=BULLISH_WATCH outlook_score=89.06 sector_rank=7 price=5.2 support=4.81 resistance=5.3 liquidity=38815108.0
- PHAR.CA: rank=28.94 outlook=BULLISH_WATCH outlook_score=95.06 sector_rank=7 price=93.43 support=83.6 resistance=97.9 liquidity=68409816.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=29.9 buy_ready=True sector_rank=4 price=245.0 support=196.0 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=14751508.0 spike=0.74
- ABUK.CA: score=24.0 buy_ready=False sector_rank=16 price=71.89 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=52278164.0 spike=0.34
- ACAMD.CA: score=27.9 buy_ready=True sector_rank=4 price=2.37 support=2.14 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=27008264.0 spike=0.36
- ACGC.CA: score=28.9 buy_ready=False sector_rank=1 price=10.64 support=8.92 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=71.54 liquidity=18694658.0 spike=0.63
- ADCI.CA: score=20.51 buy_ready=False sector_rank=4 price=260.03 support=230.0 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=74.42 liquidity=2613977.75 spike=0.23
- ADIB.CA: score=28.9 buy_ready=True sector_rank=3 price=52.54 support=44.1 resistance=51.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=69.81 liquidity=85244056.0 spike=0.68
- ADPC.CA: score=24.9 buy_ready=False sector_rank=4 price=4.05 support=3.32 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=24552582.0 spike=0.78
- AFDI.CA: score=28.1 buy_ready=False sector_rank=4 price=50.39 support=41.84 resistance=51.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=73.11 liquidity=17511170.0 spike=1.1
- AFMC.CA: score=15.9 buy_ready=False sector_rank=4 price=133.53 support=127.12 resistance=144.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=158635792.0 spike=4.14
- AJWA.CA: score=32.78 buy_ready=True sector_rank=4 price=187.0 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=56.97 liquidity=72383096.0 spike=3.44
- ALCN.CA: score=26.85 buy_ready=True sector_rank=15 price=29.19 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=58.2 liquidity=9429398.0 spike=0.42
- ALUM.CA: score=16.71 buy_ready=True sector_rank=4 price=23.4 support=20.55 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=62.75 liquidity=1810905.0 spike=0.28
- AMER.CA: score=24.9 buy_ready=False sector_rank=9 price=4.5 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=90.87 liquidity=36582396.0 spike=0.34
- AMES.CA: score=25.9 buy_ready=False sector_rank=4 price=126.24 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=71.6 liquidity=33128374.0 spike=0.31
- AMIA.CA: score=23.28 buy_ready=True sector_rank=4 price=10.59 support=8.42 resistance=10.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=68.7 liquidity=7381007.0 spike=0.56
- AMOC.CA: score=25.9 buy_ready=True sector_rank=10 price=8.24 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=66.46 liquidity=22761004.0 spike=0.38
- APSW.CA: score=16.58 buy_ready=False sector_rank=4 price=9.0 support=8.0 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=65.84 liquidity=675654.75 spike=0.41
- ARAB.CA: score=27.9 buy_ready=True sector_rank=9 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=61.73 liquidity=85933952.0 spike=0.65
- ARCC.CA: score=29.9 buy_ready=True sector_rank=2 price=56.69 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=52.99 liquidity=14655501.0 spike=0.57
- AREH.CA: score=20.9 buy_ready=False sector_rank=4 price=1.47 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=10099812.0 spike=0.32
- ARVA.CA: score=27.56 buy_ready=False sector_rank=4 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-26T21:00:00+00:00 freshness=FRESH RSI=72.58 liquidity=47243679.11 spike=1.83
- ASCM.CA: score=27.42 buy_ready=True sector_rank=4 price=63.9 support=56.29 resistance=64.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=68.48 liquidity=90723704.0 spike=1.76
- ASPI.CA: score=24.98 buy_ready=False sector_rank=4 price=0.45 support=0.3 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=90.36 liquidity=36208148.0 spike=1.04
- ATLC.CA: score=16.44 buy_ready=False sector_rank=14 price=5.18 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=42.65 liquidity=2944768.25 spike=0.44
- ATQA.CA: score=28.4 buy_ready=True sector_rank=16 price=10.1 support=9.35 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=60.91 liquidity=55380072.0 spike=1.7
- AXPH.CA: score=17.2 buy_ready=True sector_rank=4 price=1222.93 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=62.41 liquidity=1296338.88 spike=0.33
- BINV.CA: score=16.76 buy_ready=False sector_rank=13 price=47.29 support=44.98 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=38.23 liquidity=2999090.5 spike=0.41
- BIOC.CA: score=15.9 buy_ready=False sector_rank=4 price=165.15 support=142.5 resistance=171.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=223585968.0 spike=6.21
- BTFH.CA: score=28.17 buy_ready=True sector_rank=14 price=3.12 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=279171008.0 spike=1.34
- CAED.CA: score=24.9 buy_ready=False sector_rank=4 price=128.62 support=69.01 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=81.41 liquidity=37706484.0 spike=0.6
- CANA.CA: score=28.9 buy_ready=True sector_rank=3 price=38.49 support=34.7 resistance=38.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=65.53 liquidity=11532319.0 spike=0.7
- CCAP.CA: score=25.76 buy_ready=True sector_rank=13 price=5.33 support=4.65 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=65.66 liquidity=290855680.0 spike=0.42
- CCRS.CA: score=23.92 buy_ready=True sector_rank=4 price=2.59 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=66.22 liquidity=8018482.0 spike=0.46
- CEFM.CA: score=28.24 buy_ready=True sector_rank=4 price=131.04 support=95.75 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=68.36 liquidity=35569668.0 spike=2.17
- CERA.CA: score=21.36 buy_ready=True sector_rank=4 price=1.33 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=5460610.0 spike=0.23
- CFGH.CA: score=16.91 buy_ready=False sector_rank=4 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=10067.32 spike=0.64
- CICH.CA: score=20.37 buy_ready=True sector_rank=14 price=12.17 support=11.52 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=51.88 liquidity=2874193.0 spike=0.54
- CIEB.CA: score=23.5 buy_ready=False sector_rank=3 price=23.97 support=23.3 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=8582745.0 spike=1.01
- CIRA.CA: score=15.9 buy_ready=False sector_rank=8 price=36.0 support=33.56 resistance=36.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=149073840.0 spike=3.6
- CLHO.CA: score=25.9 buy_ready=True sector_rank=7 price=16.76 support=15.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=55.93 liquidity=10494439.0 spike=0.24
- CNFN.CA: score=19.8 buy_ready=True sector_rank=14 price=4.87 support=4.61 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=4303090.0 spike=0.22
- COMI.CA: score=30.9 buy_ready=True sector_rank=3 price=141.75 support=126.21 resistance=141.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=61.34 liquidity=393225888.0 spike=0.95
- COPR.CA: score=21.9 buy_ready=False sector_rank=4 price=0.41 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=78.49 liquidity=15622314.0 spike=0.54
- COSG.CA: score=25.9 buy_ready=False sector_rank=4 price=1.7 support=1.47 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=70.83 liquidity=28406256.0 spike=0.66
- CPCI.CA: score=18.32 buy_ready=False sector_rank=4 price=469.19 support=370.01 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=74.02 liquidity=2422147.25 spike=0.21
- CSAG.CA: score=17.97 buy_ready=False sector_rank=15 price=32.51 support=31.57 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=46.61 liquidity=4553501.0 spike=0.23
- DAPH.CA: score=24.9 buy_ready=False sector_rank=4 price=95.93 support=78.52 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=75.75 liquidity=11608754.0 spike=0.72
- DEIN.CA: score=0.9 buy_ready=False sector_rank=4 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=13.42 buy_ready=False sector_rank=18 price=26.8 support=26.06 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=44.4 liquidity=1012157.88 spike=0.3
- DSCW.CA: score=22.9 buy_ready=False sector_rank=4 price=1.95 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=83.33 liquidity=41604136.0 spike=0.81
- DTPP.CA: score=28.44 buy_ready=True sector_rank=4 price=248.85 support=114.67 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=64.22 liquidity=91301384.0 spike=1.27
- EALR.CA: score=24.17 buy_ready=True sector_rank=4 price=371.03 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=6270348.5 spike=0.34
- EASB.CA: score=18.78 buy_ready=True sector_rank=4 price=7.8 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=60.48 liquidity=2884520.75 spike=0.2
- EAST.CA: score=20.41 buy_ready=False sector_rank=18 price=36.29 support=36.11 resistance=38.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=36.77 liquidity=17401680.0 spike=0.28
- EBSC.CA: score=14.74 buy_ready=False sector_rank=4 price=1.92 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=24.24 liquidity=3844715.75 spike=0.48
- ECAP.CA: score=20.57 buy_ready=True sector_rank=4 price=33.67 support=31.52 resistance=34.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=57.92 liquidity=2672748.75 spike=0.42
- EDFM.CA: score=18.49 buy_ready=False sector_rank=4 price=380.0 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=73.2 liquidity=2588844.75 spike=0.61
- EEII.CA: score=19.9 buy_ready=True sector_rank=4 price=2.75 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=56.45 liquidity=4004467.0 spike=0.18
- EFIC.CA: score=17.23 buy_ready=False sector_rank=16 price=187.3 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=51.76 liquidity=4238315.5 spike=0.38
- EFID.CA: score=17.61 buy_ready=False sector_rank=18 price=27.18 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=30.46 liquidity=106729624.0 spike=2.6
- EFIH.CA: score=27.9 buy_ready=True sector_rank=11 price=22.85 support=20.0 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=25226314.0 spike=0.42
- EGAL.CA: score=24.0 buy_ready=False sector_rank=16 price=297.59 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=50.86 liquidity=12584339.0 spike=0.29
- EGAS.CA: score=20.51 buy_ready=True sector_rank=10 price=53.58 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=69.8 liquidity=2607470.0 spike=0.21
- EGBE.CA: score=16.45 buy_ready=False sector_rank=3 price=0.48 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=97.88 liquidity=47921.51 spike=1.25
- EGCH.CA: score=24.0 buy_ready=False sector_rank=16 price=13.02 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=37651004.0 spike=0.63
- EGSA.CA: score=14.1 buy_ready=False sector_rank=6 price=8.89 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=60.81 liquidity=19561.19 spike=1.09
- EGTS.CA: score=20.9 buy_ready=False sector_rank=9 price=17.94 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=42.52 liquidity=36897716.0 spike=0.8
- EHDR.CA: score=25.9 buy_ready=True sector_rank=4 price=2.91 support=2.37 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=68.54 liquidity=24587580.0 spike=0.61
- EKHO.CA: score=9.9 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=26.9 buy_ready=True sector_rank=5 price=2.2 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=25788212.0 spike=0.38
- ELKA.CA: score=25.9 buy_ready=False sector_rank=4 price=1.93 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=73.53 liquidity=29657694.0 spike=0.41
- ELNA.CA: score=18.26 buy_ready=False sector_rank=4 price=38.99 support=35.55 resistance=40.5 source=Yahoo Finance as_of=2026-07-26T21:00:00+00:00 freshness=FRESH RSI=56.63 liquidity=355315.89 spike=0.58
- ELSH.CA: score=23.9 buy_ready=True sector_rank=4 price=14.8 support=11.1 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=65.83 liquidity=59778768.0 spike=0.43
- ELWA.CA: score=14.67 buy_ready=False sector_rank=4 price=1.85 support=1.87 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=2091893.63 spike=1.84
- EMFD.CA: score=23.9 buy_ready=False sector_rank=9 price=11.61 support=11.24 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=14002283.0 spike=0.23
- ENGC.CA: score=25.9 buy_ready=False sector_rank=4 price=42.71 support=35.26 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=72.08 liquidity=15430063.0 spike=0.59
- EOSB.CA: score=15.92 buy_ready=False sector_rank=4 price=1.48 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=16879.4 spike=0.41
- EPCO.CA: score=20.33 buy_ready=False sector_rank=4 price=11.1 support=8.5 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=84.96 liquidity=7433901.5 spike=0.26
- EPPK.CA: score=18.59 buy_ready=False sector_rank=4 price=15.14 support=12.7 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=686047.19 spike=0.52
- ETEL.CA: score=26.26 buy_ready=False sector_rank=6 price=105.49 support=89.01 resistance=106.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=73.06 liquidity=92343056.0 spike=1.18
- ETRS.CA: score=23.9 buy_ready=False sector_rank=4 price=10.67 support=10.33 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=39782912.0 spike=0.78
- EXPA.CA: score=23.9 buy_ready=False sector_rank=3 price=19.92 support=18.03 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=75.74 liquidity=18956250.0 spike=0.64
- FAIT.CA: score=19.39 buy_ready=False sector_rank=3 price=37.12 support=35.06 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=55.58 liquidity=491792.66 spike=0.17
- FAITA.CA: score=11.91 buy_ready=False sector_rank=3 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=38.57 liquidity=12148.12 spike=0.26
- FERC.CA: score=20.8 buy_ready=True sector_rank=16 price=77.74 support=72.75 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=4806456.5 spike=0.41
- FWRY.CA: score=24.9 buy_ready=False sector_rank=11 price=19.14 support=18.13 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=43.04 liquidity=23149412.0 spike=0.17
- GBCO.CA: score=22.97 buy_ready=False sector_rank=17 price=30.6 support=29.5 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=44.03 liquidity=15460959.0 spike=0.21
- GDWA.CA: score=21.9 buy_ready=False sector_rank=4 price=0.85 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=80.54 liquidity=65626116.0 spike=0.75
- GGCC.CA: score=22.9 buy_ready=False sector_rank=4 price=0.87 support=0.44 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=87.27 liquidity=23744654.0 spike=0.61
- GIHD.CA: score=24.9 buy_ready=False sector_rank=4 price=61.33 support=40.66 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=75.55 liquidity=32936826.0 spike=0.67
- GMCI.CA: score=16.43 buy_ready=False sector_rank=4 price=2.06 support=1.67 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=534953.75 spike=0.4
- GRCA.CA: score=25.9 buy_ready=True sector_rank=4 price=62.4 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=68.66 liquidity=12338653.0 spike=0.8
- GSSC.CA: score=18.01 buy_ready=True sector_rank=4 price=267.36 support=240.52 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=67.62 liquidity=2112023.25 spike=0.21
- GTWL.CA: score=25.9 buy_ready=True sector_rank=4 price=102.8 support=60.0 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=63.51 liquidity=21301530.0 spike=0.15
- HDBK.CA: score=24.9 buy_ready=False sector_rank=3 price=81.58 support=75.3 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=50.69 liquidity=13033566.0 spike=0.42
- HELI.CA: score=22.9 buy_ready=False sector_rank=9 price=8.3 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=89.23 liquidity=131665880.0 spike=0.73
- HRHO.CA: score=21.49 buy_ready=False sector_rank=14 price=26.54 support=26.09 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=44.35 liquidity=37924484.0 spike=0.44
- ICID.CA: score=14.33 buy_ready=False sector_rank=4 price=8.05 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=53.09 liquidity=427654.5 spike=0.06
- IDRE.CA: score=27.9 buy_ready=True sector_rank=4 price=48.52 support=41.1 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=67.42 liquidity=15190231.0 spike=0.59
- IFAP.CA: score=23.79 buy_ready=True sector_rank=12 price=19.71 support=18.47 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=53.71 liquidity=5890284.5 spike=0.65
- INFI.CA: score=26.06 buy_ready=False sector_rank=4 price=107.25 support=88.51 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=75.42 liquidity=24109636.0 spike=1.58
- IRON.CA: score=6.92 buy_ready=False sector_rank=16 price=30.8 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=30.9 liquidity=2921241.25 spike=0.43
- ISMA.CA: score=24.9 buy_ready=False sector_rank=4 price=31.47 support=26.54 resistance=32.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=76.17 liquidity=13631799.0 spike=0.55
- ISMQ.CA: score=20.0 buy_ready=False sector_rank=16 price=9.5 support=8.6 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=34.52 liquidity=83745456.0 spike=0.82
- ISPH.CA: score=24.9 buy_ready=False sector_rank=7 price=11.56 support=11.2 resistance=12.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=23584236.0 spike=0.45
- JUFO.CA: score=20.21 buy_ready=False sector_rank=18 price=28.8 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=39.1 liquidity=33961344.0 spike=1.4
- KABO.CA: score=25.9 buy_ready=False sector_rank=1 price=8.28 support=6.04 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=86.43 liquidity=38891432.0 spike=0.83
- KWIN.CA: score=14.86 buy_ready=False sector_rank=4 price=105.72 support=96.3 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=131036248.0 spike=2.98
- KZPC.CA: score=14.31 buy_ready=False sector_rank=4 price=8.56 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=2408418.0 spike=0.48
- LCSW.CA: score=25.6 buy_ready=False sector_rank=2 price=35.02 support=27.01 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=79.64 liquidity=8699851.0 spike=0.11
- LUTS.CA: score=12.8 buy_ready=False sector_rank=4 price=0.58 support=0.58 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=19.01 liquidity=7897286.0 spike=0.23
- MAAL.CA: score=17.01 buy_ready=False sector_rank=4 price=8.72 support=6.92 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=82.04 liquidity=4109203.75 spike=0.23
- MASR.CA: score=25.9 buy_ready=True sector_rank=4 price=8.07 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=58.55 liquidity=50410980.0 spike=0.58
- MBSC.CA: score=22.51 buy_ready=False sector_rank=2 price=245.22 support=222.66 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=49.03 liquidity=5609231.0 spike=0.29
- MCQE.CA: score=25.29 buy_ready=True sector_rank=2 price=186.97 support=167.02 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=64.09 liquidity=5385203.0 spike=0.3
- MCRO.CA: score=21.9 buy_ready=False sector_rank=4 price=1.46 support=1.17 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=76.19 liquidity=66102004.0 spike=0.58
- MENA.CA: score=14.91 buy_ready=False sector_rank=9 price=7.18 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=28.18 liquidity=4012461.0 spike=0.52
- MEPA.CA: score=22.9 buy_ready=False sector_rank=4 price=1.87 support=1.52 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=75.44 liquidity=30864824.0 spike=0.68
- MFPC.CA: score=22.0 buy_ready=False sector_rank=16 price=36.62 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=19400056.0 spike=0.21
- MFSC.CA: score=12.67 buy_ready=False sector_rank=4 price=46.52 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=39.45 liquidity=1770738.75 spike=0.29
- MHOT.CA: score=8.41 buy_ready=False sector_rank=21 price=16.71 support=16.12 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=32.41 liquidity=5512117.5 spike=0.5
- MICH.CA: score=22.93 buy_ready=False sector_rank=4 price=40.3 support=34.0 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=73.41 liquidity=7030437.0 spike=0.44
- MILS.CA: score=25.92 buy_ready=False sector_rank=4 price=173.56 support=126.31 resistance=197.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=70.88 liquidity=36994232.0 spike=1.01
- MIPH.CA: score=16.37 buy_ready=False sector_rank=7 price=741.94 support=630.13 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=68.19 liquidity=467176.22 spike=0.14
- MOED.CA: score=21.9 buy_ready=False sector_rank=4 price=0.7 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=18418086.0 spike=0.89
- MOIL.CA: score=15.37 buy_ready=False sector_rank=10 price=0.66 support=0.46 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=88.76 liquidity=466295.03 spike=0.76
- MOIN.CA: score=11.9 buy_ready=False sector_rank=4 price=23.6 support=22.6 resistance=24.76 source=Yahoo Finance as_of=2026-07-26T21:00:00+00:00 freshness=FRESH RSI=44.51 liquidity=2478.0 spike=0.0
- MOSC.CA: score=27.9 buy_ready=True sector_rank=4 price=288.63 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=61.77 liquidity=10578475.0 spike=0.86
- MPCI.CA: score=24.9 buy_ready=False sector_rank=4 price=292.89 support=222.55 resistance=289.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=80.49 liquidity=94546608.0 spike=1.0
- MPCO.CA: score=23.9 buy_ready=False sector_rank=12 price=1.85 support=1.7 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=22441646.0 spike=0.42
- MPRC.CA: score=23.9 buy_ready=False sector_rank=4 price=44.4 support=37.15 resistance=45.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=74.29 liquidity=11301088.0 spike=0.33
- MTIE.CA: score=24.97 buy_ready=True sector_rank=17 price=9.38 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=43.15 liquidity=18078466.0 spike=0.84
- NAHO.CA: score=4.91 buy_ready=False sector_rank=4 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-26T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=9491.58 spike=0.29
- NCCW.CA: score=32.9 buy_ready=True sector_rank=4 price=7.09 support=5.82 resistance=6.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=66.87 liquidity=96004096.0 spike=4.36
- NEDA.CA: score=13.04 buy_ready=False sector_rank=4 price=2.75 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1100030.25 spike=1.52
- NHPS.CA: score=25.9 buy_ready=False sector_rank=4 price=87.92 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=70.99 liquidity=35220348.0 spike=0.42
- NINH.CA: score=25.14 buy_ready=False sector_rank=4 price=22.28 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=73.94 liquidity=9239559.0 spike=0.22
- NIPH.CA: score=22.9 buy_ready=False sector_rank=7 price=228.64 support=157.01 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=80.62 liquidity=61788208.0 spike=0.41
- OBRI.CA: score=15.9 buy_ready=False sector_rank=4 price=34.56 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=20275606.0 spike=0.51
- OCDI.CA: score=26.1 buy_ready=True sector_rank=9 price=28.0 support=23.75 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=56.11 liquidity=101847000.0 spike=1.1
- OCPH.CA: score=24.36 buy_ready=False sector_rank=4 price=484.37 support=341.4 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=92.83 liquidity=9463787.0 spike=0.39
- ODIN.CA: score=22.63 buy_ready=False sector_rank=4 price=2.59 support=2.05 resistance=2.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=74.6 liquidity=4729470.5 spike=0.29
- OFH.CA: score=23.92 buy_ready=False sector_rank=4 price=0.73 support=0.57 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=78.62 liquidity=91582976.0 spike=1.51
- OIH.CA: score=27.76 buy_ready=False sector_rank=13 price=1.49 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=21706516.0 spike=0.31
- OLFI.CA: score=22.06 buy_ready=True sector_rank=18 price=23.23 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=66.12 liquidity=5647000.0 spike=0.16
- ORAS.CA: score=9.1 buy_ready=False sector_rank=19 price=713.03 support=708.5 resistance=714.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=155809664.0 spike=1.0
- ORHD.CA: score=29.9 buy_ready=True sector_rank=9 price=40.24 support=37.0 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=62.04 liquidity=97599104.0 spike=0.63
- ORWE.CA: score=29.4 buy_ready=True sector_rank=1 price=23.01 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=49.59 liquidity=8504377.0 spike=0.35
- PHAR.CA: score=28.94 buy_ready=True sector_rank=7 price=93.43 support=83.6 resistance=97.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=68.9 liquidity=68409816.0 spike=1.52
- PHDC.CA: score=20.9 buy_ready=False sector_rank=9 price=14.68 support=14.26 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=47.72 liquidity=111109048.0 spike=0.46
- PHTV.CA: score=18.19 buy_ready=False sector_rank=4 price=320.29 support=250.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=82.67 liquidity=3286230.75 spike=0.57
- POUL.CA: score=22.41 buy_ready=False sector_rank=18 price=38.03 support=36.52 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=14307529.0 spike=0.42
- PRCL.CA: score=27.9 buy_ready=True sector_rank=2 price=35.35 support=30.21 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=59.75 liquidity=31207920.0 spike=0.64
- PRDC.CA: score=25.9 buy_ready=True sector_rank=9 price=9.18 support=6.8 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=13239248.0 spike=0.11
- PRMH.CA: score=21.62 buy_ready=True sector_rank=4 price=2.67 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=58.49 liquidity=5720059.0 spike=0.33
- RACC.CA: score=26.0 buy_ready=True sector_rank=4 price=10.16 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=21715806.0 spike=1.05
- RAKT.CA: score=14.07 buy_ready=False sector_rank=4 price=22.64 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-26T21:00:00+00:00 freshness=FRESH RSI=48.1 liquidity=172426.24 spike=0.59
- RAYA.CA: score=13.61 buy_ready=False sector_rank=20 price=7.46 support=7.01 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=34.02 liquidity=81456208.0 spike=0.61
- RMDA.CA: score=29.04 buy_ready=True sector_rank=7 price=5.2 support=4.81 resistance=5.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=38815108.0 spike=1.57
- ROTO.CA: score=27.9 buy_ready=True sector_rank=4 price=44.51 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=57.92 liquidity=11751085.0 spike=0.57
- RREI.CA: score=27.32 buy_ready=False sector_rank=4 price=4.45 support=3.34 resistance=4.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=83.19 liquidity=83614016.0 spike=2.21
- RTVC.CA: score=21.64 buy_ready=True sector_rank=4 price=3.96 support=3.55 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=3737762.5 spike=0.9
- RUBX.CA: score=25.9 buy_ready=True sector_rank=4 price=13.12 support=10.55 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=11257207.0 spike=0.15
- SAUD.CA: score=25.26 buy_ready=True sector_rank=3 price=22.33 support=19.99 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=66.56 liquidity=8362199.0 spike=0.91
- SCEM.CA: score=26.3 buy_ready=False sector_rank=2 price=85.0 support=60.14 resistance=85.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=84.91 liquidity=99917416.0 spike=1.7
- SCFM.CA: score=25.9 buy_ready=True sector_rank=4 price=281.89 support=230.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=65.88 liquidity=19380974.0 spike=0.94
- SCTS.CA: score=19.67 buy_ready=True sector_rank=8 price=615.18 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=49.7 liquidity=1766126.38 spike=0.26
- SDTI.CA: score=15.9 buy_ready=False sector_rank=4 price=56.0 support=52.36 resistance=58.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=94240184.0 spike=12.03
- SEIG.CA: score=16.8 buy_ready=False sector_rank=4 price=245.94 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=71.21 liquidity=2898895.5 spike=0.12
- SIPC.CA: score=29.86 buy_ready=False sector_rank=4 price=4.07 support=3.25 resistance=4.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=84.21 liquidity=67456704.0 spike=3.48
- SKPC.CA: score=21.0 buy_ready=False sector_rank=16 price=15.97 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=48.4 liquidity=11139441.0 spike=0.31
- SMFR.CA: score=23.59 buy_ready=True sector_rank=4 price=231.98 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=66.06 liquidity=7687133.0 spike=0.38
- SNFC.CA: score=18.19 buy_ready=False sector_rank=4 price=11.16 support=11.04 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=7286816.0 spike=0.66
- SPIN.CA: score=29.82 buy_ready=False sector_rank=1 price=16.06 support=13.93 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=92.76 liquidity=42613688.0 spike=1.96
- SPMD.CA: score=15.9 buy_ready=False sector_rank=4 price=0.48 support=0.45 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=135795712.0 spike=7.48
- SUGR.CA: score=14.82 buy_ready=False sector_rank=18 price=46.91 support=45.31 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=43.61 liquidity=4406670.5 spike=0.8
- SVCE.CA: score=23.9 buy_ready=False sector_rank=4 price=9.26 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=35.58 liquidity=18031470.0 spike=0.33
- SWDY.CA: score=19.75 buy_ready=False sector_rank=5 price=95.25 support=84.3 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=76.01 liquidity=6847839.5 spike=0.33
- TALM.CA: score=31.08 buy_ready=True sector_rank=8 price=16.18 support=15.27 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=51.27 liquidity=36955292.0 spike=2.59
- TMGH.CA: score=27.9 buy_ready=True sector_rank=9 price=99.9 support=92.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=55.52 liquidity=175334880.0 spike=0.49
- TRTO.CA: score=12.18 buy_ready=False sector_rank=4 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1311.11 spike=1.14
- UEFM.CA: score=18.89 buy_ready=False sector_rank=4 price=543.1 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=63.81 liquidity=986183.5 spike=0.23
- UEGC.CA: score=24.9 buy_ready=False sector_rank=4 price=2.47 support=1.33 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=90.43 liquidity=38914244.0 spike=0.81
- UNIP.CA: score=22.9 buy_ready=False sector_rank=4 price=0.4 support=0.3 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=81.16 liquidity=13356399.0 spike=0.55
- UNIT.CA: score=24.09 buy_ready=True sector_rank=9 price=18.14 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=60.04 liquidity=8187828.5 spike=0.28
- WCDF.CA: score=22.97 buy_ready=True sector_rank=4 price=577.87 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=65.37 liquidity=4768177.5 spike=2.15
- WKOL.CA: score=24.01 buy_ready=True sector_rank=4 price=313.48 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=6114718.5 spike=0.61
- ZEOT.CA: score=25.54 buy_ready=True sector_rank=4 price=11.99 support=10.4 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=66.84 liquidity=57104756.0 spike=1.82
- ZMID.CA: score=27.9 buy_ready=False sector_rank=9 price=7.6 support=6.19 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=73.1 liquidity=176528336.0 spike=0.71

## Backtesting Lite
- NCCW.CA: 180d return=7.0%, max drawdown=-34.18%, MA20>MA50 days last20=20, as_of=2026-07-26T21:00:00+00:00
- AJWA.CA: 180d return=41.66%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-07-26T21:00:00+00:00
- TALM.CA: 180d return=-2.83%, max drawdown=-12.21%, MA20>MA50 days last20=9, as_of=2026-07-26T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- NCCW.CA: status=RECENT_ACCEPTED latest=2026-07-22 age_days=6 sources=3 expected=Nasr Company for Civil Works summary=Recent evidence for Nasr Company for Civil Works (NCCW.CA) on the Egyptian Exchange (EGX) includes announcements regarding stock dividends, board and shareholder structure disclosures, and minutes from general assembly meetings, all within the last 12 months. The company also reported its First Quarter 2026 financial metrics.
  - Nasr Company for Civil Works (NCCW.CA) Declares a Stock Dividends - The Egyptian Exchange (July 22, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfOnyE8Jfq1IeiexjciATXetM-kwicLQehoes7z60CEoO35gsguONAduMhovBI95Zs3bSfEn0mO_enyFOrKdeiZRGYox4OfqigPpRRE4Op6NAw2swkf5eRqjDUid1IbdDaBDu53kF9IJ_-G191uA==
  - Release from Nasr Company for Civil Works (NCCW.CA) Concerning Stock Dividends (July 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVwxsqokwQC4KOsb2Be_yG6E87J5XjSpjM4Jb8cTONUbOTEiq2iLlNIGltJ4T_p6meXdFTEvayrz-yoQOmbHqHsxVghb_MY5dCA3K6UJW3bhl5MvA2pJWPlSzmzi7r4v3OWjYXEOPmKze_LXa0FGZx
  - Nasr Company for Civil Works (NCCW.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVwxsqokwQC4KOsb2Be_yG6E87J5XjSpjM4Jb8cTONUbOTEiq2iLlNIGltJ4T_p6meXdFTEvayrz-yoQOmbHqHsxVghb_MY5dCA3K6UJW3bhl5MvA2pJWPlSzmzi7r4v3OWjYXEOPmKze_LXa0FGZx
- AJWA.CA: status=RECENT_ACCEPTED latest=2026-07-20 age_days=8 sources=3 expected=AJWA For Food Industries Co. Egypt summary=AJWA For Food Industries Co. Egypt (AJWA.CA) has released several market announcements recently, including disclosures from the Financial Regulatory Authority (FRA), decisions from Board of Directors' meetings, and AGM invitations. The company's TTM EPS is -3.80.
  - AJWA for Food Industries company - Egypt (AJWA.CA) - Release from FRA (July 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6kPIP17EgDaa_VVy4UvSIXer2YK8HWGCcnU8ve6SW7T7N1Ao0R-mtysI3-I9hozXkhN3heyJ2rq8zMvY0d4C7ZpZ5o4DLyBsI1ZNebk4Ik_Q_VvYP6f7t0SRVjyJm_dx_OAhA_Et1BaJbniw7eI9t
  - AJWA for Food Industries company Egypt (AJWA.CA) - Decisions of the Board of Directors' Meeting (July 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6kPIP17EgDaa_VVy4UvSIXer2YK8HWGCcnU8ve6SW7T7N1Ao0R-mtysI3-I9hozXkhN3heyJ2rq8zMvY0d4C7ZpZ5o4DLyBsI1ZNebk4Ik_Q_VvYP6f7t0SRVjyJm_dx_OAhA_Et1BaJbniw7eI9t
  - AJWA for Food Industries company - Egypt (AJWA.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6kPIP17EgDaa_VVy4UvSIXer2YK8HWGCcnU8ve6SW7T7N1Ao0R-mtysI3-I9hozXkhN3heyJ2rq8zMvY0d4C7ZpZ5o4DLyBsI1ZNebk4Ik_Q_VvYP6f7t0SRVjyJm_dx_OAhA_Et1BaJbniw7eI9t
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- COMI.CA: status=RECENT_ACCEPTED latest=2026-07-21 age_days=7 sources=3 expected=Commercial International Bank Egypt summary=Commercial International Bank Egypt (COMI.CA) has released its consolidated and standalone financial results for the first half of 2026, along with various board decisions and disclosures. The bank was also honored as the Best Bank in Sustainable Finance in Africa for 2025 and is undertaking due diligence on HSBC's retail banking portfolio. Financial highlights for FY2025 and Q1 2026 are also available.
  - Release from Commercial International Bank-Egypt (CIB) (COMI.CA) Regarding Financial Results (in English) (July 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYb-uGzLj9t-5VVC7B1xrMRZXCNuMSiL4qtnFn8MSIBpugdUtMb5Wkriy_-WgF8osftCSGfWHtp3fIEv0-r0uFIgcxqIPZV173l4KY5Gypu_a8tB3jGSlgex0dc30EppbesELayTpPpgTN8aDCUfPKKUk=
  - Commercial International Bank-Egypt (CIB) (COMI.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 30/06/2026 (July 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAS2OBnim-krxDhaLxmJVC3v_y9Wv_As-d7sLN7eeaCI48QTuCPNZYbyO2xGH_GT-1E-nB3yQZbLpYF7iDubXRokbXgZi-mvSb3GPws13QJHA9LzCHM3ridzkS_AVs7a2DjHotBiAMnZlQrPI7WTH3
  - Commercial International Bank-Egypt (CIB) (COMI.CA) Reports its Financial Results (Standalone) for the Period from 01/01/2026 to 30/06/2026 (July 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAS2OBnim-krxDhaLxmJVC3v_y9Wv_As-d7sLN7eeaCI48QTuCPNZYbyO2xGH_GT-1E-nB3yQZbLpYF7iDubXRokbXgZi-mvSb3GPws13QJHA9LzCHM3ridzkS_AVs7a2DjHotBiAMnZlQrPI7WTH3
- ARCC.CA: status=RECENT_ACCEPTED latest=2026-09-02 age_days=0 sources=3 expected=Arabian Cement Company summary=Arabian Cement Company (ARCC.CA) has been active with recent disclosures regarding its Board of Directors and shareholder structure, a listing committee decision, and a capital decrease. The company also announced plans to pay EGP 2bn in dividends for 2025 and reported strong financial results for Q1 and 1H 2025, as well as for the full year 2025. The next earnings report is expected on September 2, 2026.
  - Arabian Cement Company (ARCC.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsPmXfeC9rhPMJR_kraeaA9c7LgB6-HMbFd0B-50nLX9E8Ev4beMUigScilgg5NUOXIXmM5JJnMdqY1Nvxt9sMEQ-KF790bmQAJiggHNHNJAhk52el9CxJV6kBZiLJeWSv1JPudy2NvWXNWpAyvwE=
  - Arabian Cement Company (ARCC.CA) - Listing Committee Decision (July 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsPmXfeC9rhPMJR_kraeaA9c7LgB6-HMbFd0B-50nLX9E8Ev4beMUigScilgg5NUOXIXmM5JJnMdqY1Nvxt9sMEQ-KF790bmQAJiggHNHNJAhk52el9CxJV6kBZiLJeWSv1JPudy2NvWXNWpAyvwE=
  - Arabian Cement Company (ARCC.CA) – Capital Decrease through Terminating Treasury Stocks (July 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsPmXfeC9rhPMJR_kraeaA9c7LgB6-HMbFd0B-50nLX9E8Ev4beMUigScilgg5NUOXIXmM5JJnMdqY1Nvxt9sMEQ-KF790bmQAJiggHNHNJAhk52el9CxJV6kBZiLJeWSv1JPudy2NvWXNWpAyvwE=
- ORHD.CA: status=RECENT_ACCEPTED latest=2026-07-16 age_days=12 sources=3 expected=Orascom Development Egypt summary=Orascom Development Egypt (ORHD.CA) has issued several recent announcements, including releases concerning subsidiaries, disclosures of board and shareholder structures, and minutes from AGM/EGM meetings. The company reported EGP 5.3bn net profits in 2025 and has released its Q1 2026 and FY 2025 financial statements and earning releases.
  - Release from Orascom Development Egypt (ORHD.CA) Concerning one of its Subsidiaries (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA46osVaoQdDRc622Fbg5Voyz04LSiBs1dU1Orwc74xZWF6yOTyEa4GSXGM9oVYfzg64vkkLJb-P-ZA1yNGrodGWvb22kdwdICEuXkAnyAEdJB7Kw5xqZKaaY5XBUm4Zpkyzw1zFVpNOOI87mNrceW
  - Orascom Development Egypt (ORHD.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA46osVaoQdDRc622Fbg5Voyz04LSiBs1dU1Orwc74xZWF6yOTyEa4GSXGM9oVYfzg64vkkLJb-P-ZA1yNGrodGWvb22kdwdICEuXkAnyAEdJB7Kw5xqZKaaY5XBUm4Zpkyzw1zFVpNOOI87mNrceW
  - Orascom Development Egypt (ORHD.CA) - AGM Minutes (Notarized) (June 24, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA46osVaoQdDRc622Fbg5Voyz04LSiBs1dU1Orwc74xZWF6yOTyEa4GSXGM9oVYfzg64vkkLJb-P-ZA1yNGrodGWvb22kdwdICEuXkAnyAEdJB7Kw5xqZKaaY5XBUm4Zpkyzw1zFVpNOOI87mNrceW
- AALR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=General Company For Land Reclamation, Development & Reconstruction summary=General Land Reclamation expects over EGP 8.6m net profits in FY26/27 estimated budget; General Land Reclamation incurs EGP 29.5m loss in FY18/19; General Land Reclamation turns to losses in 9M Gemini also reviewed web evidence but did not return ticker-specific citations.
  - General Land Reclamation expects over EGP 8.6m net profits in FY26/27 estimated budget: https://english.mubasher.info/news/4600324/General-Land-Reclamation-expects-over-EGP-8-6m-net-profits-in-FY26-27-estimated-budget/
  - General Land Reclamation incurs EGP 29.5m loss in FY18/19: https://english.mubasher.info/news/3525030/General-Land-Reclamation-incurs-EGP-29-5m-loss-in-FY18-19/
  - General Land Reclamation turns to losses in 9M: https://english.mubasher.info/news/3465326/General-Land-Reclamation-turns-to-losses-in-9M/
- SIPC.CA: status=RECENT_ACCEPTED latest=2026-07-20 age_days=8 sources=3 expected=Sabaa International Company for Pharmaceutical and Chemical Industry summary=Sabaa International Company for Pharmaceutical and Chemical Industry (SIPC.CA) has had several recent market announcements, including changes in company data, AGM minutes and resolutions, and disclosures regarding board and shareholder structure. The company's audited financial statements as of December 31, 2025, are available, and it has reported its First Quarter 2026 financial metrics. The company is also classified as halal as of July 2026.
  - Release from Sabaa International Company For Pharmaceutical and Chemical (SIPC.CA) Regarding Changes on Company's Data (July 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvI1FABXnskTuOnUNoZ9P8rEO9E9zUTABDirqBHf0DW8CvlTxIE9JmbcmPNH84ptFbvkANDrlh3s7muU9OsiSIgYN0QPVkgRb8byRWz__GG67S8euaaHHVlPlFmOWYXPrWbPOexpD6BYivYHbI5NKZ
  - Sabaa International Company for Pharmaceutical and Chemical (SIPC.CA) - AGM Minutes (July 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvI1FABXnskTuOnUNoZ9P8rEO9E9zUTABDirqBHf0DW8CvlTxIE9JmbcmPNH84ptFbvkANDrlh3s7muU9OsiSIgYN0QPVkgRb8byRWz__GG67S8euaaHHVlPlFmOWYXPrWbPOexpD6BYivYHbI5NKZ
  - Sabaa International Company for Pharmaceutical and Chemical (SIPC.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 9, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvI1FABXnskTuOnUNoZ9P8rEO9E9zUTABDirqBHf0DW8CvlTxIE9JmbcmPNH84ptFbvkANDrlh3s7muU9OsiSIgYN0QPVkgRb8byRWz__GG67S8euaaHHVlPlFmOWYXPrWbPOexpD6BYivYHbI5NKZ

## Warnings
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for AALR.CA matches the company but no source/report date was detected.
