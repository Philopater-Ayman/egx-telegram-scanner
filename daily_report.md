# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-07-20T14:42:50.034320+00:00
Generated Cairo: 2026-07-20 17:42
Run timing: target 15:30 Cairo | generated Cairo 2026-07-20 17:42 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-07-20 17:36

## Control Center
- Action tickets: 2 prioritized signal(s)
- BUY-ready candidates: 37
- Data quality issues: 1
- Tradeable price/liquidity tickers: 165/189
- Top sector: Industrial Goods & Cables

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 20
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 70.0% / above MA50 45.0%
- EGX70 regime: BULLISH / above MA20 72.97% / above MA50 75.68%
- Sector breadth: 47.62%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- COMI.CA: liquidity=729892736.0 spike=2.02 score=28.04
- TMGH.CA: liquidity=429303360.0 spike=1.11 score=24.62
- CCAP.CA: liquidity=383371648.0 spike=0.61 score=23.4
- NIPH.CA: liquidity=349202592.0 spike=3.0 score=13.4
- ZMID.CA: liquidity=310990048.0 spike=1.31 score=24.02

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flagged ARCC.CA and EALR.CA as BUY SETUPS under a SELECTIVE_SWING_TRADES_ONLY regime, citing price above short‑term averages, adequate liquidity spikes and defined support/resistance, while noting sector weakness and low confidence.
- ARCC.CA: price 57.18 above MA20/MA50, RSI 55.7, support 53.0, resistance 56.7, liquidity spike 5.8×, outlook BULLISH_WATCH but sector Building Materials not leading.
- EALR.CA: price 372.51 above MA20/MA50, RSI 65.3, support 332.0, resistance 425.0, liquidity spike 3.7×, outlook BULLISH_WATCH with extended momentum and sector not leading.

## Top Liquidity Spikes
- CEFM.CA: spike=15.88 liquidity=103314856.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- FERC.CA: spike=14.98 liquidity=72766872.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GRCA.CA: spike=11.04 liquidity=68196600.0 outlook=CONSTRUCTIVE score=64.77 buy_ready=False
- SCEM.CA: spike=10.31 liquidity=306993312.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCFM.CA: spike=9.14 liquidity=106575528.0 outlook=CONSTRUCTIVE score=64.77 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Cables: score=12.21 5d=4.73% 20d=6.58% aboveMA50=100.0%
- #2 Telecommunications: score=10.73 5d=-0.32% 20d=4.44% aboveMA50=100.0%
- #3 Textiles: score=10.18 5d=1.13% 20d=4.41% aboveMA50=100.0%
- #4 Automotive & Distribution: score=10.08 5d=2.34% 20d=8.45% aboveMA50=100.0%
- #5 Investment Holding: score=9.14 5d=1.71% 20d=4.19% aboveMA50=100.0%
- #6 Transportation & Logistics: score=8.96 5d=1.92% 20d=6.21% aboveMA50=100.0%
- #7 Energy & Petrochemicals: score=8.45 5d=4.13% 20d=4.09% aboveMA50=75.0%
- #8 Building Materials: score=7.91 5d=0.0% 20d=0.0% aboveMA50=16.67%

## Today's Prioritized Action Tickets
- Priority #1: BUY ARCC.CA
  - Entry: 57.18 | Take profit: 61.76 | Stop loss: 54.89
  - Confidence: LOW | score=29.4 | outlook=BULLISH_WATCH 89.91
  - Reason: BUY SETUP: ARCC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 55.7, support 53.0, resistance 56.7, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY EALR.CA
  - Entry: 372.51 | Take profit: 422.88 | Stop loss: 357.61
  - Confidence: LOW | score=29.4 | outlook=BULLISH_WATCH 80.77
  - Reason: WATCH/BUY SETUP: EALR.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 65.29, support 332.0, resistance 425.0, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- OIH.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- SPIN.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- GBCO.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARCC.CA: BULLISH_WATCH score=89.91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ARVA.CA: BULLISH_WATCH score=88.77 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ELEC.CA: BULLISH_WATCH score=88 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- ACGC.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- EFIH.CA: BULLISH_WATCH score=86.27 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- KABO.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- RAYA.CA: BULLISH_WATCH score=82.86 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- OIH.CA: rank=31.68 outlook=BULLISH_WATCH outlook_score=100 sector_rank=5 price=1.47 support=1.35 resistance=1.43 liquidity=177133744.0
