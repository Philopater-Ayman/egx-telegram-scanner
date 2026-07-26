# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-26T10:01:13.362913+00:00
Generated Cairo: 2026-07-26 13:01
Run timing: target 11:00 Cairo | generated Cairo 2026-07-26 13:01 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-26 12:53

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 58
- Data quality issues: 1
- Tradeable price/liquidity tickers: 184/189
- Top sector: Textiles

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, July 26
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 75.0% / above MA50 55.0%
- EGX70 regime: BULLISH / above MA20 77.5% / above MA50 80.0%
- Sector breadth: 57.14%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- CCAP.CA: liquidity=474916800.0 spike=0.7 score=25.9
- MCRO.CA: liquidity=208050128.0 spike=2.27 score=26.44
- DTPP.CA: liquidity=160505696.0 spike=2.72 score=14.34
- ELSH.CA: liquidity=145772096.0 spike=1.12 score=26.14
- ABUK.CA: liquidity=137310000.0 spike=0.89 score=24.2

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner prioritized ARVA.CA, SAUD.CA and CANA.CA as watch/buy setups because each trades above its MA20/MA50, shows adequate liquidity spikes, and carries a bullish‑watch outlook despite a bearish macro trend; EGX30 and EGX70 remain bullish, keeping risk mode broad risk‑on but with caution due to extended momentum.
- ARVA.CA: price 12.19 above MA20/MA50, RSI 63.5, liquidity spike 4.3×, support 10.5 / resistance 11.98; bullish watch outlook, momentum extended adds uncertainty for the next 1‑3 days.

## Top Liquidity Spikes
- TRTO.CA: spike=6.87 liquidity=6936.0 outlook=NEUTRAL score=45.61 buy_ready=False
- SDTI.CA: spike=6.52 liquidity=35319468.0 outlook=BULLISH_WATCH score=75.61 buy_ready=False
- AJWA.CA: spike=6.16 liquidity=58322720.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- IFAP.CA: spike=4.48 liquidity=30031566.0 outlook=BULLISH_WATCH score=89.5 buy_ready=True
- SAUD.CA: spike=4.44 liquidity=30503640.0 outlook=BULLISH_WATCH score=83.19 buy_ready=True

## Sector Leaderboard
- #1 Textiles: score=11.9 5d=5.58% 20d=12.01% aboveMA50=100.0%
- #2 Building Materials: score=10.91 5d=4.89% 20d=11.45% aboveMA50=83.33%
- #3 Industrial Goods & Cables: score=10.39 5d=1.72% 20d=5.64% aboveMA50=100.0%
- #4 Fintech & Payments: score=9.05 5d=4.96% 20d=7.23% aboveMA50=50.0%
- #5 Telecommunications: score=8.86 5d=2.64% 20d=5.29% aboveMA50=100.0%
- #6 General / Verified EGX Expansion: score=8.61 5d=2.95% 20d=8.89% aboveMA50=83.5%
- #7 Agriculture & Food Production: score=8.5 5d=-2.25% 20d=-1.18% aboveMA50=100.0%
- #8 Healthcare: score=8.31 5d=3.16% 20d=3.89% aboveMA50=83.33%

## Today's Prioritized Action Tickets
- Priority #1: BUY ARVA.CA
  - Entry: 12.19 | Take profit: 13.17 | Stop loss: 11.7
  - Confidence: LOW | score=34.9 | outlook=BULLISH_WATCH 89.61
  - Reason: WATCH/BUY SETUP: ARVA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 63.48, support 10.5, resistance 11.98, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY SAUD.CA
  - Entry: 22.49 | Take profit: 24.29 | Stop loss: 21.59
  - Confidence: LOW | score=32.9 | outlook=BULLISH_WATCH 83.19
  - Reason: WATCH/BUY SETUP: SAUD.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 66.67, support 19.99, resistance 22.16, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY CANA.CA
  - Entry: 38.11 | Take profit: 41.15 | Stop loss: 36.59
  - Confidence: LOW | score=31.3 | outlook=BULLISH_WATCH 89.19
  - Reason: WATCH/BUY SETUP: CANA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 62.43, support 34.7, resistance 37.5, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ARCC.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARVA.CA: BULLISH_WATCH score=89.61 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- ISMA.CA: BULLISH_WATCH score=89.61 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- IFAP.CA: BULLISH_WATCH score=89.5 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- CANA.CA: BULLISH_WATCH score=89.19 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- SWDY.CA: BULLISH_WATCH score=87 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- ATQA.CA: BULLISH_WATCH score=86.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- SPIN.CA: BULLISH_WATCH score=85 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- EALR.CA: BULLISH_WATCH score=84.61 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ASCM.CA: BULLISH_WATCH score=84.61 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- ARVA.CA: rank=34.9 outlook=BULLISH_WATCH outlook_score=89.61 sector_rank=6 price=12.19 support=10.5 resistance=11.98 liquidity=84475888.0
