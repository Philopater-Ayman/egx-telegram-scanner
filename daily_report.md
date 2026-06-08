# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-08T11:22:46.463612+00:00
Generated Cairo: 2026-06-08 14:22
Run timing: target 09:15 Cairo | generated Cairo 2026-06-08 14:22 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-08 14:19

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 63
- Data quality issues: 0
- Tradeable price/liquidity tickers: 185/190
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, June 08
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.0% / above MA50 70.0%
- EGX70 regime: MIXED / above MA20 48.72% / above MA50 82.05%
- Sector breadth: 61.9%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- RMDA.CA: liquidity=1040597248.0 spike=18.54 score=32.4
- CCAP.CA: liquidity=816531456.0 spike=0.96 score=31.4
- COMI.CA: liquidity=668613312.0 spike=1.03 score=18.76
- EFID.CA: liquidity=600245568.0 spike=12.49 score=24.13
- ELSH.CA: liquidity=464147968.0 spike=5.13 score=14.37

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner found no trade‑ready candidates after applying evidence, liquidity, freshness and technical filters, so the default action is HOLD. EGX30 remains bearish with weak breadth below MA20, while EGX70 shows mixed signals and better breadth. Risk mode is set to SELECTIVE_SWING_TRADES_ONLY, meaning only high‑conviction swing setups would be considered if they emerged.
- Liquidity spikes in RMDA.CA, ECAP.CA, MPRC.CA and others suggest accumulation, but lack of reliable news evidence keeps them out of the trade list.
- Healthcare and Investment Holding sectors lead breadth (≈62% overall), yet most top‑ranked tickets sit near resistance or show overbought RSI, adding short‑term uncertainty.
- EGX30 bearish trend and low % above MA20 increase downside risk; EGX70 mixed trend offers limited upside, so the scanner stays in a defensive HOLD stance for the next 1‑3 days.

## Top Liquidity Spikes
- RMDA.CA: spike=18.54 liquidity=1040597248.0 outlook=BULLISH_WATCH score=100 buy_ready=True
- EFID.CA: spike=12.49 liquidity=600245568.0 outlook=NEUTRAL score=47.33 buy_ready=False
- ELSH.CA: spike=5.13 liquidity=464147968.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- LUTS.CA: spike=3.79 liquidity=51360668.0 outlook=BULLISH_WATCH score=73.92 buy_ready=False
- PRCL.CA: spike=3.19 liquidity=102811912.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=10.73 5d=6.55% 20d=12.31% aboveMA50=66.67%
- #2 Tourism & Leisure: score=9.8 5d=0.75% 20d=14.57% aboveMA50=100.0%
- #3 Healthcare: score=8.99 5d=3.62% 20d=7.32% aboveMA50=100.0%
- #4 Technology & Distribution: score=8.68 5d=3.21% 20d=18.4% aboveMA50=100.0%
- #5 Real Estate: score=7.92 5d=1.26% 20d=11.28% aboveMA50=84.62%
- #6 Textiles: score=7.26 5d=1.5% 20d=6.29% aboveMA50=75.0%
- #7 Agriculture & Food Production: score=6.21 5d=4.46% 20d=0.38% aboveMA50=50.0%
- #8 General / Verified EGX Expansion: score=5.92 5d=2.25% 20d=1.3% aboveMA50=82.69%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- RMDA.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- MPRC.CA: BULLISH_WATCH score=95.92 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NIPH.CA: BULLISH_WATCH score=94.99 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=94.92 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ISPH.CA: BULLISH_WATCH score=91.99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- NEDA.CA: BULLISH_WATCH score=89.92 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance; sector is not leading
- MHOT.CA: BULLISH_WATCH score=89.8 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- AJWA.CA: BULLISH_WATCH score=87.92 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CCAP.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=far above support; close to resistance
- BINV.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=momentum is extended

