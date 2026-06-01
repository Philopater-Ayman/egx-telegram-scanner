# Telegram-First EGX Scanner Report

Scan phase: Manual scan
Generated UTC: 2026-06-01T23:19:43.344595+00:00

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 190/190
- Top sector: Industrial Goods & Cables

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, June 01
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 9.52% / above MA50 14.29%
- EGX70 regime: BEARISH / above MA20 22.5% / above MA50 45.0%
- Sector breadth: 28.57%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- HDBK.CA: liquidity=473890400.0 spike=20.8 score=19.3
- BTFH.CA: liquidity=426312576.0 spike=1.91 score=22.63
- CCAP.CA: liquidity=339120544.0 spike=0.41 score=15.34
- ACAMD.CA: liquidity=293166464.0 spike=3.47 score=18.29
- ELEC.CA: liquidity=240493456.0 spike=6.16 score=24.4

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (≈28%). Liquidity is thin and most sectors are not leading, so the risk mode is DEFENSIVE_NO_NEW_BUY. Even though a few tickets show bullish watch signals, the overall market outlook for the next 1‑3 days remains cautious.
- EGX30/EGX70 trends bearish; only ~10‑22% of stocks above MA20/MA50, indicating weak support.
- Sector breadth low (28.57%); leading sectors are Industrial Goods & Cables, Construction, and Textiles but they are not driving the market.
- Top tickets (ICID, KABO, ORWE, etc.) show bullish outlooks but liquidity spikes are modest and RSI levels vary, adding uncertainty.
- Risk mode set to DEFENSIVE_NO_NEW_BUY – market does not support initiating new long positions.
- Uncertainty remains high; any short‑term moves should be monitored for changes in liquidity or sector leadership.

