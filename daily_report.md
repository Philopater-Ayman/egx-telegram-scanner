# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-07-30T10:26:12.897588+00:00
Generated Cairo: 2026-07-30 13:26
Run timing: target 11:00 Cairo | generated Cairo 2026-07-30 13:26 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-07-30 13:19

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 176/189
- Top sector: Education

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, July 30
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 40.0% / above MA50 35.0%
- EGX70 regime: BEARISH / above MA20 42.11% / above MA50 68.42%
- Sector breadth: 28.57%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=410912288.0 spike=0.58 score=15.87
- AMOC.CA: liquidity=358768416.0 spike=5.95 score=11.1
- PHAR.CA: liquidity=249561104.0 spike=3.99 score=25.4
- TMGH.CA: liquidity=245290848.0 spike=0.67 score=16.4
- BIOC.CA: liquidity=229757632.0 spike=3.52 score=11.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: The scanner flagged several stocks with strong accumulation spikes and bullish‑watch outlooks, but the EGX30 and EGX70 indices remain bearish with weak breadth, keeping risk mode defensive and preventing new buys.
- Top tickets (AJWA.CA, TALM.CA, MILS.CA, etc.) show accumulation‑spike liquidity and bullish‑watch scores, yet many have overheated RSI and sit near resistance, limiting near‑term upside.
- Sector strength is concentrated in Education, Textiles and Agriculture & Food Production, which have above‑MA20/MA50 ratios, but overall sector breadth is only 28.6%, indicating narrow participation.
- EGX30 and EGX70 are both bearish (below MA20/MA50, negative 5‑day returns), shifting the risk mode to DEFENSIVE_NO_NEW_BUY and overriding individual stock bullish signals.
- Uncertainty remains: liquidity spikes could reverse, resistance levels are tight, and RSI extremes suggest possible pull‑backs in the next 1‑3 days.