## BUY-Ready Candidates
- RMDA.CA: rank=32.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=5.25 support=4.78 resistance=5.19 liquidity=1040597248.0
- CCAP.CA: rank=31.4 outlook=BULLISH_WATCH outlook_score=87 sector_rank=1 price=5.65 support=4.55 resistance=5.72 liquidity=816531456.0
- ECAP.CA: rank=30.67 outlook=BULLISH_WATCH outlook_score=81.92 sector_rank=8 price=31.29 support=28.7 resistance=31.5 liquidity=15541062.0
- MPRC.CA: rank=29.57 outlook=BULLISH_WATCH outlook_score=95.92 sector_rank=8 price=33.5 support=30.61 resistance=34.55 liquidity=32588596.0
- NCCW.CA: rank=28.41 outlook=BULLISH_WATCH outlook_score=83.92 sector_rank=8 price=6.19 support=5.13 resistance=6.5 liquidity=40271200.0
- AREH.CA: rank=27.97 outlook=BULLISH_WATCH outlook_score=81.92 sector_rank=8 price=1.5 support=1.27 resistance=1.57 liquidity=45594612.0
- BINV.CA: rank=27.6 outlook=BULLISH_WATCH outlook_score=87 sector_rank=1 price=46.0 support=40.5 resistance=49.5 liquidity=14334089.0
- GDWA.CA: rank=27.59 outlook=BULLISH_WATCH outlook_score=72.92 sector_rank=8 price=0.82 support=0.77 resistance=0.83 liquidity=12017676.0
- MPCO.CA: rank=27.46 outlook=BULLISH_WATCH outlook_score=85.21 sector_rank=7 price=1.78 support=1.54 resistance=1.93 liquidity=97290008.0
- CERA.CA: rank=27.17 outlook=BULLISH_WATCH outlook_score=82.92 sector_rank=8 price=1.2 support=1.13 resistance=1.23 liquidity=40354584.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=16.15 buy_ready=True sector_rank=8 price=211.35 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=48.5 liquidity=1781922.5 spike=0.13
- ABUK.CA: score=13.0 buy_ready=False sector_rank=17 price=82.0 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=26.31 liquidity=84805984.0 spike=0.65
- ACAMD.CA: score=26.41 buy_ready=True sector_rank=8 price=2.3 support=1.96 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=64.81 liquidity=119334288.0 spike=1.02
- ACGC.CA: score=24.4 buy_ready=True sector_rank=6 price=9.75 support=8.3 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=38361040.0 spike=0.7
- ADCI.CA: score=17.85 buy_ready=True sector_rank=8 price=215.04 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=3484127.5 spike=0.5
- ADIB.CA: score=21.7 buy_ready=False sector_rank=14 price=46.32 support=44.45 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=54.16 liquidity=56120816.0 spike=0.34
- ADPC.CA: score=16.12 buy_ready=False sector_rank=8 price=3.68 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=37.72 liquidity=6749350.5 spike=0.28
- AFDI.CA: score=21.28 buy_ready=True sector_rank=8 price=43.91 support=37.54 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=65.21 liquidity=6907889.0 spike=0.38
- AFMC.CA: score=15.36 buy_ready=False sector_rank=8 price=72.9 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=37.49 liquidity=2993343.75 spike=0.22
- AJWA.CA: score=25.57 buy_ready=True sector_rank=8 price=134.2 support=130.01 resistance=139.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=50.49 liquidity=16415488.0 spike=1.6
- ALCN.CA: score=17.47 buy_ready=False sector_rank=18 price=28.81 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=9522322.0 spike=0.39
- ALUM.CA: score=24.41 buy_ready=True sector_rank=8 price=25.24 support=22.5 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=56.55 liquidity=6040594.5 spike=0.27
- AMER.CA: score=24.4 buy_ready=True sector_rank=5 price=2.73 support=2.3 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=51.9 liquidity=55962256.0 spike=0.43
- AMES.CA: score=8.94 buy_ready=False sector_rank=8 price=50.66 support=48.0 resistance=57.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=29.19 liquidity=1568611.63 spike=0.17
- AMIA.CA: score=18.56 buy_ready=True sector_rank=8 price=8.93 support=8.25 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=4196817.0 spike=0.13
- AMOC.CA: score=17.25 buy_ready=False sector_rank=9 price=8.32 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=21.05 liquidity=84639880.0 spike=0.98
- ANFI.CA: score=13.01 buy_ready=False sector_rank=8 price=14.05 support=13.5 resistance=15.55 source=Yahoo Finance as_of=2026-06-03T21:00:00+00:00 freshness=FRESH RSI=24.73 liquidity=5638883.28 spike=0.28
- APSW.CA: score=11.87 buy_ready=False sector_rank=8 price=8.91 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=505992.28 spike=0.45
- ARAB.CA: score=20.4 buy_ready=False sector_rank=5 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=56361700.0 spike=0.73
- ARCC.CA: score=23.9 buy_ready=True sector_rank=12 price=57.67 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=68.08 liquidity=24813674.0 spike=0.56
- AREH.CA: score=27.97 buy_ready=True sector_rank=8 price=1.5 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=45594612.0 spike=1.8
- ARVA.CA: score=23.37 buy_ready=False sector_rank=8 price=10.97 support=7.71 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=75.37 liquidity=25109702.0 spike=0.99
- ASCM.CA: score=24.37 buy_ready=False sector_rank=8 price=55.23 support=44.75 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=73.58 liquidity=38678152.0 spike=0.59
- ASPI.CA: score=10.25 buy_ready=False sector_rank=8 price=0.34 support=0.34 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77415152.0 spike=1.44
- ATLC.CA: score=16.75 buy_ready=True sector_rank=16 price=5.02 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.3 liquidity=3625451.75 spike=0.45
- ATQA.CA: score=24.0 buy_ready=True sector_rank=17 price=9.86 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.77 liquidity=16979002.0 spike=0.35
- AXPH.CA: score=10.15 buy_ready=False sector_rank=8 price=1136.47 support=985.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=20.12 liquidity=2777568.5 spike=0.48
- BINV.CA: score=27.6 buy_ready=True sector_rank=1 price=46.0 support=40.5 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=66.86 liquidity=14334089.0 spike=1.1
- BIOC.CA: score=18.43 buy_ready=True sector_rank=8 price=73.58 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=4065215.0 spike=0.54
- BTFH.CA: score=15.12 buy_ready=False sector_rank=16 price=3.05 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=31.37 liquidity=91254040.0 spike=0.37
- CAED.CA: score=9.8 buy_ready=False sector_rank=8 price=71.62 support=66.56 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=26.71 liquidity=2433213.75 spike=0.16
- CANA.CA: score=27.16 buy_ready=True sector_rank=14 price=38.1 support=33.15 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=63.1 liquidity=24678620.0 spike=1.73
- CCAP.CA: score=31.4 buy_ready=True sector_rank=1 price=5.65 support=4.55 resistance=5.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=816531456.0 spike=0.96
- CCRS.CA: score=24.37 buy_ready=False sector_rank=8 price=2.5 support=2.0 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=15082121.0 spike=0.55
- CEFM.CA: score=8.59 buy_ready=False sector_rank=8 price=106.59 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=25.15 liquidity=1221093.25 spike=0.17
- CERA.CA: score=27.17 buy_ready=True sector_rank=8 price=1.2 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=40354584.0 spike=2.9
- CFGH.CA: score=3.37 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=2804.02 spike=0.7
- CICH.CA: score=12.66 buy_ready=False sector_rank=16 price=12.13 support=11.01 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=1534335.75 spike=0.34
- CIEB.CA: score=15.38 buy_ready=False sector_rank=14 price=23.53 support=23.31 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3675691.25 spike=0.31
- CIRA.CA: score=19.35 buy_ready=False sector_rank=15 price=26.19 support=21.0 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=56.48 liquidity=7817150.5 spike=0.27
- CLHO.CA: score=23.4 buy_ready=False sector_rank=3 price=15.22 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=24394612.0 spike=0.65
- CNFN.CA: score=22.7 buy_ready=False sector_rank=16 price=4.6 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=37123328.0 spike=2.29
- COMI.CA: score=18.76 buy_ready=False sector_rank=14 price=130.13 support=131.3 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=668613312.0 spike=1.03
- COPR.CA: score=23.37 buy_ready=True sector_rank=8 price=0.36 support=0.31 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=15840564.0 spike=0.41
- COSG.CA: score=26.37 buy_ready=True sector_rank=8 price=1.62 support=1.45 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=50596780.0 spike=0.87
- CPCI.CA: score=17.03 buy_ready=False sector_rank=8 price=364.82 support=340.01 resistance=374.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=72.04 liquidity=2657785.75 spike=0.36
- CSAG.CA: score=22.95 buy_ready=False sector_rank=18 price=31.21 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=53.77 liquidity=11715433.0 spike=0.6
- DAPH.CA: score=12.52 buy_ready=False sector_rank=8 price=80.85 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=16.14 liquidity=5154759.0 spike=0.16
- DEIN.CA: score=10.37 buy_ready=False sector_rank=8 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=4.92 buy_ready=False sector_rank=10 price=24.47 support=24.45 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=22.14 liquidity=783058.0 spike=0.32
- DSCW.CA: score=20.37 buy_ready=False sector_rank=8 price=1.81 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=18256994.0 spike=0.28
- DTPP.CA: score=8.16 buy_ready=False sector_rank=8 price=124.93 support=121.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=27.48 liquidity=793698.69 spike=0.14
- EALR.CA: score=13.98 buy_ready=False sector_rank=8 price=353.45 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=1607702.88 spike=0.13
- EASB.CA: score=15.51 buy_ready=True sector_rank=8 price=5.06 support=4.61 resistance=5.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=1140766.5 spike=0.7
- EAST.CA: score=26.61 buy_ready=True sector_rank=10 price=39.84 support=37.01 resistance=39.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=53.99 liquidity=86705504.0 spike=1.24
- EBSC.CA: score=17.47 buy_ready=True sector_rank=8 price=1.84 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=63.64 liquidity=1104910.88 spike=0.37
- ECAP.CA: score=30.67 buy_ready=True sector_rank=8 price=31.29 support=28.7 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=59.45 liquidity=15541062.0 spike=3.15
- EDFM.CA: score=13.38 buy_ready=False sector_rank=8 price=333.99 support=320.2 resistance=349.0 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=39.0 liquidity=667979.98 spike=1.17
- EEII.CA: score=26.51 buy_ready=True sector_rank=8 price=2.45 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=36488040.0 spike=2.07
- EFIC.CA: score=4.46 buy_ready=False sector_rank=17 price=204.6 support=195.25 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=6.17 liquidity=2461616.0 spike=0.55
- EFID.CA: score=24.13 buy_ready=False sector_rank=10 price=28.3 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=76.47 liquidity=600245568.0 spike=12.49
- EFIH.CA: score=19.7 buy_ready=False sector_rank=21 price=21.12 support=21.3 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=49.84 liquidity=40627996.0 spike=0.63
- EGAL.CA: score=21.0 buy_ready=False sector_rank=17 price=318.81 support=303.05 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=54.23 liquidity=43153096.0 spike=0.38
- EGAS.CA: score=15.77 buy_ready=True sector_rank=9 price=49.83 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=3526758.25 spike=0.24
- EGBE.CA: score=6.76 buy_ready=False sector_rank=14 price=0.45 support=0.41 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=54591.41 spike=0.36
- EGCH.CA: score=25.0 buy_ready=True sector_rank=17 price=14.6 support=11.95 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=49.0 liquidity=52547248.0 spike=0.44
- EGSA.CA: score=9.1 buy_ready=False sector_rank=11 price=8.89 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=84.34 liquidity=15330.06 spike=0.95
- EGTS.CA: score=22.4 buy_ready=False sector_rank=5 price=17.48 support=12.9 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=54551296.0 spike=0.49
- EHDR.CA: score=21.39 buy_ready=False sector_rank=8 price=2.66 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=75.71 liquidity=53256964.0 spike=1.01
- EKHO.CA: score=14.25 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=22.72 buy_ready=False sector_rank=13 price=2.15 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=14060370.0 spike=0.47
- ELKA.CA: score=25.37 buy_ready=True sector_rank=8 price=1.26 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=34311932.0 spike=0.81
- ELNA.CA: score=7.69 buy_ready=False sector_rank=8 price=39.54 support=37.11 resistance=42.79 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=31.33 liquidity=323002.27 spike=1.0
- ELSH.CA: score=14.37 buy_ready=False sector_rank=8 price=13.3 support=11.15 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=464147968.0 spike=5.13
- ELWA.CA: score=15.9 buy_ready=False sector_rank=8 price=2.11 support=1.79 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=84.62 liquidity=3875886.75 spike=1.33
- EMFD.CA: score=26.7 buy_ready=False sector_rank=5 price=12.1 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=71.51 liquidity=262237968.0 spike=1.15
- ENGC.CA: score=26.37 buy_ready=True sector_rank=8 price=34.04 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=42.02 liquidity=10881181.0 spike=0.91
- EOSB.CA: score=14.9 buy_ready=False sector_rank=8 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=253515.43 spike=2.14
- EPCO.CA: score=18.81 buy_ready=False sector_rank=8 price=9.12 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=46.78 liquidity=4443019.5 spike=0.35
- EPPK.CA: score=8.48 buy_ready=False sector_rank=8 price=12.5 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=1516340.5 spike=1.3
- ETEL.CA: score=22.08 buy_ready=False sector_rank=11 price=94.42 support=93.01 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=50.71 liquidity=50981388.0 spike=0.46
- ETRS.CA: score=24.55 buy_ready=False sector_rank=8 price=8.92 support=7.37 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=54295540.0 spike=1.09
- EXPA.CA: score=23.96 buy_ready=False sector_rank=14 price=19.2 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=72.8 liquidity=51483812.0 spike=1.13
- FAIT.CA: score=15.13 buy_ready=True sector_rank=14 price=37.43 support=33.57 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=1421394.13 spike=0.2
- FAITA.CA: score=11.71 buy_ready=False sector_rank=14 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=10019.24 spike=0.19
- FERC.CA: score=4.29 buy_ready=False sector_rank=17 price=77.36 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=27.01 liquidity=1285158.38 spike=0.19
- FWRY.CA: score=17.12 buy_ready=False sector_rank=21 price=18.35 support=18.6 resistance=21.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=347214720.0 spike=1.21
- GBCO.CA: score=12.14 buy_ready=False sector_rank=20 price=26.27 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=31.56 liquidity=51506744.0 spike=0.44
- GDWA.CA: score=27.59 buy_ready=True sector_rank=8 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=12017676.0 spike=1.11
- GGCC.CA: score=23.68 buy_ready=False sector_rank=8 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=7869449.5 spike=1.22
- GIHD.CA: score=18.39 buy_ready=True sector_rank=8 price=41.49 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=46.01 liquidity=2024634.5 spike=0.35
- GMCI.CA: score=16.69 buy_ready=False sector_rank=8 price=1.78 support=1.67 resistance=1.84 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=60.71 liquidity=317931.13 spike=0.89
- GRCA.CA: score=7.31 buy_ready=False sector_rank=8 price=54.47 support=53.36 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=30.73 liquidity=2943663.25 spike=0.31
- GSSC.CA: score=7.38 buy_ready=False sector_rank=8 price=249.16 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=4.44 liquidity=3008331.0 spike=0.3
- GTWL.CA: score=9.08 buy_ready=False sector_rank=8 price=45.87 support=46.3 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=10.97 liquidity=4711823.5 spike=0.42
- HDBK.CA: score=22.68 buy_ready=False sector_rank=14 price=142.12 support=140.0 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=24383838.0 spike=1.49
- HELI.CA: score=22.4 buy_ready=False sector_rank=5 price=6.4 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=56.02 liquidity=51137776.0 spike=0.3
- HRHO.CA: score=17.12 buy_ready=False sector_rank=16 price=26.4 support=26.16 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=154956976.0 spike=0.74
- ICID.CA: score=21.93 buy_ready=False sector_rank=8 price=6.1 support=4.4 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=78.54 liquidity=8558274.0 spike=0.69
- IDRE.CA: score=22.37 buy_ready=False sector_rank=8 price=43.56 support=39.72 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=47.94 liquidity=10371915.0 spike=0.3
- IFAP.CA: score=8.0 buy_ready=False sector_rank=7 price=19.36 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=31.0 liquidity=4600967.5 spike=0.27
- INFI.CA: score=15.8 buy_ready=False sector_rank=8 price=100.86 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=4428997.5 spike=0.26
- IRON.CA: score=12.12 buy_ready=False sector_rank=17 price=32.52 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=51.17 liquidity=3116251.25 spike=0.36
- ISMA.CA: score=23.37 buy_ready=False sector_rank=8 price=28.65 support=19.8 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=98.97 liquidity=48191568.0 spike=1.0
- ISMQ.CA: score=25.0 buy_ready=True sector_rank=17 price=7.81 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=28297562.0 spike=0.55
- ISPH.CA: score=28.8 buy_ready=False sector_rank=3 price=12.44 support=11.12 resistance=12.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=74.25 liquidity=243007280.0 spike=1.7
- JUFO.CA: score=26.13 buy_ready=True sector_rank=10 price=29.86 support=26.51 resistance=29.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=32322714.0 spike=0.72
- KABO.CA: score=26.4 buy_ready=True sector_rank=6 price=6.3 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=64.89 liquidity=10168903.0 spike=0.51
- KWIN.CA: score=13.68 buy_ready=False sector_rank=8 price=72.0 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=43.56 liquidity=1314506.38 spike=0.31
- KZPC.CA: score=16.17 buy_ready=False sector_rank=8 price=10.54 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=42.66 liquidity=3797583.5 spike=0.32
- LCSW.CA: score=21.9 buy_ready=False sector_rank=12 price=27.01 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=11173798.0 spike=0.64
- LUTS.CA: score=28.37 buy_ready=False sector_rank=8 price=0.63 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=78.81 liquidity=51360668.0 spike=3.79
- MAAL.CA: score=23.65 buy_ready=False sector_rank=8 price=5.95 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=97.28 liquidity=12857811.0 spike=1.14
- MASR.CA: score=22.37 buy_ready=False sector_rank=8 price=6.87 support=6.46 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=19479466.0 spike=0.31
- MBSC.CA: score=24.5 buy_ready=True sector_rank=12 price=275.03 support=259.63 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=55.46 liquidity=61702336.0 spike=1.3
- MCQE.CA: score=21.9 buy_ready=False sector_rank=12 price=190.89 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=58.89 liquidity=13762862.0 spike=0.71
- MCRO.CA: score=25.37 buy_ready=True sector_rank=8 price=1.27 support=1.21 resistance=1.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=64108828.0 spike=0.68
- MENA.CA: score=24.64 buy_ready=True sector_rank=5 price=6.75 support=5.76 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=61.37 liquidity=8242286.5 spike=0.5
- MEPA.CA: score=19.89 buy_ready=False sector_rank=8 price=1.71 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=7520281.0 spike=0.32
- MFPC.CA: score=16.0 buy_ready=False sector_rank=17 price=42.64 support=42.3 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=21.93 liquidity=62602676.0 spike=0.61
- MFSC.CA: score=10.59 buy_ready=False sector_rank=8 price=47.51 support=33.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=30.21 liquidity=3226761.75 spike=0.22
- MHOT.CA: score=26.07 buy_ready=True sector_rank=2 price=30.6 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=7668873.5 spike=0.39
- MICH.CA: score=22.07 buy_ready=True sector_rank=8 price=36.29 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=49.24 liquidity=5702454.5 spike=0.64
- MILS.CA: score=24.25 buy_ready=True sector_rank=8 price=140.68 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=52.36 liquidity=7882015.0 spike=0.28
- MIPH.CA: score=11.85 buy_ready=False sector_rank=3 price=669.81 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.24 liquidity=1445686.0 spike=0.33
- MOED.CA: score=8.07 buy_ready=False sector_rank=8 price=0.69 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=16.5 liquidity=4698649.5 spike=0.34
- MOIL.CA: score=16.35 buy_ready=False sector_rank=9 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=102546.24 spike=0.51
- MOIN.CA: score=14.27 buy_ready=False sector_rank=8 price=24.96 support=23.13 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=53.71 liquidity=898858.44 spike=0.36
- MOSC.CA: score=9.9 buy_ready=False sector_rank=8 price=270.15 support=268.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=17.07 liquidity=2532329.0 spike=0.13
- MPCI.CA: score=26.37 buy_ready=True sector_rank=8 price=226.72 support=187.01 resistance=224.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=63.07 liquidity=73852848.0 spike=0.75
- MPCO.CA: score=27.46 buy_ready=True sector_rank=7 price=1.78 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=63.83 liquidity=97290008.0 spike=1.53
- MPRC.CA: score=29.57 buy_ready=True sector_rank=8 price=33.5 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=32588596.0 spike=1.6
- MTIE.CA: score=18.36 buy_ready=False sector_rank=20 price=9.02 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=8225429.5 spike=0.32
- NAHO.CA: score=3.4 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=32070.31 spike=0.86
- NCCW.CA: score=28.41 buy_ready=True sector_rank=8 price=6.19 support=5.13 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=67.37 liquidity=40271200.0 spike=2.02
- NEDA.CA: score=20.18 buy_ready=True sector_rank=8 price=2.83 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=1393078.78 spike=2.21
- NHPS.CA: score=12.26 buy_ready=False sector_rank=8 price=68.49 support=67.53 resistance=73.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=38.38 liquidity=887276.81 spike=0.08
- NINH.CA: score=15.04 buy_ready=False sector_rank=8 price=17.85 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=47.16 liquidity=2670088.75 spike=0.19
- NIPH.CA: score=25.4 buy_ready=True sector_rank=3 price=170.36 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=59.65 liquidity=98929096.0 spike=0.79
- OBRI.CA: score=11.42 buy_ready=False sector_rank=8 price=34.3 support=34.2 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=26.33 liquidity=7052970.5 spike=0.58
- OCDI.CA: score=19.4 buy_ready=False sector_rank=5 price=20.71 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=44.4 liquidity=15642191.0 spike=0.35
- OCPH.CA: score=9.82 buy_ready=False sector_rank=8 price=357.23 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=20.34 liquidity=2453314.0 spike=0.18
- ODIN.CA: score=20.84 buy_ready=True sector_rank=8 price=2.05 support=1.89 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=6470322.5 spike=0.64
- OFH.CA: score=24.72 buy_ready=True sector_rank=8 price=0.63 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=43.4 liquidity=8353300.5 spike=0.37
- OIH.CA: score=17.72 buy_ready=False sector_rank=1 price=1.41 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=12.5 liquidity=151649312.0 spike=1.16
- OLFI.CA: score=22.13 buy_ready=False sector_rank=10 price=21.62 support=21.0 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=43.78 liquidity=13704303.0 spike=0.62
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=722.63 support=710.01 resistance=730.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=144450352.0 spike=1.0
- ORHD.CA: score=22.4 buy_ready=True sector_rank=5 price=36.5 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=150037584.0 spike=0.73
- ORWE.CA: score=21.4 buy_ready=False sector_rank=6 price=23.64 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=76.41 liquidity=33689656.0 spike=0.7
- PHAR.CA: score=19.74 buy_ready=False sector_rank=3 price=86.59 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=6342886.0 spike=0.17
- PHDC.CA: score=24.4 buy_ready=True sector_rank=5 price=14.81 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=64.65 liquidity=263687888.0 spike=0.61
- PHTV.CA: score=14.92 buy_ready=False sector_rank=8 price=206.01 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=44.25 liquidity=2551980.75 spike=0.17
- POUL.CA: score=24.13 buy_ready=True sector_rank=10 price=36.89 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=60.39 liquidity=11986566.0 spike=0.24
- PRCL.CA: score=13.28 buy_ready=False sector_rank=12 price=26.45 support=24.26 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=102811912.0 spike=3.19
- PRDC.CA: score=24.4 buy_ready=True sector_rank=5 price=6.05 support=5.2 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=69.29 liquidity=10410057.0 spike=0.52
- PRMH.CA: score=22.33 buy_ready=False sector_rank=8 price=2.8 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=76.04 liquidity=22715590.0 spike=1.48
- RACC.CA: score=16.68 buy_ready=False sector_rank=8 price=9.84 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=57.05 liquidity=4308136.0 spike=0.14
- RAKT.CA: score=7.48 buy_ready=False sector_rank=8 price=23.79 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=34.57 liquidity=113287.98 spike=0.44
- RAYA.CA: score=24.4 buy_ready=False sector_rank=4 price=7.39 support=6.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=62.76 liquidity=57502888.0 spike=0.48
- RMDA.CA: score=32.4 buy_ready=True sector_rank=3 price=5.25 support=4.78 resistance=5.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=62.85 liquidity=1040597248.0 spike=18.54
- ROTO.CA: score=22.13 buy_ready=True sector_rank=8 price=33.81 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=43.85 liquidity=7758496.5 spike=0.6
- RREI.CA: score=26.37 buy_ready=True sector_rank=8 price=3.57 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=17415730.0 spike=0.74
- RTVC.CA: score=10.24 buy_ready=False sector_rank=8 price=3.99 support=3.77 resistance=3.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9791582.0 spike=1.54
- RUBX.CA: score=16.96 buy_ready=False sector_rank=8 price=10.27 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=31.69 liquidity=9593593.0 spike=0.61
- SAUD.CA: score=18.52 buy_ready=False sector_rank=14 price=22.28 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=47.0 liquidity=6819079.0 spike=0.47
- SCEM.CA: score=19.06 buy_ready=False sector_rank=12 price=63.56 support=62.07 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=42.14 liquidity=7156234.0 spike=0.16
- SCFM.CA: score=9.94 buy_ready=False sector_rank=8 price=259.51 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=22.13 liquidity=2573836.0 spike=0.09
- SCTS.CA: score=10.07 buy_ready=False sector_rank=15 price=612.66 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=14.59 liquidity=3535975.0 spike=0.31
- SDTI.CA: score=18.74 buy_ready=True sector_rank=8 price=45.73 support=43.4 resistance=46.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=55.97 liquidity=4371393.5 spike=0.22
- SEIG.CA: score=17.64 buy_ready=True sector_rank=8 price=187.11 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=53.14 liquidity=1268047.63 spike=0.21
- SIPC.CA: score=26.37 buy_ready=True sector_rank=8 price=3.63 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=13230747.0 spike=0.86
- SKPC.CA: score=12.0 buy_ready=False sector_rank=17 price=17.17 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.72 liquidity=61575296.0 spike=0.83
- SMFR.CA: score=9.76 buy_ready=False sector_rank=8 price=206.2 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=29.94 liquidity=2392861.5 spike=0.2
- SNFC.CA: score=20.39 buy_ready=False sector_rank=8 price=11.88 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=8022560.0 spike=0.29
- SPIN.CA: score=10.98 buy_ready=False sector_rank=6 price=14.1 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=1575502.63 spike=0.32
- SPMD.CA: score=26.97 buy_ready=True sector_rank=8 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=66.96 liquidity=31023412.0 spike=1.3
- SUGR.CA: score=19.46 buy_ready=False sector_rank=10 price=49.17 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=36.46 liquidity=5324903.5 spike=0.32
- SVCE.CA: score=22.37 buy_ready=False sector_rank=8 price=8.69 support=7.98 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=53634864.0 spike=0.38
- SWDY.CA: score=21.72 buy_ready=False sector_rank=13 price=87.46 support=85.25 resistance=91.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=13926397.0 spike=0.39
- TALM.CA: score=15.61 buy_ready=False sector_rank=15 price=15.9 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=4069403.75 spike=0.31
- TMGH.CA: score=22.4 buy_ready=False sector_rank=5 price=96.0 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=218583504.0 spike=0.4
- TRTO.CA: score=10.37 buy_ready=False sector_rank=8 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=3.74 buy_ready=False sector_rank=8 price=474.09 support=455.6 resistance=508.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=30.99 liquidity=375508.84 spike=0.22
- UEGC.CA: score=27.69 buy_ready=False sector_rank=8 price=1.44 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=40540988.0 spike=1.66
- UNIP.CA: score=22.37 buy_ready=False sector_rank=8 price=0.32 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=78.46 liquidity=14723506.0 spike=0.95
- UNIT.CA: score=25.58 buy_ready=True sector_rank=5 price=14.27 support=10.83 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=9181889.0 spike=0.91
- WCDF.CA: score=7.74 buy_ready=False sector_rank=8 price=539.17 support=535.0 resistance=559.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=15.04 liquidity=370845.44 spike=0.49
- WKOL.CA: score=5.74 buy_ready=False sector_rank=8 price=292.88 support=290.0 resistance=339.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=30.88 liquidity=1368201.0 spike=0.18
- ZEOT.CA: score=19.33 buy_ready=True sector_rank=8 price=9.14 support=8.43 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=55.41 liquidity=2964632.5 spike=0.35
- ZMID.CA: score=25.82 buy_ready=True sector_rank=5 price=6.26 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=339655040.0 spike=1.71