- ARCC.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=89.91 sector_rank=8 price=57.18 support=53.0 resistance=56.7 liquidity=108804984.0
- EALR.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=80.77 sector_rank=12 price=372.51 support=332.0 resistance=425.0 liquidity=49607328.0
- COPR.CA: rank=28.68 outlook=BULLISH_WATCH outlook_score=81.77 sector_rank=12 price=0.38 support=0.35 resistance=0.4 liquidity=54707588.0
- SPIN.CA: rank=28.66 outlook=BULLISH_WATCH outlook_score=99 sector_rank=3 price=14.85 support=13.8 resistance=14.8 liquidity=31977652.0
- APSW.CA: rank=28.18 outlook=BULLISH_WATCH outlook_score=82.77 sector_rank=12 price=9.25 support=8.0 resistance=8.84 liquidity=4777997.5
- COMI.CA: rank=28.04 outlook=BULLISH_WATCH outlook_score=81.0 sector_rank=16 price=136.71 support=126.21 resistance=137.98 liquidity=729892736.0
- CLHO.CA: rank=27.8 outlook=BULLISH_WATCH outlook_score=74.2 sector_rank=14 price=17.06 support=15.5 resistance=17.39 liquidity=124138800.0
- EFIH.CA: rank=27.76 outlook=BULLISH_WATCH outlook_score=86.27 sector_rank=13 price=22.2 support=20.0 resistance=23.65 liquidity=65949708.0
- ARVA.CA: rank=27.24 outlook=BULLISH_WATCH outlook_score=88.77 sector_rank=12 price=11.15 support=10.5 resistance=11.55 liquidity=40499036.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=28.52 buy_ready=False sector_rank=12 price=241.1 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=71.91 liquidity=45927072.0 spike=3.06
- ABUK.CA: score=22.38 buy_ready=False sector_rank=17 price=72.78 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.65 liquidity=136815648.0 spike=0.84
- ACAMD.CA: score=23.56 buy_ready=False sector_rank=12 price=2.37 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.88 liquidity=120547808.0 spike=1.58
- ACGC.CA: score=25.4 buy_ready=True sector_rank=3 price=9.78 support=8.92 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.93 liquidity=16705921.0 spike=0.83
- ADCI.CA: score=12.12 buy_ready=False sector_rank=12 price=252.0 support=239.0 resistance=258.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26529714.0 spike=2.36
- ADIB.CA: score=21.36 buy_ready=False sector_rank=16 price=46.82 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=109814960.0 spike=1.18
- ADPC.CA: score=21.4 buy_ready=False sector_rank=12 price=3.8 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=83.08 liquidity=17104112.0 spike=0.7
- AFDI.CA: score=19.05 buy_ready=False sector_rank=12 price=47.62 support=41.84 resistance=48.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.3 liquidity=4651862.5 spike=0.33
- AFMC.CA: score=14.4 buy_ready=False sector_rank=12 price=109.26 support=99.0 resistance=109.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63017400.0 spike=8.53
- AJWA.CA: score=23.22 buy_ready=False sector_rank=12 price=169.55 support=172.1 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.09 liquidity=18968682.0 spike=1.41
- ALCN.CA: score=24.4 buy_ready=False sector_rank=6 price=29.76 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.16 liquidity=15409390.0 spike=0.74
- ALUM.CA: score=22.8 buy_ready=False sector_rank=12 price=23.62 support=20.55 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=80.23 liquidity=10808537.0 spike=1.7
- AMER.CA: score=23.62 buy_ready=False sector_rank=11 price=4.0 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=97.98 liquidity=108957584.0 spike=1.11
- AMES.CA: score=21.4 buy_ready=False sector_rank=12 price=116.96 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.13 liquidity=44916680.0 spike=0.51
- AMIA.CA: score=14.4 buy_ready=False sector_rank=12 price=10.63 support=9.95 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36800372.0 spike=3.71
- AMOC.CA: score=23.46 buy_ready=False sector_rank=7 price=8.3 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.41 liquidity=58666016.0 spike=1.03
- APSW.CA: score=28.18 buy_ready=True sector_rank=12 price=9.25 support=8.0 resistance=8.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=4777997.5 spike=4.48
- ARAB.CA: score=24.58 buy_ready=False sector_rank=11 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.07 liquidity=126023208.0 spike=1.09
- ARCC.CA: score=29.4 buy_ready=True sector_rank=8 price=57.18 support=53.0 resistance=56.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.7 liquidity=108804984.0 spike=5.82
- AREH.CA: score=22.4 buy_ready=False sector_rank=12 price=1.51 support=1.48 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=15211100.0 spike=0.4
- ARVA.CA: score=27.24 buy_ready=True sector_rank=12 price=11.15 support=10.5 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.88 liquidity=40499036.0 spike=2.42
- ASCM.CA: score=22.4 buy_ready=True sector_rank=12 price=60.5 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.49 liquidity=52180620.0 spike=0.75
- ASPI.CA: score=10.5 buy_ready=False sector_rank=12 price=0.36 support=0.34 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37980928.0 spike=1.55
- ATLC.CA: score=23.06 buy_ready=False sector_rank=9 price=5.18 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=10517434.0 spike=1.33
- ATQA.CA: score=21.38 buy_ready=False sector_rank=17 price=9.63 support=9.21 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=25599762.0 spike=0.85
- AXPH.CA: score=13.53 buy_ready=False sector_rank=12 price=1242.45 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=75.81 liquidity=2126335.75 spike=0.57
- BINV.CA: score=23.67 buy_ready=True sector_rank=5 price=49.6 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.84 liquidity=7105422.5 spike=1.08
- BIOC.CA: score=14.4 buy_ready=False sector_rank=12 price=118.55 support=116.7 resistance=137.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88042360.0 spike=5.13
- BTFH.CA: score=26.86 buy_ready=False sector_rank=9 price=3.11 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.45 liquidity=259506176.0 spike=1.23
- CAED.CA: score=11.42 buy_ready=False sector_rank=12 price=118.33 support=118.0 resistance=131.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86117472.0 spike=2.01
- CANA.CA: score=27.14 buy_ready=True sector_rank=16 price=36.35 support=34.7 resistance=38.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=37369076.0 spike=3.07
- CCAP.CA: score=23.4 buy_ready=False sector_rank=5 price=5.42 support=4.65 resistance=5.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.92 liquidity=383371648.0 spike=0.61
- CCRS.CA: score=28.16 buy_ready=False sector_rank=12 price=2.68 support=2.18 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.23 liquidity=28373690.0 spike=1.88
- CEFM.CA: score=14.4 buy_ready=False sector_rank=12 price=138.29 support=129.55 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103314856.0 spike=15.88
- CERA.CA: score=24.4 buy_ready=False sector_rank=12 price=1.36 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.27 liquidity=27011796.0 spike=0.98
- CFGH.CA: score=10.4 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=64.29 liquidity=4285.32 spike=0.47
- CICH.CA: score=17.08 buy_ready=False sector_rank=9 price=12.05 support=11.52 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.73 liquidity=3680553.0 spike=0.73
- CIEB.CA: score=20.7 buy_ready=False sector_rank=16 price=24.04 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=64.44 liquidity=8396136.0 spike=1.15
- CIRA.CA: score=24.08 buy_ready=False sector_rank=15 price=31.51 support=27.17 resistance=33.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=25493734.0 spike=0.69
- CLHO.CA: score=27.8 buy_ready=True sector_rank=14 price=17.06 support=15.5 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.55 liquidity=124138800.0 spike=2.7
- CNFN.CA: score=24.4 buy_ready=True sector_rank=9 price=4.87 support=4.54 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.81 liquidity=14812287.0 spike=0.3
- COMI.CA: score=28.04 buy_ready=True sector_rank=16 price=136.71 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.86 liquidity=729892736.0 spike=2.02
- COPR.CA: score=28.68 buy_ready=True sector_rank=12 price=0.38 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.96 liquidity=54707588.0 spike=2.64
- COSG.CA: score=23.8 buy_ready=False sector_rank=12 price=1.67 support=1.47 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=46470772.0 spike=1.2
- CPCI.CA: score=18.78 buy_ready=False sector_rank=12 price=470.07 support=365.01 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=76.19 liquidity=7375206.5 spike=0.69
- CSAG.CA: score=24.4 buy_ready=False sector_rank=6 price=33.58 support=30.87 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.57 liquidity=10550190.0 spike=0.53
- DAPH.CA: score=22.49 buy_ready=True sector_rank=12 price=86.79 support=78.52 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=8091840.0 spike=0.78
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=12 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=12.13 buy_ready=False sector_rank=18 price=26.68 support=25.75 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=52.49 liquidity=1172420.13 spike=0.23
- DSCW.CA: score=24.94 buy_ready=False sector_rank=12 price=1.97 support=1.71 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=96.15 liquidity=76465120.0 spike=1.77
- DTPP.CA: score=21.62 buy_ready=False sector_rank=12 price=227.88 support=114.67 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=86.11 liquidity=59214276.0 spike=1.11
- EALR.CA: score=29.4 buy_ready=True sector_rank=12 price=372.51 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.29 liquidity=49607328.0 spike=3.68
- EASB.CA: score=24.52 buy_ready=True sector_rank=12 price=7.43 support=6.88 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.31 liquidity=18604484.0 spike=1.06
- EAST.CA: score=16.96 buy_ready=False sector_rank=18 price=37.02 support=36.11 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.99 liquidity=21913230.0 spike=0.44
- EBSC.CA: score=14.09 buy_ready=False sector_rank=12 price=1.88 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=1691361.38 spike=0.25
- ECAP.CA: score=24.04 buy_ready=True sector_rank=12 price=33.39 support=31.52 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.19 liquidity=9442579.0 spike=1.1
- EDFM.CA: score=28.4 buy_ready=False sector_rank=12 price=387.41 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=88.23 liquidity=14294124.0 spike=4.71
- EEII.CA: score=24.4 buy_ready=False sector_rank=12 price=2.77 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=19026680.0 spike=0.91
- EFIC.CA: score=23.68 buy_ready=False sector_rank=17 price=185.33 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.57 liquidity=27614560.0 spike=3.15
- EFID.CA: score=17.96 buy_ready=False sector_rank=18 price=27.85 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=66.34 liquidity=23934248.0 spike=0.59
- EFIH.CA: score=27.76 buy_ready=True sector_rank=13 price=22.2 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.06 liquidity=65949708.0 spike=1.68
- EGAL.CA: score=20.16 buy_ready=False sector_rank=17 price=304.99 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.21 liquidity=63862048.0 spike=1.39
- EGAS.CA: score=26.4 buy_ready=True sector_rank=7 price=52.57 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=10512616.0 spike=0.94
- EGBE.CA: score=13.32 buy_ready=False sector_rank=16 price=0.48 support=-0.34 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=96.79 liquidity=323709.44 spike=-20.96
- EGCH.CA: score=17.38 buy_ready=False sector_rank=17 price=13.1 support=12.13 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.87 liquidity=44860928.0 spike=0.87
- EGSA.CA: score=18.45 buy_ready=False sector_rank=2 price=9.1 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=77.08 liquidity=48958.67 spike=4.13
- EGTS.CA: score=19.4 buy_ready=False sector_rank=11 price=17.65 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.7 liquidity=21175820.0 spike=0.41
- EHDR.CA: score=26.04 buy_ready=False sector_rank=12 price=2.9 support=2.37 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=81.71 liquidity=78733776.0 spike=2.32
- EKHO.CA: score=8.4 buy_ready=False sector_rank=7 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=31.88 buy_ready=False sector_rank=1 price=2.22 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=146573936.0 spike=2.74
- ELKA.CA: score=9.46 buy_ready=False sector_rank=12 price=2.03 support=1.99 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67286816.0 spike=1.03
- ELNA.CA: score=14.81 buy_ready=False sector_rank=12 price=38.64 support=35.55 resistance=40.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=61.57 liquidity=1045130.31 spike=1.68
- ELSH.CA: score=24.4 buy_ready=False sector_rank=12 price=14.29 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.32 liquidity=63775128.0 spike=0.49
- ELWA.CA: score=12.09 buy_ready=False sector_rank=12 price=1.96 support=1.87 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=694755.44 spike=0.52
- EMFD.CA: score=22.4 buy_ready=False sector_rank=11 price=11.7 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=15690098.0 spike=0.18
- ENGC.CA: score=24.4 buy_ready=False sector_rank=12 price=42.7 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.32 liquidity=18218718.0 spike=0.77
- EOSB.CA: score=14.43 buy_ready=False sector_rank=12 price=1.48 support=1.48 resistance=1.55 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=26589.68 spike=0.48
- EPCO.CA: score=25.04 buy_ready=False sector_rank=12 price=10.9 support=8.5 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=84.49 liquidity=39916764.0 spike=1.82
- EPPK.CA: score=15.05 buy_ready=False sector_rank=12 price=14.47 support=12.31 resistance=15.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=69.54 liquidity=650508.94 spike=0.57
- ETEL.CA: score=28.74 buy_ready=False sector_rank=2 price=100.43 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.26 liquidity=72666384.0 spike=1.17
- ETRS.CA: score=24.4 buy_ready=True sector_rank=12 price=10.84 support=10.12 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.47 liquidity=10018610.0 spike=0.16
- EXPA.CA: score=23.0 buy_ready=False sector_rank=16 price=19.77 support=18.03 resistance=19.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.54 liquidity=23549612.0 spike=0.9
- FAIT.CA: score=14.96 buy_ready=False sector_rank=16 price=37.28 support=35.06 resistance=37.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=961384.44 spike=0.35
- FAITA.CA: score=9.03 buy_ready=False sector_rank=16 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=27331.62 spike=0.75
- FERC.CA: score=13.38 buy_ready=False sector_rank=17 price=82.6 support=76.5 resistance=83.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72766872.0 spike=14.98
- FWRY.CA: score=23.4 buy_ready=False sector_rank=13 price=19.25 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=131527760.0 spike=0.97
- GBCO.CA: score=27.12 buy_ready=True sector_rank=4 price=31.52 support=28.6 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.68 liquidity=100741992.0 spike=1.36
- GDWA.CA: score=25.4 buy_ready=False sector_rank=12 price=0.86 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=278503616.0 spike=8.14
- GGCC.CA: score=25.46 buy_ready=False sector_rank=12 price=0.88 support=0.42 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=97.13 liquidity=54699084.0 spike=2.03
- GIHD.CA: score=24.88 buy_ready=True sector_rank=12 price=51.23 support=40.66 resistance=55.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=68.76 liquidity=41063512.0 spike=1.24
- GMCI.CA: score=15.43 buy_ready=False sector_rank=12 price=2.05 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.25 liquidity=1032682.5 spike=0.82
- GRCA.CA: score=28.4 buy_ready=False sector_rank=12 price=63.91 support=48.0 resistance=65.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=77.44 liquidity=68196600.0 spike=11.04
- GSSC.CA: score=26.26 buy_ready=False sector_rank=12 price=274.0 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=90.3 liquidity=21215298.0 spike=2.43
- GTWL.CA: score=9.62 buy_ready=False sector_rank=12 price=101.5 support=95.15 resistance=104.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=136701120.0 spike=1.11
- HDBK.CA: score=18.0 buy_ready=False sector_rank=16 price=79.77 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=40108668.0 spike=1.0
- HELI.CA: score=23.62 buy_ready=False sector_rank=11 price=8.13 support=6.36 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=89.29 liquidity=187755776.0 spike=1.11
- HRHO.CA: score=21.48 buy_ready=False sector_rank=9 price=26.96 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.62 liquidity=129160736.0 spike=1.04
- ICID.CA: score=17.39 buy_ready=True sector_rank=12 price=8.2 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.06 liquidity=2993570.75 spike=0.36
- IDRE.CA: score=23.37 buy_ready=True sector_rank=12 price=45.27 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=6972675.0 spike=0.51
- IFAP.CA: score=21.93 buy_ready=False sector_rank=19 price=19.2 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=12813061.0 spike=2.53
- INFI.CA: score=26.12 buy_ready=False sector_rank=12 price=104.09 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=77.65 liquidity=35846808.0 spike=3.36
- IRON.CA: score=11.3 buy_ready=False sector_rank=17 price=31.37 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.8 liquidity=3919769.0 spike=0.52
- ISMA.CA: score=24.78 buy_ready=True sector_rank=12 price=28.48 support=26.54 resistance=30.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.13 liquidity=27186346.0 spike=1.19
- ISMQ.CA: score=21.38 buy_ready=False sector_rank=17 price=9.1 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=56364364.0 spike=0.43
- ISPH.CA: score=19.4 buy_ready=False sector_rank=14 price=11.46 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=35919860.0 spike=0.67
- JUFO.CA: score=20.42 buy_ready=False sector_rank=18 price=28.85 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.64 liquidity=44693848.0 spike=2.23
- KABO.CA: score=27.54 buy_ready=False sector_rank=3 price=8.29 support=6.04 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=95.05 liquidity=91068720.0 spike=2.57
- KWIN.CA: score=14.4 buy_ready=False sector_rank=12 price=95.97 support=83.99 resistance=95.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=151332144.0 spike=5.75
- KZPC.CA: score=12.52 buy_ready=False sector_rank=12 price=8.56 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.0 liquidity=2117820.5 spike=0.38
- LCSW.CA: score=11.64 buy_ready=False sector_rank=8 price=35.39 support=32.15 resistance=35.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=140738784.0 spike=2.12
- LUTS.CA: score=22.4 buy_ready=False sector_rank=12 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=21168176.0 spike=0.5
- MAAL.CA: score=21.4 buy_ready=False sector_rank=12 price=8.74 support=6.46 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=91.88 liquidity=15492445.0 spike=0.83
- MASR.CA: score=23.4 buy_ready=False sector_rank=12 price=8.45 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=89.47 liquidity=63944040.0 spike=0.75
- MBSC.CA: score=22.84 buy_ready=False sector_rank=8 price=246.87 support=222.66 resistance=253.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.09 liquidity=47775256.0 spike=2.72
- MCQE.CA: score=14.4 buy_ready=False sector_rank=8 price=191.33 support=179.13 resistance=191.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80698080.0 spike=6.29
- MCRO.CA: score=24.84 buy_ready=False sector_rank=12 price=1.38 support=1.17 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=184791936.0 spike=3.22
- MENA.CA: score=18.77 buy_ready=True sector_rank=11 price=7.07 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=64.8 liquidity=4370763.0 spike=0.6
- MEPA.CA: score=27.3 buy_ready=False sector_rank=12 price=1.77 support=1.52 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=85.29 liquidity=47046672.0 spike=2.95
- MFPC.CA: score=20.38 buy_ready=False sector_rank=17 price=37.93 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=74.64 liquidity=54351416.0 spike=0.56
- MFSC.CA: score=13.6 buy_ready=False sector_rank=12 price=46.02 support=44.22 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=4195949.5 spike=0.52
- MHOT.CA: score=7.83 buy_ready=False sector_rank=21 price=16.23 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.02 liquidity=3425041.25 spike=0.23
- MICH.CA: score=22.4 buy_ready=False sector_rank=12 price=37.99 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.48 liquidity=10085098.0 spike=0.78
- MILS.CA: score=14.4 buy_ready=False sector_rank=12 price=190.0 support=170.0 resistance=197.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=175423920.0 spike=8.68
- MIPH.CA: score=14.87 buy_ready=False sector_rank=14 price=760.29 support=630.13 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=87.74 liquidity=1466607.63 spike=0.41
- MOED.CA: score=20.4 buy_ready=False sector_rank=12 price=0.72 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=11858305.0 spike=0.93
- MOIL.CA: score=15.42 buy_ready=False sector_rank=7 price=0.57 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=80.45 liquidity=641427.31 spike=1.69
- MOIN.CA: score=10.48 buy_ready=False sector_rank=12 price=24.04 support=22.6 resistance=24.76 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=65.07 liquidity=76615.48 spike=0.1
- MOSC.CA: score=22.99 buy_ready=True sector_rank=12 price=286.24 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.69 liquidity=8589674.0 spike=0.66
- MPCI.CA: score=13.74 buy_ready=False sector_rank=12 price=271.93 support=248.25 resistance=284.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=307664800.0 spike=3.17
- MPCO.CA: score=20.87 buy_ready=False sector_rank=19 price=1.86 support=1.7 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=57480188.0 spike=0.78
- MPRC.CA: score=21.4 buy_ready=False sector_rank=12 price=44.43 support=31.74 resistance=44.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=78.35 liquidity=22660044.0 spike=0.44
- MTIE.CA: score=26.4 buy_ready=True sector_rank=4 price=9.38 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.14 liquidity=14170787.0 spike=0.58
- NAHO.CA: score=8.42 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=21546.96 spike=0.86
- NCCW.CA: score=26.4 buy_ready=False sector_rank=12 price=6.71 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.35 liquidity=19234492.0 spike=0.8
- NEDA.CA: score=15.6 buy_ready=False sector_rank=12 price=2.86 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=68.57 liquidity=741345.81 spike=1.23
- NHPS.CA: score=21.4 buy_ready=False sector_rank=12 price=85.8 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=82.33 liquidity=49915176.0 spike=0.77
- NINH.CA: score=25.96 buy_ready=False sector_rank=12 price=22.43 support=17.12 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.51 liquidity=75971488.0 spike=2.28
- NIPH.CA: score=13.4 buy_ready=False sector_rank=14 price=234.2 support=203.5 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=349202592.0 spike=3.0
- OBRI.CA: score=21.4 buy_ready=False sector_rank=12 price=35.32 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.02 liquidity=27936856.0 spike=0.85
- OCDI.CA: score=21.4 buy_ready=False sector_rank=11 price=27.53 support=21.4 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.24 liquidity=26612838.0 spike=0.24
- OCPH.CA: score=21.58 buy_ready=False sector_rank=12 price=430.48 support=337.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=92.13 liquidity=22141528.0 spike=1.09
- ODIN.CA: score=19.88 buy_ready=False sector_rank=12 price=2.46 support=2.05 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=77.46 liquidity=8483541.0 spike=0.58
- OFH.CA: score=23.3 buy_ready=False sector_rank=12 price=0.72 support=0.57 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.92 liquidity=94704680.0 spike=1.95
- OIH.CA: score=31.68 buy_ready=True sector_rank=5 price=1.47 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=177133744.0 spike=2.64
- OLFI.CA: score=22.96 buy_ready=True sector_rank=18 price=22.8 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=29345876.0 spike=0.93
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=711.59 support=705.0 resistance=719.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=161437648.0 spike=1.0
- ORHD.CA: score=22.4 buy_ready=False sector_rank=11 price=38.5 support=37.0 resistance=40.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=104677664.0 spike=0.69
- ORWE.CA: score=25.84 buy_ready=True sector_rank=3 price=23.19 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.47 liquidity=24734030.0 spike=1.22
- PHAR.CA: score=27.62 buy_ready=False sector_rank=14 price=90.81 support=83.6 resistance=92.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.01 liquidity=49184776.0 spike=1.61
- PHDC.CA: score=19.4 buy_ready=False sector_rank=11 price=14.6 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.31 liquidity=220243952.0 spike=0.83
- PHTV.CA: score=15.28 buy_ready=False sector_rank=12 price=310.47 support=216.31 resistance=317.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=81.98 liquidity=1883847.88 spike=0.16
- POUL.CA: score=19.22 buy_ready=True sector_rank=18 price=39.0 support=35.28 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=6268033.5 spike=0.15
- PRCL.CA: score=9.56 buy_ready=False sector_rank=8 price=35.95 support=35.7 resistance=37.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56580576.0 spike=1.08
- PRDC.CA: score=11.22 buy_ready=False sector_rank=11 price=9.45 support=9.17 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=233224848.0 spike=1.91
- PRMH.CA: score=20.43 buy_ready=False sector_rank=12 price=2.75 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=77.05 liquidity=9033541.0 spike=0.4
- RACC.CA: score=26.4 buy_ready=True sector_rank=12 price=10.14 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.22 liquidity=19258080.0 spike=1.0
- RAKT.CA: score=12.82 buy_ready=False sector_rank=12 price=22.64 support=21.25 resistance=23.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=46.82 liquidity=340147.28 spike=1.04
- RAYA.CA: score=24.64 buy_ready=True sector_rank=10 price=7.81 support=6.99 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=142068880.0 spike=1.12
- RMDA.CA: score=19.4 buy_ready=False sector_rank=14 price=4.99 support=4.81 resistance=5.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.22 liquidity=17007824.0 spike=0.95
- ROTO.CA: score=22.4 buy_ready=False sector_rank=12 price=41.43 support=38.0 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.2 liquidity=10433161.0 spike=0.3
- RREI.CA: score=21.4 buy_ready=False sector_rank=12 price=3.79 support=3.34 resistance=4.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=19589662.0 spike=0.69
- RTVC.CA: score=29.4 buy_ready=False sector_rank=12 price=4.12 support=3.55 resistance=3.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.77 liquidity=16087975.0 spike=4.07
- RUBX.CA: score=24.4 buy_ready=True sector_rank=12 price=13.4 support=9.96 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.89 liquidity=18546470.0 spike=0.26
- SAUD.CA: score=16.36 buy_ready=False sector_rank=16 price=21.59 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.51 liquidity=5357286.0 spike=1.0
- SCEM.CA: score=14.4 buy_ready=False sector_rank=8 price=78.46 support=71.25 resistance=81.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=306993312.0 spike=10.31
- SCFM.CA: score=28.4 buy_ready=False sector_rank=12 price=296.7 support=226.5 resistance=308.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=88.04 liquidity=106575528.0 spike=9.14
- SCTS.CA: score=29.08 buy_ready=False sector_rank=15 price=612.27 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=74.17 liquidity=21008880.0 spike=4.0
- SDTI.CA: score=25.12 buy_ready=True sector_rank=12 price=47.92 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=9201032.0 spike=1.76
- SEIG.CA: score=21.07 buy_ready=False sector_rank=12 price=237.55 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=74.45 liquidity=6666076.0 spike=0.3
- SIPC.CA: score=24.66 buy_ready=False sector_rank=12 price=3.86 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.28 liquidity=20889962.0 spike=1.63
- SKPC.CA: score=19.68 buy_ready=False sector_rank=17 price=16.02 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.86 liquidity=40364652.0 spike=1.15
- SMFR.CA: score=21.4 buy_ready=False sector_rank=12 price=234.99 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=79.3 liquidity=13551754.0 spike=0.76
- SNFC.CA: score=18.38 buy_ready=False sector_rank=12 price=11.29 support=11.26 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=8976550.0 spike=0.81
- SPIN.CA: score=28.66 buy_ready=True sector_rank=3 price=14.85 support=13.8 resistance=14.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.18 liquidity=31977652.0 spike=2.63
- SPMD.CA: score=21.4 buy_ready=False sector_rank=12 price=0.45 support=0.41 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=19901340.0 spike=0.89
- SUGR.CA: score=12.96 buy_ready=False sector_rank=18 price=46.92 support=45.31 resistance=48.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=59.55 liquidity=4004536.25 spike=0.77
- SVCE.CA: score=25.12 buy_ready=True sector_rank=12 price=9.4 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=87227496.0 spike=1.36
- SWDY.CA: score=26.94 buy_ready=False sector_rank=1 price=91.4 support=84.3 resistance=93.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.82 liquidity=20902228.0 spike=1.27
- TALM.CA: score=16.33 buy_ready=False sector_rank=15 price=15.71 support=15.27 resistance=16.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=5252603.0 spike=0.4
- TMGH.CA: score=24.62 buy_ready=True sector_rank=11 price=101.99 support=92.1 resistance=103.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.19 liquidity=429303360.0 spike=1.11
- TRTO.CA: score=10.4 buy_ready=False sector_rank=12 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=393.99 spike=0.98
- UEFM.CA: score=28.4 buy_ready=False sector_rank=12 price=550.37 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=77.82 liquidity=14450299.0 spike=4.08
- UEGC.CA: score=11.44 buy_ready=False sector_rank=12 price=2.46 support=2.33 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=76859944.0 spike=2.02
- UNIP.CA: score=14.4 buy_ready=False sector_rank=12 price=0.4 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93290208.0 spike=5.27
- UNIT.CA: score=21.4 buy_ready=False sector_rank=11 price=18.92 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.53 liquidity=10702984.0 spike=0.39
- WCDF.CA: score=14.4 buy_ready=False sector_rank=12 price=586.58 support=582.11 resistance=633.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10083716.0 spike=8.48
- WKOL.CA: score=29.4 buy_ready=False sector_rank=12 price=318.34 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.61 liquidity=31269402.0 spike=4.32
- ZEOT.CA: score=22.4 buy_ready=False sector_rank=12 price=11.77 support=10.4 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.74 liquidity=15791226.0 spike=0.32
- ZMID.CA: score=24.02 buy_ready=False sector_rank=11 price=7.62 support=6.19 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.14 liquidity=310990048.0 spike=1.31

