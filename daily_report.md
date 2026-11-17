# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-11-17T14:54:14.662609+00:00
Generated Cairo: 2026-11-17 16:54
Run timing: target 08:45 Cairo | generated Cairo 2026-11-17 16:54 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-11-17 16:52

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 6
- Tradeable price/liquidity tickers: 184/184
- Top sector: Building Materials

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 84.21% / above MA50 31.58%
- EGX70 regime: BEARISH / above MA20 72.5% / above MA50 20.0%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ETEL.CA: liquidity=762416655.0 spike=2.77 score=25.94
- COMI.CA: liquidity=443762124.09 spike=0.9 score=20.4
- NIPH.CA: liquidity=345068425.0 spike=2.03 score=20.46
- AMES.CA: liquidity=342199773.08 spike=1.95 score=19.05
- CCAP.CA: liquidity=327088671.69 spike=0.82 score=18.23

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- GSSC.CA: spike=7.96 liquidity=18155135.63 outlook=NEUTRAL score=39.37 buy_ready=False
- MENA.CA: spike=7.13 liquidity=43479011.93 outlook=BULLISH_WATCH score=72.9 buy_ready=False
- CIRA.CA: spike=4.71 liquidity=79007070.5 outlook=CONSTRUCTIVE score=56.32 buy_ready=False
- SCFM.CA: spike=4.51 liquidity=17086746.25 outlook=WEAK_OR_RISKY score=34.37 buy_ready=False
- AFMC.CA: spike=4.32 liquidity=122669321.42 outlook=CONSTRUCTIVE score=61.37 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=11.91 5d=4.78% 20d=11.95% aboveMA50=66.67%
- #2 Telecommunications: score=10.66 5d=5.12% 20d=2.65% aboveMA50=100.0%
- #3 Industrial Goods & Cables: score=9.76 5d=3.79% 20d=11.45% aboveMA50=50.0%
- #4 Tourism & Leisure: score=9.21 5d=2.64% 20d=4.27% aboveMA50=100.0%
- #5 Food, Beverages & Tobacco: score=8.28 5d=4.38% 20d=2.53% aboveMA50=28.57%
- #6 Transportation & Logistics: score=7.79 5d=2.48% 20d=2.71% aboveMA50=50.0%
- #7 Fintech & Payments: score=7.62 5d=3.65% 20d=-0.1% aboveMA50=50.0%
- #8 Technology & Distribution: score=7.35 5d=5.22% 20d=2.63% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MBSC.CA: BULLISH_WATCH score=89 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- SCEM.CA: BULLISH_WATCH score=89 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- ARCC.CA: BULLISH_WATCH score=81 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- ETEL.CA: BULLISH_WATCH score=77 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support; close to resistance
- MENA.CA: BULLISH_WATCH score=72.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; sector is not leading
- SDTI.CA: BULLISH_WATCH score=70.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- CEFM.CA: CONSTRUCTIVE score=69.37 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; far above support; sector is not leading
- SAUD.CA: CONSTRUCTIVE score=68.99 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; sector is not leading
- FWRY.CA: CONSTRUCTIVE score=67.62 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50
- MCQE.CA: CONSTRUCTIVE score=67 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA50; overheated RSI; far above support

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EGAL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ISMQ.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=18.15 buy_ready=False sector_rank=12 price=239.05 support=171.02 resistance=269.99 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.12 liquidity=11460535.25 spike=0.58
- ABUK.CA: score=9.66 buy_ready=False sector_rank=17 price=77.1 support=73.6 resistance=95.75 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=31.26 liquidity=89514640.23 spike=0.65
- ACAMD.CA: score=19.93 buy_ready=False sector_rank=12 price=2.02 support=1.86 resistance=2.16 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=63.46 liquidity=82528082.96 spike=1.39
- ACGC.CA: score=14.71 buy_ready=False sector_rank=14 price=13.54 support=11.6 resistance=14.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=65.11 liquidity=6726969.86 spike=0.83
- ADCI.CA: score=14.07 buy_ready=False sector_rank=12 price=262.98 support=221.0 resistance=280.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=65.82 liquidity=4544294.59 spike=1.69
- ADIB.CA: score=20.4 buy_ready=False sector_rank=9 price=48.76 support=43.16 resistance=50.49 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=63.58 liquidity=47255898.65 spike=0.6
- ADPC.CA: score=17.55 buy_ready=False sector_rank=12 price=2.97 support=2.53 resistance=3.25 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=61.61 liquidity=10344925.9 spike=1.2
- AFDI.CA: score=16.12 buy_ready=False sector_rank=12 price=44.81 support=34.8 resistance=48.5 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=74.89 liquidity=5927198.12 spike=2.02
- AFMC.CA: score=23.15 buy_ready=False sector_rank=12 price=148.64 support=94.6 resistance=166.95 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=84.66 liquidity=122669321.42 spike=4.32
- AJWA.CA: score=15.87 buy_ready=False sector_rank=12 price=262.81 support=190.2 resistance=274.44 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=83.86 liquidity=7720306.49 spike=0.24
- ALCN.CA: score=23.46 buy_ready=False sector_rank=6 price=32.96 support=27.11 resistance=33.89 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=62.66 liquidity=12393816.62 spike=1.03
- ALUM.CA: score=8.32 buy_ready=False sector_rank=12 price=20.64 support=16.02 resistance=21.8 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=77.35 liquidity=3710948.05 spike=1.23
- AMER.CA: score=15.96 buy_ready=False sector_rank=15 price=4.24 support=3.21 resistance=4.74 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.0 liquidity=60495070.17 spike=0.9
- AMES.CA: score=19.05 buy_ready=False sector_rank=12 price=50.1 support=28.0 resistance=54.49 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=85.38 liquidity=342199773.08 spike=1.95
- AMIA.CA: score=16.15 buy_ready=False sector_rank=12 price=17.12 support=14.0 resistance=18.77 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=57.24 liquidity=12514172.77 spike=0.94
- AMOC.CA: score=18.4 buy_ready=False sector_rank=10 price=13.36 support=12.55 resistance=15.15 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=58.74 liquidity=121044335.69 spike=0.82
- APSW.CA: score=9.5 buy_ready=False sector_rank=12 price=7.72 support=7.1 resistance=8.1 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=64.85 liquidity=355946.03 spike=0.76
- ARAB.CA: score=17.96 buy_ready=False sector_rank=15 price=0.25 support=0.2 resistance=0.27 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.12 liquidity=68253441.07 spike=0.82
- ARCC.CA: score=23.2 buy_ready=False sector_rank=1 price=69.82 support=58.01 resistance=74.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=81.9 liquidity=74136272.08 spike=1.9
- AREH.CA: score=11.85 buy_ready=False sector_rank=12 price=1.08 support=0.91 resistance=1.17 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=6704876.79 spike=0.89
- ASCM.CA: score=10.96 buy_ready=False sector_rank=12 price=47.67 support=38.2 resistance=50.4 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.81 liquidity=3815411.31 spike=0.54
- ASPI.CA: score=17.15 buy_ready=False sector_rank=12 price=0.32 support=0.27 resistance=0.36 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=65.41 liquidity=20742624.71 spike=0.89
- ATLC.CA: score=17.88 buy_ready=False sector_rank=13 price=5.7 support=3.93 resistance=6.06 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=80.09 liquidity=14681803.01 spike=1.37
- ATQA.CA: score=18.48 buy_ready=False sector_rank=17 price=10.33 support=8.25 resistance=11.08 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=75.0 liquidity=65157063.33 spike=1.41
- AXPH.CA: score=12.88 buy_ready=False sector_rank=12 price=1453.39 support=1135.0 resistance=1497.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=77.74 liquidity=7027140.72 spike=1.35
- BINV.CA: score=10.67 buy_ready=False sector_rank=19 price=51.99 support=50.62 resistance=62.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=44.59 liquidity=4433187.44 spike=0.42
- BIOC.CA: score=18.81 buy_ready=False sector_rank=12 price=390.2 support=212.05 resistance=447.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=75.93 liquidity=237229121.02 spike=1.33
- BTFH.CA: score=15.14 buy_ready=False sector_rank=13 price=2.4 support=2.05 resistance=2.74 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=67.69 liquidity=111851963.64 spike=0.91
- CAED.CA: score=18.15 buy_ready=False sector_rank=12 price=100.23 support=64.0 resistance=116.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.72 liquidity=23702691.88 spike=0.9
- CANA.CA: score=15.4 buy_ready=False sector_rank=9 price=32.49 support=29.33 resistance=48.49 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=36.3 liquidity=19679323.98 spike=0.86
- CCAP.CA: score=18.23 buy_ready=False sector_rank=19 price=6.18 support=5.55 resistance=6.45 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=58.86 liquidity=327088671.69 spike=0.82
- CCRS.CA: score=17.23 buy_ready=False sector_rank=12 price=2.0 support=1.3 resistance=2.49 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=71.31 liquidity=18796898.0 spike=1.04
- CEFM.CA: score=24.12 buy_ready=False sector_rank=12 price=128.39 support=97.79 resistance=138.99 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=76.28 liquidity=9547337.13 spike=3.21
- CERA.CA: score=17.15 buy_ready=False sector_rank=12 price=1.09 support=0.93 resistance=1.29 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=63.16 liquidity=41513440.43 spike=0.58
- CFGH.CA: score=6.29 buy_ready=False sector_rank=12 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=88.89 liquidity=4365.04 spike=1.07
- CICH.CA: score=18.22 buy_ready=False sector_rank=13 price=10.78 support=9.85 resistance=11.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=60.85 liquidity=5854078.85 spike=2.61
- CIEB.CA: score=14.2 buy_ready=False sector_rank=9 price=23.41 support=21.35 resistance=23.9 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=72.36 liquidity=3804359.08 spike=0.43
- CIRA.CA: score=24.73 buy_ready=False sector_rank=16 price=39.5 support=32.01 resistance=40.11 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=86.09 liquidity=79007070.5 spike=4.71
- CLHO.CA: score=19.4 buy_ready=False sector_rank=11 price=14.09 support=12.51 resistance=15.15 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=63.4 liquidity=14927115.24 spike=0.4
- CNFN.CA: score=11.8 buy_ready=False sector_rank=13 price=4.08 support=3.25 resistance=4.32 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=67.3 liquidity=4660726.71 spike=0.57
- COMI.CA: score=20.4 buy_ready=False sector_rank=9 price=128.82 support=117.41 resistance=131.36 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=67.21 liquidity=443762124.09 spike=0.9
- COPR.CA: score=17.29 buy_ready=False sector_rank=12 price=0.4 support=0.33 resistance=0.45 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=57.42 liquidity=9145093.18 spike=0.48
- COSG.CA: score=13.61 buy_ready=False sector_rank=12 price=1.35 support=1.11 resistance=1.45 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=6463851.41 spike=0.74
- CPCI.CA: score=11.44 buy_ready=False sector_rank=12 price=592.42 support=502.25 resistance=620.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=51.63 liquidity=2295627.43 spike=0.47
- CSAG.CA: score=17.12 buy_ready=False sector_rank=6 price=36.0 support=30.1 resistance=37.36 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=83.42 liquidity=9099000.0 spike=1.31
- DAPH.CA: score=17.93 buy_ready=False sector_rank=12 price=90.49 support=65.2 resistance=98.1 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=87.42 liquidity=57194474.62 spike=2.39
- DEIN.CA: score=9.15 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=16.7 buy_ready=False sector_rank=5 price=25.02 support=20.27 resistance=26.5 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=88.79 liquidity=6303764.1 spike=2.5
- DSCW.CA: score=18.53 buy_ready=False sector_rank=12 price=1.58 support=1.23 resistance=1.66 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=68.42 liquidity=25892569.86 spike=1.69
- DTPP.CA: score=14.77 buy_ready=False sector_rank=12 price=62.69 support=36.0 resistance=69.99 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=84.79 liquidity=68062719.58 spike=1.31
- EALR.CA: score=14.74 buy_ready=False sector_rank=12 price=296.18 support=236.01 resistance=337.99 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=68.07 liquidity=7593462.65 spike=0.95
- EASB.CA: score=11.5 buy_ready=False sector_rank=12 price=6.19 support=5.03 resistance=7.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=63.18 liquidity=3350950.34 spike=0.47
- EAST.CA: score=20.4 buy_ready=False sector_rank=5 price=34.8 support=27.02 resistance=35.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.26 liquidity=44002371.84 spike=0.82
- EBSC.CA: score=10.01 buy_ready=False sector_rank=12 price=1.6 support=1.2 resistance=1.7 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=72.6 liquidity=2863648.04 spike=0.68
- ECAP.CA: score=13.04 buy_ready=False sector_rank=12 price=28.89 support=24.8 resistance=30.4 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.29 liquidity=4753358.27 spike=1.57
- EDFM.CA: score=9.79 buy_ready=False sector_rank=12 price=365.86 support=326.73 resistance=378.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=82.53 liquidity=2543824.48 spike=2.05
- EEII.CA: score=17.15 buy_ready=False sector_rank=12 price=2.03 support=1.42 resistance=2.29 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=74.74 liquidity=13541817.19 spike=1.0
- EFIC.CA: score=13.66 buy_ready=False sector_rank=17 price=164.13 support=121.0 resistance=174.88 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=75.56 liquidity=20110357.11 spike=0.71
- EFID.CA: score=20.98 buy_ready=False sector_rank=5 price=20.66 support=16.01 resistance=21.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=75.7 liquidity=118207841.93 spike=3.29
- EFIH.CA: score=18.4 buy_ready=False sector_rank=7 price=24.9 support=20.3 resistance=25.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=94.48 liquidity=31241407.02 spike=0.55
- EGAS.CA: score=12.2 buy_ready=False sector_rank=10 price=49.97 support=43.0 resistance=61.68 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.42 liquidity=3801667.72 spike=0.84
- EGBE.CA: score=12.97 buy_ready=False sector_rank=9 price=0.5 support=0.47 resistance=0.51 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=62.86 liquidity=147661.68 spike=3.21
- EGCH.CA: score=18.94 buy_ready=False sector_rank=17 price=10.8 support=9.66 resistance=11.94 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=58.19 liquidity=55176250.57 spike=1.14
- EGSA.CA: score=13.4 buy_ready=False sector_rank=2 price=9.0 support=8.7 resistance=9.07 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=74.36 liquidity=0.0 spike=0.0
- EGTS.CA: score=16.96 buy_ready=False sector_rank=15 price=13.4 support=10.19 resistance=14.45 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.26 liquidity=18199839.28 spike=0.83
- EHDR.CA: score=12.82 buy_ready=False sector_rank=12 price=2.16 support=1.8 resistance=2.32 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.74 liquidity=5672825.51 spike=0.59
- ELEC.CA: score=15.4 buy_ready=False sector_rank=3 price=1.74 support=1.34 resistance=1.96 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=79.31 liquidity=36509905.16 spike=0.7
- ELKA.CA: score=18.41 buy_ready=False sector_rank=12 price=1.52 support=1.21 resistance=1.63 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=67.27 liquidity=13045431.76 spike=1.13
- ELNA.CA: score=11.63 buy_ready=False sector_rank=12 price=41.28 support=33.46 resistance=44.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.64 liquidity=481242.23 spike=0.63
- ELSH.CA: score=14.4 buy_ready=False sector_rank=12 price=11.19 support=8.57 resistance=11.8 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=75.91 liquidity=9254733.91 spike=0.58
- ELWA.CA: score=0.95 buy_ready=False sector_rank=12 price=1.22 support=1.21 resistance=1.59 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=15.87 liquidity=801998.74 spike=0.64
- EMFD.CA: score=21.96 buy_ready=False sector_rank=15 price=12.8 support=10.6 resistance=12.85 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=89.63 liquidity=249580906.12 spike=3.61
- ENGC.CA: score=25.45 buy_ready=False sector_rank=12 price=40.01 support=26.91 resistance=43.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=74.37 liquidity=60139988.72 spike=3.15
- EOSB.CA: score=11.19 buy_ready=False sector_rank=12 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=44904.51 spike=0.45
- EPCO.CA: score=15.24 buy_ready=False sector_rank=12 price=8.71 support=7.0 resistance=9.98 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=72.46 liquidity=7694414.03 spike=1.2
- EPPK.CA: score=9.15 buy_ready=False sector_rank=12 price=9.78 support=9.78 resistance=9.78 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ETEL.CA: score=25.94 buy_ready=False sector_rank=2 price=143.0 support=115.0 resistance=144.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=77.55 liquidity=762416655.0 spike=2.77
- ETRS.CA: score=21.15 buy_ready=False sector_rank=12 price=10.95 support=9.51 resistance=11.3 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.2 liquidity=11215964.35 spike=0.72
- EXPA.CA: score=17.4 buy_ready=False sector_rank=9 price=14.64 support=12.0 resistance=15.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.49 liquidity=10030318.08 spike=0.46
- FAIT.CA: score=13.03 buy_ready=False sector_rank=9 price=46.43 support=40.0 resistance=47.46 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=73.21 liquidity=1628114.39 spike=0.63
- FAITA.CA: score=15.4 buy_ready=False sector_rank=9 price=1.0 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=57.58 liquidity=3882.88 spike=0.15
- FERC.CA: score=10.72 buy_ready=False sector_rank=17 price=66.12 support=52.63 resistance=72.69 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=66.73 liquidity=4060627.73 spike=0.51
- FWRY.CA: score=20.78 buy_ready=False sector_rank=7 price=17.44 support=15.27 resistance=18.65 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=55.54 liquidity=198917123.21 spike=1.69
- GBCO.CA: score=14.6 buy_ready=False sector_rank=21 price=22.93 support=20.9 resistance=30.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=49.5 liquidity=90656737.11 spike=0.77
- GDWA.CA: score=16.94 buy_ready=False sector_rank=12 price=0.56 support=0.46 resistance=0.6 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.21 liquidity=9793699.95 spike=0.82
- GGCC.CA: score=17.67 buy_ready=False sector_rank=12 price=0.56 support=0.49 resistance=0.65 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=64.97 liquidity=25563279.51 spike=1.26
- GIHD.CA: score=15.15 buy_ready=False sector_rank=12 price=51.53 support=32.1 resistance=57.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=76.5 liquidity=13470817.69 spike=0.78
- GMCI.CA: score=12.34 buy_ready=False sector_rank=12 price=1.76 support=1.34 resistance=1.75 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=196116.8 spike=0.51
- GRCA.CA: score=16.31 buy_ready=False sector_rank=12 price=33.02 support=22.57 resistance=37.32 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=73.46 liquidity=9165031.33 spike=0.78
- GSSC.CA: score=23.15 buy_ready=False sector_rank=12 price=264.14 support=211.52 resistance=296.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=73.14 liquidity=18155135.63 spike=7.96
- HDBK.CA: score=21.7 buy_ready=False sector_rank=9 price=108.61 support=83.01 resistance=111.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=73.59 liquidity=50402860.2 spike=1.65
- HELI.CA: score=17.96 buy_ready=False sector_rank=15 price=6.9 support=5.72 resistance=7.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=65.91 liquidity=35525029.99 spike=0.46
- HRHO.CA: score=19.14 buy_ready=False sector_rank=13 price=24.1 support=21.87 resistance=26.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=51.29 liquidity=48782088.07 spike=0.95
- ICID.CA: score=10.19 buy_ready=False sector_rank=12 price=17.0 support=14.26 resistance=17.98 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=59.37 liquidity=2044947.0 spike=0.48
- IDRE.CA: score=12.15 buy_ready=False sector_rank=12 price=43.65 support=29.11 resistance=47.25 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=84.42 liquidity=7006479.99 spike=0.89
- IFAP.CA: score=17.32 buy_ready=False sector_rank=18 price=16.5 support=15.12 resistance=19.4 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=51.05 liquidity=10309909.5 spike=1.53
- INFI.CA: score=20.49 buy_ready=False sector_rank=12 price=147.3 support=93.44 resistance=155.79 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=89.44 liquidity=67575496.7 spike=2.17
- IRON.CA: score=17.37 buy_ready=False sector_rank=17 price=25.63 support=23.13 resistance=27.61 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=62.39 liquidity=8670577.46 spike=1.02
- ISMA.CA: score=14.19 buy_ready=False sector_rank=12 price=21.44 support=14.11 resistance=23.44 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=79.93 liquidity=12451923.51 spike=1.02
- ISPH.CA: score=20.64 buy_ready=False sector_rank=11 price=10.53 support=9.02 resistance=10.94 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=62.68 liquidity=109313401.43 spike=1.62
- JUFO.CA: score=20.86 buy_ready=False sector_rank=5 price=23.9 support=21.01 resistance=25.51 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=64.7 liquidity=47373981.74 spike=1.73
- KABO.CA: score=16.99 buy_ready=False sector_rank=14 price=6.99 support=5.58 resistance=7.99 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=56.81 liquidity=10606325.08 spike=0.52
- KWIN.CA: score=14.83 buy_ready=False sector_rank=12 price=71.24 support=44.02 resistance=85.83 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=72.17 liquidity=7685228.49 spike=0.61
- KZPC.CA: score=18.65 buy_ready=False sector_rank=12 price=12.64 support=11.56 resistance=14.77 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=56.21 liquidity=12981457.31 spike=1.25
- LCSW.CA: score=21.4 buy_ready=False sector_rank=1 price=40.44 support=28.0 resistance=42.14 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=80.57 liquidity=15385114.4 spike=0.66
- LUTS.CA: score=15.89 buy_ready=False sector_rank=12 price=0.76 support=0.47 resistance=0.84 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=79.56 liquidity=94386355.82 spike=1.37
- MAAL.CA: score=23.15 buy_ready=False sector_rank=12 price=6.8 support=4.88 resistance=8.25 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.48 liquidity=87688722.46 spike=3.66
- MASR.CA: score=20.15 buy_ready=False sector_rank=12 price=6.79 support=5.6 resistance=8.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=62.06 liquidity=22059562.37 spike=0.58
- MBSC.CA: score=27.38 buy_ready=False sector_rank=1 price=363.5 support=262.0 resistance=397.9 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=86.21 liquidity=201455698.5 spike=2.99
- MCQE.CA: score=23.94 buy_ready=False sector_rank=1 price=187.12 support=144.0 resistance=205.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=81.63 liquidity=153861474.31 spike=2.77
- MCRO.CA: score=18.99 buy_ready=False sector_rank=12 price=1.39 support=1.07 resistance=1.48 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=73.08 liquidity=72966461.87 spike=1.42
- MENA.CA: score=27.96 buy_ready=False sector_rank=15 price=6.54 support=5.45 resistance=7.9 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=74.73 liquidity=43479011.93 spike=7.13
- MEPA.CA: score=17.15 buy_ready=False sector_rank=12 price=1.38 support=1.14 resistance=1.6 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=68.09 liquidity=11119728.08 spike=0.61
- MFPC.CA: score=9.9 buy_ready=False sector_rank=17 price=39.03 support=37.23 resistance=47.96 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=30.51 liquidity=99295205.11 spike=1.12
- MFSC.CA: score=8.49 buy_ready=False sector_rank=12 price=35.03 support=28.55 resistance=42.4 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=64.95 liquidity=1344801.65 spike=0.58
- MHOT.CA: score=15.66 buy_ready=False sector_rank=4 price=16.35 support=13.0 resistance=17.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=72.51 liquidity=5257963.92 spike=0.87
- MICH.CA: score=19.89 buy_ready=False sector_rank=12 price=46.22 support=35.5 resistance=48.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=86.39 liquidity=14251844.94 spike=1.87
- MILS.CA: score=19.69 buy_ready=False sector_rank=12 price=149.13 support=94.24 resistance=163.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=81.89 liquidity=36661374.75 spike=3.27
- MIPH.CA: score=10.06 buy_ready=False sector_rank=11 price=760.14 support=610.0 resistance=819.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=55.17 liquidity=1662426.21 spike=0.82
- MOED.CA: score=16.79 buy_ready=False sector_rank=12 price=0.5 support=0.39 resistance=0.57 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=73.63 liquidity=9640758.09 spike=0.65
- MOIL.CA: score=15.62 buy_ready=False sector_rank=10 price=0.7 support=0.6 resistance=0.71 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.33 liquidity=442110.32 spike=1.89
- MOIN.CA: score=16.37 buy_ready=False sector_rank=12 price=31.52 support=25.7 resistance=35.5 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=68.74 liquidity=8226972.28 spike=0.84
- MOSC.CA: score=11.46 buy_ready=False sector_rank=12 price=265.68 support=198.01 resistance=303.1 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=71.42 liquidity=3313029.51 spike=0.58
- MPCI.CA: score=18.81 buy_ready=False sector_rank=12 price=350.0 support=238.6 resistance=382.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=75.25 liquidity=162367450.0 spike=1.33
- MPCO.CA: score=19.5 buy_ready=False sector_rank=18 price=2.01 support=1.55 resistance=2.58 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=63.48 liquidity=121152154.47 spike=1.12
- MPRC.CA: score=18.15 buy_ready=False sector_rank=12 price=38.67 support=27.0 resistance=40.7 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=78.27 liquidity=13021696.51 spike=0.62
- MTIE.CA: score=17.14 buy_ready=False sector_rank=21 price=6.88 support=6.05 resistance=7.85 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=53.66 liquidity=53130587.6 spike=2.27
- NAHO.CA: score=8.16 buy_ready=False sector_rank=12 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=64.71 liquidity=11175.14 spike=0.75
- NCCW.CA: score=17.17 buy_ready=False sector_rank=12 price=5.87 support=4.05 resistance=6.34 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=76.41 liquidity=39898406.83 spike=2.01
- NEDA.CA: score=2.53 buy_ready=False sector_rank=12 price=2.46 support=2.26 resistance=2.6 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=29.41 liquidity=217392.66 spike=1.08
- NHPS.CA: score=16.3 buy_ready=False sector_rank=12 price=61.9 support=50.0 resistance=69.97 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=73.37 liquidity=8972033.82 spike=1.09
- NINH.CA: score=17.15 buy_ready=False sector_rank=12 price=16.09 support=12.36 resistance=18.5 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.8 liquidity=11213282.01 spike=0.98
- NIPH.CA: score=20.46 buy_ready=False sector_rank=11 price=325.0 support=205.0 resistance=365.5 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=81.15 liquidity=345068425.0 spike=2.03
- OBRI.CA: score=14.75 buy_ready=False sector_rank=12 price=24.22 support=18.11 resistance=26.75 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=72.48 liquidity=7606872.06 spike=0.87
- OCDI.CA: score=13.89 buy_ready=False sector_rank=15 price=25.85 support=21.0 resistance=26.8 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=71.81 liquidity=5930636.34 spike=0.18
- OCPH.CA: score=15.89 buy_ready=False sector_rank=12 price=205.12 support=147.96 resistance=224.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=81.54 liquidity=10450453.51 spike=1.87
- ODIN.CA: score=12.53 buy_ready=False sector_rank=12 price=2.12 support=1.7 resistance=2.33 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.88 liquidity=5379635.39 spike=0.64
- OFH.CA: score=18.93 buy_ready=False sector_rank=12 price=0.74 support=0.61 resistance=0.81 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.14 liquidity=31118109.66 spike=1.39
- OIH.CA: score=16.77 buy_ready=False sector_rank=19 price=1.7 support=1.5 resistance=1.84 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=64.52 liquidity=58420209.24 spike=1.27
- OLFI.CA: score=12.93 buy_ready=False sector_rank=5 price=20.52 support=17.86 resistance=21.24 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=66.24 liquidity=5531945.88 spike=0.56
- ORAS.CA: score=5.0 buy_ready=False sector_rank=20 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=16.96 buy_ready=False sector_rank=15 price=10.47 support=8.5 resistance=10.71 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=71.96 liquidity=95642405.44 spike=0.87
- ORWE.CA: score=17.99 buy_ready=False sector_rank=14 price=25.94 support=22.2 resistance=26.87 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=68.04 liquidity=15674919.76 spike=0.61
- PHAR.CA: score=19.38 buy_ready=False sector_rank=11 price=106.0 support=90.2 resistance=113.97 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=65.82 liquidity=107348108.0 spike=1.49
- PHDC.CA: score=16.96 buy_ready=False sector_rank=15 price=11.85 support=10.33 resistance=13.3 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=54.26 liquidity=63801456.7 spike=0.49
- PHTV.CA: score=8.5 buy_ready=False sector_rank=12 price=330.15 support=300.0 resistance=349.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=75.83 liquidity=2308078.61 spike=1.52
- POUL.CA: score=19.48 buy_ready=False sector_rank=5 price=8.02 support=8.01 resistance=10.81 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=37.41 liquidity=256971737.91 spike=2.04
- PRCL.CA: score=20.68 buy_ready=False sector_rank=1 price=19.26 support=16.65 resistance=23.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=54.97 liquidity=30296692.98 spike=1.14
- PRDC.CA: score=19.96 buy_ready=False sector_rank=15 price=6.5 support=5.08 resistance=7.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=62.7 liquidity=12616617.0 spike=0.63
- PRMH.CA: score=11.04 buy_ready=False sector_rank=12 price=2.16 support=1.7 resistance=2.66 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.44 liquidity=3895348.47 spike=0.57
- RACC.CA: score=7.62 buy_ready=False sector_rank=12 price=8.13 support=6.1 resistance=8.7 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=82.45 liquidity=3474323.03 spike=0.51
- RAKT.CA: score=12.24 buy_ready=False sector_rank=12 price=22.47 support=20.4 resistance=23.16 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=39.43 liquidity=93138.15 spike=0.36
- RAYA.CA: score=19.72 buy_ready=False sector_rank=8 price=5.85 support=5.02 resistance=6.33 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=61.75 liquidity=29626476.27 spike=1.16
- RMDA.CA: score=18.4 buy_ready=False sector_rank=11 price=5.41 support=4.5 resistance=5.72 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=67.84 liquidity=20885829.18 spike=0.66
- ROTO.CA: score=12.33 buy_ready=False sector_rank=12 price=33.84 support=25.0 resistance=36.8 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=67.26 liquidity=5186859.86 spike=0.5
- RREI.CA: score=15.27 buy_ready=False sector_rank=12 price=2.78 support=1.96 resistance=3.4 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.47 liquidity=13088092.53 spike=1.06
- RTVC.CA: score=9.15 buy_ready=False sector_rank=12 price=3.11 support=2.66 resistance=3.4 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=62.5 liquidity=0.0 spike=0.0
- RUBX.CA: score=16.15 buy_ready=False sector_rank=12 price=13.9 support=10.51 resistance=18.49 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=67.78 liquidity=43833648.8 spike=0.66
- SAUD.CA: score=22.9 buy_ready=False sector_rank=9 price=22.6 support=19.3 resistance=23.35 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=76.22 liquidity=41199823.3 spike=2.25
- SCEM.CA: score=25.88 buy_ready=False sector_rank=1 price=100.51 support=73.9 resistance=106.55 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=95.49 liquidity=102583724.5 spike=2.24
- SCFM.CA: score=19.15 buy_ready=False sector_rank=12 price=226.75 support=153.02 resistance=240.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=83.35 liquidity=17086746.25 spike=4.51
- SCTS.CA: score=7.96 buy_ready=False sector_rank=16 price=484.38 support=410.0 resistance=555.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=45.3 liquidity=1232747.11 spike=0.2
- SDTI.CA: score=21.15 buy_ready=False sector_rank=12 price=84.45 support=75.01 resistance=90.99 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=57.61 liquidity=13072099.48 spike=0.68
- SEIG.CA: score=14.62 buy_ready=False sector_rank=12 price=228.48 support=142.0 resistance=280.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=70.35 liquidity=3476094.65 spike=0.34
- SIPC.CA: score=18.15 buy_ready=False sector_rank=12 price=5.3 support=3.73 resistance=5.89 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=72.89 liquidity=46278520.47 spike=1.0
- SKPC.CA: score=18.68 buy_ready=False sector_rank=17 price=15.01 support=14.01 resistance=15.9 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=62.64 liquidity=39413798.96 spike=1.01
- SMFR.CA: score=13.43 buy_ready=False sector_rank=12 price=220.94 support=165.0 resistance=264.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=75.06 liquidity=5281349.82 spike=0.67
- SNFC.CA: score=21.15 buy_ready=False sector_rank=12 price=11.29 support=10.08 resistance=11.48 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=67.47 liquidity=10136139.39 spike=0.99
- SPIN.CA: score=11.87 buy_ready=False sector_rank=14 price=15.51 support=12.0 resistance=16.48 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=65.65 liquidity=3883300.8 spike=0.66
- SPMD.CA: score=17.1 buy_ready=False sector_rank=12 price=0.34 support=0.3 resistance=0.39 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=60.87 liquidity=9956429.48 spike=0.61
- SUGR.CA: score=18.4 buy_ready=False sector_rank=5 price=51.48 support=44.62 resistance=55.99 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=66.91 liquidity=14305416.71 spike=0.71
- SVCE.CA: score=21.59 buy_ready=False sector_rank=12 price=9.2 support=7.01 resistance=10.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=68.4 liquidity=153569212.02 spike=2.72
- SWDY.CA: score=19.88 buy_ready=False sector_rank=3 price=121.9 support=97.0 resistance=123.45 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=80.62 liquidity=71040639.09 spike=1.24
- TALM.CA: score=17.73 buy_ready=False sector_rank=16 price=20.1 support=17.0 resistance=21.5 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=67.16 liquidity=12570178.44 spike=0.65
- TMGH.CA: score=18.96 buy_ready=False sector_rank=15 price=83.88 support=76.5 resistance=93.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=56.78 liquidity=107167013.73 spike=0.41
- TRTO.CA: score=8.15 buy_ready=False sector_rank=12 price=0.06 support=0.05 resistance=0.06 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=62.5 liquidity=4278.0 spike=0.81
- UEFM.CA: score=8.81 buy_ready=False sector_rank=12 price=510.77 support=422.0 resistance=540.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=78.29 liquidity=662468.68 spike=0.36
- UEGC.CA: score=17.15 buy_ready=False sector_rank=12 price=1.51 support=1.21 resistance=1.6 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=68.63 liquidity=31997287.87 spike=0.99
- UNIP.CA: score=12.75 buy_ready=False sector_rank=12 price=0.31 support=0.25 resistance=0.33 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=74.49 liquidity=5605814.55 spike=0.78
- UNIT.CA: score=9.79 buy_ready=False sector_rank=15 price=16.96 support=15.06 resistance=19.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=57.82 liquidity=1829966.94 spike=0.91
- WCDF.CA: score=9.85 buy_ready=False sector_rank=12 price=546.81 support=432.5 resistance=565.0 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=91.07 liquidity=2685383.9 spike=2.01
- WKOL.CA: score=14.43 buy_ready=False sector_rank=12 price=176.26 support=145.33 resistance=309.43 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=69.37 liquidity=9279912.45 spike=0.74
- ZEOT.CA: score=16.91 buy_ready=False sector_rank=12 price=11.82 support=7.9 resistance=12.69 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=80.44 liquidity=8601886.58 spike=1.08
- ZMID.CA: score=18.4 buy_ready=False sector_rank=15 price=6.9 support=5.91 resistance=7.2 source=Yahoo Finance as_of=2026-11-15T22:00:00+00:00 freshness=FRESH RSI=68.03 liquidity=94820470.61 spike=1.22