## Backtesting Lite
- RMDA.CA: 180d return=26.65%, max drawdown=-31.33%, MA20>MA50 days last20=20, as_of=2026-06-06T21:00:00+00:00
- CCAP.CA: 180d return=120.08%, max drawdown=-25.0%, MA20>MA50 days last20=20, as_of=2026-06-06T21:00:00+00:00
- ECAP.CA: 180d return=7.11%, max drawdown=-28.16%, MA20>MA50 days last20=20, as_of=2026-06-06T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- ECAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Ezz Ceramics & Porcelain Co. summary=Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- ISPH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=523 sources=3 expected=Ibn Sina Pharma summary=Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025; EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse; Ibnsina Pharma pens import, distribution deal with OMRON Healthcare
  - Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025: https://english.mubasher.info/news/4563237/Ibnsina-Pharma-s-consolidated-profits-jump-to-EGP-952m-in-2025/
  - EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse: https://english.mubasher.info/news/4552027/EBRD-grants-EGP-1-3bn-loan-to-Ibnsina-Pharma-for-new-warehouse/
  - Ibnsina Pharma pens import, distribution deal with OMRON Healthcare: https://english.mubasher.info/news/4028068/Ibnsina-Pharma-pens-import-distribution-deal-with-OMRON-Healthcare/
- NCCW.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Nasr Company for Civil Works summary=Nasr for Civil Works unveils EGP 150m capital increase; Arabia Investments, Nasr Company for Civil Works unveil capital hike; Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda
  - Nasr for Civil Works unveils EGP 150m capital increase: https://english.mubasher.info/news/4550493/Nasr-for-Civil-Works-unveils-EGP-150m-capital-increase/
  - Arabia Investments, Nasr Company for Civil Works unveil capital hike: https://english.mubasher.info/news/4284206/Arabia-Investments-Nasr-Company-for-Civil-Works-unveil-capital-hike/
  - Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda: https://english.mubasher.info/news/4249759/Nasr-Company-for-Civil-Works-consortium-signs-EUR-46m-agreement-with-Uganda/
- LUTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lotus Agri Capital summary=Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- AREH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25; Shareholder ups stake in Real Estate Egyptian; Target for Real Estate Investment cuts stake in Real Estate Egyptian
  - Real Estate Egyptian Consortium’s net profits approach EGP 2m in 9M-25: https://english.mubasher.info/news/4528467/Real-Estate-Egyptian-Consortium-s-net-profits-approach-EGP-2m-in-9M-25/
  - Shareholder ups stake in Real Estate Egyptian: https://english.mubasher.info/news/4026301/Shareholder-ups-stake-in-Real-Estate-Egyptian/
  - Target for Real Estate Investment cuts stake in Real Estate Egyptian: https://english.mubasher.info/news/4010821/Target-for-Real-Estate-Investment-cuts-stake-in-Real-Estate-Egyptian/

## Warnings
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- Evidence for ISPH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for NCCW.CA matches the company but no source/report date was detected.
- Mubasher stock page returned no evidence titles for LUTS.CA.
- No Yahoo or Mubasher evidence found for LUTS.CA.
- Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- Evidence for AREH.CA matches the company but no source/report date was detected.
