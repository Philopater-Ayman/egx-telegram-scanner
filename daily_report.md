# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-21T10:27:39.548811+00:00
Generated Cairo: 2026-07-21 13:27
Run timing: target 11:00 Cairo | generated Cairo 2026-07-21 13:27 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-21 13:20

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 48
- Data quality issues: 1
- Tradeable price/liquidity tickers: 171/189
- Top sector: Building Materials

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, July 21
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 85.0% / above MA50 60.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 76.92% / above MA50 76.92%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- COMI.CA: liquidity=833330816.0 spike=2.23 score=26.86
- ADIB.CA: liquidity=373399744.0 spike=3.93 score=29.4
- CCAP.CA: liquidity=333460160.0 spike=0.54 score=21.4
- TMGH.CA: liquidity=217770928.0 spike=0.56 score=23.4
- EAST.CA: liquidity=210178288.0 spike=4.25 score=24.2

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 is bullish and EGX70 constructive with sector breadth around 52%; risk mode is set to selective swing trades only. The scanner prioritized tickets like ARCC.CA, ADIB.CA and GRCA.CA based on high rank scores, liquidity spikes and sector alignment, but RSI readings are overheated and evidence is limited, so confidence remains low and outlook is watchful for the next 1‑3 days.
- ARCC.CA leads with a liquidity spike of 1.95× and top Building Materials sector rank, yet it sits close to its 20‑day resistance and shows extended RSI.
- ADIB.CA exhibits a strong liquidity spike of 3.93× and solid fundamentals, but the Banking sector is not among the leaders, keeping confidence low.
- GRCA.CA, MEPA.CA and INFI.CA all show RSI above 79 and large support distances, indicating overheated moves despite notable liquidity spikes.
- Market regime: EGX30 bullish (85% above MA20) and EGX70 constructive (77% above MA20) supports only selective swing trades, adding uncertainty to short‑term expectations.

