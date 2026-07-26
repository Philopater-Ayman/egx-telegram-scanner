# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-26T08:47:11.495055+00:00
Generated Cairo: 2026-07-26 11:47
Run timing: target 09:15 Cairo | generated Cairo 2026-07-26 11:47 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-26 11:38

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 56
- Data quality issues: 1
- Tradeable price/liquidity tickers: 183/189
- Top sector: Textiles

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, July 26
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 80.0% / above MA50 55.0%
- EGX70 regime: BULLISH / above MA20 77.5% / above MA50 85.0%
- Sector breadth: 57.14%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- CCAP.CA: liquidity=287847712.0 spike=0.42 score=25.9
- MCRO.CA: liquidity=172167360.0 spike=1.88 score=25.66
- ELSH.CA: liquidity=112396768.0 spike=0.86 score=25.9
- MFPC.CA: liquidity=101194184.0 spike=1.14 score=24.38
- ABUK.CA: liquidity=97026072.0 spike=0.63 score=24.1

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flagged CANA.CA, ARCC.CA and ATQA.CA as watch/buy setups amid a bullish EGX30/EGX70 backdrop but with low confidence due to extended momentum and sector lag.
- Do not mention quantities or position sizing.
- Liquidity above threshold for all three, though ARCC.CA shows cooling and ATQA.CA extended momentum; price sits above MA20/MA50 with RSI 58‑66, near support/resistance levels.
- Outlook: BULLISH_WATCH scores 76‑90 suggest upside potential 1‑3 days if price holds above support (34.7, 53.5, 9.21) and breaks resistance (37.5, 58.5, 9.97); otherwise risk of pull‑back to stop‑loss levels.

## Top Liquidity Spikes
- TRTO.CA: spike=6.87 liquidity=6936.0 outlook=NEUTRAL score=45.43 buy_ready=False
- AJWA.CA: spike=4.8 liquidity=45443516.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- IFAP.CA: spike=3.62 liquidity=24233538.0 outlook=BULLISH_WATCH score=82.18 buy_ready=True
- ARVA.CA: spike=3.49 liquidity=68284672.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SAUD.CA: spike=3.18 liquidity=21807950.0 outlook=BULLISH_WATCH score=82.73 buy_ready=True

## Sector Leaderboard
- #1 Textiles: score=11.61 5d=5.58% 20d=12.01% aboveMA50=100.0%
- #2 Building Materials: score=10.67 5d=4.89% 20d=11.45% aboveMA50=83.33%
- #3 Industrial Goods & Cables: score=9.78 5d=1.72% 20d=5.64% aboveMA50=100.0%
- #4 Telecommunications: score=8.72 5d=2.64% 20d=5.29% aboveMA50=100.0%
- #5 Fintech & Payments: score=8.7 5d=4.96% 20d=7.23% aboveMA50=50.0%
- #6 General / Verified EGX Expansion: score=8.43 5d=2.79% 20d=8.89% aboveMA50=84.47%
- #7 Transportation & Logistics: score=8.15 5d=1.56% 20d=6.73% aboveMA50=100.0%
- #8 Real Estate: score=7.86 5d=-0.57% 20d=12.56% aboveMA50=92.31%

## Today's Prioritized Action Tickets
- Priority #1: BUY CANA.CA
  - Entry: 38.02 | Take profit: 41.06 | Stop loss: 36.5
  - Confidence: LOW | score=30.3 | outlook=BULLISH_WATCH 76.73
  - Reason: WATCH/BUY SETUP: CANA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 62.43, support 34.7, resistance 37.5, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ARCC.CA
  - Entry: 56.74 | Take profit: 61.28 | Stop loss: 54.47
  - Confidence: LOW | score=29.9 | outlook=BULLISH_WATCH 90
  - Reason: WATCH/BUY SETUP: ARCC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 58.08, support 53.5, resistance 58.5, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY ATQA.CA
  - Entry: 10.04 | Take profit: 10.84 | Stop loss: 9.64
  - Confidence: LOW | score=27.92 | outlook=BULLISH_WATCH 74.01
  - Reason: WATCH/BUY SETUP: ATQA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 66.38, support 9.21, resistance 9.97, and evidence sources. Macro trend is Bearish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- NEDA.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARCC.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SWDY.CA: BULLISH_WATCH score=86.78 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- SPIN.CA: BULLISH_WATCH score=85 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- LUTS.CA: BULLISH_WATCH score=84.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EALR.CA: BULLISH_WATCH score=84.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ASCM.CA: BULLISH_WATCH score=84.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ISMA.CA: BULLISH_WATCH score=84.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ETRS.CA: BULLISH_WATCH score=84.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SAUD.CA: BULLISH_WATCH score=82.73 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- SAUD.CA: rank=32.26 outlook=BULLISH_WATCH outlook_score=82.73 sector_rank=12 price=22.56 support=19.99 resistance=22.16 liquidity=21807950.0
