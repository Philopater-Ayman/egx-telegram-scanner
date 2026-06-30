# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-30T08:51:22.501307+00:00
Generated Cairo: 2026-06-30 11:51
Run timing: target 08:45 Cairo | generated Cairo 2026-06-30 11:51 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-30 11:43

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 183/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 30
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 20.0%
- EGX70 regime: BEARISH / above MA20 42.5% / above MA50 67.5%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- GTWL.CA: liquidity=121364576.0 spike=4.86 score=9.3
- COMI.CA: liquidity=119359048.0 spike=0.2 score=14.17
- MASR.CA: liquidity=103772096.0 spike=1.81 score=20.92
- TMGH.CA: liquidity=101533576.0 spike=0.27 score=14.32
- ORAS.CA: liquidity=87655336.0 spike=1.0 score=4.6

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (9.5%); risk mode is DEFENSIVE_NO_NEW_BUY, so the scanner flags tickets for watch only.
- Tickets were ranked by score, liquidity spikes, and closeness to 20‑day support/resistance (e.g., CSAG.CA near resistance, MHOT.CA strong sector rank but cooling liquidity).
- Liquidity regimes show accumulation spikes in some names (CAED.CA, MASR.CA) but their sectors are not leading, limiting follow‑through potential.
- Outlook scores are bullish‑watch, yet RSI levels and support/resistance distances suggest limited upside over the next 1‑3 days amid uncertainty.
- Defensive risk mode blocks new buys; only HOLD/watch is advised until breadth improves or the regime shifts.