## Top Liquidity Spikes
- EGBE.CA: spike=31.63 liquidity=98389.01 outlook=WEAK_OR_RISKY score=28.87 buy_ready=False
- DAPH.CA: spike=12.33 liquidity=126087616.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AFMC.CA: spike=11.7 liquidity=123612392.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- IDRE.CA: spike=9.54 liquidity=128068224.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- FERC.CA: spike=5.19 liquidity=43379644.0 outlook=BULLISH_WATCH score=71.47 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=12.6 5d=5.83% 20d=15.9% aboveMA50=83.33%
- #2 Telecommunications: score=11.06 5d=2.19% 20d=5.49% aboveMA50=100.0%
- #3 Industrial Goods & Cables: score=9.61 5d=3.38% 20d=4.58% aboveMA50=100.0%
- #4 Textiles: score=8.78 5d=1.97% 20d=4.19% aboveMA50=100.0%
- #5 Fintech & Payments: score=8.74 5d=-0.96% 20d=3.26% aboveMA50=100.0%
- #6 Healthcare: score=8.46 5d=5.96% 20d=4.61% aboveMA50=66.67%
- #7 Transportation & Logistics: score=8.38 5d=1.95% 20d=5.76% aboveMA50=100.0%
- #8 Education: score=8.19 5d=-0.13% 20d=4.67% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ARCC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; close to resistance
- ADIB.CA: BULLISH_WATCH score=89.87 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ETEL.CA: BULLISH_WATCH score=87 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- CLHO.CA: BULLISH_WATCH score=84.46 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- ARVA.CA: BULLISH_WATCH score=82.51 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- COMI.CA: BULLISH_WATCH score=81.87 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EFIH.CA: BULLISH_WATCH score=81.74 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- ELEC.CA: BULLISH_WATCH score=81.61 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- ADCI.CA: BULLISH_WATCH score=78.51 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance; sector is not leading
- TALM.CA: BULLISH_WATCH score=78.19 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- ARCC.CA: rank=31.3 outlook=BULLISH_WATCH outlook_score=100 sector_rank=1 price=57.45 support=53.0 resistance=57.88 liquidity=44798180.0
- ADIB.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=89.87 sector_rank=9 price=49.05 support=44.1 resistance=48.49 liquidity=373399744.0
- EFIH.CA: rank=26.92 outlook=BULLISH_WATCH outlook_score=81.74 sector_rank=5 price=22.95 support=20.0 resistance=23.65 liquidity=92886584.0
- COMI.CA: rank=26.86 outlook=BULLISH_WATCH outlook_score=81.87 sector_rank=9 price=139.59 support=126.21 resistance=137.98 liquidity=833330816.0
- HRHO.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=65.16 sector_rank=15 price=27.11 support=26.09 resistance=27.55 liquidity=70141560.0
- CLHO.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=84.46 sector_rank=6 price=16.85 support=15.7 resistance=17.9 liquidity=36566696.0
- TALM.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=78.19 sector_rank=8 price=15.9 support=15.27 resistance=16.34 liquidity=11330647.0
- BTFH.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=71.16 sector_rank=15 price=3.1 support=2.91 resistance=3.2 liquidity=85320432.0
- ADCI.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=78.51 sector_rank=13 price=257.38 support=230.0 resistance=258.0 liquidity=12093506.0
- OBRI.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=63.51 sector_rank=13 price=35.87 support=31.5 resistance=39.27 liquidity=11355731.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=26.4 buy_ready=False sector_rank=13 price=242.96 support=196.0 resistance=253.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=73.91 liquidity=10526503.0 spike=0.61
- ABUK.CA: score=20.39 buy_ready=False sector_rank=16 price=72.1 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=68.1 liquidity=56624404.0 spike=0.35
- ACAMD.CA: score=24.4 buy_ready=False sector_rank=13 price=2.4 support=2.14 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=74.29 liquidity=45615476.0 spike=0.59
- ACGC.CA: score=24.4 buy_ready=True sector_rank=4 price=9.92 support=8.92 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=66.84 liquidity=10142380.0 spike=0.49
- ADCI.CA: score=26.4 buy_ready=True sector_rank=13 price=257.38 support=230.0 resistance=258.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=60.7 liquidity=12093506.0 spike=1.0
- ADIB.CA: score=29.4 buy_ready=True sector_rank=9 price=49.05 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=57.06 liquidity=373399744.0 spike=3.93
- ADPC.CA: score=21.4 buy_ready=False sector_rank=13 price=3.88 support=3.32 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=83.08 liquidity=20483196.0 spike=0.83
- AFDI.CA: score=27.34 buy_ready=False sector_rank=13 price=47.91 support=41.84 resistance=48.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=74.69 liquidity=20788896.0 spike=1.47
- AFMC.CA: score=14.4 buy_ready=False sector_rank=13 price=99.37 support=97.0 resistance=127.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=123612392.0 spike=11.7
- AJWA.CA: score=17.93 buy_ready=False sector_rank=13 price=168.0 support=169.0 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=41.52 liquidity=5532804.5 spike=0.49
- ALCN.CA: score=20.28 buy_ready=False sector_rank=7 price=29.71 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=74.12 liquidity=5876578.0 spike=0.28
- ALUM.CA: score=15.31 buy_ready=False sector_rank=13 price=23.64 support=20.55 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=81.32 liquidity=1909173.63 spike=0.29
- AMER.CA: score=9.64 buy_ready=False sector_rank=14 price=4.22 support=4.06 resistance=4.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=109043040.0 spike=1.12
- AMES.CA: score=9.4 buy_ready=False sector_rank=13 price=107.23 support=106.59 resistance=116.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26228910.0 spike=0.29
- AMIA.CA: score=20.87 buy_ready=False sector_rank=13 price=10.5 support=8.4 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=82.96 liquidity=7467914.5 spike=0.66
- AMOC.CA: score=24.4 buy_ready=False sector_rank=12 price=8.17 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=70.88 liquidity=32749012.0 spike=0.56
- APSW.CA: score=19.41 buy_ready=False sector_rank=13 price=8.98 support=8.0 resistance=9.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=87.8 liquidity=3029262.0 spike=2.49
- ARAB.CA: score=24.4 buy_ready=True sector_rank=14 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=58603740.0 spike=0.51
- ARCC.CA: score=31.3 buy_ready=True sector_rank=1 price=57.45 support=53.0 resistance=57.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=67.63 liquidity=44798180.0 spike=1.95
- AREH.CA: score=19.4 buy_ready=False sector_rank=13 price=1.47 support=1.48 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=47.92 liquidity=17892072.0 spike=0.47
- ARVA.CA: score=24.82 buy_ready=True sector_rank=13 price=11.0 support=10.5 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=55.87 liquidity=20182186.0 spike=1.21
- ASCM.CA: score=24.4 buy_ready=True sector_rank=13 price=62.18 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=60.16 liquidity=44236572.0 spike=0.63
- ASPI.CA: score=23.4 buy_ready=False sector_rank=13 price=0.37 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=79.61 liquidity=18323142.0 spike=0.73
- ATLC.CA: score=17.23 buy_ready=False sector_rank=15 price=5.21 support=4.92 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=4825763.0 spike=0.59
- ATQA.CA: score=24.89 buy_ready=True sector_rank=16 price=9.65 support=9.21 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=62.14 liquidity=9505105.0 spike=0.34
- AXPH.CA: score=17.14 buy_ready=False sector_rank=13 price=1239.93 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=74.16 liquidity=737376.25 spike=0.2
- BINV.CA: score=14.1 buy_ready=False sector_rank=10 price=47.33 support=48.04 resistance=48.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5698388.5 spike=1.0
- BIOC.CA: score=10.58 buy_ready=False sector_rank=13 price=109.99 support=106.61 resistance=125.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33677804.0 spike=1.59
- BTFH.CA: score=26.4 buy_ready=True sector_rank=15 price=3.1 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=62.0 liquidity=85320432.0 spike=0.39
- CAED.CA: score=21.4 buy_ready=False sector_rank=13 price=119.17 support=68.0 resistance=134.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=81.23 liquidity=44095732.0 spike=0.94
- CANA.CA: score=23.4 buy_ready=True sector_rank=9 price=37.02 support=34.7 resistance=37.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=60.04 liquidity=12700118.0 spike=0.94
- CCAP.CA: score=21.4 buy_ready=False sector_rank=10 price=5.46 support=4.65 resistance=5.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=78.63 liquidity=333460160.0 spike=0.54
- CCRS.CA: score=17.03 buy_ready=False sector_rank=13 price=2.63 support=2.18 resistance=2.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=81.08 liquidity=3628653.5 spike=0.24
- CEFM.CA: score=10.28 buy_ready=False sector_rank=13 price=125.09 support=124.27 resistance=139.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16490993.0 spike=1.44
- CERA.CA: score=22.17 buy_ready=False sector_rank=13 price=1.36 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=7772167.5 spike=0.31
- CFGH.CA: score=1.14 buy_ready=False sector_rank=13 price=0.11 support=0.11 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17290.57 spike=1.86
- CICH.CA: score=19.37 buy_ready=True sector_rank=15 price=12.2 support=11.52 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=2973001.75 spike=0.57
- CIEB.CA: score=23.76 buy_ready=True sector_rank=9 price=24.3 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=63.83 liquidity=8896359.0 spike=1.23
- CIRA.CA: score=25.08 buy_ready=False sector_rank=8 price=32.4 support=27.45 resistance=33.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=70.55 liquidity=50876452.0 spike=1.34
- CLHO.CA: score=26.4 buy_ready=True sector_rank=6 price=16.85 support=15.7 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=65.11 liquidity=36566696.0 spike=0.71
- CNFN.CA: score=18.43 buy_ready=True sector_rank=15 price=4.89 support=4.61 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=68.52 liquidity=4028701.5 spike=0.08
- COMI.CA: score=26.86 buy_ready=True sector_rank=9 price=139.59 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=68.5 liquidity=833330816.0 spike=2.23
- COPR.CA: score=23.4 buy_ready=False sector_rank=13 price=0.39 support=0.35 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=74.55 liquidity=20955996.0 spike=0.99
- COSG.CA: score=23.4 buy_ready=False sector_rank=13 price=1.68 support=1.47 resistance=1.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=84.62 liquidity=13715223.0 spike=0.38
- CPCI.CA: score=21.44 buy_ready=False sector_rank=13 price=474.95 support=367.7 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=74.9 liquidity=7038995.5 spike=0.64
- CSAG.CA: score=20.69 buy_ready=True sector_rank=7 price=33.55 support=30.87 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=65.6 liquidity=6291311.0 spike=0.32
- DAPH.CA: score=14.4 buy_ready=False sector_rank=13 price=91.95 support=87.21 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=126087616.0 spike=12.33
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=13 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.99 buy_ready=False sector_rank=17 price=26.72 support=26.06 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=46.79 liquidity=793340.31 spike=0.15
- DSCW.CA: score=23.4 buy_ready=False sector_rank=13 price=1.96 support=1.71 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=96.3 liquidity=39462136.0 spike=0.9
- DTPP.CA: score=21.4 buy_ready=False sector_rank=13 price=228.65 support=114.67 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=78.19 liquidity=15174165.0 spike=0.27
- EALR.CA: score=22.56 buy_ready=True sector_rank=13 price=369.99 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=68.74 liquidity=8159205.0 spike=0.52
- EASB.CA: score=9.66 buy_ready=False sector_rank=13 price=8.15 support=7.33 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19184240.0 spike=1.13
- EAST.CA: score=24.2 buy_ready=False sector_rank=17 price=37.44 support=36.11 resistance=39.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=48.91 liquidity=210178288.0 spike=4.25
- EBSC.CA: score=14.61 buy_ready=False sector_rank=13 price=1.89 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=59.72 liquidity=2205480.75 spike=0.32
- ECAP.CA: score=18.01 buy_ready=True sector_rank=13 price=33.73 support=31.52 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=68.1 liquidity=5611007.0 spike=0.65
- EDFM.CA: score=14.7 buy_ready=False sector_rank=13 price=397.35 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=79.75 liquidity=3304336.0 spike=0.9
- EEII.CA: score=21.85 buy_ready=False sector_rank=13 price=2.79 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=73.03 liquidity=7449240.5 spike=0.35
- EFIC.CA: score=13.11 buy_ready=False sector_rank=16 price=185.05 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=3725733.75 spike=0.37
- EFID.CA: score=20.2 buy_ready=False sector_rank=17 price=27.91 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=20268874.0 spike=0.5
- EFIH.CA: score=26.92 buy_ready=True sector_rank=5 price=22.95 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=66.39 liquidity=92886584.0 spike=2.26
- EGAL.CA: score=20.39 buy_ready=False sector_rank=16 price=303.03 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=73.35 liquidity=16490867.0 spike=0.35
- EGAS.CA: score=22.87 buy_ready=False sector_rank=12 price=52.43 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=8466325.0 spike=0.74
- EGBE.CA: score=18.5 buy_ready=False sector_rank=9 price=0.49 support=-0.34 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=96.84 liquidity=98389.01 spike=31.63
- EGCH.CA: score=20.39 buy_ready=False sector_rank=16 price=13.15 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=72.04 liquidity=31436708.0 spike=0.62
- EGSA.CA: score=17.71 buy_ready=False sector_rank=2 price=8.98 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=80.7 liquidity=30107.0 spike=2.14
- EGTS.CA: score=19.4 buy_ready=False sector_rank=14 price=17.9 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=19917882.0 spike=0.4
- EHDR.CA: score=21.4 buy_ready=False sector_rank=13 price=2.87 support=2.37 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=76.14 liquidity=14804313.0 spike=0.41
- EKHO.CA: score=8.4 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=24.4 buy_ready=True sector_rank=3 price=2.24 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=69.05 liquidity=52323400.0 spike=0.88
- ELKA.CA: score=21.4 buy_ready=False sector_rank=13 price=2.09 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=86.55 liquidity=42035600.0 spike=0.64
- ELNA.CA: score=14.81 buy_ready=False sector_rank=13 price=38.64 support=35.55 resistance=40.5 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=64.05 liquidity=1050389.74 spike=1.68
- ELSH.CA: score=22.4 buy_ready=False sector_rank=13 price=14.25 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=72.31 liquidity=29503088.0 spike=0.25
- ELWA.CA: score=10.57 buy_ready=False sector_rank=13 price=1.95 support=1.87 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=48.57 liquidity=1174307.63 spike=0.91
- EMFD.CA: score=24.4 buy_ready=True sector_rank=14 price=11.75 support=11.24 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=11691613.0 spike=0.16
- ENGC.CA: score=17.52 buy_ready=False sector_rank=13 price=42.89 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=78.52 liquidity=4121737.0 spike=0.17
- EOSB.CA: score=14.57 buy_ready=False sector_rank=13 price=1.48 support=1.48 resistance=1.55 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=49079.76 spike=1.06
- EPCO.CA: score=22.62 buy_ready=False sector_rank=13 price=10.79 support=8.5 resistance=11.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=89.26 liquidity=9222670.0 spike=0.42
- EPPK.CA: score=17.05 buy_ready=False sector_rank=13 price=14.47 support=12.31 resistance=15.44 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=63.09 liquidity=646707.72 spike=0.58
- ETEL.CA: score=27.36 buy_ready=False sector_rank=2 price=104.17 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=79.25 liquidity=123536976.0 spike=1.98
- ETRS.CA: score=22.57 buy_ready=True sector_rank=13 price=10.8 support=10.12 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=60.34 liquidity=8172857.5 spike=0.13
- EXPA.CA: score=25.48 buy_ready=False sector_rank=9 price=20.1 support=18.03 resistance=19.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=83.13 liquidity=53245452.0 spike=2.04
- FAIT.CA: score=16.26 buy_ready=True sector_rank=9 price=37.57 support=35.06 resistance=37.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=67.98 liquidity=1856922.13 spike=0.69
- FAITA.CA: score=12.18 buy_ready=False sector_rank=9 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=83681.4 spike=2.35
- FERC.CA: score=27.39 buy_ready=False sector_rank=16 price=80.61 support=72.75 resistance=83.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=84.94 liquidity=43379644.0 spike=5.19
- FWRY.CA: score=24.48 buy_ready=True sector_rank=5 price=19.51 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=65.95 liquidity=137001088.0 spike=1.04
- GBCO.CA: score=24.4 buy_ready=True sector_rank=11 price=31.71 support=29.01 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=37193940.0 spike=0.49
- GDWA.CA: score=27.4 buy_ready=False sector_rank=13 price=0.88 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=82.28 liquidity=207279264.0 spike=4.39
- GGCC.CA: score=9.76 buy_ready=False sector_rank=13 price=0.83 support=0.8 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34693376.0 spike=1.18
- GIHD.CA: score=14.4 buy_ready=False sector_rank=13 price=59.98 support=51.68 resistance=61.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=148095456.0 spike=4.23
- GMCI.CA: score=14.76 buy_ready=False sector_rank=13 price=2.07 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=359012.38 spike=0.28
- GRCA.CA: score=28.4 buy_ready=False sector_rank=13 price=64.53 support=48.0 resistance=68.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=79.62 liquidity=35365124.0 spike=3.75
- GSSC.CA: score=14.33 buy_ready=False sector_rank=13 price=272.97 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=85.8 liquidity=2934939.25 spike=0.3
- GTWL.CA: score=9.94 buy_ready=False sector_rank=13 price=111.02 support=108.5 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=164314272.0 spike=1.27
- HDBK.CA: score=20.4 buy_ready=False sector_rank=9 price=81.5 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=51.26 liquidity=35483176.0 spike=0.9
- HELI.CA: score=23.4 buy_ready=False sector_rank=14 price=8.3 support=6.36 resistance=8.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=91.87 liquidity=121962896.0 spike=0.71
- HRHO.CA: score=26.4 buy_ready=True sector_rank=15 price=27.11 support=26.09 resistance=27.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=55.64 liquidity=70141560.0 spike=0.65
- ICID.CA: score=17.17 buy_ready=True sector_rank=13 price=8.11 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=59.1 liquidity=2766148.25 spike=0.33
- IDRE.CA: score=14.4 buy_ready=False sector_rank=13 price=49.24 support=45.28 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=128068224.0 spike=9.54
- IFAP.CA: score=14.44 buy_ready=False sector_rank=19 price=19.09 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=6948662.5 spike=1.25
- INFI.CA: score=28.08 buy_ready=False sector_rank=13 price=107.41 support=88.51 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=80.31 liquidity=41108048.0 spike=3.34
- IRON.CA: score=10.41 buy_ready=False sector_rank=16 price=31.3 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=35.03 liquidity=3022802.0 spike=0.42
- ISMA.CA: score=22.4 buy_ready=False sector_rank=13 price=28.23 support=26.54 resistance=30.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=15490652.0 spike=0.91
- ISMQ.CA: score=21.39 buy_ready=False sector_rank=16 price=9.2 support=8.1 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=50.61 liquidity=15850832.0 spike=0.12
- ISPH.CA: score=19.4 buy_ready=False sector_rank=6 price=11.6 support=11.2 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=47542940.0 spike=0.89
- JUFO.CA: score=19.9 buy_ready=False sector_rank=17 price=28.71 support=28.5 resistance=31.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=39117240.0 spike=1.85
- KABO.CA: score=24.24 buy_ready=False sector_rank=4 price=8.4 support=6.04 resistance=8.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=95.35 liquidity=56413892.0 spike=1.42
- KWIN.CA: score=27.06 buy_ready=False sector_rank=13 price=98.25 support=65.0 resistance=95.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=91.8 liquidity=95957928.0 spike=2.83
- KZPC.CA: score=16.4 buy_ready=True sector_rank=13 price=8.62 support=8.56 resistance=8.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2001992.25 spike=1.0
- LCSW.CA: score=26.4 buy_ready=False sector_rank=1 price=33.92 support=27.01 resistance=35.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=89.62 liquidity=55150796.0 spike=0.75
- LUTS.CA: score=24.4 buy_ready=True sector_rank=13 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=11798350.0 spike=0.29
- MAAL.CA: score=16.93 buy_ready=False sector_rank=13 price=8.7 support=6.57 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=91.79 liquidity=3528739.25 spike=0.19
- MASR.CA: score=21.4 buy_ready=False sector_rank=13 price=8.28 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=84.43 liquidity=33985340.0 spike=0.4
- MBSC.CA: score=24.42 buy_ready=False sector_rank=1 price=246.4 support=222.66 resistance=251.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=68.55 liquidity=18370356.0 spike=1.01
- MCQE.CA: score=26.6 buy_ready=False sector_rank=1 price=190.88 support=166.66 resistance=191.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=80.37 liquidity=18326348.0 spike=1.1
- MCRO.CA: score=26.32 buy_ready=False sector_rank=13 price=1.39 support=1.17 resistance=1.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=78.79 liquidity=190161552.0 spike=2.96
- MENA.CA: score=17.86 buy_ready=True sector_rank=14 price=7.14 support=6.59 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=57.67 liquidity=3459981.0 spike=0.47
- MEPA.CA: score=28.4 buy_ready=False sector_rank=13 price=1.85 support=1.52 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=85.29 liquidity=82268288.0 spike=4.59
- MFPC.CA: score=20.39 buy_ready=False sector_rank=16 price=37.64 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=69.54 liquidity=21898450.0 spike=0.23
- MFSC.CA: score=12.15 buy_ready=False sector_rank=13 price=46.69 support=45.05 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=43.36 liquidity=2746808.5 spike=0.34
- MHOT.CA: score=11.54 buy_ready=False sector_rank=21 price=16.53 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=37.28 liquidity=5140601.0 spike=0.34
- MICH.CA: score=19.87 buy_ready=True sector_rank=13 price=38.07 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=68.94 liquidity=7466286.0 spike=0.57
- MILS.CA: score=10.52 buy_ready=False sector_rank=13 price=171.24 support=170.0 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44502012.0 spike=1.56
- MIPH.CA: score=11.72 buy_ready=False sector_rank=6 price=756.85 support=630.13 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=85.68 liquidity=315667.97 spike=0.09
- MOED.CA: score=19.0 buy_ready=False sector_rank=13 price=0.71 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=73.1 liquidity=8601913.0 spike=0.69
- MOIL.CA: score=18.9 buy_ready=False sector_rank=12 price=0.59 support=0.46 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=85.92 liquidity=1277772.62 spike=3.11
- MOIN.CA: score=8.83 buy_ready=False sector_rank=13 price=23.75 support=22.6 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=65.07 liquidity=432667.31 spike=0.55
- MOSC.CA: score=18.14 buy_ready=True sector_rank=13 price=286.67 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=1740347.88 spike=0.15
- MPCI.CA: score=23.4 buy_ready=False sector_rank=13 price=267.19 support=222.55 resistance=284.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=79771600.0 spike=0.73
- MPCO.CA: score=22.99 buy_ready=True sector_rank=19 price=1.86 support=1.7 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=13494180.0 spike=0.23
- MPRC.CA: score=23.4 buy_ready=False sector_rank=13 price=44.87 support=33.7 resistance=44.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=81.85 liquidity=10620761.0 spike=0.21
- MTIE.CA: score=23.12 buy_ready=True sector_rank=11 price=9.41 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=63.5 liquidity=6723188.0 spike=0.31
- NAHO.CA: score=5.23 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=49589.18 spike=1.89
- NCCW.CA: score=26.4 buy_ready=False sector_rank=13 price=6.68 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=74.42 liquidity=18714384.0 spike=0.77
- NEDA.CA: score=15.54 buy_ready=False sector_rank=13 price=2.86 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=738923.87 spike=1.2
- NHPS.CA: score=23.5 buy_ready=False sector_rank=13 price=89.03 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=83.2 liquidity=137174416.0 spike=2.05
- NINH.CA: score=21.4 buy_ready=False sector_rank=13 price=22.2 support=17.12 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=80.89 liquidity=24557262.0 spike=0.67
- NIPH.CA: score=23.44 buy_ready=False sector_rank=6 price=227.7 support=157.01 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=89.1 liquidity=135837040.0 spike=1.02
- OBRI.CA: score=26.4 buy_ready=True sector_rank=13 price=35.87 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=64.54 liquidity=11355731.0 spike=0.34
- OCDI.CA: score=24.4 buy_ready=False sector_rank=14 price=27.5 support=22.3 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=72.02 liquidity=35598648.0 spike=0.32
- OCPH.CA: score=11.94 buy_ready=False sector_rank=13 price=467.23 support=440.05 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48447028.0 spike=2.27
- ODIN.CA: score=18.94 buy_ready=False sector_rank=13 price=2.52 support=2.05 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=77.46 liquidity=7542797.5 spike=0.53
- OFH.CA: score=23.44 buy_ready=False sector_rank=13 price=0.71 support=0.57 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=91.02 liquidity=53596276.0 spike=1.02
- OIH.CA: score=23.4 buy_ready=False sector_rank=10 price=1.49 support=1.36 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=73028096.0 spike=0.97
- OLFI.CA: score=18.78 buy_ready=True sector_rank=17 price=22.75 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=7586018.5 spike=0.24
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=709.92 support=706.1 resistance=714.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48715352.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=14 price=39.18 support=37.0 resistance=40.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=84957536.0 spike=0.56
- ORWE.CA: score=24.4 buy_ready=True sector_rank=4 price=23.0 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=67.92 liquidity=19182998.0 spike=0.92
- PHAR.CA: score=23.4 buy_ready=False sector_rank=6 price=91.14 support=83.6 resistance=92.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=75.44 liquidity=18655148.0 spike=0.58
- PHDC.CA: score=19.4 buy_ready=False sector_rank=14 price=14.77 support=14.26 resistance=15.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=84580912.0 spike=0.35
- PHTV.CA: score=12.51 buy_ready=False sector_rank=13 price=315.67 support=232.0 resistance=317.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=78.73 liquidity=1111492.13 spike=0.1
- POUL.CA: score=17.06 buy_ready=True sector_rank=17 price=38.97 support=35.94 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=57.53 liquidity=3864387.5 spike=0.09
- PRCL.CA: score=25.4 buy_ready=True sector_rank=1 price=35.94 support=27.4 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=23475876.0 spike=0.43
- PRDC.CA: score=24.4 buy_ready=True sector_rank=14 price=9.55 support=6.67 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=69.79 liquidity=59916632.0 spike=0.49
- PRMH.CA: score=16.98 buy_ready=False sector_rank=13 price=2.75 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=73.58 liquidity=2578288.5 spike=0.12
- RACC.CA: score=26.4 buy_ready=True sector_rank=13 price=10.05 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=64.35 liquidity=13915331.0 spike=0.7
- RAKT.CA: score=13.06 buy_ready=False sector_rank=13 price=22.64 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=52.22 liquidity=340573.51 spike=1.16
- RAYA.CA: score=21.04 buy_ready=False sector_rank=18 price=7.71 support=6.99 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=57182396.0 spike=0.44
- RMDA.CA: score=19.4 buy_ready=False sector_rank=6 price=4.99 support=4.81 resistance=5.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=15012650.0 spike=0.83
- ROTO.CA: score=24.4 buy_ready=True sector_rank=13 price=42.02 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=52.79 liquidity=17547726.0 spike=0.65
- RREI.CA: score=15.72 buy_ready=False sector_rank=13 price=3.79 support=3.34 resistance=4.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=76.39 liquidity=4324884.5 spike=0.16
- RTVC.CA: score=15.96 buy_ready=False sector_rank=13 price=4.11 support=3.55 resistance=4.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=79.75 liquidity=2564054.5 spike=0.58
- RUBX.CA: score=24.4 buy_ready=False sector_rank=13 price=13.7 support=9.97 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=70.96 liquidity=36325260.0 spike=0.5
- SAUD.CA: score=26.4 buy_ready=False sector_rank=9 price=22.02 support=19.99 resistance=21.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=68.13 liquidity=19804648.0 spike=3.7
- SCEM.CA: score=26.68 buy_ready=False sector_rank=1 price=77.0 support=60.14 resistance=81.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=84.16 liquidity=50246516.0 spike=1.14
- SCFM.CA: score=10.32 buy_ready=False sector_rank=13 price=273.36 support=270.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24272100.0 spike=1.46
- SCTS.CA: score=12.82 buy_ready=False sector_rank=8 price=612.01 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:26 AM market time freshness=DELAYED_CURRENT RSI=75.94 liquidity=1422448.5 spike=0.23
- SDTI.CA: score=20.53 buy_ready=True sector_rank=13 price=48.69 support=45.55 resistance=48.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=4128870.25 spike=0.75
- SEIG.CA: score=24.4 buy_ready=False sector_rank=13 price=247.23 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=71.05 liquidity=13435228.0 spike=0.59
- SIPC.CA: score=20.87 buy_ready=False sector_rank=13 price=3.77 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=84.52 liquidity=7467660.5 spike=0.57
- SKPC.CA: score=18.33 buy_ready=False sector_rank=16 price=15.98 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=51.23 liquidity=8937329.0 spike=0.25
- SMFR.CA: score=15.58 buy_ready=False sector_rank=13 price=229.56 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=76.07 liquidity=4179510.5 spike=0.23
- SNFC.CA: score=14.86 buy_ready=False sector_rank=13 price=11.29 support=11.21 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=37.11 liquidity=5459067.0 spike=0.48
- SPIN.CA: score=21.85 buy_ready=False sector_rank=4 price=14.95 support=13.8 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=82.18 liquidity=8453595.0 spike=0.62
- SPMD.CA: score=18.17 buy_ready=False sector_rank=13 price=0.45 support=0.41 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=81.67 liquidity=6769393.0 spike=0.3
- SUGR.CA: score=11.63 buy_ready=False sector_rank=17 price=46.95 support=45.31 resistance=48.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=62.91 liquidity=2432699.25 spike=0.46
- SVCE.CA: score=24.4 buy_ready=True sector_rank=13 price=9.4 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=55003676.0 spike=0.85
- SWDY.CA: score=22.4 buy_ready=False sector_rank=3 price=91.65 support=84.3 resistance=93.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=76.3 liquidity=15667664.0 spike=0.91
- TALM.CA: score=26.4 buy_ready=True sector_rank=8 price=15.9 support=15.27 resistance=16.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=53.09 liquidity=11330647.0 spike=0.87
- TMGH.CA: score=23.4 buy_ready=False sector_rank=14 price=101.18 support=92.1 resistance=103.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=77.41 liquidity=217770928.0 spike=0.56
- TRTO.CA: score=12.66 buy_ready=False sector_rank=13 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=953.53 spike=2.13
- UEFM.CA: score=17.33 buy_ready=False sector_rank=13 price=538.87 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=73.56 liquidity=2926157.5 spike=0.69
- UEGC.CA: score=23.4 buy_ready=False sector_rank=13 price=2.42 support=1.33 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=96.67 liquidity=19803950.0 spike=0.48
- UNIP.CA: score=12.46 buy_ready=False sector_rank=13 price=0.43 support=0.4 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46936292.0 spike=2.53
- UNIT.CA: score=13.55 buy_ready=False sector_rank=14 price=18.63 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=76.36 liquidity=2146853.75 spike=0.08
- WCDF.CA: score=16.4 buy_ready=True sector_rank=13 price=560.25 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=65.93 liquidity=1815841.38 spike=1.09
- WKOL.CA: score=16.87 buy_ready=False sector_rank=13 price=319.8 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=71.52 liquidity=2470321.75 spike=0.29
- ZEOT.CA: score=19.87 buy_ready=True sector_rank=13 price=11.68 support=10.4 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=64.22 liquidity=5472144.5 spike=0.14
- ZMID.CA: score=23.4 buy_ready=False sector_rank=14 price=7.45 support=6.19 resistance=7.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=82.57 liquidity=160431312.0 spike=0.65

