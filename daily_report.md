# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-20T09:37:26.602987+00:00
Generated Cairo: 2026-07-20 12:37
Run timing: target 09:15 Cairo | generated Cairo 2026-07-20 12:37 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-20 12:32

## Control Center
- Action tickets: 1 prioritized signal(s)
- BUY-ready candidates: 41
- Data quality issues: 1
- Tradeable price/liquidity tickers: 171/189
- Top sector: Industrial Goods & Cables

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, July 20
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 70.0% / above MA50 55.0%
- EGX70 regime: BULLISH / above MA20 76.92% / above MA50 76.92%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- COMI.CA: liquidity=425714624.0 spike=1.18 score=25.89
- SCEM.CA: liquidity=227673648.0 spike=7.65 score=14.4
- GDWA.CA: liquidity=191367664.0 spike=5.6 score=25.4
- CCAP.CA: liquidity=181374112.0 spike=0.29 score=23.4
- ZMID.CA: liquidity=160613600.0 spike=0.68 score=24.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: The scanner prioritized ARCC.CA as a BUY SETUP because it shows liquidity accumulation, price above MA20/MA50, RSI near 56, and sits just above support with nearby resistance, while the EGX30 and EGX70 indices are bullish but the risk mode restricts entries to selective swing trades only.
- ARCC.CA liquidity spike ~4× average indicates short‑term buying interest.
- Price above MA20/MA50 and RSI 55.7 suggests mild bullish momentum.
- Current price ~56.9 is just above 53.0 support and slightly below 56.7 resistance, creating a tight range for the next 1‑3 days.
- Building Materials sector is not among the leading groups, adding uncertainty to the setup.
- EGX30 and EGX70 are bullish, but risk mode SELECTIVE_SWING_TRADES_ONLY means only high‑confidence swing setups should be acted upon.

## Top Liquidity Spikes
- CEFM.CA: spike=12.26 liquidity=79733584.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AFMC.CA: spike=8.1 liquidity=59815424.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCEM.CA: spike=7.65 liquidity=227673648.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCFM.CA: spike=7.13 liquidity=83147752.0 outlook=CONSTRUCTIVE score=64.72 buy_ready=False
- MILS.CA: spike=6.96 liquidity=140600480.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Cables: score=10.86 5d=4.73% 20d=6.58% aboveMA50=100.0%
- #2 Telecommunications: score=9.74 5d=-0.32% 20d=4.44% aboveMA50=100.0%
- #3 Real Estate: score=9.46 5d=2.49% 20d=17.06% aboveMA50=84.62%
- #4 Automotive & Distribution: score=9.2 5d=2.34% 20d=8.45% aboveMA50=100.0%
- #5 Textiles: score=9.02 5d=1.13% 20d=4.41% aboveMA50=100.0%
- #6 Transportation & Logistics: score=8.59 5d=1.92% 20d=6.21% aboveMA50=100.0%
- #7 Investment Holding: score=8.33 5d=1.71% 20d=4.19% aboveMA50=100.0%
- #8 Building Materials: score=7.76 5d=0.01% 20d=0.0% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY ARCC.CA
  - Entry: 56.93 | Take profit: 61.49 | Stop loss: 54.65
  - Confidence: LOW | score=29.4 | outlook=BULLISH_WATCH 89.76
  - Reason: BUY SETUP: ARCC.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 55.7, support 53.0, resistance 56.7, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- OIH.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARCC.CA: BULLISH_WATCH score=89.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SPIN.CA: BULLISH_WATCH score=88.02 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- ELEC.CA: BULLISH_WATCH score=88 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- MENA.CA: BULLISH_WATCH score=87.46 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- APSW.CA: BULLISH_WATCH score=82.72 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading
- SVCE.CA: BULLISH_WATCH score=82.72 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- TMGH.CA: BULLISH_WATCH score=81.46 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- EALR.CA: BULLISH_WATCH score=80.72 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- CICH.CA: BULLISH_WATCH score=78.49 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- OIH.CA: rank=30.94 outlook=BULLISH_WATCH outlook_score=100 sector_rank=7 price=1.48 support=1.35 resistance=1.43 liquidity=152634752.0
- FERC.CA: rank=30.87 outlook=BULLISH_WATCH outlook_score=72.68 sector_rank=15 price=80.5 support=72.75 resistance=80.83 liquidity=29061512.0
- ARCC.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=89.76 sector_rank=8 price=56.93 support=53.0 resistance=56.7 liquidity=74141072.0
- EALR.CA: rank=28.32 outlook=BULLISH_WATCH outlook_score=80.72 sector_rank=11 price=375.79 support=332.0 resistance=425.0 liquidity=39967148.0
- APSW.CA: rank=27.77 outlook=BULLISH_WATCH outlook_score=82.72 sector_rank=11 price=9.28 support=8.0 resistance=8.84 liquidity=4372509.0
- SPIN.CA: rank=26.68 outlook=BULLISH_WATCH outlook_score=88.02 sector_rank=5 price=14.89 support=13.8 resistance=14.8 liquidity=25996158.0
- GBCO.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=73.2 sector_rank=4 price=32.6 support=28.6 resistance=34.2 liquidity=29165610.0
- EFIH.CA: rank=26.08 outlook=CONSTRUCTIVE outlook_score=68.2 sector_rank=14 price=22.38 support=20.0 resistance=23.65 liquidity=30291952.0
- COMI.CA: rank=25.89 outlook=CONSTRUCTIVE outlook_score=67.83 sector_rank=16 price=135.89 support=126.21 resistance=137.98 liquidity=425714624.0
- ATQA.CA: rank=25.87 outlook=CONSTRUCTIVE outlook_score=63.68 sector_rank=15 price=9.72 support=9.21 resistance=9.88 liquidity=13148941.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=12.4 buy_ready=False sector_rank=11 price=247.67 support=243.0 resistance=253.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37495412.0 spike=2.5
- ABUK.CA: score=22.87 buy_ready=False sector_rank=15 price=73.92 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=71.65 liquidity=70149416.0 spike=0.43
- ACAMD.CA: score=22.4 buy_ready=False sector_rank=11 price=2.36 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=71.88 liquidity=74904840.0 spike=0.98
- ACGC.CA: score=24.4 buy_ready=True sector_rank=5 price=9.8 support=8.92 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=67.93 liquidity=11063652.0 spike=0.55
- ADCI.CA: score=20.52 buy_ready=True sector_rank=11 price=244.61 support=227.55 resistance=249.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=51.61 liquidity=6119444.0 spike=0.55
- ADIB.CA: score=20.53 buy_ready=False sector_rank=16 price=46.62 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=39072836.0 spike=0.42
- ADPC.CA: score=18.0 buy_ready=False sector_rank=11 price=3.86 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=83.08 liquidity=6600622.5 spike=0.27
- AFDI.CA: score=15.63 buy_ready=False sector_rank=11 price=47.64 support=41.84 resistance=48.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=72.3 liquidity=1231347.75 spike=0.09
- AFMC.CA: score=14.4 buy_ready=False sector_rank=11 price=109.26 support=99.0 resistance=109.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59815424.0 spike=8.1
- AJWA.CA: score=20.01 buy_ready=False sector_rank=11 price=174.5 support=172.1 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=45.09 liquidity=7605463.5 spike=0.57
- ALCN.CA: score=24.36 buy_ready=False sector_rank=6 price=29.91 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=73.16 liquidity=9963011.0 spike=0.48
- ALUM.CA: score=20.81 buy_ready=False sector_rank=11 price=23.69 support=20.55 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=80.23 liquidity=8667318.0 spike=1.37
- AMER.CA: score=24.4 buy_ready=False sector_rank=3 price=4.08 support=2.28 resistance=4.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=97.98 liquidity=71217520.0 spike=0.72
- AMES.CA: score=21.4 buy_ready=False sector_rank=11 price=119.53 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=78.13 liquidity=24482562.0 spike=0.28
- AMIA.CA: score=12.08 buy_ready=False sector_rank=11 price=10.5 support=9.95 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23212828.0 spike=2.34
- AMOC.CA: score=23.4 buy_ready=False sector_rank=9 price=8.33 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=75.41 liquidity=35507904.0 spike=0.62
- APSW.CA: score=27.77 buy_ready=True sector_rank=11 price=9.28 support=8.0 resistance=8.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=4372509.0 spike=4.1
- ARAB.CA: score=25.4 buy_ready=False sector_rank=3 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=74.07 liquidity=67232040.0 spike=0.58
- ARCC.CA: score=29.4 buy_ready=True sector_rank=8 price=56.93 support=53.0 resistance=56.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=55.7 liquidity=74141072.0 spike=3.96
- AREH.CA: score=22.4 buy_ready=False sector_rank=11 price=1.51 support=1.48 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=10040886.0 spike=0.26
- ARVA.CA: score=25.06 buy_ready=True sector_rank=11 price=11.14 support=10.5 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=43.88 liquidity=22348742.0 spike=1.33
- ASCM.CA: score=22.4 buy_ready=True sector_rank=11 price=60.88 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=67.49 liquidity=16007145.0 spike=0.23
- ASPI.CA: score=23.93 buy_ready=False sector_rank=11 price=0.35 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=73.81 liquidity=9532139.0 spike=0.39
- ATLC.CA: score=19.43 buy_ready=False sector_rank=10 price=5.15 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=7030961.5 spike=0.89
- ATQA.CA: score=25.87 buy_ready=True sector_rank=15 price=9.72 support=9.21 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=13148941.0 spike=0.44
- AXPH.CA: score=11.82 buy_ready=False sector_rank=11 price=1225.45 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=75.81 liquidity=417081.5 spike=0.11
- BINV.CA: score=19.99 buy_ready=True sector_rank=7 price=49.5 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=62.84 liquidity=3585876.5 spike=0.54
- BIOC.CA: score=12.84 buy_ready=False sector_rank=11 price=120.41 support=116.7 resistance=137.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46648004.0 spike=2.72
- BTFH.CA: score=26.4 buy_ready=False sector_rank=10 price=3.14 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=70.45 liquidity=94634792.0 spike=0.45
- CAED.CA: score=24.02 buy_ready=False sector_rank=11 price=128.43 support=68.0 resistance=134.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=97.44 liquidity=56325468.0 spike=1.31
- CANA.CA: score=17.81 buy_ready=False sector_rank=16 price=35.81 support=34.7 resistance=38.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=13882086.0 spike=1.14
- CCAP.CA: score=23.4 buy_ready=False sector_rank=7 price=5.47 support=4.65 resistance=5.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=86.92 liquidity=181374112.0 spike=0.29
- CCRS.CA: score=22.88 buy_ready=False sector_rank=11 price=2.62 support=2.18 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=71.23 liquidity=6478059.0 spike=0.43
- CEFM.CA: score=14.4 buy_ready=False sector_rank=11 price=148.04 support=129.55 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=79733584.0 spike=12.26
- CERA.CA: score=24.4 buy_ready=False sector_rank=11 price=1.35 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=70.27 liquidity=18675452.0 spike=0.68
- CFGH.CA: score=10.4 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=64.29 liquidity=4285.32 spike=0.47
- CICH.CA: score=18.12 buy_ready=True sector_rank=10 price=12.12 support=11.52 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=52.73 liquidity=1720551.5 spike=0.34
- CIEB.CA: score=15.86 buy_ready=True sector_rank=16 price=24.18 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=64.44 liquidity=2326341.75 spike=0.32
- CIRA.CA: score=21.39 buy_ready=False sector_rank=17 price=31.29 support=27.17 resistance=33.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=70.18 liquidity=8455745.0 spike=0.23
- CLHO.CA: score=24.35 buy_ready=True sector_rank=13 price=17.22 support=15.5 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=62.55 liquidity=48414464.0 spike=1.05
- CNFN.CA: score=20.77 buy_ready=True sector_rank=10 price=4.88 support=4.54 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=69.81 liquidity=6373510.5 spike=0.13
- COMI.CA: score=25.89 buy_ready=True sector_rank=16 price=135.89 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=57.86 liquidity=425714624.0 spike=1.18
- COPR.CA: score=25.4 buy_ready=True sector_rank=11 price=0.38 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=62.96 liquidity=14718016.0 spike=0.71
- COSG.CA: score=23.4 buy_ready=False sector_rank=11 price=1.69 support=1.47 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=31280234.0 spike=0.81
- CPCI.CA: score=13.87 buy_ready=False sector_rank=11 price=458.79 support=365.01 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=76.19 liquidity=2465337.75 spike=0.23
- CSAG.CA: score=20.2 buy_ready=False sector_rank=6 price=33.3 support=30.87 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=70.57 liquidity=5803602.5 spike=0.29
- DAPH.CA: score=17.39 buy_ready=True sector_rank=11 price=86.7 support=78.52 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=2985558.25 spike=0.29
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=11 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.04 buy_ready=False sector_rank=19 price=26.87 support=25.75 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=52.49 liquidity=404958.41 spike=0.08
- DSCW.CA: score=23.64 buy_ready=False sector_rank=11 price=1.96 support=1.71 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=96.15 liquidity=48475520.0 spike=1.12
- DTPP.CA: score=21.4 buy_ready=False sector_rank=11 price=236.28 support=114.67 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=86.11 liquidity=40163576.0 spike=0.75
- EALR.CA: score=28.32 buy_ready=True sector_rank=11 price=375.79 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=65.29 liquidity=39967148.0 spike=2.96
- EASB.CA: score=14.08 buy_ready=False sector_rank=11 price=7.21 support=6.88 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=39.31 liquidity=1682747.5 spike=0.1
- EAST.CA: score=14.99 buy_ready=False sector_rank=19 price=37.18 support=36.11 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=35.99 liquidity=8354814.5 spike=0.17
- EBSC.CA: score=13.46 buy_ready=False sector_rank=11 price=1.89 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=1064679.13 spike=0.16
- ECAP.CA: score=17.81 buy_ready=True sector_rank=11 price=33.0 support=31.52 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=59.19 liquidity=3410224.0 spike=0.4
- EDFM.CA: score=28.4 buy_ready=False sector_rank=11 price=388.71 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=88.23 liquidity=11938751.0 spike=3.93
- EEII.CA: score=24.4 buy_ready=False sector_rank=11 price=2.75 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=13607119.0 spike=0.65
- EFIC.CA: score=22.69 buy_ready=False sector_rank=15 price=186.82 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=43.57 liquidity=21191846.0 spike=2.41
- EFID.CA: score=15.64 buy_ready=False sector_rank=19 price=27.65 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=66.34 liquidity=14417323.0 spike=0.35
- EFIH.CA: score=26.08 buy_ready=True sector_rank=14 price=22.38 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=64.06 liquidity=30291952.0 spike=0.77
- EGAL.CA: score=22.87 buy_ready=False sector_rank=15 price=308.17 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=78.21 liquidity=29306694.0 spike=0.64
- EGAS.CA: score=23.54 buy_ready=True sector_rank=9 price=52.57 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=7142427.5 spike=0.64
- EGBE.CA: score=12.57 buy_ready=False sector_rank=16 price=0.47 support=-0.34 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=96.79 liquidity=39240.93 spike=-2.54
- EGCH.CA: score=17.87 buy_ready=False sector_rank=15 price=13.22 support=12.13 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=78.87 liquidity=18468270.0 spike=0.36
- EGSA.CA: score=18.16 buy_ready=False sector_rank=2 price=9.0 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=77.08 liquidity=39832.3 spike=3.36
- EGTS.CA: score=20.4 buy_ready=False sector_rank=3 price=17.78 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=62.7 liquidity=11520228.0 spike=0.22
- EHDR.CA: score=24.68 buy_ready=False sector_rank=11 price=2.92 support=2.37 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=81.71 liquidity=55802444.0 spike=1.64
- EKHO.CA: score=8.4 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=29.56 buy_ready=False sector_rank=1 price=2.25 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=84635376.0 spike=1.58
- ELKA.CA: score=9.4 buy_ready=False sector_rank=11 price=2.05 support=2.02 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40547936.0 spike=0.62
- ELNA.CA: score=14.04 buy_ready=False sector_rank=11 price=38.82 support=35.55 resistance=40.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=61.57 liquidity=863557.19 spike=1.39
- ELSH.CA: score=24.4 buy_ready=False sector_rank=11 price=14.4 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=73.32 liquidity=37604504.0 spike=0.29
- ELWA.CA: score=15.95 buy_ready=False sector_rank=11 price=1.99 support=1.87 resistance=2.14 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=47.22 liquidity=2526197.55 spike=2.01
- EMFD.CA: score=19.42 buy_ready=False sector_rank=3 price=11.72 support=11.24 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=6022836.5 spike=0.07
- ENGC.CA: score=24.4 buy_ready=False sector_rank=11 price=42.57 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=72.32 liquidity=11592301.0 spike=0.49
- EOSB.CA: score=14.43 buy_ready=False sector_rank=11 price=1.48 support=1.48 resistance=1.55 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=26589.68 spike=0.48
- EPCO.CA: score=24.06 buy_ready=False sector_rank=11 price=11.16 support=8.5 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=84.49 liquidity=29055754.0 spike=1.33
- EPPK.CA: score=14.88 buy_ready=False sector_rank=11 price=14.58 support=12.31 resistance=15.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=69.54 liquidity=481858.44 spike=0.42
- ETEL.CA: score=28.4 buy_ready=False sector_rank=2 price=100.79 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=73.26 liquidity=38785660.0 spike=0.62
- ETRS.CA: score=17.66 buy_ready=True sector_rank=11 price=10.81 support=10.12 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=54.47 liquidity=3258725.0 spike=0.05
- EXPA.CA: score=22.53 buy_ready=False sector_rank=16 price=19.7 support=18.03 resistance=19.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=77.54 liquidity=13165293.0 spike=0.5
- FAIT.CA: score=14.23 buy_ready=False sector_rank=16 price=37.28 support=35.06 resistance=37.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=73.42 liquidity=700251.13 spike=0.26
- FAITA.CA: score=8.55 buy_ready=False sector_rank=16 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=19685.21 spike=0.54
- FERC.CA: score=30.87 buy_ready=True sector_rank=15 price=80.5 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=29061512.0 spike=5.98
- FWRY.CA: score=23.08 buy_ready=False sector_rank=14 price=19.25 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=62667004.0 spike=0.46
- GBCO.CA: score=26.4 buy_ready=True sector_rank=4 price=32.6 support=28.6 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=59.68 liquidity=29165610.0 spike=0.39
- GDWA.CA: score=25.4 buy_ready=False sector_rank=11 price=0.87 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=191367664.0 spike=5.6
- GGCC.CA: score=24.48 buy_ready=False sector_rank=11 price=0.88 support=0.42 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=97.13 liquidity=41589052.0 spike=1.54
- GIHD.CA: score=24.54 buy_ready=True sector_rank=11 price=51.02 support=40.66 resistance=55.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=68.76 liquidity=35364004.0 spike=1.07
- GMCI.CA: score=14.97 buy_ready=False sector_rank=11 price=2.14 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=71.25 liquidity=573794.56 spike=0.46
- GRCA.CA: score=14.4 buy_ready=False sector_rank=11 price=65.95 support=63.01 resistance=68.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37535540.0 spike=6.08
- GSSC.CA: score=24.96 buy_ready=False sector_rank=11 price=273.14 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=90.3 liquidity=15500415.0 spike=1.78
- GTWL.CA: score=9.4 buy_ready=False sector_rank=11 price=100.7 support=95.15 resistance=104.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=101990888.0 spike=0.83
- HDBK.CA: score=17.53 buy_ready=False sector_rank=16 price=78.84 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=17079430.0 spike=0.42
- HELI.CA: score=24.4 buy_ready=False sector_rank=3 price=8.05 support=6.36 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=89.29 liquidity=100264256.0 spike=0.59
- HRHO.CA: score=24.4 buy_ready=True sector_rank=10 price=27.08 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=57.62 liquidity=85217776.0 spike=0.69
- ICID.CA: score=15.85 buy_ready=True sector_rank=11 price=8.38 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=57.06 liquidity=1450878.88 spike=0.17
- IDRE.CA: score=19.79 buy_ready=True sector_rank=11 price=45.59 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=3392229.0 spike=0.25
- IFAP.CA: score=11.11 buy_ready=False sector_rank=18 price=19.2 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=2349963.25 spike=0.46
- INFI.CA: score=24.34 buy_ready=False sector_rank=11 price=107.74 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=77.65 liquidity=26393842.0 spike=2.47
- IRON.CA: score=10.18 buy_ready=False sector_rank=15 price=31.55 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=57.8 liquidity=2309901.25 spike=0.31
- ISMA.CA: score=22.4 buy_ready=False sector_rank=11 price=28.39 support=26.54 resistance=30.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=38.13 liquidity=15464813.0 spike=0.68
- ISMQ.CA: score=23.87 buy_ready=True sector_rank=15 price=9.25 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=13401357.0 spike=0.1
- ISPH.CA: score=19.25 buy_ready=False sector_rank=13 price=11.5 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=17470684.0 spike=0.33
- JUFO.CA: score=17.64 buy_ready=False sector_rank=19 price=29.11 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=46.64 liquidity=17540020.0 spike=0.88
- KABO.CA: score=24.42 buy_ready=False sector_rank=5 price=8.14 support=6.04 resistance=7.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=95.05 liquidity=53455216.0 spike=1.51
- KWIN.CA: score=13.32 buy_ready=False sector_rank=11 price=89.99 support=83.99 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78017088.0 spike=2.96
- KZPC.CA: score=11.28 buy_ready=False sector_rank=11 price=8.57 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=61.0 liquidity=883906.19 spike=0.16
- LCSW.CA: score=21.4 buy_ready=False sector_rank=8 price=33.52 support=27.01 resistance=33.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=86.54 liquidity=53957084.0 spike=0.81
- LUTS.CA: score=22.4 buy_ready=False sector_rank=11 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=10793351.0 spike=0.26
- MAAL.CA: score=18.07 buy_ready=False sector_rank=11 price=8.7 support=6.46 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=91.88 liquidity=6671342.0 spike=0.36
- MASR.CA: score=23.4 buy_ready=False sector_rank=11 price=8.32 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=89.47 liquidity=32628658.0 spike=0.38
- MBSC.CA: score=20.84 buy_ready=False sector_rank=8 price=245.09 support=222.66 resistance=253.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=65.09 liquidity=30174538.0 spike=1.72
- MCQE.CA: score=29.4 buy_ready=False sector_rank=8 price=188.0 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=71.47 liquidity=54991848.0 spike=4.28
- MCRO.CA: score=23.46 buy_ready=False sector_rank=11 price=1.39 support=1.17 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=145035840.0 spike=2.53
- MENA.CA: score=16.65 buy_ready=True sector_rank=3 price=7.11 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=64.8 liquidity=1251932.13 spike=0.17
- MEPA.CA: score=25.16 buy_ready=False sector_rank=11 price=1.79 support=1.52 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=85.29 liquidity=29910114.0 spike=1.88
- MFPC.CA: score=20.87 buy_ready=False sector_rank=15 price=38.02 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=74.64 liquidity=31421312.0 spike=0.32
- MFSC.CA: score=11.68 buy_ready=False sector_rank=11 price=46.39 support=44.22 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=2275532.0 spike=0.28
- MHOT.CA: score=5.88 buy_ready=False sector_rank=21 price=16.26 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=36.02 liquidity=1479642.75 spike=0.1
- MICH.CA: score=19.55 buy_ready=False sector_rank=11 price=38.0 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=72.48 liquidity=7147193.0 spike=0.55
- MILS.CA: score=14.4 buy_ready=False sector_rank=11 price=191.99 support=170.0 resistance=197.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=140600480.0 spike=6.96
- MIPH.CA: score=19.75 buy_ready=False sector_rank=13 price=762.73 support=630.13 resistance=780.0 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=87.74 liquidity=5422247.43 spike=1.54
- MOED.CA: score=20.16 buy_ready=False sector_rank=11 price=0.73 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=6761119.5 spike=0.53
- MOIL.CA: score=13.56 buy_ready=False sector_rank=9 price=0.56 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=80.45 liquidity=156506.36 spike=0.41
- MOIN.CA: score=10.48 buy_ready=False sector_rank=11 price=24.04 support=22.6 resistance=24.76 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=65.07 liquidity=76615.48 spike=0.1
- MOSC.CA: score=20.01 buy_ready=True sector_rank=11 price=290.0 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=66.69 liquidity=5614813.5 spike=0.43
- MPCI.CA: score=21.4 buy_ready=False sector_rank=11 price=255.37 support=221.5 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=76.59 liquidity=60236192.0 spike=0.62
- MPCO.CA: score=22.76 buy_ready=True sector_rank=18 price=1.87 support=1.7 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=36445236.0 spike=0.5
- MPRC.CA: score=16.85 buy_ready=False sector_rank=11 price=42.92 support=31.74 resistance=44.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=78.35 liquidity=5451392.0 spike=0.11
- MTIE.CA: score=25.42 buy_ready=True sector_rank=4 price=9.38 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=64.14 liquidity=9023726.0 spike=0.37
- NAHO.CA: score=8.42 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=16131.65 spike=0.64
- NCCW.CA: score=26.4 buy_ready=False sector_rank=11 price=6.67 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=71.35 liquidity=11774054.0 spike=0.49
- NEDA.CA: score=15.27 buy_ready=False sector_rank=11 price=2.86 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:58 AM market time freshness=DELAYED_CURRENT RSI=68.57 liquidity=665227.38 spike=1.1
- NHPS.CA: score=21.4 buy_ready=False sector_rank=11 price=87.56 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=82.33 liquidity=28215404.0 spike=0.44
- NINH.CA: score=23.96 buy_ready=False sector_rank=11 price=22.69 support=17.12 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=86.51 liquidity=42765104.0 spike=1.28
- NIPH.CA: score=9.73 buy_ready=False sector_rank=13 price=215.64 support=203.5 resistance=220.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=144816048.0 spike=1.24
- OBRI.CA: score=21.4 buy_ready=False sector_rank=11 price=35.71 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=68.02 liquidity=14559996.0 spike=0.44
- OCDI.CA: score=15.79 buy_ready=False sector_rank=3 price=28.09 support=21.4 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:13 AM market time freshness=DELAYED_CURRENT RSI=75.24 liquidity=3387812.5 spike=0.03
- OCPH.CA: score=21.4 buy_ready=False sector_rank=11 price=441.43 support=337.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=92.13 liquidity=12902168.0 spike=0.63
- ODIN.CA: score=16.13 buy_ready=False sector_rank=11 price=2.45 support=2.05 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=77.46 liquidity=4729071.5 spike=0.32
- OFH.CA: score=21.5 buy_ready=False sector_rank=11 price=0.71 support=0.57 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=87.92 liquidity=50810124.0 spike=1.05
- OIH.CA: score=30.94 buy_ready=True sector_rank=7 price=1.48 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=152634752.0 spike=2.27
- OLFI.CA: score=22.64 buy_ready=True sector_rank=19 price=22.91 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=20031020.0 spike=0.64
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=712.21 support=711.0 resistance=719.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=102118704.0 spike=1.0
- ORHD.CA: score=23.4 buy_ready=False sector_rank=3 price=38.8 support=37.0 resistance=40.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=43506020.0 spike=0.29
- ORWE.CA: score=24.4 buy_ready=True sector_rank=5 price=23.24 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=67.47 liquidity=14976746.0 spike=0.74
- PHAR.CA: score=26.25 buy_ready=False sector_rank=13 price=91.03 support=83.6 resistance=92.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=72.01 liquidity=22388584.0 spike=0.73
- PHDC.CA: score=20.4 buy_ready=False sector_rank=3 price=14.71 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=51.31 liquidity=75117528.0 spike=0.28
- PHTV.CA: score=14.14 buy_ready=False sector_rank=11 price=310.61 support=216.31 resistance=317.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=81.98 liquidity=742748.0 spike=0.06
- POUL.CA: score=14.76 buy_ready=True sector_rank=19 price=38.97 support=35.28 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=2117107.25 spike=0.05
- PRCL.CA: score=9.4 buy_ready=False sector_rank=8 price=35.89 support=35.75 resistance=37.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31292460.0 spike=0.6
- PRDC.CA: score=24.5 buy_ready=False sector_rank=3 price=9.76 support=6.67 resistance=10.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=81.07 liquidity=128361264.0 spike=1.05
- PRMH.CA: score=14.73 buy_ready=False sector_rank=11 price=2.73 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=77.05 liquidity=3328316.75 spike=0.15
- RACC.CA: score=23.44 buy_ready=True sector_rank=11 price=10.11 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=62.22 liquidity=7035068.0 spike=0.37
- RAKT.CA: score=11.14 buy_ready=False sector_rank=11 price=22.16 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=46.82 liquidity=357950.48 spike=1.19
- RAYA.CA: score=24.4 buy_ready=True sector_rank=12 price=7.8 support=6.99 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=71660736.0 spike=0.56
- RMDA.CA: score=15.1 buy_ready=False sector_rank=13 price=4.97 support=4.81 resistance=5.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=61.22 liquidity=5854840.0 spike=0.33
- ROTO.CA: score=17.24 buy_ready=False sector_rank=11 price=41.22 support=38.0 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=57.2 liquidity=4840344.0 spike=0.14
- RREI.CA: score=18.12 buy_ready=False sector_rank=11 price=3.83 support=3.34 resistance=4.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=6723722.5 spike=0.24
- RTVC.CA: score=29.02 buy_ready=False sector_rank=11 price=4.11 support=3.55 resistance=3.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=73.77 liquidity=13080747.0 spike=3.31
- RUBX.CA: score=23.75 buy_ready=True sector_rank=11 price=13.62 support=9.96 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=65.89 liquidity=9349827.0 spike=0.13
- SAUD.CA: score=12.7 buy_ready=False sector_rank=16 price=21.69 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=71.51 liquidity=2168774.25 spike=0.4
- SCEM.CA: score=14.4 buy_ready=False sector_rank=8 price=78.39 support=71.25 resistance=81.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=227673648.0 spike=7.65
- SCFM.CA: score=28.4 buy_ready=False sector_rank=11 price=316.36 support=226.5 resistance=308.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=88.04 liquidity=83147752.0 spike=7.13
- SCTS.CA: score=9.96 buy_ready=False sector_rank=17 price=640.41 support=602.01 resistance=648.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10552396.0 spike=2.01
- SDTI.CA: score=15.19 buy_ready=False sector_rank=11 price=47.44 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=787467.31 spike=0.15
- SEIG.CA: score=16.73 buy_ready=False sector_rank=11 price=241.02 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=74.45 liquidity=2329534.25 spike=0.1
- SIPC.CA: score=23.4 buy_ready=False sector_rank=11 price=3.83 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=75.28 liquidity=11870690.0 spike=0.92
- SKPC.CA: score=19.87 buy_ready=False sector_rank=15 price=16.03 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=53.86 liquidity=17728982.0 spike=0.51
- SMFR.CA: score=21.28 buy_ready=False sector_rank=11 price=237.75 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=79.3 liquidity=9875449.0 spike=0.56
- SNFC.CA: score=13.19 buy_ready=False sector_rank=11 price=11.34 support=11.26 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=3789518.75 spike=0.34
- SPIN.CA: score=26.68 buy_ready=True sector_rank=5 price=14.89 support=13.8 resistance=14.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=68.18 liquidity=25996158.0 spike=2.14
- SPMD.CA: score=21.4 buy_ready=False sector_rank=11 price=0.46 support=0.41 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=11165782.0 spike=0.5
- SUGR.CA: score=11.47 buy_ready=False sector_rank=19 price=47.03 support=45.31 resistance=48.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=59.55 liquidity=2830102.25 spike=0.54
- SVCE.CA: score=24.62 buy_ready=True sector_rank=11 price=9.42 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=71233792.0 spike=1.11
- SWDY.CA: score=26.4 buy_ready=False sector_rank=1 price=92.29 support=84.3 resistance=93.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=76.82 liquidity=10250485.0 spike=0.62
- TALM.CA: score=12.34 buy_ready=False sector_rank=17 price=15.7 support=15.27 resistance=16.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=2403485.0 spike=0.18
- TMGH.CA: score=25.4 buy_ready=True sector_rank=3 price=101.19 support=92.1 resistance=103.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=68.19 liquidity=130294216.0 spike=0.34
- TRTO.CA: score=10.4 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=393.99 spike=0.98
- UEFM.CA: score=27.6 buy_ready=False sector_rank=11 price=553.76 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=77.82 liquidity=10975229.0 spike=3.1
- UEGC.CA: score=23.78 buy_ready=False sector_rank=11 price=2.44 support=1.33 resistance=2.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=96.26 liquidity=45432840.0 spike=1.19
- UNIP.CA: score=14.4 buy_ready=False sector_rank=11 price=0.4 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68414912.0 spike=3.87
- UNIT.CA: score=19.17 buy_ready=False sector_rank=3 price=19.23 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=78.53 liquidity=6766804.5 spike=0.25
- WCDF.CA: score=25.9 buy_ready=False sector_rank=11 price=600.45 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=83.77 liquidity=7503235.5 spike=6.31
- WKOL.CA: score=13.8 buy_ready=False sector_rank=11 price=328.61 support=321.02 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23166336.0 spike=3.2
- ZEOT.CA: score=17.31 buy_ready=False sector_rank=11 price=11.58 support=10.4 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=71.74 liquidity=4909365.5 spike=0.1
- ZMID.CA: score=24.4 buy_ready=False sector_rank=3 price=7.67 support=6.19 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=78.14 liquidity=160613600.0 spike=0.68