## Top Liquidity Spikes
- AMES.CA: spike=17.53 liquidity=75060136.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=15.07 liquidity=30314146.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=4.86 liquidity=121364576.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GMCI.CA: spike=4.03 liquidity=1617875.0 outlook=BULLISH_WATCH score=76.75 buy_ready=False
- CAED.CA: spike=2.22 liquidity=9214614.0 outlook=BULLISH_WATCH score=88.75 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=8.59 5d=4.84% 20d=1.71% aboveMA50=100.0%
- #2 Automotive & Distribution: score=7.27 5d=2.47% 20d=7.28% aboveMA50=100.0%
- #3 Technology & Distribution: score=5.56 5d=-1.75% 20d=-2.67% aboveMA50=100.0%
- #4 Transportation & Logistics: score=3.78 5d=-0.26% 20d=-2.71% aboveMA50=50.0%
- #5 Textiles: score=2.11 5d=-2.61% 20d=-4.21% aboveMA50=100.0%
- #6 Food, Beverages & Tobacco: score=1.9 5d=-3.15% 20d=-0.4% aboveMA50=57.14%
- #7 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Education: score=0.98 5d=-3.17% 20d=-0.95% aboveMA50=33.33%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CAED.CA: BULLISH_WATCH score=88.75 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CSAG.CA: BULLISH_WATCH score=86.78 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MHOT.CA: BULLISH_WATCH score=80.59 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- RAYA.CA: BULLISH_WATCH score=79.56 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- POUL.CA: BULLISH_WATCH score=77.9 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MASR.CA: BULLISH_WATCH score=76.75 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- AFDI.CA: BULLISH_WATCH score=76.75 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- GMCI.CA: BULLISH_WATCH score=76.75 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance; sector is not leading
- AXPH.CA: BULLISH_WATCH score=76.75 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- MTIE.CA: BULLISH_WATCH score=75.27 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=2.84 buy_ready=False sector_rank=10 price=202.76 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=29.49 liquidity=537637.06 spike=0.09
- ABUK.CA: score=8.0 buy_ready=False sector_rank=20 price=67.24 support=66.66 resistance=84.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=9.05 liquidity=19569722.0 spike=0.14
- ACAMD.CA: score=12.3 buy_ready=False sector_rank=10 price=2.23 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=37784808.0 spike=0.31
- ACGC.CA: score=5.1 buy_ready=False sector_rank=5 price=9.18 support=8.92 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=2253495.25 spike=0.06
- ADCI.CA: score=11.79 buy_ready=False sector_rank=10 price=241.24 support=211.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=84.3 liquidity=3486872.5 spike=0.34
- ADIB.CA: score=14.17 buy_ready=False sector_rank=13 price=45.24 support=44.01 resistance=48.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=13123444.0 spike=0.14
- ADPC.CA: score=5.85 buy_ready=False sector_rank=10 price=3.46 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=2550199.0 spike=0.12
- AFDI.CA: score=19.36 buy_ready=False sector_rank=10 price=44.22 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=15225856.0 spike=1.03
- AFMC.CA: score=0.02 buy_ready=False sector_rank=10 price=67.39 support=66.0 resistance=74.69 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=28.48 liquidity=717029.59 spike=0.42
- AJWA.CA: score=11.02 buy_ready=False sector_rank=10 price=176.56 support=132.0 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=74.49 liquidity=1716453.5 spike=0.06
- ALCN.CA: score=9.18 buy_ready=False sector_rank=4 price=28.56 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=32.53 liquidity=8667856.0 spike=0.71
- ALUM.CA: score=2.33 buy_ready=False sector_rank=10 price=21.21 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=11.73 liquidity=3031975.5 spike=0.32
- AMER.CA: score=9.32 buy_ready=False sector_rank=9 price=2.41 support=2.28 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=19.28 liquidity=53981476.0 spike=0.76
- AMES.CA: score=9.3 buy_ready=False sector_rank=10 price=64.06 support=57.23 resistance=64.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75060136.0 spike=17.53
- AMIA.CA: score=0.47 buy_ready=False sector_rank=10 price=8.48 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=1171119.5 spike=0.09
- AMOC.CA: score=8.16 buy_ready=False sector_rank=15 price=7.61 support=7.42 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=17.54 liquidity=9231844.0 spike=0.19
- ANFI.CA: score=5.63 buy_ready=False sector_rank=10 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=-1.2 buy_ready=False sector_rank=10 price=8.34 support=8.0 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=7.62 liquidity=499536.88 spike=0.56
- ARAB.CA: score=14.32 buy_ready=False sector_rank=9 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=10994588.0 spike=0.13
- ARCC.CA: score=3.5 buy_ready=False sector_rank=16 price=54.67 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=27.87 liquidity=4627367.5 spike=0.14
- AREH.CA: score=13.3 buy_ready=False sector_rank=10 price=1.55 support=1.34 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=3995036.0 spike=0.12
- ARVA.CA: score=10.26 buy_ready=False sector_rank=10 price=10.93 support=9.43 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=46.86 liquidity=2955107.0 spike=0.09
- ASCM.CA: score=19.3 buy_ready=False sector_rank=10 price=60.2 support=47.7 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=54.53 liquidity=25114482.0 spike=0.27
- ASPI.CA: score=9.05 buy_ready=False sector_rank=10 price=0.31 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=29.06 liquidity=6754303.5 spike=0.09
- ATLC.CA: score=9.67 buy_ready=False sector_rank=12 price=5.11 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=482677.0 spike=0.08
- ATQA.CA: score=8.08 buy_ready=False sector_rank=20 price=9.49 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=36.19 liquidity=6075140.5 spike=0.18
- AXPH.CA: score=11.36 buy_ready=False sector_rank=10 price=1117.31 support=1073.0 resistance=1174.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=42.94 liquidity=1580993.73 spike=1.24
- BINV.CA: score=7.07 buy_ready=False sector_rank=17 price=45.55 support=44.02 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=39.7 liquidity=309548.5 spike=0.03
- BIOC.CA: score=6.42 buy_ready=False sector_rank=10 price=68.17 support=66.75 resistance=75.5 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=35.71 liquidity=2120973.15 spike=0.9
- BTFH.CA: score=13.19 buy_ready=False sector_rank=12 price=3.01 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=57062648.0 spike=0.31
- CAED.CA: score=20.95 buy_ready=False sector_rank=10 price=73.35 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=44.96 liquidity=9214614.0 spike=2.22
- CANA.CA: score=10.45 buy_ready=False sector_rank=13 price=35.26 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=7276884.0 spike=0.67
- CCAP.CA: score=8.76 buy_ready=False sector_rank=17 price=4.81 support=4.65 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=18.55 liquidity=77109072.0 spike=0.11
- CCRS.CA: score=2.82 buy_ready=False sector_rank=10 price=2.26 support=2.22 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=516581.06 spike=0.03
- CEFM.CA: score=1.96 buy_ready=False sector_rank=10 price=96.96 support=95.75 resistance=109.89 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=20.18 liquidity=2319574.06 spike=1.67
- CERA.CA: score=7.05 buy_ready=False sector_rank=10 price=1.21 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=754138.44 spike=0.05
- CFGH.CA: score=-1.7 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4880.0 spike=0.79
- CICH.CA: score=8.11 buy_ready=False sector_rank=12 price=11.76 support=11.1 resistance=12.8 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=48.77 liquidity=1919655.4 spike=0.74
- CIEB.CA: score=4.95 buy_ready=False sector_rank=13 price=23.69 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=776260.13 spike=0.12
- CIRA.CA: score=14.4 buy_ready=False sector_rank=8 price=28.18 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=61.39 liquidity=5009323.5 spike=0.29
- CLHO.CA: score=12.16 buy_ready=False sector_rank=11 price=16.25 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=66.94 liquidity=2872355.0 spike=0.08
- CNFN.CA: score=17.23 buy_ready=False sector_rank=12 price=4.75 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=53.55 liquidity=6039213.5 spike=0.15
- COMI.CA: score=14.17 buy_ready=False sector_rank=13 price=128.6 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=119359048.0 spike=0.2
- COPR.CA: score=8.03 buy_ready=False sector_rank=10 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=1734438.62 spike=0.06
- COSG.CA: score=6.02 buy_ready=False sector_rank=10 price=1.52 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=6716575.0 spike=0.12
- CPCI.CA: score=13.45 buy_ready=False sector_rank=10 price=391.93 support=350.04 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=71.98 liquidity=2154415.25 spike=0.91
- CSAG.CA: score=24.89 buy_ready=False sector_rank=4 price=33.05 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=61.3 liquidity=19708294.0 spike=1.19
- DAPH.CA: score=9.1 buy_ready=False sector_rank=10 price=80.59 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=795347.38 spike=0.08
- DEIN.CA: score=5.3 buy_ready=False sector_rank=10 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=10.71 buy_ready=False sector_rank=6 price=26.95 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=70.34 liquidity=952880.19 spike=0.24
- DSCW.CA: score=6.73 buy_ready=False sector_rank=10 price=1.72 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=3431381.0 spike=0.1
- DTPP.CA: score=9.3 buy_ready=False sector_rank=10 price=166.05 support=153.55 resistance=166.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30314146.0 spike=15.07
- EALR.CA: score=1.55 buy_ready=False sector_rank=10 price=341.31 support=332.0 resistance=380.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=25.74 liquidity=2252304.67 spike=0.92
- EASB.CA: score=9.39 buy_ready=False sector_rank=10 price=7.6 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=75.15 liquidity=3094881.25 spike=0.24
- EAST.CA: score=4.74 buy_ready=False sector_rank=6 price=36.92 support=36.86 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=31.93 liquidity=5982625.5 spike=0.16
- EBSC.CA: score=4.9 buy_ready=False sector_rank=10 price=1.74 support=1.69 resistance=2.09 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=37.5 liquidity=601093.44 spike=0.23
- ECAP.CA: score=10.53 buy_ready=False sector_rank=10 price=32.4 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=54.65 liquidity=1227145.88 spike=0.14
- EDFM.CA: score=-0.45 buy_ready=False sector_rank=10 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=30.71 liquidity=253893.12 spike=0.52
- EEII.CA: score=11.85 buy_ready=False sector_rank=10 price=2.42 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=2548242.5 spike=0.19
- EFIC.CA: score=-2.55 buy_ready=False sector_rank=20 price=189.93 support=189.01 resistance=212.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=6.38 liquidity=450325.13 spike=0.23
- EFID.CA: score=9.16 buy_ready=False sector_rank=6 price=27.32 support=25.5 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=41.64 liquidity=4398402.5 spike=0.06
- EFIH.CA: score=4.46 buy_ready=False sector_rank=21 price=20.34 support=20.0 resistance=22.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=36.37 liquidity=1764361.13 spike=0.04
- EGAL.CA: score=8.0 buy_ready=False sector_rank=20 price=283.68 support=272.28 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=10.71 liquidity=18987884.0 spike=0.3
- EGAS.CA: score=7.89 buy_ready=False sector_rank=15 price=49.47 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=966134.13 spike=0.1
- EGBE.CA: score=9.18 buy_ready=False sector_rank=13 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11861.59 spike=0.14
- EGCH.CA: score=5.47 buy_ready=False sector_rank=20 price=12.39 support=12.13 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=19.35 liquidity=7464462.5 spike=0.14
- EGSA.CA: score=7.07 buy_ready=False sector_rank=14 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=5801.25 spike=0.62
- EGTS.CA: score=5.24 buy_ready=False sector_rank=9 price=16.93 support=15.1 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=29.08 liquidity=2911520.0 spike=0.03
- EHDR.CA: score=9.56 buy_ready=False sector_rank=10 price=2.48 support=2.32 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=26.74 liquidity=7262421.5 spike=0.12
- EKHO.CA: score=5.93 buy_ready=False sector_rank=15 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=7.43 buy_ready=False sector_rank=19 price=2.08 support=2.05 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=11195522.0 spike=0.59
- ELKA.CA: score=4.3 buy_ready=False sector_rank=10 price=1.3 support=1.21 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27048296.0 spike=0.67
- ELNA.CA: score=-1.32 buy_ready=False sector_rank=10 price=37.8 support=35.55 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=33.43 liquidity=382456.84 spike=0.85
- ELSH.CA: score=17.3 buy_ready=False sector_rank=10 price=11.88 support=9.33 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=25436304.0 spike=0.13
- ELWA.CA: score=2.81 buy_ready=False sector_rank=10 price=2.0 support=1.95 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=505213.28 spike=0.16
- EMFD.CA: score=17.32 buy_ready=False sector_rank=9 price=11.58 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=27325420.0 spike=0.1
- ENGC.CA: score=14.75 buy_ready=False sector_rank=10 price=36.11 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=56.36 liquidity=3454175.25 spike=0.24
- EOSB.CA: score=11.34 buy_ready=False sector_rank=10 price=1.48 support=1.39 resistance=1.55 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=36743.96 spike=0.28
- EPCO.CA: score=0.14 buy_ready=False sector_rank=10 price=8.77 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=28.31 liquidity=842330.31 spike=0.1
- EPPK.CA: score=12.06 buy_ready=False sector_rank=10 price=13.67 support=11.67 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=70.53 liquidity=1702479.63 spike=1.53
- ETEL.CA: score=13.09 buy_ready=False sector_rank=14 price=91.3 support=89.01 resistance=97.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=35.42 liquidity=9034971.0 spike=0.13
- ETRS.CA: score=4.3 buy_ready=False sector_rank=10 price=10.99 support=10.9 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61050208.0 spike=0.83
- EXPA.CA: score=1.42 buy_ready=False sector_rank=13 price=18.27 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=27.33 liquidity=2245574.0 spike=0.07
- FAIT.CA: score=11.76 buy_ready=False sector_rank=13 price=37.09 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=43.7 liquidity=2587936.25 spike=0.9
- FAITA.CA: score=4.18 buy_ready=False sector_rank=13 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=8009.67 spike=0.2
- FERC.CA: score=-1.1 buy_ready=False sector_rank=20 price=72.96 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=12.94 liquidity=1899425.75 spike=0.5
- FWRY.CA: score=12.69 buy_ready=False sector_rank=21 price=18.54 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=46964568.0 spike=0.19
- GBCO.CA: score=20.4 buy_ready=False sector_rank=2 price=31.9 support=25.25 resistance=32.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=83.43 liquidity=24416854.0 spike=0.27
- GDWA.CA: score=5.87 buy_ready=False sector_rank=10 price=0.76 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=7571293.0 spike=0.54
- GGCC.CA: score=17.25 buy_ready=False sector_rank=10 price=0.47 support=0.4 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=67.68 liquidity=6954109.5 spike=0.61
- GIHD.CA: score=8.99 buy_ready=False sector_rank=10 price=41.51 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=46.44 liquidity=1690683.0 spike=0.21
- GMCI.CA: score=15.92 buy_ready=False sector_rank=10 price=1.81 support=1.66 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=1617875.0 spike=4.03
- GRCA.CA: score=7.13 buy_ready=False sector_rank=10 price=52.78 support=50.2 resistance=60.5 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=42.98 liquidity=2825313.33 spike=0.74
- GSSC.CA: score=-0.23 buy_ready=False sector_rank=10 price=243.15 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=23.83 liquidity=472639.22 spike=0.16
- GTWL.CA: score=9.3 buy_ready=False sector_rank=10 price=88.2 support=76.25 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=121364576.0 spike=4.86
- HDBK.CA: score=19.17 buy_ready=False sector_rank=13 price=159.91 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=66.54 liquidity=25361934.0 spike=0.89
- HELI.CA: score=17.32 buy_ready=False sector_rank=9 price=6.44 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=15391459.0 spike=0.13
- HRHO.CA: score=13.19 buy_ready=False sector_rank=12 price=26.69 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=11842712.0 spike=0.09
- ICID.CA: score=11.84 buy_ready=False sector_rank=10 price=7.75 support=5.24 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=61.75 liquidity=535521.69 spike=0.03
- IDRE.CA: score=3.77 buy_ready=False sector_rank=10 price=42.38 support=41.1 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=33.22 liquidity=1465560.63 spike=0.11
- IFAP.CA: score=3.21 buy_ready=False sector_rank=18 price=19.04 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=40.08 liquidity=474371.56 spike=0.07
- INFI.CA: score=-0.6 buy_ready=False sector_rank=10 price=89.98 support=88.51 resistance=105.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=9.75 liquidity=1101297.38 spike=0.18
- IRON.CA: score=9.52 buy_ready=False sector_rank=20 price=33.02 support=30.51 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=5512504.5 spike=0.72
- ISMA.CA: score=4.89 buy_ready=False sector_rank=10 price=29.0 support=25.99 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=33.55 liquidity=2592476.25 spike=0.07
- ISMQ.CA: score=20.0 buy_ready=False sector_rank=20 price=9.1 support=7.56 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=68.24 liquidity=24643976.0 spike=0.21
- ISPH.CA: score=14.29 buy_ready=False sector_rank=11 price=11.59 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=36.75 liquidity=14147501.0 spike=0.12
- JUFO.CA: score=11.01 buy_ready=False sector_rank=6 price=29.6 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=3251974.25 spike=0.1
- KABO.CA: score=11.09 buy_ready=False sector_rank=5 price=6.25 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=3244073.75 spike=0.2
- KWIN.CA: score=6.25 buy_ready=False sector_rank=10 price=67.8 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=2946301.75 spike=0.26
- KZPC.CA: score=-0.94 buy_ready=False sector_rank=10 price=8.39 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=12.29 liquidity=759176.25 spike=0.12
- LCSW.CA: score=20.88 buy_ready=False sector_rank=16 price=28.18 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=12460728.0 spike=0.43
- LUTS.CA: score=19.08 buy_ready=False sector_rank=10 price=0.73 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=64.74 liquidity=9783653.0 spike=0.21
- MAAL.CA: score=13.85 buy_ready=False sector_rank=10 price=7.19 support=5.25 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=77.89 liquidity=5554798.5 spike=0.31
- MASR.CA: score=20.92 buy_ready=False sector_rank=10 price=7.4 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=55.61 liquidity=103772096.0 spike=1.81
- MBSC.CA: score=7.71 buy_ready=False sector_rank=16 price=237.4 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=14.67 liquidity=8836497.0 spike=0.26
- MCQE.CA: score=2.74 buy_ready=False sector_rank=16 price=170.1 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=24.62 liquidity=3862192.5 spike=0.27
- MCRO.CA: score=4.9 buy_ready=False sector_rank=10 price=1.21 support=1.17 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=6600098.0 spike=0.19
- MENA.CA: score=7.65 buy_ready=False sector_rank=9 price=6.77 support=6.32 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=323199.78 spike=0.02
- MEPA.CA: score=0.77 buy_ready=False sector_rank=10 price=1.57 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=2468101.75 spike=0.22
- MFPC.CA: score=8.0 buy_ready=False sector_rank=20 price=35.01 support=34.22 resistance=43.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=9.0 liquidity=16474753.0 spike=0.19
- MFSC.CA: score=10.45 buy_ready=False sector_rank=10 price=47.44 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=51.33 liquidity=1152184.5 spike=0.13
- MHOT.CA: score=20.66 buy_ready=False sector_rank=1 price=34.45 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=4262833.0 spike=0.21
- MICH.CA: score=8.59 buy_ready=False sector_rank=10 price=36.43 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=1286062.0 spike=0.08
- MILS.CA: score=0.54 buy_ready=False sector_rank=10 price=128.43 support=126.5 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=29.31 liquidity=1243978.13 spike=0.13
- MIPH.CA: score=5.66 buy_ready=False sector_rank=11 price=651.64 support=630.13 resistance=710.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=46.04 liquidity=1373657.15 spike=0.84
- MOED.CA: score=0.83 buy_ready=False sector_rank=10 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=34.35 liquidity=2526271.0 spike=0.27
- MOIL.CA: score=6.94 buy_ready=False sector_rank=15 price=0.47 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=14086.67 spike=0.07
- MOIN.CA: score=-1.68 buy_ready=False sector_rank=10 price=23.03 support=22.6 resistance=25.66 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=21740.32 spike=0.04
- MOSC.CA: score=10.89 buy_ready=False sector_rank=10 price=280.74 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=1585307.5 spike=0.17
- MPCI.CA: score=19.3 buy_ready=False sector_rank=10 price=238.78 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=54.8 liquidity=17737246.0 spike=0.19
- MPCO.CA: score=16.74 buy_ready=False sector_rank=18 price=1.79 support=1.6 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=20109346.0 spike=0.19
- MPRC.CA: score=10.16 buy_ready=False sector_rank=10 price=38.5 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=77.97 liquidity=3857485.5 spike=0.09
- MTIE.CA: score=14.02 buy_ready=False sector_rank=2 price=9.02 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=42.65 liquidity=2618313.75 spike=0.16
- NAHO.CA: score=5.32 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=15679.68 spike=0.44
- NCCW.CA: score=7.66 buy_ready=False sector_rank=10 price=6.14 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=5363581.5 spike=0.16
- NEDA.CA: score=-0.61 buy_ready=False sector_rank=10 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=92390.06 spike=0.25
- NHPS.CA: score=-0.54 buy_ready=False sector_rank=10 price=63.3 support=61.55 resistance=68.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=33.72 liquidity=1163104.25 spike=0.33
- NINH.CA: score=9.83 buy_ready=False sector_rank=10 price=17.9 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=50.18 liquidity=1531623.63 spike=0.37
- NIPH.CA: score=17.05 buy_ready=False sector_rank=11 price=163.1 support=157.01 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=9766701.0 spike=0.14
- OBRI.CA: score=9.3 buy_ready=False sector_rank=10 price=33.51 support=31.5 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=10799457.0 spike=0.76
- OCDI.CA: score=15.33 buy_ready=False sector_rank=9 price=24.58 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=66.71 liquidity=6010731.0 spike=0.08
- OCPH.CA: score=12.55 buy_ready=False sector_rank=10 price=356.02 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=3252676.75 spike=0.52
- ODIN.CA: score=9.51 buy_ready=False sector_rank=10 price=2.08 support=1.94 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=38.3 liquidity=2207442.0 spike=0.2
- OFH.CA: score=1.48 buy_ready=False sector_rank=10 price=0.59 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=22.09 liquidity=3176928.75 spike=0.17
- OIH.CA: score=17.76 buy_ready=False sector_rank=17 price=1.41 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=15435812.0 spike=0.2
- OLFI.CA: score=19.76 buy_ready=False sector_rank=6 price=22.29 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=53.18 liquidity=10215749.0 spike=0.49
- ORAS.CA: score=4.6 buy_ready=False sector_rank=7 price=724.92 support=704.52 resistance=725.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87655336.0 spike=1.0
- ORHD.CA: score=19.32 buy_ready=False sector_rank=9 price=38.1 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=53.68 liquidity=49697412.0 spike=0.29
- ORWE.CA: score=7.61 buy_ready=False sector_rank=5 price=22.48 support=21.95 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=19.64 liquidity=4762072.5 spike=0.13
- PHAR.CA: score=10.15 buy_ready=False sector_rank=11 price=86.09 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=43.72 liquidity=2864401.5 spike=0.08
- PHDC.CA: score=17.32 buy_ready=False sector_rank=9 price=14.8 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=44.1 liquidity=71790168.0 spike=0.18
- PHTV.CA: score=9.03 buy_ready=False sector_rank=10 price=269.88 support=201.55 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=90.82 liquidity=733898.5 spike=0.05
- POUL.CA: score=16.48 buy_ready=False sector_rank=6 price=37.57 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=4715607.0 spike=0.13
- PRCL.CA: score=18.88 buy_ready=False sector_rank=16 price=30.86 support=22.86 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=68.92 liquidity=23529546.0 spike=0.58
- PRDC.CA: score=17.32 buy_ready=False sector_rank=9 price=7.35 support=5.86 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=13863823.0 spike=0.12
- PRMH.CA: score=10.76 buy_ready=False sector_rank=10 price=2.48 support=2.28 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=38.26 liquidity=3459732.0 spike=0.11
- RACC.CA: score=5.64 buy_ready=False sector_rank=10 price=9.67 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=36.84 liquidity=1340234.25 spike=0.14
- RAKT.CA: score=-1.66 buy_ready=False sector_rank=10 price=22.43 support=21.96 resistance=24.1 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=30.46 liquidity=39454.37 spike=0.15
- RAYA.CA: score=22.22 buy_ready=False sector_rank=3 price=7.64 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=44532516.0 spike=0.53
- RMDA.CA: score=7.38 buy_ready=False sector_rank=11 price=4.99 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=30.3 liquidity=5087400.5 spike=0.07
- ROTO.CA: score=19.3 buy_ready=False sector_rank=10 price=41.02 support=33.0 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=66.01 liquidity=11211016.0 spike=0.38
- RREI.CA: score=8.26 buy_ready=False sector_rank=10 price=3.47 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=41.1 liquidity=3964098.5 spike=0.24
- RTVC.CA: score=4.0 buy_ready=False sector_rank=10 price=3.8 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=4699090.0 spike=0.92
- RUBX.CA: score=21.3 buy_ready=False sector_rank=10 price=11.25 support=9.8 resistance=12.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=61.35 liquidity=12013431.0 spike=0.67
- SAUD.CA: score=0.27 buy_ready=False sector_rank=13 price=20.61 support=19.99 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=1094322.0 spike=0.13
- SCEM.CA: score=4.53 buy_ready=False sector_rank=16 price=61.23 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=38.22 liquidity=654000.75 spike=0.04
- SCFM.CA: score=-0.31 buy_ready=False sector_rank=10 price=237.47 support=226.5 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=388888.94 spike=0.09
- SCTS.CA: score=0.29 buy_ready=False sector_rank=8 price=552.43 support=540.0 resistance=630.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=3.24 liquidity=893925.25 spike=0.29
- SDTI.CA: score=8.35 buy_ready=False sector_rank=10 price=46.01 support=44.17 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:58 AM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=1052694.88 spike=0.09
- SEIG.CA: score=9.69 buy_ready=False sector_rank=10 price=188.55 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=36.97 liquidity=391433.63 spike=0.09
- SIPC.CA: score=1.34 buy_ready=False sector_rank=10 price=3.3 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=23.88 liquidity=2041156.75 spike=0.18
- SKPC.CA: score=2.06 buy_ready=False sector_rank=20 price=15.98 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=24.44 liquidity=5051839.0 spike=0.15
- SMFR.CA: score=-0.21 buy_ready=False sector_rank=10 price=190.82 support=187.01 resistance=214.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=27.39 liquidity=486591.02 spike=0.27
- SNFC.CA: score=6.03 buy_ready=False sector_rank=10 price=11.88 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=1734938.0 spike=0.1
- SPIN.CA: score=13.08 buy_ready=False sector_rank=5 price=14.27 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=53.9 liquidity=1239323.25 spike=0.21
- SPMD.CA: score=11.46 buy_ready=False sector_rank=10 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=4155265.0 spike=0.17
- SUGR.CA: score=0.91 buy_ready=False sector_rank=6 price=46.48 support=45.31 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=15.05 liquidity=2149144.25 spike=0.29
- SVCE.CA: score=11.56 buy_ready=False sector_rank=10 price=8.97 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=53.31 liquidity=4263507.5 spike=0.07
- SWDY.CA: score=7.46 buy_ready=False sector_rank=19 price=85.77 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=4023673.25 spike=0.23
- TALM.CA: score=-0.18 buy_ready=False sector_rank=8 price=15.77 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:45 AM market time freshness=DELAYED_CURRENT RSI=28.89 liquidity=431319.34 spike=0.06
- TMGH.CA: score=14.32 buy_ready=False sector_rank=9 price=94.52 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=37.8 liquidity=101533576.0 spike=0.27
- TRTO.CA: score=5.3 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=235.59 spike=0.33
- UEFM.CA: score=7.43 buy_ready=False sector_rank=10 price=470.0 support=460.0 resistance=505.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=47.13 liquidity=1309420.0 spike=1.41
- UEGC.CA: score=12.88 buy_ready=False sector_rank=10 price=1.4 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=5581218.0 spike=0.23
- UNIP.CA: score=8.13 buy_ready=False sector_rank=10 price=0.32 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=831132.44 spike=0.03
- UNIT.CA: score=4.4 buy_ready=False sector_rank=9 price=13.05 support=12.0 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=16.59 liquidity=2074166.5 spike=0.33
- WCDF.CA: score=5.42 buy_ready=False sector_rank=10 price=518.05 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=38.07 liquidity=396308.24 spike=1.36
- WKOL.CA: score=1.34 buy_ready=False sector_rank=10 price=280.06 support=273.1 resistance=312.0 source=Yahoo Finance as_of=2026-06-28T21:00:00+00:00 freshness=FRESH RSI=17.3 liquidity=2043877.86 spike=0.84
- ZEOT.CA: score=19.12 buy_ready=False sector_rank=10 price=10.96 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=66.72 liquidity=9815998.0 spike=0.32
- ZMID.CA: score=19.32 buy_ready=False sector_rank=9 price=6.3 support=5.96 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=23656190.0 spike=0.11

## Backtesting Lite
- CSAG.CA: 180d return=13.61%, max drawdown=-28.0%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- RAYA.CA: 180d return=153.47%, max drawdown=-12.86%, MA20>MA50 days last20=20, as_of=2026-06-28T21:00:00+00:00
- RUBX.CA: 180d return=6.45%, max drawdown=-21.39%, MA20>MA50 days last20=9, as_of=2026-06-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- CAED.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Educational Services SAE summary=Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution; Cairo Educational Services’ board proposes 80 piastres per-share dividends; Cairo Educational Services’ profit declines in FY18/19
  - Cairo Educational Services&#39; OGM approves EGP 1/shr coupon distribution: https://english.mubasher.info/news/3884789/Cairo-Educational-Services-OGM-approves-EGP-1-shr-coupon-distribution/
  - Cairo Educational Services’ board proposes 80 piastres per-share dividends: https://english.mubasher.info/news/3556129/Cairo-Educational-Services-board-proposes-80-piastres-per-share-dividends/
  - Cairo Educational Services’ profit declines in FY18/19: https://english.mubasher.info/news/3556119/Cairo-Educational-Services-profit-declines-in-FY18-19/
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=545 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.

## Warnings
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for CAED.CA matches the company but no source/report date was detected.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
