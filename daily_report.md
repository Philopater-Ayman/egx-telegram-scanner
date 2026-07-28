# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-28T08:09:06.490071+00:00
Generated Cairo: 2026-07-28 11:09
Run timing: target 08:45 Cairo | generated Cairo 2026-07-28 11:09 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-28 11:03

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 51
- Data quality issues: 1
- Tradeable price/liquidity tickers: 170/189
- Top sector: Building Materials

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, July 28
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 57.89% / above MA50 57.89%
- EGX70 regime: MIXED / above MA20 72.97% / above MA50 81.08%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- ARVA.CA: liquidity=108637644.73 spike=4.53 score=28.4
- CCAP.CA: liquidity=98856528.0 spike=0.14 score=26.4
- BTFH.CA: liquidity=95280520.0 spike=0.46 score=26.21
- ZMID.CA: liquidity=70931520.0 spike=0.3 score=23.81
- AFMC.CA: liquidity=68868048.0 spike=2.56 score=12.52

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 show mixed trends with modest returns, sector breadth around 52%, and risk mode set to SELECTIVE_SWING_TRADES_ONLY; the local scanner flagged a handful of tickets as the best available setups despite weak evidence and low confidence.
- Tickets such as RMDA.CA, PRCL.CA, PHAR.CA and FWRY.CA were prioritized because they have the highest rank scores (≈27‑28) and bullish‑watch or constructive outlooks, with tradeable liquidity regimes and moderate distance
- Liquidity varies: most flagged stocks sit in a TRADEABLE regime, while ARVA.CA shows an accumulation spike but an overheated RSI near resistance, suggesting near‑term pressure; several others exhibit cooling liquidity, l
- Sector exposure is mixed—Healthcare, Building Materials, Fintech & Payments and General/Verified EGX Expansion are represented, but only Building Materials appears among the leading sectors, so sector‑level support is pa
- Given the EGX30/EGX70 mixed regime and the SELECTIVE_SWING_TRADES_ONLY risk mode, the scanner maintains LOW confidence and highlights that the 1‑3‑day outlook remains uncertain, with no strong conviction to act.

