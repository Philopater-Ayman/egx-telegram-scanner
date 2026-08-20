# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-20T08:35:48.057495+00:00
Generated Cairo: 2026-08-20 11:35
Run timing: target 11:00 Cairo | generated Cairo 2026-08-20 11:35 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-20 11:30

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 144/189
- Top sector: Education

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, August 20
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 55.56% / above MA50 61.11%
- EGX70 regime: MIXED / above MA20 51.43% / above MA50 82.86%
- Sector breadth: 28.57%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- GTWL.CA: liquidity=156143792.0 spike=1.06 score=5.25
- LUTS.CA: liquidity=143206080.0 spike=1.55 score=6.23
- COMI.CA: liquidity=120312728.0 spike=0.27 score=19.4
- ZMID.CA: liquidity=92585280.0 spike=0.41 score=4.88
- AMES.CA: liquidity=69220088.0 spike=1.15 score=5.43

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flags EGX30 as constructive and EGX70 as mixed with sector breadth at 28.6%, triggering a defensive risk mode that blocks new buys; top-ranked tickets are kept HOLD despite bullish watch outlooks due to cooling liquidity and extended momentum.
- Top tickets (CCAP.CA, SCEM.CA, ETEL.CA) scored highest on rank_score and show BULLISH_WATCH/CONSTRUCTIVE outlooks, but liquidity is cooling and momentum is extended, so the scanner maintains a HOLD stance.
- Sector breadth is weak (28.6%) with leading sectors Education, Building Materials, Investment Holding; most stocks sit 6‑34% above 20‑day support and near resistance, limiting near‑term upside.
- EGX30’s constructive trend (55% above MA20) contrasts with EGX70’s mixed trend (negative 5‑day return), shifting the risk mode to DEFENSIVE_NO_NEW_BUY and restricting new entries.
- Uncertainty persists: some stocks display overheated RSI and liquidity spikes while sector fundamentals remain soft, making short‑term direction unclear.

## Top Liquidity Spikes
- NAHO.CA: spike=4.71 liquidity=323944.49 outlook=WEAK_OR_RISKY score=31.82 buy_ready=False
- AXPH.CA: spike=4.44 liquidity=18100936.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TRTO.CA: spike=4.2 liquidity=37730.25 outlook=NEUTRAL score=47.82 buy_ready=False
- KZPC.CA: spike=4.14 liquidity=64237088.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- FAITA.CA: spike=3.13 liquidity=177889.0 outlook=NEUTRAL score=44.84 buy_ready=False

