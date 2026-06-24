# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-24T10:48:26.637637+00:00
Generated Cairo: 2026-06-24 13:48
Run timing: target 11:00 Cairo | generated Cairo 2026-06-24 13:48 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-24 13:44

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 45
- Data quality issues: 0
- Tradeable price/liquidity tickers: 185/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, June 24
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 42.11% / above MA50 47.37%
- EGX70 regime: MIXED / above MA20 56.41% / above MA50 71.79%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- ZMID.CA: liquidity=398957728.0 spike=2.06 score=29.98
- COMI.CA: liquidity=315133856.0 spike=0.53 score=20.15
- CCAP.CA: liquidity=249944768.0 spike=0.34 score=21.34
- OCDI.CA: liquidity=216000384.0 spike=5.35 score=13.86
- ISMQ.CA: liquidity=181434048.0 spike=2.4 score=9.13

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlighted three BUY‑ready tickets—GIHD.CA, CLHO.CA and ZMID.CA—based on strong liquidity spikes, price above the 20‑ and 50‑day moving averages, and bullish outlook scores. All three sit near their 20‑day support levels with modest distance to resistance, but the EGX30 is in a bearish regime while the broader EGX70 remains mixed, prompting a selective swing‑trade risk mode and higher uncertainty for the next 1‑3 days.
- GIHD.CA: price 44.75 ¢, RSI 61, support 35.15 ¢, resistance 47 ¢; liquidity spike 4.86×; sector lagging, far above support.
- CLHO.CA: price 16.54 ¢, RSI 53.9, support 14.25 ¢, resistance 17 ¢; liquidity spike 2.24×; healthcare sector showing solid breadth.
- ZMID.CA: price 6.60 ¢, RSI 65, support 5.82 ¢, resistance 6.55 ¢; liquidity spike 2.06×; momentum extended, real‑estate sector weak.
- EGX30 trend bearish, EGX70 mixed → risk mode SELECTIVE_SWING_TRADES_ONLY; expect tighter risk controls.
- Outlook 1‑3 days remains uncertain; monitor price action on Thndr before confirming swing entries.

## Top Liquidity Spikes
- GTWL.CA: spike=8.7 liquidity=56018516.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPIN.CA: spike=8.29 liquidity=37681460.0 outlook=NEUTRAL score=42.66 buy_ready=False
- OCDI.CA: spike=5.35 liquidity=216000384.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GIHD.CA: spike=4.86 liquidity=28282692.0 outlook=BULLISH_WATCH score=89.89 buy_ready=True
- MPRC.CA: spike=3.89 liquidity=112407376.0 outlook=CONSTRUCTIVE score=59.89 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=17.05 5d=18.31% 20d=15.49% aboveMA50=100.0%
- #2 Automotive & Distribution: score=8.37 5d=3.97% 20d=8.41% aboveMA50=100.0%
- #3 Technology & Distribution: score=7.43 5d=1.28% 20d=-5.08% aboveMA50=100.0%
- #4 Healthcare: score=7.14 5d=2.23% 20d=3.04% aboveMA50=100.0%
- #5 Education: score=5.58 5d=-1.36% 20d=3.03% aboveMA50=66.67%
- #6 Telecommunications: score=5.17 5d=1.27% 20d=-1.83% aboveMA50=100.0%
- #7 Non-bank Financial Services: score=5.11 5d=1.67% 20d=1.05% aboveMA50=60.0%
- #8 Food, Beverages & Tobacco: score=4.96 5d=0.09% 20d=2.32% aboveMA50=71.43%

## Today's Prioritized Action Tickets
- Priority #1: BUY GIHD.CA
  - Entry: 44.75 | Take profit: 48.33 | Stop loss: 42.96
  - Confidence: LOW | score=32.56 | outlook=BULLISH_WATCH 89.89
  - Reason: BUY SETUP: GIHD.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 61.04, support 35.15, resistance 47.0, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY CLHO.CA
  - Entry: 16.54 | Take profit: 17.86 | Stop loss: 15.88
  - Confidence: LOW | score=30.88 | outlook=BULLISH_WATCH 96.14
  - Reason: BUY SETUP: CLHO.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 53.85, support 14.25, resistance 17.0, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY ZMID.CA
  - Entry: 6.6 | Take profit: 7.12 | Stop loss: 6.34
  - Confidence: LOW | score=29.98 | outlook=BULLISH_WATCH 80.66
  - Reason: BUY SETUP: ZMID.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.96, support 5.82, resistance 6.55, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- RAYA.CA: BULLISH_WATCH score=98.43 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- CLHO.CA: BULLISH_WATCH score=96.14 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- TALM.CA: BULLISH_WATCH score=92.58 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- GIHD.CA: BULLISH_WATCH score=89.89 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- MHOT.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- DAPH.CA: BULLISH_WATCH score=85.89 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NIPH.CA: BULLISH_WATCH score=83.14 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- POUL.CA: BULLISH_WATCH score=82.96 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- ATLC.CA: BULLISH_WATCH score=81.11 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=80.66 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- GIHD.CA: rank=32.56 outlook=BULLISH_WATCH outlook_score=89.89 sector_rank=13 price=44.75 support=35.15 resistance=47.0 liquidity=28282692.0