## Top Liquidity Spikes
- EOSB.CA: spike=12.26 liquidity=444839.16 outlook=CONSTRUCTIVE score=67.12 buy_ready=False
- WKOL.CA: spike=11.67 liquidity=121082384.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EALR.CA: spike=7.36 liquidity=138267536.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AALR.CA: spike=6.79 liquidity=137792576.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMOC.CA: spike=5.95 liquidity=358768416.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Education: score=14.65 5d=12.93% 20d=15.32% aboveMA50=100.0%
- #2 Textiles: score=8.15 5d=1.32% 20d=11.88% aboveMA50=75.0%
- #3 Agriculture & Food Production: score=7.91 5d=4.52% 20d=8.39% aboveMA50=50.0%
- #4 Healthcare: score=7.64 5d=-0.06% 20d=9.7% aboveMA50=83.33%
- #5 Industrial Goods & Cables: score=7.36 5d=0.31% 20d=8.52% aboveMA50=100.0%
- #6 General / Verified EGX Expansion: score=7.12 5d=0.0% 20d=12.42% aboveMA50=69.9%
- #7 Real Estate: score=6.92 5d=0.11% 20d=14.62% aboveMA50=69.23%
- #8 Telecommunications: score=6.54 5d=0.82% 20d=10.02% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=98.91 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- TALM.CA: BULLISH_WATCH score=93 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- AJWA.CA: BULLISH_WATCH score=90.12 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- SPIN.CA: BULLISH_WATCH score=85.15 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- ETRS.CA: BULLISH_WATCH score=83.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ROTO.CA: BULLISH_WATCH score=83.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ACGC.CA: BULLISH_WATCH score=80.15 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- GSSC.CA: BULLISH_WATCH score=80.12 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI
- AXPH.CA: BULLISH_WATCH score=80.12 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- CIRA.CA: BULLISH_WATCH score=77 liquidity=TRADEABLE sector=LEADING risk=overheated RSI; far above support

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=11.4 buy_ready=False sector_rank=6 price=285.3 support=240.49 resistance=289.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=137792576.0 spike=6.79
- ABUK.CA: score=19.58 buy_ready=False sector_rank=13 price=73.15 support=67.04 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=50.07 liquidity=127147120.0 spike=0.84
- ACAMD.CA: score=21.4 buy_ready=False sector_rank=6 price=2.32 support=2.2 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=37209744.0 spike=0.51
- ACGC.CA: score=23.03 buy_ready=False sector_rank=2 price=10.23 support=9.03 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=67.04 liquidity=9630652.0 spike=0.32
- ADCI.CA: score=12.95 buy_ready=False sector_rank=6 price=251.0 support=230.0 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=77.43 liquidity=4553965.0 spike=0.44
- ADIB.CA: score=18.24 buy_ready=False sector_rank=9 price=51.98 support=44.9 resistance=52.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=79.65 liquidity=97207136.0 spike=0.73
- ADPC.CA: score=21.4 buy_ready=False sector_rank=6 price=3.86 support=3.37 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=67.2 liquidity=14667467.0 spike=0.43
- AFDI.CA: score=20.4 buy_ready=False sector_rank=6 price=50.55 support=42.6 resistance=52.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=79.14 liquidity=16578659.0 spike=0.93
- AFMC.CA: score=11.4 buy_ready=False sector_rank=6 price=169.77 support=148.0 resistance=179.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=214197712.0 spike=3.5
- AJWA.CA: score=26.08 buy_ready=False sector_rank=6 price=194.05 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=68.22 liquidity=65927392.0 spike=2.34
- ALCN.CA: score=14.59 buy_ready=False sector_rank=17 price=29.22 support=27.74 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=65.48 liquidity=8697502.0 spike=0.38
- ALUM.CA: score=9.49 buy_ready=False sector_rank=6 price=22.83 support=20.8 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=53.21 liquidity=1087702.63 spike=0.17
- AMER.CA: score=20.4 buy_ready=False sector_rank=7 price=4.64 support=2.32 resistance=4.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=91.74 liquidity=37730152.0 spike=0.33
- AMES.CA: score=21.4 buy_ready=False sector_rank=6 price=121.44 support=57.23 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=68.14 liquidity=19670912.0 spike=0.18
- AMIA.CA: score=19.75 buy_ready=False sector_rank=6 price=11.13 support=8.43 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=79.14 liquidity=9348331.0 spike=0.63
- AMOC.CA: score=11.1 buy_ready=False sector_rank=10 price=8.91 support=8.55 resistance=9.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=358768416.0 spike=5.95
- APSW.CA: score=7.79 buy_ready=False sector_rank=6 price=8.65 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=387671.97 spike=0.25
- ARAB.CA: score=19.4 buy_ready=False sector_rank=7 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=60.98 liquidity=44253044.0 spike=0.33
- ARCC.CA: score=17.49 buy_ready=False sector_rank=15 price=55.85 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=24067758.0 spike=0.86
- AREH.CA: score=16.4 buy_ready=False sector_rank=6 price=1.41 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=9995430.0 spike=0.36
- ARVA.CA: score=8.4 buy_ready=False sector_rank=6 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=81.74 liquidity=0.0 spike=0.0
- ASCM.CA: score=18.4 buy_ready=False sector_rank=6 price=61.93 support=57.25 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=37970452.0 spike=0.7
- ASPI.CA: score=18.4 buy_ready=False sector_rank=6 price=0.43 support=0.31 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=87.64 liquidity=17842714.0 spike=0.46
- ATLC.CA: score=8.44 buy_ready=False sector_rank=14 price=5.04 support=4.97 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=2902621.0 spike=0.41
- ATQA.CA: score=17.58 buy_ready=False sector_rank=13 price=9.76 support=9.35 resistance=10.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=76.47 liquidity=33275194.0 spike=0.85
- AXPH.CA: score=14.84 buy_ready=False sector_rank=6 price=1210.4 support=1090.02 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=64.19 liquidity=3438367.75 spike=0.88
- BINV.CA: score=10.77 buy_ready=False sector_rank=12 price=46.78 support=45.09 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=46.93 liquidity=1901540.88 spike=0.26
- BIOC.CA: score=11.4 buy_ready=False sector_rank=6 price=233.9 support=210.5 resistance=239.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=229757632.0 spike=3.52
- BTFH.CA: score=21.54 buy_ready=False sector_rank=14 price=3.08 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=152798704.0 spike=0.7
- CAED.CA: score=18.4 buy_ready=False sector_rank=6 price=126.48 support=70.1 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=77.81 liquidity=17109728.0 spike=0.25
- CANA.CA: score=16.51 buy_ready=False sector_rank=9 price=37.5 support=35.18 resistance=39.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=6270511.5 spike=0.36
- CCAP.CA: score=15.87 buy_ready=False sector_rank=12 price=5.2 support=4.71 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=410912288.0 spike=0.58
- CCRS.CA: score=21.4 buy_ready=False sector_rank=6 price=2.51 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=68.0 liquidity=15815854.0 spike=0.9
- CEFM.CA: score=23.82 buy_ready=False sector_rank=6 price=136.03 support=96.1 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=71.78 liquidity=51136316.0 spike=2.21
- CERA.CA: score=17.57 buy_ready=False sector_rank=6 price=1.26 support=1.2 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=8166400.5 spike=0.33
- CFGH.CA: score=-0.72 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37779.77 spike=2.42
- CICH.CA: score=12.28 buy_ready=False sector_rank=14 price=12.04 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=2744786.5 spike=0.53
- CIEB.CA: score=13.32 buy_ready=False sector_rank=9 price=23.88 support=23.37 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=54.86 liquidity=7077461.5 spike=0.8
- CIRA.CA: score=23.4 buy_ready=False sector_rank=1 price=34.97 support=27.74 resistance=36.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=84.29 liquidity=50102784.0 spike=0.94
- CLHO.CA: score=19.4 buy_ready=False sector_rank=4 price=16.4 support=15.98 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=12124423.0 spike=0.28
- CNFN.CA: score=17.92 buy_ready=False sector_rank=14 price=4.72 support=4.7 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=56.82 liquidity=9384195.0 spike=0.45
- COMI.CA: score=21.24 buy_ready=False sector_rank=9 price=139.63 support=126.89 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=68.64 liquidity=125313344.0 spike=0.3
- COPR.CA: score=17.4 buy_ready=False sector_rank=6 price=0.4 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=16385719.0 spike=0.54
- COSG.CA: score=19.4 buy_ready=False sector_rank=6 price=1.62 support=1.5 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=68.18 liquidity=25680408.0 spike=0.58
- CPCI.CA: score=13.82 buy_ready=False sector_rank=6 price=463.04 support=389.0 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=72.51 liquidity=2417922.75 spike=0.21
- CSAG.CA: score=14.89 buy_ready=False sector_rank=17 price=31.5 support=32.0 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=13302444.0 spike=0.91
- DAPH.CA: score=20.4 buy_ready=False sector_rank=6 price=96.91 support=80.06 resistance=99.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=80.96 liquidity=13492319.0 spike=0.75
- DEIN.CA: score=-3.6 buy_ready=False sector_rank=6 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=9.01 buy_ready=False sector_rank=19 price=26.45 support=26.35 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=1437434.63 spike=0.45
- DSCW.CA: score=21.4 buy_ready=False sector_rank=6 price=1.93 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=35414368.0 spike=0.65
- DTPP.CA: score=21.4 buy_ready=False sector_rank=6 price=241.15 support=153.55 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=65.3 liquidity=25153896.0 spike=0.32
- EALR.CA: score=11.4 buy_ready=False sector_rank=6 price=425.0 support=365.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=138267536.0 spike=7.36
- EASB.CA: score=13.13 buy_ready=False sector_rank=6 price=7.38 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=3726191.25 spike=0.28
- EAST.CA: score=15.57 buy_ready=False sector_rank=19 price=36.4 support=36.01 resistance=37.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=47460944.0 spike=0.61
- EBSC.CA: score=10.47 buy_ready=False sector_rank=6 price=1.86 support=1.74 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1066510.13 spike=0.13
- ECAP.CA: score=12.17 buy_ready=False sector_rank=6 price=32.4 support=31.95 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=2770453.75 spike=0.48
- EDFM.CA: score=18.47 buy_ready=False sector_rank=6 price=389.39 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=73.92 liquidity=6430241.0 spike=1.32
- EEII.CA: score=19.4 buy_ready=False sector_rank=6 price=2.64 support=2.37 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=10293612.0 spike=0.45
- EFIC.CA: score=21.58 buy_ready=False sector_rank=13 price=199.42 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=71.09 liquidity=13569507.0 spike=0.82
- EFID.CA: score=9.57 buy_ready=False sector_rank=19 price=26.93 support=26.64 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=33.03 liquidity=27915212.0 spike=0.6
- EFIH.CA: score=23.04 buy_ready=False sector_rank=11 price=22.64 support=20.16 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=58.31 liquidity=42471592.0 spike=0.67
- EGAL.CA: score=17.58 buy_ready=False sector_rank=13 price=295.94 support=275.0 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=55.2 liquidity=17696840.0 spike=0.42
- EGAS.CA: score=20.8 buy_ready=False sector_rank=10 price=53.01 support=48.5 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=7702839.5 spike=0.59
- EGBE.CA: score=10.19 buy_ready=False sector_rank=9 price=0.47 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=95.96 liquidity=111958.98 spike=1.92
- EGCH.CA: score=17.58 buy_ready=False sector_rank=13 price=12.98 support=12.19 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=43148360.0 spike=0.7
- EGSA.CA: score=6.41 buy_ready=False sector_rank=8 price=8.87 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7096.0 spike=0.39
- EGTS.CA: score=16.4 buy_ready=False sector_rank=7 price=17.43 support=16.75 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=39.35 liquidity=11468212.0 spike=0.25
- EHDR.CA: score=21.4 buy_ready=False sector_rank=6 price=2.75 support=2.44 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=67.06 liquidity=21809806.0 spike=0.53
- EKHO.CA: score=5.1 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=20.4 buy_ready=False sector_rank=5 price=2.15 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=60.53 liquidity=34938932.0 spike=0.5
- ELKA.CA: score=6.4 buy_ready=False sector_rank=6 price=1.73 support=1.72 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58682956.0 spike=0.76
- ELNA.CA: score=7.74 buy_ready=False sector_rank=6 price=38.1 support=36.1 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=63.52 liquidity=339983.44 spike=0.55
- ELSH.CA: score=19.4 buy_ready=False sector_rank=6 price=13.73 support=11.53 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=60.64 liquidity=86676240.0 spike=0.6
- ELWA.CA: score=9.68 buy_ready=False sector_rank=6 price=1.79 support=1.74 resistance=2.14 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=30.77 liquidity=4460411.4 spike=2.91
- EMFD.CA: score=16.4 buy_ready=False sector_rank=7 price=11.18 support=11.4 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=45.1 liquidity=32086222.0 spike=0.53
- ENGC.CA: score=16.97 buy_ready=False sector_rank=6 price=41.49 support=36.0 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=67.59 liquidity=7573433.0 spike=0.3
- EOSB.CA: score=18.84 buy_ready=False sector_rank=6 price=1.55 support=1.5 resistance=1.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=444839.16 spike=12.26
- EPCO.CA: score=14.86 buy_ready=False sector_rank=6 price=10.49 support=8.57 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=6456147.5 spike=0.22
- EPPK.CA: score=11.73 buy_ready=False sector_rank=6 price=15.07 support=13.03 resistance=15.93 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=58.31 liquidity=334674.55 spike=0.27
- ETEL.CA: score=20.84 buy_ready=False sector_rank=8 price=103.98 support=90.05 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=84.46 liquidity=103121600.0 spike=1.22
- ETRS.CA: score=21.4 buy_ready=False sector_rank=6 price=10.58 support=10.1 resistance=11.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=18807136.0 spike=0.4
- EXPA.CA: score=20.24 buy_ready=False sector_rank=9 price=19.93 support=18.14 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=85.34 liquidity=14967881.0 spike=0.48
- FAIT.CA: score=6.97 buy_ready=False sector_rank=9 price=36.28 support=35.6 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=53.56 liquidity=725049.31 spike=0.25
- FAITA.CA: score=1.27 buy_ready=False sector_rank=9 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=29.82 liquidity=32228.94 spike=0.76
- FERC.CA: score=10.09 buy_ready=False sector_rank=13 price=75.86 support=72.91 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=52.04 liquidity=3516296.0 spike=0.3
- FWRY.CA: score=18.04 buy_ready=False sector_rank=11 price=18.96 support=18.28 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=41.7 liquidity=44140384.0 spike=0.34
- GBCO.CA: score=18.35 buy_ready=False sector_rank=16 price=29.82 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=49.45 liquidity=21392940.0 spike=0.3
- GDWA.CA: score=15.4 buy_ready=False sector_rank=6 price=0.8 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=66.86 liquidity=63719672.0 spike=0.62
- GGCC.CA: score=18.4 buy_ready=False sector_rank=6 price=0.82 support=0.46 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=79.32 liquidity=11364231.0 spike=0.3
- GIHD.CA: score=21.4 buy_ready=False sector_rank=6 price=57.36 support=40.91 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=73.4 liquidity=14649626.0 spike=0.28
- GMCI.CA: score=9.93 buy_ready=False sector_rank=6 price=1.98 support=1.74 resistance=2.26 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=532441.81 spike=0.39
- GRCA.CA: score=18.9 buy_ready=False sector_rank=6 price=60.82 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=73.51 liquidity=7497790.5 spike=0.46
- GSSC.CA: score=24.84 buy_ready=False sector_rank=6 price=283.0 support=241.32 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=76.68 liquidity=38958872.0 spike=3.22
- GTWL.CA: score=21.4 buy_ready=False sector_rank=6 price=101.81 support=76.25 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=32172652.0 spike=0.24
- HDBK.CA: score=19.24 buy_ready=False sector_rank=9 price=81.76 support=76.9 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=53.14 liquidity=11911301.0 spike=0.39
- HELI.CA: score=20.4 buy_ready=False sector_rank=7 price=8.34 support=6.4 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=86.57 liquidity=168300336.0 spike=0.83
- HRHO.CA: score=14.54 buy_ready=False sector_rank=14 price=26.19 support=26.25 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=43.65 liquidity=41269480.0 spike=0.48
- ICID.CA: score=13.29 buy_ready=False sector_rank=6 price=7.99 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=3888873.25 spike=0.51
- IDRE.CA: score=21.4 buy_ready=False sector_rank=6 price=47.63 support=41.8 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=66.69 liquidity=10630979.0 spike=0.4
- IFAP.CA: score=16.8 buy_ready=False sector_rank=3 price=19.35 support=18.96 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=61.19 liquidity=7398265.0 spike=0.78
- INFI.CA: score=18.84 buy_ready=False sector_rank=6 price=107.49 support=89.02 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=75.62 liquidity=20511590.0 spike=1.22
- IRON.CA: score=3.69 buy_ready=False sector_rank=13 price=30.42 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=25.87 liquidity=4111025.5 spike=0.65
- ISMA.CA: score=18.4 buy_ready=False sector_rank=6 price=30.29 support=26.54 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=82.93 liquidity=12434858.0 spike=0.48
- ISMQ.CA: score=18.58 buy_ready=False sector_rank=13 price=9.1 support=9.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=41.42 liquidity=69375376.0 spike=0.74
- ISPH.CA: score=18.4 buy_ready=False sector_rank=4 price=11.36 support=11.2 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=54.81 liquidity=26260386.0 spike=0.54
- JUFO.CA: score=9.57 buy_ready=False sector_rank=19 price=28.56 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=19.68 liquidity=16561727.0 spike=0.64
- KABO.CA: score=23.4 buy_ready=False sector_rank=2 price=7.84 support=6.21 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=65.11 liquidity=14823526.0 spike=0.31
- KWIN.CA: score=18.4 buy_ready=False sector_rank=6 price=99.03 support=66.1 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=89.37 liquidity=30423062.0 spike=0.59
- KZPC.CA: score=9.96 buy_ready=False sector_rank=6 price=8.48 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=2559651.5 spike=0.49
- LCSW.CA: score=5.49 buy_ready=False sector_rank=15 price=32.72 support=32.16 resistance=34.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16907144.0 spike=0.25
- LUTS.CA: score=7.02 buy_ready=False sector_rank=6 price=0.55 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=18.65 liquidity=6621074.0 spike=0.2
- MAAL.CA: score=18.4 buy_ready=False sector_rank=6 price=8.77 support=7.09 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=78.62 liquidity=10859099.0 spike=0.66
- MASR.CA: score=19.4 buy_ready=False sector_rank=6 price=7.95 support=7.24 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=62.68 liquidity=61638620.0 spike=0.72
- MBSC.CA: score=13.98 buy_ready=False sector_rank=15 price=242.12 support=230.0 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=53.17 liquidity=6488891.5 spike=0.35
- MCQE.CA: score=17.49 buy_ready=False sector_rank=15 price=180.2 support=168.05 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=10445076.0 spike=0.58
- MCRO.CA: score=20.4 buy_ready=False sector_rank=6 price=1.49 support=1.19 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=90094776.0 spike=0.68
- MENA.CA: score=10.0 buy_ready=False sector_rank=7 price=6.93 support=6.72 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=598175.38 spike=0.08
- MEPA.CA: score=21.4 buy_ready=False sector_rank=6 price=1.8 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=71.7 liquidity=25974756.0 spike=0.53
- MFPC.CA: score=17.58 buy_ready=False sector_rank=13 price=36.58 support=34.95 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=42.49 liquidity=78770600.0 spike=0.89
- MFSC.CA: score=9.95 buy_ready=False sector_rank=6 price=46.86 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=3552192.5 spike=0.63
- MHOT.CA: score=10.0 buy_ready=False sector_rank=20 price=16.43 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=50.38 liquidity=4499725.0 spike=0.39
- MICH.CA: score=21.4 buy_ready=False sector_rank=6 price=39.81 support=36.1 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=11782452.0 spike=0.72
- MILS.CA: score=25.72 buy_ready=False sector_rank=6 price=188.62 support=126.31 resistance=205.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=72.81 liquidity=97562872.0 spike=2.16
- MIPH.CA: score=12.02 buy_ready=False sector_rank=4 price=736.78 support=632.11 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=64.07 liquidity=621013.19 spike=0.18
- MOED.CA: score=15.4 buy_ready=False sector_rank=6 price=0.68 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=53.4 liquidity=23906692.0 spike=1.0
- MOIL.CA: score=11.85 buy_ready=False sector_rank=10 price=0.68 support=0.46 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=92.31 liquidity=995298.56 spike=1.38
- MOIN.CA: score=5.69 buy_ready=False sector_rank=6 price=23.6 support=22.66 resistance=24.76 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=46.41 liquidity=293159.2 spike=0.38
- MOSC.CA: score=17.23 buy_ready=False sector_rank=6 price=285.04 support=260.01 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=65.47 liquidity=5829282.0 spike=0.48
- MPCI.CA: score=20.4 buy_ready=False sector_rank=6 price=289.89 support=236.1 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=89.58 liquidity=60740616.0 spike=0.62
- MPCO.CA: score=24.64 buy_ready=False sector_rank=3 price=1.92 support=1.76 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=67.35 liquidity=90237688.0 spike=1.12
- MPRC.CA: score=20.4 buy_ready=False sector_rank=6 price=45.41 support=37.51 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=78.44 liquidity=15963849.0 spike=0.52
- MTIE.CA: score=18.35 buy_ready=False sector_rank=16 price=9.4 support=8.92 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=57.84 liquidity=21333166.0 spike=0.91
- NAHO.CA: score=5.41 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=8228.14 spike=0.28
- NCCW.CA: score=18.4 buy_ready=False sector_rank=6 price=6.9 support=5.94 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=78.41 liquidity=22732126.0 spike=0.81
- NEDA.CA: score=8.11 buy_ready=False sector_rank=6 price=2.72 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=47.37 liquidity=1028032.17 spike=1.34
- NHPS.CA: score=21.4 buy_ready=False sector_rank=6 price=83.83 support=62.1 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=13165181.0 spike=0.15
- NINH.CA: score=18.4 buy_ready=False sector_rank=6 price=21.6 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=76.48 liquidity=11431471.0 spike=0.26
- NIPH.CA: score=18.58 buy_ready=False sector_rank=4 price=224.94 support=160.55 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=79.42 liquidity=169674864.0 spike=1.09
- OBRI.CA: score=15.4 buy_ready=False sector_rank=6 price=32.6 support=32.4 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=39.48 liquidity=26300762.0 spike=0.62
- OCDI.CA: score=21.4 buy_ready=False sector_rank=7 price=27.9 support=24.31 resistance=29.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=62.34 liquidity=50896296.0 spike=0.52
- OCPH.CA: score=18.4 buy_ready=False sector_rank=6 price=454.98 support=348.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=83.04 liquidity=11620322.0 spike=0.47
- ODIN.CA: score=20.66 buy_ready=False sector_rank=6 price=2.7 support=2.07 resistance=2.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=20561346.0 spike=1.13
- OFH.CA: score=21.4 buy_ready=False sector_rank=6 price=0.7 support=0.58 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=73.74 liquidity=29753668.0 spike=0.45
- OIH.CA: score=22.99 buy_ready=False sector_rank=12 price=1.47 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=142330496.0 spike=2.06
- OLFI.CA: score=18.64 buy_ready=False sector_rank=19 price=22.79 support=21.91 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=56.11 liquidity=9068335.0 spike=0.26
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=710.55 support=702.05 resistance=719.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78450848.0 spike=1.0
- ORHD.CA: score=21.4 buy_ready=False sector_rank=7 price=38.88 support=37.52 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=58.77 liquidity=71720264.0 spike=0.49
- ORWE.CA: score=20.4 buy_ready=False sector_rank=2 price=22.61 support=22.2 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=54.81 liquidity=16418482.0 spike=0.67
- PHAR.CA: score=25.4 buy_ready=False sector_rank=4 price=99.89 support=84.2 resistance=97.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=80.84 liquidity=249561104.0 spike=3.99
- PHDC.CA: score=16.4 buy_ready=False sector_rank=7 price=14.42 support=14.41 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=46.41 liquidity=113142560.0 spike=0.48
- PHTV.CA: score=12.11 buy_ready=False sector_rank=6 price=321.26 support=260.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=83.89 liquidity=1707523.13 spike=0.35
- POUL.CA: score=9.57 buy_ready=False sector_rank=19 price=37.33 support=37.02 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=33.27 liquidity=11595091.0 spike=0.34
- PRCL.CA: score=17.03 buy_ready=False sector_rank=15 price=34.97 support=30.6 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=48.73 liquidity=8546390.0 spike=0.17
- PRDC.CA: score=21.4 buy_ready=False sector_rank=7 price=9.09 support=7.26 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=34328344.0 spike=0.28
- PRMH.CA: score=14.25 buy_ready=False sector_rank=6 price=2.58 support=2.45 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=7852512.0 spike=0.47
- RACC.CA: score=16.4 buy_ready=False sector_rank=6 price=9.93 support=9.55 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=54.59 liquidity=11710759.0 spike=0.53
- RAKT.CA: score=11.48 buy_ready=False sector_rank=6 price=22.84 support=21.25 resistance=23.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=523245.41 spike=1.78
- RAYA.CA: score=14.28 buy_ready=False sector_rank=21 price=7.46 support=7.12 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=43.52 liquidity=36737204.0 spike=0.27
- RMDA.CA: score=21.64 buy_ready=False sector_rank=4 price=5.23 support=4.9 resistance=5.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=69.35 liquidity=32083498.0 spike=1.12
- ROTO.CA: score=21.4 buy_ready=False sector_rank=6 price=42.55 support=40.5 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=58.75 liquidity=11588947.0 spike=0.58
- RREI.CA: score=10.18 buy_ready=False sector_rank=6 price=4.64 support=4.57 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=157333616.0 spike=2.89
- RTVC.CA: score=11.51 buy_ready=False sector_rank=6 price=3.8 support=3.65 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=3105246.5 spike=0.68
- RUBX.CA: score=16.68 buy_ready=False sector_rank=6 price=12.49 support=11.07 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=48.66 liquidity=7278257.0 spike=0.11
- SAUD.CA: score=16.96 buy_ready=False sector_rank=9 price=21.85 support=20.5 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=8715015.0 spike=0.9
- SCEM.CA: score=17.49 buy_ready=False sector_rank=15 price=80.62 support=60.14 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=85.83 liquidity=69424248.0 spike=0.95
- SCFM.CA: score=22.16 buy_ready=False sector_rank=6 price=284.05 support=235.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=67.3 liquidity=34489524.0 spike=1.38
- SCTS.CA: score=14.25 buy_ready=False sector_rank=1 price=609.99 support=543.01 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=51.64 liquidity=1850166.88 spike=0.26
- SDTI.CA: score=21.66 buy_ready=False sector_rank=6 price=58.27 support=45.85 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=92.97 liquidity=27253784.0 spike=1.63
- SEIG.CA: score=9.16 buy_ready=False sector_rank=6 price=271.14 support=242.1 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57740424.0 spike=2.38
- SIPC.CA: score=18.4 buy_ready=False sector_rank=6 price=3.88 support=3.27 resistance=4.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=84.27 liquidity=19196764.0 spike=0.79
- SKPC.CA: score=17.66 buy_ready=False sector_rank=13 price=15.81 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=44.95 liquidity=54273744.0 spike=1.54
- SMFR.CA: score=21.4 buy_ready=False sector_rank=6 price=233.34 support=191.02 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=65.78 liquidity=13286946.0 spike=0.64
- SNFC.CA: score=10.83 buy_ready=False sector_rank=6 price=11.1 support=11.04 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=4425578.0 spike=0.39
- SPIN.CA: score=23.4 buy_ready=False sector_rank=2 price=15.73 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=68.14 liquidity=22553632.0 spike=0.91
- SPMD.CA: score=21.4 buy_ready=False sector_rank=6 price=0.45 support=0.42 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=13743162.0 spike=0.5
- SUGR.CA: score=10.7 buy_ready=False sector_rank=19 price=46.55 support=46.01 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=54.27 liquidity=5123916.0 spike=0.95
- SVCE.CA: score=16.4 buy_ready=False sector_rank=6 price=9.15 support=8.9 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=56.48 liquidity=13008093.0 spike=0.24
- SWDY.CA: score=18.4 buy_ready=False sector_rank=5 price=92.33 support=85.11 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=79.22 liquidity=18289512.0 spike=0.87
- TALM.CA: score=25.72 buy_ready=False sector_rank=1 price=17.31 support=15.27 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=87.76 liquidity=60943892.0 spike=2.16
- TMGH.CA: score=16.4 buy_ready=False sector_rank=7 price=96.4 support=92.6 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=245290848.0 spike=0.67
- TRTO.CA: score=7.4 buy_ready=False sector_rank=6 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=18.71 buy_ready=False sector_rank=6 price=548.26 support=467.2 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=74.27 liquidity=6607664.0 spike=1.35
- UEGC.CA: score=21.4 buy_ready=False sector_rank=6 price=2.28 support=1.36 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=18157236.0 spike=0.34
- UNIP.CA: score=21.4 buy_ready=False sector_rank=6 price=0.37 support=0.32 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=70.51 liquidity=14016351.0 spike=0.52
- UNIT.CA: score=11.95 buy_ready=False sector_rank=7 price=17.52 support=12.66 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=57.56 liquidity=2547202.75 spike=0.08
- WCDF.CA: score=15.93 buy_ready=False sector_rank=6 price=586.73 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=2534927.25 spike=0.81
- WKOL.CA: score=11.4 buy_ready=False sector_rank=6 price=350.86 support=311.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=121082384.0 spike=11.67
- ZEOT.CA: score=21.02 buy_ready=False sector_rank=6 price=12.43 support=10.8 resistance=12.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=79.82 liquidity=39229176.0 spike=1.31
- ZMID.CA: score=18.4 buy_ready=False sector_rank=7 price=7.38 support=6.23 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=76.54 liquidity=139138912.0 spike=0.54