## Sector Leaderboard
- #1 Education: score=9.84 5d=0.0% 20d=18.85% aboveMA50=100.0%
- #2 Building Materials: score=8.56 5d=-0.87% 20d=21.54% aboveMA50=83.33%
- #3 Investment Holding: score=8.07 5d=5.85% 20d=2.22% aboveMA50=100.0%
- #4 Basic Resources & Chemicals: score=7.55 5d=3.55% 20d=5.67% aboveMA50=90.0%
- #5 Agriculture & Food Production: score=7.41 5d=-1.35% 20d=16.25% aboveMA50=100.0%
- #6 Banking & Financials: score=6.84 5d=1.62% 20d=7.58% aboveMA50=80.0%
- #7 Transportation & Logistics: score=6.55 5d=-0.67% 20d=10.94% aboveMA50=100.0%
- #8 Telecommunications: score=6.4 5d=3.66% 20d=7.38% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CIRA.CA: BULLISH_WATCH score=89.84 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CCAP.CA: BULLISH_WATCH score=88.07 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- GSSC.CA: BULLISH_WATCH score=81.82 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- PHTV.CA: BULLISH_WATCH score=76.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- MCQE.CA: BULLISH_WATCH score=76.56 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- CLHO.CA: BULLISH_WATCH score=76.31 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- BINV.CA: BULLISH_WATCH score=76.07 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- SCFM.CA: BULLISH_WATCH score=73.82 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- WKOL.CA: BULLISH_WATCH score=73.82 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- EBSC.CA: BULLISH_WATCH score=72.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=14.78 buy_ready=False sector_rank=14 price=336.35 support=234.05 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=69.9 liquidity=4650239.0 spike=0.08
- ABUK.CA: score=18.4 buy_ready=False sector_rank=4 price=75.64 support=70.6 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=76.55 liquidity=11939783.0 spike=0.1
- ACAMD.CA: score=11.31 buy_ready=False sector_rank=14 price=2.16 support=2.16 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=37.88 liquidity=6182732.0 spike=0.1
- ACGC.CA: score=10.55 buy_ready=False sector_rank=13 price=12.95 support=13.1 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5871886.5 spike=1.0
- ADCI.CA: score=14.18 buy_ready=False sector_rank=14 price=288.51 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=60.31 liquidity=2052461.25 spike=0.09
- ADIB.CA: score=19.96 buy_ready=False sector_rank=6 price=53.74 support=46.99 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=72.18 liquidity=8562763.0 spike=0.08
- ADPC.CA: score=5.13 buy_ready=False sector_rank=14 price=3.97 support=3.93 resistance=4.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11932008.0 spike=0.24
- AFDI.CA: score=10.83 buy_ready=False sector_rank=14 price=59.83 support=47.03 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=68.96 liquidity=701456.94 spike=0.03
- AFMC.CA: score=20.13 buy_ready=False sector_rank=14 price=241.28 support=97.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=70.93 liquidity=19833308.0 spike=0.11
- AJWA.CA: score=16.82 buy_ready=False sector_rank=14 price=194.46 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=60.17 liquidity=2696281.25 spike=0.06
- ALCN.CA: score=11.83 buy_ready=False sector_rank=7 price=30.48 support=28.8 resistance=32.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=66.17 liquidity=2425868.25 spike=0.11
- ALUM.CA: score=-3.58 buy_ready=False sector_rank=14 price=27.04 support=27.01 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1289269.0 spike=0.06
- AMER.CA: score=4.88 buy_ready=False sector_rank=15 price=5.94 support=5.92 resistance=6.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11773221.0 spike=0.1
- AMES.CA: score=5.43 buy_ready=False sector_rank=14 price=160.25 support=149.1 resistance=167.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69220088.0 spike=1.15
- AMIA.CA: score=14.12 buy_ready=False sector_rank=14 price=15.93 support=10.1 resistance=17.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=93.6 liquidity=4994535.5 spike=0.15
- AMOC.CA: score=20.4 buy_ready=False sector_rank=9 price=11.26 support=8.16 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=87.61 liquidity=14347645.0 spike=0.11
- APSW.CA: score=13.23 buy_ready=False sector_rank=14 price=8.74 support=8.6 resistance=9.39 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=46.38 liquidity=3520498.13 spike=2.29
- ARAB.CA: score=9.79 buy_ready=False sector_rank=15 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=46.87 liquidity=1914507.75 spike=0.02
- ARCC.CA: score=16.2 buy_ready=False sector_rank=2 price=72.91 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=82.5 liquidity=5796063.0 spike=0.06
- AREH.CA: score=9.53 buy_ready=False sector_rank=14 price=1.49 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=62.22 liquidity=2403186.75 spike=0.07
- ARVA.CA: score=5.13 buy_ready=False sector_rank=14 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=10.49 buy_ready=False sector_rank=14 price=62.63 support=60.63 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=48.56 liquidity=2360654.0 spike=0.04
- ASPI.CA: score=-0.83 buy_ready=False sector_rank=14 price=0.51 support=0.5 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4042759.75 spike=0.09
- ATLC.CA: score=10.59 buy_ready=False sector_rank=18 price=5.27 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=1050249.25 spike=0.05
- ATQA.CA: score=20.12 buy_ready=False sector_rank=4 price=10.92 support=9.6 resistance=11.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=79.82 liquidity=9721778.0 spike=0.14
- AXPH.CA: score=10.13 buy_ready=False sector_rank=14 price=1588.93 support=1362.0 resistance=1630.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18100936.0 spike=4.44
- BINV.CA: score=14.43 buy_ready=False sector_rank=3 price=47.97 support=46.01 resistance=50.9 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=55.14 liquidity=4034181.16 spike=0.76
- BIOC.CA: score=5.13 buy_ready=False sector_rank=14 price=469.06 support=460.0 resistance=480.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16204716.0 spike=0.07
- BTFH.CA: score=13.54 buy_ready=False sector_rank=18 price=3.0 support=3.05 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=51807508.0 spike=0.23
- CAED.CA: score=5.13 buy_ready=False sector_rank=14 price=173.63 support=165.01 resistance=181.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15322223.0 spike=0.23
- CANA.CA: score=10.94 buy_ready=False sector_rank=6 price=41.56 support=36.05 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=78.13 liquidity=2540039.5 spike=0.12
- CCAP.CA: score=26.4 buy_ready=False sector_rank=3 price=5.45 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=42363472.0 spike=0.07
- CCRS.CA: score=6.89 buy_ready=False sector_rank=14 price=2.41 support=2.44 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=1763306.0 spike=0.1
- CEFM.CA: score=5.13 buy_ready=False sector_rank=14 price=155.73 support=147.51 resistance=161.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12170700.0 spike=0.34
- CERA.CA: score=7.53 buy_ready=False sector_rank=14 price=1.26 support=1.25 resistance=1.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2405251.0 spike=0.12
- CFGH.CA: score=13.15 buy_ready=False sector_rank=14 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=58951.25 spike=2.98
- CICH.CA: score=2.9 buy_ready=False sector_rank=18 price=12.08 support=11.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=65.24 liquidity=361580.06 spike=0.05
- CIEB.CA: score=13.02 buy_ready=False sector_rank=6 price=24.33 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=1619998.13 spike=0.12
- CIRA.CA: score=17.17 buy_ready=False sector_rank=1 price=37.52 support=31.35 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=56.01 liquidity=2773389.25 spike=0.05
- CLHO.CA: score=21.12 buy_ready=False sector_rank=12 price=17.45 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=40227452.0 spike=0.72
- CNFN.CA: score=8.26 buy_ready=False sector_rank=18 price=4.8 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=724777.81 spike=0.04
- COMI.CA: score=19.4 buy_ready=False sector_rank=6 price=136.7 support=136.7 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=120312728.0 spike=0.27
- COPR.CA: score=19.13 buy_ready=False sector_rank=14 price=0.5 support=0.38 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=85.53 liquidity=23196394.0 spike=0.41
- COSG.CA: score=14.65 buy_ready=False sector_rank=14 price=1.76 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=67.44 liquidity=4526397.0 spike=0.1
- CPCI.CA: score=14.53 buy_ready=False sector_rank=14 price=560.98 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=72.55 liquidity=4398026.0 spike=0.5
- CSAG.CA: score=13.2 buy_ready=False sector_rank=7 price=38.5 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=74.6 liquidity=1801682.5 spike=0.07
- DAPH.CA: score=-0.06 buy_ready=False sector_rank=14 price=119.0 support=115.8 resistance=122.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4810206.5 spike=0.12
- DEIN.CA: score=-4.87 buy_ready=False sector_rank=14 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=10.41 buy_ready=False sector_rank=10 price=28.02 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=66.71 liquidity=1081577.13 spike=0.07
- DSCW.CA: score=18.13 buy_ready=False sector_rank=14 price=1.95 support=1.89 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=16135639.0 spike=0.16
- DTPP.CA: score=15.1 buy_ready=False sector_rank=14 price=294.21 support=222.0 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=70.26 liquidity=4969285.0 spike=0.08
- EALR.CA: score=14.66 buy_ready=False sector_rank=14 price=408.28 support=360.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=2528711.5 spike=0.05
- EASB.CA: score=8.82 buy_ready=False sector_rank=14 price=7.31 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=49.47 liquidity=687552.88 spike=0.07
- EAST.CA: score=7.8 buy_ready=False sector_rank=10 price=36.05 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=475201.88 spike=0.01
- EBSC.CA: score=17.53 buy_ready=False sector_rank=14 price=1.92 support=1.85 resistance=2.06 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=8117930.7 spike=1.64
- ECAP.CA: score=-4.24 buy_ready=False sector_rank=14 price=35.62 support=35.0 resistance=37.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=628115.19 spike=0.05
- EDFM.CA: score=7.48 buy_ready=False sector_rank=14 price=414.74 support=352.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=80.52 liquidity=355183.63 spike=0.06
- EEII.CA: score=17.23 buy_ready=False sector_rank=14 price=3.13 support=2.54 resistance=3.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=73.73 liquidity=5102231.0 spike=0.24
- EFIC.CA: score=16.71 buy_ready=False sector_rank=4 price=217.46 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=67.36 liquidity=5305338.5 spike=0.12
- EFID.CA: score=13.64 buy_ready=False sector_rank=10 price=31.74 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=87.63 liquidity=5316927.0 spike=0.06
- EFIH.CA: score=21.18 buy_ready=False sector_rank=11 price=24.11 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=65.16 liquidity=17039088.0 spike=0.15
- EGAL.CA: score=20.4 buy_ready=False sector_rank=4 price=328.46 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=83.84 liquidity=18863618.0 spike=0.18
- EGAS.CA: score=10.6 buy_ready=False sector_rank=9 price=57.23 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=74.56 liquidity=1199118.0 spike=0.05
- EGBE.CA: score=14.16 buy_ready=False sector_rank=6 price=0.52 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=62.43 liquidity=398400.72 spike=2.18
- EGCH.CA: score=18.0 buy_ready=False sector_rank=4 price=13.84 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=9597264.0 spike=0.08
- EGSA.CA: score=1.41 buy_ready=False sector_rank=8 price=8.7 support=8.65 resistance=9.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 12:46 PM market time freshness=DELAYED_CURRENT RSI=30.23 liquidity=10214.45 spike=0.48
- EGTS.CA: score=-2.84 buy_ready=False sector_rank=15 price=17.15 support=16.91 resistance=17.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2280389.0 spike=0.06
- EHDR.CA: score=0.52 buy_ready=False sector_rank=14 price=2.94 support=2.89 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5392397.0 spike=0.11
- EKHO.CA: score=7.4 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.93 buy_ready=False sector_rank=19 price=2.11 support=2.12 resistance=2.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=10022970.0 spike=0.14
- ELKA.CA: score=15.77 buy_ready=False sector_rank=14 price=1.73 support=1.69 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=7638640.0 spike=0.1
- ELNA.CA: score=1.26 buy_ready=False sector_rank=14 price=37.67 support=36.5 resistance=39.49 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=24.88 liquidity=131920.33 spike=0.38
- ELSH.CA: score=8.49 buy_ready=False sector_rank=14 price=13.43 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=42.04 liquidity=3364966.0 spike=0.04
- ELWA.CA: score=8.29 buy_ready=False sector_rank=14 price=1.74 support=1.65 resistance=2.0 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=41.38 liquidity=1162346.11 spike=0.92
- EMFD.CA: score=10.87 buy_ready=False sector_rank=15 price=11.64 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=5994708.0 spike=0.1
- ENGC.CA: score=-3.16 buy_ready=False sector_rank=14 price=46.27 support=45.1 resistance=46.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1711303.13 spike=0.06
- EOSB.CA: score=12.13 buy_ready=False sector_rank=14 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=497.55 spike=0.01
- EPCO.CA: score=-1.29 buy_ready=False sector_rank=14 price=11.37 support=11.05 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3586066.25 spike=0.13
- EPPK.CA: score=3.47 buy_ready=False sector_rank=14 price=13.0 support=12.62 resistance=15.93 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=18.35 liquidity=1498926.0 spike=1.92
- ETEL.CA: score=23.4 buy_ready=False sector_rank=8 price=115.05 support=100.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=65.53 liquidity=19222550.0 spike=0.14
- ETRS.CA: score=8.41 buy_ready=False sector_rank=14 price=10.9 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=79.37 liquidity=1285675.75 spike=0.04
- EXPA.CA: score=14.06 buy_ready=False sector_rank=6 price=20.63 support=19.6 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:23 AM market time freshness=DELAYED_CURRENT RSI=73.28 liquidity=2660288.25 spike=0.07
- FAIT.CA: score=-3.22 buy_ready=False sector_rank=6 price=39.7 support=39.58 resistance=39.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=384539.75 spike=0.1
- FAITA.CA: score=17.84 buy_ready=False sector_rank=6 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=62.79 liquidity=177889.0 spike=3.13
- FERC.CA: score=13.6 buy_ready=False sector_rank=4 price=77.18 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=3199737.75 spike=0.17
- FWRY.CA: score=18.18 buy_ready=False sector_rank=11 price=18.87 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=53.73 liquidity=11491193.0 spike=0.1
- GBCO.CA: score=6.99 buy_ready=False sector_rank=20 price=29.52 support=29.53 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=50.71 liquidity=3492343.0 spike=0.07
- GDWA.CA: score=4.91 buy_ready=False sector_rank=14 price=0.78 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=5781488.0 spike=0.05
- GGCC.CA: score=11.83 buy_ready=False sector_rank=14 price=0.92 support=0.8 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=56.82 liquidity=3703760.75 spike=0.07
- GIHD.CA: score=1.98 buy_ready=False sector_rank=14 price=59.39 support=58.01 resistance=63.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6851942.0 spike=0.16
- GMCI.CA: score=8.51 buy_ready=False sector_rank=14 price=1.92 support=1.88 resistance=2.12 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=40.62 liquidity=382552.31 spike=0.75
- GRCA.CA: score=10.31 buy_ready=False sector_rank=14 price=56.51 support=54.7 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=36.08 liquidity=2177431.5 spike=0.11
- GSSC.CA: score=13.9 buy_ready=False sector_rank=14 price=284.5 support=264.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=1775892.75 spike=0.08
- GTWL.CA: score=5.25 buy_ready=False sector_rank=14 price=193.42 support=184.0 resistance=219.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156143792.0 spike=1.06
- HDBK.CA: score=10.96 buy_ready=False sector_rank=6 price=89.83 support=79.95 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=95.8 liquidity=4561884.5 spike=0.11
- HELI.CA: score=12.88 buy_ready=False sector_rank=15 price=7.63 support=7.5 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=22.93 liquidity=12326622.0 spike=0.07
- HRHO.CA: score=9.92 buy_ready=False sector_rank=18 price=26.1 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=6378828.5 spike=0.06
- ICID.CA: score=16.61 buy_ready=False sector_rank=14 price=15.4 support=7.83 resistance=16.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=96.8 liquidity=7483799.5 spike=0.37
- IDRE.CA: score=-3.58 buy_ready=False sector_rank=14 price=52.4 support=52.27 resistance=53.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1296571.88 spike=0.05
- IFAP.CA: score=12.91 buy_ready=False sector_rank=5 price=20.54 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=63.58 liquidity=1512163.13 spike=0.06
- INFI.CA: score=-1.31 buy_ready=False sector_rank=14 price=148.23 support=143.0 resistance=149.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3561905.75 spike=0.06
- IRON.CA: score=13.09 buy_ready=False sector_rank=4 price=31.89 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=61.1 liquidity=692746.06 spike=0.07
- ISMA.CA: score=11.25 buy_ready=False sector_rank=14 price=35.78 support=27.27 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=79.16 liquidity=2122529.0 spike=0.07
- ISMQ.CA: score=12.78 buy_ready=False sector_rank=4 price=9.11 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=3376465.0 spike=0.06
- ISPH.CA: score=19.11 buy_ready=False sector_rank=12 price=13.01 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=7986043.5 spike=0.04
- JUFO.CA: score=6.72 buy_ready=False sector_rank=10 price=26.61 support=22.78 resistance=29.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=91.13 liquidity=2393867.5 spike=0.04
- KABO.CA: score=12.41 buy_ready=False sector_rank=13 price=8.94 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=1729246.0 spike=0.04
- KWIN.CA: score=4.0 buy_ready=False sector_rank=14 price=84.97 support=84.08 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=27.96 liquidity=868302.06 spike=0.01
- KZPC.CA: score=10.13 buy_ready=False sector_rank=14 price=15.0 support=13.4 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64237088.0 spike=4.14
- LCSW.CA: score=11.81 buy_ready=False sector_rank=2 price=33.24 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=414486.72 spike=0.01
- LUTS.CA: score=6.23 buy_ready=False sector_rank=14 price=1.67 support=1.5 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=143206080.0 spike=1.55
- MAAL.CA: score=9.14 buy_ready=False sector_rank=14 price=8.6 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=44.76 liquidity=1015047.0 spike=0.07
- MASR.CA: score=11.58 buy_ready=False sector_rank=14 price=7.63 support=7.45 resistance=8.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=36.3 liquidity=6451832.5 spike=0.09
- MBSC.CA: score=16.2 buy_ready=False sector_rank=2 price=374.25 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=81.15 liquidity=5796795.0 spike=0.08
- MCQE.CA: score=19.38 buy_ready=False sector_rank=2 price=224.43 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=66.22 liquidity=5983986.0 spike=0.12
- MCRO.CA: score=18.13 buy_ready=False sector_rank=14 price=1.5 support=1.38 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=14830793.0 spike=0.08
- MENA.CA: score=10.36 buy_ready=False sector_rank=15 price=7.01 support=6.83 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:17 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=484891.16 spike=0.07
- MEPA.CA: score=10.51 buy_ready=False sector_rank=14 price=1.83 support=1.76 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=2385447.5 spike=0.04
- MFPC.CA: score=21.4 buy_ready=False sector_rank=4 price=39.18 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=74.65 liquidity=11388413.0 spike=0.14
- MFSC.CA: score=8.66 buy_ready=False sector_rank=14 price=48.96 support=46.0 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=536381.19 spike=0.05
- MHOT.CA: score=8.22 buy_ready=False sector_rank=16 price=18.1 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=61.78 liquidity=392024.59 spike=0.02
- MICH.CA: score=0.72 buy_ready=False sector_rank=14 price=47.48 support=47.2 resistance=48.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5594720.5 spike=0.15
- MILS.CA: score=22.13 buy_ready=False sector_rank=14 price=222.62 support=165.55 resistance=229.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=66.57 liquidity=47888380.0 spike=0.58
- MIPH.CA: score=9.69 buy_ready=False sector_rank=12 price=775.8 support=722.7 resistance=828.36 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=65.18 liquidity=567109.79 spike=0.16
- MOED.CA: score=21.13 buy_ready=False sector_rank=14 price=0.76 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=66.99 liquidity=36497608.0 spike=0.85
- MOIL.CA: score=4.47 buy_ready=False sector_rank=9 price=0.65 support=0.57 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=65291.47 spike=0.1
- MOIN.CA: score=8.47 buy_ready=False sector_rank=14 price=35.53 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=76.55 liquidity=1341074.75 spike=0.05
- MOSC.CA: score=8.47 buy_ready=False sector_rank=14 price=326.45 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=84.17 liquidity=1343524.25 spike=0.09
- MPCI.CA: score=18.14 buy_ready=False sector_rank=14 price=371.96 support=261.0 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=71.02 liquidity=8013507.0 spike=0.05
- MPCO.CA: score=23.4 buy_ready=False sector_rank=5 price=2.2 support=1.82 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=22366422.0 spike=0.21
- MPRC.CA: score=3.54 buy_ready=False sector_rank=14 price=41.09 support=39.5 resistance=41.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8416873.0 spike=0.32
- MTIE.CA: score=2.39 buy_ready=False sector_rank=20 price=8.35 support=8.25 resistance=8.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8887257.0 spike=0.17
- NAHO.CA: score=14.45 buy_ready=False sector_rank=14 price=0.15 support=0.1 resistance=0.16 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=97.83 liquidity=323944.49 spike=4.71
- NCCW.CA: score=2.98 buy_ready=False sector_rank=14 price=5.62 support=5.59 resistance=5.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7847302.5 spike=0.23
- NEDA.CA: score=-3.52 buy_ready=False sector_rank=14 price=2.75 support=2.7 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1013605.06 spike=1.17
- NHPS.CA: score=9.92 buy_ready=False sector_rank=14 price=87.0 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=58.53 liquidity=1793588.63 spike=0.04
- NINH.CA: score=11.45 buy_ready=False sector_rank=14 price=21.74 support=21.12 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=47.39 liquidity=3324259.5 spike=0.06
- NIPH.CA: score=6.12 buy_ready=False sector_rank=12 price=341.0 support=326.51 resistance=349.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60103600.0 spike=0.2
- OBRI.CA: score=-2.52 buy_ready=False sector_rank=14 price=32.19 support=32.0 resistance=32.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2356683.75 spike=0.07
- OCDI.CA: score=19.88 buy_ready=False sector_rank=15 price=32.53 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=73.8 liquidity=21747844.0 spike=0.16
- OCPH.CA: score=4.67 buy_ready=False sector_rank=14 price=258.05 support=225.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=23.41 liquidity=3542245.75 spike=0.13
- ODIN.CA: score=1.74 buy_ready=False sector_rank=14 price=3.25 support=3.2 resistance=3.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6613219.5 spike=0.17
- OFH.CA: score=15.53 buy_ready=False sector_rank=14 price=0.9 support=0.69 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=82.93 liquidity=8401257.0 spike=0.09
- OIH.CA: score=19.4 buy_ready=False sector_rank=3 price=1.85 support=1.43 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=83.67 liquidity=23473482.0 spike=0.19
- OLFI.CA: score=12.14 buy_ready=False sector_rank=10 price=23.62 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=60.67 liquidity=818729.13 spike=0.01
- ORAS.CA: score=4.6 buy_ready=False sector_rank=17 price=749.89 support=740.0 resistance=760.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23606912.0 spike=1.0
- ORHD.CA: score=17.88 buy_ready=False sector_rank=15 price=40.7 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=60.93 liquidity=15603235.0 spike=0.09
- ORWE.CA: score=11.13 buy_ready=False sector_rank=13 price=25.21 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=75.89 liquidity=3455216.5 spike=0.04
- PHAR.CA: score=21.12 buy_ready=False sector_rank=12 price=132.08 support=90.01 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=66.18 liquidity=42922384.0 spike=0.1
- PHDC.CA: score=19.88 buy_ready=False sector_rank=15 price=15.19 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=67.56 liquidity=25323562.0 spike=0.1
- PHTV.CA: score=22.44 buy_ready=False sector_rank=14 price=367.95 support=309.09 resistance=447.99 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=62.43 liquidity=6687123.52 spike=2.81
- POUL.CA: score=7.47 buy_ready=False sector_rank=10 price=37.11 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=48.36 liquidity=1147203.13 spike=0.04
- PRCL.CA: score=-0.56 buy_ready=False sector_rank=2 price=33.1 support=32.85 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1037119.0 spike=0.03
- PRDC.CA: score=5.88 buy_ready=False sector_rank=15 price=9.09 support=8.7 resistance=9.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=34.15 liquidity=2998836.25 spike=0.03
- PRMH.CA: score=-3.19 buy_ready=False sector_rank=14 price=2.39 support=2.37 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1681632.5 spike=0.13
- RACC.CA: score=22.13 buy_ready=False sector_rank=14 price=10.46 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=18 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.17 liquidity=15967555.0 spike=0.81
- RAKT.CA: score=5.78 buy_ready=False sector_rank=14 price=22.23 support=21.66 resistance=24.0 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=35.51 liquidity=369262.52 spike=1.64
- RAYA.CA: score=4.8 buy_ready=False sector_rank=21 price=6.99 support=6.97 resistance=7.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=26.25 liquidity=6718376.0 spike=0.07
- RMDA.CA: score=14.55 buy_ready=False sector_rank=12 price=6.12 support=4.97 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=66.78 liquidity=3422102.25 spike=0.03
- ROTO.CA: score=-3.51 buy_ready=False sector_rank=14 price=47.32 support=47.1 resistance=48.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1363242.13 spike=0.06
- RREI.CA: score=2.02 buy_ready=False sector_rank=14 price=4.51 support=4.4 resistance=4.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6889196.5 spike=0.11
- RTVC.CA: score=13.51 buy_ready=False sector_rank=14 price=4.09 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:22 AM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=1384685.0 spike=0.23
- RUBX.CA: score=10.42 buy_ready=False sector_rank=14 price=12.4 support=12.02 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=51.51 liquidity=2291827.25 spike=0.1
- SAUD.CA: score=16.36 buy_ready=False sector_rank=6 price=24.0 support=21.4 resistance=24.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=71.73 liquidity=2959136.75 spike=0.15
- SCEM.CA: score=25.4 buy_ready=False sector_rank=2 price=98.0 support=75.85 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=63.08 liquidity=29447920.0 spike=0.14
- SCFM.CA: score=17.73 buy_ready=False sector_rank=14 price=285.12 support=270.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=50.87 liquidity=7600392.5 spike=0.23
- SCTS.CA: score=16.94 buy_ready=False sector_rank=1 price=621.12 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=539434.75 spike=0.05
- SDTI.CA: score=-4.36 buy_ready=False sector_rank=14 price=67.07 support=67.0 resistance=69.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=513603.47 spike=0.02
- SEIG.CA: score=7.13 buy_ready=False sector_rank=14 price=271.73 support=237.7 resistance=295.0 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=75.98 liquidity=2002921.91 spike=0.2
- SIPC.CA: score=14.73 buy_ready=False sector_rank=14 price=4.81 support=3.76 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=73.61 liquidity=4600372.5 spike=0.07
- SKPC.CA: score=6.48 buy_ready=False sector_rank=4 price=17.83 support=17.75 resistance=18.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51933792.0 spike=1.04
- SMFR.CA: score=12.52 buy_ready=False sector_rank=14 price=259.58 support=225.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=69.28 liquidity=2395381.75 spike=0.08
- SNFC.CA: score=8.87 buy_ready=False sector_rank=14 price=10.95 support=10.6 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=1746592.0 spike=0.15
- SPIN.CA: score=-1.87 buy_ready=False sector_rank=13 price=18.64 support=18.41 resistance=18.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2450176.25 spike=0.05
- SPMD.CA: score=8.55 buy_ready=False sector_rank=14 price=0.45 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=60.24 liquidity=3423376.5 spike=0.1
- SUGR.CA: score=12.46 buy_ready=False sector_rank=10 price=50.15 support=46.47 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=82.64 liquidity=2140173.25 spike=0.11
- SVCE.CA: score=17.51 buy_ready=False sector_rank=14 price=10.41 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=7385609.5 spike=0.07
- SWDY.CA: score=3.93 buy_ready=False sector_rank=19 price=119.77 support=115.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15746695.0 spike=0.18
- TALM.CA: score=20.11 buy_ready=False sector_rank=1 price=19.63 support=15.7 resistance=20.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=67.93 liquidity=5705767.5 spike=0.13
- TMGH.CA: score=14.88 buy_ready=False sector_rank=15 price=96.16 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=45.93 liquidity=14803869.0 spike=0.05
- TRTO.CA: score=19.17 buy_ready=False sector_rank=14 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=37730.25 spike=4.2
- UEFM.CA: score=11.55 buy_ready=False sector_rank=14 price=544.63 support=530.0 resistance=594.0 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=47.02 liquidity=3425178.1 spike=0.78
- UEGC.CA: score=4.67 buy_ready=False sector_rank=14 price=2.03 support=1.95 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9546326.0 spike=0.22
- UNIP.CA: score=5.13 buy_ready=False sector_rank=14 price=0.36 support=0.35 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11781231.0 spike=0.36
- UNIT.CA: score=10.25 buy_ready=False sector_rank=15 price=19.05 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=56.15 liquidity=368027.94 spike=0.03
- WCDF.CA: score=9.75 buy_ready=False sector_rank=14 price=640.39 support=550.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=81.31 liquidity=623027.0 spike=0.11
- WKOL.CA: score=15.9 buy_ready=False sector_rank=14 price=341.12 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:25 AM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=3767483.75 spike=0.11
- ZEOT.CA: score=-2.35 buy_ready=False sector_rank=14 price=13.36 support=13.25 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2521757.0 spike=0.09
- ZMID.CA: score=4.88 buy_ready=False sector_rank=15 price=7.93 support=7.83 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92585280.0 spike=0.41