## Top Liquidity Spikes
- ARVA.CA: spike=4.53 liquidity=108637644.73 outlook=CONSTRUCTIVE score=62.63 buy_ready=False
- CFGH.CA: spike=4.08 liquidity=59256.08 outlook=NEUTRAL score=36.63 buy_ready=False
- NCCW.CA: spike=2.94 liquidity=62504236.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AFMC.CA: spike=2.56 liquidity=68868048.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SIPC.CA: spike=2.43 liquidity=35567152.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=9.67 5d=3.41% 20d=13.39% aboveMA50=83.33%
- #2 Telecommunications: score=9.07 5d=2.4% 20d=5.67% aboveMA50=100.0%
- #3 Industrial Goods & Cables: score=8.75 5d=2.93% 20d=7.02% aboveMA50=100.0%
- #4 Fintech & Payments: score=8.36 5d=2.44% 20d=5.99% aboveMA50=100.0%
- #5 Agriculture & Food Production: score=7.2 5d=1.81% 20d=1.8% aboveMA50=100.0%
- #6 Investment Holding: score=7.17 5d=1.84% 20d=6.43% aboveMA50=100.0%
- #7 Textiles: score=7.06 5d=3.06% 20d=5.9% aboveMA50=75.0%
- #8 General / Verified EGX Expansion: score=6.63 5d=1.28% 20d=7.83% aboveMA50=71.84%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ARCC.CA: BULLISH_WATCH score=89.67 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PRCL.CA: BULLISH_WATCH score=85.67 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- RMDA.CA: BULLISH_WATCH score=84.57 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- WCDF.CA: BULLISH_WATCH score=80.63 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading
- FWRY.CA: BULLISH_WATCH score=78.36 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- RACC.CA: BULLISH_WATCH score=77.63 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- APSW.CA: BULLISH_WATCH score=77.63 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- CLHO.CA: BULLISH_WATCH score=77.57 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MPCO.CA: BULLISH_WATCH score=77.2 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ELEC.CA: BULLISH_WATCH score=75.75 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- RMDA.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=84.57 sector_rank=9 price=5.3 support=4.81 resistance=5.17 liquidity=20258172.0
- ELSH.CA: rank=28.4 outlook=CONSTRUCTIVE outlook_score=61.63 sector_rank=8 price=15.2 support=11.1 resistance=15.59 liquidity=23334176.0
- PRCL.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=85.67 sector_rank=1 price=36.41 support=29.15 resistance=38.25 liquidity=11099573.0
- PHAR.CA: rank=26.42 outlook=BULLISH_WATCH outlook_score=70.57 sector_rank=9 price=94.0 support=83.6 resistance=93.5 liquidity=29126436.0
- FWRY.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=78.36 sector_rank=4 price=19.28 support=18.13 resistance=19.68 liquidity=10262016.0
- DTPP.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=61.63 sector_rank=8 price=241.88 support=114.67 resistance=273.0 liquidity=10412977.0
- BTFH.CA: rank=26.21 outlook=BULLISH_WATCH outlook_score=70.53 sector_rank=11 price=3.13 support=2.91 resistance=3.2 liquidity=95280520.0
- TMGH.CA: rank=25.81 outlook=CONSTRUCTIVE outlook_score=69.52 sector_rank=14 price=100.07 support=92.1 resistance=103.87 liquidity=42149528.0
- AFDI.CA: rank=24.4 outlook=CONSTRUCTIVE outlook_score=53.63 sector_rank=8 price=51.01 support=41.84 resistance=49.99 liquidity=10017800.0
- AJWA.CA: rank=24.4 outlook=BULLISH_WATCH outlook_score=70.63 sector_rank=8 price=187.0 support=161.0 resistance=192.0 liquidity=12722945.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=17.61 buy_ready=False sector_rank=8 price=245.36 support=196.0 resistance=253.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=70.31 liquidity=1206788.75 spike=0.06
- ABUK.CA: score=22.04 buy_ready=False sector_rank=17 price=70.9 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=53.74 liquidity=18179976.0 spike=0.12
- ACAMD.CA: score=23.11 buy_ready=True sector_rank=8 price=2.39 support=2.14 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=8711102.0 spike=0.12
- ACGC.CA: score=17.63 buy_ready=False sector_rank=7 price=10.77 support=8.92 resistance=11.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=74.82 liquidity=3234223.25 spike=0.11
- ADCI.CA: score=14.87 buy_ready=False sector_rank=8 price=260.25 support=230.0 resistance=266.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=68.4 liquidity=467059.25 spike=0.04
- ADIB.CA: score=9.11 buy_ready=False sector_rank=12 price=51.98 support=51.2 resistance=51.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13890686.0 spike=0.12
- ADPC.CA: score=7.12 buy_ready=False sector_rank=8 price=4.19 support=4.17 resistance=4.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7723410.5 spike=0.24
- AFDI.CA: score=24.4 buy_ready=True sector_rank=8 price=51.01 support=41.84 resistance=49.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=69.03 liquidity=10017800.0 spike=0.7
- AFMC.CA: score=12.52 buy_ready=False sector_rank=8 price=132.97 support=127.12 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68868048.0 spike=2.56
- AJWA.CA: score=24.4 buy_ready=True sector_rank=8 price=187.0 support=161.0 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=50.49 liquidity=12722945.0 spike=0.88
- ALCN.CA: score=14.58 buy_ready=False sector_rank=13 price=29.46 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=69.59 liquidity=584148.25 spike=0.03
- ALUM.CA: score=13.83 buy_ready=False sector_rank=8 price=23.35 support=20.55 resistance=24.09 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=67.09 liquidity=2434167.49 spike=0.36
- AMER.CA: score=6.83 buy_ready=False sector_rank=14 price=4.54 support=4.54 resistance=4.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8025028.0 spike=0.08
- AMES.CA: score=9.4 buy_ready=False sector_rank=8 price=129.12 support=127.55 resistance=133.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18426794.0 spike=0.19
- AMIA.CA: score=15.27 buy_ready=False sector_rank=8 price=10.5 support=8.4 resistance=10.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:29 AM market time freshness=DELAYED_CURRENT RSI=72.62 liquidity=870414.38 spike=0.07
- AMOC.CA: score=20.25 buy_ready=True sector_rank=10 price=8.28 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=5845837.0 spike=0.1
- APSW.CA: score=14.7 buy_ready=True sector_rank=8 price=8.73 support=8.0 resistance=9.34 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=55.83 liquidity=1860362.9 spike=1.22
- ARAB.CA: score=21.81 buy_ready=True sector_rank=14 price=0.25 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=22726832.0 spike=0.17
- ARCC.CA: score=21.98 buy_ready=True sector_rank=1 price=56.67 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=53.22 liquidity=2579910.5 spike=0.1
- AREH.CA: score=14.08 buy_ready=False sector_rank=8 price=1.5 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=41.82 liquidity=1681078.62 spike=0.05
- ARVA.CA: score=28.4 buy_ready=False sector_rank=8 price=12.47 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=76.51 liquidity=108637644.73 spike=4.53
- ASCM.CA: score=9.4 buy_ready=False sector_rank=8 price=65.33 support=65.0 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49957464.0 spike=1.0
- ASPI.CA: score=9.4 buy_ready=False sector_rank=8 price=0.44 support=0.44 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13132679.0 spike=0.48
- ATLC.CA: score=17.61 buy_ready=False sector_rank=11 price=5.19 support=4.92 resistance=5.43 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=45.07 liquidity=5402110.17 spike=0.77
- ATQA.CA: score=17.38 buy_ready=True sector_rank=17 price=9.86 support=9.35 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=66.09 liquidity=2336136.0 spike=0.07
- AXPH.CA: score=16.88 buy_ready=False sector_rank=8 price=1218.49 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=481792.34 spike=0.12
- BINV.CA: score=12.91 buy_ready=False sector_rank=6 price=47.16 support=44.98 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=505642.56 spike=0.07
- BIOC.CA: score=10.66 buy_ready=False sector_rank=8 price=164.3 support=142.5 resistance=171.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52200036.0 spike=1.63
- BTFH.CA: score=26.21 buy_ready=True sector_rank=11 price=3.13 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=95280520.0 spike=0.46
- CAED.CA: score=9.4 buy_ready=False sector_rank=8 price=130.03 support=128.4 resistance=135.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16444444.0 spike=0.31
- CANA.CA: score=20.38 buy_ready=True sector_rank=12 price=38.74 support=34.7 resistance=38.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=4264222.5 spike=0.27
- CCAP.CA: score=26.4 buy_ready=False sector_rank=6 price=5.4 support=4.65 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=98856528.0 spike=0.14
- CCRS.CA: score=16.34 buy_ready=True sector_rank=8 price=2.62 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=69.01 liquidity=1942403.63 spike=0.11
- CEFM.CA: score=9.4 buy_ready=False sector_rank=8 price=133.49 support=130.01 resistance=136.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14200056.0 spike=0.99
- CERA.CA: score=16.29 buy_ready=True sector_rank=8 price=1.35 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=1889253.25 spike=0.08
- CFGH.CA: score=15.46 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=53.85 liquidity=59256.08 spike=4.08
- CICH.CA: score=16.88 buy_ready=False sector_rank=11 price=12.2 support=11.52 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=671170.69 spike=0.13
- CIEB.CA: score=12.9 buy_ready=False sector_rank=12 price=24.11 support=23.3 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=785635.5 spike=0.1
- CIRA.CA: score=8.29 buy_ready=False sector_rank=16 price=33.89 support=33.56 resistance=34.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11852310.0 spike=0.33
- CLHO.CA: score=18.29 buy_ready=True sector_rank=9 price=16.82 support=15.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=56.49 liquidity=3888548.25 spike=0.09
- CNFN.CA: score=14.62 buy_ready=False sector_rank=11 price=4.89 support=4.61 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=407137.84 spike=0.02
- COMI.CA: score=24.11 buy_ready=True sector_rank=12 price=140.53 support=126.21 resistance=140.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.21 liquidity=16383013.0 spike=0.04
- COPR.CA: score=15.69 buy_ready=False sector_rank=8 price=0.42 support=0.35 resistance=0.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=83.91 liquidity=3294013.0 spike=0.12
- COSG.CA: score=15.78 buy_ready=False sector_rank=8 price=1.71 support=1.47 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=80.77 liquidity=4377775.0 spike=0.1
- CPCI.CA: score=15.05 buy_ready=False sector_rank=8 price=466.29 support=370.01 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=72.77 liquidity=649406.81 spike=0.06
- CSAG.CA: score=15.17 buy_ready=False sector_rank=13 price=32.6 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=53.28 liquidity=1170177.75 spike=0.06
- DAPH.CA: score=14.98 buy_ready=False sector_rank=8 price=96.62 support=78.52 resistance=98.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=75.22 liquidity=1581169.75 spike=0.09
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=8 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=16.35 buy_ready=True sector_rank=18 price=27.02 support=26.06 resistance=27.83 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=46.55 liquidity=3366205.7 spike=0.92
- DSCW.CA: score=14.21 buy_ready=False sector_rank=8 price=1.96 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=87.1 liquidity=2807499.0 spike=0.06
- DTPP.CA: score=26.4 buy_ready=True sector_rank=8 price=241.88 support=114.67 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=68.78 liquidity=10412977.0 spike=0.15
- EALR.CA: score=17.57 buy_ready=True sector_rank=8 price=372.0 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=1165542.75 spike=0.07
- EASB.CA: score=15.06 buy_ready=False sector_rank=8 price=7.87 support=6.88 resistance=8.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=61.65 liquidity=664483.56 spike=0.04
- EAST.CA: score=10.88 buy_ready=False sector_rank=18 price=36.38 support=36.11 resistance=38.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=1892841.13 spike=0.03
- EBSC.CA: score=9.78 buy_ready=False sector_rank=8 price=1.93 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=21.87 liquidity=381778.09 spike=0.05
- ECAP.CA: score=19.95 buy_ready=True sector_rank=8 price=34.01 support=31.52 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:28 AM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=1553900.25 spike=0.2
- EDFM.CA: score=13.13 buy_ready=False sector_rank=8 price=380.05 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=82.59 liquidity=1733190.88 spike=0.42
- EEII.CA: score=15.61 buy_ready=True sector_rank=8 price=2.8 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=49.12 liquidity=1214789.0 spike=0.06
- EFIC.CA: score=9.62 buy_ready=False sector_rank=17 price=185.16 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:28 AM market time freshness=DELAYED_CURRENT RSI=53.18 liquidity=575795.5 spike=0.05
- EFID.CA: score=17.98 buy_ready=False sector_rank=18 price=27.05 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=19990500.0 spike=0.49
- EFIH.CA: score=23.73 buy_ready=True sector_rank=4 price=23.02 support=20.0 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=9329646.0 spike=0.17
- EGAL.CA: score=17.65 buy_ready=False sector_rank=17 price=298.71 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=5606733.5 spike=0.13
- EGAS.CA: score=15.36 buy_ready=False sector_rank=10 price=53.93 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=67.8 liquidity=956672.31 spike=0.08
- EGBE.CA: score=13.12 buy_ready=False sector_rank=12 price=0.49 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=97.71 liquidity=8233.64 spike=0.32
- EGCH.CA: score=22.04 buy_ready=False sector_rank=17 price=13.17 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=55.68 liquidity=15451180.0 spike=0.27
- EGSA.CA: score=14.41 buy_ready=False sector_rank=2 price=8.97 support=8.67 resistance=9.21 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=65.71 liquidity=13688.22 spike=0.88
- EGTS.CA: score=6.84 buy_ready=False sector_rank=14 price=17.82 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=3029155.75 spike=0.06
- EHDR.CA: score=22.19 buy_ready=False sector_rank=8 price=2.93 support=2.37 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=70.33 liquidity=5788653.5 spike=0.16
- EKHO.CA: score=8.4 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.87 buy_ready=True sector_rank=3 price=2.22 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=4474722.0 spike=0.07
- ELKA.CA: score=18.43 buy_ready=False sector_rank=8 price=1.95 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=79.21 liquidity=7034967.5 spike=0.1
- ELNA.CA: score=16.75 buy_ready=False sector_rank=8 price=38.99 support=35.55 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=27 July 12:52 PM market time freshness=DELAYED_CURRENT RSI=54.53 liquidity=354476.25 spike=0.57
- ELSH.CA: score=28.4 buy_ready=True sector_rank=8 price=15.2 support=11.1 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=63.2 liquidity=23334176.0 spike=0.17
- ELWA.CA: score=10.5 buy_ready=False sector_rank=8 price=1.91 support=1.87 resistance=2.14 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=1103044.08 spike=0.93
- EMFD.CA: score=13.46 buy_ready=False sector_rank=14 price=11.62 support=11.24 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=47.71 liquidity=1653013.25 spike=0.03
- ENGC.CA: score=22.94 buy_ready=False sector_rank=8 price=43.61 support=35.1 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=70.98 liquidity=8544839.0 spike=0.33
- EOSB.CA: score=14.41 buy_ready=False sector_rank=8 price=1.48 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6979.68 spike=0.16
- EPCO.CA: score=15.0 buy_ready=False sector_rank=8 price=11.26 support=8.5 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=86.46 liquidity=1598345.38 spike=0.06
- EPPK.CA: score=23.21 buy_ready=True sector_rank=8 price=15.82 support=12.37 resistance=15.83 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=62.06 liquidity=2727510.33 spike=2.04
- ETEL.CA: score=23.4 buy_ready=False sector_rank=2 price=105.51 support=89.01 resistance=106.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=77.8 liquidity=31649754.0 spike=0.42
- ETRS.CA: score=22.4 buy_ready=False sector_rank=8 price=10.82 support=10.25 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=10551199.0 spike=0.18
- EXPA.CA: score=18.16 buy_ready=False sector_rank=12 price=19.99 support=18.03 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=74.78 liquidity=4051586.25 spike=0.13
- FAIT.CA: score=18.13 buy_ready=True sector_rank=12 price=37.33 support=35.06 resistance=38.0 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=59.26 liquidity=2017313.3 spike=0.7
- FAITA.CA: score=10.19 buy_ready=False sector_rank=12 price=0.96 support=0.96 resistance=0.99 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=36.76 liquidity=93572.78 spike=1.99
- FERC.CA: score=15.13 buy_ready=True sector_rank=17 price=77.88 support=72.75 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=57.31 liquidity=1091786.13 spike=0.1
- FWRY.CA: score=26.4 buy_ready=True sector_rank=4 price=19.28 support=18.13 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=10262016.0 spike=0.08
- GBCO.CA: score=16.93 buy_ready=False sector_rank=15 price=30.38 support=29.5 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=48.14 liquidity=5485201.5 spike=0.07
- GDWA.CA: score=20.4 buy_ready=False sector_rank=8 price=0.87 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=81.53 liquidity=11889625.0 spike=0.15
- GGCC.CA: score=17.68 buy_ready=False sector_rank=8 price=0.89 support=0.42 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=89.37 liquidity=4276984.0 spike=0.11
- GIHD.CA: score=23.4 buy_ready=False sector_rank=8 price=62.23 support=40.66 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=76.45 liquidity=22277482.0 spike=0.46
- GMCI.CA: score=15.07 buy_ready=False sector_rank=8 price=2.0 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=53.33 liquidity=672628.0 spike=0.5
- GRCA.CA: score=16.18 buy_ready=True sector_rank=8 price=61.99 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=1777059.0 spike=0.12
- GSSC.CA: score=15.18 buy_ready=False sector_rank=8 price=267.45 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=68.87 liquidity=779636.38 spike=0.08
- GTWL.CA: score=23.68 buy_ready=True sector_rank=8 price=102.24 support=60.0 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=60.62 liquidity=9278647.0 spike=0.06
- HDBK.CA: score=11.53 buy_ready=False sector_rank=12 price=82.41 support=75.3 resistance=163.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=42.05 liquidity=1414114.0 spike=0.04
- HELI.CA: score=20.81 buy_ready=False sector_rank=14 price=8.42 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=89.9 liquidity=48944332.0 spike=0.27
- HRHO.CA: score=19.04 buy_ready=True sector_rank=11 price=26.81 support=26.09 resistance=27.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=49.81 liquidity=3825438.5 spike=0.04
- ICID.CA: score=14.84 buy_ready=False sector_rank=8 price=8.11 support=6.55 resistance=8.98 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=52.87 liquidity=444776.71 spike=0.06
- IDRE.CA: score=22.28 buy_ready=True sector_rank=8 price=50.02 support=41.1 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=63.02 liquidity=3882550.0 spike=0.17
- IFAP.CA: score=19.33 buy_ready=False sector_rank=5 price=19.79 support=18.47 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=57.38 liquidity=926932.44 spike=0.1
- INFI.CA: score=15.47 buy_ready=False sector_rank=8 price=107.84 support=88.51 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=74.8 liquidity=1068463.0 spike=0.07
- IRON.CA: score=2.37 buy_ready=False sector_rank=17 price=30.94 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=29.61 liquidity=328443.28 spike=0.05
- ISMA.CA: score=22.43 buy_ready=False sector_rank=8 price=31.94 support=26.54 resistance=31.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=70.84 liquidity=6032984.0 spike=0.27
- ISMQ.CA: score=18.04 buy_ready=False sector_rank=17 price=9.43 support=8.6 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=30.41 liquidity=14922596.0 spike=0.14
- ISPH.CA: score=16.75 buy_ready=False sector_rank=9 price=11.68 support=11.2 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=51.54 liquidity=3345466.75 spike=0.06
- JUFO.CA: score=16.99 buy_ready=False sector_rank=18 price=28.95 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=44.46 liquidity=9006892.0 spike=0.39
- KABO.CA: score=14.8 buy_ready=False sector_rank=7 price=8.62 support=6.04 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=89.21 liquidity=3400309.5 spike=0.07
- KWIN.CA: score=9.46 buy_ready=False sector_rank=8 price=107.09 support=96.3 resistance=107.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46774404.0 spike=1.03
- KZPC.CA: score=12.83 buy_ready=False sector_rank=8 price=8.62 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=51.69 liquidity=434089.31 spike=0.08
- LCSW.CA: score=18.52 buy_ready=False sector_rank=1 price=35.89 support=27.01 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=77.83 liquidity=2123292.75 spike=0.03
- LUTS.CA: score=5.56 buy_ready=False sector_rank=8 price=0.59 support=0.58 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=19.01 liquidity=2164468.5 spike=0.06
- MAAL.CA: score=21.4 buy_ready=False sector_rank=8 price=8.79 support=6.78 resistance=8.86 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=83.78 liquidity=14934825.24 spike=0.83
- MASR.CA: score=24.4 buy_ready=False sector_rank=8 price=8.04 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=74.65 liquidity=14337126.0 spike=0.17
- MBSC.CA: score=17.72 buy_ready=False sector_rank=1 price=245.28 support=222.66 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=1317098.13 spike=0.07
- MCQE.CA: score=18.33 buy_ready=False sector_rank=1 price=187.19 support=166.66 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=66.84 liquidity=928639.19 spike=0.05
- MCRO.CA: score=22.4 buy_ready=False sector_rank=8 price=1.48 support=1.17 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=83.72 liquidity=12974224.0 spike=0.12
- MENA.CA: score=14.88 buy_ready=False sector_rank=14 price=6.98 support=6.59 resistance=7.59 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=52.69 liquidity=3073203.27 spike=0.4
- MEPA.CA: score=17.99 buy_ready=False sector_rank=8 price=1.92 support=1.52 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=3594247.75 spike=0.08
- MFPC.CA: score=13.75 buy_ready=False sector_rank=17 price=36.6 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=52.84 liquidity=3705741.5 spike=0.04
- MFSC.CA: score=5.1 buy_ready=False sector_rank=8 price=46.44 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=30.28 liquidity=697308.44 spike=0.11
- MHOT.CA: score=1.79 buy_ready=False sector_rank=21 price=16.66 support=16.12 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=31.72 liquidity=391009.22 spike=0.03
- MICH.CA: score=14.89 buy_ready=False sector_rank=8 price=41.05 support=34.0 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=83.28 liquidity=1491481.38 spike=0.1
- MILS.CA: score=9.4 buy_ready=False sector_rank=8 price=178.28 support=172.2 resistance=180.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15899626.0 spike=0.47
- MIPH.CA: score=14.73 buy_ready=False sector_rank=9 price=741.97 support=630.13 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=72.06 liquidity=330957.66 spike=0.1
- MOED.CA: score=13.0 buy_ready=False sector_rank=8 price=0.71 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=598005.12 spike=0.03
- MOIL.CA: score=13.53 buy_ready=False sector_rank=10 price=0.64 support=0.46 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=86.93 liquidity=128349.33 spike=0.24
- MOIN.CA: score=10.87 buy_ready=False sector_rank=8 price=23.6 support=22.6 resistance=24.76 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=46.84 liquidity=465840.41 spike=0.59
- MOSC.CA: score=23.26 buy_ready=True sector_rank=8 price=286.38 support=250.0 resistance=329.5 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=63.16 liquidity=6859946.64 spike=0.56
- MPCI.CA: score=16.5 buy_ready=False sector_rank=8 price=285.94 support=222.55 resistance=289.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=78.68 liquidity=3099194.5 spike=0.03
- MPCO.CA: score=17.26 buy_ready=True sector_rank=5 price=1.86 support=1.7 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=56.41 liquidity=2858739.25 spike=0.05
- MPRC.CA: score=10.72 buy_ready=False sector_rank=8 price=44.24 support=36.7 resistance=45.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:29 AM market time freshness=DELAYED_CURRENT RSI=75.27 liquidity=1321708.63 spike=0.04
- MTIE.CA: score=21.12 buy_ready=True sector_rank=15 price=9.49 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=7677071.5 spike=0.35
- NAHO.CA: score=3.43 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=25.0 liquidity=26677.79 spike=0.8
- NCCW.CA: score=13.28 buy_ready=False sector_rank=8 price=7.17 support=6.95 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62504236.0 spike=2.94
- NEDA.CA: score=9.95 buy_ready=False sector_rank=8 price=2.76 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=51.11 liquidity=552394.68 spike=0.82
- NHPS.CA: score=19.52 buy_ready=False sector_rank=8 price=88.06 support=61.55 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=79.33 liquidity=8121894.5 spike=0.1
- NINH.CA: score=16.71 buy_ready=False sector_rank=8 price=22.31 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=72.36 liquidity=2309569.75 spike=0.06
- NIPH.CA: score=21.4 buy_ready=False sector_rank=9 price=230.83 support=157.01 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=89.55 liquidity=19172062.0 spike=0.13
- OBRI.CA: score=8.59 buy_ready=False sector_rank=8 price=34.28 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=4192133.25 spike=0.11
- OCDI.CA: score=23.81 buy_ready=True sector_rank=14 price=28.02 support=23.75 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=61.06 liquidity=42913996.0 spike=0.42
- OCPH.CA: score=16.88 buy_ready=False sector_rank=8 price=482.35 support=341.4 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=90.9 liquidity=5476962.0 spike=0.23
- ODIN.CA: score=14.45 buy_ready=False sector_rank=8 price=2.66 support=2.05 resistance=2.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=76.81 liquidity=1047716.5 spike=0.06
- OFH.CA: score=21.4 buy_ready=False sector_rank=8 price=0.72 support=0.57 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=20312870.0 spike=0.34
- OIH.CA: score=22.8 buy_ready=False sector_rank=6 price=1.49 support=1.4 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=6395635.5 spike=0.1
- OLFI.CA: score=13.87 buy_ready=False sector_rank=18 price=23.46 support=21.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.26 liquidity=888515.13 spike=0.03
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=711.92 support=708.5 resistance=712.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10944102.0 spike=1.0
- ORHD.CA: score=23.81 buy_ready=True sector_rank=14 price=40.67 support=37.0 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=61.59 liquidity=33403016.0 spike=0.22
- ORWE.CA: score=18.65 buy_ready=True sector_rank=7 price=23.11 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=2249424.75 spike=0.09
- PHAR.CA: score=26.42 buy_ready=True sector_rank=9 price=94.0 support=83.6 resistance=93.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=55.66 liquidity=29126436.0 spike=1.01
- PHDC.CA: score=18.81 buy_ready=False sector_rank=14 price=14.77 support=14.26 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=21731122.0 spike=0.09
- PHTV.CA: score=13.14 buy_ready=False sector_rank=8 price=311.36 support=246.51 resistance=319.0 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=79.62 liquidity=1743615.92 spike=0.28
- POUL.CA: score=13.63 buy_ready=False sector_rank=18 price=38.12 support=36.52 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=53.32 liquidity=2649650.5 spike=0.08
- PRCL.CA: score=27.4 buy_ready=True sector_rank=1 price=36.41 support=29.15 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=61.78 liquidity=11099573.0 spike=0.22
- PRDC.CA: score=21.29 buy_ready=True sector_rank=14 price=9.39 support=6.8 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=63.96 liquidity=5485053.5 spike=0.05
- PRMH.CA: score=16.01 buy_ready=True sector_rank=8 price=2.7 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=56.86 liquidity=1605872.88 spike=0.09
- RACC.CA: score=17.27 buy_ready=True sector_rank=8 price=10.1 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=52.51 liquidity=2866545.5 spike=0.14
- RAKT.CA: score=12.56 buy_ready=False sector_rank=8 price=22.64 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=62.22 liquidity=156465.04 spike=0.54
- RAYA.CA: score=20.94 buy_ready=False sector_rank=19 price=7.62 support=7.01 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=32102846.0 spike=0.24
- RMDA.CA: score=28.4 buy_ready=True sector_rank=9 price=5.3 support=4.81 resistance=5.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=20258172.0 spike=0.99
- ROTO.CA: score=17.43 buy_ready=True sector_rank=8 price=45.15 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=3032867.5 spike=0.13
- RREI.CA: score=9.96 buy_ready=False sector_rank=8 price=4.47 support=4.26 resistance=4.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37104784.0 spike=1.28
- RTVC.CA: score=17.79 buy_ready=True sector_rank=8 price=4.05 support=3.55 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=56.96 liquidity=1387399.38 spike=0.3
- RUBX.CA: score=15.34 buy_ready=False sector_rank=8 price=13.18 support=10.38 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=51.3 liquidity=935851.56 spike=0.01
- SAUD.CA: score=17.42 buy_ready=True sector_rank=12 price=22.51 support=19.99 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=68.81 liquidity=1304943.38 spike=0.15
- SCEM.CA: score=24.4 buy_ready=False sector_rank=1 price=82.5 support=60.14 resistance=85.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=80.14 liquidity=16855800.0 spike=0.3
- SCFM.CA: score=20.76 buy_ready=True sector_rank=8 price=283.32 support=230.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=61.36 liquidity=4359073.5 spike=0.23
- SCTS.CA: score=13.84 buy_ready=False sector_rank=16 price=619.72 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=551711.06 spike=0.08
- SDTI.CA: score=16.45 buy_ready=False sector_rank=8 price=53.0 support=45.55 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=80.99 liquidity=3054692.0 spike=0.4
- SEIG.CA: score=14.06 buy_ready=False sector_rank=8 price=250.0 support=182.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=71.54 liquidity=1660320.13 spike=0.07
- SIPC.CA: score=12.26 buy_ready=False sector_rank=8 price=4.23 support=4.14 resistance=4.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35567152.0 spike=2.43
- SKPC.CA: score=11.51 buy_ready=False sector_rank=17 price=16.01 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=2473834.75 spike=0.07
- SMFR.CA: score=15.53 buy_ready=False sector_rank=8 price=231.13 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=1129985.25 spike=0.06
- SNFC.CA: score=10.18 buy_ready=False sector_rank=8 price=11.21 support=11.2 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=784964.25 spike=0.07
- SPIN.CA: score=9.4 buy_ready=False sector_rank=7 price=16.42 support=16.06 resistance=16.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11418422.0 spike=0.74
- SPMD.CA: score=22.44 buy_ready=True sector_rank=8 price=0.47 support=0.41 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=65.31 liquidity=18481840.0 spike=1.02
- SUGR.CA: score=11.8 buy_ready=False sector_rank=18 price=46.96 support=45.31 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=48.13 liquidity=812652.69 spike=0.15
- SVCE.CA: score=17.67 buy_ready=False sector_rank=8 price=9.3 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=5265384.0 spike=0.09
- SWDY.CA: score=17.75 buy_ready=False sector_rank=3 price=95.75 support=84.3 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=78.81 liquidity=3347651.5 spike=0.16
- TALM.CA: score=14.36 buy_ready=False sector_rank=16 price=15.77 support=15.27 resistance=16.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=42.69 liquidity=2070552.25 spike=0.15
- TMGH.CA: score=25.81 buy_ready=True sector_rank=14 price=100.07 support=92.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=42149528.0 spike=0.11
- TRTO.CA: score=12.06 buy_ready=False sector_rank=8 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=2036.5 spike=1.83
- UEFM.CA: score=14.83 buy_ready=False sector_rank=8 price=543.25 support=460.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=67.95 liquidity=429788.16 spike=0.1
- UEGC.CA: score=19.72 buy_ready=False sector_rank=8 price=2.57 support=1.33 resistance=2.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=90.91 liquidity=6316009.0 spike=0.14
- UNIP.CA: score=13.48 buy_ready=False sector_rank=8 price=0.42 support=0.3 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=80.45 liquidity=2079676.75 spike=0.09
- UNIT.CA: score=16.52 buy_ready=True sector_rank=14 price=18.71 support=12.0 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=69.19 liquidity=4713784.0 spike=0.16
- WCDF.CA: score=21.78 buy_ready=True sector_rank=8 price=585.52 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=64.42 liquidity=3536032.5 spike=1.92
- WKOL.CA: score=14.98 buy_ready=False sector_rank=8 price=314.07 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=575888.5 spike=0.06
- ZEOT.CA: score=16.76 buy_ready=True sector_rank=8 price=11.85 support=10.4 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=64.13 liquidity=2358756.75 spike=0.07
- ZMID.CA: score=23.81 buy_ready=False sector_rank=14 price=7.7 support=6.19 resistance=7.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=70.27 liquidity=70931520.0 spike=0.3