- CLHO.CA: rank=30.88 outlook=BULLISH_WATCH outlook_score=96.14 sector_rank=4 price=16.54 support=14.25 resistance=17.0 liquidity=65154704.0
- POUL.CA: rank=30.8 outlook=BULLISH_WATCH outlook_score=82.96 sector_rank=8 price=39.37 support=34.99 resistance=39.5 liquidity=90359232.0
- ZMID.CA: rank=29.98 outlook=BULLISH_WATCH outlook_score=80.66 sector_rank=10 price=6.6 support=5.82 resistance=6.55 liquidity=398957728.0
- MHOT.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=86 sector_rank=1 price=35.21 support=28.83 resistance=38.38 liquidity=10778351.0
- DAPH.CA: rank=26.7 outlook=BULLISH_WATCH outlook_score=85.89 sector_rank=13 price=82.58 support=76.6 resistance=82.5 liquidity=12181920.0
- ISPH.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=77.14 sector_rank=4 price=12.3 support=11.3 resistance=12.74 liquidity=21416682.0
- PHAR.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=71.14 sector_rank=4 price=88.47 support=83.02 resistance=89.99 liquidity=11021183.0
- CIRA.CA: rank=26.25 outlook=BULLISH_WATCH outlook_score=72.58 sector_rank=5 price=28.7 support=25.23 resistance=31.0 liquidity=18983922.0
- PRDC.CA: rank=26.22 outlook=CONSTRUCTIVE outlook_score=62.66 sector_rank=10 price=7.25 support=5.7 resistance=9.0 liquidity=124614384.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.16 buy_ready=False sector_rank=13 price=206.45 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=606105.0 spike=0.1
- ABUK.CA: score=11.71 buy_ready=False sector_rank=21 price=70.0 support=68.01 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=6.56 liquidity=172911680.0 spike=1.19
- ACAMD.CA: score=21.56 buy_ready=False sector_rank=13 price=2.23 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=79103392.0 spike=0.63
- ACGC.CA: score=21.06 buy_ready=False sector_rank=17 price=9.56 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=36.27 liquidity=26450530.0 spike=0.47
- ADCI.CA: score=23.34 buy_ready=False sector_rank=13 price=242.0 support=211.0 resistance=242.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=93.25 liquidity=11664471.0 spike=1.39
- ADIB.CA: score=18.15 buy_ready=False sector_rank=15 price=45.78 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=44.42 liquidity=59632628.0 spike=0.59
- ADPC.CA: score=15.62 buy_ready=False sector_rank=13 price=3.63 support=3.45 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=5062267.0 spike=0.19
- AFDI.CA: score=25.71 buy_ready=True sector_rank=13 price=46.53 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=51.12 liquidity=8152405.0 spike=0.56
- AFMC.CA: score=8.94 buy_ready=False sector_rank=13 price=69.62 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=37.38 liquidity=380721.13 spike=0.11
- AJWA.CA: score=15.76 buy_ready=False sector_rank=13 price=177.17 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=84.31 liquidity=5200490.5 spike=0.19
- ALCN.CA: score=6.15 buy_ready=False sector_rank=16 price=28.11 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=33.42 liquidity=3008031.0 spike=0.22
- ALUM.CA: score=9.81 buy_ready=False sector_rank=13 price=22.7 support=22.81 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=33.63 liquidity=6251896.0 spike=0.61
- AMER.CA: score=13.86 buy_ready=False sector_rank=10 price=2.42 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=25.84 liquidity=47698092.0 spike=0.55
- AMES.CA: score=8.67 buy_ready=False sector_rank=13 price=48.24 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=36.38 liquidity=1111395.13 spike=0.33
- AMIA.CA: score=13.17 buy_ready=False sector_rank=13 price=8.72 support=8.55 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=41.55 liquidity=1611359.88 spike=0.12
- AMOC.CA: score=13.86 buy_ready=False sector_rank=9 price=7.66 support=7.58 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=14.41 liquidity=22417502.0 spike=0.36
- ANFI.CA: score=18.89 buy_ready=True sector_rank=13 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=3.07 buy_ready=False sector_rank=13 price=8.56 support=8.24 resistance=9.21 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=11.11 liquidity=509508.34 spike=0.92
- ARAB.CA: score=18.86 buy_ready=False sector_rank=10 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=27258082.0 spike=0.32
- ARCC.CA: score=15.58 buy_ready=False sector_rank=19 price=55.97 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=23.35 liquidity=26336770.0 spike=0.77
- AREH.CA: score=23.58 buy_ready=True sector_rank=13 price=1.63 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=31072566.0 spike=1.01
- ARVA.CA: score=18.85 buy_ready=True sector_rank=13 price=11.04 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=59.13 liquidity=5289203.5 spike=0.16
- ASCM.CA: score=23.24 buy_ready=False sector_rank=13 price=61.67 support=47.45 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=75.5 liquidity=110249752.0 spike=1.34
- ASPI.CA: score=23.56 buy_ready=True sector_rank=13 price=0.32 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=17298660.0 spike=0.24
- ATLC.CA: score=19.62 buy_ready=True sector_rank=7 price=5.12 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=57.24 liquidity=3576763.75 spike=0.61
- ATQA.CA: score=10.33 buy_ready=False sector_rank=21 price=9.41 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=22977802.0 spike=0.73
- AXPH.CA: score=13.86 buy_ready=False sector_rank=13 price=1119.75 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=301218.09 spike=0.19
- BINV.CA: score=14.19 buy_ready=False sector_rank=14 price=47.24 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=52.09 liquidity=851307.06 spike=0.08
- BIOC.CA: score=12.49 buy_ready=False sector_rank=13 price=71.83 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=51.74 liquidity=931425.5 spike=0.37
- BTFH.CA: score=18.04 buy_ready=False sector_rank=7 price=3.02 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=76793928.0 spike=0.39
- CAED.CA: score=13.09 buy_ready=False sector_rank=13 price=70.3 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=49.85 liquidity=1534875.0 spike=0.27
- CANA.CA: score=22.85 buy_ready=False sector_rank=15 price=36.14 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=51.92 liquidity=13183533.0 spike=1.35
- CCAP.CA: score=21.34 buy_ready=False sector_rank=14 price=5.03 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=249944768.0 spike=0.34
- CCRS.CA: score=14.84 buy_ready=False sector_rank=13 price=2.39 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=3281547.0 spike=0.15
- CEFM.CA: score=4.43 buy_ready=False sector_rank=13 price=101.37 support=100.53 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=28.56 liquidity=873534.5 spike=0.37
- CERA.CA: score=22.0 buy_ready=True sector_rank=13 price=1.24 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=7443344.5 spike=0.5
- CFGH.CA: score=2.56 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1497.53 spike=0.26
- CICH.CA: score=13.54 buy_ready=False sector_rank=7 price=12.01 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=1500183.88 spike=0.42
- CIEB.CA: score=22.54 buy_ready=True sector_rank=15 price=24.1 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=5385022.0 spike=0.79
- CIRA.CA: score=26.25 buy_ready=True sector_rank=5 price=28.7 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=18983922.0 spike=1.01
- CLHO.CA: score=30.88 buy_ready=True sector_rank=4 price=16.54 support=14.25 resistance=17.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=65154704.0 spike=2.24
- CNFN.CA: score=27.86 buy_ready=False sector_rank=7 price=5.0 support=4.36 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=73.13 liquidity=67617048.0 spike=1.91
- COMI.CA: score=20.15 buy_ready=False sector_rank=15 price=132.43 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=54.25 liquidity=315133856.0 spike=0.53
- COPR.CA: score=20.56 buy_ready=False sector_rank=13 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=11129637.0 spike=0.28
- COSG.CA: score=19.43 buy_ready=False sector_rank=13 price=1.54 support=1.53 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=7878264.5 spike=0.13
- CPCI.CA: score=11.9 buy_ready=False sector_rank=13 price=375.84 support=347.11 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=1345365.13 spike=0.67
- CSAG.CA: score=23.14 buy_ready=True sector_rank=16 price=31.63 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=11085694.0 spike=0.99
- DAPH.CA: score=26.7 buy_ready=True sector_rank=13 price=82.58 support=76.6 resistance=82.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=12181920.0 spike=1.57
- DEIN.CA: score=9.56 buy_ready=False sector_rank=13 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=20.94 buy_ready=False sector_rank=8 price=27.47 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=74.05 liquidity=4291794.5 spike=1.33
- DSCW.CA: score=19.56 buy_ready=False sector_rank=13 price=1.8 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=18956934.0 spike=0.39
- DTPP.CA: score=4.4 buy_ready=False sector_rank=13 price=117.18 support=114.0 resistance=130.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=11.41 liquidity=840354.0 spike=0.46
- EALR.CA: score=12.1 buy_ready=False sector_rank=13 price=355.47 support=350.2 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=539280.19 spike=0.16
- EASB.CA: score=21.1 buy_ready=False sector_rank=13 price=7.15 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=82.31 liquidity=10069010.0 spike=1.27
- EAST.CA: score=23.98 buy_ready=True sector_rank=8 price=39.24 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=51.91 liquidity=31492058.0 spike=0.69
- EBSC.CA: score=14.28 buy_ready=False sector_rank=13 price=1.82 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=719454.88 spike=0.26
- ECAP.CA: score=18.55 buy_ready=False sector_rank=13 price=32.92 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=70.87 liquidity=4997318.0 spike=0.78
- EDFM.CA: score=6.63 buy_ready=False sector_rank=13 price=332.0 support=322.11 resistance=355.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=16.43 liquidity=76692.0 spike=0.15
- EEII.CA: score=19.96 buy_ready=True sector_rank=13 price=2.41 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=4408430.0 spike=0.3
- EFIC.CA: score=0.73 buy_ready=False sector_rank=21 price=198.07 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=17.89 liquidity=405969.63 spike=0.19
- EFID.CA: score=13.98 buy_ready=False sector_rank=8 price=27.49 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=31.48 liquidity=16774947.0 spike=0.22
- EFIH.CA: score=15.56 buy_ready=False sector_rank=20 price=21.0 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=38.99 liquidity=9074127.0 spike=0.18
- EGAL.CA: score=11.33 buy_ready=False sector_rank=21 price=283.02 support=286.11 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=11.25 liquidity=35956188.0 spike=0.47
- EGAS.CA: score=20.19 buy_ready=True sector_rank=9 price=51.01 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=6326833.0 spike=0.52
- EGBE.CA: score=11.16 buy_ready=False sector_rank=15 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=10478.46 spike=0.11
- EGCH.CA: score=11.33 buy_ready=False sector_rank=21 price=13.0 support=12.8 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=20.74 liquidity=12780315.0 spike=0.19
- EGSA.CA: score=7.07 buy_ready=False sector_rank=6 price=8.78 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=2247.68 spike=0.28
- EGTS.CA: score=16.86 buy_ready=False sector_rank=10 price=17.62 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=33.94 liquidity=12713176.0 spike=0.11
- EHDR.CA: score=21.56 buy_ready=False sector_rank=13 price=2.57 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=10871192.0 spike=0.19
- EKHO.CA: score=13.86 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.09 buy_ready=False sector_rank=12 price=2.11 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9443770.0 spike=0.42
- ELKA.CA: score=19.81 buy_ready=False sector_rank=13 price=1.24 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=9257453.0 spike=0.23
- ELNA.CA: score=9.52 buy_ready=False sector_rank=13 price=37.77 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=44.89 liquidity=680675.94 spike=1.64
- ELSH.CA: score=23.56 buy_ready=True sector_rank=13 price=12.0 support=8.31 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=51.24 liquidity=40276016.0 spike=0.21
- ELWA.CA: score=12.4 buy_ready=False sector_rank=13 price=2.06 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=841448.25 spike=0.26
- EMFD.CA: score=21.86 buy_ready=False sector_rank=10 price=11.6 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=48.8 liquidity=50751620.0 spike=0.18
- ENGC.CA: score=17.21 buy_ready=True sector_rank=13 price=36.23 support=32.81 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=67.22 liquidity=3649248.5 spike=0.26
- EOSB.CA: score=15.64 buy_ready=False sector_rank=13 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=86582.96 spike=0.7
- EPCO.CA: score=11.88 buy_ready=False sector_rank=13 price=9.03 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=3319748.5 spike=0.35
- EPPK.CA: score=12.97 buy_ready=False sector_rank=13 price=12.52 support=11.67 resistance=13.12 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=52.26 liquidity=415463.7 spike=0.5
- ETEL.CA: score=24.07 buy_ready=True sector_rank=6 price=94.81 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=41.29 liquidity=34641928.0 spike=0.43
- ETRS.CA: score=21.4 buy_ready=True sector_rank=13 price=10.29 support=7.93 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=65.81 liquidity=7845217.0 spike=0.13
- EXPA.CA: score=18.15 buy_ready=False sector_rank=15 price=18.26 support=18.21 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=18550332.0 spike=0.56
- FAIT.CA: score=12.45 buy_ready=False sector_rank=15 price=36.31 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=1300281.38 spike=0.34
- FAITA.CA: score=11.16 buy_ready=False sector_rank=15 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=8417.5 spike=0.22
- FERC.CA: score=11.68 buy_ready=False sector_rank=21 price=75.12 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=43.52 liquidity=4215282.0 spike=1.07
- FWRY.CA: score=13.48 buy_ready=False sector_rank=20 price=18.97 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=34.23 liquidity=31169072.0 spike=0.11
- GBCO.CA: score=25.4 buy_ready=False sector_rank=2 price=31.46 support=25.25 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=86.15 liquidity=36112332.0 spike=0.35
- GDWA.CA: score=13.19 buy_ready=False sector_rank=13 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=45.11 liquidity=5632872.0 spike=0.4
- GGCC.CA: score=17.7 buy_ready=True sector_rank=13 price=0.42 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=3144726.0 spike=0.39
- GIHD.CA: score=32.56 buy_ready=True sector_rank=13 price=44.75 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=28282692.0 spike=4.86
- GMCI.CA: score=8.94 buy_ready=False sector_rank=13 price=1.71 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=448782.67 spike=1.47
- GRCA.CA: score=5.18 buy_ready=False sector_rank=13 price=53.3 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=1628809.5 spike=0.31
- GSSC.CA: score=12.04 buy_ready=False sector_rank=13 price=249.34 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=38.36 liquidity=1484713.25 spike=0.37
- GTWL.CA: score=13.56 buy_ready=False sector_rank=13 price=57.58 support=49.37 resistance=57.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56018516.0 spike=8.7
- HDBK.CA: score=23.85 buy_ready=False sector_rank=15 price=163.56 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=78.35 liquidity=44359836.0 spike=1.85
- HELI.CA: score=23.86 buy_ready=True sector_rank=10 price=6.54 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=44.08 liquidity=104432656.0 spike=0.76
- HRHO.CA: score=22.04 buy_ready=False sector_rank=7 price=27.04 support=25.8 resistance=27.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=39973836.0 spike=0.28
- ICID.CA: score=19.42 buy_ready=False sector_rank=13 price=7.44 support=5.0 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=77.09 liquidity=8864940.0 spike=0.55
- IDRE.CA: score=15.96 buy_ready=False sector_rank=13 price=44.38 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=4408858.5 spike=0.26
- IFAP.CA: score=4.34 buy_ready=False sector_rank=11 price=19.09 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=31.95 liquidity=1639594.0 spike=0.26
- INFI.CA: score=4.17 buy_ready=False sector_rank=13 price=94.09 support=93.0 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=15.58 liquidity=1613108.13 spike=0.19
- IRON.CA: score=4.38 buy_ready=False sector_rank=21 price=31.77 support=31.0 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=26.16 liquidity=4056137.5 spike=0.51
- ISMA.CA: score=18.44 buy_ready=False sector_rank=13 price=29.55 support=25.79 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=73.58 liquidity=6879867.5 spike=0.17
- ISMQ.CA: score=9.13 buy_ready=False sector_rank=21 price=8.72 support=8.1 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=181434048.0 spike=2.4
- ISPH.CA: score=26.4 buy_ready=True sector_rank=4 price=12.3 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=21416682.0 spike=0.17
- JUFO.CA: score=25.98 buy_ready=True sector_rank=8 price=30.82 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=62.06 liquidity=14102764.0 spike=0.34
- KABO.CA: score=16.06 buy_ready=False sector_rank=17 price=6.21 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=12907966.0 spike=0.7
- KWIN.CA: score=11.86 buy_ready=False sector_rank=13 price=66.26 support=66.1 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=4308057.5 spike=0.67
- KZPC.CA: score=14.48 buy_ready=False sector_rank=13 price=10.55 support=10.34 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=47.41 liquidity=2924739.75 spike=0.43
- LCSW.CA: score=20.66 buy_ready=True sector_rank=19 price=27.44 support=26.0 resistance=28.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=54.16 liquidity=6086470.0 spike=0.6
- LUTS.CA: score=23.56 buy_ready=False sector_rank=13 price=0.74 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=72.96 liquidity=26348436.0 spike=0.63
- MAAL.CA: score=22.74 buy_ready=False sector_rank=13 price=6.91 support=5.16 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=79.1 liquidity=30415586.0 spike=2.09
- MASR.CA: score=25.56 buy_ready=True sector_rank=13 price=7.09 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=52.49 liquidity=35031640.0 spike=0.63
- MBSC.CA: score=14.73 buy_ready=False sector_rank=19 price=243.44 support=243.0 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=36.19 liquidity=7153722.0 spike=0.16
- MCQE.CA: score=5.95 buy_ready=False sector_rank=19 price=172.07 support=171.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=19.3 liquidity=3369343.25 spike=0.21
- MCRO.CA: score=12.56 buy_ready=False sector_rank=13 price=1.22 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=16226698.0 spike=0.38
- MENA.CA: score=9.87 buy_ready=False sector_rank=10 price=6.73 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=32.08 liquidity=1001210.81 spike=0.06
- MEPA.CA: score=14.1 buy_ready=False sector_rank=13 price=1.61 support=1.62 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=6545342.0 spike=0.47
- MFPC.CA: score=11.33 buy_ready=False sector_rank=21 price=36.17 support=35.15 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=4.07 liquidity=84334784.0 spike=0.95
- MFSC.CA: score=16.84 buy_ready=True sector_rank=13 price=49.2 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=58.36 liquidity=3285693.75 spike=0.27
- MHOT.CA: score=29.4 buy_ready=True sector_rank=1 price=35.21 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=66.46 liquidity=10778351.0 spike=0.42
- MICH.CA: score=25.56 buy_ready=True sector_rank=13 price=38.53 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=62.39 liquidity=11318899.0 spike=0.75
- MILS.CA: score=18.07 buy_ready=False sector_rank=13 price=133.02 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=6514095.5 spike=0.47
- MIPH.CA: score=13.72 buy_ready=False sector_rank=4 price=661.85 support=651.0 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=52.48 liquidity=1318605.75 spike=0.59
- MOED.CA: score=12.36 buy_ready=False sector_rank=13 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=2806149.5 spike=0.25
- MOIL.CA: score=15.94 buy_ready=False sector_rank=9 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=71762.77 spike=0.43
- MOIN.CA: score=2.7 buy_ready=False sector_rank=13 price=23.51 support=23.2 resistance=25.66 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=12.26 liquidity=139414.3 spike=0.23
- MOSC.CA: score=12.74 buy_ready=False sector_rank=13 price=270.81 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=46.96 liquidity=1185020.63 spike=0.14
- MPCI.CA: score=24.34 buy_ready=False sector_rank=13 price=245.37 support=204.36 resistance=253.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=75.08 liquidity=169126416.0 spike=1.89
- MPCO.CA: score=23.7 buy_ready=True sector_rank=11 price=1.85 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=65.43 liquidity=52268368.0 spike=0.51
- MPRC.CA: score=30.56 buy_ready=False sector_rank=13 price=36.7 support=31.1 resistance=36.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=72.53 liquidity=112407376.0 spike=3.89
- MTIE.CA: score=21.8 buy_ready=False sector_rank=2 price=8.96 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=7402192.5 spike=0.45
- NAHO.CA: score=7.56 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=8410.06 spike=0.42
- NCCW.CA: score=23.56 buy_ready=False sector_rank=13 price=6.42 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=73.75 liquidity=10306645.0 spike=0.32
- NEDA.CA: score=8.87 buy_ready=False sector_rank=13 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=318130.41 spike=0.72
- NHPS.CA: score=12.36 buy_ready=False sector_rank=13 price=66.98 support=65.03 resistance=71.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=41.25 liquidity=2807392.25 spike=0.65
- NINH.CA: score=14.0 buy_ready=False sector_rank=13 price=17.81 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=44.05 liquidity=3448843.5 spike=0.68
- NIPH.CA: score=24.4 buy_ready=True sector_rank=4 price=165.14 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=41602584.0 spike=0.55
- OBRI.CA: score=13.99 buy_ready=False sector_rank=13 price=34.64 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=3433409.5 spike=0.25
- OCDI.CA: score=13.86 buy_ready=False sector_rank=10 price=24.0 support=22.86 resistance=24.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=216000384.0 spike=5.35
- OCPH.CA: score=12.02 buy_ready=False sector_rank=13 price=346.38 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=44.61 liquidity=3462345.75 spike=0.55
- ODIN.CA: score=15.75 buy_ready=False sector_rank=13 price=2.08 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=2190166.0 spike=0.2
- OFH.CA: score=12.56 buy_ready=False sector_rank=13 price=0.6 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=26.25 liquidity=16103695.0 spike=0.77
- OIH.CA: score=20.34 buy_ready=False sector_rank=14 price=1.41 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=72375344.0 spike=0.83
- OLFI.CA: score=21.92 buy_ready=False sector_rank=8 price=21.87 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=7932628.5 spike=0.4
- ORAS.CA: score=7.6 buy_ready=False sector_rank=18 price=794.01 support=783.0 resistance=795.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=148255728.0 spike=1.0
- ORHD.CA: score=23.86 buy_ready=True sector_rank=10 price=39.43 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=98765304.0 spike=0.53
- ORWE.CA: score=20.92 buy_ready=False sector_rank=17 price=22.85 support=22.65 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=9860279.0 spike=0.25
- PHAR.CA: score=26.4 buy_ready=True sector_rank=4 price=88.47 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=11021183.0 spike=0.31
- PHDC.CA: score=23.86 buy_ready=True sector_rank=10 price=15.48 support=14.43 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=98097512.0 spike=0.23
- PHTV.CA: score=23.6 buy_ready=False sector_rank=13 price=251.0 support=201.55 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=84.24 liquidity=28654874.0 spike=1.52
- POUL.CA: score=30.8 buy_ready=True sector_rank=8 price=39.37 support=34.99 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=61.33 liquidity=90359232.0 spike=2.41
- PRCL.CA: score=9.78 buy_ready=False sector_rank=19 price=29.69 support=28.92 resistance=31.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70764384.0 spike=2.1
- PRDC.CA: score=26.22 buy_ready=True sector_rank=10 price=7.25 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=124614384.0 spike=1.18
- PRMH.CA: score=22.0 buy_ready=False sector_rank=13 price=2.58 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=55.93 liquidity=34599044.0 spike=1.22
- RACC.CA: score=19.01 buy_ready=True sector_rank=13 price=9.89 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=46.32 liquidity=5457254.0 spike=0.55
- RAKT.CA: score=9.35 buy_ready=False sector_rank=13 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=37.86 liquidity=391159.87 spike=1.7
- RAYA.CA: score=25.98 buy_ready=True sector_rank=3 price=7.38 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=110363720.0 spike=1.29
- RMDA.CA: score=22.4 buy_ready=False sector_rank=4 price=5.01 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=21657420.0 spike=0.26
- ROTO.CA: score=20.56 buy_ready=False sector_rank=13 price=42.0 support=32.76 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=82.18 liquidity=10098705.0 spike=0.37
- RREI.CA: score=15.93 buy_ready=False sector_rank=13 price=3.5 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=37.97 liquidity=5371932.0 spike=0.27
- RTVC.CA: score=11.56 buy_ready=False sector_rank=13 price=3.83 support=3.76 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=1008678.0 spike=0.21
- RUBX.CA: score=16.7 buy_ready=False sector_rank=13 price=10.38 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=50.28 liquidity=4145749.5 spike=0.38
- SAUD.CA: score=4.49 buy_ready=False sector_rank=15 price=21.26 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=34.35 liquidity=1340968.5 spike=0.14
- SCEM.CA: score=13.28 buy_ready=False sector_rank=19 price=62.1 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=27.56 liquidity=25384850.0 spike=1.35
- SCFM.CA: score=6.02 buy_ready=False sector_rank=13 price=244.1 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=21.0 liquidity=2464729.75 spike=0.32
- SCTS.CA: score=5.1 buy_ready=False sector_rank=5 price=586.28 support=565.25 resistance=645.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=866784.38 spike=0.21
- SDTI.CA: score=16.73 buy_ready=True sector_rank=13 price=46.83 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=55.69 liquidity=3171667.25 spike=0.24
- SEIG.CA: score=9.08 buy_ready=False sector_rank=13 price=186.45 support=178.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=25.31 liquidity=520995.03 spike=0.12
- SIPC.CA: score=10.79 buy_ready=False sector_rank=13 price=3.44 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=35.19 liquidity=2230530.75 spike=0.18
- SKPC.CA: score=10.33 buy_ready=False sector_rank=21 price=16.12 support=16.01 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=23050912.0 spike=0.52
- SMFR.CA: score=8.88 buy_ready=False sector_rank=13 price=199.09 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=320676.69 spike=0.12
- SNFC.CA: score=15.32 buy_ready=False sector_rank=13 price=11.93 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=44.51 liquidity=3765918.25 spike=0.15
- SPIN.CA: score=20.06 buy_ready=False sector_rank=17 price=14.2 support=13.3 resistance=14.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=24.78 liquidity=37681460.0 spike=8.29
- SPMD.CA: score=25.56 buy_ready=True sector_rank=13 price=0.44 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=54.67 liquidity=15983064.0 spike=0.59
- SUGR.CA: score=6.33 buy_ready=False sector_rank=8 price=47.35 support=47.6 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=22.87 liquidity=3346197.75 spike=0.35
- SVCE.CA: score=23.56 buy_ready=True sector_rank=13 price=9.28 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=56999352.0 spike=0.74
- SWDY.CA: score=22.61 buy_ready=True sector_rank=12 price=87.44 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=8960486.0 spike=0.5
- TALM.CA: score=25.91 buy_ready=True sector_rank=5 price=15.98 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=14109126.0 spike=1.84
- TMGH.CA: score=23.86 buy_ready=True sector_rank=10 price=95.88 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=180298320.0 spike=0.37
- TRTO.CA: score=9.56 buy_ready=False sector_rank=13 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=326.64 spike=0.46
- UEFM.CA: score=15.04 buy_ready=False sector_rank=13 price=483.2 support=465.01 resistance=490.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=55.92 liquidity=480926.81 spike=0.61
- UEGC.CA: score=19.23 buy_ready=False sector_rank=13 price=1.4 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=5669990.0 spike=0.23
- UNIP.CA: score=19.62 buy_ready=False sector_rank=13 price=0.32 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=6064658.0 spike=0.25
- UNIT.CA: score=8.7 buy_ready=False sector_rank=10 price=13.1 support=12.92 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=30.42 liquidity=1837119.5 spike=0.26
- WCDF.CA: score=8.73 buy_ready=False sector_rank=13 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=44.29 liquidity=172883.75 spike=0.7
- WKOL.CA: score=8.87 buy_ready=False sector_rank=13 price=287.83 support=287.66 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=36.68 liquidity=309464.91 spike=0.1
- ZEOT.CA: score=21.46 buy_ready=False sector_rank=13 price=11.66 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=80.14 liquidity=32606602.0 spike=1.45
- ZMID.CA: score=29.98 buy_ready=True sector_rank=10 price=6.6 support=5.82 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=64.96 liquidity=398957728.0 spike=2.06