## Backtesting Lite
- OIH.CA: 180d return=30.28%, max drawdown=-14.56%, MA20>MA50 days last20=0, as_of=2026-07-18T21:00:00+00:00
- FERC.CA: 180d return=-1.88%, max drawdown=-23.88%, MA20>MA50 days last20=0, as_of=2026-07-18T21:00:00+00:00
- ELEC.CA: 180d return=-19.57%, max drawdown=-35.96%, MA20>MA50 days last20=0, as_of=2026-07-18T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- FERC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Ferchem Misr Fertilizers and Chemicals summary=Recent evidence for Ferchem Misr Fertilizers and Chemicals (FERC.CA) confirms its operations in Egypt's fertilizer industry, its listing on the Egyptian Exchange (EGX), and its global export network.
  - Ferchem Misr - Egypt's Leading Fertilizer producer (Official Website): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjFV3IgfEmFmtpW0qtdPoY9FG7DoFzH65JwU9Jb1tjYtL-FyrGzvnyOpS95710ZpOnPPOu5PuvNe93VvRNst-pmKNhVlvdrr_7omXmOnB9K0AfL7w=
  - About Us - Ferchem Fertilizers (Official Website): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL2x30SUoddu6mLo1webZ0AbupErccHcH3dcQPHmh9dXQdxq-JHBoO8FUV1unOVdpy7a3dmrXM2mJD_AK1SFCkRWaWkahnjahQDNdbr0edMNmQkIe6WoGVY9ga37o=
  - Ferchem Misr for Fertilizers and Chemicals (FERC) - Mubasher Info: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPbXbvYSLIn9_74xSJOccDLIxKY8Qao1dARk9dh5pZ0lHqz2Eeqls0BkzNCxtRmjQfCdRzmTOY719TJkinOrQOxaHfwlN4n9R2O21A2ubflN4sJ2tHtD7AVS0sfHLnvY6CkBIBC8RO0iocGfXmnVio
