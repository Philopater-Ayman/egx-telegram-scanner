# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-08-10T13:57:19.982550+00:00
Generated Cairo: 2026-08-10 16:57
Run timing: target 15:30 Cairo | generated Cairo 2026-08-10 16:57 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-08-10 16:50

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 60
- Data quality issues: 1
- Tradeable price/liquidity tickers: 139/189
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, August 10
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 80.0% / above MA50 80.0%
- EGX70 regime: BULLISH / above MA20 70.97% / above MA50 90.32%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- PHAR.CA: liquidity=1597483904.0 spike=5.9 score=14.03
- BIOC.CA: liquidity=636810880.0 spike=3.83 score=13.71
- NIPH.CA: liquidity=442661856.0 spike=2.11 score=11.25
- ISPH.CA: liquidity=402864832.0 spike=2.66 score=12.35
- GTWL.CA: liquidity=400987968.0 spike=4.1 score=13.71

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flagged MOSC.CA, EGCH.CA and CLHO.CA as watch/buy setups in a bullish EGX30/EGX70 backdrop, but the selective swing‑trade risk mode, low confidence and sector‑wide headwinds add uncertainty for the next 1‑3 days.
- MOSC.CA: price above MA20/MA50, RSI 68.1, liquidity spike, support 270/resistance 329; bullish watch but momentum extended and sector not leading.
- EGCH.CA: price above MAs, RSI 63.0, liquidity spike, support 12.69/resistance 14.62; bullish watch, low confidence, sector not leading.
- CLHO.CA: price above MAs, RSI 60.1, liquidity spike, support 15.98/resistance 19.72; bullish watch, sector not leading.

## Top Liquidity Spikes
- INFI.CA: spike=8.8 liquidity=375247136.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- FERC.CA: spike=8.03 liquidity=113240704.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ECAP.CA: spike=7.93 liquidity=48132044.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EEII.CA: spike=7.5 liquidity=105745672.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ATQA.CA: spike=6.38 liquidity=248954096.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=12.39 5d=7.65% 20d=8.35% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=11.2 5d=6.27% 20d=11.77% aboveMA50=100.0%
- #3 Non-bank Financial Services: score=9.4 5d=2.46% 20d=3.59% aboveMA50=100.0%
- #4 Food, Beverages & Tobacco: score=9.16 5d=7.42% 20d=1.79% aboveMA50=71.43%
- #5 Textiles: score=8.86 5d=2.73% 20d=11.29% aboveMA50=75.0%
- #6 Fintech & Payments: score=8.65 5d=1.88% 20d=2.62% aboveMA50=100.0%
- #7 Agriculture & Food Production: score=8.48 5d=2.79% 20d=3.57% aboveMA50=50.0%
- #8 Energy & Petrochemicals: score=8.18 5d=-0.93% 20d=17.59% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY MOSC.CA
  - Entry: 306.0 | Take profit: 330.48 | Stop loss: 293.76
  - Confidence: LOW | score=29.45 | outlook=BULLISH_WATCH 86.27
  - Reason: WATCH/BUY SETUP: MOSC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 68.12, support 270.02, resistance 329.5, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY EGCH.CA
  - Entry: 14.18 | Take profit: 15.32 | Stop loss: 13.61
  - Confidence: LOW | score=28.5 | outlook=BULLISH_WATCH 79.8
  - Reason: WATCH/BUY SETUP: EGCH.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 63.0, support 12.69, resistance 14.62, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY CLHO.CA
  - Entry: 18.0 | Take profit: 19.62 | Stop loss: 17.28
  - Confidence: LOW | score=27.77 | outlook=BULLISH_WATCH 87.08
  - Reason: WATCH/BUY SETUP: CLHO.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 60.09, support 15.98, resistance 19.72, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CNFN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- ATLC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- POUL.CA: BULLISH_WATCH score=96.16 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- HRHO.CA: BULLISH_WATCH score=94.4 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- SCTS.CA: BULLISH_WATCH score=93.02 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SUGR.CA: BULLISH_WATCH score=90.16 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- BTFH.CA: BULLISH_WATCH score=88.4 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20
