# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-25T09:47:26.516855+00:00
Generated Cairo: 2026-06-25 12:47
Run timing: target 09:15 Cairo | generated Cairo 2026-06-25 12:47 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-25 12:41

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 57
- Data quality issues: 0
- Tradeable price/liquidity tickers: 185/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, June 25
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 45.0% / above MA50 50.0%
- EGX70 regime: MIXED / above MA20 51.28% / above MA50 71.79%
- Sector breadth: 47.62%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=389094720.0 spike=0.56 score=21.17
- ORAS.CA: liquidity=318168288.0 spike=1.0 score=7.6
- TMGH.CA: liquidity=165056512.0 spike=0.34 score=23.61
- ISMQ.CA: liquidity=141254720.0 spike=1.59 score=24.91
- HRHO.CA: liquidity=125177320.0 spike=1.0 score=24.18

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner found no trade‑ready candidates that passed all evidence, liquidity, freshness and technical gates, so the default action is HOLD. EGX30 remains bearish with weak breadth (45% above MA20) and negative 5‑day returns, while EGX70 shows mixed signals – about half the stocks sit above MA20 and a majority above MA50, but 5‑day returns are still down. Risk mode is set to SELECTIVE_SWING_TRADES_ONLY, meaning only high‑conviction setups would be considered. Leading sectors (Tourism & Leisure, Technology & Distribution, Automotive & Distribution) are modestly outperforming, yet overall sector breadth is sub‑50%, adding uncertainty to short‑term outlook.
- EGX30 bearish, low breadth; EGX70 mixed, modestly better MA50 coverage
- Risk mode restricts activity to selective swing trades – no clear entry signals now
- Top‑ranked tickets (DAPH, OCDI, CIRA, etc.) show bullish outlooks but lack sufficient evidence or liquidity confidence
- Sector breadth at 47.6% signals limited market participation; leading sectors modestly positive
- Uncertainty remains high for the next 1‑3 days as broader market pressure persists

## Top Liquidity Spikes
- GTWL.CA: spike=11.38 liquidity=105411808.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KWIN.CA: spike=7.98 liquidity=52417176.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DAPH.CA: spike=6.05 liquidity=47142512.0 outlook=BULLISH_WATCH score=87.48 buy_ready=True
- LCSW.CA: spike=3.74 liquidity=38296344.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELNA.CA: spike=3.17 liquidity=1179628.44 outlook=NEUTRAL score=40.48 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=16.19 5d=17.17% 20d=14.38% aboveMA50=100.0%
- #2 Technology & Distribution: score=8.61 5d=5.56% 20d=-1.07% aboveMA50=100.0%
- #3 Automotive & Distribution: score=8.32 5d=4.13% 20d=8.6% aboveMA50=100.0%
- #4 Healthcare: score=6.51 5d=1.61% 20d=3.32% aboveMA50=100.0%
- #5 Non-bank Financial Services: score=5.46 5d=1.0% 20d=0.0% aboveMA50=80.0%
- #6 Education: score=5.35 5d=0.0% 20d=2.84% aboveMA50=66.67%
- #7 Agriculture & Food Production: score=4.51 5d=-2.46% 20d=6.22% aboveMA50=50.0%
- #8 Energy & Petrochemicals: score=4.06 5d=0.82% 20d=2.15% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- RAYA.CA: BULLISH_WATCH score=94.61 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- DAPH.CA: BULLISH_WATCH score=87.48 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NIPH.CA: BULLISH_WATCH score=82.51 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ATLC.CA: BULLISH_WATCH score=81.46 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MHOT.CA: BULLISH_WATCH score=78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- ISPH.CA: BULLISH_WATCH score=76.51 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- PHAR.CA: BULLISH_WATCH score=76.51 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- AFDI.CA: BULLISH_WATCH score=76.48 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MTIE.CA: BULLISH_WATCH score=76.32 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- OCDI.CA: BULLISH_WATCH score=76.03 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading

