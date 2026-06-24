# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-24T10:05:04.318352+00:00
Generated Cairo: 2026-06-24 13:05
Run timing: target 09:15 Cairo | generated Cairo 2026-06-24 13:05 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-24 12:49

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 46
- Data quality issues: 0
- Tradeable price/liquidity tickers: 188/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 38.1% / above MA50 42.86%
- EGX70 regime: MIXED / above MA20 53.85% / above MA50 74.36%
- Sector breadth: 47.62%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- COMI.CA: liquidity=493644952.5 spike=1.3 score=23.34
- TMGH.CA: liquidity=344128000.0 spike=1.29 score=22.81
- ZMID.CA: liquidity=282524748.93 spike=1.82 score=29.87
- PHDC.CA: liquidity=279405883.0 spike=0.92 score=24.23
- OCDI.CA: liquidity=152740660.49 spike=4.48 score=33.23

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlights a handful of high‑rank, buy‑ready EGX stocks despite a bearish EGX30 and mixed EGX70 backdrop. Liquidity spikes and bullish outlooks drive the picks, while sector breadth (≈48%) and the selective‑swing‑trades‑only risk mode signal caution over the next 1‑3 days.
- CLHO.CA (Healthcare) sits near support (14% below) with strong earnings news and an accumulation‑spike liquidity regime.
- MHOT.CA (Tourism & Leisure) shows robust profit growth, RSI 66 and a clear bullish watch, though still 22% above 20‑day support.
- OCDI.CA (Real Estate) is close to resistance (1.7% away) and benefits from a liquidity spike, but evidence is limited.
- POUL.CA (Food & Beverages) trades at its 20‑day resistance, supported by recent block‑trade activity and strong fundamentals.
- EGX30’s bearish trend and low above‑MA20/50 percentages push the scanner into a selective swing‑trade risk mode, adding uncertainty to short‑term moves.

## Top Liquidity Spikes
- GTWL.CA: spike=8.54 liquidity=54988928.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPIN.CA: spike=6.39 liquidity=29024316.0 outlook=CONSTRUCTIVE score=59.39 buy_ready=False
- CLHO.CA: spike=5.14 liquidity=121636140.37 outlook=BULLISH_WATCH score=100 buy_ready=True
- POUL.CA: spike=4.72 liquidity=102571625.0 outlook=BULLISH_WATCH score=94.25 buy_ready=True
- OCDI.CA: spike=4.48 liquidity=152740660.49 outlook=BULLISH_WATCH score=88.58 buy_ready=True

## Sector Leaderboard
- #1 Tourism & Leisure: score=21.1 5d=18.31% 20d=15.49% aboveMA50=100.0%
- #2 Automotive & Distribution: score=8.26 5d=3.97% 20d=8.41% aboveMA50=100.0%
- #3 Healthcare: score=6.92 5d=2.64% 20d=2.72% aboveMA50=100.0%
- #4 Technology & Distribution: score=6.7 5d=1.28% 20d=-5.08% aboveMA50=100.0%
- #5 Industrial Goods & Cables: score=5.91 5d=0.75% 20d=0.67% aboveMA50=50.0%
- #6 Real Estate: score=5.58 5d=-0.63% 20d=2.63% aboveMA50=84.62%
- #7 Food, Beverages & Tobacco: score=5.25 5d=0.09% 20d=2.32% aboveMA50=71.43%
- #8 Education: score=5.05 5d=-1.36% 20d=3.03% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: macro source is missing, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CLHO.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MHOT.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- POUL.CA: BULLISH_WATCH score=94.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- NIPH.CA: BULLISH_WATCH score=92.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SWDY.CA: BULLISH_WATCH score=92.91 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- OCDI.CA: BULLISH_WATCH score=88.58 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- RAYA.CA: BULLISH_WATCH score=87.7 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ISPH.CA: BULLISH_WATCH score=86.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PHAR.CA: BULLISH_WATCH score=86.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=86.58 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; close to resistance