## Backtesting Lite
- RMDA.CA: 180d return=22.97%, max drawdown=-27.97%, MA20>MA50 days last20=13, as_of=2026-07-25T21:00:00+00:00
- ARVA.CA: 180d return=65.38%, max drawdown=-31.83%, MA20>MA50 days last20=20, as_of=2026-07-25T21:00:00+00:00
- ELSH.CA: 180d return=87.11%, max drawdown=-27.17%, MA20>MA50 days last20=20, as_of=2026-07-25T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- ARVA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Arab Valves Company summary=Evidence rejected for ARVA.CA: source text did not clearly match ARVA.CA / Arab Valves Company.
- ELSH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Al Shams Housing and Urbanization SAE summary=Al Shams Housing’s stock tests key support amid selling pressure; FRA approves Al Shams Housing’s capital increase; Al Shams Housing awards part of NAC project to Olive Tree
  - Al Shams Housing’s stock tests key support amid selling pressure: https://english.mubasher.info/news/4553488/Al-Shams-Housing-s-stock-tests-key-support-amid-selling-pressure/
  - FRA approves Al Shams Housing’s capital increase: https://english.mubasher.info/news/3899254/FRA-approves-Al-Shams-Housing-s-capital-increase/
  - Al Shams Housing awards part of NAC project to Olive Tree: https://english.mubasher.info/news/3896693/Al-Shams-Housing-awards-part-of-NAC-project-to-Olive-Tree/
- PRCL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ceramic and Porcelain summary=Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- DTPP.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=573 sources=3 expected=Delta Co. For Printing & Packaging S.A.E summary=Delta for Printing to disburse EGP 56m dividends for 2025; Delta for Printing&#39;s profit leaps 89% in 2020; dividends proposed; Delta for Printing Q1 profits rise 175%
  - Delta for Printing to disburse EGP 56m dividends for 2025: https://english.mubasher.info/news/4596419/Delta-for-Printing-to-disburse-EGP-56m-dividends-for-2025/
  - Delta for Printing&#39;s profit leaps 89% in 2020; dividends proposed: https://english.mubasher.info/news/3759564/Delta-for-Printing-s-profit-leaps-89-in-2020-dividends-proposed/
  - Delta for Printing Q1 profits rise 175%: https://english.mubasher.info/news/3106332/Delta-for-Printing-Q1-profits-rise-175-/

## Warnings
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Mubasher stock-page evidence failed for ARVA.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ARVA
- No Yahoo or Mubasher evidence found for ARVA.CA.
- Evidence rejected for ARVA.CA: source text did not clearly match ARVA.CA / Arab Valves Company.
- Evidence for ELSH.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for DTPP.CA matches the company but appears old; latest detected date is 2025-01-01.
