# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-09T10:53:06.201091+00:00
Generated Cairo: 2026-07-09 13:53
Run timing: target 11:00 Cairo | generated Cairo 2026-07-09 13:53 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-09 13:49

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 74
- Data quality issues: 0
- Tradeable price/liquidity tickers: 174/190
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, July 09
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 65.0% / above MA50 55.0%
- EGX70 regime: BULLISH / above MA20 78.38% / above MA50 72.97%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- HELI.CA: liquidity=565749568.0 spike=4.66 score=14.4
- CCAP.CA: liquidity=328125024.0 spike=0.47 score=26.4
- GTWL.CA: liquidity=215761760.0 spike=2.93 score=12.86
- AMER.CA: liquidity=181573696.0 spike=2.68 score=12.76
- COMI.CA: liquidity=179778224.0 spike=0.39 score=26.22

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: EGX30 and EGX70 are bullish but the scanner runs in SELECTIVE_SWING_TRADES_ONLY mode, so only setups with aligned price, adequate liquidity and clear support/resistance are flagged; GSSC.CA, ETEL.CA and NHPS.CA meet those technical filters despite low confidence and sector‑specific caveats.
- ? That's okay as it's from data, not invented. But maybe better to avoid exact numbers? The instruction:
- Using given data is fine. But we can keep description qualitative.

We need to output only valid compact JSON. Ensure proper escaping.

Let's craft:

{

## Top Liquidity Spikes
- GIHD.CA: spike=14.17 liquidity=132443312.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UNIT.CA: spike=10.07 liquidity=107747280.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- UEFM.CA: spike=8.66 liquidity=9568085.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCFM.CA: spike=6.99 liquidity=28193078.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMES.CA: spike=6.79 liquidity=174367888.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=9.81 5d=3.06% 20d=2.85% aboveMA50=100.0%
- #2 Technology & Distribution: score=9.16 5d=1.56% 20d=4.56% aboveMA50=100.0%
- #3 Fintech & Payments: score=9.06 5d=7.64% 20d=4.37% aboveMA50=50.0%
- #4 Transportation & Logistics: score=7.3 5d=-0.59% 20d=1.07% aboveMA50=100.0%
- #5 Investment Holding: score=6.91 5d=3.23% 20d=0.71% aboveMA50=66.67%
- #6 Textiles: score=6.87 5d=2.95% 20d=0.0% aboveMA50=100.0%
- #7 Automotive & Distribution: score=6.59 5d=-2.15% 20d=4.7% aboveMA50=100.0%
- #8 Real Estate: score=6.01 5d=1.68% 20d=2.08% aboveMA50=76.92%

## Today's Prioritized Action Tickets
- Priority #1: BUY GSSC.CA
  - Entry: 257.08 | Take profit: 277.64 | Stop loss: 246.8
  - Confidence: LOW | score=31.0 | outlook=BULLISH_WATCH 86.99
  - Reason: BUY SETUP: GSSC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 60.77, support 240.0, resistance 263.63, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ETEL.CA
  - Entry: 98.01 | Take profit: 105.85 | Stop loss: 94.09
  - Confidence: LOW | score=29.4 | outlook=BULLISH_WATCH 89.81
  - Reason: BUY SETUP: ETEL.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 60.23, support 89.01, resistance 101.5, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY NHPS.CA
  - Entry: 71.61 | Take profit: 77.33 | Stop loss: 68.75
  - Confidence: LOW | score=29.0 | outlook=BULLISH_WATCH 78.99
  - Reason: WATCH/BUY SETUP: NHPS.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 65.33, support 61.55, resistance 75.49, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EALR.CA: BULLISH_WATCH score=92.99 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ETEL.CA: BULLISH_WATCH score=89.81 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=87.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- GSSC.CA: BULLISH_WATCH score=86.99 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ENGC.CA: BULLISH_WATCH score=86.99 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- BIOC.CA: BULLISH_WATCH score=82.99 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- CCAP.CA: BULLISH_WATCH score=82.91 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- BINV.CA: BULLISH_WATCH score=82.91 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ACGC.CA: BULLISH_WATCH score=82.87 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ALCN.CA: BULLISH_WATCH score=82.3 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- GSSC.CA: rank=31.0 outlook=BULLISH_WATCH outlook_score=86.99 sector_rank=12 price=257.08 support=240.0 resistance=263.63 liquidity=15167496.0
- ETEL.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=89.81 sector_rank=1 price=98.01 support=89.01 resistance=101.5 liquidity=27810870.0
- NHPS.CA: rank=29.0 outlook=BULLISH_WATCH outlook_score=78.99 sector_rank=12 price=71.61 support=61.55 resistance=75.49 liquidity=86459864.0
- RREI.CA: rank=28.74 outlook=BULLISH_WATCH outlook_score=76.99 sector_rank=12 price=3.77 support=3.34 resistance=3.93 liquidity=23894944.0
- CERA.CA: rank=28.6 outlook=BULLISH_WATCH outlook_score=80.99 sector_rank=12 price=1.32 support=1.15 resistance=1.3 liquidity=44930244.0
- RAYA.CA: rank=28.56 outlook=BULLISH_WATCH outlook_score=80.16 sector_rank=2 price=7.94 support=6.7 resistance=8.28 liquidity=112793000.0
- ENGC.CA: rank=28.0 outlook=BULLISH_WATCH outlook_score=86.99 sector_rank=12 price=37.65 support=33.0 resistance=39.55 liquidity=30620716.0
- ARAB.CA: rank=27.86 outlook=BULLISH_WATCH outlook_score=82.01 sector_rank=8 price=0.23 support=0.2 resistance=0.24 liquidity=128122952.0
- EFIH.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=87.06 sector_rank=3 price=22.25 support=20.0 resistance=23.65 liquidity=27130148.0
- ALCN.CA: rank=27.2 outlook=BULLISH_WATCH outlook_score=82.3 sector_rank=4 price=29.08 support=25.51 resistance=33.2 liquidity=15441307.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=26.0 buy_ready=True sector_rank=12 price=221.41 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=62.25 liquidity=12483920.0 spike=0.93
- ABUK.CA: score=20.3 buy_ready=False sector_rank=19 price=70.25 support=66.66 resistance=81.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=113549488.0 spike=0.83
- ACAMD.CA: score=26.0 buy_ready=True sector_rank=12 price=2.34 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=72775464.0 spike=0.71
- ACGC.CA: score=18.81 buy_ready=True sector_rank=6 price=9.56 support=8.92 resistance=10.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=51.27 liquidity=4406875.0 spike=0.18
- ADCI.CA: score=14.86 buy_ready=False sector_rank=12 price=231.31 support=219.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=56.4 liquidity=2864055.25 spike=0.24
- ADIB.CA: score=26.88 buy_ready=True sector_rank=10 price=47.25 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=117654096.0 spike=1.33
- ADPC.CA: score=12.52 buy_ready=False sector_rank=12 price=3.69 support=3.51 resistance=3.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36139168.0 spike=2.76
- AFDI.CA: score=26.94 buy_ready=True sector_rank=12 price=46.42 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=17398476.0 spike=1.47
- AFMC.CA: score=24.0 buy_ready=True sector_rank=12 price=72.69 support=70.97 resistance=70.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=17962236.0 spike=1.0
- AJWA.CA: score=14.86 buy_ready=False sector_rank=12 price=177.2 support=144.0 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=34.21 liquidity=5864457.5 spike=0.22
- ALCN.CA: score=27.2 buy_ready=True sector_rank=4 price=29.08 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=50.15 liquidity=15441307.0 spike=1.4
- ALUM.CA: score=18.92 buy_ready=False sector_rank=12 price=22.89 support=20.55 resistance=25.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=49.4 liquidity=5923762.5 spike=0.73
- AMER.CA: score=12.76 buy_ready=False sector_rank=8 price=3.02 support=2.75 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=181573696.0 spike=2.68
- AMES.CA: score=14.0 buy_ready=False sector_rank=12 price=77.3 support=70.78 resistance=84.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=174367888.0 spike=6.79
- AMIA.CA: score=16.13 buy_ready=False sector_rank=12 price=8.85 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=4131807.5 spike=0.42
- AMOC.CA: score=23.79 buy_ready=False sector_rank=14 price=7.96 support=7.42 resistance=8.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=59.59 liquidity=80997464.0 spike=1.56
- ANFI.CA: score=10.33 buy_ready=False sector_rank=12 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=10.34 buy_ready=False sector_rank=12 price=8.45 support=8.0 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=48.41 liquidity=343856.63 spike=0.37
- ARAB.CA: score=27.86 buy_ready=True sector_rank=8 price=0.23 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=58.18 liquidity=128122952.0 spike=1.73
- ARCC.CA: score=16.74 buy_ready=False sector_rank=13 price=55.21 support=53.0 resistance=58.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=44.73 liquidity=7913122.5 spike=0.35
- AREH.CA: score=24.0 buy_ready=True sector_rank=12 price=1.6 support=1.42 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=20258286.0 spike=0.55
- ARVA.CA: score=14.4 buy_ready=False sector_rank=12 price=10.9 support=10.3 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=2403356.25 spike=0.1
- ASCM.CA: score=22.0 buy_ready=False sector_rank=12 price=58.14 support=54.12 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=19632182.0 spike=0.25
- ASPI.CA: score=22.0 buy_ready=False sector_rank=12 price=0.32 support=0.3 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=12223593.0 spike=0.32
- ATLC.CA: score=15.21 buy_ready=True sector_rank=18 price=5.2 support=4.7 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=1782705.38 spike=0.25
- ATQA.CA: score=17.38 buy_ready=False sector_rank=19 price=9.58 support=9.02 resistance=10.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=6072251.0 spike=0.18
- AXPH.CA: score=15.74 buy_ready=True sector_rank=12 price=1182.27 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=65.94 liquidity=1748443.0 spike=0.57
- BINV.CA: score=16.06 buy_ready=True sector_rank=5 price=48.1 support=44.02 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=1662609.5 spike=0.24
- BIOC.CA: score=21.79 buy_ready=True sector_rank=12 price=73.79 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=54.48 liquidity=3618517.5 spike=1.09
- BTFH.CA: score=21.43 buy_ready=False sector_rank=18 price=3.06 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=49276180.0 spike=0.25
- CAED.CA: score=21.14 buy_ready=True sector_rank=12 price=72.72 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=54.04 liquidity=5108398.5 spike=1.02
- CANA.CA: score=23.22 buy_ready=True sector_rank=10 price=36.7 support=34.5 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=39.38 liquidity=11550920.0 spike=1.0
- CCAP.CA: score=26.4 buy_ready=True sector_rank=5 price=5.17 support=4.65 resistance=5.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=328125024.0 spike=0.47
- CCRS.CA: score=15.52 buy_ready=False sector_rank=12 price=2.36 support=2.18 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=32.2 liquidity=8519937.0 spike=0.68
- CEFM.CA: score=27.29 buy_ready=False sector_rank=12 price=103.16 support=95.75 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=9295465.0 spike=5.13
- CERA.CA: score=28.6 buy_ready=True sector_rank=12 price=1.32 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=44930244.0 spike=2.3
- CFGH.CA: score=5.0 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1494.6 spike=0.32
- CICH.CA: score=14.72 buy_ready=False sector_rank=18 price=11.66 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=3971035.5 spike=1.16
- CIEB.CA: score=18.08 buy_ready=True sector_rank=10 price=24.16 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=50.86 liquidity=1863499.25 spike=0.27
- CIRA.CA: score=21.57 buy_ready=True sector_rank=15 price=29.03 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=68.69 liquidity=12984298.0 spike=0.68
- CLHO.CA: score=21.97 buy_ready=True sector_rank=11 price=16.36 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=59.22 liquidity=7769217.0 spike=0.21
- CNFN.CA: score=22.73 buy_ready=True sector_rank=18 price=4.84 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=7302221.5 spike=0.16
- COMI.CA: score=26.22 buy_ready=True sector_rank=10 price=134.41 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=49.31 liquidity=179778224.0 spike=0.39
- COPR.CA: score=19.54 buy_ready=False sector_rank=12 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=37.29 liquidity=8545371.0 spike=0.36
- COSG.CA: score=26.0 buy_ready=True sector_rank=12 price=1.62 support=1.47 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=28451220.0 spike=0.6
- CPCI.CA: score=11.55 buy_ready=False sector_rank=12 price=399.69 support=354.0 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=75.84 liquidity=554511.69 spike=0.2
- CSAG.CA: score=22.78 buy_ready=True sector_rank=4 price=32.33 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=61.35 liquidity=6382612.0 spike=0.37
- DAPH.CA: score=21.52 buy_ready=True sector_rank=12 price=82.9 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=49.3 liquidity=5521447.0 spike=0.61
- DEIN.CA: score=-1.0 buy_ready=False sector_rank=12 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=17.03 buy_ready=False sector_rank=9 price=26.72 support=23.7 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=72.53 liquidity=2638619.0 spike=0.52
- DSCW.CA: score=14.66 buy_ready=False sector_rank=12 price=1.78 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=9663848.0 spike=0.33
- DTPP.CA: score=23.96 buy_ready=False sector_rank=12 price=207.46 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=88.92 liquidity=46335640.0 spike=1.48
- EALR.CA: score=27.16 buy_ready=True sector_rank=12 price=363.45 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=15982596.0 spike=1.58
- EASB.CA: score=22.52 buy_ready=False sector_rank=12 price=7.01 support=4.87 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=45.15 liquidity=19871592.0 spike=1.26
- EAST.CA: score=14.07 buy_ready=False sector_rank=9 price=37.0 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=60470436.0 spike=1.34
- EBSC.CA: score=19.78 buy_ready=True sector_rank=12 price=1.9 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=3783739.0 spike=0.76
- ECAP.CA: score=13.19 buy_ready=False sector_rank=12 price=32.61 support=30.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=1191263.0 spike=0.12
- EDFM.CA: score=21.56 buy_ready=True sector_rank=12 price=341.52 support=310.2 resistance=344.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=52.76 liquidity=2563294.0 spike=4.51
- EEII.CA: score=24.0 buy_ready=True sector_rank=12 price=2.81 support=2.3 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=20209296.0 spike=0.93
- EFIC.CA: score=3.72 buy_ready=False sector_rank=19 price=180.46 support=180.02 resistance=208.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=15.88 liquidity=1413080.63 spike=0.55
- EFID.CA: score=26.39 buy_ready=True sector_rank=9 price=28.33 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=45761212.0 spike=0.6
- EFIH.CA: score=27.4 buy_ready=True sector_rank=3 price=22.25 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=62.91 liquidity=27130148.0 spike=0.62
- EGAL.CA: score=20.3 buy_ready=False sector_rank=19 price=293.46 support=272.28 resistance=318.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=45.46 liquidity=15437403.0 spike=0.31
- EGAS.CA: score=13.45 buy_ready=False sector_rank=14 price=49.0 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=42.74 liquidity=4780467.5 spike=0.6
- EGBE.CA: score=16.26 buy_ready=False sector_rank=10 price=0.46 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=36715.83 spike=0.56
- EGCH.CA: score=19.88 buy_ready=False sector_rank=19 price=13.0 support=12.13 resistance=14.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=38.61 liquidity=74556856.0 spike=1.79
- EGSA.CA: score=17.06 buy_ready=False sector_rank=1 price=9.11 support=8.62 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=23453.27 spike=2.32
- EGTS.CA: score=26.96 buy_ready=True sector_rank=8 price=18.5 support=15.1 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=82102208.0 spike=1.28
- EHDR.CA: score=24.0 buy_ready=True sector_rank=12 price=2.66 support=2.37 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=40.58 liquidity=34296140.0 spike=0.78
- EKHO.CA: score=10.67 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.76 buy_ready=False sector_rank=17 price=2.1 support=2.04 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=5304410.5 spike=0.34
- ELKA.CA: score=10.64 buy_ready=False sector_rank=12 price=1.53 support=1.42 resistance=1.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=79499312.0 spike=1.82
- ELNA.CA: score=13.33 buy_ready=False sector_rank=12 price=38.35 support=35.55 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=35.49 liquidity=694548.38 spike=1.32
- ELSH.CA: score=24.0 buy_ready=True sector_rank=12 price=13.68 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=47.58 liquidity=127410928.0 spike=0.71
- ELWA.CA: score=9.59 buy_ready=False sector_rank=12 price=1.94 support=1.89 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=598747.31 spike=0.29
- EMFD.CA: score=22.4 buy_ready=False sector_rank=8 price=11.85 support=11.11 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=35.26 liquidity=36644568.0 spike=0.18
- ENGC.CA: score=28.0 buy_ready=True sector_rank=12 price=37.65 support=33.0 resistance=39.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=30620716.0 spike=2.0
- EOSB.CA: score=14.01 buy_ready=False sector_rank=12 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=11715.68 spike=0.12
- EPCO.CA: score=11.07 buy_ready=False sector_rank=12 price=9.01 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=2069011.25 spike=0.31
- EPPK.CA: score=14.31 buy_ready=False sector_rank=12 price=14.16 support=11.72 resistance=15.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=74.03 liquidity=314018.44 spike=0.29
- ETEL.CA: score=29.4 buy_ready=True sector_rank=1 price=98.01 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=27810870.0 spike=0.37
- ETRS.CA: score=24.0 buy_ready=True sector_rank=12 price=10.77 support=8.77 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=57.43 liquidity=36714788.0 spike=0.47
- EXPA.CA: score=21.32 buy_ready=True sector_rank=10 price=18.5 support=18.03 resistance=19.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=41.76 liquidity=31156760.0 spike=1.05
- FAIT.CA: score=21.36 buy_ready=True sector_rank=10 price=37.04 support=35.01 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=4937469.5 spike=2.1
- FAITA.CA: score=9.72 buy_ready=False sector_rank=10 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=52.0 liquidity=36826.02 spike=1.23
- FERC.CA: score=18.16 buy_ready=False sector_rank=19 price=76.18 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=5733890.5 spike=1.56
- FWRY.CA: score=24.4 buy_ready=False sector_rank=3 price=19.24 support=17.71 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=47983484.0 spike=0.22
- GBCO.CA: score=24.4 buy_ready=True sector_rank=7 price=30.83 support=26.62 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=17875724.0 spike=0.2
- GDWA.CA: score=6.18 buy_ready=False sector_rank=12 price=0.77 support=0.76 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=28.72 liquidity=3185984.0 spike=0.22
- GGCC.CA: score=23.0 buy_ready=False sector_rank=12 price=0.56 support=0.4 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=91.88 liquidity=16149624.0 spike=0.98
- GIHD.CA: score=14.0 buy_ready=False sector_rank=12 price=52.06 support=43.0 resistance=52.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=132443312.0 spike=14.17
- GMCI.CA: score=17.55 buy_ready=False sector_rank=12 price=2.09 support=1.66 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=2017686.25 spike=2.27
- GRCA.CA: score=5.87 buy_ready=False sector_rank=12 price=49.45 support=48.75 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=14.64 liquidity=1877304.88 spike=0.56
- GSSC.CA: score=31.0 buy_ready=True sector_rank=12 price=257.08 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=15167496.0 spike=4.0
- GTWL.CA: score=12.86 buy_ready=False sector_rank=12 price=110.28 support=98.02 resistance=115.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=215761760.0 spike=2.93
- HDBK.CA: score=13.22 buy_ready=False sector_rank=10 price=79.47 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=20.35 liquidity=20169852.0 spike=0.52
- HELI.CA: score=14.4 buy_ready=False sector_rank=8 price=7.33 support=6.83 resistance=7.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=565749568.0 spike=4.66
- HRHO.CA: score=19.43 buy_ready=False sector_rank=18 price=26.81 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=48636104.0 spike=0.36
- ICID.CA: score=16.56 buy_ready=True sector_rank=12 price=7.75 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=2566299.25 spike=0.24
- IDRE.CA: score=10.1 buy_ready=False sector_rank=12 price=46.43 support=42.51 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15796568.0 spike=1.55
- IFAP.CA: score=20.18 buy_ready=False sector_rank=16 price=19.56 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=47.09 liquidity=6840495.5 spike=1.4
- INFI.CA: score=27.0 buy_ready=False sector_rank=12 price=97.51 support=88.51 resistance=102.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=40.25 liquidity=29627888.0 spike=4.85
- IRON.CA: score=14.83 buy_ready=False sector_rank=19 price=32.1 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=44.92 liquidity=3528189.0 spike=0.46
- ISMA.CA: score=14.2 buy_ready=False sector_rank=12 price=26.91 support=26.82 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=3.11 liquidity=7208542.0 spike=0.22
- ISMQ.CA: score=20.3 buy_ready=False sector_rank=19 price=9.68 support=7.67 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=56921020.0 spike=0.41
- ISPH.CA: score=19.2 buy_ready=False sector_rank=11 price=11.4 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=25479090.0 spike=0.34
- JUFO.CA: score=23.04 buy_ready=True sector_rank=9 price=30.88 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=51.44 liquidity=8647591.0 spike=0.3
- KABO.CA: score=23.4 buy_ready=False sector_rank=6 price=7.39 support=5.96 resistance=7.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=87.66 liquidity=22489622.0 spike=0.82
- KWIN.CA: score=8.66 buy_ready=False sector_rank=12 price=67.15 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=30.79 liquidity=5667485.0 spike=0.44
- KZPC.CA: score=11.2 buy_ready=False sector_rank=12 price=8.42 support=8.26 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=35.83 liquidity=3199021.25 spike=0.48
- LCSW.CA: score=25.82 buy_ready=True sector_rank=13 price=31.1 support=26.0 resistance=31.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=68.46 liquidity=45959056.0 spike=0.86
- LUTS.CA: score=24.0 buy_ready=True sector_rank=12 price=0.74 support=0.62 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=49.66 liquidity=24771626.0 spike=0.44
- MAAL.CA: score=9.64 buy_ready=False sector_rank=12 price=8.35 support=8.02 resistance=8.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21951334.0 spike=1.32
- MASR.CA: score=26.0 buy_ready=True sector_rank=12 price=7.73 support=6.54 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=58.67 liquidity=62912520.0 spike=0.81
- MBSC.CA: score=20.82 buy_ready=False sector_rank=13 price=243.01 support=222.66 resistance=257.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=40.85 liquidity=15631198.0 spike=0.62
- MCQE.CA: score=20.83 buy_ready=False sector_rank=13 price=179.13 support=166.66 resistance=189.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=52.03 liquidity=8001057.0 spike=0.55
- MCRO.CA: score=25.0 buy_ready=True sector_rank=12 price=1.25 support=1.17 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=27337092.0 spike=0.89
- MENA.CA: score=18.43 buy_ready=True sector_rank=8 price=7.03 support=6.41 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=59.16 liquidity=2029010.25 spike=0.24
- MEPA.CA: score=23.0 buy_ready=False sector_rank=12 price=1.65 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=10495509.0 spike=0.95
- MFPC.CA: score=22.5 buy_ready=False sector_rank=19 price=37.0 support=34.22 resistance=42.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=106017448.0 spike=1.1
- MFSC.CA: score=15.94 buy_ready=False sector_rank=12 price=46.86 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=3945172.0 spike=0.54
- MHOT.CA: score=9.62 buy_ready=False sector_rank=21 price=16.93 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=16905414.0 spike=1.11
- MICH.CA: score=23.54 buy_ready=True sector_rank=12 price=38.0 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=51.51 liquidity=9541079.0 spike=0.59
- MILS.CA: score=22.0 buy_ready=False sector_rank=12 price=133.67 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=29.41 liquidity=48901456.0 spike=5.4
- MIPH.CA: score=17.79 buy_ready=True sector_rank=11 price=689.88 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=59.58 liquidity=1593998.63 spike=0.7
- MOED.CA: score=18.3 buy_ready=False sector_rank=12 price=0.7 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=43.8 liquidity=6299763.5 spike=0.69
- MOIL.CA: score=13.78 buy_ready=False sector_rank=14 price=0.52 support=0.46 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=72.63 liquidity=116132.42 spike=0.41
- MOIN.CA: score=14.95 buy_ready=False sector_rank=12 price=24.05 support=22.6 resistance=25.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=1370380.0 spike=1.79
- MOSC.CA: score=10.15 buy_ready=False sector_rank=12 price=269.75 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=41.71 liquidity=1158337.88 spike=0.13
- MPCI.CA: score=24.0 buy_ready=True sector_rank=12 price=239.71 support=213.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=61.06 liquidity=26471376.0 spike=0.26
- MPCO.CA: score=16.54 buy_ready=False sector_rank=16 price=1.85 support=1.66 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=29704088.0 spike=0.32
- MPRC.CA: score=21.56 buy_ready=False sector_rank=12 price=42.68 support=31.15 resistance=41.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=89.34 liquidity=59321336.0 spike=1.28
- MTIE.CA: score=26.01 buy_ready=True sector_rank=7 price=9.38 support=8.65 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=9613066.0 spike=0.48
- NAHO.CA: score=10.22 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=27985.9 spike=1.1
- NCCW.CA: score=22.0 buy_ready=False sector_rank=12 price=6.2 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=12863486.0 spike=0.45
- NEDA.CA: score=10.9 buy_ready=False sector_rank=12 price=2.74 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=31.58 liquidity=1905448.07 spike=5.71
- NHPS.CA: score=29.0 buy_ready=True sector_rank=12 price=71.61 support=61.55 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=65.33 liquidity=86459864.0 spike=5.82
- NINH.CA: score=14.38 buy_ready=False sector_rank=12 price=17.62 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=47.76 liquidity=5387089.0 spike=0.78
- NIPH.CA: score=26.22 buy_ready=True sector_rank=11 price=177.84 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=64.8 liquidity=96777664.0 spike=1.01
- OBRI.CA: score=26.04 buy_ready=False sector_rank=12 price=35.75 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=68827256.0 spike=2.52
- OCDI.CA: score=21.4 buy_ready=False sector_rank=8 price=26.91 support=20.0 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=81.43 liquidity=48454800.0 spike=0.5
- OCPH.CA: score=15.85 buy_ready=False sector_rank=12 price=354.17 support=337.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=58.42 liquidity=2852004.75 spike=0.44
- ODIN.CA: score=24.75 buy_ready=True sector_rank=12 price=2.34 support=2.01 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=58.18 liquidity=8749410.0 spike=0.64
- OFH.CA: score=26.0 buy_ready=True sector_rank=12 price=0.64 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=17681292.0 spike=0.87
- OIH.CA: score=21.4 buy_ready=False sector_rank=5 price=1.41 support=1.33 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=24696280.0 spike=0.32
- OLFI.CA: score=26.39 buy_ready=True sector_rank=9 price=22.68 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=11587235.0 spike=0.4
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=690.89 support=680.1 resistance=694.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=135159248.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=8 price=39.24 support=35.01 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=86180864.0 spike=0.51
- ORWE.CA: score=19.77 buy_ready=False sector_rank=6 price=22.75 support=21.95 resistance=23.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=7365477.0 spike=0.34
- PHAR.CA: score=17.82 buy_ready=True sector_rank=11 price=86.82 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=1619726.38 spike=0.07
- PHDC.CA: score=17.4 buy_ready=False sector_rank=8 price=14.9 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=21.98 liquidity=134425104.0 spike=0.41
- PHTV.CA: score=10.84 buy_ready=False sector_rank=12 price=291.01 support=273.5 resistance=297.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24397328.0 spike=1.92
- POUL.CA: score=24.39 buy_ready=True sector_rank=9 price=39.41 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=66.8 liquidity=16586138.0 spike=0.42
- PRCL.CA: score=22.82 buy_ready=False sector_rank=13 price=36.16 support=23.75 resistance=36.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=84.32 liquidity=20926108.0 spike=0.4
- PRDC.CA: score=26.4 buy_ready=True sector_rank=8 price=8.35 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=11648288.0 spike=0.08
- PRMH.CA: score=10.54 buy_ready=False sector_rank=12 price=2.55 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=3539152.5 spike=0.13
- RACC.CA: score=20.81 buy_ready=True sector_rank=12 price=10.01 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=57.74 liquidity=4817813.5 spike=0.46
- RAKT.CA: score=11.11 buy_ready=False sector_rank=12 price=22.35 support=21.4 resistance=23.79 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=41.67 liquidity=371568.76 spike=1.37
- RAYA.CA: score=28.56 buy_ready=True sector_rank=2 price=7.94 support=6.7 resistance=8.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=63.3 liquidity=112793000.0 spike=1.08
- RMDA.CA: score=17.41 buy_ready=False sector_rank=11 price=5.0 support=4.81 resistance=5.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=5209122.0 spike=0.07
- ROTO.CA: score=24.0 buy_ready=True sector_rank=12 price=42.0 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=19139396.0 spike=0.6
- RREI.CA: score=28.74 buy_ready=True sector_rank=12 price=3.77 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=58.46 liquidity=23894944.0 spike=1.37
- RTVC.CA: score=12.46 buy_ready=False sector_rank=12 price=3.78 support=3.55 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=1463344.25 spike=0.3
- RUBX.CA: score=21.0 buy_ready=False sector_rank=12 price=13.11 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=78.82 liquidity=23786924.0 spike=0.46
- SAUD.CA: score=15.35 buy_ready=False sector_rank=10 price=21.47 support=19.99 resistance=22.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=40.61 liquidity=2130874.5 spike=0.3
- SCEM.CA: score=22.82 buy_ready=False sector_rank=13 price=62.58 support=59.3 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=10627812.0 spike=0.62
- SCFM.CA: score=14.0 buy_ready=False sector_rank=12 price=255.76 support=243.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28193078.0 spike=6.99
- SCTS.CA: score=19.03 buy_ready=True sector_rank=15 price=615.04 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=3455188.25 spike=0.67
- SDTI.CA: score=13.65 buy_ready=False sector_rank=12 price=46.51 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=1654327.5 spike=0.21
- SEIG.CA: score=26.4 buy_ready=False sector_rank=12 price=248.0 support=180.0 resistance=272.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=96.63 liquidity=34992184.0 spike=2.7
- SIPC.CA: score=15.1 buy_ready=False sector_rank=12 price=3.49 support=3.25 resistance=3.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=47.44 liquidity=2101858.25 spike=0.21
- SKPC.CA: score=22.06 buy_ready=False sector_rank=19 price=16.3 support=15.58 resistance=17.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=52.23 liquidity=45211404.0 spike=1.38
- SMFR.CA: score=13.33 buy_ready=False sector_rank=12 price=202.52 support=187.01 resistance=209.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=49.19 liquidity=332086.19 spike=0.16
- SNFC.CA: score=8.0 buy_ready=False sector_rank=12 price=11.3 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=4001295.75 spike=0.34
- SPIN.CA: score=16.53 buy_ready=False sector_rank=6 price=14.56 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=70.21 liquidity=2131294.5 spike=0.24
- SPMD.CA: score=24.0 buy_ready=True sector_rank=12 price=0.45 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=58.73 liquidity=13531227.0 spike=0.72
- SUGR.CA: score=6.15 buy_ready=False sector_rank=9 price=47.15 support=45.31 resistance=50.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=29.6 liquidity=2762134.75 spike=0.53
- SVCE.CA: score=26.0 buy_ready=True sector_rank=12 price=9.46 support=8.11 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=51.59 liquidity=30657230.0 spike=0.43
- SWDY.CA: score=19.99 buy_ready=True sector_rank=17 price=88.34 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=4535222.0 spike=0.33
- TALM.CA: score=9.64 buy_ready=False sector_rank=15 price=15.42 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=23.53 liquidity=6065131.5 spike=0.55
- TMGH.CA: score=26.4 buy_ready=True sector_rank=8 price=97.02 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=57.6 liquidity=124077248.0 spike=0.34
- TRTO.CA: score=10.0 buy_ready=False sector_rank=12 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=13.56 buy_ready=False sector_rank=12 price=522.72 support=480.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9568085.0 spike=8.66
- UEGC.CA: score=23.0 buy_ready=False sector_rank=12 price=1.75 support=1.33 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=76.36 liquidity=22263860.0 spike=0.87
- UNIP.CA: score=18.99 buy_ready=True sector_rank=12 price=0.33 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=4989600.0 spike=0.25
- UNIT.CA: score=14.4 buy_ready=False sector_rank=8 price=18.8 support=16.64 resistance=19.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107747280.0 spike=10.07
- WCDF.CA: score=11.3 buy_ready=False sector_rank=12 price=523.65 support=450.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-07T21:00:00+00:00 freshness=FRESH RSI=37.43 liquidity=304240.66 spike=0.98
- WKOL.CA: score=21.58 buy_ready=True sector_rank=12 price=314.0 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=5583566.0 spike=0.85
- ZEOT.CA: score=20.85 buy_ready=True sector_rank=12 price=11.06 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=6851372.0 spike=0.18
- ZMID.CA: score=26.4 buy_ready=True sector_rank=8 price=6.83 support=6.03 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=63.95 liquidity=146565168.0 spike=0.7

## Backtesting Lite
- GSSC.CA: 180d return=-1.79%, max drawdown=-19.21%, MA20>MA50 days last20=3, as_of=2026-07-07T21:00:00+00:00
- ETEL.CA: 180d return=93.86%, max drawdown=-30.44%, MA20>MA50 days last20=9, as_of=2026-07-07T21:00:00+00:00
- NHPS.CA: 180d return=8.65%, max drawdown=-40.18%, MA20>MA50 days last20=7, as_of=2026-07-07T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GSSC.CA: status=RECENT_ACCEPTED latest=2026-07-02 age_days=7 sources=3 expected=General Co. For Silos & Storage summary=General Co. For Silos & Storage (GSSC.CA) has shown recent financial activity, including dividend approvals and profit increases. The company approved an EGP 74.37M dividend in November 2025 and reported higher profits in FY2024/25 in October 2025. Its market capitalization was approximately 4.30 billion EGP as of July 2, 2026.
  - General Company for Silos approves EGP 74.37M dividend (November 9, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNqTaJ9_m5Ylr3tMPS3XuXpenxGtgwNvJ5gsVHTQWdkMA6UnBlClT10anTngHXWzvr0Zq4JK5nVW9Z7PURt-mzh0gxvReFWZ_PepwrMV6K2Kbi62J2f77QsEEiVuHleJUHAcng49ukLDTvfQlCTeWVcQ==
  - General Company for Silos records 28.7% YoY higher profits in FY2024/25 (October 13, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNqTaJ9_m5Ylr3tMPS3XuXpenxGtgwNvJ5gsVHTQWdkMA6UnBlClT10anTngHXWzvr0Zq4JK5nVW9Z7PURt-mzh0gxvReFWZ_PepwrMV6K2Kbi62J2f77QsEEiVuHleJUHAcng49ukLDTvfQlCTeWVcQ==
  - General Silos & Storage Co. Market Cap (July 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQJBYKrbDaIQFQOKHVyIT7vc0nfB1hmfuzrImihyONOi9rIdLS47VfAbwqUG5_nJMhtoX2zZEXIrufkQ0oir0JWqUNl_lXB8MybwIR7jk9MZ9OM119LpuPD3dJnJ1oB6kVgP1e2XyL44yPHNBwj2y1C2W5e7eMsXWIWpFCNTyiPfP8YWeC
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-05-21 age_days=49 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) has released its audited financial results for the full year ended December 31, 2025 (February 2026) and for the first quarter ended March 31, 2026 (May 2026). The company also declared cash dividends in April 2026 and had a Central Auditing Organization Report in June 2026. In the last 12 months, Telecom Egypt reported revenue of EGP 110.17 billion and profits of EGP 19.30 billion.
  - FY 2025 Results: Telecom Egypt Delivers Growth Ahead of Expectations (February 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmOU0fdh4SjSu6yszP8jAUNMN069NdjNSV_G_GxFc3w5KNDxkT98lL1vW7flwfq4jd501je0GfkLAOTXekZ_K9XR8omvtyulWGwQM=
  - Q1 2026 Results: Telecom Egypt Reports Strong Underlying Business Performance (May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmOU0fdh4SjSu6yszP8jAUNMN069NdjNSV_G_GxFc3w5KNDxkT98lL1vW7flwfq4jd501je0GfkLAOTXekZ_K9XR8omvtyulWGwQM=
  - Telecom Egypt (ETEL.CA) Declares Cash Dividends (April 27, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpoY848Tnp9eua15zgW0bY8UsaO7XPs4URkQqfkoAz6caN-FpZp3d8cCXmuNhVdZpdX3BKjnlyd7jp3-FU-ArKiub206S4aGUeeHoa_egnjSbmd031HCV5JiCT3Y-DQUxp_BLeV4ywd6MiXDfOjNP8
- NHPS.CA: status=RECENT_ACCEPTED latest=2026-06-09 age_days=30 sources=3 expected=National Company for Housing Professional Syndicates SAE summary=National Company for Housing Professional Syndicates SAE (NHPS.CA) declared cash dividends in June 2026 and had a Central Auditing Organization Report in May 2026. The company's equityholders approved EGP 3.5/share dividends for 2025. NHPS also completed the sale of Le Méridien Heliopolis for EGP 605 million.
  - National Housing for Professional Syndicates (NHPS.CA) Declares Cash Dividends (June 9, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrdoiKwdoXCHvw4Mwft_R1_vre2VBT_OakRBqK6uvEzgSSdTVp8cQyT2a_sQtdSElkEWqD1XlUpHIXJazkMnChUrjEVtXQ05jRTSaxymyFM5s1Ag47D7vGC6CJmD0inWbS-DQndHgSh2O8M3xuqfqd
  - National Housing for Professional Syndicates (NHPS.CA) - Central Auditing Organization Report (May 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrdoiKwdoXCHvw4Mwft_R1_vre2VBT_OakRBqK6uvEzgSSdTVp8cQyT2a_sQtdSElkEWqD1XlUpHIXJazkMnChUrjEVtXQ05jRTSaxymyFM5s1Ag47D7vGC6CJmD0inWbS-DQndHgSh2O8M3xuqfqd
  - NCH El-Watania's equityholders approve EGP 3.5/shr dividends for 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrdoiKwdoXCHvw4Mwft_R1_vre2VBT_OakRBqK6uvEzgSSdTVp8cQyT2a_sQtdSElkEWqD1XlUpHIXJazkMnChUrjEVtXQ05jRTSaxymyFM5s1Ag47D7vGC6CJmD0inWbS-DQndHgSh2O8M3xuqfqd
- RREI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Arab Real Estate Investment Co. summary=Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
- CERA.CA: status=RECENT_ACCEPTED latest=2026-07-02 age_days=7 sources=3 expected=The Arab Ceramic Co. summary=The Arab Ceramic Co. (CERA.CA) reported its 2025 revenue as 2.29 billion EGP, an increase of 21.30% from the previous year, with earnings of 37.57 million EGP. The company's market capitalization was 1.32 billion EGP as of July 2, 2026, showing a 64.87% increase in one year. Recent activities include AGM Minutes and Board of Directors' Decisions in May 2026, and news regarding a stock split.
  - The Arab Ceramic Co. (EGX:CERA) Financial Performance in 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnyK16bJKMZ-zh7WWMMuu_gRQT3e67QWslfGyz2NwP0x7DSMLtH28WJpiwZJADn1z2HqKld2YCDDcz8YGH4GTPeqP11NwN-x58Row3CW6i8O9gbrKcSylwLyQQkv4IjR1tkcg=
  - The Arab Ceramic Co. (EGX:CERA) Market Cap & Net Worth (July 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcD6YxbT5woVPUyFuljcp5uHuTuX6nWeA6Aa045Z7QfjUtr5LC97sPgR6HYU42Qjd2WNuJzOTXSzW0wdAplH9oO0Ac9I4QNk2QEbHtHPrMwb5Reut6cXWjWALIiyX79cBthfzeoCdv8TLNLFcNfA==
  - The Arab Ceramic CO.- Ceramica Remas (CERA.CA) - AGM Minutes (after Certification) (May 24, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHRrCZpgvN2woVF-nMu4Ljm1yPUsShJd44KqZvW72lRVAzIk3pEsBsNUxg7uLh5ZhF-RRrl5hH05tfC8CTNLDqxlkiAJAKYVuh0-7gYLZJWL6PwygJAISC7qjBwdcWBmGHksmB0a79Y-NjSOWUrQpb
- RAYA.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=2 sources=3 expected=Raya Holding summary=Raya Holding (RAYA.CA) reported revenue of EGP 66.76 billion and profits of EGP 2.60 billion in the last 12 months (as of July 2026). The company's FY 2025 revenue increased by 41.47% to EGP 63.83 billion, with earnings up 53.29% to EGP 2.59 billion. Raya Holding also released its Q1 2026 financial results in May 2026 and had Board of Directors' Decisions in July 2026.
  - Raya Holding Company for Financial Investments (S.A.E) (EGX:RAYA) Statistics & Valuation Metrics (July 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNiRlEQZQt0gCc-X01ESpZFAsYUiru0C4CAErSFgbCUCHxBxcV0dEkN2EdanLYQTM7PtYpG-nFnr_uwdsCusBh-3zCdEBfXdYdw0nIqqHpGtX1oag03rLffBlY-YfYqUJeVUYszf4RCLCNGPZeaQ==
  - Raya Holding Company for Financial Investments (SAE) (EGX:RAYA) Financial Performance in 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSYK_MwfjEcv2SP99f4geyXNFK8dnXzVd5zi91bGCDzE5krkM6BlZJT7ksRsKktCTPRMObF_jG1CvFO6WHOAUWypEzM4utPeP5VDUkJUZeNlQTLn7RwnQAlwA9d7ys9JmEpyw=
  - Raya Holding For Financial Investments (RAYA.CA) Reports Its Financial Results (Standalone) for The Period From 01/01/2026 to 31/03/2026 (May 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH5XND_LUzbqWqa5lmImEzgUtA-IAoJFy_ITp3B3yyAJ-4lzNT7j4g_a6SdPEM-MnTwSAFJinmE3AwSRcPKPwFnAAqHeVKYnevejvoB3KnuN2CCvnT0WI_-rH2GMipvBjdlhCmfZTMr179FQUJwBiM
- ENGC.CA: status=RECENT_ACCEPTED latest=2026-03-31 age_days=100 sources=2 expected=Industrial Engineering Company for Construction and Development (ICON) (S.A.E) summary=Industrial Engineering Company for Construction and Development (ICON) (S.A.E) (ENGC.CA) has detailed annual and quarterly financial statements available as of March 31, 2026. The company specializes in manufacturing and trading construction materials, including steel sheets, sandwich panels, and prefabricated buildings.
  - Industrial Engineering Company for Construction and Development (ICON) (S.A.E) (EGX:ENGC) Financials & Income Statement (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHrskV7ud91D9EwNR7vM9vXkPbKXmAXGheOvVUvI17a0xIBXHHm6j6Gz65XkdOhe_UIcyc9kcuoh4JVXE-wFnm9AFXr-uROfko920ORcoJQ59eA6QoW8ec9gDG1WzQy8q0d8hB2tjONA_c7eR9sQ==
  - Industrial Engineering Company for Construction and Development (ICON) (S.A.E) Company Profile: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr6yVOYdTFIQm8saJojSMj27DYuYimVDWi5bvbGxWWKUaWd9FWSybG__oi9pg53h6vVAybrnmP1OtBcB4JFO4VBID5yUUgiO28R9Cq86NS0yrmHSR6oehdIpcszt-7hP8LQD8=
- ARAB.CA: status=RECENT_ACCEPTED latest=2026-04-30 age_days=70 sources=3 expected=Arab Developers Holding summary=Arab Developers Holding (ARAB.CA) reported its 2025 revenue as 1.59 billion EGP and earnings of 96.91 million EGP. The company released its full-year earnings for 2025 in April 2026, showing a consolidated profit of EGP 95.8 million. In November 2025, the board approved an issued capital increase. Recent disclosures include a release regarding a disclosure form in July 2026 and AGM Minutes in June 2026.
  - Arab Developers Holding (EGX:ARAB) Financial Performance in 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJgWxPMxQsS7p5vsgfUHwwTh87FXh2JuWALw45HOzfpSEUYtMKnGsLMYd9lMuoQvPtu3xM1f-peLoKhzAd56RkFCu2MY40TDMPpPsF4_nidB-WMV7ecRqxRLHsd8g19BoT4x8=
  - Arab Developers Holding Reports Earnings Results for the Full Year Ended December 31, 2025 (April 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGPuEKbNYgE3EnD8VWWJL9xezfuDAAM0yzkfQg-Hil1WjPhKVtkyl1tZ1Lg0qxig1m6RYXiMjxMk7EmbV36v-ht0jgsih_KimeR1bVlUYs0d3clt4gOBpDpZr6AqJWVwAzHJYhPBsxLhMGF4EVL1gBrZxsXs_NFVqp2d0E2XRwnMN5T5vw9w==
  - Arab Developers Holding board approves issued capital increase (November 2, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGPuEKbNYgE3EnD8VWWJL9xezfuDAAM0yzkfQg-Hil1WjPhKVtkyl1tZ1Lg0qxig1m6RYXiMjxMk7EmbV36v-ht0jgsih_KimeR1bVlUYs0d3clt4gOBpDpZr6AqJWVwAzHJYhPBsxLhMGF4EVL1gBrZxsXs_NFVqp2d0E2XRwnMN5T5vw9w==

## Warnings
- Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
