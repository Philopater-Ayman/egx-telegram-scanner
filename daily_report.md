# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-23T08:48:28.150900+00:00
Generated Cairo: 2026-06-23 11:48
Run timing: target 08:45 Cairo | generated Cairo 2026-06-23 11:48 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-23 11:45

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 48
- Data quality issues: 0
- Tradeable price/liquidity tickers: 173/190
- Top sector: Healthcare

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 23
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 45.0% / above MA50 55.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 50.0% / above MA50 75.0%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- CNFN.CA: liquidity=298207712.0 spike=18.19 score=35.4
- CCAP.CA: liquidity=287820416.0 spike=0.37 score=21.3
- ASCM.CA: liquidity=211389648.0 spike=3.17 score=13.11
- ZMID.CA: liquidity=140029680.0 spike=0.68 score=24.4
- COMI.CA: liquidity=117727032.0 spike=0.2 score=27.42

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner found no trade‑ready candidates; all tickets are HOLD. EGX30 shows a mixed regime with weak breadth below MA20, while EGX70 remains constructive with solid breadth. Sector breadth is modest (≈43%). Risk mode is SELECTIVE_SMALL_MID_SWINGS, meaning only high‑conviction, low‑risk moves would be taken – none met the evidence, liquidity, freshness, and technical gates.
- EGX30 mixed trend, <50% of stocks above MA20 → higher short‑term uncertainty.
- EGX70 constructive, 75% above MA50 → broader market support for mid‑term moves.
- Healthcare and Non‑bank Financial Services lead sector breadth, but no ticket cleared all filters.
- Liquidity spikes observed (e.g., CNFN.CA) but proximity to resistance adds short‑term risk.
- Overall outlook remains cautious; monitor sector momentum and index breadth for any breakout.