## Backtesting Lite
- MENA.CA: 180d return=45.01%, max drawdown=-26.35%, MA20>MA50 days last20=0, as_of=2026-11-15T22:00:00+00:00
- MBSC.CA: 180d return=35.83%, max drawdown=-39.52%, MA20>MA50 days last20=0, as_of=2026-11-15T22:00:00+00:00
- ETEL.CA: 180d return=48.7%, max drawdown=-22.52%, MA20>MA50 days last20=15, as_of=2026-11-15T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MENA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Mena Touristic and Real Estate Investment summary=Evidence rejected for MENA.CA: source text did not clearly match MENA.CA / Mena Touristic and Real Estate Investment.
- MBSC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Beni Suef Cement summary=Evidence rejected for MBSC.CA: source text did not clearly match MBSC.CA / Misr Beni Suef Cement.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- SCEM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sinai Cement summary=Evidence rejected for SCEM.CA: source text did not clearly match SCEM.CA / Sinai Cement.
- ENGC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Industrial Engineering Company for Construction and Development (ICON) (S.A.E) summary=Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- CIRA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Cairo Investment and Real Estate Development summary=Evidence rejected for CIRA.CA: source text did not clearly match CIRA.CA / Cairo Investment and Real Estate Development.
- CEFM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Middle Egypt Flour Mills summary=Evidence rejected for CEFM.CA: source text did not clearly match CEFM.CA / Middle Egypt Flour Mills.
- MCQE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Cement Qena summary=Evidence rejected for MCQE.CA: source text did not clearly match MCQE.CA / Misr Cement Qena.