## Backtesting Lite
- ELEC.CA: 180d return=-19.57%, max drawdown=-35.96%, MA20>MA50 days last20=0, as_of=2026-07-18T21:00:00+00:00
- OIH.CA: 180d return=30.28%, max drawdown=-14.56%, MA20>MA50 days last20=0, as_of=2026-07-18T21:00:00+00:00
- ARCC.CA: 180d return=42.22%, max drawdown=-12.39%, MA20>MA50 days last20=12, as_of=2026-07-18T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ELEC.CA: status=RECENT_ACCEPTED latest=2025-12-31 age_days=201 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt (ELEC.CA) reported its 6-month consolidated results for the period ending June 30, 2025, with a net profit of EGP 486,422,541, as disclosed on August 28, 2025. The company's financial statements for Q1 2025 and fiscal year 2025 are also available, with fiscal year 2025 financials showing updates as of December 31, 2025.
  - Electro Cable Egypt (ELEC.CA) Reports 6 Months Consolidated Results (August 28, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhJKpzAvDZnT8PoTtEKAI3ubz14KxV7vc8Sc6SSIsdmDDEkaCyroHIyq1Jj0jhfwatgb_rQJwRWKnwQxidzrOuG2P_19TyfUQKCpYjcO-wEzSLcOV2RMXKT9WPBRhQbldbHQQ6hniw0lTTNixuR3exINYKk1WfVH6D8SCGItA3zwgz4_8jFtypuTR_4gFeh2fN-rwJF6YC_wBPg==
  - Electro Cable Egypt Income Statement (Fiscal Year 2025 data as of December 31, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-GhJ8lQnCkEAtpvCovgC0rtM_yn7IOo0LUpuFShL-rW2VEQ079RfhURZi6FXAd6zV9s3EWSvlVT7k0VH_yAbpe_5wmIoaHDu3UyVV4tB2NyzpM_nHo5ogCF-vsH5r9sVEowS9SWpdZ4iPwhM_8w==
  - Financial Statements - Electro Cable Egypt (2025 Q1): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3EZvV42woRTxz29m7eMyy5L9e5BV3EaMw4cSpzqkfQ-Tdnc97Q1RTWjQeisV2yP4BmgN-WK_zOkKYyjaVvhd5rE51sQDvvUvX6CXMvI7kDKIHGIoLrj94d5Wt-nn4LQOm60d1O4jVDYqPYw==
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- ARCC.CA: status=RECENT_ACCEPTED latest=2026-07-16 age_days=4 sources=3 expected=Arabian Cement Company summary=Arabian Cement Company (ARCC.CA) has filed several disclosure forms with the Egyptian Exchange (EGX) regarding its Board of Directors and shareholders' structure, with recent filings on July 16, 2026, and March 31, 2026. The company also announced Board of Directors' meeting decisions on June 23, 2026, and June 1, 2026.
  - Arabian Cement Company (ARCC.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8ng16QHqdkSODNXyJ-t_H7uvrm-CtNkM3Fcr6upM19GVSJqs9SwkBt7OeT0SlYdQfNQS_B7Yct46w2z75cGaURxec16s_0UtHezDm6GluQ-BmgxZJLJafhN9iXKT6Az2jwFvNarL-IPtbNqJuhg==
  - Arabian Cement Company (ARCC.CA) - Disclosure Form for the BoD & the Shareholders' Structure (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDL2MHLaWk51Uj9sMa95NWPAKqaMilkeP1hHkdEN9e63O97hTm0gnNkuM1FPy4_92CR2-5Hcld0HwNJf4DeUo_ybthkaC89Krskfrach9IoAEqBSH_7bs9byd2nwEVYG8s6aSB_9cbdWk3PQT9QQ==
  - Arabian Cement Company (ARCC.CA) - Decisions of the BoD Meeting (June 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJXIjZela8vt54uJZot4aBHcOMPesL9Rmo9OmeO3DW1tRTgamCiXOVoZASBwugUTSmECaXPCEyCeIFSGKza89KJG1le6l1-s2Gy3xlcJfwQH7_k8_WW8F-6W0nIEU93SgQYyp5ip265V-jY1YNwXvsdhtdZkWXU4HfbvSz9ts=
- EALR.CA: status=RECENT_ACCEPTED latest=2026-07-09 age_days=11 sources=3 expected=Arab Company For Land Reclamation summary=Arab Company For Land Reclamation (EALR.CA) reported its 3-month results on July 9, 2026. The company's fiscal year 2025 revenue was EGP 168.58 million, with earnings of EGP 5.11 million. As of June 19, 2026, the company's profile and key executives were updated.
  - El Arabia for Land Reclamation (EALR.CA) Reports 3 Months Results (July 9, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGteT04k82VOSHZDeyg1HC5f67D1uZ9JO_mq5xZTHtdFWpa-fuH2PdUlFNgUmTHtsj3QldI9NLFQEQsCSfp87de5qInZg78gI0bvU0X0xKRIzbXD7wy8MywMoCOIN9Nq2ysF8M2bJz7332pEdIDD9gFcY=
  - Arab Company For Land Reclamation (EGX:EALR) - Stock Analysis (June 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_2h2tkOeBkISYqqxDL1GZ1-pj0W_brtbRNa9h61T_P-jeUC9cfXaWnDOmsRkG9As1PD2KPFWI-tR7BpzxbBlCOnht_pmVLfmB25XDmtG9XWmNBKx6Hls1LvXaNki9pJLKoIlig1PKrqvPLg==
  - Arab Company For Land Reclamation (EGX:EALR) Stock Price & Overview (Fiscal Year 2025 Financials): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGcGDA40ZY5Y-SnM1dSAFAFMTg0oprkQL6-PAkWSH5KsNSi8RwpTPF-mPtfl4nnG6AZZE07RtL5-p1DFSroNQbikAL2FmpLcv8BBJwOyTy60i6dxgfcjMCwWznxVKB2WNIYzM=
- RTVC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Remco Tourism Villages Construction summary=Evidence rejected for RTVC.CA: source text did not clearly match RTVC.CA / Remco Tourism Villages Construction.
- WKOL.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=565 sources=2 expected=Wadi Kom Ombo For Land Reclamation Co. summary=Wadi Kom Ombo For Land Reclamation Co. (WKOL.CA) reported a significant increase in its fiscal year 2025 revenue to EGP 311.01 million, up 122.44% from the previous year, with earnings reaching EGP 81.16 million, an increase of 254.58%.
  - Wadi Kom Ombo For Land Reclamation Co. (EGX:WKOL) - Stock Analysis (Fiscal Year 2025 Financials): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfZSfbMfpHcIByS67nNCvCWVNrzStGZHXT9Fx6VF-zuvl1q_o-ADYfIJ6j0aRR8_WRbjVwTqfxq8sP_TuEO2_wj1KQ9uPiI87gZHzFOiIEIPJpNsZw_2HG4FvmMC6b-vkYKv8=
  - Wadi Kom Ombo Land Reclamation (WKOL) Revenue - Starta | Master the EGX (Fiscal Year 2025 Revenue): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeVsCw5Jb0vuU8Ji1qnWKn4Is2jfAQsCGPjYQTQTSlMFPQ2E0d1FUt_vWhnVqFAUCHtSeQ88a1PM3I7YOc5ZP8WtnDYgS_3NJUqTXTnzW9TqNacYlLKUNwl3g1uQLriXuyXuDa14Ul
- SCTS.CA: status=RECENT_ACCEPTED latest=2026-07-14 age_days=6 sources=3 expected=Suez Canal Company for Technology Settling summary=Suez Canal Company for Technology Settling (SCTS.CA) released its third-quarter 2026 earnings on July 14, 2026, reporting an EPS of EGP 2.90. Consolidated financial statements for the fiscal period ending May 31, 2026, were attached on July 12, 2026, along with decisions from the Board of Directors' meeting. The company also declared cash dividends on June 11, 2026, and its fiscal year 2025 revenue was EGP 2.72 billion with earnings of EGP 1.73 billion.
  - Suez Canal Company for Technology Settling (S.A.E) (CASE:SCTS) Stock Price - Third quarter 2026 earnings released (July 14, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtTe8RodSGMg_ISOUtEOo7D5pq3DArImbEIKhxAZTXI0iw04tpYjIQuQeAzAaHYSOYvSg0V40jJc0PsABEKQwWBuQ2bvjllFj-jvYM4aJuOYNtaiFWTcOJiOSA7x24aA==
  - Sues Canal Company For Technology Settling (SCTS.CA) - Consolidated Financial Statements for Fiscal Period Ending on 31/05/2026 (July 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbYrtCV23nzVC0-ItxsoIw9oru9VMxSPUm6miZhy9gUuENy7XGplMifnaZyhF4CmNo_1RBQeLUXuZ6msyDBqhxeRKchu_whd3Sl2P3PK0YaEzVmn8M_7Xl9tnV0QGXB9TBc6JuI0BhIOu-d4LaaEbp
  - Sues Canal Company For Technology Settling (SCTS.CA) - Decisions of the Board of Directors' Meeting (July 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbYrtCV23nzVC0-ItxsoIw9oru9VMxSPUm6miZhy9gUuENy7XGplMifnaZyhF4CmNo_1RBQeLUXuZ6msyDBqhxeRKchu_whd3Sl2P3PK0YaEzVmn8M_7Xl9tnV0QGXB9TBc6JuI0BhIOu-d4LaaEbp
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-07-16 age_days=4 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) announced on July 16, 2026, that its Board of Directors resolved not to proceed with the proposed RDH transaction with Helios Investments. The company released its Q1 2026 audited financial results on May 21, 2026, reporting strong underlying business performance. Telecom Egypt's 2025 consolidated profits exceeded EGP 22.5 billion, and the company announced dividends for 2025.
  - Telecom Egypt Announces It Will Not Proceed with the Proposed RDH Transaction with Helios Investments (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwvwXGwShOkLQGDEaG9Wa5SQLgq7MUKEE4jEatHZG3Z8tqoTTzQiINLeKmW-SLl__1cxqRAjbJiK1APLW9AuW6uSdBg-kx7OAIGA8=
  - Telecom Egypt's Board of Directors & Executive Managers Release (July 16, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRjec_ZATugUz6QFMro68skgOVqNZLBYpalY5tTRffTsbYI3mxLVDEIYmczvp-ZI8s9GAreBV0zSxDmXmGj2CZ5H2aVEnyLQur4xJkO8VEQWLAjNA1nuoL5ENSP7d0yLZeYIHiAnZ2x8qBthf5u2
  - Q1 2026 Results: Telecom Egypt Reports Strong Underlying Business Performance (May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwvwXGwShOkLQGDEaG9Wa5SQLgq7MUKEE4jEatHZG3Z8tqoTTzQiINLeKmW-SLl__1cxqRAjbJiK1APLW9AuW6uSdBg-kx7OAIGA8=

## Warnings
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for RTVC.CA: source text did not clearly match RTVC.CA / Remco Tourism Villages Construction.
- Evidence for WKOL.CA matches the company but appears old; latest detected date is 2025-01-01.