## Top Liquidity Spikes
- CNFN.CA: spike=18.19 liquidity=298207712.0 outlook=BULLISH_WATCH score=100 buy_ready=True
- GIHD.CA: spike=12.52 liquidity=39637420.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DOMT.CA: spike=8.05 liquidity=17038986.0 outlook=BULLISH_WATCH score=87.88 buy_ready=True
- NINH.CA: spike=4.1 liquidity=18431198.0 outlook=CONSTRUCTIVE score=66.42 buy_ready=False
- OCPH.CA: spike=3.45 liquidity=18624086.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Healthcare: score=7.97 5d=3.13% 20d=5.12% aboveMA50=100.0%
- #2 Non-bank Financial Services: score=7.52 5d=3.31% 20d=2.68% aboveMA50=80.0%
- #3 Education: score=6.53 5d=-0.06% 20d=5.23% aboveMA50=100.0%
- #4 Real Estate: score=6.08 5d=1.63% 20d=5.26% aboveMA50=84.62%
- #5 Industrial Goods & Cables: score=5.21 5d=1.46% 20d=1.89% aboveMA50=50.0%
- #6 Technology & Distribution: score=5.13 5d=6.14% 20d=-2.88% aboveMA50=100.0%
- #7 Agriculture & Food Production: score=4.88 5d=-1.64% 20d=8.88% aboveMA50=50.0%
- #8 Telecommunications: score=4.79 5d=1.51% 20d=-3.06% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CNFN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- OCDI.CA: BULLISH_WATCH score=95.08 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- NIPH.CA: BULLISH_WATCH score=93.97 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CLHO.CA: BULLISH_WATCH score=92.97 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- CIRA.CA: BULLISH_WATCH score=91.53 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- PHAR.CA: BULLISH_WATCH score=89.97 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; close to resistance
- ISPH.CA: BULLISH_WATCH score=87.97 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- DOMT.CA: BULLISH_WATCH score=87.88 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BTFH.CA: BULLISH_WATCH score=87.52 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MASR.CA: BULLISH_WATCH score=83.42 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- CNFN.CA: rank=35.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=4.83 support=4.36 resistance=4.88 liquidity=298207712.0
- DOMT.CA: rank=32.55 outlook=BULLISH_WATCH outlook_score=87.88 sector_rank=11 price=27.34 support=23.7 resistance=26.3 liquidity=17038986.0
- CLHO.CA: rank=30.72 outlook=BULLISH_WATCH outlook_score=92.97 sector_rank=1 price=16.6 support=14.25 resistance=16.85 liquidity=68127912.0
- OCDI.CA: rank=30.32 outlook=BULLISH_WATCH outlook_score=95.08 sector_rank=4 price=22.76 support=20.0 resistance=22.49 liquidity=72630936.0
- ISPH.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=87.97 sector_rank=1 price=12.35 support=11.3 resistance=12.74 liquidity=14480853.0
- MPRC.CA: rank=28.47 outlook=BULLISH_WATCH outlook_score=80.42 sector_rank=9 price=34.96 support=30.61 resistance=34.55 liquidity=50369592.0
- BTFH.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=87.52 sector_rank=2 price=3.09 support=2.96 resistance=3.23 liquidity=40346972.0
- MASR.CA: rank=27.77 outlook=BULLISH_WATCH outlook_score=83.42 sector_rank=9 price=7.19 support=6.54 resistance=7.69 liquidity=28000084.0
- COMI.CA: rank=27.42 outlook=CONSTRUCTIVE outlook_score=62.54 sector_rank=12 price=135.34 support=129.8 resistance=137.07 liquidity=117727032.0
- NIPH.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=93.97 sector_rank=1 price=168.27 support=157.1 resistance=176.9 liquidity=23937684.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=14.58 buy_ready=False sector_rank=9 price=208.25 support=199.25 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=813498.38 spike=0.13
- ABUK.CA: score=12.28 buy_ready=False sector_rank=20 price=68.79 support=70.5 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=8.05 liquidity=24657958.0 spike=0.17
- ACAMD.CA: score=21.77 buy_ready=False sector_rank=9 price=2.31 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=55.74 liquidity=42870144.0 spike=0.34
- ACGC.CA: score=13.21 buy_ready=False sector_rank=14 price=9.52 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=2353384.5 spike=0.04
- ADCI.CA: score=19.6 buy_ready=False sector_rank=9 price=240.46 support=211.0 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=79.84 liquidity=6834647.0 spike=0.88
- ADIB.CA: score=18.42 buy_ready=False sector_rank=12 price=46.32 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=14002491.0 spike=0.13
- ADPC.CA: score=24.24 buy_ready=True sector_rank=9 price=3.8 support=3.45 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=67.03 liquidity=8470571.0 spike=0.32
- AFDI.CA: score=10.61 buy_ready=False sector_rank=9 price=46.6 support=46.52 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26196612.0 spike=1.92
- AFMC.CA: score=9.23 buy_ready=False sector_rank=9 price=70.22 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=464283.34 spike=0.1
- AJWA.CA: score=19.06 buy_ready=False sector_rank=9 price=180.47 support=130.01 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=84.42 liquidity=8291245.0 spike=0.31
- ALCN.CA: score=4.09 buy_ready=False sector_rank=17 price=28.09 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=34.02 liquidity=1476226.25 spike=0.1
- ALUM.CA: score=13.21 buy_ready=False sector_rank=9 price=23.62 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=1445418.0 spike=0.13
- AMER.CA: score=14.4 buy_ready=False sector_rank=4 price=2.4 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=26522544.0 spike=0.3
- AMES.CA: score=12.03 buy_ready=False sector_rank=9 price=49.96 support=48.0 resistance=53.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=35.12 liquidity=1262854.63 spike=0.36
- AMIA.CA: score=12.66 buy_ready=False sector_rank=9 price=8.79 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=54.63 liquidity=896223.44 spike=0.06
- AMOC.CA: score=13.76 buy_ready=False sector_rank=10 price=7.73 support=7.71 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=17.2 liquidity=12918828.0 spike=0.18
- ANFI.CA: score=14.04 buy_ready=False sector_rank=9 price=33.12 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=76.32 liquidity=3274408.69 spike=0.04
- APSW.CA: score=3.15 buy_ready=False sector_rank=9 price=8.58 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=21.33 liquidity=378426.69 spike=0.41
- ARAB.CA: score=24.4 buy_ready=False sector_rank=4 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=20868990.0 spike=0.24
- ARCC.CA: score=15.47 buy_ready=False sector_rank=19 price=55.31 support=54.31 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=38.83 liquidity=4958564.5 spike=0.14
- AREH.CA: score=22.51 buy_ready=False sector_rank=9 price=1.6 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=80.85 liquidity=9744043.0 spike=0.31
- ARVA.CA: score=23.77 buy_ready=True sector_rank=9 price=11.18 support=7.81 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=11050756.0 spike=0.34
- ASCM.CA: score=13.11 buy_ready=False sector_rank=9 price=67.28 support=66.52 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=211389648.0 spike=3.17
- ASPI.CA: score=22.18 buy_ready=True sector_rank=9 price=0.32 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=60.96 liquidity=8411822.0 spike=0.12
- ATLC.CA: score=24.07 buy_ready=True sector_rank=2 price=5.3 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=5590643.5 spike=1.04
- ATQA.CA: score=9.79 buy_ready=False sector_rank=20 price=9.38 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=45.49 liquidity=3513845.75 spike=0.1
- AXPH.CA: score=11.77 buy_ready=False sector_rank=9 price=1118.16 support=1073.0 resistance=1174.0 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=47.39 liquidity=0.0 spike=0.0
- BINV.CA: score=14.08 buy_ready=False sector_rank=13 price=47.41 support=42.9 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=778722.19 spike=0.07
- BIOC.CA: score=12.38 buy_ready=False sector_rank=9 price=72.07 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=46.54 liquidity=608268.38 spike=0.23
- BTFH.CA: score=28.4 buy_ready=True sector_rank=2 price=3.09 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=40346972.0 spike=0.2
- CAED.CA: score=18.74 buy_ready=False sector_rank=9 price=75.25 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=56.39 liquidity=972508.63 spike=0.18
- CANA.CA: score=17.2 buy_ready=True sector_rank=12 price=37.02 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=62.15 liquidity=1784663.75 spike=0.18
- CCAP.CA: score=21.3 buy_ready=False sector_rank=13 price=5.18 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=287820416.0 spike=0.37
- CCRS.CA: score=17.47 buy_ready=False sector_rank=9 price=2.4 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=47.89 liquidity=5703227.0 spike=0.25
- CEFM.CA: score=4.44 buy_ready=False sector_rank=9 price=101.24 support=100.53 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=27.36 liquidity=674817.0 spike=0.2
- CERA.CA: score=16.31 buy_ready=True sector_rank=9 price=1.24 support=1.14 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=68.0 liquidity=3545484.25 spike=0.22
- CFGH.CA: score=2.77 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- CICH.CA: score=16.43 buy_ready=False sector_rank=2 price=12.0 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=2032764.13 spike=0.57
- CIEB.CA: score=22.48 buy_ready=True sector_rank=12 price=24.39 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=55.74 liquidity=5065667.5 spike=0.75
- CIRA.CA: score=25.4 buy_ready=True sector_rank=3 price=29.0 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=66.92 liquidity=15372292.0 spike=0.84
- CLHO.CA: score=30.72 buy_ready=True sector_rank=1 price=16.6 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=45.29 liquidity=68127912.0 spike=2.66
- CNFN.CA: score=35.4 buy_ready=True sector_rank=2 price=4.83 support=4.36 resistance=4.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=298207712.0 spike=18.19
- COMI.CA: score=27.42 buy_ready=True sector_rank=12 price=135.34 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=117727032.0 spike=0.2
- COPR.CA: score=8.77 buy_ready=False sector_rank=9 price=0.36 support=0.36 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10362708.0 spike=0.24
- COSG.CA: score=21.77 buy_ready=False sector_rank=9 price=1.57 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=10459977.0 spike=0.17
- CPCI.CA: score=14.38 buy_ready=False sector_rank=9 price=373.18 support=346.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=73.6 liquidity=610706.63 spike=0.3
- CSAG.CA: score=12.77 buy_ready=False sector_rank=17 price=31.21 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=47.26 liquidity=2156194.5 spike=0.19
- DAPH.CA: score=15.9 buy_ready=False sector_rank=9 price=80.95 support=76.6 resistance=82.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=52.65 liquidity=1131604.88 spike=0.11
- DEIN.CA: score=9.77 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=32.55 buy_ready=True sector_rank=11 price=27.34 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=61.63 liquidity=17038986.0 spike=8.05
- DSCW.CA: score=21.77 buy_ready=False sector_rank=9 price=1.81 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=10027916.0 spike=0.2
- DTPP.CA: score=3.77 buy_ready=False sector_rank=9 price=117.33 support=114.0 resistance=131.0 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=10.98 liquidity=0.0 spike=0.0
- EALR.CA: score=14.12 buy_ready=False sector_rank=9 price=358.72 support=350.15 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=49.3 liquidity=351542.81 spike=0.1
- EASB.CA: score=4.68 buy_ready=False sector_rank=9 price=7.51 support=7.31 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5908232.0 spike=0.81
- EAST.CA: score=17.54 buy_ready=False sector_rank=11 price=38.5 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=3983398.0 spike=0.09
- EBSC.CA: score=17.1 buy_ready=True sector_rank=9 price=1.83 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=1329730.25 spike=0.5
- ECAP.CA: score=16.67 buy_ready=False sector_rank=9 price=33.81 support=29.36 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=94.89 liquidity=3899928.25 spike=0.64
- EDFM.CA: score=11.77 buy_ready=False sector_rank=9 price=332.0 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=35.25 liquidity=0.0 spike=0.0
- EEII.CA: score=20.67 buy_ready=True sector_rank=9 price=2.42 support=2.29 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=2898255.25 spike=0.17
- EFIC.CA: score=1.28 buy_ready=False sector_rank=20 price=202.08 support=192.01 resistance=213.79 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=23.61 liquidity=0.0 spike=0.0
- EFID.CA: score=12.39 buy_ready=False sector_rank=11 price=27.86 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=33.77 liquidity=8833058.0 spike=0.12
- EFIH.CA: score=11.8 buy_ready=False sector_rank=21 price=21.07 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=37.27 liquidity=5159489.0 spike=0.1
- EGAL.CA: score=12.28 buy_ready=False sector_rank=20 price=290.3 support=294.99 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=13.55 liquidity=41416168.0 spike=0.55
- EGAS.CA: score=13.33 buy_ready=True sector_rank=10 price=51.39 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=68.92 liquidity=1567265.63 spike=0.13
- EGBE.CA: score=11.47 buy_ready=False sector_rank=12 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=50062.53 spike=0.47
- EGCH.CA: score=15.57 buy_ready=False sector_rank=20 price=13.08 support=12.9 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=36.02 liquidity=5290230.5 spike=0.07
- EGSA.CA: score=6.92 buy_ready=False sector_rank=8 price=8.78 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=0.0 spike=0.0
- EGTS.CA: score=17.4 buy_ready=False sector_rank=4 price=18.2 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=11952961.0 spike=0.1
- EHDR.CA: score=16.94 buy_ready=True sector_rank=9 price=2.64 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=5173309.0 spike=0.09
- EKHO.CA: score=13.76 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=11.79 buy_ready=False sector_rank=5 price=2.12 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=1707168.5 spike=0.07
- ELKA.CA: score=26.03 buy_ready=True sector_rank=9 price=1.28 support=1.13 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=9258539.0 spike=0.23
- ELNA.CA: score=8.4 buy_ready=False sector_rank=9 price=38.05 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=51.56 liquidity=434554.38 spike=1.1
- ELSH.CA: score=23.77 buy_ready=True sector_rank=9 price=12.34 support=8.24 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=60.75 liquidity=22391880.0 spike=0.12
- ELWA.CA: score=14.39 buy_ready=False sector_rank=9 price=2.09 support=1.87 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=622881.19 spike=0.2
- EMFD.CA: score=24.4 buy_ready=True sector_rank=4 price=11.86 support=10.4 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=54.13 liquidity=28518478.0 spike=0.1
- ENGC.CA: score=16.77 buy_ready=False sector_rank=9 price=36.92 support=32.61 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=74.34 liquidity=1004435.06 spike=0.07
- EOSB.CA: score=15.77 buy_ready=False sector_rank=9 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=17.41 buy_ready=True sector_rank=9 price=9.23 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=1637452.13 spike=0.17
- EPPK.CA: score=17.77 buy_ready=False sector_rank=9 price=12.68 support=11.67 resistance=13.12 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=57.63 liquidity=0.0 spike=0.0
- ETEL.CA: score=18.92 buy_ready=False sector_rank=8 price=96.39 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=31666024.0 spike=0.4
- ETRS.CA: score=22.77 buy_ready=False sector_rank=9 price=10.41 support=7.65 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=14380463.0 spike=0.23
- EXPA.CA: score=18.64 buy_ready=False sector_rank=12 price=18.6 support=18.21 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=7226255.5 spike=0.21
- FAIT.CA: score=11.42 buy_ready=False sector_rank=12 price=37.11 support=35.01 resistance=38.29 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=42.28 liquidity=0.0 spike=0.0
- FAITA.CA: score=11.42 buy_ready=False sector_rank=12 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- FERC.CA: score=15.56 buy_ready=False sector_rank=20 price=77.5 support=75.0 resistance=79.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=9295511.0 spike=2.49
- FWRY.CA: score=11.64 buy_ready=False sector_rank=21 price=19.0 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=32.04 liquidity=53793420.0 spike=0.19
- GBCO.CA: score=7.82 buy_ready=False sector_rank=15 price=30.83 support=30.78 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12488474.0 spike=0.12
- GDWA.CA: score=14.34 buy_ready=False sector_rank=9 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=4574326.0 spike=0.33
- GGCC.CA: score=19.48 buy_ready=True sector_rank=9 price=0.43 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=4707679.5 spike=0.6
- GIHD.CA: score=13.77 buy_ready=False sector_rank=9 price=44.18 support=42.79 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39637420.0 spike=12.52
- GMCI.CA: score=15.77 buy_ready=False sector_rank=9 price=1.77 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=62.5 liquidity=0.0 spike=0.0
- GRCA.CA: score=8.78 buy_ready=False sector_rank=9 price=54.15 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=34.33 liquidity=5007163.5 spike=0.91
- GSSC.CA: score=6.57 buy_ready=False sector_rank=9 price=252.85 support=228.1 resistance=257.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=28.98 liquidity=803083.25 spike=0.17
- GTWL.CA: score=17.56 buy_ready=True sector_rank=9 price=48.88 support=45.47 resistance=52.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=48.56 liquidity=1794998.63 spike=0.27
- HDBK.CA: score=24.68 buy_ready=False sector_rank=12 price=165.0 support=138.0 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=75.16 liquidity=42992416.0 spike=2.13
- HELI.CA: score=22.4 buy_ready=False sector_rank=4 price=6.49 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=21230756.0 spike=0.15
- HRHO.CA: score=25.4 buy_ready=False sector_rank=2 price=27.29 support=25.8 resistance=27.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=20870012.0 spike=0.14
- ICID.CA: score=13.44 buy_ready=False sector_rank=9 price=7.38 support=4.56 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=86.27 liquidity=671232.69 spike=0.04
- IDRE.CA: score=23.77 buy_ready=True sector_rank=9 price=45.19 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=50.46 liquidity=16697859.0 spike=0.92
- IFAP.CA: score=4.5 buy_ready=False sector_rank=7 price=19.09 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=33.05 liquidity=1552882.38 spike=0.23
- INFI.CA: score=8.69 buy_ready=False sector_rank=9 price=95.57 support=93.0 resistance=105.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=12.22 liquidity=5919631.5 spike=0.65
- IRON.CA: score=10.18 buy_ready=False sector_rank=20 price=32.01 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=46.83 liquidity=1904232.88 spike=0.23
- ISMA.CA: score=13.29 buy_ready=False sector_rank=9 price=29.82 support=25.1 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=81.53 liquidity=4526381.0 spike=0.11
- ISMQ.CA: score=24.28 buy_ready=True sector_rank=20 price=8.2 support=7.31 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=58.1 liquidity=13509149.0 spike=0.18
- ISPH.CA: score=29.4 buy_ready=True sector_rank=1 price=12.35 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=14480853.0 spike=0.11
- JUFO.CA: score=20.89 buy_ready=True sector_rank=11 price=31.3 support=27.6 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=69.51 liquidity=5341384.0 spike=0.13
- KABO.CA: score=9.22 buy_ready=False sector_rank=14 price=6.14 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=1361406.63 spike=0.07
- KWIN.CA: score=3.13 buy_ready=False sector_rank=9 price=68.83 support=67.77 resistance=70.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4363505.5 spike=0.73
- KZPC.CA: score=16.71 buy_ready=False sector_rank=9 price=10.75 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=943252.5 spike=0.12
- LCSW.CA: score=20.49 buy_ready=True sector_rank=19 price=28.17 support=26.0 resistance=28.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=53.08 liquidity=3978355.75 spike=0.4
- LUTS.CA: score=8.77 buy_ready=False sector_rank=9 price=0.75 support=0.75 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13436446.0 spike=0.34
- MAAL.CA: score=13.78 buy_ready=False sector_rank=9 price=6.64 support=4.68 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=80.1 liquidity=1015944.06 spike=0.07
- MASR.CA: score=27.77 buy_ready=True sector_rank=9 price=7.19 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=57.93 liquidity=28000084.0 spike=0.5
- MBSC.CA: score=15.15 buy_ready=False sector_rank=19 price=245.54 support=247.43 resistance=260.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=49.73 liquidity=7638753.0 spike=0.18
- MCQE.CA: score=5.94 buy_ready=False sector_rank=19 price=174.71 support=174.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=22.19 liquidity=3428533.5 spike=0.21
- MCRO.CA: score=11.65 buy_ready=False sector_rank=9 price=1.23 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=8879923.0 spike=0.19
- MENA.CA: score=9.74 buy_ready=False sector_rank=4 price=6.77 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=29.06 liquidity=339925.22 spike=0.02
- MEPA.CA: score=12.39 buy_ready=False sector_rank=9 price=1.66 support=1.66 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=3617843.0 spike=0.21
- MFPC.CA: score=12.28 buy_ready=False sector_rank=20 price=35.42 support=36.76 resistance=44.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=6.41 liquidity=33804796.0 spike=0.36
- MFSC.CA: score=12.17 buy_ready=False sector_rank=9 price=53.9 support=46.99 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32591228.0 spike=2.7
- MHOT.CA: score=8.43 buy_ready=False sector_rank=16 price=36.69 support=36.3 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31685846.0 spike=1.32
- MICH.CA: score=22.37 buy_ready=True sector_rank=9 price=38.1 support=35.31 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=68.78 liquidity=6604436.5 spike=0.41
- MILS.CA: score=12.88 buy_ready=False sector_rank=9 price=137.57 support=131.58 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=48.27 liquidity=1108802.75 spike=0.06
- MIPH.CA: score=21.4 buy_ready=False sector_rank=1 price=694.0 support=648.25 resistance=710.0 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=64.54 liquidity=0.0 spike=0.0
- MOED.CA: score=11.6 buy_ready=False sector_rank=9 price=0.69 support=0.65 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=1827248.12 spike=0.15
- MOIL.CA: score=15.84 buy_ready=False sector_rank=10 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=52.83 liquidity=78741.95 spike=0.49
- MOIN.CA: score=2.77 buy_ready=False sector_rank=9 price=24.09 support=24.01 resistance=25.66 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=14.86 liquidity=0.0 spike=0.0
- MOSC.CA: score=13.23 buy_ready=False sector_rank=9 price=276.2 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=1466248.75 spike=0.17
- MPCI.CA: score=25.77 buy_ready=False sector_rank=9 price=246.6 support=202.3 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=77146432.0 spike=0.95
- MPCO.CA: score=23.95 buy_ready=False sector_rank=7 price=1.95 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=71.6 liquidity=76263712.0 spike=0.78
- MPRC.CA: score=28.47 buy_ready=True sector_rank=9 price=34.96 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=57.87 liquidity=50369592.0 spike=2.35
- MTIE.CA: score=13.34 buy_ready=False sector_rank=15 price=9.1 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=48.87 liquidity=2514883.75 spike=0.14
- NAHO.CA: score=2.77 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=20.0 liquidity=0.0 spike=0.0
- NCCW.CA: score=10.57 buy_ready=False sector_rank=9 price=6.8 support=6.65 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53755976.0 spike=1.9
- NEDA.CA: score=11.77 buy_ready=False sector_rank=9 price=2.77 support=2.65 resistance=2.84 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=56.76 liquidity=0.0 spike=0.0
- NHPS.CA: score=17.89 buy_ready=True sector_rank=9 price=69.01 support=65.03 resistance=71.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=1117295.0 spike=0.25
- NINH.CA: score=23.77 buy_ready=False sector_rank=9 price=18.04 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=32.32 liquidity=18431198.0 spike=4.1
- NIPH.CA: score=27.4 buy_ready=True sector_rank=1 price=168.27 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=23937684.0 spike=0.31
- OBRI.CA: score=16.06 buy_ready=False sector_rank=9 price=34.65 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=48.1 liquidity=5287360.0 spike=0.39
- OCDI.CA: score=30.32 buy_ready=True sector_rank=4 price=22.76 support=20.0 resistance=22.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=72630936.0 spike=1.96
- OCPH.CA: score=13.67 buy_ready=False sector_rank=9 price=361.55 support=346.57 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18624086.0 spike=3.45
- ODIN.CA: score=18.43 buy_ready=True sector_rank=9 price=2.13 support=1.9 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=2662079.5 spike=0.24
- OFH.CA: score=10.02 buy_ready=False sector_rank=9 price=0.6 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=44.66 liquidity=2256499.5 spike=0.1
- OIH.CA: score=13.3 buy_ready=False sector_rank=13 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=78980192.0 spike=0.92
- OLFI.CA: score=19.36 buy_ready=True sector_rank=11 price=22.13 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=5812920.5 spike=0.29
- ORAS.CA: score=7.6 buy_ready=False sector_rank=18 price=803.81 support=800.02 resistance=812.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73523424.0 spike=1.0
- ORHD.CA: score=26.4 buy_ready=True sector_rank=4 price=39.16 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=59.61 liquidity=38465388.0 spike=0.21
- ORWE.CA: score=13.57 buy_ready=False sector_rank=14 price=23.05 support=22.12 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=2712762.5 spike=0.07
- PHAR.CA: score=26.83 buy_ready=True sector_rank=1 price=88.36 support=83.02 resistance=89.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=60.2 liquidity=5425706.5 spike=0.15
- PHDC.CA: score=24.4 buy_ready=True sector_rank=4 price=15.8 support=14.32 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=50648720.0 spike=0.12
- PHTV.CA: score=19.4 buy_ready=False sector_rank=9 price=235.0 support=201.55 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=6629008.0 spike=0.36
- POUL.CA: score=8.91 buy_ready=False sector_rank=11 price=38.36 support=37.6 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39707824.0 spike=1.18
- PRCL.CA: score=7.52 buy_ready=False sector_rank=19 price=29.95 support=28.66 resistance=30.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28705406.0 spike=0.93
- PRDC.CA: score=9.4 buy_ready=False sector_rank=4 price=6.77 support=6.67 resistance=7.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48056176.0 spike=0.48
- PRMH.CA: score=19.88 buy_ready=True sector_rank=9 price=2.78 support=2.23 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=60.55 liquidity=4110034.5 spike=0.15
- RACC.CA: score=25.35 buy_ready=True sector_rank=9 price=10.16 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=43.96 liquidity=17540270.0 spike=1.79
- RAKT.CA: score=7.77 buy_ready=False sector_rank=9 price=22.49 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=39.79 liquidity=0.0 spike=0.0
- RAYA.CA: score=22.05 buy_ready=False sector_rank=6 price=7.3 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=48.55 liquidity=15605243.0 spike=0.17
- RMDA.CA: score=19.01 buy_ready=False sector_rank=1 price=5.05 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=3607510.75 spike=0.04
- ROTO.CA: score=23.81 buy_ready=False sector_rank=9 price=43.36 support=32.66 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=84.24 liquidity=37666708.0 spike=1.52
- RREI.CA: score=17.57 buy_ready=True sector_rank=9 price=3.62 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=1799430.25 spike=0.09
- RTVC.CA: score=13.82 buy_ready=False sector_rank=9 price=3.86 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=1051848.38 spike=0.21
- RUBX.CA: score=2.25 buy_ready=False sector_rank=9 price=10.54 support=10.36 resistance=10.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3486696.75 spike=0.32
- SAUD.CA: score=3.82 buy_ready=False sector_rank=12 price=21.71 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=32.06 liquidity=406464.59 spike=0.04
- SCEM.CA: score=3.93 buy_ready=False sector_rank=19 price=61.32 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=1412562.0 spike=0.07
- SCFM.CA: score=5.87 buy_ready=False sector_rank=9 price=242.6 support=248.1 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=23.66 liquidity=2098205.0 spike=0.19
- SCTS.CA: score=10.07 buy_ready=False sector_rank=3 price=598.62 support=565.25 resistance=648.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=28.59 liquidity=1673905.0 spike=0.34
- SDTI.CA: score=16.37 buy_ready=False sector_rank=9 price=47.15 support=43.6 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=71.18 liquidity=599833.25 spike=0.04
- SEIG.CA: score=14.07 buy_ready=False sector_rank=9 price=185.34 support=177.32 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:57 AM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=302515.88 spike=0.07
- SIPC.CA: score=9.87 buy_ready=False sector_rank=9 price=3.49 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=1098353.5 spike=0.09
- SKPC.CA: score=10.63 buy_ready=False sector_rank=20 price=16.2 support=16.13 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=4348523.5 spike=0.08
- SMFR.CA: score=9.28 buy_ready=False sector_rank=9 price=198.83 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=41.88 liquidity=512313.53 spike=0.15
- SNFC.CA: score=13.88 buy_ready=False sector_rank=9 price=12.01 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=2113495.75 spike=0.08
- SPIN.CA: score=6.14 buy_ready=False sector_rank=14 price=13.82 support=13.3 resistance=14.9 source=Yahoo Finance as_of=2026-06-20T21:00:00+00:00 freshness=FRESH RSI=23.33 liquidity=2418790.17 spike=1.43
- SPMD.CA: score=25.77 buy_ready=True sector_rank=9 price=0.44 support=0.39 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=66.13 liquidity=23672284.0 spike=0.89
- SUGR.CA: score=3.27 buy_ready=False sector_rank=11 price=48.07 support=48.0 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=24.76 liquidity=719872.38 spike=0.05
- SVCE.CA: score=23.77 buy_ready=True sector_rank=9 price=9.2 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=42.4 liquidity=23984722.0 spike=0.27
- SWDY.CA: score=25.26 buy_ready=True sector_rank=5 price=90.01 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=37.66 liquidity=28438068.0 spike=1.59
- TALM.CA: score=19.22 buy_ready=True sector_rank=3 price=16.05 support=15.32 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=1815149.75 spike=0.23
- TMGH.CA: score=22.4 buy_ready=False sector_rank=4 price=95.86 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=42285832.0 spike=0.09
- TRTO.CA: score=9.77 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=9.32 buy_ready=False sector_rank=9 price=486.31 support=455.6 resistance=489.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=30.31 liquidity=990341.94 spike=1.28
- UEGC.CA: score=17.72 buy_ready=True sector_rank=9 price=1.42 support=1.31 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=3952735.0 spike=0.16
- UNIP.CA: score=16.4 buy_ready=False sector_rank=9 price=0.33 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=85.29 liquidity=3629957.0 spike=0.15
- UNIT.CA: score=9.4 buy_ready=False sector_rank=4 price=13.7 support=12.5 resistance=15.8 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=30.53 liquidity=0.0 spike=0.0
- WCDF.CA: score=8.94 buy_ready=False sector_rank=9 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-20T21:00:00+00:00 freshness=FRESH RSI=42.27 liquidity=167032.3 spike=0.63
- WKOL.CA: score=9.08 buy_ready=False sector_rank=9 price=291.64 support=287.66 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=35.88 liquidity=316607.38 spike=0.1
- ZEOT.CA: score=22.01 buy_ready=False sector_rank=9 price=11.68 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=84.02 liquidity=9245648.0 spike=0.44
- ZMID.CA: score=24.4 buy_ready=True sector_rank=4 price=6.43 support=5.81 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=58.87 liquidity=140029680.0 spike=0.68

