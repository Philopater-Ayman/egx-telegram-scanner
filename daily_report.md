# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-10-26T21:10:28.909237+00:00
Generated Cairo: 2026-10-27 00:10
Run timing: target 19:30 Cairo | generated Cairo 2026-10-27 00:10 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-10-27 00:06

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 150/186
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, October 26
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 12.5% / above MA50 6.25%
- EGX70 regime: BEARISH / above MA20 0.0% / above MA50 0.0%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=1304304000.0 spike=3.0 score=18.28
- CCAP.CA: liquidity=459328832.0 spike=0.91 score=12.63
- ETEL.CA: liquidity=400781792.0 spike=1.6 score=10.08
- ORAS.CA: liquidity=385820512.0 spike=1.0 score=6.6
- MBSC.CA: liquidity=216724608.0 spike=2.25 score=9.9

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- EOSB.CA: spike=8.08 liquidity=440994.09 outlook=NEUTRAL score=49 buy_ready=False
- MENA.CA: spike=5.54 liquidity=10951899.0 outlook=WEAK_OR_RISKY score=17 buy_ready=False
- EPCO.CA: spike=4.16 liquidity=17226066.0 outlook=WEAK_OR_RISKY score=23 buy_ready=False
- SCTS.CA: spike=3.94 liquidity=10547106.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RREI.CA: spike=3.52 liquidity=24571568.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=1.58 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #2 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #3 Textiles: score=0.32 5d=-2.13% 20d=-6.08% aboveMA50=0.0%
- #4 Telecommunications: score=-0.3 5d=-3.98% 20d=-4.22% aboveMA50=0.0%
- #5 Banking & Financials: score=-1.8 5d=-2.88% 20d=-11.31% aboveMA50=0.0%
- #6 Energy & Petrochemicals: score=-2.16 5d=-3.2% 20d=-9.79% aboveMA50=0.0%
- #7 Non-bank Financial Services: score=-2.95 5d=-2.57% 20d=-13.95% aboveMA50=0.0%
- #8 Basic Resources & Chemicals: score=-3.06 5d=-2.87% 20d=-17.79% aboveMA50=10.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELNA.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- ABUK.CA: BULLISH_WATCH score=76 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- EAST.CA: CONSTRUCTIVE score=61 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA50; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=60 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=overheated RSI; sector is not leading
- AJWA.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- SDTI.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- EOSB.CA: NEUTRAL score=49 liquidity=THIN sector=LAGGING risk=liquidity below minimum; close to resistance; sector is not leading
- LCSW.CA: WEAK_OR_RISKY score=31 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; below MA50; sector is not leading
- HELI.CA: WEAK_OR_RISKY score=28 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA20; below MA50; weak RSI; sector is not leading
- BTFH.CA: WEAK_OR_RISKY score=28 liquidity=ACCUMULATION_SPIKE sector=NEUTRAL risk=below MA20; below MA50; weak RSI

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=0.31 buy_ready=False sector_rank=18 price=189.71 support=192.0 resistance=293.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=18.98 liquidity=3914608.5 spike=0.43
- ABUK.CA: score=19.78 buy_ready=False sector_rank=8 price=88.91 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=70018008.0 spike=0.91
- ACAMD.CA: score=11.4 buy_ready=False sector_rank=18 price=1.88 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=43625368.0 spike=0.96
- ACGC.CA: score=6.34 buy_ready=False sector_rank=3 price=12.18 support=12.35 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=22.39 liquidity=6215404.0 spike=0.6
- ADCI.CA: score=0.63 buy_ready=False sector_rank=18 price=232.94 support=230.0 resistance=288.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=15.31 liquidity=2312089.75 spike=1.46
- ADIB.CA: score=7.76 buy_ready=False sector_rank=5 price=44.41 support=43.16 resistance=51.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.89 liquidity=93188024.0 spike=1.24
- ADPC.CA: score=3.06 buy_ready=False sector_rank=18 price=2.71 support=2.53 resistance=3.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=13.48 liquidity=6659504.0 spike=0.65
- AFDI.CA: score=0.56 buy_ready=False sector_rank=18 price=39.1 support=38.01 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=16.59 liquidity=4162706.75 spike=0.96
- AFMC.CA: score=7.4 buy_ready=False sector_rank=18 price=101.2 support=98.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=8.26 liquidity=10287109.0 spike=0.57
- AJWA.CA: score=17.4 buy_ready=False sector_rank=18 price=195.41 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=61.2 liquidity=10617809.0 spike=0.3
- ALCN.CA: score=12.49 buy_ready=False sector_rank=13 price=30.96 support=27.11 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.82 liquidity=14193787.0 spike=0.66
- ALUM.CA: score=-1.13 buy_ready=False sector_rank=18 price=16.68 support=16.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:11 PM market time freshness=DELAYED_CURRENT RSI=14.12 liquidity=2471532.75 spike=0.66
- AMER.CA: score=7.63 buy_ready=False sector_rank=10 price=3.45 support=3.4 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=26.29 liquidity=39094460.0 spike=0.76
- AMES.CA: score=8.4 buy_ready=False sector_rank=18 price=29.19 support=29.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=5.17 liquidity=29227132.0 spike=0.49
- AMIA.CA: score=7.4 buy_ready=False sector_rank=18 price=16.68 support=15.33 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=26.66 liquidity=15385415.0 spike=0.93
- AMOC.CA: score=13.14 buy_ready=False sector_rank=6 price=12.7 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.96 liquidity=90876968.0 spike=0.72
- APSW.CA: score=-1.26 buy_ready=False sector_rank=18 price=7.12 support=7.4 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=31.35 liquidity=977208.19 spike=1.68
- ARAB.CA: score=2.63 buy_ready=False sector_rank=10 price=0.23 support=0.21 resistance=0.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90005056.0 spike=0.82
- ARCC.CA: score=7.4 buy_ready=False sector_rank=17 price=60.22 support=58.12 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=20.33 liquidity=31461608.0 spike=0.72
- AREH.CA: score=3.73 buy_ready=False sector_rank=18 price=0.95 support=0.94 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=12.24 liquidity=7334851.5 spike=0.9
- ASCM.CA: score=2.76 buy_ready=False sector_rank=18 price=40.34 support=40.0 resistance=60.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=13.89 liquidity=6356568.0 spike=0.71
- ASPI.CA: score=6.4 buy_ready=False sector_rank=18 price=0.28 support=0.27 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=17.96 liquidity=14631715.0 spike=0.76
- ATLC.CA: score=3.68 buy_ready=False sector_rank=7 price=4.4 support=3.93 resistance=4.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10507526.0 spike=1.43
- ATQA.CA: score=6.78 buy_ready=False sector_rank=8 price=8.75 support=8.43 resistance=12.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=23.27 liquidity=30846922.0 spike=0.55
- AXPH.CA: score=0.22 buy_ready=False sector_rank=18 price=1172.18 support=1135.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:12 PM market time freshness=DELAYED_CURRENT RSI=12.16 liquidity=2815844.25 spike=0.48
- BINV.CA: score=10.79 buy_ready=False sector_rank=1 price=53.53 support=52.57 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33628660.0 spike=2.58
- BIOC.CA: score=7.4 buy_ready=False sector_rank=18 price=224.92 support=213.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=12.31 liquidity=38946068.0 spike=0.36
- BTFH.CA: score=7.94 buy_ready=False sector_rank=7 price=2.17 support=2.05 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=17.86 liquidity=154446688.0 spike=1.56
- CAED.CA: score=4.31 buy_ready=False sector_rank=18 price=69.21 support=70.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=4.39 liquidity=7912896.5 spike=0.96
- CANA.CA: score=8.28 buy_ready=False sector_rank=5 price=41.0 support=38.1 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=32.46 liquidity=11843268.0 spike=0.67
- CCAP.CA: score=12.63 buy_ready=False sector_rank=1 price=5.91 support=5.87 resistance=7.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.15 liquidity=459328832.0 spike=0.91
- CCRS.CA: score=1.32 buy_ready=False sector_rank=18 price=1.48 support=1.3 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8399872.0 spike=1.26
- CEFM.CA: score=-3.26 buy_ready=False sector_rank=18 price=107.59 support=103.05 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:08 PM market time freshness=DELAYED_CURRENT RSI=18.03 liquidity=344057.22 spike=0.17
- CERA.CA: score=6.4 buy_ready=False sector_rank=18 price=0.99 support=1.01 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=18.57 liquidity=91956312.0 spike=0.76
- CFGH.CA: score=0.14 buy_ready=False sector_rank=18 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:10 PM market time freshness=DELAYED_CURRENT RSI=10.0 liquidity=15876.28 spike=2.86
- CICH.CA: score=-2.64 buy_ready=False sector_rank=7 price=10.27 support=9.63 resistance=12.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=17.01 liquidity=543459.38 spike=0.23
- CIEB.CA: score=6.99 buy_ready=False sector_rank=5 price=21.42 support=21.4 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=9494112.0 spike=1.11
- CIRA.CA: score=7.7 buy_ready=False sector_rank=9 price=33.17 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=25.39 liquidity=12051720.0 spike=0.7
- CLHO.CA: score=6.4 buy_ready=False sector_rank=15 price=12.93 support=12.71 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=3.95 liquidity=18177642.0 spike=0.49
- CNFN.CA: score=1.41 buy_ready=False sector_rank=7 price=3.53 support=3.5 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=4594822.0 spike=0.48
- COMI.CA: score=18.28 buy_ready=False sector_rank=5 price=120.91 support=120.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.2 liquidity=1304304000.0 spike=3.0
- COPR.CA: score=6.4 buy_ready=False sector_rank=18 price=0.37 support=0.33 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=9.29 liquidity=10867546.0 spike=0.65
- COSG.CA: score=3.91 buy_ready=False sector_rank=18 price=1.15 support=1.11 resistance=1.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=16.22 liquidity=7510480.5 spike=0.65
- CPCI.CA: score=16.05 buy_ready=False sector_rank=18 price=589.94 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=36.68 liquidity=7634690.0 spike=1.51
- CSAG.CA: score=4.87 buy_ready=False sector_rank=13 price=30.92 support=30.1 resistance=38.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=18.45 liquidity=8033951.0 spike=1.17
- DAPH.CA: score=6.4 buy_ready=False sector_rank=18 price=68.6 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=24.85 liquidity=23236694.0 spike=0.56
- DEIN.CA: score=5.4 buy_ready=False sector_rank=18 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=-0.97 buy_ready=False sector_rank=14 price=20.87 support=20.27 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=7.97 liquidity=2633048.25 spike=0.75
- DSCW.CA: score=6.4 buy_ready=False sector_rank=18 price=1.37 support=1.23 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=12601348.0 spike=0.79
- DTPP.CA: score=2.4 buy_ready=False sector_rank=18 price=39.86 support=36.0 resistance=41.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19090274.0 spike=0.46
- EALR.CA: score=-1.8 buy_ready=False sector_rank=18 price=244.04 support=240.0 resistance=362.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=10.26 liquidity=1798120.25 spike=0.54
- EASB.CA: score=-3.63 buy_ready=False sector_rank=18 price=5.51 support=5.23 resistance=5.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3972039.75 spike=0.82
- EAST.CA: score=17.28 buy_ready=False sector_rank=14 price=30.18 support=27.01 resistance=31.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=84920224.0 spike=1.94
- EBSC.CA: score=-2.45 buy_ready=False sector_rank=18 price=1.27 support=1.25 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=1154619.62 spike=0.55
- ECAP.CA: score=-2.57 buy_ready=False sector_rank=18 price=25.57 support=25.0 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=16.05 liquidity=1029912.31 spike=0.29
- EDFM.CA: score=-7.08 buy_ready=False sector_rank=18 price=356.38 support=350.0 resistance=370.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=520284.91 spike=0.47
- EEII.CA: score=-0.42 buy_ready=False sector_rank=18 price=1.56 support=1.5 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=9.76 liquidity=3180286.75 spike=0.47
- EFIC.CA: score=2.78 buy_ready=False sector_rank=8 price=122.91 support=122.0 resistance=134.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15335040.0 spike=0.54
- EFID.CA: score=8.54 buy_ready=False sector_rank=14 price=16.99 support=16.3 resistance=20.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=44292952.0 spike=1.07
- EFIH.CA: score=6.57 buy_ready=False sector_rank=11 price=20.53 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=32.51 liquidity=59256492.0 spike=0.91
- EGAL.CA: score=6.78 buy_ready=False sector_rank=8 price=289.1 support=275.0 resistance=362.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=22.91 liquidity=70056056.0 spike=0.76
- EGAS.CA: score=1.65 buy_ready=False sector_rank=6 price=43.9 support=43.55 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=18.9 liquidity=4509420.0 spike=0.65
- EGBE.CA: score=-1.53 buy_ready=False sector_rank=5 price=0.48 support=0.48 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=22.89 liquidity=107462.78 spike=1.04
- EGCH.CA: score=6.78 buy_ready=False sector_rank=8 price=10.31 support=10.0 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=18.75 liquidity=39994768.0 spike=0.62
- EGSA.CA: score=6.39 buy_ready=False sector_rank=4 price=8.81 support=8.75 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 11:15 AM market time freshness=DELAYED_CURRENT RSI=66.07 liquidity=7998.91 spike=1.25
- EGTS.CA: score=8.15 buy_ready=False sector_rank=10 price=10.62 support=10.71 resistance=19.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=10.73 liquidity=37634812.0 spike=1.76
- EHDR.CA: score=5.49 buy_ready=False sector_rank=18 price=1.86 support=1.8 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=17.95 liquidity=9091109.0 spike=0.9
- ELEC.CA: score=6.4 buy_ready=False sector_rank=16 price=1.4 support=1.36 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=49215080.0 spike=0.98
- ELKA.CA: score=2.6 buy_ready=False sector_rank=18 price=1.33 support=1.21 resistance=1.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13863657.0 spike=1.1
- ELNA.CA: score=16.59 buy_ready=False sector_rank=18 price=36.92 support=33.46 resistance=38.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:06 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1447311.25 spike=3.37
- ELSH.CA: score=3.65 buy_ready=False sector_rank=18 price=8.76 support=8.6 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=7253004.0 spike=0.36
- ELWA.CA: score=8.4 buy_ready=False sector_rank=18 price=1.65 support=1.43 resistance=1.67 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=782.1 spike=0.0
- EMFD.CA: score=7.63 buy_ready=False sector_rank=10 price=11.49 support=10.6 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=31017912.0 spike=0.53
- ENGC.CA: score=3.52 buy_ready=False sector_rank=18 price=28.18 support=28.12 resistance=41.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=14.83 liquidity=7124886.0 spike=0.65
- EOSB.CA: score=16.84 buy_ready=False sector_rank=18 price=1.61 support=1.57 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:09 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=440994.09 spike=8.08
- EPCO.CA: score=11.4 buy_ready=False sector_rank=18 price=7.21 support=7.0 resistance=11.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=17.88 liquidity=17226066.0 spike=4.16
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=18 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=10.08 buy_ready=False sector_rank=4 price=117.99 support=121.01 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=19.29 liquidity=400781792.0 spike=1.6
- ETRS.CA: score=5.7 buy_ready=False sector_rank=18 price=10.34 support=9.63 resistance=10.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27731614.0 spike=2.65
- EXPA.CA: score=7.28 buy_ready=False sector_rank=5 price=13.03 support=12.0 resistance=22.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=14.73 liquidity=28885162.0 spike=0.76
- FAIT.CA: score=2.0 buy_ready=False sector_rank=5 price=41.89 support=40.0 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=30.72 liquidity=3395792.5 spike=1.16
- FAITA.CA: score=3.29 buy_ready=False sector_rank=5 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:11 PM market time freshness=DELAYED_CURRENT RSI=47.41 liquidity=11296.91 spike=0.31
- FERC.CA: score=0.76 buy_ready=False sector_rank=8 price=55.0 support=53.57 resistance=77.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=12.85 liquidity=3724304.75 spike=1.13
- FWRY.CA: score=7.25 buy_ready=False sector_rank=11 price=17.01 support=16.45 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.5 liquidity=148384352.0 spike=1.34
- GBCO.CA: score=6.5 buy_ready=False sector_rank=12 price=22.99 support=22.02 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=12.34 liquidity=80938008.0 spike=0.69
- GDWA.CA: score=6.88 buy_ready=False sector_rank=18 price=0.51 support=0.49 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=16.01 liquidity=18020642.0 spike=1.24
- GGCC.CA: score=5.73 buy_ready=False sector_rank=18 price=0.5 support=0.5 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=21.05 liquidity=9327005.0 spike=0.59
- GIHD.CA: score=5.98 buy_ready=False sector_rank=18 price=34.25 support=34.83 resistance=78.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=5.04 liquidity=9579690.0 spike=0.65
- GMCI.CA: score=-1.56 buy_ready=False sector_rank=18 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=34.62 liquidity=39066.72 spike=0.12
- GRCA.CA: score=-3.61 buy_ready=False sector_rank=18 price=23.79 support=22.57 resistance=26.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3986642.5 spike=0.77
- GSSC.CA: score=-2.62 buy_ready=False sector_rank=18 price=230.3 support=222.22 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=25.72 liquidity=980061.44 spike=0.8
- HDBK.CA: score=4.68 buy_ready=False sector_rank=5 price=95.92 support=92.52 resistance=97.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35665996.0 spike=1.7
- HELI.CA: score=8.63 buy_ready=False sector_rank=10 price=6.28 support=5.96 resistance=7.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=101435224.0 spike=1.5
- HRHO.CA: score=11.82 buy_ready=False sector_rank=7 price=23.99 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.07 liquidity=74208856.0 spike=0.58
- ICID.CA: score=2.4 buy_ready=False sector_rank=18 price=15.81 support=14.26 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=30.61 liquidity=4997591.5 spike=0.7
- IDRE.CA: score=-1.54 buy_ready=False sector_rank=18 price=30.04 support=29.11 resistance=32.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5984438.5 spike=1.04
- IFAP.CA: score=1.34 buy_ready=False sector_rank=20 price=16.35 support=15.51 resistance=20.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:12 PM market time freshness=DELAYED_CURRENT RSI=10.73 liquidity=4938249.5 spike=0.93
- INFI.CA: score=6.4 buy_ready=False sector_rank=18 price=101.11 support=99.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.57 liquidity=10646966.0 spike=0.52
- IRON.CA: score=9.38 buy_ready=False sector_rank=8 price=23.91 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.35 liquidity=7607729.0 spike=0.71
- ISMA.CA: score=5.95 buy_ready=False sector_rank=18 price=15.95 support=16.3 resistance=29.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=15.24 liquidity=8971402.0 spike=1.29
- ISMQ.CA: score=6.78 buy_ready=False sector_rank=8 price=6.22 support=6.0 resistance=8.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=17.7 liquidity=12031830.0 spike=0.69
- ISPH.CA: score=6.4 buy_ready=False sector_rank=15 price=9.65 support=9.14 resistance=12.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=9.99 liquidity=42509568.0 spike=0.92
- JUFO.CA: score=6.4 buy_ready=False sector_rank=14 price=21.82 support=21.01 resistance=26.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=21.97 liquidity=11284047.0 spike=0.67
- KABO.CA: score=7.57 buy_ready=False sector_rank=3 price=6.7 support=5.58 resistance=6.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46498692.0 spike=2.22
- KWIN.CA: score=-0.29 buy_ready=False sector_rank=18 price=47.89 support=48.5 resistance=90.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=12.55 liquidity=3308247.0 spike=0.65
- KZPC.CA: score=6.85 buy_ready=False sector_rank=18 price=11.9 support=12.0 resistance=14.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=40.57 liquidity=4450730.5 spike=0.58
- LCSW.CA: score=11.55 buy_ready=False sector_rank=17 price=31.03 support=28.0 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=9148546.0 spike=0.46
- LUTS.CA: score=6.4 buy_ready=False sector_rank=18 price=0.52 support=0.51 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=8.3 liquidity=51163852.0 spike=0.93
- MAAL.CA: score=1.37 buy_ready=False sector_rank=18 price=5.6 support=4.88 resistance=5.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8971333.0 spike=0.5
- MASR.CA: score=7.0 buy_ready=False sector_rank=18 price=6.18 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=21.58 liquidity=63814184.0 spike=1.3
- MBSC.CA: score=9.9 buy_ready=False sector_rank=17 price=281.31 support=262.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=31.1 liquidity=216724608.0 spike=2.25
- MCQE.CA: score=8.68 buy_ready=False sector_rank=17 price=147.96 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=11.65 liquidity=138335008.0 spike=2.14
- MCRO.CA: score=2.4 buy_ready=False sector_rank=18 price=1.15 support=1.09 resistance=1.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39024804.0 spike=0.86
- MENA.CA: score=11.63 buy_ready=False sector_rank=10 price=5.64 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:00 PM market time freshness=DELAYED_CURRENT RSI=34.16 liquidity=10951899.0 spike=5.54
- MEPA.CA: score=8.72 buy_ready=False sector_rank=18 price=1.21 support=1.2 resistance=1.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=16.85 liquidity=14479293.0 spike=2.16
- MFPC.CA: score=2.9 buy_ready=False sector_rank=8 price=44.68 support=44.01 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52135840.0 spike=1.06
- MFSC.CA: score=-4.88 buy_ready=False sector_rank=18 price=30.73 support=28.55 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2539344.0 spike=1.09
- MHOT.CA: score=1.6 buy_ready=False sector_rank=21 price=13.5 support=13.0 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=16.71 liquidity=5196502.0 spike=0.35
- MICH.CA: score=9.36 buy_ready=False sector_rank=18 price=38.79 support=35.5 resistance=45.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=35.66 liquidity=6962302.5 spike=0.87
- MILS.CA: score=5.33 buy_ready=False sector_rank=18 price=104.16 support=106.4 resistance=201.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=8.96 liquidity=8688719.0 spike=1.12
- MIPH.CA: score=-0.02 buy_ready=False sector_rank=15 price=740.72 support=675.0 resistance=759.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6320700.0 spike=1.63
- MOED.CA: score=2.56 buy_ready=False sector_rank=18 price=0.4 support=0.39 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13939397.0 spike=1.08
- MOIL.CA: score=-0.78 buy_ready=False sector_rank=6 price=0.62 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=23.77 liquidity=285934.41 spike=1.4
- MOIN.CA: score=-0.37 buy_ready=False sector_rank=18 price=26.03 support=25.88 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=19.06 liquidity=3228106.25 spike=0.33
- MOSC.CA: score=-5.92 buy_ready=False sector_rank=18 price=211.13 support=198.01 resistance=237.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1683536.13 spike=0.5
- MPCI.CA: score=7.4 buy_ready=False sector_rank=18 price=254.65 support=239.0 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=10.7 liquidity=92483832.0 spike=0.95
- MPCO.CA: score=6.4 buy_ready=False sector_rank=20 price=1.69 support=1.55 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=18.4 liquidity=90619568.0 spike=0.95
- MPRC.CA: score=7.56 buy_ready=False sector_rank=18 price=27.82 support=27.1 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=9.71 liquidity=25479910.0 spike=1.58
- MTIE.CA: score=4.82 buy_ready=False sector_rank=12 price=6.67 support=6.05 resistance=6.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42609636.0 spike=2.16
- NAHO.CA: score=-4.0 buy_ready=False sector_rank=18 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42978.92 spike=2.78
- NCCW.CA: score=6.4 buy_ready=False sector_rank=18 price=4.37 support=4.21 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=8.4 liquidity=12827369.0 spike=0.51
- NEDA.CA: score=-0.57 buy_ready=False sector_rank=18 price=2.6 support=2.47 resistance=2.74 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=25040.6 spike=0.11
- NHPS.CA: score=0.36 buy_ready=False sector_rank=18 price=50.93 support=50.06 resistance=79.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=7.11 liquidity=3957517.5 spike=0.46
- NINH.CA: score=1.76 buy_ready=False sector_rank=18 price=12.87 support=12.36 resistance=20.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=5.04 liquidity=5361905.0 spike=0.52
- NIPH.CA: score=7.4 buy_ready=False sector_rank=15 price=225.98 support=220.0 resistance=341.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=24.02 liquidity=113979520.0 spike=0.97
- OBRI.CA: score=6.4 buy_ready=False sector_rank=18 price=19.27 support=19.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=18.63 liquidity=10032792.0 spike=0.69
- OCDI.CA: score=3.13 buy_ready=False sector_rank=10 price=22.09 support=21.35 resistance=23.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44852612.0 spike=1.25
- OCPH.CA: score=-0.88 buy_ready=False sector_rank=18 price=151.08 support=147.96 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=4.7 liquidity=2718348.25 spike=0.92
- ODIN.CA: score=3.11 buy_ready=False sector_rank=18 price=1.79 support=1.8 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=17.74 liquidity=6531553.0 spike=1.09
- OFH.CA: score=6.4 buy_ready=False sector_rank=18 price=0.66 support=0.63 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=12.73 liquidity=13816093.0 spike=0.31
- OIH.CA: score=7.73 buy_ready=False sector_rank=1 price=1.52 support=1.5 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60999512.0 spike=1.05
- OLFI.CA: score=6.84 buy_ready=False sector_rank=14 price=18.98 support=18.02 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=16.32 liquidity=18027746.0 spike=1.22
- ORAS.CA: score=6.6 buy_ready=False sector_rank=2 price=779.98 support=772.0 resistance=819.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=385820512.0 spike=1.0
- ORHD.CA: score=8.63 buy_ready=False sector_rank=10 price=9.26 support=8.5 resistance=41.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=14.58 liquidity=97770264.0 spike=0.82
- ORWE.CA: score=10.13 buy_ready=False sector_rank=3 price=23.49 support=23.31 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=22.42 liquidity=37669444.0 spike=0.96
- PHAR.CA: score=6.48 buy_ready=False sector_rank=15 price=93.1 support=91.61 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=16.55 liquidity=61996532.0 spike=1.04
- PHDC.CA: score=6.63 buy_ready=False sector_rank=10 price=11.67 support=11.45 resistance=13.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.94 liquidity=63151860.0 spike=0.64
- PHTV.CA: score=-0.42 buy_ready=False sector_rank=18 price=307.56 support=305.0 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:08 PM market time freshness=DELAYED_CURRENT RSI=31.97 liquidity=1380312.5 spike=1.4
- POUL.CA: score=13.62 buy_ready=False sector_rank=14 price=9.0 support=8.85 resistance=38.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.66 liquidity=63200244.0 spike=1.11
- PRCL.CA: score=4.62 buy_ready=False sector_rank=17 price=18.38 support=17.25 resistance=31.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=22.18 liquidity=8222013.0 spike=0.82
- PRDC.CA: score=6.63 buy_ready=False sector_rank=10 price=5.88 support=5.45 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=17.87 liquidity=19202024.0 spike=0.55
- PRMH.CA: score=-2.3 buy_ready=False sector_rank=18 price=1.74 support=1.7 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:12 PM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=1303117.25 spike=0.43
- RACC.CA: score=4.54 buy_ready=False sector_rank=18 price=6.91 support=6.1 resistance=7.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13715907.0 spike=2.07
- RAKT.CA: score=9.48 buy_ready=False sector_rank=18 price=23.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=63.62 liquidity=79464.76 spike=0.2
- RAYA.CA: score=6.4 buy_ready=False sector_rank=19 price=5.26 support=5.02 resistance=7.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=15.84 liquidity=16304331.0 spike=0.57
- RMDA.CA: score=7.12 buy_ready=False sector_rank=15 price=4.8 support=4.52 resistance=5.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=24.43 liquidity=34760184.0 spike=1.36
- ROTO.CA: score=-1.32 buy_ready=False sector_rank=18 price=28.39 support=25.51 resistance=29.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6279032.0 spike=0.7
- RREI.CA: score=7.4 buy_ready=False sector_rank=18 price=2.27 support=1.96 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24571568.0 spike=3.52
- RTVC.CA: score=-2.29 buy_ready=False sector_rank=18 price=2.89 support=3.04 resistance=3.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=1311471.38 spike=0.5
- RUBX.CA: score=2.52 buy_ready=False sector_rank=18 price=11.55 support=10.51 resistance=13.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87660040.0 spike=1.06
- SAUD.CA: score=6.22 buy_ready=False sector_rank=5 price=20.02 support=20.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=18.94 liquidity=8944153.0 spike=0.74
- SCEM.CA: score=7.4 buy_ready=False sector_rank=17 price=76.32 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=32.38 liquidity=20102720.0 spike=0.33
- SCFM.CA: score=-2.41 buy_ready=False sector_rank=18 price=165.94 support=153.02 resistance=189.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3351429.0 spike=1.92
- SCTS.CA: score=7.7 buy_ready=False sector_rank=9 price=500.4 support=437.0 resistance=503.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10547106.0 spike=3.94
- SDTI.CA: score=15.4 buy_ready=False sector_rank=18 price=81.77 support=75.01 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=16046768.0 spike=0.56
- SEIG.CA: score=-2.26 buy_ready=False sector_rank=18 price=150.58 support=142.0 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=13.0 liquidity=1341956.5 spike=0.64
- SIPC.CA: score=12.4 buy_ready=False sector_rank=18 price=4.05 support=4.04 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.85 liquidity=27015500.0 spike=0.47
- SKPC.CA: score=6.78 buy_ready=False sector_rank=8 price=14.31 support=14.15 resistance=17.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=27.74 liquidity=33620652.0 spike=0.52
- SMFR.CA: score=-2.29 buy_ready=False sector_rank=18 price=167.97 support=173.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=21.79 liquidity=1309665.5 spike=0.43
- SNFC.CA: score=1.35 buy_ready=False sector_rank=18 price=10.71 support=10.3 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=29.81 liquidity=4949956.5 spike=0.61
- SPIN.CA: score=8.21 buy_ready=False sector_rank=3 price=14.17 support=12.0 resistance=14.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13413918.0 spike=2.54
- SPMD.CA: score=2.39 buy_ready=False sector_rank=18 price=0.31 support=0.31 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=5987692.5 spike=0.51
- SUGR.CA: score=9.14 buy_ready=False sector_rank=14 price=49.38 support=50.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=41.55 liquidity=7743524.5 spike=0.86
- SVCE.CA: score=6.4 buy_ready=False sector_rank=18 price=8.0 support=7.01 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=10.45 liquidity=53933700.0 spike=0.77
- SWDY.CA: score=7.84 buy_ready=False sector_rank=16 price=103.44 support=97.0 resistance=124.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=24.23 liquidity=73369544.0 spike=1.22
- TALM.CA: score=7.7 buy_ready=False sector_rank=9 price=18.03 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=19.7 liquidity=16805266.0 spike=0.59
- TMGH.CA: score=13.63 buy_ready=False sector_rank=10 price=82.0 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.53 liquidity=213250656.0 spike=0.83
- TRTO.CA: score=2.89 buy_ready=False sector_rank=18 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:02 PM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=14480.36 spike=2.24
- UEFM.CA: score=-2.69 buy_ready=False sector_rank=18 price=431.45 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=23.14 liquidity=914783.38 spike=0.32
- UEGC.CA: score=2.4 buy_ready=False sector_rank=18 price=1.32 support=1.22 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40734376.0 spike=0.91
- UNIP.CA: score=4.99 buy_ready=False sector_rank=18 price=0.27 support=0.26 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=19.53 liquidity=8485166.0 spike=1.05
- UNIT.CA: score=1.0 buy_ready=False sector_rank=10 price=16.0 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=3370345.0 spike=0.89
- WCDF.CA: score=-2.83 buy_ready=False sector_rank=18 price=468.97 support=432.5 resistance=686.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:12 PM market time freshness=DELAYED_CURRENT RSI=14.36 liquidity=765243.0 spike=0.3
- WKOL.CA: score=0.45 buy_ready=False sector_rank=18 price=222.25 support=218.0 resistance=249.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7909256.0 spike=1.07
- ZEOT.CA: score=2.3 buy_ready=False sector_rank=18 price=9.15 support=9.01 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=5897997.0 spike=0.75
- ZMID.CA: score=6.97 buy_ready=False sector_rank=10 price=6.04 support=6.01 resistance=8.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=26 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=16.6 liquidity=85356064.0 spike=1.17