## Backtesting Lite
- CCAP.CA: 180d return=42.08%, max drawdown=-23.12%, MA20>MA50 days last20=18, as_of=2026-08-18T21:00:00+00:00
- SCEM.CA: 180d return=63.75%, max drawdown=-14.53%, MA20>MA50 days last20=20, as_of=2026-08-18T21:00:00+00:00
- ETEL.CA: 180d return=89.41%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-08-18T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=596 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=596 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- PHTV.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2423 sources=3 expected=Pyramisa Hotels & Resorts summary=Pyramisa Hotels logs EGP 170.5m consolidated profits in Q1-25; Pyramisa Hotels’ EGM nods to capital cut; Pyramisa Hotels posts 44% lower profit in 2020
  - Pyramisa Hotels logs EGP 170.5m consolidated profits in Q1-25: https://english.mubasher.info/news/4455411/Pyramisa-Hotels-logs-EGP-170-5m-consolidated-profits-in-Q1-25/
  - Pyramisa Hotels’ EGM nods to capital cut: https://english.mubasher.info/news/4052716/Pyramisa-Hotels-EGM-nods-to-capital-cut/
  - Pyramisa Hotels posts 44% lower profit in 2020: https://english.mubasher.info/news/3761369/Pyramisa-Hotels-posts-44-lower-profit-in-2020/
- MILS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=North Cairo Flour Mills summary=North Cairo Mills stock hits historic peak amid clear emergence of buying power; North Cairo Mills approves EGP 0.5/shr dividends for FY19/20; North Cairo Mills reports 37% profit decline in FY19/20 initial results
  - North Cairo Mills stock hits historic peak amid clear emergence of buying power: https://english.mubasher.info/news/4540088/North-Cairo-Mills-stock-hits-historic-peak-amid-clear-emergence-of-buying-power/
  - North Cairo Mills approves EGP 0.5/shr dividends for FY19/20: https://english.mubasher.info/news/3726135/North-Cairo-Mills-approves-EGP-0-5-shr-dividends-for-FY19-20/
  - North Cairo Mills reports 37% profit decline in FY19/20 initial results: https://english.mubasher.info/news/3676432/North-Cairo-Mills-reports-37-profit-decline-in-FY19-20-initial-results/
- RACC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Raya Customer Experience summary=Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.

## Warnings
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for PHTV.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for MILS.CA matches the company but no source/report date was detected.
- Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