## Backtesting Lite
- AJWA.CA: 180d return=44.49%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-07-28T21:00:00+00:00
- TALM.CA: 180d return=10.3%, max drawdown=-12.21%, MA20>MA50 days last20=8, as_of=2026-07-28T21:00:00+00:00
- MILS.CA: 180d return=49.77%, max drawdown=-29.51%, MA20>MA50 days last20=15, as_of=2026-07-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- MILS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=North Cairo Flour Mills summary=North Cairo Mills stock hits historic peak amid clear emergence of buying power; North Cairo Mills approves EGP 0.5/shr dividends for FY19/20; North Cairo Mills reports 37% profit decline in FY19/20 initial results
  - North Cairo Mills stock hits historic peak amid clear emergence of buying power: https://english.mubasher.info/news/4540088/North-Cairo-Mills-stock-hits-historic-peak-amid-clear-emergence-of-buying-power/
  - North Cairo Mills approves EGP 0.5/shr dividends for FY19/20: https://english.mubasher.info/news/3726135/North-Cairo-Mills-approves-EGP-0-5-shr-dividends-for-FY19-20/
  - North Cairo Mills reports 37% profit decline in FY19/20 initial results: https://english.mubasher.info/news/3676432/North-Cairo-Mills-reports-37-profit-decline-in-FY19-20-initial-results/
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- GSSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=General Co. For Silos & Storage summary=General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials; General Company for Silos to set up new firm with EGP 500m capital; General Company for Silos’ EGM nods to EGP 25m capital hike
  - General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials: https://english.mubasher.info/news/4529067/General-Company-for-Silos-generates-nearly-EGP-62m-net-profits-in-Q1-25-26-audited-financials/
  - General Company for Silos to set up new firm with EGP 500m capital: https://english.mubasher.info/news/4043715/General-Company-for-Silos-to-set-up-new-firm-with-EGP-500m-capital/
  - General Company for Silos’ EGM nods to EGP 25m capital hike: https://english.mubasher.info/news/4018676/General-Company-for-Silos-EGM-nods-to-EGP-25m-capital-hike/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=575 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- CEFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Middle Egypt Flour Mills summary=Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26; Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend; Middle Egypt Mills reports 23% profit drop in FY19/20
  - Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26: https://english.mubasher.info/news/4601809/Middle-Egypt-Flour-Mills-posts-lower-net-profits-at-EGP-77m-in-9M-25-26/
  - Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend: https://english.mubasher.info/news/3870911/Middle-Egypt-Flour-Mills-shareholders-approve-EGP-3-25-shr-dividend/
  - Middle Egypt Mills reports 23% profit drop in FY19/20: https://english.mubasher.info/news/3703590/Middle-Egypt-Mills-reports-23-profit-drop-in-FY19-20/
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/

## Warnings
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for MILS.CA matches the company but no source/report date was detected.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence for GSSC.CA matches the company but no source/report date was detected.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CEFM.CA matches the company but no source/report date was detected.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