## Top Liquidity Spikes
- HDBK.CA: spike=20.8 liquidity=473890400.0 outlook=NEUTRAL score=40.25 buy_ready=False
- PRMH.CA: spike=11.37 liquidity=124150192.0 outlook=NEUTRAL score=40.37 buy_ready=False
- SIPC.CA: spike=11.14 liquidity=162426640.0 outlook=CONSTRUCTIVE score=65.37 buy_ready=False
- ELEC.CA: spike=6.16 liquidity=240493456.0 outlook=BULLISH_WATCH score=75.42 buy_ready=False
- ICID.CA: spike=5.42 liquidity=34468940.0 outlook=BULLISH_WATCH score=91.37 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Cables: score=8.42 5d=1.26% 20d=-1.21% aboveMA50=50.0%
- #2 Industrial Goods & Construction: score=7.5 5d=0.0% 20d=0.0% aboveMA50=100.0%
- #3 Textiles: score=6.18 5d=2.01% 20d=4.31% aboveMA50=75.0%
- #4 Automotive & Distribution: score=5.18 5d=4.24% 20d=3.26% aboveMA50=50.0%
- #5 Transportation & Logistics: score=5.15 5d=2.76% 20d=2.08% aboveMA50=50.0%
- #6 Technology & Distribution: score=4.8 5d=5.2% 20d=9.04% aboveMA50=0.0%
- #7 Non-bank Financial Services: score=4.53 5d=0.34% 20d=2.77% aboveMA50=40.0%
- #8 Real Estate: score=4.36 5d=3.04% 20d=9.08% aboveMA50=23.08%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KABO.CA: BULLISH_WATCH score=99.18 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- ORWE.CA: BULLISH_WATCH score=94.18 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ICID.CA: BULLISH_WATCH score=91.37 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- ORAS.CA: BULLISH_WATCH score=90.5 liquidity=TRADEABLE sector=LEADING risk=far above support
- ARAB.CA: BULLISH_WATCH score=86.36 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BTFH.CA: BULLISH_WATCH score=85.53 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ECAP.CA: BULLISH_WATCH score=79.37 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ELEC.CA: BULLISH_WATCH score=75.42 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=weak RSI; far above support
- SPMD.CA: BULLISH_WATCH score=75.37 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- COSG.CA: BULLISH_WATCH score=74.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=5.75 buy_ready=False sector_rank=10 price=183.38 support=177.5 resistance=256.93 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=25.38 liquidity=5399751.0 spike=0.2
- ABUK.CA: score=14.35 buy_ready=False sector_rank=9 price=51.0 support=78.0 resistance=92.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=56.48 liquidity=25078658.0 spike=0.18
- ACAMD.CA: score=18.29 buy_ready=False sector_rank=10 price=1.72 support=1.94 resistance=2.28 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=66.67 liquidity=293166464.0 spike=3.47
- ACGC.CA: score=22.4 buy_ready=False sector_rank=3 price=8.96 support=8.3 resistance=10.86 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=63.96 liquidity=16762178.0 spike=0.39
- ADCI.CA: score=11.46 buy_ready=False sector_rank=10 price=215.85 support=181.13 resistance=225.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=53.07 liquidity=1114307.0 spike=0.14
- ADIB.CA: score=14.3 buy_ready=False sector_rank=13 price=29.9 support=44.25 resistance=50.08 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=52.2 liquidity=36456864.0 spike=0.22
- ADPC.CA: score=22.37 buy_ready=False sector_rank=10 price=3.84 support=3.54 resistance=4.45 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=37.5 liquidity=40054816.0 spike=2.01
- AFDI.CA: score=11.49 buy_ready=False sector_rank=10 price=33.8 support=35.03 resistance=44.6 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=61.91 liquidity=7145536.0 spike=0.5
- AFMC.CA: score=13.62 buy_ready=False sector_rank=10 price=62.24 support=67.11 resistance=80.89 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=36.93 liquidity=8267087.0 spike=0.51
- AJWA.CA: score=19.51 buy_ready=False sector_rank=10 price=129.13 support=130.01 resistance=139.5 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=46.82 liquidity=15468334.0 spike=1.58
- ALCN.CA: score=18.06 buy_ready=False sector_rank=5 price=24.48 support=28.4 resistance=30.35 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=44.8 liquidity=17632852.0 spike=0.49
- ALUM.CA: score=15.35 buy_ready=False sector_rank=10 price=21.2 support=20.75 resistance=26.12 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=54.31 liquidity=15716760.0 spike=0.75
- AMER.CA: score=20.74 buy_ready=False sector_rank=8 price=2.26 support=2.06 resistance=2.87 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=73.63 liquidity=60357364.0 spike=0.52
- AMES.CA: score=7.1 buy_ready=False sector_rank=10 price=55.11 support=50.0 resistance=65.87 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=23.78 liquidity=1753719.0 spike=0.09
- AMIA.CA: score=14.35 buy_ready=False sector_rank=10 price=4.83 support=7.3 resistance=10.08 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=39.86 liquidity=11345314.0 spike=0.34
- AMOC.CA: score=14.08 buy_ready=False sector_rank=18 price=6.93 support=8.12 resistance=9.15 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=44.62 liquidity=10737433.0 spike=0.1
- ANFI.CA: score=15.48 buy_ready=False sector_rank=10 price=14.14 support=13.5 resistance=17.77 source=Yahoo Finance as_of=2026-05-31T21:00:00+00:00 freshness=FRESH RSI=54.8 liquidity=7134436.15 spike=0.29
- APSW.CA: score=7.88 buy_ready=False sector_rank=10 price=8.93 support=8.62 resistance=9.38 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=56.57 liquidity=534214.0 spike=0.38
- ARAB.CA: score=24.02 buy_ready=False sector_rank=8 price=0.21 support=0.19 resistance=0.21 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=50.0 liquidity=150615824.0 spike=2.64
- ARCC.CA: score=15.26 buy_ready=False sector_rank=14 price=50.8 support=52.6 resistance=58.7 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=55.0 liquidity=19918242.0 spike=0.55
- AREH.CA: score=10.88 buy_ready=False sector_rank=10 price=1.33 support=1.27 resistance=1.43 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=42.86 liquidity=2535114.0 spike=0.11
- ARVA.CA: score=5.33 buy_ready=False sector_rank=10 price=8.16 support=7.65 resistance=9.23 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=26.91 liquidity=1983096.0 spike=0.1
- ASCM.CA: score=12.91 buy_ready=False sector_rank=10 price=43.39 support=43.76 resistance=50.98 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=56.4 liquidity=7558283.0 spike=0.2
- ASPI.CA: score=16.11 buy_ready=False sector_rank=10 price=0.27 support=0.29 resistance=0.32 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=56.86 liquidity=25227688.0 spike=1.88
- ATLC.CA: score=8.74 buy_ready=False sector_rank=7 price=4.13 support=4.62 resistance=5.44 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=26.53 liquidity=7924632.0 spike=0.96
- ATQA.CA: score=20.35 buy_ready=False sector_rank=9 price=10.07 support=9.41 resistance=10.72 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=36.76 liquidity=32112844.0 spike=0.6
- AXPH.CA: score=6.82 buy_ready=False sector_rank=10 price=809.97 support=908.0 resistance=1239.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=39.7 liquidity=1469577.0 spike=0.25
- BINV.CA: score=18.1 buy_ready=False sector_rank=11 price=37.0 support=38.0 resistance=45.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=69.39 liquidity=24629380.0 spike=2.38
- BIOC.CA: score=8.59 buy_ready=False sector_rank=10 price=63.65 support=67.52 resistance=79.99 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=41.54 liquidity=3246046.0 spike=0.37
- BTFH.CA: score=22.63 buy_ready=False sector_rank=7 price=3.42 support=3.02 resistance=3.32 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=48.0 liquidity=426312576.0 spike=1.91
- CAED.CA: score=9.51 buy_ready=False sector_rank=10 price=66.33 support=61.05 resistance=89.99 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=43.96 liquidity=1165824.0 spike=0.07
- CANA.CA: score=14.21 buy_ready=False sector_rank=13 price=38.55 support=33.0 resistance=38.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=62.07 liquidity=1914543.0 spike=0.13
- CCAP.CA: score=15.34 buy_ready=False sector_rank=11 price=3.76 support=4.47 resistance=5.66 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=62.35 liquidity=339120544.0 spike=0.41
- CCRS.CA: score=13.35 buy_ready=False sector_rank=10 price=1.8 support=1.95 resistance=2.7 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=71.95 liquidity=15364190.0 spike=0.56
- CEFM.CA: score=7.38 buy_ready=False sector_rank=10 price=102.59 support=97.1 resistance=119.9 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=31.34 liquidity=4027551.0 spike=0.51
- CERA.CA: score=11.19 buy_ready=False sector_rank=10 price=1.17 support=1.13 resistance=1.23 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=42.86 liquidity=1837327.0 spike=0.12
- CFGH.CA: score=0.86 buy_ready=False sector_rank=10 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=0.0 liquidity=7091.0 spike=1.75
- CICH.CA: score=9.7 buy_ready=False sector_rank=7 price=9.1 support=10.9 resistance=13.47 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=69.76 liquidity=6108746.0 spike=1.39
- CIEB.CA: score=6.08 buy_ready=False sector_rank=13 price=22.5 support=23.31 resistance=24.8 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=38.85 liquidity=780830.0 spike=0.05
- CIRA.CA: score=-0.58 buy_ready=False sector_rank=21 price=17.37 support=19.16 resistance=28.4 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=76.1 liquidity=1204030.0 spike=0.04
- CLHO.CA: score=14.06 buy_ready=False sector_rank=20 price=13.2 support=14.45 resistance=16.6 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=53.93 liquidity=9078826.0 spike=0.22
- CNFN.CA: score=20.81 buy_ready=False sector_rank=7 price=5.19 support=4.33 resistance=4.95 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=45.83 liquidity=13865195.0 spike=0.93
- COMI.CA: score=9.3 buy_ready=False sector_rank=13 price=103.0 support=131.5 resistance=144.93 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=27.65 liquidity=118840000.0 spike=0.2
- COPR.CA: score=16.35 buy_ready=False sector_rank=10 price=0.36 support=0.29 resistance=0.37 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=76.92 liquidity=20233232.0 spike=0.5
- COSG.CA: score=20.35 buy_ready=False sector_rank=10 price=1.54 support=1.44 resistance=1.65 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=61.29 liquidity=14189483.0 spike=0.3
- CPCI.CA: score=7.13 buy_ready=False sector_rank=10 price=268.8 support=315.1 resistance=383.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=37.53 liquidity=1778627.0 spike=0.2
- CSAG.CA: score=18.24 buy_ready=False sector_rank=5 price=34.86 support=30.05 resistance=32.43 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=39.38 liquidity=7181852.0 spike=0.35
- DAPH.CA: score=20.35 buy_ready=False sector_rank=10 price=88.82 support=79.25 resistance=96.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=38.67 liquidity=31801306.0 spike=0.99
- DEIN.CA: score=6.35 buy_ready=False sector_rank=10 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-05-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=11.39 buy_ready=False sector_rank=19 price=26.25 support=24.5 resistance=26.49 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=54.95 liquidity=1369465.0 spike=0.63
- DSCW.CA: score=9.35 buy_ready=False sector_rank=10 price=1.77 support=1.71 resistance=2.14 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=10.71 liquidity=30192190.0 spike=0.35
- DTPP.CA: score=16.9 buy_ready=False sector_rank=10 price=119.92 support=121.0 resistance=139.7 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=59.0 liquidity=8547515.0 spike=0.88
- EALR.CA: score=8.47 buy_ready=False sector_rank=10 price=373.0 support=330.15 resistance=449.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=29.61 liquidity=3126785.0 spike=0.13
- EASB.CA: score=2.62 buy_ready=False sector_rank=10 price=3.64 support=4.61 resistance=5.37 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=29.51 liquidity=2267647.0 spike=0.49
- EAST.CA: score=14.02 buy_ready=False sector_rank=19 price=37.1 support=36.41 resistance=39.75 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=43.26 liquidity=19699736.0 spike=0.29
- EBSC.CA: score=0.67 buy_ready=False sector_rank=10 price=1.68 support=1.64 resistance=1.9 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=11.11 liquidity=317800.0 spike=0.17
- ECAP.CA: score=22.91 buy_ready=False sector_rank=10 price=31.49 support=27.82 resistance=31.33 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=48.39 liquidity=12657803.0 spike=2.28
- EDFM.CA: score=-0.03 buy_ready=False sector_rank=10 price=309.5 support=320.2 resistance=378.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=18.89 liquidity=622298.0 spike=0.55
- EEII.CA: score=18.95 buy_ready=False sector_rank=10 price=2.33 support=2.27 resistance=2.58 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=43.18 liquidity=27133828.0 spike=1.3
- EFIC.CA: score=10.96 buy_ready=False sector_rank=9 price=224.0 support=195.25 resistance=219.1 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=46.09 liquidity=612487.0 spike=0.12
- EFID.CA: score=17.02 buy_ready=False sector_rank=19 price=27.5 support=27.49 resistance=29.06 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=53.81 liquidity=15353191.0 spike=0.32
- EFIH.CA: score=17.22 buy_ready=False sector_rank=16 price=18.49 support=20.1 resistance=22.83 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=47.26 liquidity=32610652.0 spike=0.53
- EGAL.CA: score=15.35 buy_ready=False sector_rank=9 price=235.5 support=294.5 resistance=344.99 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=61.14 liquidity=56123300.0 spike=0.46
- EGAS.CA: score=7.48 buy_ready=False sector_rank=18 price=44.26 support=45.53 resistance=51.88 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=47.62 liquidity=2400035.0 spike=0.09
- EGBE.CA: score=8.65 buy_ready=False sector_rank=13 price=0.45 support=0.38 resistance=0.47 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=71.28 liquidity=146529.0 spike=1.1
- EGCH.CA: score=16.35 buy_ready=False sector_rank=9 price=12.49 support=11.64 resistance=14.98 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=71.82 liquidity=33835672.0 spike=0.28
- EGSA.CA: score=4.34 buy_ready=False sector_rank=12 price=6.92 support=7.6 resistance=9.19 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=91.62 liquidity=1082.0 spike=0.06
- EGTS.CA: score=10.22 buy_ready=False sector_rank=8 price=8.15 support=12.9 resistance=20.99 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=79.49 liquidity=8477489.0 spike=0.09
- EHDR.CA: score=20.47 buy_ready=False sector_rank=10 price=2.51 support=2.17 resistance=2.44 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=39.29 liquidity=32288416.0 spike=1.06
- EKHO.CA: score=10.08 buy_ready=False sector_rank=18 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-05-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=24.4 buy_ready=False sector_rank=1 price=3.11 support=2.06 resistance=2.26 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=29.17 liquidity=240493456.0 spike=6.16
- ELKA.CA: score=19.35 buy_ready=False sector_rank=10 price=1.19 support=1.1 resistance=1.25 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=44.44 liquidity=15340772.0 spike=0.54
- ELNA.CA: score=12.69 buy_ready=False sector_rank=10 price=40.12 support=37.01 resistance=42.79 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=49.58 liquidity=818253.0 spike=1.76
- ELSH.CA: score=20.35 buy_ready=False sector_rank=10 price=8.37 support=7.54 resistance=8.67 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=63.83 liquidity=13010044.0 spike=0.52
- ELWA.CA: score=4.73 buy_ready=False sector_rank=10 price=1.11 support=1.79 resistance=2.04 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=85.19 liquidity=1386478.0 spike=0.49
- EMFD.CA: score=10.74 buy_ready=False sector_rank=8 price=9.7 support=9.83 resistance=11.39 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=31.18 liquidity=16055408.0 spike=0.15
- ENGC.CA: score=5.59 buy_ready=False sector_rank=10 price=33.24 support=32.31 resistance=35.86 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=33.17 liquidity=2239583.0 spike=0.15
- EOSB.CA: score=5.41 buy_ready=False sector_rank=10 price=1.45 support=1.34 resistance=1.54 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=0.0 liquidity=66794.0 spike=0.43
- EPCO.CA: score=10.36 buy_ready=False sector_rank=10 price=6.76 support=8.56 resistance=9.9 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=45.11 liquidity=6015859.0 spike=0.45
- EPPK.CA: score=5.79 buy_ready=False sector_rank=10 price=11.79 support=12.01 resistance=13.6 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=50.27 liquidity=444183.0 spike=0.66
- ETEL.CA: score=14.34 buy_ready=False sector_rank=12 price=65.77 support=91.0 resistance=101.89 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=41.52 liquidity=45953328.0 spike=0.4
- ETRS.CA: score=22.95 buy_ready=False sector_rank=10 price=8.05 support=7.37 resistance=8.18 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=59.06 liquidity=42519444.0 spike=1.3
- EXPA.CA: score=14.3 buy_ready=False sector_rank=13 price=15.4 support=17.31 resistance=21.18 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=54.02 liquidity=16824208.0 spike=0.4
- FAIT.CA: score=7.78 buy_ready=False sector_rank=13 price=32.07 support=33.0 resistance=38.48 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=70.96 liquidity=2479647.0 spike=0.34
- FAITA.CA: score=8.32 buy_ready=False sector_rank=13 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=57.14 liquidity=23606.0 spike=0.4
- FERC.CA: score=9.61 buy_ready=False sector_rank=9 price=82.52 support=77.0 resistance=83.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=31.83 liquidity=4265073.0 spike=0.42
- FWRY.CA: score=14.22 buy_ready=False sector_rank=16 price=16.12 support=19.0 resistance=21.66 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=38.64 liquidity=46199224.0 spike=0.18
- GBCO.CA: score=19.07 buy_ready=False sector_rank=4 price=27.0 support=25.25 resistance=29.5 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=35.34 liquidity=57489240.0 spike=0.51
- GDWA.CA: score=4.33 buy_ready=False sector_rank=10 price=0.78 support=0.77 resistance=0.84 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=25.81 liquidity=4978343.0 spike=0.41
- GGCC.CA: score=1.28 buy_ready=False sector_rank=10 price=0.41 support=0.39 resistance=0.43 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=27.59 liquidity=1934873.0 spike=0.36
- GIHD.CA: score=22.81 buy_ready=False sector_rank=10 price=43.82 support=39.1 resistance=44.5 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=37.68 liquidity=12485290.0 spike=2.23
- GMCI.CA: score=4.45 buy_ready=False sector_rank=10 price=1.71 support=1.67 resistance=1.8 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=81.82 liquidity=101301.0 spike=0.31
- GRCA.CA: score=3.83 buy_ready=False sector_rank=10 price=30.09 support=52.51 resistance=60.95 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=69.29 liquidity=1486856.0 spike=0.16
- GSSC.CA: score=1.15 buy_ready=False sector_rank=10 price=240.11 support=254.1 resistance=277.77 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=7.61 liquidity=1804549.0 spike=0.09
- GTWL.CA: score=8.87 buy_ready=False sector_rank=10 price=47.82 support=45.7 resistance=59.79 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=20.05 liquidity=5518615.0 spike=0.45
- HDBK.CA: score=19.3 buy_ready=False sector_rank=13 price=89.66 support=140.0 resistance=154.99 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=40.51 liquidity=473890400.0 spike=20.8
- HELI.CA: score=14.74 buy_ready=False sector_rank=8 price=3.6 support=5.79 resistance=6.72 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=47.84 liquidity=57334288.0 spike=0.28
- HRHO.CA: score=9.81 buy_ready=False sector_rank=7 price=24.92 support=26.16 resistance=30.05 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=15.15 liquidity=49913468.0 spike=0.23
- ICID.CA: score=27.35 buy_ready=False sector_rank=10 price=4.68 support=4.3 resistance=5.07 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=69.18 liquidity=34468940.0 spike=5.42
- IDRE.CA: score=18.35 buy_ready=False sector_rank=10 price=40.71 support=37.62 resistance=49.6 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=62.33 liquidity=11283737.0 spike=0.34
- IFAP.CA: score=9.24 buy_ready=False sector_rank=15 price=18.85 support=19.51 resistance=22.2 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=22.9 liquidity=11728377.0 spike=0.49
- INFI.CA: score=16.13 buy_ready=False sector_rank=10 price=127.0 support=95.7 resistance=112.5 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=50.13 liquidity=5779083.0 spike=0.27
- IRON.CA: score=16.82 buy_ready=False sector_rank=9 price=35.01 support=31.83 resistance=35.08 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=46.14 liquidity=6473015.0 spike=0.67
- ISMA.CA: score=10.23 buy_ready=False sector_rank=10 price=13.8 support=18.59 resistance=27.9 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=93.18 liquidity=6880648.0 spike=0.13
- ISMQ.CA: score=16.21 buy_ready=False sector_rank=9 price=7.03 support=7.26 resistance=7.94 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=36.11 liquidity=70272056.0 spike=1.43
- ISPH.CA: score=14.98 buy_ready=False sector_rank=20 price=11.72 support=10.6 resistance=12.25 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=32.5 liquidity=32849440.0 spike=0.29
- JUFO.CA: score=14.02 buy_ready=False sector_rank=19 price=25.28 support=26.51 resistance=29.95 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=40.29 liquidity=43754036.0 spike=0.85
- KABO.CA: score=26.4 buy_ready=False sector_rank=3 price=6.4 support=5.92 resistance=6.3 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=54.69 liquidity=12369860.0 spike=0.86
- KWIN.CA: score=7.83 buy_ready=False sector_rank=10 price=73.33 support=69.0 resistance=90.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=23.85 liquidity=4480919.0 spike=0.56
- KZPC.CA: score=7.82 buy_ready=False sector_rank=10 price=10.2 support=10.16 resistance=11.6 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=43.78 liquidity=3472665.0 spike=0.25
- LCSW.CA: score=10.81 buy_ready=False sector_rank=14 price=25.58 support=25.93 resistance=29.29 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=59.0 liquidity=6548993.0 spike=0.38
- LUTS.CA: score=8.04 buy_ready=False sector_rank=10 price=0.56 support=0.54 resistance=0.59 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=48.61 liquidity=689838.0 spike=0.1
- MAAL.CA: score=15.69 buy_ready=False sector_rank=10 price=4.22 support=4.44 resistance=5.17 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=79.12 liquidity=11487554.0 spike=1.67
- MASR.CA: score=14.35 buy_ready=False sector_rank=10 price=4.23 support=5.95 resistance=7.34 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=53.82 liquidity=21007516.0 spike=0.29
- MBSC.CA: score=18.17 buy_ready=False sector_rank=14 price=267.01 support=258.5 resistance=295.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=60.65 liquidity=9904248.0 spike=0.21
- MCQE.CA: score=18.24 buy_ready=False sector_rank=14 price=170.98 support=185.12 resistance=201.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=56.18 liquidity=49689096.0 spike=2.49
- MCRO.CA: score=21.35 buy_ready=False sector_rank=10 price=1.27 support=1.18 resistance=1.4 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=40.91 liquidity=40912416.0 spike=0.38
- MENA.CA: score=8.5 buy_ready=False sector_rank=8 price=4.79 support=5.62 resistance=6.8 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=64.8 liquidity=1760335.0 spike=0.19
- MEPA.CA: score=12.16 buy_ready=False sector_rank=10 price=1.7 support=1.62 resistance=1.84 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=37.5 liquidity=3816512.0 spike=0.14
- MFPC.CA: score=14.35 buy_ready=False sector_rank=9 price=30.5 support=43.0 resistance=47.94 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=51.26 liquidity=11236114.0 spike=0.08
- MFSC.CA: score=5.42 buy_ready=False sector_rank=10 price=34.05 support=31.9 resistance=65.6 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=73.84 liquidity=68441.0 spike=0.01
- MHOT.CA: score=7.56 buy_ready=False sector_rank=17 price=25.9 support=26.3 resistance=34.3 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=64.75 liquidity=442410.0 spike=0.03
- MICH.CA: score=7.35 buy_ready=False sector_rank=10 price=28.98 support=34.96 resistance=38.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=53.39 liquidity=3005080.0 spike=0.36
- MILS.CA: score=16.52 buy_ready=False sector_rank=10 price=129.38 support=109.0 resistance=153.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=48.83 liquidity=8168110.0 spike=0.29
- MIPH.CA: score=-0.29 buy_ready=False sector_rank=20 price=347.02 support=630.1 resistance=772.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=28.13 liquidity=728225.0 spike=0.13
- MOED.CA: score=4.79 buy_ready=False sector_rank=10 price=0.72 support=0.68 resistance=0.84 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=16.56 liquidity=5439314.0 spike=0.41
- MOIL.CA: score=15.65 buy_ready=False sector_rank=18 price=0.48 support=0.43 resistance=0.47 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=62.5 liquidity=566258.0 spike=3.75
- MOIN.CA: score=13.38 buy_ready=False sector_rank=10 price=30.43 support=23.13 resistance=26.49 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=63.85 liquidity=1030296.0 spike=0.27
- MOSC.CA: score=3.52 buy_ready=False sector_rank=10 price=181.89 support=271.0 resistance=340.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=21.41 liquidity=4168233.0 spike=0.11
- MPCI.CA: score=14.35 buy_ready=False sector_rank=10 price=156.2 support=171.52 resistance=224.88 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=59.8 liquidity=73635400.0 spike=0.77
- MPCO.CA: score=17.24 buy_ready=False sector_rank=15 price=1.62 support=1.54 resistance=1.78 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=46.67 liquidity=26778606.0 spike=0.68
- MPRC.CA: score=11.39 buy_ready=False sector_rank=10 price=28.5 support=30.01 resistance=33.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=44.09 liquidity=7044473.0 spike=0.47
- MTIE.CA: score=15.61 buy_ready=False sector_rank=4 price=7.2 support=8.44 resistance=10.38 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=39.26 liquidity=41006252.0 spike=1.27
- NAHO.CA: score=4.35 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=44.44 liquidity=1211.0 spike=0.03
- NCCW.CA: score=24.75 buy_ready=False sector_rank=10 price=6.12 support=5.13 resistance=5.78 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=35.96 liquidity=41513460.0 spike=3.2
- NEDA.CA: score=5.31 buy_ready=False sector_rank=10 price=2.38 support=2.65 resistance=3.19 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=53.57 liquidity=963100.0 spike=0.71
- NHPS.CA: score=7.98 buy_ready=False sector_rank=10 price=76.37 support=67.56 resistance=80.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=28.95 liquidity=2630641.0 spike=0.19
- NINH.CA: score=10.79 buy_ready=False sector_rank=10 price=10.3 support=17.53 resistance=25.89 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=46.2 liquidity=6443652.0 spike=0.28
- NIPH.CA: score=8.98 buy_ready=False sector_rank=20 price=100.22 support=128.04 resistance=186.89 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=34.58 liquidity=18710334.0 spike=0.14
- OBRI.CA: score=15.35 buy_ready=False sector_rank=10 price=38.16 support=34.71 resistance=40.84 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=10.82 liquidity=10519077.0 spike=0.79
- OCDI.CA: score=9.74 buy_ready=False sector_rank=8 price=17.93 support=20.19 resistance=23.67 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=30.48 liquidity=11843437.0 spike=0.26
- OCPH.CA: score=0.91 buy_ready=False sector_rank=10 price=204.99 support=334.22 resistance=416.5 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=21.6 liquidity=1566068.0 spike=0.06
- ODIN.CA: score=15.37 buy_ready=False sector_rank=10 price=2.25 support=1.89 resistance=2.07 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=42.86 liquidity=5018488.0 spike=0.48
- OFH.CA: score=13.35 buy_ready=False sector_rank=10 price=0.62 support=0.6 resistance=0.65 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=32.35 liquidity=12208500.0 spike=0.63
- OIH.CA: score=18.34 buy_ready=False sector_rank=11 price=1.47 support=1.44 resistance=1.66 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=37.5 liquidity=38583204.0 spike=0.26
- OLFI.CA: score=7.89 buy_ready=False sector_rank=19 price=24.99 support=21.0 resistance=22.9 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=33.66 liquidity=2862082.0 spike=0.11
- ORAS.CA: score=25.4 buy_ready=False sector_rank=2 price=430.0 support=71.05 resistance=71.05 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=50.0 liquidity=111898008.0 spike=1.0
- ORHD.CA: score=16.74 buy_ready=False sector_rank=8 price=25.4 support=30.15 resistance=37.88 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=70.84 liquidity=28849162.0 spike=0.14
- ORWE.CA: score=26.4 buy_ready=False sector_rank=3 price=23.25 support=21.43 resistance=22.69 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=59.23 liquidity=16191202.0 spike=0.38
- PHAR.CA: score=9.98 buy_ready=False sector_rank=20 price=77.5 support=83.96 resistance=92.4 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=27.46 liquidity=16728426.0 spike=0.59
- PHDC.CA: score=18.74 buy_ready=False sector_rank=8 price=8.61 support=11.27 resistance=15.25 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=59.95 liquidity=72670040.0 spike=0.17
- PHTV.CA: score=5.61 buy_ready=False sector_rank=10 price=175.24 support=201.08 resistance=233.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=59.91 liquidity=263317.0 spike=0.01
- POUL.CA: score=18.02 buy_ready=False sector_rank=19 price=25.75 support=33.8 resistance=39.17 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=64.63 liquidity=17500206.0 spike=0.28
- PRCL.CA: score=12.49 buy_ready=False sector_rank=14 price=16.1 support=18.78 resistance=24.43 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=39.75 liquidity=7223686.0 spike=0.23
- PRDC.CA: score=15.74 buy_ready=False sector_rank=8 price=4.35 support=4.96 resistance=6.09 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=47.52 liquidity=17137188.0 spike=0.95
- PRMH.CA: score=19.35 buy_ready=False sector_rank=10 price=1.59 support=2.05 resistance=2.35 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=61.11 liquidity=124150192.0 spike=11.37
- RACC.CA: score=14.35 buy_ready=False sector_rank=10 price=8.39 support=9.28 resistance=12.02 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=42.78 liquidity=11341669.0 spike=0.31
- RAKT.CA: score=-0.41 buy_ready=False sector_rank=10 price=22.8 support=22.1 resistance=26.1 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=26.61 liquidity=246161.0 spike=0.7
- RAYA.CA: score=14.92 buy_ready=False sector_rank=6 price=3.46 support=6.2 resistance=8.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=55.45 liquidity=77725800.0 spike=0.61
- RMDA.CA: score=13.98 buy_ready=False sector_rank=20 price=3.33 support=4.36 resistance=5.22 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=52.05 liquidity=24752992.0 spike=0.4
- ROTO.CA: score=20.35 buy_ready=False sector_rank=10 price=36.33 support=32.66 resistance=36.69 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=41.03 liquidity=11049509.0 spike=0.81
- RREI.CA: score=11.03 buy_ready=False sector_rank=10 price=2.94 support=3.32 resistance=3.86 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=21.21 liquidity=34382884.0 spike=1.34
- RTVC.CA: score=9.03 buy_ready=False sector_rank=10 price=3.79 support=3.75 resistance=4.4 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=31.46 liquidity=8478855.0 spike=1.1
- RUBX.CA: score=4.03 buy_ready=False sector_rank=10 price=10.24 support=9.8 resistance=11.98 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=31.49 liquidity=1682369.0 spike=0.05
- SAUD.CA: score=3.06 buy_ready=False sector_rank=13 price=15.39 support=21.8 resistance=25.1 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=28.9 liquidity=3755838.0 spike=0.25
- SCEM.CA: score=18.26 buy_ready=False sector_rank=14 price=62.25 support=58.71 resistance=72.2 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=58.19 liquidity=40225284.0 spike=0.93
- SCFM.CA: score=13.35 buy_ready=False sector_rank=10 price=263.1 support=240.2 resistance=315.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=28.98 liquidity=11402460.0 spike=0.38
- SCTS.CA: score=5.0 buy_ready=False sector_rank=21 price=294.0 support=590.01 resistance=709.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=52.15 liquidity=1779686.0 spike=0.09
- SDTI.CA: score=14.35 buy_ready=False sector_rank=10 price=25.61 support=43.15 resistance=46.25 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=53.83 liquidity=16884766.0 spike=0.73
- SEIG.CA: score=9.21 buy_ready=False sector_rank=10 price=172.81 support=173.35 resistance=207.99 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=44.25 liquidity=866985.0 spike=0.12
- SIPC.CA: score=20.35 buy_ready=False sector_rank=10 price=3.72 support=3.4 resistance=3.8 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=31.71 liquidity=162426640.0 spike=11.14
- SKPC.CA: score=20.35 buy_ready=False sector_rank=9 price=19.6 support=16.8 resistance=18.98 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=44.75 liquidity=25652360.0 spike=0.19
- SMFR.CA: score=5.71 buy_ready=False sector_rank=10 price=191.85 support=199.9 resistance=239.9 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=48.77 liquidity=361636.0 spike=0.03
- SNFC.CA: score=13.35 buy_ready=False sector_rank=10 price=10.3 support=11.64 resistance=12.79 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=69.23 liquidity=10547929.0 spike=0.4
- SPIN.CA: score=9.42 buy_ready=False sector_rank=3 price=9.99 support=13.69 resistance=15.2 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=49.37 liquidity=3024128.0 spike=0.63
- SPMD.CA: score=24.61 buy_ready=False sector_rank=10 price=0.43 support=0.38 resistance=0.43 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=60.47 liquidity=31287526.0 spike=1.13
- SUGR.CA: score=5.86 buy_ready=False sector_rank=19 price=47.19 support=47.0 resistance=52.9 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=46.53 liquidity=1831162.0 spike=0.11
- SVCE.CA: score=18.63 buy_ready=False sector_rank=10 price=8.6 support=7.29 resistance=10.15 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=63.33 liquidity=206264256.0 spike=1.14
- SWDY.CA: score=18.4 buy_ready=False sector_rank=1 price=78.25 support=86.01 resistance=93.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=36.99 liquidity=35265068.0 spike=0.72
- TALM.CA: score=8.97 buy_ready=False sector_rank=21 price=15.5 support=15.12 resistance=17.27 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=38.41 liquidity=1752234.0 spike=0.14
- TMGH.CA: score=15.74 buy_ready=False sector_rank=8 price=80.0 support=91.87 resistance=101.4 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=39.21 liquidity=238304896.0 spike=0.41
- TRTO.CA: score=6.35 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=50.0 liquidity=374.0 spike=0.28
- UEFM.CA: score=0.02 buy_ready=False sector_rank=10 price=479.0 support=455.6 resistance=530.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=10.22 liquidity=670513.0 spike=0.32
- UEGC.CA: score=10.35 buy_ready=False sector_rank=10 price=1.34 support=1.3 resistance=1.43 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=18.18 liquidity=10424904.0 spike=0.65
- UNIP.CA: score=10.51 buy_ready=False sector_rank=10 price=0.29 support=0.28 resistance=0.3 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=46.87 liquidity=3158031.0 spike=0.37
- UNIT.CA: score=5.57 buy_ready=False sector_rank=8 price=10.68 support=10.06 resistance=14.4 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=65.87 liquidity=1823622.0 spike=0.29
- WCDF.CA: score=0.11 buy_ready=False sector_rank=10 price=483.0 support=530.26 resistance=570.0 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=10.69 liquidity=758574.0 spike=0.91
- WKOL.CA: score=8.43 buy_ready=False sector_rank=10 price=313.07 support=279.7 resistance=364.6 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=21.67 liquidity=3077300.0 spike=0.18
- ZEOT.CA: score=15.29 buy_ready=False sector_rank=10 price=8.63 support=8.43 resistance=9.7 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=23.13 liquidity=34749052.0 spike=3.47
- ZMID.CA: score=18.74 buy_ready=False sector_rank=8 price=5.74 support=5.77 resistance=6.57 source=Yahoo Finance history + DirectFN delayed current liquidity as_of=2026-06-01T23:18:29.806063+00:00 freshness=DELAYED_CURRENT RSI=49.61 liquidity=45971304.0 spike=0.27