- SAUD.CA: rank=32.9 outlook=BULLISH_WATCH outlook_score=83.19 sector_rank=13 price=22.49 support=19.99 resistance=22.16 liquidity=30503640.0
- CANA.CA: rank=31.3 outlook=BULLISH_WATCH outlook_score=89.19 sector_rank=13 price=38.11 support=34.7 resistance=37.5 liquidity=25410694.0
- ORWE.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=76 sector_rank=1 price=23.03 support=21.95 resistance=23.47 liquidity=15602589.0
- IFAP.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=89.5 sector_rank=7 price=19.8 support=18.47 resistance=20.0 liquidity=30031566.0
- ARCC.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=90 sector_rank=2 price=57.09 support=53.5 resistance=58.5 liquidity=14621508.0
- PRCL.CA: rank=28.74 outlook=BULLISH_WATCH outlook_score=77 sector_rank=2 price=36.86 support=28.92 resistance=38.25 liquidity=70580680.0
- RMDA.CA: rank=28.64 outlook=BULLISH_WATCH outlook_score=84.31 sector_rank=8 price=5.1 support=4.81 resistance=5.15 liquidity=44857060.0
- ATQA.CA: rank=28.5 outlook=BULLISH_WATCH outlook_score=86.25 sector_rank=17 price=10.0 support=9.21 resistance=9.97 liquidity=52310264.0
- IDRE.CA: rank=28.26 outlook=BULLISH_WATCH outlook_score=75.61 sector_rank=6 price=48.44 support=41.1 resistance=52.68 liquidity=24984588.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=25.9 buy_ready=True sector_rank=6 price=242.54 support=196.0 resistance=253.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=67.83 liquidity=12859787.0 spike=0.71
- ABUK.CA: score=24.2 buy_ready=False sector_rank=17 price=71.45 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=63.47 liquidity=137310000.0 spike=0.89
- ACAMD.CA: score=24.9 buy_ready=False sector_rank=6 price=2.43 support=2.14 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=76.92 liquidity=28851996.0 spike=0.37
- ACGC.CA: score=27.92 buy_ready=False sector_rank=1 price=10.77 support=8.92 resistance=10.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=78.17 liquidity=28374868.0 spike=1.01
- ADCI.CA: score=20.58 buy_ready=False sector_rank=6 price=257.01 support=230.0 resistance=266.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=70.91 liquidity=2681151.0 spike=0.24
- ADIB.CA: score=27.9 buy_ready=True sector_rank=13 price=48.79 support=44.1 resistance=49.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=64.55 liquidity=19773686.0 spike=0.17
- ADPC.CA: score=24.9 buy_ready=False sector_rank=6 price=4.02 support=3.32 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=87.06 liquidity=15996101.0 spike=0.53
- AFDI.CA: score=25.35 buy_ready=False sector_rank=6 price=48.47 support=41.84 resistance=49.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=7452007.0 spike=0.52
- AFMC.CA: score=23.06 buy_ready=False sector_rank=6 price=104.2 support=66.0 resistance=127.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=80.16 liquidity=27119984.0 spike=1.08
- AJWA.CA: score=15.9 buy_ready=False sector_rank=6 price=183.16 support=175.0 resistance=189.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58322720.0 spike=6.16
- ALCN.CA: score=19.04 buy_ready=True sector_rank=9 price=29.71 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=69.4 liquidity=3139952.75 spike=0.14
- ALUM.CA: score=17.58 buy_ready=False sector_rank=6 price=23.48 support=20.55 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=71.91 liquidity=1683897.25 spike=0.24
- AMER.CA: score=24.9 buy_ready=False sector_rank=10 price=4.23 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=89.87 liquidity=15777051.0 spike=0.15
- AMES.CA: score=25.9 buy_ready=False sector_rank=6 price=118.06 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=71.65 liquidity=15736384.0 spike=0.16
- AMIA.CA: score=22.1 buy_ready=False sector_rank=6 price=10.41 support=8.4 resistance=10.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=76.94 liquidity=9196056.0 spike=0.77
- AMOC.CA: score=27.9 buy_ready=True sector_rank=12 price=8.4 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=67.05 liquidity=26642732.0 spike=0.46
- APSW.CA: score=18.07 buy_ready=True sector_rank=6 price=8.77 support=8.0 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=64.24 liquidity=1173530.0 spike=0.81
- ARAB.CA: score=25.9 buy_ready=True sector_rank=10 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=64.37 liquidity=100915064.0 spike=0.82
- ARCC.CA: score=29.9 buy_ready=True sector_rank=2 price=57.09 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=58.08 liquidity=14621508.0 spike=0.57
- AREH.CA: score=20.21 buy_ready=False sector_rank=6 price=1.49 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=43.4 liquidity=9313635.0 spike=0.25
- ARVA.CA: score=34.9 buy_ready=True sector_rank=6 price=12.19 support=10.5 resistance=11.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=84475888.0 spike=4.32
- ASCM.CA: score=22.41 buy_ready=True sector_rank=6 price=61.32 support=56.29 resistance=65.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=58.68 liquidity=6513723.0 spike=0.12
- ASPI.CA: score=23.27 buy_ready=False sector_rank=6 price=0.37 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=78.75 liquidity=8367974.0 spike=0.35
- ATLC.CA: score=16.65 buy_ready=False sector_rank=15 price=5.2 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=2752411.0 spike=0.39
- ATQA.CA: score=28.5 buy_ready=True sector_rank=17 price=10.0 support=9.21 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=66.38 liquidity=52310264.0 spike=1.65
- AXPH.CA: score=18.64 buy_ready=False sector_rank=6 price=1222.95 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=53.16 liquidity=739395.75 spike=0.19
- BINV.CA: score=18.37 buy_ready=False sector_rank=11 price=47.11 support=44.98 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=56.82 liquidity=4470402.5 spike=0.65
- BIOC.CA: score=22.94 buy_ready=False sector_rank=6 price=121.87 support=66.75 resistance=137.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=78.79 liquidity=30741336.0 spike=1.02
- BTFH.CA: score=23.9 buy_ready=True sector_rank=15 price=3.08 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=63.04 liquidity=78332384.0 spike=0.38
- CAED.CA: score=22.9 buy_ready=False sector_rank=6 price=122.29 support=68.0 resistance=134.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=80.57 liquidity=13772627.0 spike=0.27
- CANA.CA: score=31.3 buy_ready=True sector_rank=13 price=38.11 support=34.7 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=62.43 liquidity=25410694.0 spike=1.7
- CCAP.CA: score=25.9 buy_ready=False sector_rank=11 price=5.62 support=4.65 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=73.96 liquidity=474916800.0 spike=0.7
- CCRS.CA: score=25.9 buy_ready=False sector_rank=6 price=2.73 support=2.18 resistance=2.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=14864046.0 spike=0.92
- CEFM.CA: score=20.55 buy_ready=True sector_rank=6 price=123.52 support=95.75 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=69.93 liquidity=4653593.0 spike=0.33
- CERA.CA: score=27.9 buy_ready=True sector_rank=6 price=1.36 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=11096854.0 spike=0.45
- CFGH.CA: score=21.04 buy_ready=False sector_rank=6 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=73.68 liquidity=35526.7 spike=3.05
- CICH.CA: score=22.39 buy_ready=True sector_rank=15 price=12.16 support=11.52 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=59.7 liquidity=4489230.5 spike=0.95
- CIEB.CA: score=18.29 buy_ready=True sector_rank=13 price=24.17 support=23.3 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=2387783.75 spike=0.29
- CIRA.CA: score=25.9 buy_ready=True sector_rank=14 price=32.06 support=27.45 resistance=33.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=67.73 liquidity=10062917.0 spike=0.28
- CLHO.CA: score=22.52 buy_ready=True sector_rank=8 price=16.88 support=15.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=63.04 liquidity=4616198.5 spike=0.09
- CNFN.CA: score=18.77 buy_ready=True sector_rank=15 price=4.86 support=4.61 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=2873894.75 spike=0.11
- COMI.CA: score=27.9 buy_ready=False sector_rank=13 price=138.83 support=126.21 resistance=140.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=72.02 liquidity=59060168.0 spike=0.14
- COPR.CA: score=25.58 buy_ready=False sector_rank=6 price=0.41 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=78.79 liquidity=44639908.0 spike=1.84
- COSG.CA: score=24.9 buy_ready=False sector_rank=6 price=1.73 support=1.47 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=85.19 liquidity=16620654.0 spike=0.4
- CPCI.CA: score=17.07 buy_ready=False sector_rank=6 price=466.64 support=369.52 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=1169290.88 spike=0.1
- CSAG.CA: score=23.27 buy_ready=True sector_rank=9 price=33.02 support=30.92 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=5366033.0 spike=0.26
- DAPH.CA: score=27.9 buy_ready=False sector_rank=6 price=93.92 support=78.52 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=72.8 liquidity=13710974.0 spike=0.77
- DEIN.CA: score=0.9 buy_ready=False sector_rank=6 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=17.09 buy_ready=True sector_rank=18 price=27.07 support=26.06 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=42.91 liquidity=2230011.5 spike=0.6
- DSCW.CA: score=22.9 buy_ready=False sector_rank=6 price=1.94 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=87.1 liquidity=30291238.0 spike=0.61
- DTPP.CA: score=14.34 buy_ready=False sector_rank=6 price=259.99 support=225.11 resistance=265.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=160505696.0 spike=2.72
- EALR.CA: score=27.9 buy_ready=True sector_rank=6 price=365.77 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=58.95 liquidity=11141442.0 spike=0.67
- EASB.CA: score=25.62 buy_ready=True sector_rank=6 price=8.0 support=6.88 resistance=8.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=58.8 liquidity=9723695.0 spike=0.61
- EAST.CA: score=16.91 buy_ready=False sector_rank=18 price=37.14 support=36.11 resistance=39.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=51.23 liquidity=6053391.5 spike=0.1
- EBSC.CA: score=9.95 buy_ready=False sector_rank=6 price=1.87 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=18.92 liquidity=1049160.5 spike=0.15
- ECAP.CA: score=18.19 buy_ready=True sector_rank=6 price=33.43 support=31.52 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=59.27 liquidity=2289650.5 spike=0.29
- EDFM.CA: score=14.06 buy_ready=False sector_rank=6 price=385.89 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=80.85 liquidity=1159188.0 spike=0.28
- EEII.CA: score=25.58 buy_ready=True sector_rank=6 price=2.72 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=65.0 liquidity=9681937.0 spike=0.45
- EFIC.CA: score=13.88 buy_ready=False sector_rank=17 price=186.24 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=2678580.25 spike=0.25
- EFID.CA: score=19.86 buy_ready=False sector_rank=18 price=27.59 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=53.96 liquidity=13622449.0 spike=0.33
- EFIH.CA: score=26.4 buy_ready=True sector_rank=4 price=23.6 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=69.87 liquidity=64370724.0 spike=1.25
- EGAL.CA: score=24.2 buy_ready=False sector_rank=17 price=298.83 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=25059806.0 spike=0.58
- EGAS.CA: score=26.58 buy_ready=True sector_rank=12 price=53.27 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=65.74 liquidity=16074756.0 spike=1.34
- EGBE.CA: score=19.98 buy_ready=False sector_rank=13 price=0.49 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=97.44 liquidity=75770.38 spike=4.03
- EGCH.CA: score=24.2 buy_ready=False sector_rank=17 price=13.16 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=64.81 liquidity=39932088.0 spike=0.74
- EGSA.CA: score=15.91 buy_ready=False sector_rank=5 price=8.98 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=12021.88 spike=0.76
- EGTS.CA: score=19.92 buy_ready=False sector_rank=10 price=17.51 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=9019791.0 spike=0.19
- EHDR.CA: score=25.9 buy_ready=True sector_rank=6 price=2.86 support=2.37 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=69.32 liquidity=13341650.0 spike=0.37
- EKHO.CA: score=9.9 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=25.9 buy_ready=True sector_rank=3 price=2.23 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=19154856.0 spike=0.3
- ELKA.CA: score=22.9 buy_ready=False sector_rank=6 price=2.03 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=82.86 liquidity=35691796.0 spike=0.53
- ELNA.CA: score=14.45 buy_ready=False sector_rank=6 price=38.48 support=35.55 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:25 AM market time freshness=DELAYED_CURRENT RSI=55.92 liquidity=553929.56 spike=0.85
- ELSH.CA: score=26.14 buy_ready=False sector_rank=6 price=15.28 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=74.08 liquidity=145772096.0 spike=1.12
- ELWA.CA: score=11.67 buy_ready=False sector_rank=6 price=1.89 support=1.87 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=766191.5 spike=0.63
- EMFD.CA: score=23.9 buy_ready=False sector_rank=10 price=11.7 support=11.24 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=15281689.0 spike=0.23
- ENGC.CA: score=25.9 buy_ready=False sector_rank=6 price=41.23 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=71.46 liquidity=15352482.0 spike=0.62
- EOSB.CA: score=15.92 buy_ready=False sector_rank=6 price=1.48 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=18812.28 spike=0.41
- EPCO.CA: score=25.42 buy_ready=False sector_rank=6 price=11.27 support=8.5 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=85.93 liquidity=31826834.0 spike=1.26
- EPPK.CA: score=19.75 buy_ready=True sector_rank=6 price=15.69 support=12.37 resistance=15.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=58.99 liquidity=1450511.25 spike=1.2
- ETEL.CA: score=22.9 buy_ready=False sector_rank=5 price=102.53 support=89.01 resistance=106.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=79.14 liquidity=17585436.0 spike=0.23
- ETRS.CA: score=19.79 buy_ready=False sector_rank=6 price=10.8 support=10.18 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=56.99 liquidity=5886757.0 spike=0.1
- EXPA.CA: score=22.9 buy_ready=False sector_rank=13 price=19.9 support=18.03 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=82.66 liquidity=22133300.0 spike=0.74
- FAIT.CA: score=20.7 buy_ready=False sector_rank=13 price=37.66 support=35.06 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=64.74 liquidity=798929.69 spike=0.28
- FAITA.CA: score=10.96 buy_ready=False sector_rank=13 price=0.97 support=0.97 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=36.23 liquidity=43346.1 spike=1.01
- FERC.CA: score=21.92 buy_ready=True sector_rank=17 price=76.97 support=72.75 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=5718488.5 spike=0.53
- FWRY.CA: score=22.9 buy_ready=False sector_rank=4 price=19.02 support=18.13 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=65.85 liquidity=32840468.0 spike=0.24
- GBCO.CA: score=22.42 buy_ready=False sector_rank=19 price=31.13 support=29.5 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=46.04 liquidity=16335196.0 spike=0.21
- GDWA.CA: score=22.8 buy_ready=False sector_rank=6 price=0.88 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=86.27 liquidity=105154872.0 spike=1.45
- GGCC.CA: score=24.9 buy_ready=False sector_rank=6 price=0.88 support=0.42 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=89.68 liquidity=34364036.0 spike=0.99
- GIHD.CA: score=13.04 buy_ready=False sector_rank=6 price=60.76 support=56.66 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90326032.0 spike=2.07
- GMCI.CA: score=18.48 buy_ready=False sector_rank=6 price=2.03 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=60.49 liquidity=584761.79 spike=0.45
- GRCA.CA: score=20.71 buy_ready=False sector_rank=6 price=60.04 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=75.04 liquidity=7809363.5 spike=0.56
- GSSC.CA: score=14.2 buy_ready=False sector_rank=6 price=268.67 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=78.83 liquidity=1298416.63 spike=0.13
- GTWL.CA: score=25.9 buy_ready=True sector_rank=6 price=105.89 support=49.37 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=60.89 liquidity=53240460.0 spike=0.37
- HDBK.CA: score=20.2 buy_ready=False sector_rank=13 price=81.97 support=75.3 resistance=166.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=8297621.0 spike=0.25
- HELI.CA: score=22.9 buy_ready=False sector_rank=10 price=8.41 support=6.36 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=90.71 liquidity=46935588.0 spike=0.26
- HRHO.CA: score=27.9 buy_ready=True sector_rank=15 price=26.98 support=26.09 resistance=27.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=29511960.0 spike=0.28
- ICID.CA: score=16.22 buy_ready=False sector_rank=6 price=8.13 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=50.43 liquidity=318481.03 spike=0.04
- IDRE.CA: score=28.26 buy_ready=True sector_rank=6 price=48.44 support=41.1 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=63.26 liquidity=24984588.0 spike=1.18
- IFAP.CA: score=30.9 buy_ready=True sector_rank=7 price=19.8 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=48.99 liquidity=30031566.0 spike=4.48
- INFI.CA: score=20.4 buy_ready=False sector_rank=6 price=106.0 support=88.51 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=74.79 liquidity=4495397.5 spike=0.32
- IRON.CA: score=7.4 buy_ready=False sector_rank=17 price=31.26 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=29.74 liquidity=3203868.75 spike=0.49
- ISMA.CA: score=26.52 buy_ready=True sector_rank=6 price=28.99 support=26.54 resistance=30.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=22373748.0 spike=1.31
- ISMQ.CA: score=23.2 buy_ready=False sector_rank=17 price=9.29 support=8.1 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=20560888.0 spike=0.17
- ISPH.CA: score=24.9 buy_ready=False sector_rank=8 price=11.66 support=11.2 resistance=12.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=55.37 liquidity=31188642.0 spike=0.59
- JUFO.CA: score=19.86 buy_ready=False sector_rank=18 price=29.3 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=39.85 liquidity=20817118.0 spike=0.94
- KABO.CA: score=27.9 buy_ready=False sector_rank=1 price=8.57 support=6.04 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=96.93 liquidity=23905946.0 spike=0.54
- KWIN.CA: score=24.9 buy_ready=False sector_rank=6 price=101.64 support=65.0 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=93.14 liquidity=33361390.0 spike=0.77
- KZPC.CA: score=15.63 buy_ready=False sector_rank=6 price=8.6 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=56.12 liquidity=1727436.5 spike=0.33
- LCSW.CA: score=24.9 buy_ready=False sector_rank=2 price=34.33 support=27.01 resistance=35.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=78.41 liquidity=73646616.0 spike=0.98
- LUTS.CA: score=23.9 buy_ready=False sector_rank=6 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=19925040.0 spike=0.57
- MAAL.CA: score=18.79 buy_ready=False sector_rank=6 price=8.72 support=6.64 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=85.44 liquidity=7889648.0 spike=0.42
- MASR.CA: score=22.9 buy_ready=False sector_rank=6 price=8.31 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=81.63 liquidity=25735942.0 spike=0.31
- MBSC.CA: score=23.8 buy_ready=False sector_rank=2 price=245.63 support=222.66 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=6895733.5 spike=0.36
- MCQE.CA: score=23.88 buy_ready=False sector_rank=2 price=188.09 support=166.66 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=71.15 liquidity=5981521.5 spike=0.34
- MCRO.CA: score=26.44 buy_ready=False sector_rank=6 price=1.52 support=1.17 resistance=1.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=82.05 liquidity=208050128.0 spike=2.27
- MENA.CA: score=16.76 buy_ready=False sector_rank=10 price=7.01 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=53.66 liquidity=862982.69 spike=0.11
- MEPA.CA: score=22.9 buy_ready=False sector_rank=6 price=1.91 support=1.52 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=80.7 liquidity=24689136.0 spike=0.59
- MFPC.CA: score=25.02 buy_ready=False sector_rank=17 price=36.81 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=57.88 liquidity=125315120.0 spike=1.41
- MFSC.CA: score=12.22 buy_ready=False sector_rank=6 price=47.01 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=6315165.0 spike=1.0
- MHOT.CA: score=17.63 buy_ready=False sector_rank=21 price=16.64 support=16.12 resistance=35.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=43.13 liquidity=9727713.0 spike=0.83
- MICH.CA: score=24.9 buy_ready=False sector_rank=6 price=40.46 support=34.0 resistance=41.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=12529164.0 spike=0.87
- MILS.CA: score=24.56 buy_ready=False sector_rank=6 price=169.86 support=126.31 resistance=197.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=71.49 liquidity=8657142.0 spike=0.26
- MIPH.CA: score=13.75 buy_ready=False sector_rank=8 price=747.11 support=630.13 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=77.75 liquidity=848755.5 spike=0.24
- MOED.CA: score=24.52 buy_ready=True sector_rank=6 price=0.71 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=64.75 liquidity=23539992.0 spike=1.31
- MOIL.CA: score=15.64 buy_ready=False sector_rank=12 price=0.59 support=0.46 resistance=0.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=86.49 liquidity=538208.5 spike=1.1
- MOIN.CA: score=13.98 buy_ready=False sector_rank=6 price=23.82 support=22.6 resistance=24.76 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=52.66 liquidity=83131.8 spike=0.11
- MOSC.CA: score=22.76 buy_ready=True sector_rank=6 price=288.17 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=64.22 liquidity=4860662.0 spike=0.4
- MPCI.CA: score=24.9 buy_ready=False sector_rank=6 price=286.07 support=222.55 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=75.99 liquidity=56559080.0 spike=0.55
- MPCO.CA: score=25.9 buy_ready=True sector_rank=7 price=1.85 support=1.7 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=19548406.0 spike=0.37
- MPRC.CA: score=25.9 buy_ready=False sector_rank=6 price=44.27 support=36.21 resistance=45.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=72.88 liquidity=13963124.0 spike=0.33
- MTIE.CA: score=15.89 buy_ready=False sector_rank=19 price=9.33 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=3465166.5 spike=0.16
- NAHO.CA: score=9.91 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=6253.55 spike=0.19
- NCCW.CA: score=23.94 buy_ready=True sector_rank=6 price=6.61 support=5.82 resistance=6.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=6035124.5 spike=0.28
- NEDA.CA: score=13.37 buy_ready=False sector_rank=6 price=2.76 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=60.53 liquidity=466289.81 spike=0.7
- NHPS.CA: score=24.9 buy_ready=False sector_rank=6 price=90.73 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=82.88 liquidity=32852778.0 spike=0.4
- NINH.CA: score=25.05 buy_ready=False sector_rank=6 price=21.91 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=72.84 liquidity=9145112.0 spike=0.23
- NIPH.CA: score=24.9 buy_ready=False sector_rank=8 price=236.7 support=157.01 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=82.45 liquidity=62691120.0 spike=0.44
- OBRI.CA: score=20.9 buy_ready=False sector_rank=6 price=35.22 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=13979449.0 spike=0.38
- OCDI.CA: score=23.9 buy_ready=True sector_rank=10 price=26.7 support=22.86 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=57662740.0 spike=0.53
- OCPH.CA: score=20.16 buy_ready=False sector_rank=6 price=455.09 support=341.11 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=92.31 liquidity=7260813.5 spike=0.32
- ODIN.CA: score=22.06 buy_ready=False sector_rank=6 price=2.65 support=2.05 resistance=2.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=79.75 liquidity=7157662.5 spike=0.46
- OFH.CA: score=24.9 buy_ready=False sector_rank=6 price=0.71 support=0.57 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=84.39 liquidity=23149370.0 spike=0.39
- OIH.CA: score=25.11 buy_ready=False sector_rank=11 price=1.47 support=1.39 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=9208450.0 spike=0.14
- OLFI.CA: score=26.86 buy_ready=False sector_rank=18 price=23.45 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=71.11 liquidity=17794208.0 spike=0.52
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=705.77 support=705.3 resistance=713.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49119932.0 spike=1.0
- ORHD.CA: score=25.9 buy_ready=True sector_rank=10 price=40.5 support=37.0 resistance=40.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=65.49 liquidity=88568912.0 spike=0.58
- ORWE.CA: score=30.9 buy_ready=True sector_rank=1 price=23.03 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=63.27 liquidity=15602589.0 spike=0.68
- PHAR.CA: score=27.9 buy_ready=True sector_rank=8 price=91.85 support=83.6 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=66.24 liquidity=25947926.0 spike=0.96
- PHDC.CA: score=20.9 buy_ready=False sector_rank=10 price=14.84 support=14.26 resistance=15.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=59.58 liquidity=61116732.0 spike=0.26
- PHTV.CA: score=14.14 buy_ready=False sector_rank=6 price=311.01 support=243.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=75.12 liquidity=1239052.75 spike=0.16
- POUL.CA: score=20.82 buy_ready=False sector_rank=18 price=38.0 support=36.52 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=54.32 liquidity=7963610.5 spike=0.22
- PRCL.CA: score=28.74 buy_ready=True sector_rank=2 price=36.86 support=28.92 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=70580680.0 spike=1.42
- PRDC.CA: score=25.9 buy_ready=True sector_rank=10 price=9.5 support=6.8 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=69.19 liquidity=44370844.0 spike=0.36
- PRMH.CA: score=26.16 buy_ready=True sector_rank=6 price=2.65 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=64.44 liquidity=8257757.0 spike=0.44
- RACC.CA: score=18.27 buy_ready=False sector_rank=6 price=10.0 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=4367575.0 spike=0.21
- RAKT.CA: score=13.98 buy_ready=False sector_rank=6 price=22.64 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=62.22 liquidity=83518.96 spike=0.29
- RAYA.CA: score=23.24 buy_ready=False sector_rank=16 price=7.63 support=7.01 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=51.09 liquidity=48561484.0 spike=0.36
- RMDA.CA: score=28.64 buy_ready=True sector_rank=8 price=5.1 support=4.81 resistance=5.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=44857060.0 spike=2.37
- ROTO.CA: score=26.62 buy_ready=True sector_rank=6 price=44.3 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=56.41 liquidity=29533696.0 spike=1.36
- RREI.CA: score=23.9 buy_ready=False sector_rank=6 price=3.88 support=3.34 resistance=4.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=70.15 liquidity=25528150.0 spike=0.92
- RTVC.CA: score=18.33 buy_ready=True sector_rank=6 price=3.98 support=3.55 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=2426871.5 spike=0.54
- RUBX.CA: score=22.72 buy_ready=True sector_rank=6 price=13.2 support=10.26 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=58.99 liquidity=6819285.5 spike=0.09
- SAUD.CA: score=32.9 buy_ready=True sector_rank=13 price=22.49 support=19.99 resistance=22.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=30503640.0 spike=4.44
- SCEM.CA: score=27.22 buy_ready=False sector_rank=2 price=82.73 support=60.14 resistance=82.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=82.26 liquidity=63380456.0 spike=1.16
- SCFM.CA: score=22.12 buy_ready=True sector_rank=6 price=271.38 support=230.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=64.76 liquidity=4221421.0 spike=0.22
- SCTS.CA: score=22.32 buy_ready=False sector_rank=14 price=621.64 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=32.93 liquidity=10616058.0 spike=1.71
- SDTI.CA: score=29.9 buy_ready=False sector_rank=6 price=51.78 support=45.55 resistance=50.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=75.29 liquidity=35319468.0 spike=6.52
- SEIG.CA: score=17.08 buy_ready=False sector_rank=6 price=245.36 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=70.84 liquidity=1183972.25 spike=0.05
- SIPC.CA: score=20.29 buy_ready=False sector_rank=6 price=3.78 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=79.73 liquidity=7391438.0 spike=0.52
- SKPC.CA: score=23.2 buy_ready=False sector_rank=17 price=16.1 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=52.28 liquidity=21659378.0 spike=0.62
- SMFR.CA: score=18.73 buy_ready=False sector_rank=6 price=235.0 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=71.88 liquidity=2830691.75 spike=0.14
- SNFC.CA: score=16.26 buy_ready=False sector_rank=6 price=11.33 support=11.2 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=38.55 liquidity=5355424.0 spike=0.48
- SPIN.CA: score=29.22 buy_ready=False sector_rank=1 price=15.07 support=13.8 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=85.19 liquidity=40141412.0 spike=2.66
- SPMD.CA: score=20.91 buy_ready=True sector_rank=6 price=0.45 support=0.41 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=7007557.0 spike=0.38
- SUGR.CA: score=16.37 buy_ready=False sector_rank=18 price=47.49 support=45.31 resistance=47.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=55.2 liquidity=3513825.25 spike=0.66
- SVCE.CA: score=23.9 buy_ready=False sector_rank=6 price=9.32 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=41.98 liquidity=14697231.0 spike=0.23
- SWDY.CA: score=33.18 buy_ready=False sector_rank=3 price=94.51 support=84.3 resistance=93.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=74.21 liquidity=54152148.0 spike=3.14
- TALM.CA: score=20.83 buy_ready=False sector_rank=14 price=15.75 support=15.27 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=48.63 liquidity=5929789.5 spike=0.41
- TMGH.CA: score=25.9 buy_ready=True sector_rank=10 price=99.52 support=92.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=68.36 liquidity=63581388.0 spike=0.17
- TRTO.CA: score=16.91 buy_ready=False sector_rank=6 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6936.0 spike=6.87
- UEFM.CA: score=16.95 buy_ready=True sector_rank=6 price=540.45 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=67.82 liquidity=1053394.0 spike=0.24
- UEGC.CA: score=17.45 buy_ready=False sector_rank=6 price=2.39 support=1.33 resistance=2.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=90.83 liquidity=4546585.5 spike=0.1
- UNIP.CA: score=22.9 buy_ready=False sector_rank=6 price=0.4 support=0.3 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=81.68 liquidity=16324185.0 spike=0.76
- UNIT.CA: score=24.34 buy_ready=False sector_rank=10 price=18.22 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=70.48 liquidity=8443264.0 spike=0.29
- WCDF.CA: score=18.75 buy_ready=False sector_rank=6 price=575.06 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=849642.25 spike=0.47
- WKOL.CA: score=23.31 buy_ready=True sector_rank=6 price=316.63 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=65.19 liquidity=7409002.5 spike=0.82
- ZEOT.CA: score=18.73 buy_ready=True sector_rank=6 price=11.64 support=10.4 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=66.14 liquidity=4830451.0 spike=0.14
- ZMID.CA: score=25.9 buy_ready=False sector_rank=10 price=7.52 support=6.19 resistance=7.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=72.64 liquidity=72810992.0 spike=0.29