- ELEC.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=200 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt (ELEC.CA) has recent financial disclosures and company information confirming its status as a leading cable manufacturer in Egypt, with operations and exports across Africa, Europe, and the Arab world.
  - Electro Cable Egypt (EGX:ELEC) Financials & Income Statement (December 31, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfID1ARPVrkxN6Mes2yRZS9vtBIO06LKyz7ZOVR4gB1gzFeRiYMFIeglRc_K1kh08MnlWKW8IWtNgXMkSuAGCW2Nlfm0G7_A_T8ziQF3HzfdXPmmtpdP59cM251S1hwJ4i2D7btA-K5fOAjJR7sg==
  - Electro Cable Egypt (EGX:ELEC) Stock Price & Overview (2025 Financial Performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5ZFUn9B5NG4iWpF2RU1xEzVo-EbAo3rr-8Om5L4XPE6NEsHTCGuOIbwDl6GMhi9iW9F4gPNMh0L8Uflv4NpuporZwxiz8IXHDs9zJEjJk8vkBNNDl_1tZmqrBJrb-FU_6S3M=
  - Electro Cable Egypt S.A.E Company Profile (Q1 2026 Financial Highlights): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDqD1XEiVs-eUGFuAaskoZP2N4iAe3pPY-kA1CAv5MH6ik6g6kCE4d4xzotULwIb0_uLxp8WMrpHAzeoYj501UBAA6kz4wTLgjpmKd9f9eI_z3BABTRDka2ScTJWAKzMetgs5LvDZfbP5oHaLSD9I4bjJkQTtuddORWdVCDg26NW-YXPjbEP7W_XSm-Bq6V-KYICvTqFpcUmQDcG5sgzcmEiIlft_vbYHiXxsPiwEoUp4u42jnUOn7otC_HHaZYmKPnrT2Ozid6oU2ciQzv0dcZatM0LosI7qGjaBnIA68HSq9vCNxQE2COH-754wB0PxsBVZG4Jm6Uc158FOpfptM7U8pc9Fmo3dS2IRszX2RppCD1e5GUt8HFRZ7aszxEoEOy-_cXT_TtiUolPEzZEOpZ3BJV-Yl4WUDeQQtpPJ0A2sY4a8d1DCluWSvwtBpFZPH-5XBUeNLIWicBFfXLOy_-4trkMCj__A8b4LxvwJrXr0ObcsavCS_Fl3nA_aactuO-P3gZ4VO35T3d7eBN7b9Ru8XtYlPBsIXNiQ5hI8F0TrbkZDb-PJD-2pracpADaS01BZnEQFdfPfxhJCX9baP8oXpTSLSwHNS8fvUMDb6JoDhcnDAEpxKUMR7ocaBLA==
- ARCC.CA: status=RECENT_ACCEPTED latest=2026-08-13 age_days=0 sources=3 expected=Arabian Cement Company summary=Arabian Cement Company (ARCC.CA) has recent financial reports and news, confirming its position as a major cement producer in Egypt and its listing on the EGX. The company has also been recognized among Egypt's most valuable companies in 2026.
  - Financial Information - Arabian Cement Company (FY 2024, Q1-Q3 2024 Financials): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQifE1MZx1f0vN3WyoLYu9f42n3vY04QG8bskzz2g1l8rq2vfj5t20sE9I58Isrnpqy7rxGckbRP8Uk7QevN30ZyfEoW5UuUjnYCPfNmqKxZed1i4fEVNgrxALadpqyBgGeY5BPA-M7CUWTpulQscFQhEfmhWOXzebGB6qxcIWjAv1k0c=
  - Arabian Cement Company S.A.E. (EGX:ARCC) Stock Price & Overview (2025 Financial Performance, Aug 13, 2026 Earnings Date): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEr7XY9B9V0qtgoMcNNI4GzGCbPjLaUCahwKQy9e5PyepsqKRiXeur_y7U2Ot6EiJJYn-AUAd_RZ87IkFHvcYaIxKcSDC4uNFAsrKeLZh3ggmUMBqStAikSIh7Prqi8MKZ8ww=
  - Arabian Cement Company (News: April 1, 2026, January 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdRz0ilzNpqCjh68Pnuxjcggl3aaW_7LkLqwY_QpMmE75Lc6xsw0mUYaYQld3ZtSDG-ffPUgL1rLCtkXk2WwzKxM7iyWgnMLtAiYXGftSWrgrfMAkP3TflYroM
- MCQE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=565 sources=3 expected=Misr Cement Qena summary=Misr Cement to distribute EGP 10/shr dividends for 2025; Misr Cement stock is testing technical level ahead of historical peak – Analysis; Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Misr Cement to distribute EGP 10/shr dividends for 2025: https://english.mubasher.info/news/4586191/Misr-Cement-to-distribute-EGP-10-shr-dividends-for-2025/
  - Misr Cement stock is testing technical level ahead of historical peak – Analysis: https://english.mubasher.info/news/4560306/Misr-Cement-stock-is-testing-technical-level-ahead-of-historical-peak-Analysis/
  - Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits: https://english.mubasher.info/news/4524754/Misr-Cement-witnesses-3-254-remarkable-jump-in-9M-25-consolidated-net-profits/
- RTVC.CA: status=RECENT_ACCEPTED latest=2026-07-16 age_days=4 sources=3 expected=Remco Tourism Villages Construction summary=Remco Tourism Villages Construction (RTVC.CA) has recent financial reports and company information confirming its operations in real estate and tourism development in Egypt, and its listing on the Egyptian Stock Exchange.
  - Remco Tourism Villages Construction (EGX:RTVC) Revenue (December 31, 2024): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8U1zNmEPV3TYIQPISuc7WhxlUO-a6uERUDj85KRVivTMXU1Lmf1QKzUglNja50URcJ17gh1fvp0--aJfUHrUX3931F4eLZj0_gSFRttL_fcysKupD5g1sASezyBo1ZvCkd51zMgN0e0dR2g==
  - Remco Tourism Villages Construction Stock (RTVC) - Quote Egyptian Exchange (May 8, 2025 Earnings Report, July 16, 2026 Price Change): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEw1APQr1lbGrB9J0AIQCGEJGsaCN7AuK_y_3lpazED7JymDyV2iMkcVrzC3qKcpS0d_WtjHSDNZ82autYeNDCSRjXYE8wLGDuiW1HAONr1NBBhvrhB6N6YxL5wHwQ7h_dpn4gs9_LpJqRuig51IiotQbIa8gVbnXQAE1LxcEJtUo4-E0BoFcA=
  - REMCO WEBSITE - Identity (Company Overview): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpvjV1obEPEuIsc_Y5iYdbesXARZ867oOTbSlNah_l9LJ3my3_kBAtuXjo6DEzvCIXGUj_fNLgI6tVfDqsdGDjBWusYluXk2BhX-P_LU4MSjZkBjg6PDo1hgPLVQ==
- ETEL.CA: status=RECENT_ACCEPTED latest=2026-07-18 age_days=2 sources=3 expected=Telecom Egypt summary=Telecom Egypt (ETEL.CA) has very recent financial reports and statistics, highlighting its revenue and profit performance, and its active presence on the Egyptian Exchange.
  - Telecom Egypt Company (EGX:ETEL) Statistics & Valuation Metrics - Stock Analysis (Last 12 months revenue and profits, July 18, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFewGReTDVbKgFczZz5kLGQOoCLz2OOeQ3VyXqJxEm2fw6Q--JSV-QAvaCX_pbVTgWa9akhbVHI_eEk475QvlG7v7fYWKj0b3-qhCuxPcQek2ttrnQ7fEqsvSu6YhyKfFevc70g5wfBQKF1yUjfrw==
  - Telecom Egypt Company (EGX:ETEL) Financials & Income Statement - Stock Analysis (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXkqANrRNhrxrd8-jJ1k0CC6ELqeCHr5julPHNwZoCbEqN1WtmUvVhCAf4_Gl4zJkJUpcRno5tTatxg7dGbRolZbLG0xUBgtClFPcA4cmE_unBPAe9Y0nLNVeOjCkIApWLDHkhmhLjLWAqbBnksg==
  - Telecom Egypt - EGX:ETEL Financials - Investing.com (May 19, 2026 Latest Release): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaNvjdwJQCSuM0DKjAzzDK8QL-wTijHy1wX3WkBAjc6EP_8t8hhBjCVSC-R1Osud40A68t50qI9Tdm8m_pL7iPTsHBOA9g4RNolSYNaDVy7lB4f3A1vopDPSmIGup_gGJt5N-JDyVrdgoqUp4sEZaDXXSTqr1ULzvjbPG2
- EDFM.CA: status=RECENT_ACCEPTED latest=2026-05-11 age_days=70 sources=3 expected=East Delta Flour Mills summary=East Delta Flour Mills (EDFM.CA) has recent financial reports and company information detailing its operations in the manufacturing and distribution of grains and related products in Egypt, and its listing on the Egyptian Exchange.
  - East Delta Flour Mills (EGX:EDFM) Stock Price & Overview (Fiscal Year 2025 Financial Performance): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy0oOuK6VbetG3NCJO3eqF6Ti2dObiFgIfkQvQIVj2Hzv5OWNuT6T5Tw8wq4UyxkqDpRSl0ODZNnft0hoI_wRiulD0OBQu6dw-H4AJcbtsATxV5s1cmfq6gQ1cdz6qpO-dIGE=
  - East Delta Flour Mills - EGX:EDFM Financials - Investing.com (May 11, 2026 Latest Release): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQvVtFYsEE1tywRLsm0b1ECLRotw6DifT1etQRsKpWoBCqWB5goVxFp7z4xe_sZyEy2nhcxipc2eOwPi9Ry9iLoIrVX6mtkvipWvw14_oUqtJTtWpR1-_Y4zu0IZ8KWObKm3ikJ-tfeTcTtddkBsQqfuSJK6e9pq6AgGNL_g==
  - East Delta Flour Mills (EGX:EDFM) Balance Sheet - Stock Analysis (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmUd7rLs492DeHHF5YTbfDMdDMccBPBAG231sUihi9Pvt-cpYh50ZZ_eypPYotWaHL8GUBQq2l8MP9sT67q9ZVtS3yLYk471lwJjz0LxgUqXpDMDHXqfq-VqAyFTM0L8hXIMRG1DHcZyrh26vOdYlkpzPirjP52uWr9a6W

## Warnings
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for FERC.CA matches the company but no source/report date was detected.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