## Backtesting Lite
- CNFN.CA: 180d return=11.14%, max drawdown=-27.78%, MA20>MA50 days last20=20, as_of=2026-06-21T21:00:00+00:00
- DOMT.CA: 180d return=22.78%, max drawdown=-13.36%, MA20>MA50 days last20=16, as_of=2026-06-21T21:00:00+00:00
- CLHO.CA: 180d return=42.86%, max drawdown=-14.16%, MA20>MA50 days last20=20, as_of=2026-06-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/
- DOMT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Arabian Food Industries Domty summary=Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn; Selling pressure pushes Domty’s stock toward EGP 23.50–22.85; Domty unveils demerger, establishes Dairy Products Euro Arabian
  - Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn: https://english.mubasher.info/news/4593671/Domty-posts-lower-consolidated-net-profits-at-EGP-161m-in-2025-net-sales-exceed-EGP-9-3bn/
  - Selling pressure pushes Domty’s stock toward EGP 23.50–22.85: https://english.mubasher.info/news/4562323/Selling-pressure-pushes-Domty-s-stock-toward-EGP-23-50-22-85/
  - Domty unveils demerger, establishes Dairy Products Euro Arabian: https://english.mubasher.info/news/4543153/Domty-unveils-demerger-establishes-Dairy-Products-Euro-Arabian/
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- ISPH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Ibn Sina Pharma summary=Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025; EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse; Ibnsina Pharma pens import, distribution deal with OMRON Healthcare
  - Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025: https://english.mubasher.info/news/4563237/Ibnsina-Pharma-s-consolidated-profits-jump-to-EGP-952m-in-2025/
  - EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse: https://english.mubasher.info/news/4552027/EBRD-grants-EGP-1-3bn-loan-to-Ibnsina-Pharma-for-new-warehouse/
  - Ibnsina Pharma pens import, distribution deal with OMRON Healthcare: https://english.mubasher.info/news/4028068/Ibnsina-Pharma-pens-import-distribution-deal-with-OMRON-Healthcare/
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- BTFH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Beltone Holding summary=Evidence rejected for BTFH.CA: source text did not clearly match BTFH.CA / Beltone Holding.
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/

## Warnings
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for DOMT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Evidence for ISPH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- Evidence rejected for BTFH.CA: source text did not clearly match BTFH.CA / Beltone Holding.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