## Backtesting Lite
- ICID.CA: 180d return=29.23%, max drawdown=-24.79%, MA20>MA50 days last20=20, as_of=2026-05-27T21:00:00+00:00
- KABO.CA: 180d return=18.18%, max drawdown=-24.26%, MA20>MA50 days last20=20, as_of=2026-05-27T21:00:00+00:00
- ORWE.CA: 180d return=11.5%, max drawdown=-13.64%, MA20>MA50 days last20=20, as_of=2026-05-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ICID.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=International Co. For Investment & Development summary=ICID stock targets higher levels after breaking EGP 4.10; International Company for Investment reports EGP 13m in 9M-25 consolidated net profits; ICID to sell land plot for EGP 4.39m
  - ICID stock targets higher levels after breaking EGP 4.10: https://english.mubasher.info/news/4595529/ICID-stock-targets-higher-levels-after-breaking-EGP-4-10/
  - International Company for Investment reports EGP 13m in 9M-25 consolidated net profits: https://english.mubasher.info/news/4530420/International-Company-for-Investment-reports-EGP-13m-in-9M-25-consolidated-net-profits/
  - ICID to sell land plot for EGP 4.39m: https://english.mubasher.info/news/4013131/ICID-to-sell-land-plot-for-EGP-4-39m/
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=516 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- ORAS.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=516 sources=3 expected=Orascom Construction summary=Orascom Construction’s consolidated backlog hits $9.3bn in Q1-26; Orascom Construction’s standalone net losses widen to nearly $23m in 2025; Dual-listed Orascom Construction to develop wind farm in Egypt under BOO model
  - Orascom Construction’s consolidated backlog hits $9.3bn in Q1-26: https://english.mubasher.info/news/4613299/Orascom-Construction-s-consolidated-backlog-hits-9-3bn-in-Q1-26/
  - Orascom Construction’s standalone net losses widen to nearly $23m in 2025: https://english.mubasher.info/news/4588683/Orascom-Construction-s-standalone-net-losses-widen-to-nearly-23m-in-2025/
  - Dual-listed Orascom Construction to develop wind farm in Egypt under BOO model: https://english.mubasher.info/news/4581024/Dual-listed-Orascom-Construction-to-develop-wind-farm-in-Egypt-under-BOO-model/
