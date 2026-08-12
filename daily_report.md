# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-12T09:10:43.851094+00:00
Generated Cairo: 2026-08-12 12:10
Run timing: target 11:00 Cairo | generated Cairo 2026-08-12 12:10 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-12 12:06

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 57
- Data quality issues: 1
- Tradeable price/liquidity tickers: 169/189
- Top sector: Agriculture & Food Production

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, August 12
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 73.68% / above MA50 78.95%
- EGX70 regime: BULLISH / above MA20 83.78% / above MA50 91.89%
- Sector breadth: 61.9%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- SCEM.CA: liquidity=542870976.0 spike=4.0 score=34.9
- ARCC.CA: liquidity=480230752.0 spike=9.12 score=31.9
- CCAP.CA: liquidity=448616576.0 spike=0.71 score=23.77
- SVCE.CA: liquidity=374959424.0 spike=5.43 score=29.9
- PHAR.CA: liquidity=323039776.0 spike=0.98 score=24.9

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: {
  "summary": "Scanner flagged SUGR.CA, SAUD.CA and

## Top Liquidity Spikes
- MENA.CA: spike=10.96 liquidity=40860124.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MCQE.CA: spike=10.07 liquidity=171838496.0 outlook=WEAK_OR_RISKY score=10 buy_ready=False
- ARCC.CA: spike=9.12 liquidity=480230752.0 outlook=BULLISH_WATCH score=83 buy_ready=False
- MBSC.CA: spike=8.74 liquidity=301109120.0 outlook=WEAK_OR_RISKY score=4 buy_ready=False
- ALUM.CA: spike=7.24 liquidity=54713980.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Agriculture & Food Production: score=14.98 5d=11.93% 20d=14.89% aboveMA50=100.0%
- #2 Building Materials: score=14.28 5d=0.0% 20d=6.11% aboveMA50=66.67%
- #3 Transportation & Logistics: score=13.92 5d=9.79% 20d=14.04% aboveMA50=100.0%
- #4 Textiles: score=11.44 5d=4.45% 20d=14.36% aboveMA50=100.0%
- #5 Automotive & Distribution: score=11.21 5d=6.98% 20d=8.81% aboveMA50=100.0%
- #6 Education: score=11.18 5d=1.64% 20d=17.68% aboveMA50=100.0%
- #7 Healthcare: score=9.05 5d=2.35% 20d=15.95% aboveMA50=66.67%
- #8 Basic Resources & Chemicals: score=8.72 5d=3.58% 20d=5.34% aboveMA50=80.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY SUGR.CA
  - Entry: 50.4 | Take profit: 54.44 | Stop loss: 48.38
  - Confidence: LOW | score=32.8 | outlook=BULLISH_WATCH 87.76
  - Reason: WATCH/BUY SETUP: SUGR.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 66.67, support 46.47, resistance 49.25, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY SAUD.CA
  - Entry: 23.02 | Take profit: 24.86 | Stop loss: 22.1
  - Confidence: LOW | score=30.04 | outlook=BULLISH_WATCH 76.21
  - Reason: BUY SETUP: SAUD.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 62.05, support 21.25, resistance 22.8, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY PHDC.CA
  - Entry: 15.34 | Take profit: 16.56 | Stop loss: 14.73
  - Confidence: LOW | score=29.9 | outlook=BULLISH_WATCH 79.94
  - Reason: BUY SETUP: PHDC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 61.45, support 14.32, resistance 15.73, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- LCSW.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SUGR.CA: BULLISH_WATCH score=87.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- ALCN.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- GBCO.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SPIN.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SCTS.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- NHPS.CA: BULLISH_WATCH score=85.72 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ETRS.CA: BULLISH_WATCH score=84.72 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- SCEM.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- ARCC.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support

## BUY-Ready Candidates
- SUGR.CA: rank=32.8 outlook=BULLISH_WATCH outlook_score=87.76 sector_rank=15 price=50.4 support=46.47 resistance=49.25 liquidity=57278636.0
- SAUD.CA: rank=30.04 outlook=BULLISH_WATCH outlook_score=76.21 sector_rank=13 price=23.02 support=21.25 resistance=22.8 liquidity=15735859.0
- PHDC.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=79.94 sector_rank=11 price=15.34 support=14.32 resistance=15.73 liquidity=136508000.0
- ADPC.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=65.72 sector_rank=12 price=4.4 support=3.71 resistance=4.55 liquidity=14485812.0
- EHDR.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=72.72 sector_rank=12 price=3.1 support=2.64 resistance=3.15 liquidity=41930160.0
- PRMH.CA: rank=29.9 outlook=CONSTRUCTIVE outlook_score=67.72 sector_rank=12 price=2.88 support=2.56 resistance=2.92 liquidity=12624918.0
- UEFM.CA: rank=29.74 outlook=BULLISH_WATCH outlook_score=80.72 sector_rank=12 price=572.7 support=496.0 resistance=625.0 liquidity=14833806.0
- ATLC.CA: rank=28.41 outlook=CONSTRUCTIVE outlook_score=63.92 sector_rank=14 price=5.71 support=5.0 resistance=5.73 liquidity=20507566.0
- FERC.CA: rank=28.28 outlook=BULLISH_WATCH outlook_score=76.72 sector_rank=8 price=82.77 support=75.01 resistance=87.3 liquidity=18680346.0
- MFPC.CA: rank=28.24 outlook=BULLISH_WATCH outlook_score=72.72 sector_rank=8 price=38.61 support=35.37 resistance=38.8 liquidity=88295680.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=24.51 buy_ready=True sector_rank=12 price=296.21 support=225.1 resistance=325.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=69.73 liquidity=8611758.0 spike=0.22
- ABUK.CA: score=27.9 buy_ready=True sector_rank=8 price=75.25 support=69.88 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=57.99 liquidity=51417220.0 spike=0.35
- ACAMD.CA: score=25.9 buy_ready=False sector_rank=12 price=2.27 support=2.19 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=62.33 liquidity=18635780.0 spike=0.31
- ACGC.CA: score=24.9 buy_ready=False sector_rank=4 price=11.98 support=9.75 resistance=11.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=78.97 liquidity=28722906.0 spike=0.85
- ADCI.CA: score=27.42 buy_ready=False sector_rank=12 price=309.87 support=233.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=70.34 liquidity=9523990.0 spike=0.44
- ADIB.CA: score=24.9 buy_ready=False sector_rank=13 price=53.15 support=46.02 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=78.75 liquidity=17317142.0 spike=0.15
- ADPC.CA: score=29.9 buy_ready=True sector_rank=12 price=4.4 support=3.71 resistance=4.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=63.19 liquidity=14485812.0 spike=0.29
- AFDI.CA: score=10.9 buy_ready=False sector_rank=12 price=68.18 support=66.7 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13702189.0 spike=0.56
- AFMC.CA: score=24.9 buy_ready=False sector_rank=12 price=264.98 support=72.5 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=78.82 liquidity=95245536.0 spike=0.65
- AJWA.CA: score=23.9 buy_ready=False sector_rank=12 price=189.92 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=71.91 liquidity=14081614.0 spike=0.38
- ALCN.CA: score=27.04 buy_ready=True sector_rank=3 price=31.7 support=28.8 resistance=31.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=69.12 liquidity=30872940.0 spike=1.07
- ALUM.CA: score=15.9 buy_ready=False sector_rank=12 price=29.98 support=28.32 resistance=30.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54713980.0 spike=7.24
- AMER.CA: score=11.34 buy_ready=False sector_rank=11 price=8.13 support=7.3 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=132411072.0 spike=1.22
- AMES.CA: score=24.87 buy_ready=True sector_rank=12 price=121.86 support=102.31 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=60.95 liquidity=8969584.0 spike=0.1
- AMIA.CA: score=15.72 buy_ready=False sector_rank=12 price=12.37 support=8.74 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=80.42 liquidity=2823276.0 spike=0.17
- AMOC.CA: score=25.9 buy_ready=False sector_rank=9 price=9.59 support=8.13 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=72.31 liquidity=47140692.0 spike=0.48
- APSW.CA: score=6.0 buy_ready=False sector_rank=12 price=8.69 support=8.32 resistance=9.34 source=Yahoo Finance as_of=2026-08-10T21:00:00+00:00 freshness=FRESH RSI=34.66 liquidity=1101370.55 spike=0.63
- ARAB.CA: score=25.9 buy_ready=True sector_rank=11 price=0.25 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=28458088.0 spike=0.23
- ARCC.CA: score=31.9 buy_ready=False sector_rank=2 price=79.0 support=54.2 resistance=76.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=89.88 liquidity=480230752.0 spike=9.12
- AREH.CA: score=22.37 buy_ready=False sector_rank=12 price=1.53 support=1.38 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=55.1 liquidity=7466366.5 spike=0.19
- ARVA.CA: score=6.9 buy_ready=False sector_rank=12 price=12.35 support=12.35 resistance=12.35 source=Yahoo Finance as_of=2026-08-10T21:00:00+00:00 freshness=FRESH RSI=92.21 liquidity=0.0 spike=0.0
- ASCM.CA: score=25.9 buy_ready=False sector_rank=12 price=66.85 support=60.1 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=73.92 liquidity=48615480.0 spike=0.73
- ASPI.CA: score=24.9 buy_ready=False sector_rank=12 price=0.49 support=0.31 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=79.74 liquidity=14180494.0 spike=0.32
- ATLC.CA: score=28.41 buy_ready=True sector_rank=14 price=5.71 support=5.0 resistance=5.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=68.22 liquidity=20507566.0 spike=1.27
- ATQA.CA: score=24.9 buy_ready=False sector_rank=8 price=10.82 support=9.43 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=79.2 liquidity=28469382.0 spike=0.54
- AXPH.CA: score=20.26 buy_ready=True sector_rank=12 price=1309.14 support=1121.56 resistance=1460.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=68.41 liquidity=2357504.25 spike=0.52
- BINV.CA: score=16.25 buy_ready=False sector_rank=16 price=48.57 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=66.76 liquidity=481514.72 spike=0.07
- BIOC.CA: score=10.9 buy_ready=False sector_rank=12 price=501.28 support=501.01 resistance=560.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80660840.0 spike=0.49
- BTFH.CA: score=25.87 buy_ready=False sector_rank=14 price=3.1 support=3.03 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=48.84 liquidity=36782988.0 spike=0.16
- CAED.CA: score=10.9 buy_ready=False sector_rank=12 price=131.93 support=122.0 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53033840.0 spike=0.75
- CANA.CA: score=22.06 buy_ready=False sector_rank=13 price=40.02 support=35.2 resistance=40.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=73.66 liquidity=4155921.25 spike=0.21
- CCAP.CA: score=23.77 buy_ready=False sector_rank=16 price=5.33 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=35.79 liquidity=448616576.0 spike=0.71
- CCRS.CA: score=20.04 buy_ready=False sector_rank=12 price=2.51 support=2.44 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=6135810.0 spike=0.3
- CEFM.CA: score=27.9 buy_ready=True sector_rank=12 price=138.07 support=101.57 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=58.23 liquidity=20896380.0 spike=0.77
- CERA.CA: score=17.16 buy_ready=False sector_rank=12 price=1.33 support=1.25 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=3259814.75 spike=0.15
- CFGH.CA: score=9.91 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=12065.7 spike=0.68
- CICH.CA: score=18.89 buy_ready=True sector_rank=14 price=12.44 support=11.75 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=59.18 liquidity=1026166.06 spike=0.13
- CIEB.CA: score=22.21 buy_ready=True sector_rank=13 price=24.26 support=23.75 resistance=24.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=4305811.5 spike=0.4
- CIRA.CA: score=25.18 buy_ready=False sector_rank=6 price=39.13 support=30.66 resistance=39.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=78.83 liquidity=67220776.0 spike=1.14
- CLHO.CA: score=27.9 buy_ready=True sector_rank=7 price=17.46 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=62.89 liquidity=11626101.0 spike=0.23
- CNFN.CA: score=23.38 buy_ready=True sector_rank=14 price=4.92 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=3513271.0 spike=0.16
- COMI.CA: score=23.9 buy_ready=False sector_rank=13 price=138.93 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=45.38 liquidity=33545252.0 spike=0.07
- COPR.CA: score=23.6 buy_ready=True sector_rank=12 price=0.41 support=0.37 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=7700346.0 spike=0.24
- COSG.CA: score=22.76 buy_ready=True sector_rank=12 price=1.73 support=1.6 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=6863327.5 spike=0.18
- CPCI.CA: score=19.23 buy_ready=False sector_rank=12 price=539.39 support=426.05 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=78.47 liquidity=4330746.5 spike=0.29
- CSAG.CA: score=25.9 buy_ready=False sector_rank=3 price=41.18 support=31.35 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=78.97 liquidity=11324369.0 spike=0.52
- DAPH.CA: score=24.9 buy_ready=False sector_rank=12 price=129.11 support=82.0 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=91.3 liquidity=35742368.0 spike=1.0
- DEIN.CA: score=0.9 buy_ready=False sector_rank=12 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=21.15 buy_ready=True sector_rank=15 price=28.0 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=3342489.5 spike=0.29
- DSCW.CA: score=27.9 buy_ready=False sector_rank=12 price=2.15 support=1.77 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=23568404.0 spike=0.3
- DTPP.CA: score=24.9 buy_ready=False sector_rank=12 price=314.0 support=201.21 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=82.2 liquidity=29043738.0 spike=0.47
- EALR.CA: score=26.45 buy_ready=True sector_rank=12 price=390.32 support=360.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=58.87 liquidity=8547416.0 spike=0.26
- EASB.CA: score=10.53 buy_ready=False sector_rank=12 price=7.29 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=1631335.75 spike=0.15
- EAST.CA: score=16.8 buy_ready=False sector_rank=15 price=36.33 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=33.16 liquidity=10001483.0 spike=0.15
- EBSC.CA: score=19.14 buy_ready=True sector_rank=12 price=1.94 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=1235772.75 spike=0.19
- ECAP.CA: score=9.93 buy_ready=False sector_rank=12 price=39.48 support=39.21 resistance=41.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9025357.0 spike=0.86
- EDFM.CA: score=5.76 buy_ready=False sector_rank=12 price=418.74 support=402.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4858683.5 spike=0.85
- EEII.CA: score=25.72 buy_ready=True sector_rank=12 price=2.94 support=2.54 resistance=3.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=61.73 liquidity=5824611.0 spike=0.41
- EFIC.CA: score=21.45 buy_ready=False sector_rank=8 price=210.9 support=184.0 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=73.26 liquidity=3554674.25 spike=0.13
- EFID.CA: score=22.8 buy_ready=False sector_rank=15 price=31.51 support=26.64 resistance=32.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=77.22 liquidity=12915313.0 spike=0.16
- EFIH.CA: score=26.69 buy_ready=True sector_rank=19 price=23.96 support=21.87 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=46696320.0 spike=0.49
- EGAL.CA: score=15.9 buy_ready=False sector_rank=8 price=346.98 support=325.2 resistance=352.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=247493488.0 spike=3.8
- EGAS.CA: score=20.74 buy_ready=False sector_rank=9 price=61.75 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=77.15 liquidity=7839563.5 spike=0.29
- EGBE.CA: score=3.27 buy_ready=False sector_rank=13 price=0.52 support=0.52 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=269340.44 spike=2.05
- EGCH.CA: score=28.36 buy_ready=False sector_rank=8 price=14.55 support=12.69 resistance=14.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=224324464.0 spike=2.23
- EGSA.CA: score=5.35 buy_ready=False sector_rank=17 price=8.69 support=8.68 resistance=9.21 source=Yahoo Finance as_of=2026-08-10T21:00:00+00:00 freshness=FRESH RSI=18.37 liquidity=2615.69 spike=0.13
- EGTS.CA: score=28.6 buy_ready=False sector_rank=11 price=19.41 support=17.11 resistance=19.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=74.11 liquidity=51124776.0 spike=1.35
- EHDR.CA: score=29.9 buy_ready=True sector_rank=12 price=3.1 support=2.64 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=41930160.0 spike=0.91
- EKHO.CA: score=9.9 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=17.9 buy_ready=False sector_rank=10 price=2.17 support=2.12 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=17699584.0 spike=0.21
- ELKA.CA: score=18.9 buy_ready=False sector_rank=12 price=1.79 support=1.6 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=19.23 liquidity=82838280.0 spike=1.0
- ELNA.CA: score=10.07 buy_ready=False sector_rank=12 price=37.88 support=36.5 resistance=39.49 source=Yahoo Finance as_of=2026-08-10T21:00:00+00:00 freshness=FRESH RSI=43.03 liquidity=173831.32 spike=0.37
- ELSH.CA: score=23.9 buy_ready=False sector_rank=12 price=14.15 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=49.68 liquidity=36490672.0 spike=0.34
- ELWA.CA: score=7.05 buy_ready=False sector_rank=12 price=1.79 support=1.65 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=22.86 liquidity=1145121.12 spike=0.72
- EMFD.CA: score=27.9 buy_ready=True sector_rank=11 price=11.91 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=37093464.0 spike=0.64
- ENGC.CA: score=24.9 buy_ready=False sector_rank=12 price=49.38 support=40.11 resistance=50.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=76.77 liquidity=12736670.0 spike=0.38
- EOSB.CA: score=19.9 buy_ready=False sector_rank=12 price=1.55 support=1.52 resistance=1.62 source=Yahoo Finance as_of=2026-08-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=700.6 spike=0.01
- EPCO.CA: score=24.9 buy_ready=False sector_rank=12 price=12.7 support=9.72 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=75.39 liquidity=10752545.0 spike=0.32
- EPPK.CA: score=7.8 buy_ready=False sector_rank=12 price=13.25 support=13.06 resistance=15.93 source=Yahoo Finance as_of=2026-08-10T21:00:00+00:00 freshness=FRESH RSI=34.44 liquidity=1161534.75 spike=1.37
- ETEL.CA: score=27.34 buy_ready=True sector_rank=17 price=108.91 support=96.0 resistance=114.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=14641078.0 spike=0.14
- ETRS.CA: score=27.9 buy_ready=True sector_rank=12 price=10.8 support=10.21 resistance=10.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=61.23 liquidity=20206556.0 spike=0.9
- EXPA.CA: score=26.22 buy_ready=False sector_rank=13 price=21.01 support=18.61 resistance=21.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=74.38 liquidity=8315366.5 spike=0.24
- FAIT.CA: score=21.49 buy_ready=True sector_rank=13 price=39.0 support=36.1 resistance=39.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=62.15 liquidity=1591956.0 spike=0.54
- FAITA.CA: score=12.92 buy_ready=False sector_rank=13 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=48.94 liquidity=19909.38 spike=0.46
- FERC.CA: score=28.28 buy_ready=True sector_rank=8 price=82.77 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=64.45 liquidity=18680346.0 spike=1.19
- FWRY.CA: score=19.69 buy_ready=False sector_rank=19 price=18.79 support=18.43 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=38732592.0 spike=0.32
- GBCO.CA: score=22.66 buy_ready=True sector_rank=5 price=31.89 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=6755793.5 spike=0.1
- GDWA.CA: score=14.9 buy_ready=False sector_rank=12 price=0.81 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=17.53 liquidity=10504753.0 spike=0.09
- GGCC.CA: score=22.77 buy_ready=False sector_rank=12 price=1.18 support=0.59 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=7866676.5 spike=0.17
- GIHD.CA: score=27.9 buy_ready=False sector_rank=12 price=70.06 support=47.65 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=72.71 liquidity=27599404.0 spike=0.55
- GMCI.CA: score=13.9 buy_ready=False sector_rank=12 price=1.98 support=1.91 resistance=2.12 source=Yahoo Finance as_of=2026-08-09T21:00:00+00:00 freshness=FRESH RSI=36.73 liquidity=0.0 spike=0.0
- GRCA.CA: score=10.02 buy_ready=False sector_rank=12 price=57.72 support=51.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=29.62 liquidity=1122340.13 spike=0.06
- GSSC.CA: score=24.19 buy_ready=True sector_rank=12 price=283.11 support=258.15 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=52.87 liquidity=8291562.0 spike=0.48
- GTWL.CA: score=22.9 buy_ready=False sector_rank=12 price=125.45 support=85.0 resistance=139.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=75.19 liquidity=31522082.0 spike=0.35
- HDBK.CA: score=18.84 buy_ready=False sector_rank=13 price=84.93 support=76.9 resistance=85.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=65.77 liquidity=4944255.5 spike=0.13
- HELI.CA: score=25.9 buy_ready=True sector_rank=11 price=8.31 support=7.32 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=51.2 liquidity=10335407.0 spike=0.06
- HRHO.CA: score=27.87 buy_ready=True sector_rank=14 price=27.46 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=16222145.0 spike=0.17
- ICID.CA: score=27.92 buy_ready=False sector_rank=12 price=10.26 support=7.51 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=82.09 liquidity=19372770.0 spike=2.51
- IDRE.CA: score=23.57 buy_ready=False sector_rank=12 price=56.98 support=44.52 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=75.94 liquidity=8670507.0 spike=0.29
- IFAP.CA: score=27.09 buy_ready=False sector_rank=1 price=21.57 support=18.96 resistance=21.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=83.7 liquidity=9185731.0 spike=0.45
- INFI.CA: score=25.26 buy_ready=False sector_rank=12 price=168.5 support=99.02 resistance=178.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=93.26 liquidity=57519172.0 spike=1.18
- IRON.CA: score=18.74 buy_ready=False sector_rank=8 price=31.6 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=50.13 liquidity=6842363.0 spike=0.81
- ISMA.CA: score=24.9 buy_ready=False sector_rank=12 price=34.76 support=27.1 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=83.76 liquidity=12282866.0 spike=0.44
- ISMQ.CA: score=25.9 buy_ready=True sector_rank=8 price=9.81 support=8.96 resistance=9.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=66.11 liquidity=61338652.0 spike=0.88
- ISPH.CA: score=25.9 buy_ready=False sector_rank=7 price=13.88 support=11.2 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=73.14 liquidity=51591648.0 spike=0.29
- JUFO.CA: score=21.8 buy_ready=False sector_rank=15 price=26.42 support=22.78 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=45.34 liquidity=16131693.0 spike=0.3
- KABO.CA: score=18.74 buy_ready=True sector_rank=4 price=8.57 support=7.4 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=48.09 liquidity=2843932.25 spike=0.07
- KWIN.CA: score=20.09 buy_ready=False sector_rank=12 price=90.06 support=68.07 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=38.06 liquidity=6194709.0 spike=0.1
- KZPC.CA: score=24.15 buy_ready=False sector_rank=12 price=9.58 support=8.42 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=82.32 liquidity=9831619.0 spike=1.21
- LCSW.CA: score=27.9 buy_ready=True sector_rank=2 price=34.67 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=55.5 liquidity=27614164.0 spike=0.57
- LUTS.CA: score=11.08 buy_ready=False sector_rank=12 price=1.02 support=0.89 resistance=1.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58597160.0 spike=1.09
- MAAL.CA: score=25.9 buy_ready=False sector_rank=12 price=9.22 support=8.22 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=74.36 liquidity=14052154.0 spike=0.9
- MASR.CA: score=18.9 buy_ready=False sector_rank=12 price=7.8 support=7.45 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=48742564.0 spike=0.63
- MBSC.CA: score=17.9 buy_ready=False sector_rank=2 price=357.35 support=318.01 resistance=381.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=301109120.0 spike=8.74
- MCQE.CA: score=17.9 buy_ready=False sector_rank=2 price=263.19 support=240.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=171838496.0 spike=10.07
- MCRO.CA: score=23.9 buy_ready=True sector_rank=12 price=1.58 support=1.32 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=67635704.0 spike=0.36
- MENA.CA: score=15.9 buy_ready=False sector_rank=11 price=7.68 support=7.13 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40860124.0 spike=10.96
- MEPA.CA: score=21.52 buy_ready=True sector_rank=12 price=1.91 support=1.64 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=5623407.0 spike=0.09
- MFPC.CA: score=28.24 buy_ready=True sector_rank=8 price=38.61 support=35.37 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=50.46 liquidity=88295680.0 spike=1.17
- MFSC.CA: score=27.9 buy_ready=True sector_rank=12 price=51.26 support=45.75 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=55.55 liquidity=11664518.0 spike=0.97
- MHOT.CA: score=12.24 buy_ready=False sector_rank=18 price=19.39 support=19.0 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31237256.0 spike=2.21
- MICH.CA: score=11.4 buy_ready=False sector_rank=12 price=49.59 support=46.64 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40187212.0 spike=1.25
- MILS.CA: score=28.06 buy_ready=True sector_rank=12 price=193.53 support=135.3 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=60.51 liquidity=67919920.0 spike=1.08
- MIPH.CA: score=10.94 buy_ready=False sector_rank=7 price=782.81 support=783.84 resistance=783.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1043171.19 spike=1.0
- MOED.CA: score=15.32 buy_ready=False sector_rank=12 price=0.7 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=29.27 liquidity=37054664.0 spike=1.21
- MOIL.CA: score=11.2 buy_ready=False sector_rank=9 price=0.67 support=0.53 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=90.83 liquidity=300010.12 spike=0.46
- MOIN.CA: score=10.9 buy_ready=False sector_rank=12 price=35.3 support=34.92 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22126434.0 spike=1.0
- MOSC.CA: score=24.9 buy_ready=False sector_rank=12 price=313.54 support=275.01 resistance=318.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=79.76 liquidity=12782319.0 spike=0.78
- MPCI.CA: score=10.9 buy_ready=False sector_rank=12 price=375.92 support=370.0 resistance=401.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62890156.0 spike=0.45
- MPCO.CA: score=28.28 buy_ready=False sector_rank=1 price=2.23 support=1.82 resistance=2.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=82.76 liquidity=115687040.0 spike=1.19
- MPRC.CA: score=24.9 buy_ready=False sector_rank=12 price=50.84 support=41.0 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=76.28 liquidity=13828839.0 spike=0.55
- MTIE.CA: score=24.9 buy_ready=False sector_rank=5 price=11.23 support=9.3 resistance=11.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=86.38 liquidity=28242228.0 spike=0.77
- NAHO.CA: score=11.91 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8515.73 spike=0.41
- NCCW.CA: score=16.99 buy_ready=False sector_rank=12 price=5.89 support=5.67 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=42.47 liquidity=6087548.0 spike=0.17
- NEDA.CA: score=6.17 buy_ready=False sector_rank=12 price=2.73 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-08-10T21:00:00+00:00 freshness=FRESH RSI=24.0 liquidity=274818.18 spike=0.39
- NHPS.CA: score=27.9 buy_ready=True sector_rank=12 price=91.04 support=82.0 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=55.31 liquidity=16729497.0 spike=0.21
- NINH.CA: score=21.68 buy_ready=True sector_rank=12 price=22.64 support=17.7 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=5777895.0 spike=0.1
- NIPH.CA: score=10.9 buy_ready=False sector_rank=7 price=416.64 support=413.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=154143456.0 spike=0.73
- OBRI.CA: score=13.01 buy_ready=False sector_rank=12 price=32.81 support=31.61 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=8109596.0 spike=0.24
- OCDI.CA: score=24.9 buy_ready=False sector_rank=11 price=34.3 support=26.2 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=88.52 liquidity=46859968.0 spike=0.38
- OCPH.CA: score=20.9 buy_ready=False sector_rank=12 price=307.69 support=225.0 resistance=500.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=40.63 liquidity=15362368.0 spike=0.45
- ODIN.CA: score=24.9 buy_ready=False sector_rank=12 price=3.69 support=2.41 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=89.66 liquidity=29799890.0 spike=0.94
- OFH.CA: score=24.9 buy_ready=False sector_rank=12 price=0.9 support=0.62 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=83.45 liquidity=27541800.0 spike=0.31
- OIH.CA: score=25.09 buy_ready=False sector_rank=16 price=1.72 support=1.41 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=84.85 liquidity=97601016.0 spike=1.16
- OLFI.CA: score=24.8 buy_ready=False sector_rank=15 price=24.21 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=79.62 liquidity=16907928.0 spike=0.41
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=715.49 support=713.0 resistance=719.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30351354.0 spike=1.0
- ORHD.CA: score=27.9 buy_ready=False sector_rank=11 price=42.47 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=73.79 liquidity=36961808.0 spike=0.23
- ORWE.CA: score=22.9 buy_ready=False sector_rank=4 price=27.3 support=22.42 resistance=27.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=81.54 liquidity=66595656.0 spike=0.99
- PHAR.CA: score=24.9 buy_ready=False sector_rank=7 price=147.8 support=85.4 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=79.88 liquidity=323039776.0 spike=0.98
- PHDC.CA: score=29.9 buy_ready=True sector_rank=11 price=15.34 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=61.45 liquidity=136508000.0 spike=0.57
- PHTV.CA: score=15.27 buy_ready=False sector_rank=12 price=405.41 support=291.51 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=90.2 liquidity=367632.34 spike=0.13
- POUL.CA: score=24.39 buy_ready=True sector_rank=15 price=39.56 support=36.5 resistance=40.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=4590054.0 spike=0.15
- PRCL.CA: score=19.36 buy_ready=False sector_rank=2 price=34.97 support=32.76 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=45.68 liquidity=3456554.25 spike=0.09
- PRDC.CA: score=23.9 buy_ready=False sector_rank=11 price=8.99 support=8.21 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=36.68 liquidity=10750565.0 spike=0.1
- PRMH.CA: score=29.9 buy_ready=True sector_rank=12 price=2.88 support=2.56 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=12624918.0 spike=0.69
- RACC.CA: score=24.29 buy_ready=True sector_rank=12 price=10.16 support=9.8 resistance=10.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=8394614.0 spike=0.37
- RAKT.CA: score=11.22 buy_ready=False sector_rank=12 price=22.69 support=21.66 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=81.67 liquidity=317042.5 spike=0.95
- RAYA.CA: score=11.94 buy_ready=False sector_rank=21 price=7.31 support=7.2 resistance=8.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=33.98 liquidity=12059663.0 spike=0.11
- RMDA.CA: score=24.9 buy_ready=False sector_rank=7 price=6.49 support=4.94 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=78.23 liquidity=52317028.0 spike=0.49
- ROTO.CA: score=24.9 buy_ready=False sector_rank=12 price=49.49 support=40.5 resistance=51.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=82.38 liquidity=18781006.0 spike=0.85
- RREI.CA: score=25.9 buy_ready=False sector_rank=12 price=4.62 support=3.72 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=71.16 liquidity=11303809.0 spike=0.17
- RTVC.CA: score=8.83 buy_ready=False sector_rank=12 price=3.8 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=30.68 liquidity=2929645.0 spike=0.56
- RUBX.CA: score=17.69 buy_ready=False sector_rank=12 price=12.39 support=12.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=23.37 liquidity=8793532.0 spike=0.26
- SAUD.CA: score=30.04 buy_ready=True sector_rank=13 price=23.02 support=21.25 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=62.05 liquidity=15735859.0 spike=1.07
- SCEM.CA: score=34.9 buy_ready=False sector_rank=2 price=100.0 support=61.28 resistance=98.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=73.23 liquidity=542870976.0 spike=4.0
- SCFM.CA: score=25.9 buy_ready=True sector_rank=12 price=288.95 support=250.12 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=17555100.0 spike=0.6
- SCTS.CA: score=20.22 buy_ready=True sector_rank=6 price=617.99 support=602.0 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=4315995.5 spike=0.51
- SDTI.CA: score=19.26 buy_ready=False sector_rank=12 price=73.0 support=46.6 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=86.16 liquidity=4362227.0 spike=0.15
- SEIG.CA: score=22.9 buy_ready=False sector_rank=12 price=280.12 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=86.48 liquidity=10311067.0 spike=0.59
- SIPC.CA: score=19.76 buy_ready=False sector_rank=12 price=4.75 support=3.45 resistance=5.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=75.51 liquidity=6856444.0 spike=0.12
- SKPC.CA: score=24.92 buy_ready=True sector_rank=8 price=16.71 support=14.8 resistance=16.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=65.98 liquidity=43783980.0 spike=1.01
- SMFR.CA: score=25.9 buy_ready=False sector_rank=12 price=266.58 support=206.41 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=74.12 liquidity=16842872.0 spike=0.44
- SNFC.CA: score=9.85 buy_ready=False sector_rank=12 price=10.7 support=10.6 resistance=11.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=24.78 liquidity=3945668.75 spike=0.33
- SPIN.CA: score=21.71 buy_ready=True sector_rank=4 price=15.51 support=14.57 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=59.59 liquidity=5807467.5 spike=0.2
- SPMD.CA: score=26.63 buy_ready=True sector_rank=12 price=0.48 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=64.49 liquidity=8733977.0 spike=0.26
- SUGR.CA: score=32.8 buy_ready=True sector_rank=15 price=50.4 support=46.47 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=57278636.0 spike=5.99
- SVCE.CA: score=29.9 buy_ready=False sector_rank=12 price=11.61 support=9.06 resistance=11.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=82.29 liquidity=374959424.0 spike=5.43
- SWDY.CA: score=24.9 buy_ready=False sector_rank=10 price=109.61 support=87.41 resistance=114.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=77.41 liquidity=43658644.0 spike=0.71
- TALM.CA: score=25.9 buy_ready=False sector_rank=6 price=19.01 support=15.51 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=70.69 liquidity=26075932.0 spike=0.66
- TMGH.CA: score=23.9 buy_ready=False sector_rank=11 price=97.8 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=36.42 liquidity=49250616.0 spike=0.14
- TRTO.CA: score=11.9 buy_ready=False sector_rank=12 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-08-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=212.67 spike=0.14
- UEFM.CA: score=29.74 buy_ready=True sector_rank=12 price=572.7 support=496.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=62.85 liquidity=14833806.0 spike=2.92
- UEGC.CA: score=19.23 buy_ready=True sector_rank=12 price=2.7 support=1.88 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=67.65 liquidity=3327328.75 spike=0.06
- UNIP.CA: score=20.86 buy_ready=True sector_rank=12 price=0.42 support=0.34 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=46.79 liquidity=4963674.0 spike=0.17
- UNIT.CA: score=26.78 buy_ready=False sector_rank=11 price=20.77 support=17.32 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=70.64 liquidity=27762000.0 spike=1.44
- WCDF.CA: score=27.36 buy_ready=False sector_rank=12 price=640.77 support=519.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=88.24 liquidity=13593840.0 spike=3.23
- WKOL.CA: score=19.42 buy_ready=True sector_rank=12 price=328.7 support=307.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=3524565.0 spike=0.15
- ZEOT.CA: score=17.34 buy_ready=True sector_rank=12 price=13.12 support=11.1 resistance=13.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=65.33 liquidity=3437876.25 spike=0.12
- ZMID.CA: score=25.9 buy_ready=True sector_rank=11 price=7.51 support=7.06 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=58.27 liquidity=26861632.0 spike=0.1

## Backtesting Lite
- SCEM.CA: 180d return=61.84%, max drawdown=-14.53%, MA20>MA50 days last20=15, as_of=2026-08-10T21:00:00+00:00
- SUGR.CA: 180d return=3.97%, max drawdown=-11.28%, MA20>MA50 days last20=0, as_of=2026-08-10T21:00:00+00:00
- ARCC.CA: 180d return=80.23%, max drawdown=-12.0%, MA20>MA50 days last20=3, as_of=2026-08-10T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SCEM.CA: status=RECENT_ACCEPTED latest=2026-07-22 age_days=21 sources=3 expected=Sinai Cement summary=Recent disclosures from Sinai Cement (SCEM.CA) on the Egyptian Exchange include updates on its Board of Directors and shareholder structure. The company is listed on the EGX and operates in the construction materials sector. Financial information is available through various market data providers.
  - Sinai Cement (SCEM.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 22, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4sgaTRyWOZcTlHl5x6ZYlr-G6TBj2HtDFctPmFRwt8XcetuhP_zhm8zKceoIKYTSKU_r1lN61TcAr1F2FGaNEiGOh-30RbgnGbHfdpSe_X04ZJlyhY7uMNjc8n43h2SRUwD7w__LHJAEoRoQgaVI=
  - Sinai Cement Co. (S.A.E) (EGX:SCEM) Financials & Income Statement - Stock Analysis: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElBlq3sHZ2WkWxOpZp1pXA93z9DMJCKqUaChpItma6kMYvc7DLkch50QzlvIkLV_o0TANira8XStiknbzee8nRjMJBQn-8kD4jhlX5eS3gWZ0NCTYcAzHHw-Xz-E1POQ6e7ih834foXX90XmmnsQ==
  - Sinai Cement Profile - Decypha (as of 2025 for employee count): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7geSfclef42kYPitZSyFdOSIpDgFEcl30Tyw0qNV4qwneCI5i8kEqv4Qe8cAoYP8Gxj0MZKXTXIe2Iur_HUYFG15iEoW5D9X2a6IQBsPY2sY2yezcNFOXgFKA-HjYQtbSp0TQ7EbJAQdbhzpPfFVvY_zQpAgPBUEl
- SUGR.CA: status=RECENT_ACCEPTED latest=2026-08-10 age_days=2 sources=3 expected=Delta Sugar summary=Delta Sugar (SUGR.CA) has recently submitted disclosure forms regarding its Board of Directors and shareholder structure. The company's financial results for Q1 2026 show a net income of 72.51 million EGP and revenue of 2.04 billion EGP. Upcoming earnings are expected around August 10, 2026.
  - Delta Sugar (SUGR.CA) - Disclosure form Regarding the BoD and Shareholder Structure (April 07, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsgDbbrIIcrq682bK91LuSELA0njP9RxLhNVKKFMMqA0pFmkqc4ee6zImqFQUsukopXnqn5W59O9w68cJCzCe3DDBA2n_ckA9u1am89WsFl48PjXilmNwRXSRSrSjbK_50A1tLYh_ncvpddi_RLXjt3-c=
  - Delta Sugar Income Statement – EGX:SUGR - TradingView (Q1 2026 results): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-99m8bGUxNnKvG2UF8cw0G-ydEr9p2xub8hcTVXZeu3qQfMG_iCeyzm_1x7PM6UkmUtcXPveF549aKuyDVPmgqCsP4mKWy9KlszsPqVpRUvD-Ojz07v8r4JWXM8tkTfuCtcx-rxnYI83W8eSFchPA2P0sM8Rb2-UbdIp3XN5Ct-mzyg==
  - Delta Sugar Company (CASE:SUGR) - Stock Analysis - Simply Wall St (August 05, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyPWpo-uHC8O0ksNFIVuT7AuEmDQntDCknYCQrzq-P1nMY5yLGg_kbhMR8Ayzgocd3vGdXzGMSPAqgi7TyQv_dqkT3g7fbUJjrpIl8tvo2iW0K0ubsvRmjvWL7bTUjaDpZhvG6DKvk7iVT41CypQMaRDDS8z8naks1M8FZA7pJwi7dmvXPiZHYqFQQAA==
- ARCC.CA: status=RECENT_ACCEPTED latest=2026-09-02 age_days=0 sources=3 expected=Arabian Cement Company summary=Arabian Cement Company (ARCC.CA) has released several disclosures and decisions from its Board of Directors meetings in recent months. The company reported significant revenue and earnings growth in 2025, with revenue at 12.45 billion EGP and earnings at 3.58 billion EGP. The next earnings report is anticipated around September 2, 2026.
  - Arabian Cement Company (ARCC.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9Ia7CICIx8XYH8i8yvlEw1x9gtQVgly0KA6UBYbpUWuXg62boMGy3kRg5ShTgF2hY2LCE4wPzdsnliVey0Mu8yO4Y1gYAzzMQWKQ8tqugl6_oxjXzeiSKxLMPqJO-eodl5IaB4w50z5JIeN3fOBuAaBD2Sqlo5dNyd-nrYYU=
  - Arabian Cement Company (ARCC.CA) - Decisions of the BoD Meeting (June 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9Ia7CICIx8XYH8i8yvlEw1x9gtQVgly0KA6UBYbpUWuXg62boMGy3kRg5ShTgF2hY2LCE4wPzdsnliVey0Mu8yO4Y1gYAzzMQWKQ8tqugl6_oxjXzeiSKxLMPqJO-eodl5IaB4w50z5JIeN3fOBuAaBD2Sqlo5dNyd-nrYYU=
  - Arabian Cement Company S.A.E. (EGX:ARCC) Stock Price & Overview - Stock Analysis (2025 Financials, Earnings Date: August 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaHMH6ncIA6nb-mw0IN2DWF92ozyLf1XgcaN-usA4vB0bSZzi_QHWt-cr95V-ta1xfByDeYMqpy5meguDa_Ym7eycGPafPulMw0Ntvyk_efNgpFZJk5iHiNqk28j0ImVmysUQ=
- SAUD.CA: status=RECENT_ACCEPTED latest=2026-08-05 age_days=7 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt (SAUD.CA) is listed on the Egyptian Exchange and provides corporate and retail banking services. A recent Central Bank of Egypt approval for a CFO appointment was announced in May 2025. The bank's investor relations contact is Hatem Mohamed Abdul Ghani Mohamed.
  - alBaraka Bank - Central Bank of Egypt approval for CFO appointment (May 25, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXHaqiJfh7CsyDvHwu2J1n7Wpj3AF5I_Yewwn_oRNyZySlsxAMA1qScaWJYm9iNCnkWYzmQQPOjoGRfA9bipN_QjU7gcEGF3HUDyftU7_oLx5JTKKbWJGgNfj6GNtZ-LdExmHMGNRFRZfrubhe7VX5Rg==
  - Al Baraka Bank - Egypt (SAUD) - Investor Relations Contact: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUBARdE5sli_5QYh95BDXfxXogP0hMVc2l4v5EGpuKrJTk9TrhjAQjq5f9qVu4HGYLgrzLYhSWtmRiJlHHWo529hXgCw-8Qqd0QCbGsWnGYPLcoMi7GbEkDDT6dvF6gM9ZCeZcPlwFPV8vN_aArpXMozlX7Kk5VfQ=
  - Al Baraka Bank Egypt (SAUD.EG) Company Profile | Finance | MyStocks Af (August 05, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPEYlXJ65J-VlFdyCetG7bFmue_npHMhUIJJM2uU7MbBEGL4teqVdf4gH3yn7IdJXF6DoecDRW4CWdy52pxjynQYpTh5Bx1q1zKNlrLjfGnDaJnLVPIZ0WdwcHQ-lcWLd3dxBbEf4DNRa5sefT-FGHJsaPRA==
- PHDC.CA: status=RECENT_ACCEPTED latest=2026-08-11 age_days=1 sources=3 expected=Palm Hills Development summary=Palm Hills Development (PHDC.CA) is a real estate developer listed on the EGX. The company reported its Q1 2026 earnings with revenue of 9.35 billion EGP and net income of 1.21 billion EGP. In 2025, its revenue was 36.17 billion EGP and earnings were 4.22 billion EGP. The stock price was recently updated on August 11, 2026.
  - Stock Information - Palm Hills Developments (Last Updated: August 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5Z-YLuVnUIJF5CD035g0zwwLqotq7xL6O1iyEPEOkEc1bDv8IVQ0vwrPh5-f6GrsFYmxwi9Yx8Byjgn6ltGF8jYUvQcsLDE52QXLXDUHZeY9iu1cQLeK8URN9_OCTI1XtNK3AeKnhANPO-HpB1U5h9TZlktw=
  - Palm Hills DevelopmentsE (CASE:PHDC) Stock Price - Simply Wall St (Q1 2026 earnings released: March 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaii5kQIycCtfwXGEHRipi-BAGfZHKnIgO5Mm_vkoOSOnPPn6BVWXDeruBPiPsUbas1o7L2Dv_LeBxZ0GVq0-udpAZtH8U-HY4go97jw-IQLYinjddx70Or7BiDSaErQ==
  - Palm Hills Developments S.A.E. (EGX:PHDC) Stock Price & Overview - Stock Analysis (2025 Financials, Earnings Date: August 10, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK4MJ4e33IrSK6lNng7c5nUuUWzh0NNq8MxmQ4nKb1h82sNT1qP9WtoIGThIaa4aTlbG3v748BZE--aPKRhUqrTwCvADtruY8OJw10RC0wq42Vc3HP0Vt0MxlEeqfgTqck3wI=
- ADPC.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=0 sources=3 expected=The Arab Dairy Products Co. summary=The Arab Dairy Products Co. (ADPC.CA) recently announced a capital decrease through terminating treasury stocks, approved by the Listing Committee on July 29, 2026. The company also reported its consolidated financial results for Q1 2026, showing a net loss of 122,922,483 EGP. The company's 2024 revenue was 3.08 billion EGP.
  - Capital Decrease Through Terminating Treasury Stocks - The Egyptian Exchange (July 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLUrf1WfIxXlc-T_Q7LVH7oMbhz5_d35lNJ9eJiaI4xHi6kv8Mhzzsu7_xM-j5SnIkuW2fu5XDlpnSbMi8vQkZO_LfReTBlH70yc2zgvoGL5koxlY9rXHGXRtOkb8EevS54UzlOlyIXaQ-GCeW-tXDlCc=
  - Arab Dairy - Panda (ADPC.CA) Reports its Financial Results (Consolidated) for the Period from 01/01/2026 to 31/03/2026 (June 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBMnl0FebWTT3ehGVCCNqYyRTKhihD1tN2wICE7HmHx92LKxJy0XZGNLb6s6QHfSvZ1gIIJJsd1tTwI7oATfqI8IFA-oioRLINx2LSCcHTSz21DlisinaMIkNmKnqJJJLq03COwDdSbVxN1tDQaw==
  - The Arab Dairy Products Co. (EGX:ADPC) Stock Price & Overview - Stock Analysis (2024 Financials, Earnings Date: August 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiewLWvn2DbMBkWEnibvnnHGRKost-VdBxZ1PJ1eIek-sDBJFqcSDWqA6SjUujpE0U_HEq449PrREpelehHsQgckqvNSxI8LcXLu9ZuuEflFjv668CQJi0Z0BiVNYTb7VGGqI=
- EHDR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=588 sources=3 expected=Egyptians for Housing & Development Co. summary=Egyptians for Housing to disburse EGP 0.01/shr for 2025; EGX-listed companies, banks propose cash dividends for 2025; Egyptians for Housing stock witnesses selling pressures amid key levels to observe – Analysis Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Egyptians for Housing to disburse EGP 0.01/shr for 2025: https://english.mubasher.info/news/4584569/Egyptians-for-Housing-to-disburse-EGP-0-01-shr-for-2025/
  - EGX-listed companies, banks propose cash dividends for 2025: https://english.mubasher.info/news/4560139/EGX-listed-companies-banks-propose-cash-dividends-for-2025/
  - Egyptians for Housing stock witnesses selling pressures amid key levels to observe – Analysis: https://english.mubasher.info/news/4547337/Egyptians-for-Housing-stock-witnesses-selling-pressures-amid-key-levels-to-observe-Analysis/
- PRMH.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=0 sources=3 expected=Prime Holding S.A.E summary=Prime Holding S.A.E (PRMH.CA) has submitted a disclosure form concerning its Board of Directors and shareholder structure on July 13, 2026. The company is a regional investment bank listed on the Egyptian Exchange since 2008, with a paid capital of EGP 350 million. Its next earnings report is expected around August 13, 2026.
  - Prime Holding (PRMH.CA) - Disclosure Form Concerning the BoD & the Shareholders' Structure - The Egyptian Exchange (July 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkpFW0UnRFHVKGMX_tDX7rXjFRJs_vdVe2nO-rJJS0WZ2u__C8845J6V9jQ0ZroROx7U1kkwAeqcUnp27HnvGRjqj-nYxEaBgq7G9HHGHo77NSnWyX7_e0TLgw7nnnnAax-TLH_whKSst2XyHZRSLIZIE=
  - Investor Relations - Prime Holding (General Information): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEntEJN2Z1zdCfCwmtwmAj-15ut3WlcBKEnF_fc1eeBRMpiwU8nWPWOCVu0Pw4C2fsIhie15nnEdcC6_YTgOV5Tg_L6_ZosL7PTkuN1fHWzVvAxONUqAESmptG0PFaWNZABKK_-yqtG8Q==
  - Prime Holding S.A.E (EGX:PRMH) Stock Price & Overview - Stock Analysis (Earnings Date: August 13, 2026): https://vertexaisearch.google.com/grounding-api-redirect/AUZIYQHDTYDL2T40AArIR0hGJ0nZKTnPXCLl1j-P7hYb_HmA2hMigvKne8QmJpBLJnyWLa2D4b5G6IobkTcf4-us0OlQIH2mVG5PsaWzVUFW-ETndgnK7aUrB0_CfVg2YA1p9rmBz08

## Warnings
- Evidence for EHDR.CA matches the company but appears old; latest detected date is 2025-01-01.