- CLHO.CA: BULLISH_WATCH score=87.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MOSC.CA: BULLISH_WATCH score=86.27 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- FWRY.CA: BULLISH_WATCH score=83.65 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- CNFN.CA: rank=31.74 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=4.96 support=4.68 resistance=5.05 liquidity=46335324.0
- ALUM.CA: rank=29.85 outlook=BULLISH_WATCH outlook_score=72.27 sector_rank=19 price=25.25 support=22.41 resistance=25.15 liquidity=22311354.0
- MOSC.CA: rank=29.45 outlook=BULLISH_WATCH outlook_score=86.27 sector_rank=19 price=306.0 support=270.02 resistance=329.5 liquidity=45419776.0
- EGCH.CA: rank=28.5 outlook=BULLISH_WATCH outlook_score=79.8 sector_rank=13 price=14.18 support=12.69 resistance=14.62 liquidity=211316784.0
- CLHO.CA: rank=27.77 outlook=BULLISH_WATCH outlook_score=87.08 sector_rank=16 price=18.0 support=15.98 resistance=19.72 liquidity=91939648.0
- HRHO.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=94.4 sector_rank=3 price=27.33 support=25.95 resistance=28.1 liquidity=88568000.0
- GBCO.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=74 sector_rank=1 price=31.75 support=29.53 resistance=34.2 liquidity=41242080.0
- SUGR.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=90.16 sector_rank=4 price=48.54 support=46.47 resistance=49.25 liquidity=13348391.0
- EMFD.CA: rank=26.54 outlook=BULLISH_WATCH outlook_score=76.19 sector_rank=11 price=11.8 support=11.08 resistance=12.12 liquidity=62722740.0
- ATLC.CA: rank=26.46 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=5.47 support=5.0 resistance=5.59 liquidity=21913642.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=23.71 buy_ready=True sector_rank=19 price=291.11 support=223.25 resistance=317.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=69.22 liquidity=32853082.0 spike=0.9
- ABUK.CA: score=26.32 buy_ready=True sector_rank=13 price=73.66 support=69.01 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.32 liquidity=42075124.0 spike=0.28
- ACAMD.CA: score=17.71 buy_ready=False sector_rank=19 price=2.28 support=2.3 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=91769720.0 spike=1.0
- ACGC.CA: score=23.4 buy_ready=False sector_rank=5 price=11.27 support=9.55 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.1 liquidity=13622193.0 spike=0.42
- ADCI.CA: score=13.39 buy_ready=False sector_rank=19 price=341.08 support=291.0 resistance=344.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63884408.0 spike=3.34
- ADIB.CA: score=21.4 buy_ready=False sector_rank=9 price=53.79 support=46.02 resistance=53.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.57 liquidity=45318388.0 spike=0.38
- ADPC.CA: score=10.95 buy_ready=False sector_rank=19 price=4.48 support=4.4 resistance=4.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=104882784.0 spike=2.12
- AFDI.CA: score=8.71 buy_ready=False sector_rank=19 price=64.95 support=60.0 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23051598.0 spike=0.95
- AFMC.CA: score=20.71 buy_ready=False sector_rank=19 price=220.95 support=72.0 resistance=250.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.31 liquidity=75557592.0 spike=0.54
- AJWA.CA: score=23.71 buy_ready=True sector_rank=19 price=186.09 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=63.87 liquidity=12939987.0 spike=0.36
- ALCN.CA: score=26.4 buy_ready=True sector_rank=12 price=30.74 support=28.8 resistance=31.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.2 liquidity=18768488.0 spike=0.65
- ALUM.CA: score=29.85 buy_ready=True sector_rank=19 price=25.25 support=22.41 resistance=25.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.07 liquidity=22311354.0 spike=3.07
- AMER.CA: score=9.4 buy_ready=False sector_rank=11 price=6.47 support=6.15 resistance=6.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75758120.0 spike=0.66
- AMES.CA: score=23.71 buy_ready=True sector_rank=19 price=121.33 support=72.1 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.25 liquidity=24239588.0 spike=0.25
- AMIA.CA: score=20.97 buy_ready=False sector_rank=19 price=12.74 support=8.74 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.49 liquidity=18811254.0 spike=1.13
- AMOC.CA: score=24.4 buy_ready=True sector_rank=8 price=9.15 support=7.95 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.29 liquidity=33305198.0 spike=0.34
- APSW.CA: score=11.67 buy_ready=False sector_rank=19 price=8.74 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=49.76 liquidity=960635.5 spike=0.52
- ARAB.CA: score=22.4 buy_ready=False sector_rank=11 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=88758360.0 spike=0.7
- ARCC.CA: score=9.94 buy_ready=False sector_rank=15 price=63.72 support=62.62 resistance=64.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49388840.0 spike=1.39
- AREH.CA: score=20.71 buy_ready=False sector_rank=19 price=1.52 support=1.38 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=20265786.0 spike=0.51
- ARVA.CA: score=4.71 buy_ready=False sector_rank=19 price=12.35 support=12.35 resistance=12.35 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=88.83 liquidity=0.0 spike=0.0
- ASCM.CA: score=23.79 buy_ready=False sector_rank=19 price=68.0 support=58.16 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.12 liquidity=66446972.0 spike=1.04
- ASPI.CA: score=9.11 buy_ready=False sector_rank=19 price=0.5 support=0.49 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50793424.0 spike=1.2
- ATLC.CA: score=26.46 buy_ready=True sector_rank=3 price=5.47 support=5.0 resistance=5.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.91 liquidity=21913642.0 spike=1.53
- ATQA.CA: score=14.32 buy_ready=False sector_rank=13 price=10.7 support=10.09 resistance=10.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=248954096.0 spike=6.38
- AXPH.CA: score=11.32 buy_ready=False sector_rank=19 price=1340.91 support=1281.35 resistance=1346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9809763.0 spike=2.4
- BINV.CA: score=19.91 buy_ready=True sector_rank=10 price=48.85 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.9 liquidity=3507572.75 spike=0.49
- BIOC.CA: score=13.71 buy_ready=False sector_rank=19 price=521.68 support=402.0 resistance=563.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=636810880.0 spike=3.83
- BTFH.CA: score=26.92 buy_ready=False sector_rank=3 price=3.09 support=3.03 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.84 liquidity=400787936.0 spike=1.76
- CAED.CA: score=22.33 buy_ready=True sector_rank=19 price=120.38 support=73.25 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=8617524.0 spike=0.12
- CANA.CA: score=9.58 buy_ready=False sector_rank=9 price=40.75 support=40.67 resistance=41.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21147704.0 spike=1.09
- CCAP.CA: score=19.4 buy_ready=False sector_rank=10 price=5.16 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=282977696.0 spike=0.44
- CCRS.CA: score=13.64 buy_ready=False sector_rank=19 price=2.46 support=2.35 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.69 liquidity=9933193.0 spike=0.51
- CEFM.CA: score=21.38 buy_ready=True sector_rank=19 price=134.81 support=101.57 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=5667985.5 spike=0.18
- CERA.CA: score=21.71 buy_ready=False sector_rank=19 price=1.32 support=1.25 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=11441920.0 spike=0.5
- CFGH.CA: score=7.71 buy_ready=False sector_rank=19 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- CICH.CA: score=19.04 buy_ready=False sector_rank=3 price=12.48 support=11.61 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=78.91 liquidity=6638076.0 spike=0.8
- CIEB.CA: score=23.89 buy_ready=True sector_rank=9 price=24.49 support=23.75 resistance=24.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.64 liquidity=5486500.0 spike=0.53
- CIRA.CA: score=9.01 buy_ready=False sector_rank=17 price=38.5 support=38.25 resistance=39.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50551776.0 spike=0.86
- CLHO.CA: score=27.77 buy_ready=True sector_rank=16 price=18.0 support=15.98 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=91939648.0 spike=1.87
- CNFN.CA: score=31.74 buy_ready=True sector_rank=3 price=4.96 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=46335324.0 spike=2.17
- COMI.CA: score=22.4 buy_ready=True sector_rank=9 price=140.0 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.99 liquidity=234007872.0 spike=0.56
- COPR.CA: score=23.71 buy_ready=True sector_rank=19 price=0.41 support=0.36 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=29685572.0 spike=0.92
- COSG.CA: score=23.71 buy_ready=True sector_rank=19 price=1.7 support=1.6 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=27344396.0 spike=0.7
- CPCI.CA: score=13.71 buy_ready=False sector_rank=19 price=574.08 support=484.2 resistance=579.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49205584.0 spike=3.68
- CSAG.CA: score=11.5 buy_ready=False sector_rank=12 price=39.0 support=38.0 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42720700.0 spike=2.05
- DAPH.CA: score=13.71 buy_ready=False sector_rank=19 price=128.94 support=108.0 resistance=128.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=112999048.0 spike=4.46
- DEIN.CA: score=-1.29 buy_ready=False sector_rank=19 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=24.46 buy_ready=False sector_rank=4 price=28.73 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=70.35 liquidity=11421562.0 spike=1.03
- DSCW.CA: score=26.17 buy_ready=False sector_rank=19 price=2.14 support=1.77 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=99045184.0 spike=1.23
- DTPP.CA: score=9.41 buy_ready=False sector_rank=19 price=284.44 support=280.01 resistance=292.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=79315416.0 spike=1.35
- EALR.CA: score=25.71 buy_ready=True sector_rank=19 price=384.23 support=360.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=22422866.0 spike=0.77
- EASB.CA: score=15.39 buy_ready=False sector_rank=19 price=7.22 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.88 liquidity=3681430.0 spike=0.32
- EAST.CA: score=20.4 buy_ready=False sector_rank=4 price=36.4 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.86 liquidity=39079488.0 spike=0.57
- EBSC.CA: score=19.2 buy_ready=False sector_rank=19 price=1.94 support=1.85 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=3493759.75 spike=0.53
- ECAP.CA: score=13.71 buy_ready=False sector_rank=19 price=37.68 support=34.0 resistance=37.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48132044.0 spike=7.93
- EDFM.CA: score=14.81 buy_ready=True sector_rank=19 price=395.32 support=337.96 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=1103545.38 spike=0.19
- EEII.CA: score=13.71 buy_ready=False sector_rank=19 price=3.0 support=2.68 resistance=3.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=105745672.0 spike=7.5
- EFIC.CA: score=26.32 buy_ready=True sector_rank=13 price=211.31 support=181.69 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.15 liquidity=21226020.0 spike=0.84
- EFID.CA: score=23.88 buy_ready=False sector_rank=4 price=31.59 support=26.64 resistance=32.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=83.88 liquidity=103373256.0 spike=1.24
- EFIH.CA: score=26.4 buy_ready=True sector_rank=6 price=24.06 support=21.87 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.61 liquidity=73993048.0 spike=0.82
- EGAL.CA: score=22.78 buy_ready=False sector_rank=13 price=302.02 support=290.0 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.1 liquidity=71772520.0 spike=1.73
- EGAS.CA: score=21.4 buy_ready=False sector_rank=8 price=59.2 support=48.95 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=75.45 liquidity=17214608.0 spike=0.67
- EGBE.CA: score=12.45 buy_ready=False sector_rank=9 price=0.56 support=-0.34 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=81.06 liquidity=166615.3 spike=1.44
- EGCH.CA: score=28.5 buy_ready=True sector_rank=13 price=14.18 support=12.69 resistance=14.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=211316784.0 spike=2.09
- EGSA.CA: score=4.65 buy_ready=False sector_rank=18 price=8.69 support=8.8 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=29978.24 spike=1.38
- EGTS.CA: score=24.0 buy_ready=False sector_rank=11 price=18.27 support=17.11 resistance=19.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.09 liquidity=47701036.0 spike=1.3
- EHDR.CA: score=23.71 buy_ready=True sector_rank=19 price=2.93 support=2.64 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=33595576.0 spike=0.81
- EKHO.CA: score=8.4 buy_ready=False sector_rank=8 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.78 buy_ready=False sector_rank=2 price=2.19 support=2.1 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=94343448.0 spike=1.19
- ELKA.CA: score=16.71 buy_ready=False sector_rank=19 price=1.69 support=1.59 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.87 liquidity=68862232.0 spike=0.82
- ELNA.CA: score=8.09 buy_ready=False sector_rank=19 price=37.88 support=36.5 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.89 liquidity=386503.59 spike=0.62
- ELSH.CA: score=21.71 buy_ready=False sector_rank=19 price=14.11 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.8 liquidity=45998612.0 spike=0.4
- ELWA.CA: score=5.94 buy_ready=False sector_rank=19 price=1.77 support=1.65 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=8.33 liquidity=1852097.12 spike=1.19
- EMFD.CA: score=26.54 buy_ready=True sector_rank=11 price=11.8 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.15 liquidity=62722740.0 spike=1.07
- ENGC.CA: score=23.71 buy_ready=True sector_rank=19 price=46.22 support=38.15 resistance=47.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.31 liquidity=21413898.0 spike=0.65
- EOSB.CA: score=17.71 buy_ready=False sector_rank=19 price=1.55 support=1.52 resistance=1.62 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=11.53 buy_ready=False sector_rank=19 price=12.49 support=11.92 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78048208.0 spike=2.41
- EPPK.CA: score=12.98 buy_ready=False sector_rank=19 price=13.73 support=13.87 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=990766.0 spike=1.14
- ETEL.CA: score=23.86 buy_ready=True sector_rank=18 price=108.6 support=96.0 resistance=114.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=70446600.0 spike=0.7
- ETRS.CA: score=23.71 buy_ready=True sector_rank=19 price=10.7 support=10.21 resistance=10.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.26 liquidity=24432260.0 spike=0.92
- EXPA.CA: score=24.4 buy_ready=False sector_rank=9 price=20.63 support=18.61 resistance=20.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=73.74 liquidity=13431565.0 spike=0.38
- FAIT.CA: score=22.06 buy_ready=True sector_rank=9 price=39.42 support=36.1 resistance=38.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=3380292.5 spike=1.14
- FAITA.CA: score=16.55 buy_ready=False sector_rank=9 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=105498.45 spike=2.52
- FERC.CA: score=14.32 buy_ready=False sector_rank=13 price=85.06 support=83.1 resistance=87.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=113240704.0 spike=8.03
- FWRY.CA: score=26.42 buy_ready=True sector_rank=6 price=19.28 support=18.43 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=116867320.0 spike=1.01
- GBCO.CA: score=27.4 buy_ready=True sector_rank=1 price=31.75 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.48 liquidity=41242080.0 spike=0.63
- GDWA.CA: score=17.71 buy_ready=False sector_rank=19 price=0.81 support=0.78 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=41469648.0 spike=0.35
- GGCC.CA: score=8.77 buy_ready=False sector_rank=19 price=1.2 support=1.16 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45754984.0 spike=1.03
- GIHD.CA: score=11.07 buy_ready=False sector_rank=19 price=68.05 support=59.53 resistance=71.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=122254520.0 spike=2.18
- GMCI.CA: score=11.71 buy_ready=False sector_rank=19 price=1.98 support=1.91 resistance=2.2 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=37.25 liquidity=0.0 spike=0.0
- GRCA.CA: score=23.71 buy_ready=True sector_rank=19 price=58.68 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.29 liquidity=13201902.0 spike=0.72
- GSSC.CA: score=19.45 buy_ready=True sector_rank=19 price=274.62 support=257.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.41 liquidity=3745310.75 spike=0.21
- GTWL.CA: score=13.71 buy_ready=False sector_rank=19 price=128.24 support=125.65 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=400987968.0 spike=4.1
- HDBK.CA: score=19.4 buy_ready=False sector_rank=9 price=85.02 support=76.9 resistance=85.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=80.83 liquidity=22047362.0 spike=0.58
- HELI.CA: score=24.4 buy_ready=True sector_rank=11 price=8.44 support=7.24 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=172978144.0 spike=0.86
- HRHO.CA: score=27.4 buy_ready=True sector_rank=3 price=27.33 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=88568000.0 spike=0.91
- ICID.CA: score=13.71 buy_ready=False sector_rank=19 price=9.01 support=8.16 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43995500.0 spike=5.95
- IDRE.CA: score=9.83 buy_ready=False sector_rank=19 price=56.47 support=55.7 resistance=59.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47804340.0 spike=1.56
- IFAP.CA: score=23.3 buy_ready=False sector_rank=7 price=21.44 support=18.96 resistance=21.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.22 liquidity=37890744.0 spike=1.95
- INFI.CA: score=13.71 buy_ready=False sector_rank=19 price=174.19 support=173.1 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=375247136.0 spike=8.8
- IRON.CA: score=22.82 buy_ready=False sector_rank=13 price=31.81 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=9956749.0 spike=1.27
- ISMA.CA: score=12.17 buy_ready=False sector_rank=19 price=33.08 support=32.1 resistance=33.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65652984.0 spike=2.73
- ISMQ.CA: score=24.32 buy_ready=True sector_rank=13 price=9.41 support=8.96 resistance=9.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.27 liquidity=53895940.0 spike=0.82
- ISPH.CA: score=12.35 buy_ready=False sector_rank=16 price=14.52 support=13.5 resistance=14.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=402864832.0 spike=2.66
- JUFO.CA: score=20.4 buy_ready=False sector_rank=4 price=26.6 support=22.78 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=38.53 liquidity=43196644.0 spike=0.84
- KABO.CA: score=11.42 buy_ready=False sector_rank=5 price=8.49 support=8.46 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=76556496.0 spike=2.01
- KWIN.CA: score=23.71 buy_ready=True sector_rank=19 price=91.86 support=67.32 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.3 liquidity=41435164.0 spike=0.7
- KZPC.CA: score=17.0 buy_ready=False sector_rank=19 price=8.93 support=8.4 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.98 liquidity=6934891.5 spike=1.18
- LCSW.CA: score=22.16 buy_ready=False sector_rank=15 price=33.59 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=43804008.0 spike=0.83
- LUTS.CA: score=10.27 buy_ready=False sector_rank=19 price=0.81 support=0.79 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78580128.0 spike=1.78
- MAAL.CA: score=4.97 buy_ready=False sector_rank=19 price=8.17 support=8.1 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6258700.0 spike=0.42
- MASR.CA: score=19.33 buy_ready=False sector_rank=19 price=7.77 support=7.7 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.4 liquidity=171749136.0 spike=2.31
- MBSC.CA: score=23.78 buy_ready=False sector_rank=15 price=265.01 support=231.51 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=75.29 liquidity=27463880.0 spike=1.31
- MCQE.CA: score=13.5 buy_ready=False sector_rank=15 price=201.67 support=197.06 resistance=203.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64060292.0 spike=3.17
- MCRO.CA: score=9.05 buy_ready=False sector_rank=19 price=1.63 support=1.56 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=205139168.0 spike=1.17
- MENA.CA: score=13.12 buy_ready=False sector_rank=11 price=7.02 support=6.83 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=719284.94 spike=0.19
- MEPA.CA: score=23.71 buy_ready=True sector_rank=19 price=1.94 support=1.64 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=43113324.0 spike=0.71
- MFPC.CA: score=16.32 buy_ready=False sector_rank=13 price=36.99 support=35.37 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.32 liquidity=33715080.0 spike=0.43
- MFSC.CA: score=26.37 buy_ready=True sector_rank=19 price=49.04 support=45.05 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.81 liquidity=15610979.0 spike=1.33
- MHOT.CA: score=23.03 buy_ready=False sector_rank=14 price=17.26 support=16.2 resistance=17.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.21 liquidity=12724757.0 spike=1.37
- MICH.CA: score=20.71 buy_ready=False sector_rank=19 price=47.99 support=37.46 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.87 liquidity=20696674.0 spike=0.65
- MILS.CA: score=25.71 buy_ready=True sector_rank=19 price=187.77 support=134.03 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.54 liquidity=39180572.0 spike=0.64
- MIPH.CA: score=26.16 buy_ready=True sector_rank=16 price=816.55 support=690.01 resistance=831.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=8546150.0 spike=1.79
- MOED.CA: score=12.71 buy_ready=False sector_rank=19 price=0.68 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.44 liquidity=22625500.0 spike=0.75
- MOIL.CA: score=11.64 buy_ready=False sector_rank=8 price=0.67 support=0.51 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=92.52 liquidity=241664.42 spike=0.37
- MOIN.CA: score=24.37 buy_ready=False sector_rank=19 price=36.12 support=23.03 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=97.0 liquidity=40690816.0 spike=1.83
- MOSC.CA: score=29.45 buy_ready=True sector_rank=19 price=306.0 support=270.02 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.12 liquidity=45419776.0 spike=2.87
- MPCI.CA: score=10.79 buy_ready=False sector_rank=19 price=393.72 support=328.11 resistance=393.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=250900320.0 spike=2.04
- MPCO.CA: score=13.22 buy_ready=False sector_rank=7 price=2.13 support=2.11 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=266065536.0 spike=2.91
- MPRC.CA: score=23.71 buy_ready=True sector_rank=19 price=46.54 support=41.0 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.5 liquidity=11168698.0 spike=0.46
- MTIE.CA: score=27.58 buy_ready=False sector_rank=1 price=11.27 support=9.3 resistance=11.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.45 liquidity=58714004.0 spike=1.59
- NAHO.CA: score=9.71 buy_ready=False sector_rank=19 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=0.0 spike=0.0
- NCCW.CA: score=8.71 buy_ready=False sector_rank=19 price=5.99 support=5.93 resistance=6.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33293112.0 spike=0.93
- NEDA.CA: score=4.16 buy_ready=False sector_rank=19 price=2.73 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.04 liquidity=456171.56 spike=0.61
- NHPS.CA: score=12.67 buy_ready=False sector_rank=19 price=96.56 support=88.35 resistance=104.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=241032640.0 spike=2.98
- NINH.CA: score=25.71 buy_ready=True sector_rank=19 price=23.1 support=17.52 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.84 liquidity=25240292.0 spike=0.45
- NIPH.CA: score=11.25 buy_ready=False sector_rank=16 price=430.8 support=362.0 resistance=430.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=442661856.0 spike=2.11
- OBRI.CA: score=12.71 buy_ready=False sector_rank=19 price=33.43 support=32.05 resistance=34.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108755664.0 spike=3.0
- OCDI.CA: score=28.18 buy_ready=False sector_rank=11 price=31.49 support=26.2 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.17 liquidity=200571312.0 spike=1.89
- OCPH.CA: score=12.07 buy_ready=False sector_rank=19 price=289.92 support=241.0 resistance=289.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80451000.0 spike=2.68
- ODIN.CA: score=11.61 buy_ready=False sector_rank=19 price=3.25 support=2.82 resistance=3.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53723904.0 spike=2.45
- OFH.CA: score=22.71 buy_ready=False sector_rank=19 price=0.86 support=0.62 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.65 liquidity=68815776.0 spike=0.79
- OIH.CA: score=23.4 buy_ready=False sector_rank=10 price=1.64 support=1.41 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=84.85 liquidity=81762584.0 spike=0.93
- OLFI.CA: score=23.4 buy_ready=False sector_rank=4 price=24.44 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.84 liquidity=31753290.0 spike=0.8
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=718.3 support=716.0 resistance=724.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=169305088.0 spike=1.0
- ORHD.CA: score=26.4 buy_ready=False sector_rank=11 price=42.54 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=74.79 liquidity=104684080.0 spike=0.64
- ORWE.CA: score=21.4 buy_ready=False sector_rank=5 price=26.32 support=22.42 resistance=27.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.06 liquidity=54178580.0 spike=0.85
- PHAR.CA: score=14.03 buy_ready=False sector_rank=16 price=160.18 support=133.5 resistance=160.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1597483904.0 spike=5.9
- PHDC.CA: score=24.4 buy_ready=True sector_rank=11 price=15.51 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.45 liquidity=132453504.0 spike=0.55
- PHTV.CA: score=4.87 buy_ready=False sector_rank=19 price=382.44 support=348.0 resistance=397.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5381548.0 spike=1.39
- POUL.CA: score=26.16 buy_ready=True sector_rank=4 price=39.67 support=36.5 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=57969576.0 spike=1.88
- PRCL.CA: score=22.16 buy_ready=False sector_rank=15 price=35.03 support=32.76 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=34850416.0 spike=0.91
- PRDC.CA: score=22.4 buy_ready=False sector_rank=11 price=9.24 support=8.2 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.13 liquidity=87730144.0 spike=0.78
- PRMH.CA: score=21.45 buy_ready=True sector_rank=19 price=2.77 support=2.56 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.19 liquidity=5746526.5 spike=0.33
- RACC.CA: score=21.23 buy_ready=False sector_rank=19 price=10.14 support=9.8 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=9521086.0 spike=0.44
- RAKT.CA: score=9.71 buy_ready=False sector_rank=19 price=22.96 support=21.25 resistance=23.5 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=89.22 liquidity=0.0 spike=0.0
- RAYA.CA: score=16.45 buy_ready=False sector_rank=21 price=7.35 support=7.3 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.37 liquidity=53377988.0 spike=0.48
- RMDA.CA: score=11.03 buy_ready=False sector_rank=16 price=6.85 support=6.26 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=192514960.0 spike=2.0
- ROTO.CA: score=25.23 buy_ready=False sector_rank=19 price=48.6 support=40.5 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=79.38 liquidity=47491424.0 spike=2.26
- RREI.CA: score=9.23 buy_ready=False sector_rank=19 price=4.81 support=4.76 resistance=4.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80616568.0 spike=1.26
- RTVC.CA: score=13.14 buy_ready=False sector_rank=19 price=3.8 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=4434457.5 spike=0.86
- RUBX.CA: score=16.71 buy_ready=False sector_rank=19 price=12.22 support=12.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.96 liquidity=11604307.0 spike=0.33
- SAUD.CA: score=25.33 buy_ready=True sector_rank=9 price=22.35 support=21.25 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.72 liquidity=8928968.0 spike=0.65
- SCEM.CA: score=25.1 buy_ready=True sector_rank=15 price=81.84 support=61.28 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=151452528.0 spike=1.47
- SCFM.CA: score=20.83 buy_ready=True sector_rank=19 price=278.51 support=250.12 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.78 liquidity=7121269.0 spike=0.24
- SCTS.CA: score=25.07 buy_ready=True sector_rank=17 price=620.33 support=602.0 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.82 liquidity=12738672.0 spike=1.53
- SDTI.CA: score=11.21 buy_ready=False sector_rank=19 price=72.8 support=69.98 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61243632.0 spike=2.25
- SEIG.CA: score=13.63 buy_ready=False sector_rank=19 price=269.5 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=75.66 liquidity=2920000.25 spike=0.15
- SIPC.CA: score=10.29 buy_ready=False sector_rank=19 price=5.1 support=4.72 resistance=5.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92186616.0 spike=1.79
- SKPC.CA: score=25.32 buy_ready=True sector_rank=13 price=16.43 support=14.8 resistance=16.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=37958428.0 spike=0.85
- SMFR.CA: score=9.93 buy_ready=False sector_rank=19 price=258.54 support=258.05 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56569108.0 spike=1.61
- SNFC.CA: score=12.44 buy_ready=False sector_rank=19 price=10.84 support=10.7 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.91 liquidity=8733094.0 spike=0.73
- SPIN.CA: score=24.4 buy_ready=True sector_rank=5 price=15.71 support=14.55 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=66.76 liquidity=13839308.0 spike=0.49
- SPMD.CA: score=25.71 buy_ready=True sector_rank=19 price=0.49 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.47 liquidity=22962710.0 spike=0.7
- SUGR.CA: score=27.4 buy_ready=True sector_rank=4 price=48.54 support=46.47 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=13348391.0 spike=1.5
- SVCE.CA: score=23.71 buy_ready=True sector_rank=19 price=9.39 support=9.06 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.62 liquidity=26852132.0 spike=0.75
- SWDY.CA: score=26.92 buy_ready=False sector_rank=2 price=107.49 support=87.41 resistance=114.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=73.84 liquidity=72072720.0 spike=1.26
- TALM.CA: score=24.01 buy_ready=True sector_rank=17 price=18.81 support=15.4 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=31483378.0 spike=0.81
- TMGH.CA: score=22.4 buy_ready=False sector_rank=11 price=98.45 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=313039744.0 spike=0.93
- TRTO.CA: score=9.71 buy_ready=False sector_rank=19 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-08-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=14.47 buy_ready=False sector_rank=19 price=546.03 support=491.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.89 liquidity=762137.75 spike=0.14
- UEGC.CA: score=8.71 buy_ready=False sector_rank=19 price=2.8 support=2.69 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20552610.0 spike=0.38
- UNIP.CA: score=24.01 buy_ready=True sector_rank=19 price=0.41 support=0.34 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=34471784.0 spike=1.15
- UNIT.CA: score=10.51 buy_ready=False sector_rank=11 price=17.79 support=17.32 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.77 liquidity=3108387.75 spike=0.13
- WCDF.CA: score=12.69 buy_ready=False sector_rank=19 price=587.89 support=508.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.6 liquidity=1986034.88 spike=0.51
- WKOL.CA: score=23.71 buy_ready=True sector_rank=19 price=321.43 support=307.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.89 liquidity=19826542.0 spike=0.95
- ZEOT.CA: score=25.71 buy_ready=True sector_rank=19 price=13.06 support=11.1 resistance=13.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.38 liquidity=25290720.0 spike=0.86
- ZMID.CA: score=24.52 buy_ready=True sector_rank=11 price=7.6 support=6.9 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.46 liquidity=283339904.0 spike=1.06