## Backtesting Lite
- ARCC.CA: 180d return=43.15%, max drawdown=-12.39%, MA20>MA50 days last20=11, as_of=2026-07-19T21:00:00+00:00
- ADIB.CA: 180d return=79.69%, max drawdown=-16.93%, MA20>MA50 days last20=5, as_of=2026-07-19T21:00:00+00:00
- GRCA.CA: 180d return=156.87%, max drawdown=-18.71%, MA20>MA50 days last20=0, as_of=2026-07-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=566 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- ADIB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Dhabi Islamic Bank Egypt summary=ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26; ADIB Egypt stock approaches breakout above EGP 41; ADIB Egypt’s stock holds uptrend despite corrections
  - ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26: https://english.mubasher.info/news/4607278/ADIB-Egypt-s-consolidated-profits-leap-to-EGP-3-6bn-in-Q1-26/
  - ADIB Egypt stock approaches breakout above EGP 41: https://english.mubasher.info/news/4591391/ADIB-Egypt-stock-approaches-breakout-above-EGP-41/
  - ADIB Egypt’s stock holds uptrend despite corrections: https://english.mubasher.info/news/4562331/ADIB-Egypt-s-stock-holds-uptrend-despite-corrections/
- GRCA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Grand Capital for Financial Investments summary=Grand Investment Capital logs lower consolidated net profits in H1-25/26; Grand Investment Capital sees EGP 8m block-trading deal; Grand Investment Capital’s profit hikes 131% in 12M
  - Grand Investment Capital logs lower consolidated net profits in H1-25/26: https://english.mubasher.info/news/4527603/Grand-Investment-Capital-logs-lower-consolidated-net-profits-in-H1-25-26/
  - Grand Investment Capital sees EGP 8m block-trading deal: https://english.mubasher.info/news/3765574/Grand-Investment-Capital-sees-EGP-8m-block-trading-deal/
  - Grand Investment Capital’s profit hikes 131% in 12M: https://english.mubasher.info/news/3481392/Grand-Investment-Capital-s-profit-hikes-131-in-12M/