## BUY-Ready Candidates
- CLHO.CA: rank=34.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=16.4 support=14.25 resistance=17.0 liquidity=121636140.37
- MHOT.CA: rank=33.64 outlook=BULLISH_WATCH outlook_score=100 sector_rank=1 price=35.34 support=28.83 resistance=38.38 liquidity=42242467.62
- OCDI.CA: rank=33.23 outlook=BULLISH_WATCH outlook_score=88.58 sector_rank=6 price=22.8 support=20.0 resistance=23.19 liquidity=152740660.49
- POUL.CA: rank=33.1 outlook=BULLISH_WATCH outlook_score=94.25 sector_rank=7 price=39.5 support=34.99 resistance=39.5 liquidity=102571625.0
- ZMID.CA: rank=29.87 outlook=BULLISH_WATCH outlook_score=86.58 sector_rank=6 price=6.46 support=5.82 resistance=6.55 liquidity=282524748.93
- CIEB.CA: rank=29.22 outlook=BULLISH_WATCH outlook_score=80.36 sector_rank=11 price=24.37 support=23.27 resistance=24.75 liquidity=9574169.12
- SWDY.CA: rank=28.46 outlook=BULLISH_WATCH outlook_score=92.91 sector_rank=5 price=88.22 support=84.01 resistance=90.97 liquidity=40756670.14
- MICH.CA: rank=27.54 outlook=BULLISH_WATCH outlook_score=77.71 sector_rank=13 price=38.49 support=35.4 resistance=40.4 liquidity=27188028.53
- ISPH.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=86.92 sector_rank=3 price=12.27 support=11.3 resistance=12.74 liquidity=14862001.0
- PRDC.CA: rank=26.31 outlook=CONSTRUCTIVE outlook_score=68.58 sector_rank=6 price=7.24 support=5.7 resistance=9.0 liquidity=109149792.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=11.96 buy_ready=False sector_rank=13 price=206.76 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=44.48 liquidity=476739.06 spike=0.08
- ABUK.CA: score=11.86 buy_ready=False sector_rank=21 price=68.6 support=68.01 resistance=86.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=6.56 liquidity=104220547.68 spike=1.09
- ACAMD.CA: score=21.48 buy_ready=False sector_rank=13 price=2.24 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=71290448.0 spike=0.57
- ACGC.CA: score=21.36 buy_ready=False sector_rank=14 price=9.6 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=36.27 liquidity=22558576.0 spike=0.4
- ADCI.CA: score=20.83 buy_ready=False sector_rank=13 price=240.85 support=211.0 resistance=242.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=93.25 liquidity=8349335.5 spike=1.0
- ADIB.CA: score=18.74 buy_ready=False sector_rank=11 price=45.7 support=44.01 resistance=48.48 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=44.42 liquidity=55344848.82 spike=0.98
- ADPC.CA: score=13.69 buy_ready=False sector_rank=13 price=3.65 support=3.45 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=3208212.25 spike=0.12
- AFDI.CA: score=22.18 buy_ready=True sector_rank=13 price=46.39 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=51.12 liquidity=4700648.5 spike=0.32
- AFMC.CA: score=10.95 buy_ready=False sector_rank=13 price=70.08 support=67.0 resistance=74.69 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=37.38 liquidity=2008703.09 spike=1.23
- AJWA.CA: score=14.32 buy_ready=False sector_rank=13 price=177.17 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=84.31 liquidity=3836373.25 spike=0.14
- ALCN.CA: score=9.9 buy_ready=False sector_rank=18 price=28.09 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=35.47 liquidity=2503989.0 spike=0.18
- ALUM.CA: score=8.76 buy_ready=False sector_rank=13 price=22.75 support=22.81 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=33.63 liquidity=5280561.0 spike=0.52
- AMER.CA: score=14.23 buy_ready=False sector_rank=6 price=2.43 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=25.84 liquidity=39764000.0 spike=0.46
- AMES.CA: score=8.56 buy_ready=False sector_rank=13 price=48.25 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=36.38 liquidity=1078541.25 spike=0.32
- AMIA.CA: score=12.64 buy_ready=False sector_rank=13 price=8.78 support=8.55 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=41.55 liquidity=1151157.38 spike=0.08
- AMOC.CA: score=14.94 buy_ready=False sector_rank=9 price=7.6 support=7.58 resistance=8.59 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=14.41 liquidity=59246050.06 spike=1.52
- ANFI.CA: score=18.82 buy_ready=True sector_rank=13 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=2.99 buy_ready=False sector_rank=13 price=8.56 support=8.24 resistance=9.21 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=11.11 liquidity=509508.34 spike=0.92
- ARAB.CA: score=19.23 buy_ready=False sector_rank=6 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=24560794.0 spike=0.28
- ARCC.CA: score=15.48 buy_ready=False sector_rank=17 price=55.79 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=23.35 liquidity=22446796.0 spike=0.65
- AREH.CA: score=23.48 buy_ready=True sector_rank=13 price=1.57 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=10433300.0 spike=0.34
- ARVA.CA: score=15.74 buy_ready=True sector_rank=13 price=10.96 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=59.13 liquidity=2256109.25 spike=0.07
- ASCM.CA: score=25.48 buy_ready=True sector_rank=13 price=63.7 support=47.49 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=66.14 liquidity=78306072.0 spike=0.95
- ASPI.CA: score=20.81 buy_ready=True sector_rank=13 price=0.32 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=7323765.5 spike=0.1
- ATLC.CA: score=19.23 buy_ready=True sector_rank=10 price=5.12 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=57.24 liquidity=3338750.75 spike=0.57
- ATQA.CA: score=10.68 buy_ready=False sector_rank=21 price=9.34 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=12954670.0 spike=0.41
- AXPH.CA: score=14.35 buy_ready=False sector_rank=13 price=1125.93 support=1073.0 resistance=1174.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=52.91 liquidity=863588.35 spike=0.8
- BINV.CA: score=13.97 buy_ready=False sector_rank=16 price=47.25 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=52.09 liquidity=769894.56 spike=0.07
- BIOC.CA: score=12.28 buy_ready=False sector_rank=13 price=72.04 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=51.74 liquidity=799155.25 spike=0.32
- BTFH.CA: score=17.89 buy_ready=False sector_rank=10 price=3.04 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=27898996.0 spike=0.14
- CAED.CA: score=12.88 buy_ready=False sector_rank=13 price=70.17 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=49.85 liquidity=1391642.88 spike=0.25
- CANA.CA: score=24.32 buy_ready=False sector_rank=11 price=36.15 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=51.92 liquidity=12623953.0 spike=1.29
- CCAP.CA: score=21.2 buy_ready=False sector_rank=16 price=5.08 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=87983256.0 spike=0.12
- CCRS.CA: score=12.75 buy_ready=False sector_rank=13 price=2.38 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=1263459.75 spike=0.06
- CEFM.CA: score=4.23 buy_ready=False sector_rank=13 price=101.55 support=100.53 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=28.56 liquidity=747290.63 spike=0.32
- CERA.CA: score=18.39 buy_ready=True sector_rank=13 price=1.23 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=3901914.75 spike=0.26
- CFGH.CA: score=2.49 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1497.53 spike=0.26
- CICH.CA: score=12.31 buy_ready=False sector_rank=10 price=11.9 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=414940.53 spike=0.12
- CIEB.CA: score=29.22 buy_ready=True sector_rank=11 price=24.37 support=23.27 resistance=24.75 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=62.5 liquidity=9574169.12 spike=1.95
- CIRA.CA: score=26.02 buy_ready=True sector_rank=8 price=28.7 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=12379824.0 spike=0.66
- CLHO.CA: score=34.4 buy_ready=True sector_rank=3 price=16.4 support=14.25 resistance=17.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=53.85 liquidity=121636140.37 spike=5.14
- CNFN.CA: score=26.95 buy_ready=False sector_rank=10 price=5.06 support=4.36 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=73.13 liquidity=54030528.0 spike=1.53
- COMI.CA: score=23.34 buy_ready=False sector_rank=11 price=133.5 support=129.8 resistance=137.07 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=54.25 liquidity=493644952.5 spike=1.3
- COPR.CA: score=17.36 buy_ready=False sector_rank=13 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=53.97 liquidity=6871548.0 spike=0.17
- COSG.CA: score=16.67 buy_ready=False sector_rank=13 price=1.54 support=1.53 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=5188464.5 spike=0.09
- CPCI.CA: score=10.92 buy_ready=False sector_rank=13 price=370.91 support=347.11 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=438277.75 spike=0.22
- CSAG.CA: score=14.99 buy_ready=False sector_rank=18 price=31.0 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=41.0 liquidity=4594525.5 spike=0.41
- DAPH.CA: score=14.69 buy_ready=False sector_rank=13 price=80.99 support=76.6 resistance=82.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=2203458.0 spike=0.28
- DEIN.CA: score=9.48 buy_ready=False sector_rank=13 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=19.37 buy_ready=False sector_rank=7 price=27.5 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=74.05 liquidity=3247300.0 spike=1.01
- DSCW.CA: score=19.48 buy_ready=False sector_rank=13 price=1.81 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=15155850.0 spike=0.31
- DTPP.CA: score=4.01 buy_ready=False sector_rank=13 price=117.55 support=114.0 resistance=130.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=11.41 liquidity=523388.63 spike=0.29
- EALR.CA: score=11.83 buy_ready=False sector_rank=13 price=354.99 support=350.2 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=350386.69 spike=0.11
- EASB.CA: score=16.11 buy_ready=False sector_rank=13 price=7.06 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=82.31 liquidity=5629111.5 spike=0.71
- EAST.CA: score=24.1 buy_ready=True sector_rank=7 price=39.03 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=48.99 liquidity=14437128.0 spike=0.31
- EBSC.CA: score=17.18 buy_ready=True sector_rank=13 price=1.84 support=1.66 resistance=2.09 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=51.11 liquidity=1692742.99 spike=0.67
- ECAP.CA: score=15.93 buy_ready=False sector_rank=13 price=32.8 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=70.87 liquidity=2443588.5 spike=0.38
- EDFM.CA: score=6.56 buy_ready=False sector_rank=13 price=332.0 support=322.11 resistance=355.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=16.43 liquidity=76692.0 spike=0.15
- EEII.CA: score=18.17 buy_ready=True sector_rank=13 price=2.4 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=2686253.25 spike=0.18
- EFIC.CA: score=1.03 buy_ready=False sector_rank=21 price=198.01 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=17.89 liquidity=352588.84 spike=0.17
- EFID.CA: score=14.1 buy_ready=False sector_rank=7 price=27.58 support=27.06 resistance=29.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=31.48 liquidity=24250845.71 spike=0.39
- EFIH.CA: score=16.79 buy_ready=False sector_rank=20 price=20.99 support=20.2 resistance=22.78 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=38.99 liquidity=18762457.04 spike=0.6
- EGAL.CA: score=13.5 buy_ready=False sector_rank=21 price=287.33 support=286.11 resistance=334.9 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=11.25 liquidity=88374945.96 spike=1.91
- EGAS.CA: score=18.42 buy_ready=True sector_rank=9 price=52.24 support=48.2 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=60.21 liquidity=4519823.5 spike=0.37
- EGBE.CA: score=13.66 buy_ready=False sector_rank=11 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=41.51 liquidity=95564.4 spike=1.91
- EGCH.CA: score=11.68 buy_ready=False sector_rank=21 price=12.83 support=12.8 resistance=15.37 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=20.74 liquidity=29343967.54 spike=0.67
- EGSA.CA: score=6.35 buy_ready=False sector_rank=15 price=8.78 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=2247.68 spike=0.28
- EGTS.CA: score=11.88 buy_ready=False sector_rank=6 price=17.68 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=33.94 liquidity=4646257.5 spike=0.04
- EHDR.CA: score=21.21 buy_ready=False sector_rank=13 price=2.57 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=47.87 liquidity=9727910.0 spike=0.17
- EKHO.CA: score=13.9 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=15.96 buy_ready=False sector_rank=5 price=2.11 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5598594.0 spike=0.25
- ELKA.CA: score=17.78 buy_ready=False sector_rank=13 price=1.25 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=7292444.5 spike=0.18
- ELNA.CA: score=8.19 buy_ready=False sector_rank=13 price=38.0 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=44.89 liquidity=465982.31 spike=1.12
- ELSH.CA: score=23.48 buy_ready=True sector_rank=13 price=12.11 support=8.31 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=51.24 liquidity=20613736.0 spike=0.11
- ELWA.CA: score=11.98 buy_ready=False sector_rank=13 price=2.06 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=493033.66 spike=0.15
- EMFD.CA: score=22.23 buy_ready=False sector_rank=6 price=11.6 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=48.8 liquidity=98491473.64 spike=0.37
- ENGC.CA: score=16.58 buy_ready=True sector_rank=13 price=36.33 support=32.81 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=67.22 liquidity=3096253.75 spike=0.22
- EOSB.CA: score=15.57 buy_ready=False sector_rank=13 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=86582.96 spike=0.7
- EPCO.CA: score=10.92 buy_ready=False sector_rank=13 price=9.04 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=2433764.25 spike=0.26
- EPPK.CA: score=12.9 buy_ready=False sector_rank=13 price=12.52 support=11.67 resistance=13.12 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=52.26 liquidity=415463.7 spike=0.5
- ETEL.CA: score=20.35 buy_ready=False sector_rank=15 price=94.59 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=47.2 liquidity=24738570.0 spike=0.31
- ETRS.CA: score=20.55 buy_ready=True sector_rank=13 price=10.29 support=7.93 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=65.81 liquidity=7062536.5 spike=0.11
- EXPA.CA: score=15.79 buy_ready=False sector_rank=11 price=18.36 support=18.21 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=4043710.25 spike=0.12
- FAIT.CA: score=12.68 buy_ready=False sector_rank=11 price=36.49 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=936448.88 spike=0.24
- FAITA.CA: score=11.75 buy_ready=False sector_rank=11 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=6435.52 spike=0.17
- FERC.CA: score=11.21 buy_ready=False sector_rank=21 price=75.38 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=43.52 liquidity=3533044.5 spike=0.9
- FWRY.CA: score=13.79 buy_ready=False sector_rank=20 price=18.85 support=17.71 resistance=20.61 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=34.23 liquidity=142904850.04 spike=0.72
- GBCO.CA: score=25.4 buy_ready=False sector_rank=2 price=31.39 support=25.25 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=86.15 liquidity=29804962.0 spike=0.29
- GDWA.CA: score=10.79 buy_ready=False sector_rank=13 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=45.11 liquidity=3307331.0 spike=0.24
- GGCC.CA: score=16.1 buy_ready=True sector_rank=13 price=0.42 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:18 AM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=1617845.5 spike=0.2
- GIHD.CA: score=25.01 buy_ready=True sector_rank=13 price=43.08 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=7081814.5 spike=1.22
- GMCI.CA: score=8.87 buy_ready=False sector_rank=13 price=1.71 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=40.0 liquidity=448782.67 spike=1.47
- GRCA.CA: score=4.28 buy_ready=False sector_rank=13 price=53.96 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=791067.44 spike=0.15
- GSSC.CA: score=11.55 buy_ready=False sector_rank=13 price=249.3 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=38.36 liquidity=1061846.75 spike=0.26
- GTWL.CA: score=13.48 buy_ready=False sector_rank=13 price=57.58 support=49.37 resistance=57.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54988928.0 spike=8.54
- HDBK.CA: score=27.74 buy_ready=False sector_rank=11 price=163.0 support=138.0 resistance=172.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=78.35 liquidity=88627175.0 spike=4.35
- HELI.CA: score=22.23 buy_ready=False sector_rank=6 price=6.4 support=6.28 resistance=6.87 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=44.08 liquidity=84694663.66 spike=0.98
- HRHO.CA: score=20.09 buy_ready=False sector_rank=10 price=27.0 support=25.8 resistance=27.95 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=49.89 liquidity=103803309.0 spike=1.1
- ICID.CA: score=19.08 buy_ready=False sector_rank=13 price=7.46 support=5.0 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=77.09 liquidity=8600701.0 spike=0.54
- IDRE.CA: score=16.97 buy_ready=True sector_rank=13 price=44.8 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=3483486.5 spike=0.2
- IFAP.CA: score=3.7 buy_ready=False sector_rank=12 price=19.08 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=31.95 liquidity=1096683.75 spike=0.17
- INFI.CA: score=3.75 buy_ready=False sector_rank=13 price=93.88 support=93.0 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=15.58 liquidity=1265437.88 spike=0.15
- IRON.CA: score=11.65 buy_ready=False sector_rank=21 price=31.24 support=31.0 resistance=34.15 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=26.16 liquidity=9535822.49 spike=1.72
- ISMA.CA: score=15.42 buy_ready=False sector_rank=13 price=29.49 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=71.45 liquidity=3937725.25 spike=0.1
- ISMQ.CA: score=23.68 buy_ready=True sector_rank=21 price=8.35 support=7.38 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=57.82 liquidity=53529668.0 spike=0.71
- ISPH.CA: score=27.4 buy_ready=True sector_rank=3 price=12.27 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=14862001.0 spike=0.12
- JUFO.CA: score=23.7 buy_ready=True sector_rank=7 price=30.75 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=62.06 liquidity=7600462.5 spike=0.18
- KABO.CA: score=16.36 buy_ready=False sector_rank=14 price=6.23 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=11185257.0 spike=0.61
- KWIN.CA: score=10.81 buy_ready=False sector_rank=13 price=67.19 support=66.1 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=3327569.5 spike=0.52
- KZPC.CA: score=13.93 buy_ready=False sector_rank=13 price=10.53 support=10.34 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=47.41 liquidity=2445553.0 spike=0.36
- LCSW.CA: score=18.32 buy_ready=True sector_rank=17 price=27.65 support=26.0 resistance=28.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT RSI=54.16 liquidity=3844065.75 spike=0.38
- LUTS.CA: score=23.48 buy_ready=False sector_rank=13 price=0.73 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=72.96 liquidity=11449893.0 spike=0.27
- MAAL.CA: score=21.84 buy_ready=False sector_rank=13 price=6.83 support=5.16 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=79.1 liquidity=24462386.0 spike=1.68
- MASR.CA: score=25.48 buy_ready=True sector_rank=13 price=7.11 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=52.49 liquidity=25809830.0 spike=0.46
- MBSC.CA: score=12.87 buy_ready=False sector_rank=17 price=243.9 support=243.0 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=36.19 liquidity=5390698.5 spike=0.12
- MCQE.CA: score=4.94 buy_ready=False sector_rank=17 price=172.04 support=171.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=19.3 liquidity=2468333.25 spike=0.15
- MCRO.CA: score=12.48 buy_ready=False sector_rank=13 price=1.22 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=12335875.0 spike=0.29
- MENA.CA: score=9.81 buy_ready=False sector_rank=6 price=6.82 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:16 AM market time freshness=DELAYED_CURRENT RSI=32.08 liquidity=581751.69 spike=0.04
- MEPA.CA: score=13.33 buy_ready=False sector_rank=13 price=1.61 support=1.62 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=5844067.0 spike=0.42
- MFPC.CA: score=12.82 buy_ready=False sector_rank=21 price=35.66 support=35.15 resistance=44.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=4.07 liquidity=96453595.51 spike=1.57
- MFSC.CA: score=16.38 buy_ready=True sector_rank=13 price=49.29 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=58.36 liquidity=2896460.25 spike=0.23
- MHOT.CA: score=33.64 buy_ready=True sector_rank=1 price=35.34 support=28.83 resistance=38.38 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=66.46 liquidity=42242467.62 spike=3.12
- MICH.CA: score=27.54 buy_ready=True sector_rank=13 price=38.49 support=35.4 resistance=40.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=62.39 liquidity=27188028.53 spike=2.03
- MILS.CA: score=17.62 buy_ready=False sector_rank=13 price=132.66 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=6138295.5 spike=0.44
- MIPH.CA: score=14.68 buy_ready=False sector_rank=3 price=661.3 support=651.0 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=52.48 liquidity=1281528.88 spike=0.58
- MOED.CA: score=11.57 buy_ready=False sector_rank=13 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=2084609.12 spike=0.19
- MOIL.CA: score=15.97 buy_ready=False sector_rank=9 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=62102.77 spike=0.37
- MOIN.CA: score=2.62 buy_ready=False sector_rank=13 price=23.51 support=23.2 resistance=25.66 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=12.26 liquidity=139414.3 spike=0.23
- MOSC.CA: score=12.49 buy_ready=False sector_rank=13 price=272.08 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=46.96 liquidity=1005863.19 spike=0.12
- MPCI.CA: score=22.54 buy_ready=False sector_rank=13 price=249.96 support=204.36 resistance=253.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=75.08 liquidity=91968664.0 spike=1.03
- MPCO.CA: score=23.6 buy_ready=True sector_rank=12 price=1.9 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=65.43 liquidity=29932404.0 spike=0.29
- MPRC.CA: score=29.0 buy_ready=False sector_rank=13 price=37.26 support=31.1 resistance=36.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=72.53 liquidity=79682080.0 spike=2.76
- MTIE.CA: score=20.31 buy_ready=False sector_rank=2 price=9.0 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=5909723.5 spike=0.36
- NAHO.CA: score=7.49 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=8410.06 spike=0.42
- NCCW.CA: score=20.12 buy_ready=False sector_rank=13 price=6.48 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=73.75 liquidity=6635055.0 spike=0.21
- NEDA.CA: score=10.63 buy_ready=False sector_rank=13 price=2.76 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=39.29 liquidity=602524.56 spike=1.77
- NHPS.CA: score=11.06 buy_ready=False sector_rank=13 price=67.03 support=65.03 resistance=71.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=41.25 liquidity=1572177.38 spike=0.37
- NINH.CA: score=11.57 buy_ready=False sector_rank=13 price=17.73 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=44.05 liquidity=3089208.75 spike=0.61
- NIPH.CA: score=25.4 buy_ready=True sector_rank=3 price=165.25 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=60.31 liquidity=13456839.0 spike=0.18
- OBRI.CA: score=13.24 buy_ready=False sector_rank=13 price=34.53 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:12 AM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=2755386.0 spike=0.2
- OCDI.CA: score=33.23 buy_ready=True sector_rank=6 price=22.8 support=20.0 resistance=23.19 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=60.98 liquidity=152740660.49 spike=4.48
- OCPH.CA: score=11.35 buy_ready=False sector_rank=13 price=346.44 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=44.61 liquidity=2863736.0 spike=0.45
- ODIN.CA: score=17.29 buy_ready=True sector_rank=13 price=2.1 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:11 AM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=1806154.75 spike=0.16
- OFH.CA: score=12.78 buy_ready=False sector_rank=13 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=26.25 liquidity=9297208.0 spike=0.44
- OIH.CA: score=20.2 buy_ready=False sector_rank=16 price=1.41 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=68894400.0 spike=0.79
- OLFI.CA: score=20.85 buy_ready=True sector_rank=7 price=21.94 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=4745437.5 spike=0.24
- ORAS.CA: score=8.0 buy_ready=False sector_rank=19 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=24.47 buy_ready=True sector_rank=6 price=38.9 support=35.01 resistance=39.68 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=54.37 liquidity=142936538.51 spike=1.12
- ORWE.CA: score=18.36 buy_ready=False sector_rank=14 price=22.98 support=22.65 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=7000462.0 spike=0.18
- PHAR.CA: score=25.25 buy_ready=True sector_rank=3 price=87.84 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=7853909.5 spike=0.22
- PHDC.CA: score=24.23 buy_ready=True sector_rank=6 price=15.5 support=14.43 resistance=16.43 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=53.64 liquidity=279405883.0 spike=0.92
- PHTV.CA: score=22.88 buy_ready=False sector_rank=13 price=252.76 support=201.55 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=84.24 liquidity=22512576.0 spike=1.2
- POUL.CA: score=33.1 buy_ready=True sector_rank=7 price=39.5 support=34.99 resistance=39.5 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=61.33 liquidity=102571625.0 spike=4.72
- PRCL.CA: score=8.3 buy_ready=False sector_rank=17 price=29.26 support=28.97 resistance=31.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47279848.0 spike=1.41
- PRDC.CA: score=26.31 buy_ready=True sector_rank=6 price=7.24 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=109149792.0 spike=1.04
- PRMH.CA: score=21.48 buy_ready=False sector_rank=13 price=2.6 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=55.93 liquidity=27581256.0 spike=0.98
- RACC.CA: score=16.08 buy_ready=False sector_rank=13 price=9.87 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=46.32 liquidity=4591659.0 spike=0.46
- RAKT.CA: score=9.28 buy_ready=False sector_rank=13 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=37.86 liquidity=391159.87 spike=1.7
- RAYA.CA: score=24.4 buy_ready=True sector_rank=4 price=7.42 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=40.98 liquidity=68504144.0 spike=0.8
- RMDA.CA: score=23.4 buy_ready=False sector_rank=3 price=5.0 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=17631158.0 spike=0.21
- ROTO.CA: score=16.94 buy_ready=False sector_rank=13 price=42.0 support=32.76 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=82.18 liquidity=6452237.5 spike=0.24
- RREI.CA: score=14.96 buy_ready=False sector_rank=13 price=3.5 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=37.97 liquidity=4475035.0 spike=0.22
- RTVC.CA: score=11.11 buy_ready=False sector_rank=13 price=3.81 support=3.76 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=48.68 liquidity=623447.19 spike=0.13
- RUBX.CA: score=16.32 buy_ready=False sector_rank=13 price=10.42 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=50.28 liquidity=3836976.5 spike=0.35
- SAUD.CA: score=9.46 buy_ready=False sector_rank=11 price=21.58 support=20.82 resistance=23.27 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=34.35 liquidity=5715657.2 spike=0.88
- SCEM.CA: score=12.48 buy_ready=False sector_rank=17 price=61.0 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=27.56 liquidity=17684898.0 spike=0.94
- SCFM.CA: score=5.77 buy_ready=False sector_rank=13 price=242.93 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=21.0 liquidity=2283984.5 spike=0.3
- SCTS.CA: score=4.71 buy_ready=False sector_rank=8 price=586.84 support=565.25 resistance=645.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:17 AM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=690949.5 spike=0.17
- SDTI.CA: score=15.45 buy_ready=True sector_rank=13 price=46.3 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=55.69 liquidity=1966146.63 spike=0.15
- SEIG.CA: score=13.8 buy_ready=False sector_rank=13 price=185.87 support=179.43 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:19 AM market time freshness=DELAYED_CURRENT RSI=40.93 liquidity=311134.19 spike=0.07
- SIPC.CA: score=10.31 buy_ready=False sector_rank=13 price=3.44 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=35.19 liquidity=1821783.75 spike=0.15
- SKPC.CA: score=10.68 buy_ready=False sector_rank=21 price=16.02 support=16.01 resistance=17.5 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=27.31 liquidity=16607742.23 spike=0.66
- SMFR.CA: score=9.15 buy_ready=False sector_rank=13 price=199.48 support=192.0 resistance=214.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=37.93 liquidity=663270.99 spike=0.38
- SNFC.CA: score=15.09 buy_ready=False sector_rank=13 price=11.98 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=44.51 liquidity=3604686.0 spike=0.15
- SPIN.CA: score=23.36 buy_ready=False sector_rank=14 price=14.39 support=13.3 resistance=14.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=27.72 liquidity=29024316.0 spike=6.39
- SPMD.CA: score=24.43 buy_ready=True sector_rank=13 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=54.67 liquidity=8945169.0 spike=0.33
- SUGR.CA: score=5.28 buy_ready=False sector_rank=7 price=47.53 support=47.6 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=22.87 liquidity=2182198.0 spike=0.23
- SVCE.CA: score=23.48 buy_ready=True sector_rank=13 price=9.09 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=13101611.0 spike=0.17
- SWDY.CA: score=28.46 buy_ready=True sector_rank=5 price=88.22 support=84.01 resistance=90.97 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=46.1 liquidity=40756670.14 spike=3.05
- TALM.CA: score=24.88 buy_ready=True sector_rank=8 price=15.99 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=10953859.0 spike=1.43
- TMGH.CA: score=22.81 buy_ready=False sector_rank=6 price=95.0 support=92.91 resistance=98.98 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=43.48 liquidity=344128000.0 spike=1.29
- TRTO.CA: score=9.48 buy_ready=False sector_rank=13 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=326.64 spike=0.46
- UEFM.CA: score=21.6 buy_ready=False sector_rank=13 price=484.15 support=465.01 resistance=490.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=55.92 liquidity=2120576.97 spike=3.63
- UEGC.CA: score=17.4 buy_ready=False sector_rank=13 price=1.39 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=3917370.25 spike=0.16
- UNIP.CA: score=16.37 buy_ready=False sector_rank=13 price=0.32 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:20 AM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=2890467.75 spike=0.12
- UNIT.CA: score=8.41 buy_ready=False sector_rank=6 price=13.12 support=12.92 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=30.42 liquidity=1178248.13 spike=0.16
- WCDF.CA: score=8.66 buy_ready=False sector_rank=13 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=44.29 liquidity=172883.75 spike=0.72
- WKOL.CA: score=10.19 buy_ready=False sector_rank=13 price=288.18 support=287.66 resistance=312.0 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=36.68 liquidity=1703431.94 spike=0.78
- ZEOT.CA: score=21.1 buy_ready=False sector_rank=13 price=11.85 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=80.14 liquidity=29545716.0 spike=1.31
- ZMID.CA: score=29.87 buy_ready=True sector_rank=6 price=6.46 support=5.82 resistance=6.55 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.96 liquidity=282524748.93 spike=1.82

## Backtesting Lite
- CLHO.CA: 180d return=45.91%, max drawdown=-14.16%, MA20>MA50 days last20=20, as_of=2026-06-22T21:00:00+00:00
- MHOT.CA: 180d return=44.78%, max drawdown=-15.7%, MA20>MA50 days last20=20, as_of=2026-06-22T21:00:00+00:00
- OCDI.CA: 180d return=41.18%, max drawdown=-18.11%, MA20>MA50 days last20=11, as_of=2026-06-22T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=539 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=539 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- CIEB.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Credit Agricole Egypt summary=Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations; Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
  - Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport: https://english.mubasher.info/news/4580464/Elsewedy-Electric-s-subsidiary-leads-expansion-of-SAL-project-at-Riyadh-airport/

## Warnings
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CIEB.CA: source text did not clearly match CIEB.CA / Credit Agricole Egypt.
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