## Backtesting Lite
- GIHD.CA: 180d return=3.78%, max drawdown=-35.06%, MA20>MA50 days last20=20, as_of=2026-06-22T21:00:00+00:00
- CLHO.CA: 180d return=45.91%, max drawdown=-14.16%, MA20>MA50 days last20=20, as_of=2026-06-22T21:00:00+00:00
- POUL.CA: 180d return=73.38%, max drawdown=-14.26%, MA20>MA50 days last20=20, as_of=2026-06-22T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GIHD.CA: status=RECENT_ACCEPTED latest=2026-05-25 age_days=30 sources=3 expected=Gharbia Islamic Housing Development Company summary=Gharbia Islamic Housing Development Company (GIHD.CA) has reported its financial results for Q1 2026 and Q1 2025, showing an increase in net profit. The company also held its Annual General Meeting in March 2026 and experienced board changes in May 2026. Recent financial data indicates a significant increase in revenue and earnings for 2025.
  - Gharbia Islamic Housing Development (GIHD.CA) Reports Its Financial Results for the Period from 01/01/2026 to 31/03/2026 (May 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYqgpi3J4F0zcgkkgYWzOw7bZNgwkfjenBOjgWJU3dUn-v3BcBFoUt7ahTNQH1lPDHWhQphZp5xN4pv1DaPYW-BpwOvq6vtVHr-vrP2AZS3xMcLwAnVLoYSAr_Aioym-k-PDdwVla_aX2RLiGwARwD8Q
  - Gharbia Islamic Housing Development (GIHD.CA) Reports Its Financial Results for the Period from 01/01/2025 to 31/03/2025 (May 29, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOfkGwFmFf0QfAAjbSH6ucy_tEIwudRY6MiQjfFMjbgcE9DLxy16VXVy77Ut0sdsN64SE39eVSyUMQjOc1ykb5YC4g7UQZ23DQ4N1ggNegIyog-W8gwkabok8yz1gAXvLrUHvCJotKghYI-Wr0vVg6RQ
  - Gharbia Islamic Housing Development Company, Annual General Meeting (March 28, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESIDO-nJqdNj6LH-VTAP7ylE17tWiTrmRro6hq1RcAHrCWQ2cMy3doBWrN4jwBc0h9uhK436DvUEASYFEZ5kOyMD6IwmU80BLUoLtAwP0PVGM79UoFiOTl-3iB53Uk
- CLHO.CA: status=RECENT_ACCEPTED latest=2026-06-08 age_days=16 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospital Group (CLHO.CA) has released its Q1 2026 earnings and FY 2025 results, demonstrating significant revenue growth. The company also held its Annual General Meeting in April 2026 and has ongoing investor relations activities, including presentations and conference calls.
  - Investors Presentation Q1 2026 - Cleopatra Hospitals Group (2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0oo8pXuO4eY3kPy5T3Q1_fA-rjst_KI5SKFzJN__Q9zCS5awjr7GCkkOKWrVJ6B5WQMEOEDuIrSnC2GvcBm55K7PqfFjYUHNytGrYLdEesh7869CnChzVAgaWHnL4YlNl_dXuAG74yh0=
  - Cleopatra Hospitals Group Reports Record FY2025 Results (March 17, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEajGyHMb89qVM6plIq2lkZGVL80gNM6NumT1BBUkLAofhr_U5_NuH4wMCPrIczPby96R071TWLtsCfjUNYy9fR86PFHeOjTGgfau_yxInfTtaT1711Qw63X3RCYq1D3x089BkL7M3pKOTI755LjqY5SYEqDbf2z4xVErvRHZwAPYacg2l8Y5e8HacHWAJxS8=
  - First quarter 2026 earnings released: EPS: ج.م0.08 (vs ج.م0.14 in 1Q 2025) (June 08, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFscJWmwPKX-Kl4MA01XrL3GdnKldlVkkwT2YWpVOz9MLUUaBK35bq1E49hbQh6X-77f4FnrVOHdwOy-FHgNWK_f_g0ju0GeZ6Zqgw404SF-gn6dmXNmOWd0SYxygUw
- POUL.CA: status=RECENT_ACCEPTED latest=2026-04-01 age_days=84 sources=3 expected=Cairo Poultry summary=Cairo Poultry (POUL.CA) has reported strong financial performance for 9M25 with significant growth in net profit and EBITDA. The company has also made recent announcements regarding its Extraordinary General Meeting (EGM) and Ordinary General Meeting (OGM).
  - Cairo Poultry Company Demonstrates Resilient Growth and Operational Strength in 9M25 (November 11, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEve3c52bZ-0ZfZLbzBxSzVV-qLTZ1JwupLi1f__sJtVkHbNmlyZX-DtKhy5bahP4fyq357eq3ELnp1g8OlKy5-UyRVE1FfmNhwZUAU4JKSykYbB5Z5psW1uB_GS6XS2SsqZmB52Xm3dui0eqSOuIcY
  - Cairo Poultry calls for the company's EGM (April 01, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDteg2dEdKEl4VBAc0DrzGaghiOnTGzlWXI5ZzXAYEYu52SfIJIlPLIebdGqtdgWLCSfe5V35ItjrtjhmYsE0EP0x6zz_d9xgm9XpjgB-O_U2BUO1cU3pYgkuoH3CY_JkM2YRuRWROHaEca1HXcaJ1vG17yke-6cni7CwQi4r0J2YIE2mRGHdhqpd36jKV
  - Cairo Poultry calls for the company's OGM (February 18, 2026): https://vertexaisearch.google.com/grounding-api-redirect/AUZIYQGDteg2dEdKEl4VBAc0DrzGaghiOnTGzlWXI5ZzXAYEYu52SfIJIlPLIebdGqtdgWLCSfe5V35ItjrtjhmYsE0EP0x6zz_d9xgm9XpjgB-O_U2BUO1cU3pYgkuoH3CY_JkM2YRuRWROHaEca1HXcaJ1vG17yke-6cni7CwQi4r0J2YIE2mRGHdhqpd36jKV
- MPRC.CA: status=RECENT_ACCEPTED latest=2026-06-19 age_days=5 sources=3 expected=Egyptian Media Production City summary=Egyptian Media Production City (MPRC.CA) has reported its latest quarterly earnings, showing an increase in revenue and net income. The company continues to operate as a major media and production entity in the Middle East, offering various studios and production services.
  - EGX:MPRC Financials | Egyptian Media Production City - Latest Quarter Earnings (June 17, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM9ZG6IVuBJOl0bXwWyoJkzZtTHBOnRbrsKZ9q8IPIlb24wFBqEz8ZH21BO2x64HetrWvqYQCxHWAeBE5jKjA3gZ2crTomHcfeS-nogwvIjBb44VhAdLPnQSgPj8WMzgAaV66t1cR0TTMrSAH-5XSh_343Gy8N9QqgEPuD
  - Egyptian Media Production City (EGX:MPRC) Company Profile & Description (June 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXTRZRMFEXxl3wo2CYlPgtU4JIBPhYW_D5EESCHVB3GknzDm8xZUex0zfOvTOrZ7SfLtuQrmxBuKnnlk1pAN4G0BCN8xDylnWIWYGadWHXrB4Z-3uh59TVurl9MXTVcfBgjdGLumVEgFZh
  - About Us - The Egyptian Media Production City: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-kTdI9JW6vcC4L7X6NiDSWGqNcfW_pKHUIGKNU8P6FerjpJ-3QT_aRWAe5-Abm7trbXBZH7C8IGnntxAUnV2atUci8xMDYpXCkSE-QKyFfRqfomdrM0t-ay8BesJXXus=
- ZMID.CA: status=RECENT_ACCEPTED latest=2026-05-23 age_days=32 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi Investment and Development (ZMID.CA) has released its Q1 2026 results and Q1 2025 earnings. The company has also had several market announcements regarding its EGM, AGM, and Board of Directors' decisions in late 2024 and early 2026. A new minor risk related to dividend sustainability was identified in September 2025.
  - Zahraa Maadi Investment & Development (ZMID.CA) Reports 9 Months Results (November 14, 2024): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUvHHH2egl9N8JZFVSy6JdPz3njM43AlhfZ6KGLuSyw97U1oTfZciMjjs49U9sM_FZRnkyZTAPyEXM53prUqGvqcqJcDKfG4qE1AiT_WD2ZD9I1AgGiu9qV9vdojiOXff4O8ruaH3CC-vSlCW5liKsYxFCTQoYrbAlp5OE_x6ueQ==
  - First quarter 2025 earnings released: EPS: ج.م0.13 (vs ج.م0.042 in 1Q 2024) (May 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUSe4TxfkaZo6ytSianGa4ayV4ZpkDHB451oa5r_9HWXZ6jNSD0vybbzlacubn3ZonWjOIk8BfJSctLXAD5JbJxfhFsKTAYdbEoh7pp8zuNsZAG4mfqptZvN03UN8E
  - Zahraa El Maadi Investment and Development Company SAE, Annual General Meeting (March 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUSe4TxfkaZo6ytSianGa4ayV4ZpkDHB451oa5r_9HWXZ6jNSD0vybbzlacubn3ZonWjOIk8BfJSctLXAD5JbJxfhFsKTAYdbEoh7pp8zuNsZAG4mfqptZvN03UN8E
- MHOT.CA: status=RECENT_ACCEPTED latest=2026-06-22 age_days=2 sources=3 expected=Misr Hotels summary=Misr Hotels (MHOT.CA) has announced stock dividends in June 2026 and reported its financial performance for fiscal year 2025, showing increased revenue and earnings. The company has also had several Board of Directors' meetings in recent months and reported its 9M-25/26 net profits.
  - Relaese from Misr Hotels (MHOT.CA) Concerning Stock Dividends (June 22, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4lazEb7arOkOq7RGRgrq6lipi2itmjHoFwOHnqiiJ0pNvJxgpZ0HkSc73ZXDZxv8tIwaa4Z1GZICti7xIK_SYUOFTocJ85UKiQhsQXK4mDaE0RkdIW1gAjx2vfoCK5hsK1FyKSNAMq1tF085L-WMpNNQ=
  - Misr Hotels Company (EGX:MHOT) Stock Price & Overview - Financial Performance in fiscal year 2025 (June 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6xq3Sm3sYrzNZuNOpyob_XCIUPHnmOiYKRBfqeQMKXA7qT6hyxBhCK5Mi6IpjIgycigZnFbvXKcpYAHwHRD6KhC8Oxf5v38glzeeIl_RR-9AHKdpCllI5YWQIpPSu5bdPkjo=
  - Misr Hotels (MHOT.CA) - Decisions of the BoD Meeting (June 17, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8YwvrOf8_DZFjSDX0f9ZWv4MSn4LPRKzgM0XtxFsUY-ETfDv4NNBhfoaLFmzY1qWrWGL4rJH6YEr7MklXc_uxjwg6qGnpB-sZUzcFVl3YnRS29hvfJY1bxQBc-xKrZiDt2pmni3a3WHvZef72CCmN
- CNFN.CA: status=RECENT_ACCEPTED latest=2026-03-25 age_days=91 sources=3 expected=Contact Financial Holding summary=Contact Financial Holding (CNFN.CA) has released its Q1 2026 highlights and FY 2025 results, demonstrating its position as a leading non-bank financial services provider in Egypt. The company also announced Board Resolutions in November 2025.
  - Q1 2026 Highlights - Contact Financial Holding - Investor Relations: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsguIDjg6O_SM43P1OGLrSisK-JB7K3ugrGZPoAh8amtmKNeZpcLBzRS5UpR5utn3C1aptHTasPq3cr3jZY2WtpMtpdve8kWOy5jvsyS_0NVPlk6u9BsIdz7Yw0obe
  - Contact Financial announces FY 2025 Results (March 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsguIDjg6O_SM43P1OGLrSisK-JB7K3ugrGZPoAh8amtmKNeZpcLBzRS5UpR5utn3C1aptHTasPq3cr3jZY2WtpMtpdve8kWOy5jvsyS_0NVPlk6u9BsIdz7Yw0obe
  - Board Resolutions (November 17, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsguIDjg6O_SM43P1OGLrSisK-JB7K3ugrGZPoAh8amtmKNeZpcLBzRS5UpR5utn3C1aptHTasPq3cr3jZY2WtpMtpdve8kWOy5jvsyS_0NVPlk6u9BsIdz7Yw0obe
- DAPH.CA: status=RECENT_ACCEPTED latest=2026-06-21 age_days=3 sources=3 expected=Development & Engineering Consultants summary=Development & Engineering Consultants (DAPH.CA) has held its Annual General Meeting (AGM) in June 2026 and made several announcements regarding Board of Directors' decisions. The company also reported its latest quarterly financials, showing a significant increase in revenue, though it is currently running at an operating cash loss.
  - Development & Engineering Consultants (DAPH.CA) - AGM Minutes (June 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHirEtXOe-oxx-78uwBgkNBQcohHjmQBoX9zNcHpwaU1jvs2m4NKYW-B9M7HfQCk77TkA_fq4s95SiUt_SPGteYFGfPiRvzfK1vDjA_0jaJ_hLUzW3hnKPy8M1qcRd87Q8FPN88u-LiKd7XEnaq23MO
  - Development & Engineering Consultants (DAPH.CA) - AGM Resolutions (June 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHirEtXOe-oxx-78uwBgkNBQcohHjmQBoX9zNcHpwaU1jvs2m4NKYW-B9M7HfQCk77TkA_fq4s95SiUt_SPGteYFGfPiRvzfK1vDjA_0jaJ_hLUzW3hnKPy8M1qcRd87Q8FPN88u-LiKd7XEnaq23MO
  - Development & Engineering Consultants (DAPH.CA) - Minutes of the BoD Meeting (June 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHirEtXOe-oxx-78uwBgkNBQcohHjmQBoX9zNcHpwaU1jvs2m4NKYW-B9M7HfQCk77TkA_fq4s95SiUt_SPGteYFGfPiRvzfK1vDjA_0jaJ_hLUzW3hnKPy8M1qcRd87Q8FPN88u-LiKd7XEnaq23MO

## Warnings
- No blocking warnings.