- MEPA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Medical Packaging Company summary=Medical Packaging stock close to break above EGP 1.7; Medical Packaging announces EGP 62m capital hike; Medical Packaging&#39;s profit jumps 54% in Q1-21
  - Medical Packaging stock close to break above EGP 1.7: https://english.mubasher.info/news/4598700/Medical-Packaging-stock-close-to-break-above-EGP-1-7/
  - Medical Packaging announces EGP 62m capital hike: https://english.mubasher.info/news/3936298/Medical-Packaging-announces-EGP-62m-capital-hike/
  - Medical Packaging&#39;s profit jumps 54% in Q1-21: https://english.mubasher.info/news/3815448/Medical-Packaging-s-profit-jumps-54-in-Q1-21/
- INFI.CA: status=RECENT_ACCEPTED latest=2026-01-01 age_days=201 sources=3 expected=Ismailia National Co. for Food Industries summary=Foodico stock targets higher levels; Foodico plans to log nearly EGP 70.5m profits in 2026; Foodico to secure EGP 12m loan from national bank
  - Foodico stock targets higher levels: https://english.mubasher.info/news/4564894/Foodico-stock-targets-higher-levels/
  - Foodico plans to log nearly EGP 70.5m profits in 2026: https://english.mubasher.info/news/4541309/Foodico-plans-to-log-nearly-EGP-70-5m-profits-in-2026/
  - Foodico to secure EGP 12m loan from national bank: https://english.mubasher.info/news/3888447/Foodico-to-secure-EGP-12m-loan-from-national-bank/