## BUY-Ready Candidates
- DAPH.CA: rank=32.39 outlook=BULLISH_WATCH outlook_score=87.48 sector_rank=12 price=85.95 support=76.6 resistance=82.95 liquidity=47142512.0
- OCDI.CA: rank=28.09 outlook=BULLISH_WATCH outlook_score=76.03 sector_rank=9 price=24.8 support=20.0 resistance=24.23 liquidity=114709936.0
- CIRA.CA: rank=27.52 outlook=BULLISH_WATCH outlook_score=75.35 sector_rank=6 price=28.7 support=25.23 resistance=31.0 liquidity=9375688.0
- GIHD.CA: rank=27.33 outlook=CONSTRUCTIVE outlook_score=63.48 sector_rank=12 price=44.83 support=35.15 resistance=47.0 liquidity=9358523.0
- CLHO.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=70.51 sector_rank=4 price=16.81 support=14.25 resistance=17.39 liquidity=23336314.0
- RAYA.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=94.61 sector_rank=2 price=7.39 support=6.7 resistance=7.81 liquidity=35243792.0
- CNFN.CA: rank=26.38 outlook=CONSTRUCTIVE outlook_score=66.46 sector_rank=5 price=5.08 support=4.36 resistance=5.25 liquidity=40717668.0
- MPCO.CA: rank=25.8 outlook=BULLISH_WATCH outlook_score=74.51 sector_rank=7 price=1.87 support=1.58 resistance=2.04 liquidity=14645403.0
- ZMID.CA: rank=25.61 outlook=CONSTRUCTIVE outlook_score=57.03 sector_rank=9 price=6.61 support=5.82 resistance=6.69 liquidity=88089872.0
- PRDC.CA: rank=25.61 outlook=CONSTRUCTIVE outlook_score=57.03 sector_rank=9 price=7.29 support=5.7 resistance=9.0 liquidity=36669312.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.54 buy_ready=False sector_rank=12 price=206.17 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=44.24 liquidity=1146851.63 spike=0.19
- ABUK.CA: score=11.73 buy_ready=False sector_rank=21 price=69.22 support=68.01 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=12.81 liquidity=28858276.0 spike=0.22
- ACAMD.CA: score=21.39 buy_ready=False sector_rank=12 price=2.23 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=27179566.0 spike=0.21
- ACGC.CA: score=23.01 buy_ready=True sector_rank=18 price=9.69 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=38.39 liquidity=12922010.0 spike=0.23
- ADCI.CA: score=15.95 buy_ready=False sector_rank=12 price=238.91 support=211.0 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=92.86 liquidity=3559658.5 spike=0.4
- ADIB.CA: score=18.08 buy_ready=False sector_rank=17 price=45.2 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=40.29 liquidity=30174816.0 spike=0.3
- ADPC.CA: score=20.39 buy_ready=False sector_rank=12 price=3.56 support=3.45 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=42.42 liquidity=14566442.0 spike=0.65
- AFDI.CA: score=22.3 buy_ready=True sector_rank=12 price=45.32 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=57.85 liquidity=4903709.5 spike=0.34
- AFMC.CA: score=9.43 buy_ready=False sector_rank=12 price=70.56 support=67.0 resistance=74.69 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=37.62 liquidity=1042453.4 spike=0.62
- AJWA.CA: score=15.57 buy_ready=False sector_rank=12 price=176.99 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=83.33 liquidity=5173785.0 spike=0.19
- ALCN.CA: score=6.8 buy_ready=False sector_rank=16 price=27.99 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=28.02 liquidity=3667405.25 spike=0.28
- ALUM.CA: score=7.3 buy_ready=False sector_rank=12 price=22.0 support=22.35 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=27.36 liquidity=3908131.5 spike=0.38
- AMER.CA: score=13.61 buy_ready=False sector_rank=9 price=2.4 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=31.87 liquidity=11224864.0 spike=0.14
- AMES.CA: score=9.07 buy_ready=False sector_rank=12 price=48.53 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=36.42 liquidity=1680630.88 spike=0.52
- AMIA.CA: score=15.15 buy_ready=False sector_rank=12 price=8.61 support=8.55 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=41.84 liquidity=3755460.75 spike=0.27
- AMOC.CA: score=13.62 buy_ready=False sector_rank=8 price=7.65 support=7.58 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=20.72 liquidity=11237101.0 spike=0.21
- ANFI.CA: score=18.72 buy_ready=True sector_rank=12 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=2.99 buy_ready=False sector_rank=12 price=8.5 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=12.9 liquidity=598185.25 spike=0.74
- ARAB.CA: score=18.61 buy_ready=False sector_rank=9 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=12067161.0 spike=0.14
- ARCC.CA: score=13.38 buy_ready=False sector_rank=19 price=55.72 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=33.77 liquidity=7456416.5 spike=0.22
- AREH.CA: score=23.39 buy_ready=True sector_rank=12 price=1.65 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=23672422.0 spike=0.73
- ARVA.CA: score=15.78 buy_ready=True sector_rank=12 price=11.18 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=2386139.5 spike=0.07
- ASCM.CA: score=23.39 buy_ready=True sector_rank=12 price=61.0 support=47.49 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=68.91 liquidity=33986300.0 spike=0.38
- ASPI.CA: score=14.74 buy_ready=False sector_rank=12 price=0.32 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=8351059.0 spike=0.12
- ATLC.CA: score=19.56 buy_ready=True sector_rank=5 price=5.04 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=56.08 liquidity=3374225.75 spike=0.57
- ATQA.CA: score=15.73 buy_ready=False sector_rank=21 price=9.44 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=13668805.0 spike=0.44
- AXPH.CA: score=12.32 buy_ready=False sector_rank=12 price=1101.95 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=925377.13 spike=0.59
- BINV.CA: score=13.7 buy_ready=False sector_rank=14 price=47.18 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=532722.94 spike=0.05
- BIOC.CA: score=11.92 buy_ready=False sector_rank=12 price=71.99 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=525196.94 spike=0.23
- BTFH.CA: score=18.18 buy_ready=False sector_rank=5 price=3.01 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=43.84 liquidity=64684604.0 spike=0.34
- CAED.CA: score=14.85 buy_ready=True sector_rank=12 price=71.73 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:56 AM market time freshness=DELAYED_CURRENT RSI=47.44 liquidity=1454103.0 spike=0.28
- CANA.CA: score=12.72 buy_ready=False sector_rank=17 price=36.01 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=2644223.5 spike=0.26
- CCAP.CA: score=21.17 buy_ready=False sector_rank=14 price=4.99 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=38.62 liquidity=389094720.0 spike=0.56
- CCRS.CA: score=21.39 buy_ready=False sector_rank=12 price=2.42 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=10874872.0 spike=0.59
- CEFM.CA: score=4.06 buy_ready=False sector_rank=12 price=102.04 support=100.27 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=30.83 liquidity=666238.94 spike=0.31
- CERA.CA: score=19.81 buy_ready=True sector_rank=12 price=1.24 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=5422619.0 spike=0.36
- CFGH.CA: score=2.39 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1858.4 spike=0.32
- CICH.CA: score=15.61 buy_ready=False sector_rank=5 price=11.99 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=1427023.88 spike=0.44
- CIEB.CA: score=17.07 buy_ready=True sector_rank=17 price=23.98 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=56.49 liquidity=1995335.13 spike=0.31
- CIRA.CA: score=27.52 buy_ready=True sector_rank=6 price=28.7 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=63.7 liquidity=9375688.0 spike=0.52
- CLHO.CA: score=26.4 buy_ready=True sector_rank=4 price=16.81 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=65.46 liquidity=23336314.0 spike=0.66
- CNFN.CA: score=26.38 buy_ready=True sector_rank=5 price=5.08 support=4.36 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=40717668.0 spike=1.1
- COMI.CA: score=20.08 buy_ready=False sector_rank=17 price=132.19 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=49.01 liquidity=60634152.0 spike=0.1
- COPR.CA: score=21.75 buy_ready=True sector_rank=12 price=0.37 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=54.69 liquidity=9360348.0 spike=0.26
- COSG.CA: score=11.33 buy_ready=False sector_rank=12 price=1.53 support=1.53 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=4937876.0 spike=0.09
- CPCI.CA: score=14.96 buy_ready=False sector_rank=12 price=375.5 support=347.11 resistance=377.0 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=72.1 liquidity=1571092.0 spike=0.97
- CSAG.CA: score=21.27 buy_ready=True sector_rank=16 price=31.82 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=8138935.0 spike=0.73
- DAPH.CA: score=32.39 buy_ready=True sector_rank=12 price=85.95 support=76.6 resistance=82.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=53.9 liquidity=47142512.0 spike=6.05
- DEIN.CA: score=9.39 buy_ready=False sector_rank=12 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=15.79 buy_ready=False sector_rank=15 price=27.0 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=73.9 liquidity=2636724.75 spike=0.77
- DSCW.CA: score=17.55 buy_ready=False sector_rank=12 price=1.77 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=8156044.5 spike=0.17
- DTPP.CA: score=4.57 buy_ready=False sector_rank=12 price=117.3 support=114.0 resistance=130.89 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=18.44 liquidity=1122912.93 spike=1.03
- EALR.CA: score=9.1 buy_ready=False sector_rank=12 price=354.24 support=350.2 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:55 AM market time freshness=DELAYED_CURRENT RSI=43.9 liquidity=707978.88 spike=0.22
- EASB.CA: score=22.83 buy_ready=False sector_rank=12 price=8.16 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=84.31 liquidity=20762994.0 spike=2.22
- EAST.CA: score=13.82 buy_ready=False sector_rank=15 price=38.02 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=6666567.5 spike=0.15
- EBSC.CA: score=7.57 buy_ready=False sector_rank=12 price=1.82 support=1.66 resistance=2.09 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=1175370.59 spike=0.46
- ECAP.CA: score=24.16 buy_ready=True sector_rank=12 price=33.81 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=63.01 liquidity=8271070.5 spike=1.25
- EDFM.CA: score=3.7 buy_ready=False sector_rank=12 price=330.44 support=322.11 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=312277.5 spike=0.51
- EEII.CA: score=16.86 buy_ready=True sector_rank=12 price=2.47 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=3466336.5 spike=0.25
- EFIC.CA: score=1.24 buy_ready=False sector_rank=21 price=198.15 support=192.01 resistance=213.79 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=17.89 liquidity=510236.23 spike=0.31
- EFID.CA: score=13.15 buy_ready=False sector_rank=15 price=26.92 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=31.55 liquidity=22227064.0 spike=0.31
- EFIH.CA: score=18.52 buy_ready=True sector_rank=13 price=20.87 support=20.82 resistance=20.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5220037.5 spike=1.0
- EGAL.CA: score=11.73 buy_ready=False sector_rank=21 price=281.87 support=282.5 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=10.26 liquidity=14459646.0 spike=0.19
- EGAS.CA: score=15.69 buy_ready=True sector_rank=8 price=51.01 support=48.2 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=61.65 liquidity=2066105.5 spike=0.19
- EGBE.CA: score=13.42 buy_ready=False sector_rank=17 price=0.45 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:55 AM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=103247.59 spike=1.12
- EGCH.CA: score=14.73 buy_ready=False sector_rank=21 price=13.2 support=12.69 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=29.6 liquidity=20191282.0 spike=0.34
- EGSA.CA: score=6.58 buy_ready=False sector_rank=11 price=8.76 support=8.55 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=15045.0 spike=1.07
- EGTS.CA: score=18.49 buy_ready=False sector_rank=9 price=17.6 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=37.09 liquidity=6880526.0 spike=0.06
- EHDR.CA: score=18.32 buy_ready=False sector_rank=12 price=2.61 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=37.65 liquidity=6931470.0 spike=0.12
- EKHO.CA: score=13.62 buy_ready=False sector_rank=8 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=14.96 buy_ready=False sector_rank=10 price=2.12 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=5478134.5 spike=0.26
- ELKA.CA: score=17.7 buy_ready=False sector_rank=12 price=1.25 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=7308367.0 spike=0.18
- ELNA.CA: score=12.91 buy_ready=False sector_rank=12 price=37.73 support=37.11 resistance=41.51 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=47.24 liquidity=1179628.44 spike=3.17
- ELSH.CA: score=17.39 buy_ready=False sector_rank=12 price=11.86 support=11.87 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=10111965.0 spike=1.0
- ELWA.CA: score=12.17 buy_ready=False sector_rank=12 price=2.05 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=47.92 liquidity=773485.38 spike=0.24
- EMFD.CA: score=21.61 buy_ready=False sector_rank=9 price=11.81 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=42.9 liquidity=39426936.0 spike=0.14
- ENGC.CA: score=18.15 buy_ready=True sector_rank=12 price=35.67 support=32.81 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=64.75 liquidity=2756891.0 spike=0.21
- EOSB.CA: score=15.46 buy_ready=False sector_rank=12 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=67810.64 spike=0.53
- EPCO.CA: score=9.13 buy_ready=False sector_rank=12 price=9.03 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=737533.38 spike=0.08
- EPPK.CA: score=12.45 buy_ready=False sector_rank=12 price=12.52 support=11.67 resistance=13.12 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=54.94 liquidity=53222.52 spike=0.06
- ETEL.CA: score=18.93 buy_ready=False sector_rank=11 price=94.49 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=41.45 liquidity=6503845.5 spike=0.08
- ETRS.CA: score=8.39 buy_ready=False sector_rank=12 price=10.8 support=10.25 resistance=10.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18860542.0 spike=0.31
- EXPA.CA: score=21.08 buy_ready=False sector_rank=17 price=18.43 support=18.2 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=11138704.0 spike=0.34
- FAIT.CA: score=11.38 buy_ready=False sector_rank=17 price=36.25 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:56 AM market time freshness=DELAYED_CURRENT RSI=35.99 liquidity=303026.75 spike=0.09
- FAITA.CA: score=11.1 buy_ready=False sector_rank=17 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=25309.95 spike=0.71
- FERC.CA: score=4.26 buy_ready=False sector_rank=21 price=75.16 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=23.73 liquidity=1525958.13 spike=0.39
- FWRY.CA: score=20.3 buy_ready=False sector_rank=13 price=18.99 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=32858938.0 spike=0.12
- GBCO.CA: score=24.4 buy_ready=False sector_rank=3 price=31.18 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=85.89 liquidity=20213428.0 spike=0.21
- GDWA.CA: score=8.91 buy_ready=False sector_rank=12 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=1516694.12 spike=0.11
- GGCC.CA: score=23.59 buy_ready=True sector_rank=12 price=0.43 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=9001952.0 spike=1.1
- GIHD.CA: score=27.33 buy_ready=True sector_rank=12 price=44.83 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=63.56 liquidity=9358523.0 spike=1.29
- GMCI.CA: score=2.58 buy_ready=False sector_rank=12 price=1.71 support=1.66 resistance=1.84 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=187734.06 spike=0.6
- GRCA.CA: score=4.58 buy_ready=False sector_rank=12 price=52.77 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=32.12 liquidity=1190942.0 spike=0.24
- GSSC.CA: score=10.94 buy_ready=False sector_rank=12 price=248.87 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=36.64 liquidity=548276.0 spike=0.16
- GTWL.CA: score=13.39 buy_ready=False sector_rank=12 price=66.0 support=60.5 resistance=68.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=105411808.0 spike=11.38
- HDBK.CA: score=21.59 buy_ready=False sector_rank=17 price=162.53 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=82.54 liquidity=9514974.0 spike=0.36
- HELI.CA: score=23.61 buy_ready=True sector_rank=9 price=6.53 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=50.3 liquidity=68331168.0 spike=0.5
- HRHO.CA: score=24.18 buy_ready=True sector_rank=5 price=27.23 support=26.89 resistance=26.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=125177320.0 spike=1.0
- ICID.CA: score=13.02 buy_ready=False sector_rank=12 price=7.42 support=5.0 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=78.35 liquidity=631582.25 spike=0.04
- IDRE.CA: score=16.06 buy_ready=True sector_rank=12 price=44.56 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=2669388.0 spike=0.16
- IFAP.CA: score=18.33 buy_ready=False sector_rank=7 price=19.19 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=9469785.0 spike=1.53
- INFI.CA: score=3.05 buy_ready=False sector_rank=12 price=93.33 support=93.0 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=16.44 liquidity=661235.31 spike=0.08
- IRON.CA: score=3.6 buy_ready=False sector_rank=21 price=31.89 support=30.95 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=2870043.75 spike=0.36
- ISMA.CA: score=14.37 buy_ready=True sector_rank=12 price=29.45 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=67.7 liquidity=2973214.0 spike=0.08
- ISMQ.CA: score=24.91 buy_ready=True sector_rank=21 price=8.87 support=7.38 resistance=8.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=68.66 liquidity=141254720.0 spike=1.59
- ISPH.CA: score=24.4 buy_ready=True sector_rank=4 price=12.17 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=45.17 liquidity=17461708.0 spike=0.14
- JUFO.CA: score=18.24 buy_ready=True sector_rank=15 price=30.51 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=56.88 liquidity=3086062.75 spike=0.08
- KABO.CA: score=12.42 buy_ready=False sector_rank=18 price=6.2 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:01 AM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=1409840.75 spike=0.08
- KWIN.CA: score=13.39 buy_ready=False sector_rank=12 price=70.64 support=68.25 resistance=75.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52417176.0 spike=7.98
- KZPC.CA: score=10.95 buy_ready=False sector_rank=12 price=8.71 support=8.8 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3556361.25 spike=1.0
- LCSW.CA: score=12.92 buy_ready=False sector_rank=19 price=28.94 support=27.34 resistance=29.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38296344.0 spike=3.74
- LUTS.CA: score=19.08 buy_ready=False sector_rank=12 price=0.74 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=71.88 liquidity=5689951.0 spike=0.13
- MAAL.CA: score=14.98 buy_ready=False sector_rank=12 price=6.81 support=5.16 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=79.41 liquidity=2585538.5 spike=0.16
- MASR.CA: score=19.69 buy_ready=True sector_rank=12 price=7.13 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=6297843.5 spike=0.11
- MBSC.CA: score=6.28 buy_ready=False sector_rank=19 price=243.34 support=242.2 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=33.82 liquidity=3364765.25 spike=0.08
- MCQE.CA: score=8.41 buy_ready=False sector_rank=19 price=167.26 support=171.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=19.54 liquidity=5489286.0 spike=0.35
- MCRO.CA: score=12.31 buy_ready=False sector_rank=12 price=1.22 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=9916132.0 spike=0.26
- MENA.CA: score=7.07 buy_ready=False sector_rank=9 price=6.73 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=32.08 liquidity=455001.69 spike=0.03
- MEPA.CA: score=8.47 buy_ready=False sector_rank=12 price=1.63 support=1.6 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=20.83 liquidity=5080132.5 spike=0.4
- MFPC.CA: score=11.73 buy_ready=False sector_rank=21 price=35.91 support=35.15 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=8.6 liquidity=24416268.0 spike=0.29
- MFSC.CA: score=16.4 buy_ready=True sector_rank=12 price=49.68 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=54.35 liquidity=3004221.5 spike=0.3
- MHOT.CA: score=25.23 buy_ready=True sector_rank=1 price=34.98 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=7833404.0 spike=0.3
- MICH.CA: score=19.07 buy_ready=True sector_rank=12 price=37.97 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=64.57 liquidity=3676315.0 spike=0.24
- MILS.CA: score=11.93 buy_ready=False sector_rank=12 price=133.58 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=42.36 liquidity=542987.19 spike=0.04
- MIPH.CA: score=13.33 buy_ready=False sector_rank=4 price=653.38 support=651.0 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=47.49 liquidity=929417.44 spike=0.43
- MOED.CA: score=9.87 buy_ready=False sector_rank=12 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=477833.81 spike=0.05
- MOIL.CA: score=13.88 buy_ready=False sector_rank=8 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=175061.97 spike=1.04
- MOIN.CA: score=2.48 buy_ready=False sector_rank=12 price=23.51 support=23.02 resistance=25.66 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=1.06 liquidity=89690.65 spike=0.15
- MOSC.CA: score=12.29 buy_ready=False sector_rank=12 price=263.67 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=44.89 liquidity=895498.56 spike=0.11
- MPCI.CA: score=23.39 buy_ready=True sector_rank=12 price=241.11 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=34249772.0 spike=0.36
- MPCO.CA: score=25.8 buy_ready=True sector_rank=7 price=1.87 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=14645403.0 spike=0.14
- MPRC.CA: score=25.39 buy_ready=False sector_rank=12 price=37.01 support=31.1 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=73.84 liquidity=29191840.0 spike=0.84
- MTIE.CA: score=19.65 buy_ready=False sector_rank=3 price=9.05 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=45.99 liquidity=6253439.0 spike=0.39
- NAHO.CA: score=9.4 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:57 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11601.35 spike=0.35
- NCCW.CA: score=20.51 buy_ready=True sector_rank=12 price=6.34 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=56.8 liquidity=7119657.5 spike=0.22
- NEDA.CA: score=8.71 buy_ready=False sector_rank=12 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=42.31 liquidity=318344.16 spike=0.89
- NHPS.CA: score=16.25 buy_ready=True sector_rank=12 price=64.14 support=63.19 resistance=63.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2862845.5 spike=1.0
- NINH.CA: score=15.36 buy_ready=True sector_rank=12 price=17.98 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=48.53 liquidity=1964735.88 spike=0.39
- NIPH.CA: score=24.14 buy_ready=True sector_rank=4 price=163.56 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=9735978.0 spike=0.13
- OBRI.CA: score=10.83 buy_ready=False sector_rank=12 price=34.52 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=48.38 liquidity=2434114.0 spike=0.18
- OCDI.CA: score=28.09 buy_ready=True sector_rank=9 price=24.8 support=20.0 resistance=24.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=67.7 liquidity=114709936.0 spike=2.24
- OCPH.CA: score=16.81 buy_ready=True sector_rank=12 price=351.65 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=3419729.25 spike=0.56
- ODIN.CA: score=16.41 buy_ready=True sector_rank=12 price=2.11 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3019621.0 spike=0.28
- OFH.CA: score=5.94 buy_ready=False sector_rank=12 price=0.6 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:07 AM market time freshness=DELAYED_CURRENT RSI=22.09 liquidity=3546768.75 spike=0.18
- OIH.CA: score=20.17 buy_ready=False sector_rank=14 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=10630216.0 spike=0.12
- OLFI.CA: score=16.6 buy_ready=False sector_rank=15 price=21.77 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=54.79 liquidity=8446147.0 spike=0.42
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=755.84 support=741.01 resistance=795.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=318168288.0 spike=1.0
- ORHD.CA: score=23.61 buy_ready=True sector_rank=9 price=39.11 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=56.72 liquidity=25578184.0 spike=0.14
- ORWE.CA: score=15.23 buy_ready=False sector_rank=18 price=22.89 support=22.65 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=4215161.0 spike=0.11
- PHAR.CA: score=19.82 buy_ready=True sector_rank=4 price=87.18 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=52.04 liquidity=3418382.0 spike=0.1
- PHDC.CA: score=21.61 buy_ready=False sector_rank=9 price=15.2 support=14.43 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=81293336.0 spike=0.2
- PHTV.CA: score=15.75 buy_ready=False sector_rank=12 price=250.06 support=201.55 resistance=256.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:58 AM market time freshness=DELAYED_CURRENT RSI=87.78 liquidity=3356863.25 spike=0.17
- POUL.CA: score=22.99 buy_ready=True sector_rank=15 price=39.12 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=59.88 liquidity=5837021.0 spike=0.15
- PRCL.CA: score=22.92 buy_ready=True sector_rank=19 price=30.21 support=22.02 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=27608900.0 spike=0.76
- PRDC.CA: score=25.61 buy_ready=True sector_rank=9 price=7.29 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=63.66 liquidity=36669312.0 spike=0.33
- PRMH.CA: score=19.77 buy_ready=False sector_rank=12 price=2.57 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=37.62 liquidity=8374767.5 spike=0.28
- RACC.CA: score=15.1 buy_ready=True sector_rank=12 price=9.87 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=41.58 liquidity=1708183.25 spike=0.18
- RAKT.CA: score=9.45 buy_ready=False sector_rank=12 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=37.86 liquidity=58537.63 spike=0.25
- RAYA.CA: score=26.4 buy_ready=True sector_rank=2 price=7.39 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=46.7 liquidity=35243792.0 spike=0.4
- RMDA.CA: score=21.13 buy_ready=False sector_rank=4 price=5.01 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=44.9 liquidity=8728122.0 spike=0.11
- ROTO.CA: score=21.43 buy_ready=False sector_rank=12 price=42.06 support=32.76 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=75.77 liquidity=41437780.0 spike=1.52
- RREI.CA: score=14.15 buy_ready=False sector_rank=12 price=3.5 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=5762296.5 spike=0.29
- RTVC.CA: score=11.05 buy_ready=False sector_rank=12 price=3.76 support=3.76 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=2656152.0 spike=0.56
- RUBX.CA: score=22.01 buy_ready=True sector_rank=12 price=10.51 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=6622292.5 spike=0.68
- SAUD.CA: score=4.64 buy_ready=False sector_rank=17 price=21.05 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=19.48 liquidity=1568197.63 spike=0.18
- SCEM.CA: score=18.76 buy_ready=False sector_rank=19 price=63.0 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=39.9 liquidity=7838439.5 spike=0.41
- SCFM.CA: score=4.1 buy_ready=False sector_rank=12 price=242.66 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=28.61 liquidity=707631.88 spike=0.11
- SCTS.CA: score=9.02 buy_ready=False sector_rank=6 price=576.58 support=577.41 resistance=577.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:57 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=881601.94 spike=1.0
- SDTI.CA: score=14.02 buy_ready=False sector_rank=12 price=46.49 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=627289.88 spike=0.05
- SEIG.CA: score=14.39 buy_ready=False sector_rank=12 price=187.67 support=179.43 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=43.31 liquidity=999263.94 spike=0.24
- SIPC.CA: score=5.28 buy_ready=False sector_rank=12 price=3.45 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=1883954.75 spike=0.16
- SKPC.CA: score=10.73 buy_ready=False sector_rank=21 price=16.1 support=15.95 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=31.92 liquidity=13559173.0 spike=0.35
- SMFR.CA: score=4.0 buy_ready=False sector_rank=12 price=198.05 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:03 AM market time freshness=DELAYED_CURRENT RSI=34.4 liquidity=606939.38 spike=0.25
- SNFC.CA: score=20.49 buy_ready=False sector_rank=12 price=12.0 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=37.79 liquidity=9095772.0 spike=0.44
- SPIN.CA: score=14.03 buy_ready=False sector_rank=18 price=14.04 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:06 AM market time freshness=DELAYED_CURRENT RSI=29.13 liquidity=10036840.0 spike=1.51
- SPMD.CA: score=18.07 buy_ready=True sector_rank=12 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=54.97 liquidity=2679540.5 spike=0.1
- SUGR.CA: score=4.26 buy_ready=False sector_rank=15 price=47.2 support=47.27 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=23.98 liquidity=2108262.25 spike=0.24
- SVCE.CA: score=25.49 buy_ready=True sector_rank=12 price=9.56 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=77482880.0 spike=1.05
- SWDY.CA: score=18.97 buy_ready=True sector_rank=10 price=88.23 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=43.89 liquidity=5488294.0 spike=0.31
- TALM.CA: score=18.15 buy_ready=True sector_rank=6 price=15.99 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:05 AM market time freshness=DELAYED_CURRENT RSI=47.56 liquidity=4010053.25 spike=0.5
- TMGH.CA: score=23.61 buy_ready=True sector_rank=9 price=95.8 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=45.8 liquidity=165056512.0 spike=0.34
- TRTO.CA: score=9.39 buy_ready=False sector_rank=12 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=15.82 buy_ready=False sector_rank=12 price=496.25 support=465.01 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=74.13 liquidity=432496.84 spike=0.45
- UEGC.CA: score=13.72 buy_ready=False sector_rank=12 price=1.4 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:09 AM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=2332154.25 spike=0.1
- UNIP.CA: score=14.51 buy_ready=False sector_rank=12 price=0.32 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=3119782.25 spike=0.14
- UNIT.CA: score=7.24 buy_ready=False sector_rank=9 price=13.02 support=12.92 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:02 AM market time freshness=DELAYED_CURRENT RSI=34.19 liquidity=623016.25 spike=0.09
- WCDF.CA: score=8.62 buy_ready=False sector_rank=12 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-23T21:00:00+00:00 freshness=FRESH RSI=44.29 liquidity=223950.96 spike=0.89
- WKOL.CA: score=9.93 buy_ready=False sector_rank=12 price=285.65 support=287.2 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:00 AM market time freshness=DELAYED_CURRENT RSI=36.6 liquidity=1540767.0 spike=0.53
- ZEOT.CA: score=20.39 buy_ready=False sector_rank=12 price=11.1 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:10 AM market time freshness=DELAYED_CURRENT RSI=76.79 liquidity=12717595.0 spike=0.52
- ZMID.CA: score=25.61 buy_ready=True sector_rank=9 price=6.61 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:04 AM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=88089872.0 spike=0.42