- ORWE.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=76 sector_rank=1 price=23.06 support=21.95 resistance=23.47 liquidity=11695390.0
- IFAP.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=82.18 sector_rank=15 price=19.75 support=18.47 resistance=20.0 liquidity=24233538.0
- CANA.CA: rank=30.3 outlook=BULLISH_WATCH outlook_score=76.73 sector_rank=12 price=38.02 support=34.7 resistance=37.5 liquidity=17875432.0
- ARCC.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=90 sector_rank=2 price=56.74 support=53.5 resistance=58.5 liquidity=11381568.0
- ATQA.CA: rank=27.92 outlook=BULLISH_WATCH outlook_score=74.01 sector_rank=17 price=10.04 support=9.21 resistance=9.97 liquidity=44825340.0
- BTFH.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=63.68 sector_rank=13 price=3.1 support=2.91 resistance=3.2 liquidity=53249104.0
- PHAR.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=66.55 sector_rank=9 price=92.58 support=83.6 resistance=93.0 liquidity=17160346.0
- PRCL.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=77 sector_rank=2 price=37.0 support=28.92 resistance=38.25 liquidity=48301088.0
- ADIB.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=57.73 sector_rank=12 price=48.98 support=44.1 resistance=49.87 liquidity=13331153.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=25.9 buy_ready=True sector_rank=6 price=242.78 support=196.0 resistance=253.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=67.83 liquidity=10487860.0 spike=0.58
- ABUK.CA: score=24.1 buy_ready=False sector_rank=17 price=71.74 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=63.47 liquidity=97026072.0 spike=0.63
- ACAMD.CA: score=24.9 buy_ready=False sector_rank=6 price=2.44 support=2.14 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=76.92 liquidity=21857616.0 spike=0.28
- ACGC.CA: score=27.9 buy_ready=False sector_rank=1 price=10.84 support=8.92 resistance=10.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=78.17 liquidity=22458846.0 spike=0.8
- ADCI.CA: score=19.94 buy_ready=False sector_rank=6 price=258.37 support=230.0 resistance=266.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=70.91 liquidity=2044233.38 spike=0.18
- ADIB.CA: score=27.9 buy_ready=True sector_rank=12 price=48.98 support=44.1 resistance=49.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=64.55 liquidity=13331153.0 spike=0.11
- ADPC.CA: score=24.9 buy_ready=False sector_rank=6 price=4.05 support=3.32 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=87.06 liquidity=11128535.0 spike=0.37
- AFDI.CA: score=23.08 buy_ready=False sector_rank=6 price=48.71 support=41.84 resistance=49.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=5179220.0 spike=0.36
- AFMC.CA: score=22.9 buy_ready=False sector_rank=6 price=104.17 support=66.0 resistance=127.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=80.16 liquidity=20689206.0 spike=0.83
- AJWA.CA: score=15.9 buy_ready=False sector_rank=6 price=182.79 support=175.0 resistance=189.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45443516.0 spike=4.8
- ALCN.CA: score=17.83 buy_ready=True sector_rank=7 price=29.74 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=69.4 liquidity=1925349.5 spike=0.09
- ALUM.CA: score=17.24 buy_ready=False sector_rank=6 price=23.43 support=20.55 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=71.91 liquidity=1336636.5 spike=0.19
- AMER.CA: score=24.27 buy_ready=False sector_rank=8 price=4.2 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=89.87 liquidity=9372421.0 spike=0.09
- AMES.CA: score=25.9 buy_ready=False sector_rank=6 price=117.77 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=71.65 liquidity=12744798.0 spike=0.13
- AMIA.CA: score=19.45 buy_ready=False sector_rank=6 price=10.7 support=8.4 resistance=10.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=76.94 liquidity=6546840.0 spike=0.55
- AMOC.CA: score=27.9 buy_ready=True sector_rank=14 price=8.39 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=67.05 liquidity=17666470.0 spike=0.3
- APSW.CA: score=18.04 buy_ready=True sector_rank=6 price=8.77 support=8.0 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=64.24 liquidity=1137137.0 spike=0.79
- ARAB.CA: score=25.9 buy_ready=True sector_rank=8 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=64.37 liquidity=87845288.0 spike=0.71
- ARCC.CA: score=29.9 buy_ready=True sector_rank=2 price=56.74 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=58.08 liquidity=11381568.0 spike=0.45
- AREH.CA: score=20.33 buy_ready=False sector_rank=6 price=1.5 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=43.4 liquidity=6431319.0 spike=0.17
- ARVA.CA: score=15.88 buy_ready=False sector_rank=6 price=12.3 support=11.98 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68284672.0 spike=3.49
- ASCM.CA: score=21.2 buy_ready=True sector_rank=6 price=61.33 support=56.29 resistance=65.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=58.68 liquidity=5296423.5 spike=0.09
- ASPI.CA: score=21.1 buy_ready=False sector_rank=6 price=0.37 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=78.75 liquidity=6197957.0 spike=0.26
- ATLC.CA: score=16.07 buy_ready=False sector_rank=13 price=5.2 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=2172610.0 spike=0.31
- ATQA.CA: score=27.92 buy_ready=True sector_rank=17 price=10.04 support=9.21 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=66.38 liquidity=44825340.0 spike=1.41
- AXPH.CA: score=18.35 buy_ready=False sector_rank=6 price=1223.88 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=53.16 liquidity=445910.66 spike=0.12
- BINV.CA: score=15.58 buy_ready=False sector_rank=11 price=47.57 support=44.98 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=56.82 liquidity=1679186.75 spike=0.24
- BIOC.CA: score=22.9 buy_ready=False sector_rank=6 price=118.5 support=66.75 resistance=137.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=78.79 liquidity=19527222.0 spike=0.65
- BTFH.CA: score=27.9 buy_ready=True sector_rank=13 price=3.1 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=63.04 liquidity=53249104.0 spike=0.26
- CAED.CA: score=17.9 buy_ready=False sector_rank=6 price=118.3 support=68.0 resistance=134.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=80.57 liquidity=5003936.0 spike=0.1
- CANA.CA: score=30.3 buy_ready=True sector_rank=12 price=38.02 support=34.7 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=62.43 liquidity=17875432.0 spike=1.2
- CCAP.CA: score=25.9 buy_ready=False sector_rank=11 price=5.57 support=4.65 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=73.96 liquidity=287847712.0 spike=0.42
- CCRS.CA: score=18.64 buy_ready=False sector_rank=6 price=2.66 support=2.18 resistance=2.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=2741292.25 spike=0.17
- CEFM.CA: score=18.77 buy_ready=True sector_rank=6 price=123.59 support=95.75 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=69.93 liquidity=2865331.75 spike=0.2
- CERA.CA: score=27.9 buy_ready=True sector_rank=6 price=1.35 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=10656664.0 spike=0.43
- CFGH.CA: score=21.04 buy_ready=False sector_rank=6 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=73.68 liquidity=35526.7 spike=3.05
- CICH.CA: score=21.19 buy_ready=True sector_rank=13 price=12.15 support=11.52 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=59.7 liquidity=3291439.75 spike=0.69
- CIEB.CA: score=17.12 buy_ready=True sector_rank=12 price=24.3 support=23.3 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=1224098.13 spike=0.15
- CIRA.CA: score=21.18 buy_ready=True sector_rank=10 price=32.0 support=27.45 resistance=33.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=67.73 liquidity=5280981.5 spike=0.15
- CLHO.CA: score=21.51 buy_ready=True sector_rank=9 price=16.82 support=15.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=63.04 liquidity=3612953.0 spike=0.07
- CNFN.CA: score=16.67 buy_ready=False sector_rank=13 price=4.86 support=4.61 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=769238.56 spike=0.03
- COMI.CA: score=27.9 buy_ready=False sector_rank=12 price=139.0 support=126.21 resistance=140.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=72.02 liquidity=44081396.0 spike=0.1
- COPR.CA: score=24.78 buy_ready=False sector_rank=6 price=0.41 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=78.79 liquidity=34871112.0 spike=1.44
- COSG.CA: score=24.9 buy_ready=False sector_rank=6 price=1.73 support=1.47 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=85.19 liquidity=13979190.0 spike=0.34
- CPCI.CA: score=16.44 buy_ready=False sector_rank=6 price=468.02 support=369.52 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=537529.56 spike=0.05
- CSAG.CA: score=20.8 buy_ready=True sector_rank=7 price=33.51 support=30.92 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=2897208.25 spike=0.14
- DAPH.CA: score=27.3 buy_ready=False sector_rank=6 price=94.53 support=78.52 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=72.8 liquidity=9402226.0 spike=0.53
- DEIN.CA: score=0.9 buy_ready=False sector_rank=6 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=16.83 buy_ready=True sector_rank=18 price=27.16 support=26.06 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=42.91 liquidity=1891176.88 spike=0.51
- DSCW.CA: score=22.9 buy_ready=False sector_rank=6 price=1.94 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=87.1 liquidity=20898738.0 spike=0.42
- DTPP.CA: score=11.04 buy_ready=False sector_rank=6 price=250.0 support=225.11 resistance=253.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63372724.0 spike=1.07
- EALR.CA: score=24.3 buy_ready=True sector_rank=6 price=368.92 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=58.95 liquidity=6404221.0 spike=0.38
- EASB.CA: score=21.67 buy_ready=True sector_rank=6 price=7.78 support=6.88 resistance=8.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=58.8 liquidity=5774551.0 spike=0.36
- EAST.CA: score=14.28 buy_ready=False sector_rank=18 price=37.32 support=36.11 resistance=39.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=51.23 liquidity=1343220.5 spike=0.02
- EBSC.CA: score=9.47 buy_ready=False sector_rank=6 price=1.88 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=18.92 liquidity=571173.94 spike=0.08
- ECAP.CA: score=17.79 buy_ready=True sector_rank=6 price=33.49 support=31.52 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=59.27 liquidity=1888689.25 spike=0.24
- EDFM.CA: score=13.62 buy_ready=False sector_rank=6 price=387.3 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=80.85 liquidity=724237.38 spike=0.18
- EEII.CA: score=21.61 buy_ready=True sector_rank=6 price=2.74 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=65.0 liquidity=5706907.0 spike=0.26
- EFIC.CA: score=13.12 buy_ready=False sector_rank=17 price=186.16 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=2018253.25 spike=0.19
- EFID.CA: score=18.01 buy_ready=False sector_rank=18 price=27.69 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=53.96 liquidity=8077189.0 spike=0.2
- EFIH.CA: score=25.9 buy_ready=True sector_rank=5 price=23.7 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=69.87 liquidity=45089252.0 spike=0.88
- EGAL.CA: score=24.1 buy_ready=False sector_rank=17 price=297.75 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=20808142.0 spike=0.48
- EGAS.CA: score=18.61 buy_ready=True sector_rank=14 price=52.29 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=65.74 liquidity=2708710.75 spike=0.23
- EGBE.CA: score=14.91 buy_ready=False sector_rank=12 price=0.48 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=97.44 liquidity=12863.4 spike=0.68
- EGCH.CA: score=24.1 buy_ready=False sector_rank=17 price=13.18 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=64.81 liquidity=32230262.0 spike=0.6
- EGSA.CA: score=15.91 buy_ready=False sector_rank=4 price=8.98 support=8.67 resistance=9.21 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=10632.32 spike=0.68
- EGTS.CA: score=14.39 buy_ready=False sector_rank=8 price=17.5 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=3489256.25 spike=0.07
- EHDR.CA: score=25.9 buy_ready=True sector_rank=6 price=2.85 support=2.37 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=69.32 liquidity=10157284.0 spike=0.28
- EKHO.CA: score=9.9 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=25.9 buy_ready=True sector_rank=3 price=2.23 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=13615697.0 spike=0.21
- ELKA.CA: score=22.9 buy_ready=False sector_rank=6 price=2.07 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=82.86 liquidity=19348262.0 spike=0.29
- ELNA.CA: score=15.48 buy_ready=False sector_rank=6 price=38.79 support=35.55 resistance=40.5 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=55.92 liquidity=883791.38 spike=1.35
- ELSH.CA: score=25.9 buy_ready=False sector_rank=6 price=15.44 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=74.08 liquidity=112396768.0 spike=0.86
- ELWA.CA: score=11.4 buy_ready=False sector_rank=6 price=1.9 support=1.87 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=499198.69 spike=0.41
- EMFD.CA: score=23.07 buy_ready=False sector_rank=8 price=11.7 support=11.24 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=9173763.0 spike=0.14
- ENGC.CA: score=25.9 buy_ready=False sector_rank=6 price=40.94 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=71.46 liquidity=10095660.0 spike=0.41
- EOSB.CA: score=15.92 buy_ready=False sector_rank=6 price=1.48 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=18812.28 spike=0.41
- EPCO.CA: score=24.45 buy_ready=False sector_rank=6 price=11.34 support=8.5 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=85.93 liquidity=9547840.0 spike=0.38
- EPPK.CA: score=18.89 buy_ready=False sector_rank=6 price=15.67 support=12.37 resistance=15.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=58.99 liquidity=989721.88 spike=0.82
- ETEL.CA: score=22.9 buy_ready=False sector_rank=4 price=103.42 support=89.01 resistance=106.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=79.14 liquidity=10066336.0 spike=0.13
- ETRS.CA: score=18.42 buy_ready=True sector_rank=6 price=10.84 support=10.18 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=56.99 liquidity=2520485.25 spike=0.04
- EXPA.CA: score=19.02 buy_ready=False sector_rank=12 price=19.97 support=18.03 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=82.66 liquidity=6117274.5 spike=0.2
- FAIT.CA: score=20.48 buy_ready=False sector_rank=12 price=37.64 support=35.06 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=64.74 liquidity=578808.56 spike=0.2
- FAITA.CA: score=14.84 buy_ready=False sector_rank=12 price=0.97 support=0.97 resistance=0.99 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=36.23 liquidity=124623.0 spike=2.91
- FERC.CA: score=18.21 buy_ready=True sector_rank=17 price=77.64 support=72.75 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=2103958.5 spike=0.19
- FWRY.CA: score=22.9 buy_ready=False sector_rank=5 price=19.11 support=18.13 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=65.85 liquidity=18352138.0 spike=0.14
- GBCO.CA: score=21.98 buy_ready=False sector_rank=19 price=31.4 support=29.5 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=46.04 liquidity=9600241.0 spike=0.12
- GDWA.CA: score=22.18 buy_ready=False sector_rank=6 price=0.88 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=86.27 liquidity=83174224.0 spike=1.14
- GGCC.CA: score=24.9 buy_ready=False sector_rank=6 price=0.86 support=0.42 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=89.68 liquidity=22995664.0 spike=0.66
- GIHD.CA: score=12.58 buy_ready=False sector_rank=6 price=61.28 support=56.66 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80387648.0 spike=1.84
- GMCI.CA: score=18.48 buy_ready=False sector_rank=6 price=2.03 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=60.49 liquidity=584761.79 spike=0.45
- GRCA.CA: score=17.53 buy_ready=False sector_rank=6 price=60.91 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=75.04 liquidity=4628767.5 spike=0.33
- GSSC.CA: score=13.9 buy_ready=False sector_rank=6 price=267.06 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=78.83 liquidity=1003106.0 spike=0.1
- GTWL.CA: score=25.9 buy_ready=True sector_rank=6 price=104.0 support=49.37 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=60.89 liquidity=31053660.0 spike=0.22
- HDBK.CA: score=19.11 buy_ready=False sector_rank=12 price=81.57 support=75.3 resistance=166.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=7211114.5 spike=0.21
- HELI.CA: score=22.9 buy_ready=False sector_rank=8 price=8.33 support=6.36 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=90.71 liquidity=23883088.0 spike=0.13
- HRHO.CA: score=25.84 buy_ready=True sector_rank=13 price=26.91 support=26.09 resistance=27.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=8937951.0 spike=0.09
- ICID.CA: score=17.74 buy_ready=False sector_rank=6 price=8.0 support=6.55 resistance=8.98 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=50.43 liquidity=3839504.0 spike=0.48
- IDRE.CA: score=27.9 buy_ready=True sector_rank=6 price=48.49 support=41.1 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=63.26 liquidity=20334228.0 spike=0.96
- IFAP.CA: score=30.9 buy_ready=True sector_rank=15 price=19.75 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=48.99 liquidity=24233538.0 spike=3.62
- INFI.CA: score=19.26 buy_ready=False sector_rank=6 price=106.6 support=88.51 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=74.79 liquidity=3362760.25 spike=0.24
- IRON.CA: score=6.71 buy_ready=False sector_rank=17 price=31.25 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=29.74 liquidity=2604870.75 spike=0.4
- ISMA.CA: score=19.87 buy_ready=True sector_rank=6 price=28.23 support=26.54 resistance=30.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=3970966.75 spike=0.23
- ISMQ.CA: score=23.1 buy_ready=False sector_rank=17 price=9.32 support=8.1 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=14989939.0 spike=0.12
- ISPH.CA: score=24.9 buy_ready=False sector_rank=9 price=11.66 support=11.2 resistance=12.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=55.37 liquidity=22240964.0 spike=0.42
- JUFO.CA: score=19.94 buy_ready=False sector_rank=18 price=29.29 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=39.85 liquidity=17209946.0 spike=0.77
- KABO.CA: score=27.9 buy_ready=False sector_rank=1 price=8.49 support=6.04 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=96.93 liquidity=18913314.0 spike=0.42
- KWIN.CA: score=24.9 buy_ready=False sector_rank=6 price=100.25 support=65.0 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=93.14 liquidity=27131690.0 spike=0.63
- KZPC.CA: score=15.21 buy_ready=False sector_rank=6 price=8.6 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=56.12 liquidity=1308850.88 spike=0.25
- LCSW.CA: score=24.9 buy_ready=False sector_rank=2 price=35.23 support=27.01 resistance=35.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=78.41 liquidity=58910072.0 spike=0.78
- LUTS.CA: score=25.9 buy_ready=True sector_rank=6 price=0.75 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=14384374.0 spike=0.41
- MAAL.CA: score=15.26 buy_ready=False sector_rank=6 price=8.7 support=6.64 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=85.44 liquidity=4363178.5 spike=0.23
- MASR.CA: score=22.9 buy_ready=False sector_rank=6 price=8.31 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=81.63 liquidity=17477638.0 spike=0.21
- MBSC.CA: score=22.07 buy_ready=False sector_rank=2 price=245.18 support=222.66 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=5169531.0 spike=0.27
- MCQE.CA: score=22.28 buy_ready=False sector_rank=2 price=189.06 support=166.66 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=71.15 liquidity=4378968.0 spike=0.25
- MCRO.CA: score=25.66 buy_ready=False sector_rank=6 price=1.51 support=1.17 resistance=1.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=82.05 liquidity=172167360.0 spike=1.88
- MENA.CA: score=16.21 buy_ready=False sector_rank=8 price=7.06 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=53.66 liquidity=314409.47 spike=0.04
- MEPA.CA: score=22.9 buy_ready=False sector_rank=6 price=1.92 support=1.52 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=80.7 liquidity=15019398.0 spike=0.36
- MFPC.CA: score=24.38 buy_ready=False sector_rank=17 price=36.72 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=57.88 liquidity=101194184.0 spike=1.14
- MFSC.CA: score=7.4 buy_ready=False sector_rank=6 price=46.33 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=1500102.88 spike=0.24
- MHOT.CA: score=8.49 buy_ready=False sector_rank=21 price=16.61 support=16.12 resistance=35.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=43.13 liquidity=594774.5 spike=0.05
- MICH.CA: score=24.52 buy_ready=False sector_rank=6 price=41.0 support=34.0 resistance=41.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=9617141.0 spike=0.67
- MILS.CA: score=22.01 buy_ready=False sector_rank=6 price=168.93 support=126.31 resistance=197.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=71.49 liquidity=6106766.5 spike=0.18
- MIPH.CA: score=13.48 buy_ready=False sector_rank=9 price=750.36 support=630.13 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=77.75 liquidity=577069.5 spike=0.17
- MOED.CA: score=24.02 buy_ready=True sector_rank=6 price=0.71 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=64.75 liquidity=19110058.0 spike=1.06
- MOIL.CA: score=15.24 buy_ready=False sector_rank=14 price=0.59 support=0.46 resistance=0.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=86.49 liquidity=343420.19 spike=0.7
- MOIN.CA: score=13.98 buy_ready=False sector_rank=6 price=23.82 support=22.6 resistance=24.76 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=52.66 liquidity=83131.8 spike=0.11
- MOSC.CA: score=18.65 buy_ready=False sector_rank=6 price=287.7 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=64.22 liquidity=749217.69 spike=0.06
- MPCI.CA: score=24.9 buy_ready=False sector_rank=6 price=286.5 support=222.55 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=75.99 liquidity=34135864.0 spike=0.33
- MPCO.CA: score=20.75 buy_ready=False sector_rank=15 price=1.84 support=1.7 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=6854874.0 spike=0.13
- MPRC.CA: score=19.83 buy_ready=False sector_rank=6 price=44.09 support=36.21 resistance=45.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=72.88 liquidity=3933441.5 spike=0.09
- MTIE.CA: score=15.08 buy_ready=False sector_rank=19 price=9.32 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=2699734.0 spike=0.12
- NAHO.CA: score=13.08 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=81853.88 spike=2.55
- NCCW.CA: score=20.83 buy_ready=True sector_rank=6 price=6.61 support=5.82 resistance=6.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=2929821.25 spike=0.14
- NEDA.CA: score=20.62 buy_ready=True sector_rank=6 price=2.83 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=60.53 liquidity=1176278.15 spike=1.77
- NHPS.CA: score=24.9 buy_ready=False sector_rank=6 price=90.97 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=82.88 liquidity=24489308.0 spike=0.3
- NINH.CA: score=23.12 buy_ready=False sector_rank=6 price=22.03 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=72.84 liquidity=7224599.0 spike=0.18
- NIPH.CA: score=24.9 buy_ready=False sector_rank=9 price=237.35 support=157.01 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=82.45 liquidity=37412864.0 spike=0.26
- OBRI.CA: score=20.9 buy_ready=False sector_rank=6 price=35.19 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=10178044.0 spike=0.27
- OCDI.CA: score=23.9 buy_ready=True sector_rank=8 price=26.88 support=22.86 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=24173512.0 spike=0.22
- OCPH.CA: score=17.63 buy_ready=False sector_rank=6 price=455.72 support=341.11 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=92.31 liquidity=4729112.0 spike=0.21
- ODIN.CA: score=20.82 buy_ready=False sector_rank=6 price=2.66 support=2.05 resistance=2.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=79.75 liquidity=5916108.5 spike=0.38
- OFH.CA: score=24.9 buy_ready=False sector_rank=6 price=0.71 support=0.57 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=84.39 liquidity=14443372.0 spike=0.24
- OIH.CA: score=22.64 buy_ready=False sector_rank=11 price=1.47 support=1.39 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=6739422.5 spike=0.1
- OLFI.CA: score=26.94 buy_ready=False sector_rank=18 price=23.5 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=71.11 liquidity=14287223.0 spike=0.42
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=708.42 support=706.0 resistance=713.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31922390.0 spike=1.0
- ORHD.CA: score=25.9 buy_ready=True sector_rank=8 price=40.55 support=37.0 resistance=40.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=65.49 liquidity=52257600.0 spike=0.34
- ORWE.CA: score=30.9 buy_ready=True sector_rank=1 price=23.06 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=63.27 liquidity=11695390.0 spike=0.51
- PHAR.CA: score=27.9 buy_ready=True sector_rank=9 price=92.58 support=83.6 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=66.24 liquidity=17160346.0 spike=0.63
- PHDC.CA: score=25.9 buy_ready=True sector_rank=8 price=14.9 support=14.26 resistance=15.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=59.58 liquidity=42553860.0 spike=0.18
- PHTV.CA: score=13.34 buy_ready=False sector_rank=6 price=311.01 support=243.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=75.12 liquidity=440785.31 spike=0.06
- POUL.CA: score=15.99 buy_ready=False sector_rank=18 price=38.28 support=36.52 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=54.32 liquidity=3049595.25 spike=0.08
- PRCL.CA: score=27.9 buy_ready=True sector_rank=2 price=37.0 support=28.92 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=48301088.0 spike=0.97
- PRDC.CA: score=25.9 buy_ready=True sector_rank=8 price=9.59 support=6.8 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=69.19 liquidity=31584610.0 spike=0.26
- PRMH.CA: score=24.23 buy_ready=True sector_rank=6 price=2.68 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=64.44 liquidity=6326658.5 spike=0.34
- RACC.CA: score=17.52 buy_ready=False sector_rank=6 price=10.0 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=3615135.25 spike=0.18
- RAKT.CA: score=13.98 buy_ready=False sector_rank=6 price=22.64 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=62.22 liquidity=83518.96 spike=0.29
- RAYA.CA: score=23.16 buy_ready=False sector_rank=16 price=7.7 support=7.01 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=51.09 liquidity=31094456.0 spike=0.23
- RMDA.CA: score=22.52 buy_ready=False sector_rank=9 price=5.02 support=4.81 resistance=5.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=9620087.0 spike=0.51
- ROTO.CA: score=25.67 buy_ready=True sector_rank=6 price=43.64 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=56.41 liquidity=9774618.0 spike=0.45
- RREI.CA: score=23.9 buy_ready=False sector_rank=6 price=3.91 support=3.34 resistance=4.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=70.15 liquidity=19778446.0 spike=0.72
- RTVC.CA: score=18.03 buy_ready=True sector_rank=6 price=3.95 support=3.55 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=2130266.75 spike=0.47
- RUBX.CA: score=21.58 buy_ready=True sector_rank=6 price=13.19 support=10.26 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=58.99 liquidity=5681268.5 spike=0.07
- SAUD.CA: score=32.26 buy_ready=True sector_rank=12 price=22.56 support=19.99 resistance=22.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=21807950.0 spike=3.18
- SCEM.CA: score=26.9 buy_ready=False sector_rank=2 price=83.0 support=60.14 resistance=82.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=82.26 liquidity=53084860.0 spike=0.97
- SCFM.CA: score=21.07 buy_ready=True sector_rank=6 price=271.45 support=230.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=64.76 liquidity=3166988.0 spike=0.16
- SCTS.CA: score=11.68 buy_ready=False sector_rank=10 price=611.07 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=32.93 liquidity=777019.31 spike=0.12
- SDTI.CA: score=22.42 buy_ready=False sector_rank=6 price=52.01 support=45.55 resistance=50.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=75.29 liquidity=6958262.0 spike=1.28
- SEIG.CA: score=16.78 buy_ready=False sector_rank=6 price=245.75 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=70.84 liquidity=879729.13 spike=0.04
- SIPC.CA: score=17.64 buy_ready=False sector_rank=6 price=3.8 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=79.73 liquidity=4737958.5 spike=0.33
- SKPC.CA: score=19.81 buy_ready=False sector_rank=17 price=16.14 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=52.28 liquidity=6707116.5 spike=0.19
- SMFR.CA: score=17.84 buy_ready=False sector_rank=6 price=234.83 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=71.88 liquidity=1939731.0 spike=0.1
- SNFC.CA: score=15.3 buy_ready=False sector_rank=6 price=11.35 support=11.2 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=38.55 liquidity=4395622.5 spike=0.39
- SPIN.CA: score=28.14 buy_ready=False sector_rank=1 price=15.23 support=13.8 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=85.19 liquidity=31956006.0 spike=2.12
- SPMD.CA: score=18.12 buy_ready=True sector_rank=6 price=0.45 support=0.41 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=4217898.5 spike=0.23
- SUGR.CA: score=14.93 buy_ready=False sector_rank=18 price=47.21 support=45.31 resistance=47.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=55.2 liquidity=1990292.5 spike=0.37
- SVCE.CA: score=23.9 buy_ready=False sector_rank=6 price=9.33 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=41.98 liquidity=11109787.0 spike=0.18
- SWDY.CA: score=31.72 buy_ready=False sector_rank=3 price=95.5 support=84.3 resistance=93.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=74.21 liquidity=41588704.0 spike=2.41
- TALM.CA: score=21.91 buy_ready=True sector_rank=10 price=15.86 support=15.27 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=48.63 liquidity=4014008.75 spike=0.28
- TMGH.CA: score=25.9 buy_ready=True sector_rank=8 price=99.77 support=92.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=68.36 liquidity=44363256.0 spike=0.12
- TRTO.CA: score=16.91 buy_ready=False sector_rank=6 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6936.0 spike=6.87
- UEFM.CA: score=16.75 buy_ready=False sector_rank=6 price=541.39 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=67.82 liquidity=852299.0 spike=0.19
- UEGC.CA: score=16.09 buy_ready=False sector_rank=6 price=2.38 support=1.33 resistance=2.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=90.83 liquidity=3194964.5 spike=0.07
- UNIP.CA: score=22.9 buy_ready=False sector_rank=6 price=0.4 support=0.3 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=81.68 liquidity=11838040.0 spike=0.55
- UNIT.CA: score=23.32 buy_ready=False sector_rank=8 price=18.33 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=70.48 liquidity=7415238.0 spike=0.26
- WCDF.CA: score=18.31 buy_ready=False sector_rank=6 price=569.46 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=409925.91 spike=0.23
- WKOL.CA: score=22.39 buy_ready=True sector_rank=6 price=319.76 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=65.19 liquidity=6485934.5 spike=0.71
- ZEOT.CA: score=16.68 buy_ready=True sector_rank=6 price=11.64 support=10.4 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=66.14 liquidity=2776549.25 spike=0.08
- ZMID.CA: score=25.9 buy_ready=False sector_rank=8 price=7.5 support=6.19 resistance=7.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=72.64 liquidity=48656208.0 spike=0.19