- NCCW.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Nasr Company for Civil Works summary=Nasr for Civil Works unveils EGP 150m capital increase; Arabia Investments, Nasr Company for Civil Works unveil capital hike; Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda
  - Nasr for Civil Works unveils EGP 150m capital increase: https://english.mubasher.info/news/4550493/Nasr-for-Civil-Works-unveils-EGP-150m-capital-increase/
  - Arabia Investments, Nasr Company for Civil Works unveil capital hike: https://english.mubasher.info/news/4284206/Arabia-Investments-Nasr-Company-for-Civil-Works-unveil-capital-hike/
  - Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda: https://english.mubasher.info/news/4249759/Nasr-Company-for-Civil-Works-consortium-signs-EUR-46m-agreement-with-Uganda/
- SPMD.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Speed Medical Co summary=Speed Medical’s stock reflects strong technical breakthrough; Speed Medical turns to losses in 9M-22; Shareholder ups stake in Speed Medical for EGP 3.5m
  - Speed Medical’s stock reflects strong technical breakthrough: https://english.mubasher.info/news/4546374/Speed-Medical-s-stock-reflects-strong-technical-breakthrough/
  - Speed Medical turns to losses in 9M-22: https://english.mubasher.info/news/4054471/Speed-Medical-turns-to-losses-in-9M-22/
  - Shareholder ups stake in Speed Medical for EGP 3.5m: https://english.mubasher.info/news/4049449/Shareholder-ups-stake-in-Speed-Medical-for-EGP-3-5m/
- ELEC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=516 sources=3 expected=Electro Cable Egypt summary=Electro Cable Egypt sees lower profits in 2025; revenues exceed EGP 10.8bn; Mashareq reduces equity in Electro Cable Egypt to 0.77%; Electro Cable Egypt stock is testing significant demand zone, will it succeed to rebound?
  - Electro Cable Egypt sees lower profits in 2025; revenues exceed EGP 10.8bn: https://english.mubasher.info/news/4580607/Electro-Cable-Egypt-sees-lower-profits-in-2025-revenues-exceed-EGP-10-8bn/
  - Mashareq reduces equity in Electro Cable Egypt to 0.77%: https://english.mubasher.info/news/4561520/Mashareq-reduces-equity-in-Electro-Cable-Egypt-to-0-77-/
  - Electro Cable Egypt stock is testing significant demand zone, will it succeed to rebound?: https://english.mubasher.info/news/4556412/Electro-Cable-Egypt-stock-is-testing-significant-demand-zone-will-it-succeed-to-rebound-/
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/

## Warnings
- Evidence for ICID.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ORAS.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for NCCW.CA matches the company but no source/report date was detected.
- Evidence for SPMD.CA matches the company but no source/report date was detected.
- Evidence for ELEC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