## Backtesting Lite
- DAPH.CA: 180d return=5.24%, max drawdown=-30.86%, MA20>MA50 days last20=12, as_of=2026-06-23T21:00:00+00:00
- OCDI.CA: 180d return=48.65%, max drawdown=-18.11%, MA20>MA50 days last20=10, as_of=2026-06-23T21:00:00+00:00
- CIRA.CA: 180d return=82.14%, max drawdown=-17.17%, MA20>MA50 days last20=20, as_of=2026-06-23T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- DAPH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Development & Engineering Consultants summary=Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- GIHD.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3828 sources=3 expected=Gharbia Islamic Housing Development Company summary=Gharbia Islamic Housing to discuss raising capital mid-December; Gharbia Islamic Housing to distribute EGP 0.2/shr; Gharbia Islamic Housing profits fall 46% in 2016
  - Gharbia Islamic Housing to discuss raising capital mid-December: https://english.mubasher.info/news/3147599/Gharbia-Islamic-Housing-to-discuss-raising-capital-mid-December/
  - Gharbia Islamic Housing to distribute EGP 0.2/shr: https://english.mubasher.info/news/3082262/Gharbia-Islamic-Housing-to-distribute-EGP-0-2-shr/
  - Gharbia Islamic Housing profits fall 46% in 2016: https://english.mubasher.info/news/3068305/Gharbia-Islamic-Housing-profits-fall-46-in-2016/
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=540 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=540 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=540 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=540 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/

## Warnings
- Evidence rejected for DAPH.CA: source text did not clearly match DAPH.CA / Development & Engineering Consultants.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence for GIHD.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