## Backtesting Lite
- ARVA.CA: 180d return=50.71%, max drawdown=-31.83%, MA20>MA50 days last20=20, as_of=2026-07-21T21:00:00+00:00
- SWDY.CA: 180d return=20.8%, max drawdown=-20.2%, MA20>MA50 days last20=15, as_of=2026-07-21T21:00:00+00:00
- SAUD.CA: 180d return=62.92%, max drawdown=-19.12%, MA20>MA50 days last20=0, as_of=2026-07-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ARVA.CA: status=RECENT_ACCEPTED latest=2026-07-21 age_days=5 sources=3 expected=Arab Valves Company summary=Recent evidence for Arab Valves Company (ARVA.CA) from the last 12 months indicates financial performance data, stock price movements, and corporate announcements on the Egyptian Exchange.
  - Arab Valves Company (EGX:ARVA) Statistics & Valuation Metrics (July 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLfUY8WcIkDX3ub7na4lvs7dnb8QK5CiGXrby5lSqHIYtc1ErqbAjUD7XNfyS0CAd-IuQWSaFjRW_RbN8IE-6QhC8g-e6VsGnPsJ4TEA5Sox6cVCqO2ZF0FmjSeiKkVPvrVJHv46XfAR1_HVCD3g==
  - Arab Valves Company (EGX:ARVA) Stock Price & Overview (Jul 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGmQ8C61YepxrUzYPcWAJuorSxz8ntgr0wQcVwX3wit9ccRKLcP1-QFpY-vhHk7lr9VoRfEu8k7err1Hf5k01mDixGW7vYU6jWlApMNK1Ulei5YYpSOiSt-og8THw3zR4q1ZM=
  - Arab Valves Co SAE (ARVA) - Mubasher Info Announcements (July 21, 2026, July 20, 2026, July 5, 2026, June 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE422jFj51uapn6GcgzAlEVoobZya4ob8nIwR7jbd_pvIA4SyMS846gQQRsklP9ULBRpJAcDmH0BkRHHKLIQdv-RYdslrJeUWZEBf9mVhTkKu0F1-p07wqwGq8wq8tlUfUNjyoAnunx72flGkE6gcbA
- SWDY.CA: status=RECENT_ACCEPTED latest=2026-08-12 age_days=0 sources=3 expected=Elsewedy Electric summary=Elsewedy Electric (SWDY.CA) has recent financial reports and corporate announcements from the Egyptian Exchange, detailing its performance and strategic activities.
  - Elsewedy Electric Co SAE (SWDY) - Mubasher Info News (Q1-26 Financial Results, July 19, 2026, July 13, 2026, June 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2zYCkaqrdoopAUY3dTZGKJM1MnGpJSkN60pG2yc4Vt_rWPKjZjObOGF_2QJxrrfQgVqtCDLPcSHHryL5DeDBIuT4FAudQZS69Gs9PUE9K8HZ5bDIOE62SWCmYdhhx61X39jNU_Se0Kb5O592hLPWW
  - El Sewedy Electric Company (EGX:SWDY) Stock Price & Overview (Earnings Date: Aug 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlcWm-BX5muCcCzBCHM9_6LK1tjVxKsANpci2iflYIpGbBKdHFbUZP68TamqGM7x_sZ6QSHltinU3x2CPsz4gBcOhUwq_8GGPDS_zVJRAxnQeMsMCg7mk0NtjfZqlp2HbVl-4=
  - EGX:SWDY Financials | ElSewedy Electric - Investing.com (Trailing Twelve Months and Latest Quarter): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHC8EHps3zqptGtpBWmSdM6qc23Sk2adhQlwt24GtmRW_obg-VL4jJVOSNY0BJ3Yrabx54Qj_UkPdlfRqHKHtGLrtIn7HnbwEuLaMA6eapyAoL2PH2TmLYbfFNLCrPgiUrq0IsA2UhXzB8NUkMmfLnRQBg83a8fQZKbn4ymaA==
- SAUD.CA: status=RECENT_ACCEPTED latest=2026-08-11 age_days=0 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt (SAUD.CA) has released recent financial results and corporate news, including Q1 2026 performance and 2025 consolidated profits.
  - Al Baraka Bank - Egypt News - Mubasher Info (Q1-26, 2025, 2024 Financial Results, May 13, 2026, March 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnVXbbjoPmYi2dt8GcPXRB60fD2J3kTwVpCY_eWjeA9AG0MBjkoucY_3iE0_KowdsjHQNzduPaVi5VQl4lEpybEXH4faXMSWv2558LNotdx8vdP59xsYzClqN9HHWZw_n92bvaSkEZj4ItkyKurVhVmS2p1A==
  - alBaraka Bank Egypt S.A.E. (EGX:SAUD) Stock Price & Overview (Earnings Date: Aug 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFutODfwK3NtEG2UTpH71WC1Klq-hwEpp8jGWjjkGP7sxjotVJ2MixVOP-oY4IAKk3ZKrGyUYhS7RlYUL4lyrZXQerGSdqX16dwwl6lqsI9ceHENuqamSIaE_tcBX4FBThJmuE=
  - EGX:SAUD Financials | Al Baraka Bank - Investing.com (Trailing Twelve Months and Latest Quarter): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZAqWmHW1H2XIwE_Atd--L9oVe1MkmBwttTJTXX9bScCZHO0VrA-hNLl5L75n7O2hSnYD_VjdsJ-JfNwxjE1bLxJ5ApHJl_039COdLwS204F-Vwn2OYyJ-6tUgS6owXv82StOBwJAooJY5RXGOgjlyOnB-IxOLb4JjgWVr4A==
- CANA.CA: status=RECENT_ACCEPTED latest=2026-07-16 age_days=10 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank (CANA.CA) has provided recent earnings reports and corporate actions, including Q1 2026 results and a bonus share approval.
  - Suez Canal Bank (S.A.E) Stock (CANA) - MarketScreener News (May 11, 2026, Mar 24, 2026, Feb 12, 2026, Feb 11, 2026, Nov 13, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0380tThSSuLas38j_H4E-qalKLd9jlgwn6QnQKPoB8Bt03U_iSxZhO635XTMZ12OOdxuFRFaAUSUTzR3CdZZTwZTd7XNYlHRL9dFiJrZkXYEaIH-dvIfFeDR0VG_61OxfkSVs01-zk8655FcnrcfiC21iohy_Wf-YY6bBinQlHvJvXw==
  - Suez Canal Bank SAE (CANA.EG) Live Chart & Key Stats | EGX - mystocks.africa (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHA3uI26eULUULnPG1ain2kG3nlIK85LeZkOhfAEjcTkZNvm7zw3iz0NRFR7ND1HJD1XzH-PfeceKHYCv6na7ifGKhgVrhujETUhNxriUFFg-NjWLusWH3r8bZ-lukpi--P69WmOdyTdvLwgNx_6jgw
  - EGX:CANA Financials | Suez Canal Bank - Investing.com (Trailing Twelve Months and Latest Quarter, Jan 20, 2026, Feb 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIbIWwwZBOJYyTr2xY_bIcTcOWvanB8YoaMpK39g7cC6k5Q09XBUAAkBUhvZvNqNbbkSdp0uCmwCRHa0IdTjV8I0wuiZV4z1Ap3U4yYIhLoOLpmIcKyEmVdS5a8KSdszSwzlYKr-DtKhzg2hAaeqrob8CJH93IHyVDcNNTxA==
- ORWE.CA: status=RECENT_ACCEPTED latest=2026-09-02 age_days=0 sources=3 expected=Oriental Weavers summary=Oriental Weavers (ORWE.CA) has published recent financial results for 2025 and H1 2025, along with various corporate announcements on the Egyptian Exchange.
  - Oriental Weavers Carpets Company (S.A.E) (EGX:ORWE) Statistics & Valuation Metrics (July 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAqjvXIY-Fk4J8lu6M2gKHmMNSo6Died2a3zz6sTBkHSNJ1APhpGvqrk2AqP3Sh3WG4tVX4BTkCgUpPQrt-9IQBi6cTOhrklH1_hwQpinGf5mmDYrxelRJ1FyaIOEZ9f7r23wK9VV_fVOUEsKI_g==
  - Oriental Weavers Announcements - Mubasher Info (March 1, 2026, Jan 19, 2026, Nov 19, 2025, Aug 20, 2025, Aug 13, 2025, July 20, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHz4xCqWaJH5wH4r5qFCxmQ4kUo7ZdZpBih9a1VG8K_R6A5ESG4phCrV9FOJwQpQ4pvOolap9_m3uPAViu2PWWDipFkWyyUoSzocIFbvaJtIPYic4pVzhd4NkIovjSmWklQCmxil0R7vTUGIdv5RpKu2HvmE2g8yciMDlMouIg==
  - Oriental Weavers Carpets Company (S.A.E) (EGX:ORWE) Stock Price & Overview (Earnings Date: Sep 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF70dYAun3_ewQogctKmEnahrnV87454tRXQ38XK5wG5GGaOj5Hfx2fP0feHvgMSRGsr82aVI8J3QLoU7x46SKkY3oDpch3OSi3IYUR3QvP1UEvJ4QUeWypez7J_bttk2W8u5o=
- IFAP.CA: status=RECENT_ACCEPTED latest=2026-07-24 age_days=2 sources=3 expected=International Agricultural Products summary=International Agricultural Products (IFAP.CA) has recent financial statistics, corporate announcements, and an overview of its fiscal year 2025 performance.
  - International Company for Agricultural Crops (EGX:IFAP) Statistics & Valuation Metrics (June 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWhnDJnfoHL46WThFi3eAR9F0K3S502-7Bu5yc3fUKmUalPslqzoZfzYJHWXP_rqWOdRKjdqb_XCilKobgz4NPk2PRAVihUJactSGIRdMGgcG67frdE4NA9hO00F7SVnxtOjjlk12z8skqwvB7-w==
  - International Agricultural Products Stock Overview - Decypha (July 8, 2026, July 7, 2026, June 30, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA6iVp8IIHaNsXY1El9d6vGb-wBTr0k5swe0ZEe8koobH4BaethFj3VWGFvOnnFYkR3OikpzBgQIk0OeU0RjERoMzwMvfxnFn67tOGlfLOl_KDbqrYV-m_Zqq4CN9KqVq4lABF2dc9kmPKyFGl8RGQnURk7A==
  - International Company for Agricultural Crops (EGX:IFAP) Stock Price & Overview (Jul 24, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjwOopapTaFbjcOG-qUEYUvbA26kvUpL3zLDAW0ZnMItqdJy5fF2mYEfLsJu_9MX2thneMsGGHKpF-9NWcwHIYRJbUgPjbojTmUPrpmKIq1cIMf9EWIDqZBE-uK1VmZkO1vLw=
- ARCC.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=0 sources=3 expected=Arabian Cement Company summary=Arabian Cement Company (ARCC.CA) has recent financial performance data for 2025, upcoming earnings dates, and various corporate disclosures on the Egyptian Exchange.
  - Arabian Cement Company (ACC) Announcements - Mubasher Info (July 16, 2026, June 23, 2026, June 1, 2026, May 20, 2026, April 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYKy8D_8PxufRdaNQBD_PbyY51AIiHxIgMjTvX4mBPfQ_0wQjt-USIg3PgHxfVSYYKYEoD-9ddN7ZhXFBSHkWbr-3t2WrudIAN90TeVUInb1ULqvqoB6mRY7FSTtKMLHxLLI_3W1BwiNdbpRXklqxwum0IDvOsJEK8mIpOrqg==
  - The Egyptian Exchange - EGX News & Media Releases (July 16, 2026, July 5, 2026, July 1, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERxBLVJQpsiI1jcfWPG_suEmabm3xjKmsQzywbtwMQ-406Xx8vUfQelJqkHOz8tD_F30Pfe0bx4YdCZMS7Pjxhhe-yz2MqzkV1ccw5iuYW5u_hHltNe0lawnmdHLlau_RyY8jTc_PL74bFJnR8I2w==
  - Arabian Cement Company S.A.E. (EGX:ARCC) Stock Price & Overview (Earnings Date: Aug 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhc43EQH25Tw0suWotPpwz48Q3grPeHo6pRnV3-cv1VMi3O3yCv3syodVTJQo8lWoM5ZaaVrEW1cpNDbRYqos7_4yHhY-UoZX9AEQCxDmyiAIDZPqczSQM5YESzprj4dWgm9U=
- SDTI.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=0 sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=SHARM DREAMS Co. for Touristic Investment S.A.E (SDTI.CA) has reported recent earnings for Q1 2026 and FY 2025, along with other corporate news.
  - SHARM DREAMS Co. for Touristic Investment S.A.E Stock (SDTI) - MarketScreener News (May 25, 2026, Apr 23, 2026, Nov 13, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKfaOkV2cuDRCGqE9fqMxd69ERBMAeNphoMmbSBHSlaIKoujYpK7DdnUrXwgA881_IPuY6lLowol0h13Dylr6veAxyWU4QAf54r2bIAL0PCgXViZlSJK-wyuAnYF7laNYxJaPdcsKa6R5aeccK2HE2ICF2aMByUS3H0D--JLQVIDKlpkCZh_Wp
  - SHARM DREAMS Co. for Touristic Investment S.A.E (EGX:SDTI) Stock Price & Overview (Earnings Date: Aug 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyuL2QSuFoGyadGsb-uA3MG0vOf9yEoo2nxHIgeXlMz7opJ9bIWLbnFaUDmfZ8EO-UZy0zpHMd8VKFjF8i4dcF2rdPqn29W7Au7ZTi2btVQrwyCW5LM3HCeb4f-c5JCx2L8mg=
  - EGX:SDTI Financials | Sharm Dreams Co. - Investing.com (Trailing Twelve Months and Latest Quarter): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNb6ffcnqf_DQ0ucrYhvHtkEwVtiWXUssoNmTKM2zpefYMroNcfWQVch3sDc9ZSjkkewucdUCpbAlt5cnii-ReR1oiekhBmKSsHXuLsRD_-_rp2zybYiQJG4mc76O4VJVNwWcI7Bl8lLbO2WBdtsRscyT1yD8_VbuKg7IFDcYLYdYmVyw8N1gS7o8qAtxn7V4=

## Warnings
- No blocking warnings.