## Backtesting Lite
- SAUD.CA: 180d return=62.92%, max drawdown=-19.12%, MA20>MA50 days last20=0, as_of=2026-07-21T21:00:00+00:00
- SWDY.CA: 180d return=20.8%, max drawdown=-20.2%, MA20>MA50 days last20=15, as_of=2026-07-21T21:00:00+00:00
- ORWE.CA: 180d return=1.95%, max drawdown=-13.64%, MA20>MA50 days last20=18, as_of=2026-07-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=571 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025 Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- SWDY.CA: status=RECENT_ACCEPTED latest=2026-07-19 age_days=7 sources=3 expected=Elsewedy Electric summary=Elsewedy Electric (SWDY.CA) has released several disclosures and financial statements within the last 12 months. These include EGM minutes, disclosures regarding the Board of Directors and shareholders' structure, and interim consolidated financial statements.
  - ELSWEDY ELECTRIC (SWDY.CA) - EGM Minutes (Notarized) (July 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5OO8S_TqzbC00sHLAZoa903uNdYMvBer91Io3fFdI2Ye5ADkemHoSLG9vkHYKtVgVRYQoIsODUsMcumbSFqDkQ4988p8H5gPnVRHnZIHQg-Xy_SFN3p9vUJbttoCeWg6Yzc43f2pP8YkVnMA8CXfCvn3hJ1D_UMhFAQ7I38Y
  - Release from El sewedy Electric (SWDY.CA) Concerning a Circulated News (July 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5OO8S_TqzbC00sHLAZoa903uNdYMvBer91Io3fFdI2Ye5ADkemHoSLG9vkHYKtVgVRYQoIsODUsMcumbSFqDkQ4988p8H5gPnVRHnZIHQg-Xy_SFN3p9vUJbttoCeWg6Yzc43f2pP8YkVnMA8CXfCvn3hJ1D_UMhFAQ7I38Y
  - ELSWEDY ELECTRIC (SWDY.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5OO8S_TqzbC00sHLAZoa903uNdYMvBer91Io3fFdI2Ye5ADkemHoSLG9vkHYKtVgVRYQoIsODUsMcumbSFqDkQ4988p8H5gPnVRHnZIHQg-Xy_SFN3p9vUJbttoCeWg6Yzc43f2pP8YkVnMA8CXfCvn3hJ1D_UMhFAQ7I38Y
- ORWE.CA: status=RECENT_ACCEPTED latest=2026-05-21 age_days=66 sources=3 expected=Oriental Weavers summary=Oriental Weavers (ORWE.CA) has provided several disclosures and minutes of meetings within the last 12 months, including Board of Directors' minutes, AGM minutes, and shareholder structure disclosures. Recent financial performance data for the latest quarter is also available.
  - Release from Oriental Weavers (ORWE.CA) Concerning the Board of Directors' Minutes (May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuELLZSlPYWVR-0C9Q7NP8DbcSBZ241Lj2aXasmgrIDtcJiwKZmzVnmdk_BQFGCqUPf3sd8qg-4tDY05s-Yr0VHjhBfA8COewP1OF9FoTv1nhn2s9Qf5YKWid93MGt-KIk8O9qoYwoldOLerLVQctT
  - Oriental Weavers (ORWE.CA) - Minutes of the Board of Directors' Meeting (May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuELLZSlPYWVR-0C9Q7NP8DbcSBZ241Lj2aXasmgrIDtcJiwKZmzVnmdk_BQFGCqUPf3sd8qg-4tDY05s-Yr0VHjhBfA8COewP1OF9FoTv1nhn2s9Qf5YKWid93MGt-KIk8O9qoYwoldOLerLVQctT
  - Oriental Weavers (ORWE.CA) - AGM Minutes (Notarized) (May 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuELLZSlPYWVR-0C9Q7NP8DbcSBZ241Lj2aXasmgrIDtcJiwKZmzVnmdk_BQFGCqUPf3sd8qg-4tDY05s-Yr0VHjhBfA8COewP1OF9FoTv1nhn2s9Qf5YKWid93MGt-KIk8O9qoYwoldOLerLVQctT
- IFAP.CA: status=RECENT_ACCEPTED latest=2026-07-24 age_days=2 sources=3 expected=International Agricultural Products summary=International Agricultural Products (IFAP.CA) has reported consolidated financial results for the period from July 2025 to March 2026 and received a release from the FRA regarding a disclosure report. Fiscal year 2025 revenue and earnings information is also available.
  - International Agricultural Products (IFAP.CA) Reports its Financial Results (Consolidated) for the Period from 01/07/2025 to 31/03/2026 (June 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8UEr_JhtvwSaP115XMexLjR2eHaJFye4N-HyNkJkktLjdF4SI-53j2I1LId-KRFgHyd8p4_9H_8S8s2uAA30RHt5vYnbcm43jpNZynz7A5rLyFKe6rbdSSnm3T1np
  - International Agricultural Products (IFAP.CA) - Release from FRA (June 9, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_aF0FELdCPHMavb38D4M75rcU9Bao4gSTQUNPa9CTItVk09x_lurRosH9vSPqjSK0Fxu3L9FaRUIcMF1zuTFB2BXg439poUndDmYj_eplmkfoiTpJUXJe9fPz9aQoFqB-Et8keE7dU3UgH4GYCfB-iKM=
  - International Company for Agricultural Crops (EGX:IFAP) Fiscal Year 2025 Financial Performance (July 24, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFz5Y5al3N0xSHsSB-G_r3mrxs4nxygqOEMTzt3VT7ZDft4wfmMrkfxEgbu-hGG-iG8UNhW_qWWx-I4OynEgwH0y_8KZ9WcN0cZZHY97A2BgnoYEw_RjIxTqNbzTj0VSA00u-g=
- CANA.CA: status=RECENT_ACCEPTED latest=2026-07-23 age_days=3 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank (CANA.CA) has provided recent investor relations updates, including a disclosure form for its Board of Directors and shareholders' structure. The bank's investor relations page was updated in July 2026, and the company details on the Egyptian Exchange were updated in June 2026.
  - Suez Canal Bank Investor Relations (Last Updated: July 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH6Zq8nWJJowhRKzcJ6I00i4rWBnS6Zqq8eQAzg6I3YO_frrAuHfkZmM5S9Qe8F2XCigGRsR8cRrERqhXIA3xhmNdojtbtdb1spXbMOK96u8fuLAH96VWjvn2n84k=
  - Suez Canal Bank (CANA.CA) - Disclosure Form for the BoD & the Shareholders' Structure (April 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZODW_vV75okRk_ExiAQzloViWJWk6cfWFl-hZVUh1P6HZrEhH-t6dtw7APDUuUZtElkWYGL0kUv53_P3BrYjMkZvQdBc3LK0JeoAIpBEUbnEH1-MCIuOwUej0kFsWL9lVjyibQQMTY0L-EE4CiUk4jIU=
  - Suez Canal Bank (S.A.E) Company Profile & Description (Last updated: July 3, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFznJwqGn9B6NCQFAuW50E_sBFMI5T4DxQoozBzKQsfxejHIIN3iCXcaanM7m_Bf2PS2e0esVYpdZu05vvopYp3AF25fMRXYgxtlh12XAP5LUBafOeCMGFPYXiMoCB5Cmk6Eo5ujkIkac-5wA==
- ARCC.CA: status=RECENT_ACCEPTED latest=2026-07-16 age_days=10 sources=3 expected=Arabian Cement Company summary=Arabian Cement Company (ARCC.CA) has issued several disclosures and decisions from its Board of Directors and Listing Committee within the last 12 months. Recent financial performance data for the latest quarter is also available.
  - Arabian Cement Company (ARCC.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgWa2Qe3ixwJ5XFTbaZukai3821iEfxf76qDjaTNsJSko-WvnGzxynyUh0RSOUBRdgd6KYMq9HJNH1E_4pZPcQClGVTJQjOQG46ASFWBOP77HMyUq_swNOVvCJATMUDmh7KsssBXaD9062zl2PBA==
  - Arabian Cement Company (ARCC.CA) - Listing Committee Decision (July 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYmtdMB_SmUGqOAGSi6b5NutXrSM0wQccno6KgkMYUjT14exMBV8XsOGYENLObfF9JiIPNpc5EUCysydbBLNzYX-vbd62Nn7bTdkMuAD614Fc9kg43x9839fUoIvv0Wlm4tpG2ncsLilwqyusQ9I4=
  - Arabian Cement Company (ARCC.CA) - Decisions of the BoD Meeting (June 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7rJpDQqEQLmcKXB456rcNkxCuHw4W4cVxEBG72elH24-A0LwBeGnsfRr5mDtucBfi_11Xynx33waeDHwCv11s6thZdg97v7tneimbwIy4LhZfwZWvVmwQjXk1fX6ns_VGxEEYc7gqwdris4Tz7Y79WMk8hiknjUIl8I-abqM=
- SPIN.CA: status=RECENT_ACCEPTED latest=2026-07-15 age_days=11 sources=2 expected=Alexandria Spinning and Weaving summary=Alexandria Spinning and Weaving (SPIN.CA) has a recent disclosure form for its Board of Directors and shareholders' structure from July 2026. The company's details on the Egyptian Exchange were also updated in July 2026.
  - Alexandria Spinning & Weaving (SPINALEX) (SPIN.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9gTanqTJOGkCOcr6DHahPxKncf1dP47xSsxNhPkYTnxMB-Ex5SlBoxO3lgwWNRg0b-3nGtzdmyQ-DIcRlQxi1IxbAE479uX_LUNcKEG2Pq0BZ2UaKEhSt4bSApv5dfO4T8EakkePOBT1VOVeQijjhpyysge-Dm_uVmkHmlHa4FrzK153U2QGFQw==
  - The Egyptian Exchange - Company Details for Alexandria Spinning & Weaving (Last Trading Date: July 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwH3dJlcTseMqFym9u4AAjzFrCrImzxZ_ViD93_6izBf14DpK2o2jVS09Y593Xqv1xcp7zEGxLpdxbwTauoqKQ-SBgDngNa1qkKOJeK3yDBfmgvjrxU3Ews9kpfsQNT2XIQ6CpzCCaRqmn243Vl9fI-k6qbPI=
- ATQA.CA: status=RECENT_ACCEPTED latest=2026-07-08 age_days=18 sources=3 expected=Misr National Steel Ataqa summary=Misr National Steel Ataqa (ATQA.CA) has released several disclosure forms and minutes of meetings within the last 12 months, including those related to its Board of Directors, shareholders' structure, and AGM/EGM minutes.
  - Misr National Steel - Ataqa (ATQA.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 8, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt2xy8V0nNwE-P05TdnIhAUhcAiOs6KQCCcF6X2Y4lwO1iQDCwDQdndA2IzIONAFFB6ZTgAKo6IDq7vZ0xlDc13reg0WXpSs5bu7Ivd6z54-w3-G72TpmhKN4dRjm3sFd93hDAxAfybFoXHznDSmWKanLSkczmFV9sQniCn68=
  - Misr National Steel - Ataqa (ATQA.CA) - AGM Minutes (after Certification) (April 27, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt2xy8V0nNwE-P05TdnIhAUhcAiOs6KQCCcF6X2Y4lwO1iQDCwDQdndA2IzIONAFFB6ZTgAKo6IDq7vZ0xlDc13reg0WXpSs5bu7Ivd6z54-w3-G72TpmhKN4dRjm3sFd93hDAxAfybFoXHznDSmWKanLSkczmFV9sQniCn68=
  - Misr National Steel - Ataqa (ATQA.CA) - Disclosure Form of the Company for the Board of Directors and the Shareholders' Structure (April 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt2xy8V0nNwE-P05TdnIhAUhcAiOs6KQCCcF6X2Y4lwO1iQDCwDQdndA2IzIONAFFB6ZTgAKo6IDq7vZ0xlDc13reg0WXpSs5bu7Ivd6z54-w3-G72TpmhKN4dRjm3sFd93hDAxAfybFoXHznDSmWKanLSkczmFV9sQniCn68=

## Warnings
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