## Warnings
- OpenRouter API error: 404
- Mubasher stock page returned no evidence titles for MENA.CA.
- No Yahoo or Mubasher evidence found for MENA.CA.
- Evidence rejected for MENA.CA: source text did not clearly match MENA.CA / Mena Touristic and Real Estate Investment.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock page returned no evidence titles for MBSC.CA.
- No Yahoo or Mubasher evidence found for MBSC.CA.
- Evidence rejected for MBSC.CA: source text did not clearly match MBSC.CA / Misr Beni Suef Cement.
- Mubasher stock page returned no evidence titles for ETEL.CA.
- No Yahoo or Mubasher evidence found for ETEL.CA.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Mubasher stock page returned no evidence titles for SCEM.CA.
- No Yahoo or Mubasher evidence found for SCEM.CA.
- Evidence rejected for SCEM.CA: source text did not clearly match SCEM.CA / Sinai Cement.
- Mubasher stock page returned no evidence titles for ENGC.CA.
- No Yahoo or Mubasher evidence found for ENGC.CA.
- Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- Mubasher stock page returned no evidence titles for CIRA.CA.
- No Yahoo or Mubasher evidence found for CIRA.CA.
- Evidence rejected for CIRA.CA: source text did not clearly match CIRA.CA / Cairo Investment and Real Estate Development.
- Mubasher stock page returned no evidence titles for CEFM.CA.
- No Yahoo or Mubasher evidence found for CEFM.CA.
- Evidence rejected for CEFM.CA: source text did not clearly match CEFM.CA / Middle Egypt Flour Mills.
- Mubasher stock page returned no evidence titles for MCQE.CA.
- No Yahoo or Mubasher evidence found for MCQE.CA.
- Evidence rejected for MCQE.CA: source text did not clearly match MCQE.CA / Misr Cement Qena.