## Backtesting Lite
- ABUK.CA: 180d return=55.92%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-24T21:00:00+00:00
- COMI.CA: 180d return=-2.24%, max drawdown=-18.04%, MA20>MA50 days last20=0, as_of=2026-10-24T21:00:00+00:00
- AJWA.CA: 180d return=71.28%, max drawdown=-14.31%, MA20>MA50 days last20=9, as_of=2026-10-24T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- EOSB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Orouba Securities Brokerage summary=El Orouba Brokerage turns profitable in Q4; El Orouba Securities suffers 598,000 losses in Q3; El Orouba Securities H1 losses down 7%
  - El Orouba Brokerage turns profitable in Q4: https://english.mubasher.info/news/3067539/El-Orouba-Brokerage-turns-profitable-in-Q4/
  - El Orouba Securities suffers 598,000 losses in Q3: https://english.mubasher.info/news/3016624/El-Orouba-Securities-suffers-598-000-losses-in-Q3/
  - El Orouba Securities H1 losses down 7%: https://english.mubasher.info/news/2984110/El-Orouba-Securities-H1-losses-down-7-/
- ELNA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Manufacturing Agricultural Crops S.A.E summary=Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops; El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m; EGX halts trading on El Nasr for Manufacturing Agricultural Crops
  - Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops: https://english.mubasher.info/news/3749421/Consortium-offers-to-acquire-controlling-stake-in-El-Nasr-for-Agricultural-Crops/
  - El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m: https://english.mubasher.info/news/3685533/El-Nasr-for-Agricultural-Crops-to-sell-Sohag-factory-land-for-EGP-650m/
  - EGX halts trading on El Nasr for Manufacturing Agricultural Crops: https://english.mubasher.info/news/3489525/EGX-halts-trading-on-El-Nasr-for-Manufacturing-Agricultural-Crops/
- CPCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Kahira Pharmaceuticals & Chemical Industries Company summary=Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22; Kahira Pharmaceuticals sees EGP 9m block trading deal; Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals
  - Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22: https://english.mubasher.info/news/3910780/Kahira-Pharmaceuticals-net-profits-up-22-5-in-H1-21-22/
  - Kahira Pharmaceuticals sees EGP 9m block trading deal: https://english.mubasher.info/news/3903033/Kahira-Pharmaceuticals-sees-EGP-9m-block-trading-deal/
  - Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals: https://english.mubasher.info/news/3816375/Adel-Taha-Abdel-Wahab-named-Chairman-of-Kahira-Pharmaceuticals/
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/

## Warnings
- OpenRouter API error: 404
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence for EOSB.CA matches the company but no source/report date was detected.
- Evidence for ELNA.CA matches the company but no source/report date was detected.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