- GDWA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Gadwa for Industrial Development summary=Evidence rejected for GDWA.CA: source text did not clearly match GDWA.CA / Gadwa for Industrial Development.
- FERC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=566 sources=3 expected=Ferchem Misr Fertilizers and Chemicals summary=Ferchem Misr’s board greenlights EGP 500m dividends for 2025; Ferchem Misr’s profits soar 4,238% in 2025; Ferchem Misr’s profit leaps 75% in 9M
  - Ferchem Misr’s board greenlights EGP 500m dividends for 2025: https://english.mubasher.info/news/4600298/Ferchem-Misr-s-board-greenlights-EGP-500m-dividends-for-2025/
  - Ferchem Misr’s profits soar 4,238% in 2025: https://english.mubasher.info/news/4564349/Ferchem-Misr-s-profits-soar-4-238-in-2025/
  - Ferchem Misr’s profit leaps 75% in 9M: https://english.mubasher.info/news/3560738/Ferchem-Misr-s-profit-leaps-75-in-9M/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.

## Warnings
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 'NoneType' object has no attribute 'strip'
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence for GRCA.CA matches the company but no source/report date was detected.
- Evidence for MEPA.CA matches the company but no source/report date was detected.
- Evidence rejected for GDWA.CA: source text did not clearly match GDWA.CA / Gadwa for Industrial Development.
- Evidence for FERC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