## Backtesting Lite
- CNFN.CA: 180d return=3.73%, max drawdown=-27.78%, MA20>MA50 days last20=20, as_of=2026-08-08T21:00:00+00:00
- ALUM.CA: 180d return=46.02%, max drawdown=-21.86%, MA20>MA50 days last20=4, as_of=2026-08-08T21:00:00+00:00
- MOSC.CA: 180d return=58.06%, max drawdown=-22.97%, MA20>MA50 days last20=9, as_of=2026-08-08T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CNFN.CA: status=RECENT_ACCEPTED latest=2026-03-25 age_days=138 sources=3 expected=Contact Financial Holding summary=Contact Financial Holding (CNFN.CA) has reported its full-year 2025 results and interim financial statements for Q1 2025. The company also announced board resolutions in late 2025.
  - Contact Financial announces FY 2025 Results (Mar 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTczGmFWrLmgjqgeYHX4KXLFUWmB3BA4f-DbMx7tLohErQc4YTHF_40FPlb9fofUWB7Gr-QXfNwGD5qg4PLkuk97AX18viecZYv1mAjXbK7LW3D0JSLHs6sUUOZ6qemw==
  - Contact Financial Holding (S.A.E) Separate interim financial statements For the period ended March 31, 2025 (approved June 18, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE09wC-MjCyBKfJddLJg-vu2tAzsAS512-tYqt26UPt5KDvZlbTNAqXSSBMXxTFW_aS106_7KkP2zJD_d9YCExpyNYPsxEHXCHYXAW7a0Rbxx6dtoWlUMi6mHvvRk0ZcknqYNaSOzP0N1_-ChO4sZM_FDlSk6T2C3EP1e1cz-s2LwbvyjE6AuZenhts0fsA0eMVapdABKgPKt1U1Ss7-yKHaOPw
  - Board Resolutions (Nov 17, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTczGmFWrLmgjqgeYHX4KXLFUWmB3BA4f-DbMx7tLohErQc4YTHF_40FPlb9fofUWB7Gr-QXfNwGD5qg4PLkuk97AX18viecZYv1mAjXbK7LW3D0JSLHs6sUUOZ6qemw==
- ALUM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Aluminum Company (S.A.E) summary=Arab Aluminum’s stock holds steady as bullish pattern breaks; Arab Aluminum profits rise 7% in H1-17; Arab Aluminum OGM approves EGP 1/shr dividends Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Arab Aluminum’s stock holds steady as bullish pattern breaks: https://english.mubasher.info/news/4564438/Arab-Aluminum-s-stock-holds-steady-as-bullish-pattern-breaks/
  - Arab Aluminum profits rise 7% in H1-17: https://english.mubasher.info/news/3144589/Arab-Aluminum-profits-rise-7-in-H1-17/
  - Arab Aluminum OGM approves EGP 1/shr dividends: https://english.mubasher.info/news/3076498/Arab-Aluminum-OGM-approves-EGP-1-shr-dividends/
- MOSC.CA: status=RECENT_ACCEPTED latest=2026-08-02 age_days=8 sources=3 expected=Misr Oils & Soap summary=Misr Oils & Soap (MOSC.CA) has reported strong financial performance in fiscal year 2025 and Q1 2026, with significant revenue and earnings growth. The company has also released recent board decisions, AGM minutes, and financial statements.
  - Misr Oils & Soap Q1 2026 Revenue and Earnings (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1kmy98FgLu7zEyVrI_f4XbuxLlA1uJD9uL0LAeWDrLkrbBeWNF-yvHpxWeyVJpQWkOGLugcaIP7AeUrX2HeV2UU2aBKLCYNKIlXkCDJzqIHwnVxEkLN1llw3WG89mmaVvprh9vzN9b7EKSQ==
  - Misr Oils & Soap FY 2025 Revenue and Earnings (Fiscal Year 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUIixxwweYKRpEthq15X-ZHT6yOVk5F5FiLfgVjBiDcfd2ffWhYCph-xThQ-xpTUmKRxGCIh_-8XfttMbS-bsdKaAyNADH8pf7YT7oesXJYcwGirOfh_4h4qP_nUq6SAYTxwE=
  - Misr Oils & Soap (MOSC.CA) - Decisions of the BoD Meeting (August 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmiI-dkIxTPRKOX6d-3_bnZ1-CWq7lEvYc3NFGR2Wke-jroXrkWEbpsSBpPrE3LnO0a5aRRWH5FumZFyzcDyQmpdUsHyyukpnk4ElJZPDoRDSzB4m2H2cLgDJlb5xhRCijunyYf41xH6qZLEcnxcQ==
- EGCH.CA: status=RECENT_ACCEPTED latest=2026-05-03 age_days=99 sources=3 expected=Egyptian Chemical Industries Kima summary=Egyptian Chemical Industries Kima (EGCH.CA) has reported varying profit results in recent quarters and fiscal years, along with strategic decisions regarding land sales. The company's stock price has also seen recent movements.
  - Kima sees 34.5% YoY lower profits in 9 months (May 3, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExsDUUOelWiOCq4Gam9tsUNzFHUBfz6UpjVCZJQJSu8uEYmLh0Jnt8BwAMw6B8Ee76Cc8pbkhDPcz-gk5UVNFMNWYsq8EKP-WWV0VO4UotEj9WS7-2pi_wmpDowzlANn3HG16CMlpxyje3hrqjJ1bqCg==
  - KIMA targets EGP 1.5B in profits for FY2026/27 (March 3, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExsDUUOelWiOCq4Gam9tsUNzFHUBfz6UpjVCZJQJSu8uEYmLh0Jnt8BwAMw6B8Ee76Cc8pbkhDPcz-gk5UVNFMNWYsq8EKP-WWV0VO4UotEj9WS7-2pi_wmpDowzlANn3HG16CMlpxyje3hrqjJ1bqCg==
  - KIMA's profits surge 46.89% YoY in H1 FY2025/26 (January 28, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExsDUUOelWiOCq4Gam9tsUNzFHUBfz6UpjVCZJQJSu8uEYmLh0Jnt8BwAMw6B8Ee76Cc8pbkhDPcz-gk5UVNFMNWYsq8EKP-WWV0VO4UotEj9WS7-2pi_wmpDowzlANn3HG16CMlpxyje3hrqjJ1bqCg==
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- CLHO.CA: status=RECENT_ACCEPTED latest=2026-08-10 age_days=0 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospital Group (CLHO.CA) has demonstrated strong financial performance in the last 12 months, with significant revenue and profit growth. The company has also been active with capital investments, hospital openings, and regular investor communications.
  - Cleopatra Hospitals Group Reports EGP 7.58 Billion Revenue and EGP 587.34 Million Profits in Last 12 Months (July 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBrtR7V-Jb9Z4qKed9ovVd5uIeqGS2KznEKH1c_gkZJmg8ONRLSZXb6R2XPWy9i6TZzmItoomXolnCsGkEWpmGtniG6LLzoZkuT7E1aDzIMNd8dSQhXkliBdKARBKBW5KFK7P86yFPtIbGXT5VJg==
  - Cleopatra Hospital Company Stock Price Increased by 98.77% Over Last Year (August 10, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8X4WYZXZft3MLAcjmk-3ChQ26lpdPeWZdOKgPJ1IXPbdmbN8JkWGqNmElLLHYezSQxogFJ3ZyEvLV1RLTE1zS7MoJWKHpTvyUhtfDNjAVv6OgNWclaGK0uVErHDmwCIZ4U8SLTKgo4ddZuz3b5iyRQ5c2LMcHOWNjSltM0h1zsBz0zzqFAw==
  - Cleopatra Hospital Group Q1 2026 Earnings Release: EPS EGP 0.08, Revenue EGP 1.97 Billion (June 8, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECMJ9JeomVSOjqPh0hYLjcp3yJ55zUap-lTaLnLuc0XsluwwdkjW6u2oWYLQ8SFXX1Ofx6ZyhWztcV6FqWwNGLHmr8Rh7zGVmkQ2VzWWyOrelC9wdx7ndG_wpvHr8PHIl_zUmQn1YYy8JoTTbu4YwpD0v-LGEP13pkoFYTWpIwe7s=
- MTIE.CA: status=RECENT_ACCEPTED latest=2026-03-31 age_days=132 sources=3 expected=MM Group For Industry and International Trade summary=MM Group For Industry and International Trade (MTIE.CA) has reported solid financial results for Q1 2026, Q4 2025, Q3 2025, and H1 2025. The company has also announced stock dividends and upcoming earnings reports.
  - MM Group For Industry And International Trade Q1 2026 Consolidated Net Profit EGP 318.2 Million (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQM-6XXSdxzMABPO48cvhAP41d85ytVGEG7CAMx0OEcUScFd5mKMUJuidSTnj0omAIq3Frc2vBRGGxcRrOfg09s8tuT-6xcG0wOxfE55odPrr7xRiozLdZOXq5XbMAOzF0bI0fT4KlN6dD9G_e3T6mEzU=
  - MM Group for Industry and International Trade S.A.E. Balance Sheet (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFI4vqfcWVdRbpcKQAZrZnzkyu9Vo7poIazeIIV2vx31vuUzk2SdXIvryAYKQApHHn7qWnkSUQY7WNi7JG6PVJ9y0de7CgqyJn4JQi0C6teH-CPuC4phMShMD83mUj43crTLrXL8KXdMpNFvqGc2MonVSc9Zg6ImNpg1CrC
  - MM Group for Industry Q3 2025 Consolidated Profit EGP 381 Million (November 17, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb_WbJDzeOvrItsv5Oxx8Er0gxlmnYZWeuDpdt1lCnrBx0wMf4n90Erx5pgyNd6YjGpeOm0W1_3wwni3YWtsIBp6BvqMGDDyyAIcVcdgIrqMhS1JSJaSMiUypmZlif0i4vqRc27XGToS7rKOWlHaqAWw9cppCzsRTbZgjItPsuPwrqmzfa4wbCghxzYrux5tNxvriEOUgKeTUCDA==
- HRHO.CA: status=RECENT_ACCEPTED latest=2025-11-19 age_days=264 sources=3 expected=EFG Holding summary=EFG Holding (HRHO.CA) has reported its full-year 2025 financial results, along with Q2 and Q3 2025 profits. The company has also made recent announcements regarding cash dividends, shareholder meetings, and strategic advisory roles.
  - EFG Holding Company S.A.E. FY 2025 Revenue EGP 26.57 Billion, Earnings EGP 4.06 Billion (2025 Fiscal Year): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpjw0VK0zObaiWAComybPxKDAkoigPVqfMB1ImQLEsKmTNxN7zPb3_b8zRzUVSGukavIBZgUP6ea1rGe6EeYDDnjSKKqds8Pkyi0RT3_Z9jSw3dmjYxhAr7UX1Yqt8BFONpzg==
  - EFG Holding Reports Q3 2025 Profit of EGP 846 Million (November 19, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8mUdSdkIfgrpZ5raqC6b4pAg2z_XujNEd5WB65ancH5j7R2_Duv0S8BK2fjaGSDH6mDNsiPS5cUtEGGgk6Jnn0AlABFcl0bR6cyxusVObrb-lYUKKe_7PPnMGd_SNmad-29MAzRwD5Z4EJA==
  - EFG Holding Reports Q2 2025 Profit Growth of 2% to EGP 802 Million (August 14, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8mUdSdkIfgrpZ5raqC6b4pAg2z_XujNEd5WB65ancH5j7R2_Duv0S8BK2fjaGSDH6mDNsiPS5cUtEGGgk6Jnn0AlABFcl0bR6cyxusVObrb-lYUKKe_7PPnMGd_SNmad-29MAzRwD5Z4EJA==

## Warnings
- Evidence for ALUM.CA matches the company but no source/report date was detected.
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
