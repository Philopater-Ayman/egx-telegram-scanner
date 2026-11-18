# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-11-18T15:35:00.333249+00:00
Generated Cairo: 2026-11-18 17:35
Run timing: target 09:15 Cairo | generated Cairo 2026-11-18 17:35 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-11-18 17:32

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 186/186
- Top sector: Telecommunications

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 65.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 65.0% / above MA50 15.0%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=634407947.8 spike=1.28 score=22.95
- ETEL.CA: liquidity=543879557.37 spike=1.85 score=26.1
- CCAP.CA: liquidity=513039487.5 spike=1.31 score=18.71
- AMES.CA: liquidity=453789331.93 spike=2.32 score=18.8
- NIPH.CA: liquidity=251136745.0 spike=1.53 score=21.75

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- INFI.CA: spike=4.43 liquidity=168426362.5 outlook=CONSTRUCTIVE score=54.9 buy_ready=False
- SAUD.CA: spike=3.95 liquidity=86693496.42 outlook=CONSTRUCTIVE score=62.98 buy_ready=False
- PRMH.CA: spike=3.23 liquidity=25813309.19 outlook=BULLISH_WATCH score=72.9 buy_ready=False
- MPRC.CA: spike=2.52 liquidity=57092986.75 outlook=BULLISH_WATCH score=72.9 buy_ready=False
- ATLC.CA: spike=2.5 liquidity=29373391.06 outlook=CONSTRUCTIVE score=50.08 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=8.96 5d=3.02% 20d=1.8% aboveMA50=100.0%
- #2 Tourism & Leisure: score=8.39 5d=1.25% 20d=3.59% aboveMA50=100.0%
- #3 Building Materials: score=7.65 5d=0.95% 20d=8.38% aboveMA50=50.0%
- #4 Energy & Petrochemicals: score=6.68 5d=2.12% 20d=2.24% aboveMA50=33.33%
- #5 Industrial Goods & Cables: score=6.44 5d=-1.7% 20d=6.05% aboveMA50=50.0%
- #6 Banking & Financials: score=5.98 5d=0.45% 20d=4.14% aboveMA50=50.0%
- #7 Education: score=5.79 5d=-2.86% 20d=1.64% aboveMA50=66.67%
- #8 Transportation & Logistics: score=5.28 5d=0.39% 20d=4.29% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- TALM.CA: BULLISH_WATCH score=80.79 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- MBSC.CA: BULLISH_WATCH score=78.65 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- MIPH.CA: BULLISH_WATCH score=76.22 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- COMI.CA: BULLISH_WATCH score=75.98 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ETEL.CA: BULLISH_WATCH score=73.96 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- PRMH.CA: BULLISH_WATCH score=72.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- MPRC.CA: BULLISH_WATCH score=72.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- MHOT.CA: BULLISH_WATCH score=71.39 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- SDTI.CA: CONSTRUCTIVE score=67.9 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- AMOC.CA: CONSTRUCTIVE score=65.68 liquidity=TRADEABLE sector=IMPROVING risk=below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CPCI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=13.98 buy_ready=False sector_rank=14 price=236.08 support=171.02 resistance=269.99 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=63.88 liquidity=4821697.96 spike=0.24
- ABUK.CA: score=8.6 buy_ready=False sector_rank=17 price=77.05 support=73.6 resistance=95.75 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=24.96 liquidity=93481686.7 spike=0.68
- ACAMD.CA: score=17.78 buy_ready=False sector_rank=14 price=1.92 support=1.86 resistance=2.16 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=45.28 liquidity=112900413.48 spike=1.81
- ACGC.CA: score=18.25 buy_ready=False sector_rank=15 price=13.6 support=11.6 resistance=14.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=58.47 liquidity=8926360.25 spike=1.08
- ADCI.CA: score=10.47 buy_ready=False sector_rank=14 price=261.53 support=221.0 resistance=280.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=53.23 liquidity=1310265.29 spike=0.5
- ADIB.CA: score=18.39 buy_ready=False sector_rank=6 price=47.41 support=43.16 resistance=50.49 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=53.03 liquidity=47952559.89 spike=0.62
- ADPC.CA: score=15.92 buy_ready=False sector_rank=14 price=2.9 support=2.53 resistance=3.25 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=52.38 liquidity=9537041.81 spike=1.11
- AFDI.CA: score=8.28 buy_ready=False sector_rank=14 price=43.83 support=34.8 resistance=48.5 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.59 liquidity=1121083.79 spike=0.4
- AFMC.CA: score=14.32 buy_ready=False sector_rank=14 price=143.01 support=94.6 resistance=166.95 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=75.35 liquidity=31329914.55 spike=1.08
- AJWA.CA: score=17.16 buy_ready=False sector_rank=14 price=258.56 support=190.2 resistance=274.44 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=77.67 liquidity=16524310.88 spike=0.53
- ALCN.CA: score=15.71 buy_ready=False sector_rank=8 price=32.41 support=27.11 resistance=33.89 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=55.92 liquidity=5593058.49 spike=0.49
- ALUM.CA: score=11.58 buy_ready=False sector_rank=14 price=19.84 support=16.02 resistance=21.8 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=62.52 liquidity=3244633.62 spike=1.09
- AMER.CA: score=17.26 buy_ready=False sector_rank=13 price=4.14 support=3.21 resistance=4.74 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=52.32 liquidity=53996200.8 spike=0.8
- AMES.CA: score=18.8 buy_ready=False sector_rank=14 price=43.99 support=28.0 resistance=54.49 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=67.78 liquidity=453789331.93 spike=2.32
- AMIA.CA: score=15.16 buy_ready=False sector_rank=14 price=16.91 support=14.0 resistance=18.77 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=48.46 liquidity=11769782.64 spike=0.91
- AMOC.CA: score=19.2 buy_ready=False sector_rank=4 price=13.5 support=12.6 resistance=15.15 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=56.76 liquidity=212701504.5 spike=1.4
- APSW.CA: score=8.33 buy_ready=False sector_rank=14 price=7.72 support=7.1 resistance=8.07 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=64.85 liquidity=173522.44 spike=0.38
- ARAB.CA: score=17.26 buy_ready=False sector_rank=13 price=0.25 support=0.2 resistance=0.27 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=64033179.62 spike=0.78
- ARCC.CA: score=19.6 buy_ready=False sector_rank=3 price=68.04 support=58.01 resistance=74.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=65.42 liquidity=30037074.88 spike=1.1
- AREH.CA: score=11.76 buy_ready=False sector_rank=14 price=1.04 support=0.91 resistance=1.17 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=46.88 liquidity=5601823.55 spike=0.76
- ASCM.CA: score=14.89 buy_ready=False sector_rank=14 price=46.41 support=38.2 resistance=50.4 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.74 liquidity=6731306.38 spike=1.0
- ASPI.CA: score=18.16 buy_ready=False sector_rank=14 price=0.33 support=0.27 resistance=0.36 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.67 liquidity=19405975.16 spike=0.84
- ATLC.CA: score=21.83 buy_ready=False sector_rank=16 price=5.38 support=3.93 resistance=6.06 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=64.79 liquidity=29373391.06 spike=2.5
- ATQA.CA: score=18.6 buy_ready=False sector_rank=17 price=10.09 support=8.25 resistance=11.08 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.13 liquidity=40935120.53 spike=0.87
- AXPH.CA: score=16.62 buy_ready=False sector_rank=14 price=1479.7 support=1135.0 resistance=1497.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=74.29 liquidity=6099323.2 spike=1.18
- BINV.CA: score=15.43 buy_ready=False sector_rank=18 price=51.79 support=50.62 resistance=62.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=42.66 liquidity=17494299.78 spike=1.67
- BIOC.CA: score=20.16 buy_ready=False sector_rank=14 price=384.95 support=212.05 resistance=447.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=71.79 liquidity=141859853.75 spike=0.8
- BTFH.CA: score=15.83 buy_ready=False sector_rank=16 price=2.35 support=2.05 resistance=2.74 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=56.67 liquidity=53941427.81 spike=0.44
- CAED.CA: score=19.16 buy_ready=False sector_rank=14 price=97.76 support=64.0 resistance=116.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=63.57 liquidity=18600795.61 spike=0.7
- CANA.CA: score=10.39 buy_ready=False sector_rank=6 price=32.28 support=29.33 resistance=48.49 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=31.85 liquidity=13751699.12 spike=0.61
- CCAP.CA: score=18.71 buy_ready=False sector_rank=18 price=6.25 support=5.55 resistance=6.45 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=55.78 liquidity=513039487.5 spike=1.31
- CCRS.CA: score=16.16 buy_ready=False sector_rank=14 price=2.01 support=1.3 resistance=2.49 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.03 liquidity=13455364.05 spike=0.73
- CEFM.CA: score=8.61 buy_ready=False sector_rank=14 price=124.63 support=97.79 resistance=138.99 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=65.83 liquidity=1452936.51 spike=0.49
- CERA.CA: score=16.16 buy_ready=False sector_rank=14 price=1.04 support=0.93 resistance=1.29 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=48.65 liquidity=32355717.53 spike=0.48
- CFGH.CA: score=4.31 buy_ready=False sector_rank=14 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=80.0 liquidity=6591.63 spike=1.57
- CICH.CA: score=8.11 buy_ready=False sector_rank=16 price=10.37 support=9.91 resistance=11.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=42.92 liquidity=2274058.01 spike=0.99
- CIEB.CA: score=14.96 buy_ready=False sector_rank=6 price=23.25 support=21.35 resistance=23.9 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.71 liquidity=4570113.0 spike=0.55
- CIRA.CA: score=19.8 buy_ready=False sector_rank=7 price=38.98 support=32.01 resistance=40.11 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=78.62 liquidity=30783986.88 spike=1.74
- CLHO.CA: score=18.69 buy_ready=False sector_rank=11 price=13.87 support=12.51 resistance=15.15 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=50.96 liquidity=16054552.61 spike=0.44
- CNFN.CA: score=11.66 buy_ready=False sector_rank=16 price=3.98 support=3.25 resistance=4.32 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=55.71 liquidity=3829181.9 spike=0.49
- COMI.CA: score=22.95 buy_ready=False sector_rank=6 price=128.22 support=117.41 resistance=131.36 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.66 liquidity=634407947.8 spike=1.28
- COPR.CA: score=15.1 buy_ready=False sector_rank=14 price=0.38 support=0.33 resistance=0.45 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=43.38 liquidity=8944540.49 spike=0.47
- COSG.CA: score=14.26 buy_ready=False sector_rank=14 price=1.3 support=1.11 resistance=1.45 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=8098985.4 spike=0.98
- CSAG.CA: score=15.56 buy_ready=False sector_rank=8 price=36.07 support=30.1 resistance=37.36 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=80.25 liquidity=8047902.26 spike=1.2
- DAPH.CA: score=16.24 buy_ready=False sector_rank=14 price=86.0 support=65.2 resistance=98.1 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=67.77 liquidity=23331112.0 spike=1.04
- DEIN.CA: score=8.16 buy_ready=False sector_rank=14 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=7.88 buy_ready=False sector_rank=9 price=24.31 support=20.27 resistance=26.5 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=71.15 liquidity=896577.09 spike=0.36
- DSCW.CA: score=18.5 buy_ready=False sector_rank=14 price=1.53 support=1.23 resistance=1.66 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=51.06 liquidity=18111832.13 spike=1.17
- DTPP.CA: score=16.16 buy_ready=False sector_rank=14 price=59.24 support=36.0 resistance=69.99 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=74.52 liquidity=38337463.29 spike=0.73
- EALR.CA: score=10.23 buy_ready=False sector_rank=14 price=303.62 support=236.01 resistance=337.99 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=4066686.21 spike=0.5
- EASB.CA: score=10.05 buy_ready=False sector_rank=14 price=6.04 support=5.03 resistance=7.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=49.31 liquidity=2893510.3 spike=0.41
- EAST.CA: score=21.99 buy_ready=False sector_rank=9 price=34.09 support=28.14 resistance=35.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.36 liquidity=33013778.85 spike=0.61
- EBSC.CA: score=9.71 buy_ready=False sector_rank=14 price=1.53 support=1.2 resistance=1.7 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=56.45 liquidity=1549176.99 spike=0.39
- ECAP.CA: score=9.44 buy_ready=False sector_rank=14 price=28.33 support=24.8 resistance=30.4 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.67 liquidity=1281847.51 spike=0.42
- EDFM.CA: score=7.57 buy_ready=False sector_rank=14 price=362.76 support=326.73 resistance=378.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=73.05 liquidity=407742.25 spike=0.33
- EEII.CA: score=18.16 buy_ready=False sector_rank=14 price=1.92 support=1.42 resistance=2.29 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=64.29 liquidity=13336912.98 spike=0.95
- EFIC.CA: score=17.6 buy_ready=False sector_rank=17 price=158.7 support=121.0 resistance=174.88 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=63.66 liquidity=10438492.3 spike=0.38
- EFID.CA: score=19.41 buy_ready=False sector_rank=9 price=20.85 support=16.01 resistance=21.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=72.88 liquidity=43847884.4 spike=1.21
- EFIH.CA: score=17.38 buy_ready=False sector_rank=12 price=24.91 support=20.3 resistance=25.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=92.37 liquidity=29079759.45 spike=0.52
- EGAL.CA: score=16.6 buy_ready=False sector_rank=17 price=310.07 support=270.1 resistance=318.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=71.82 liquidity=84680429.07 spike=0.97
- EGAS.CA: score=11.64 buy_ready=False sector_rank=4 price=49.11 support=43.0 resistance=61.68 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=57.88 liquidity=2239612.47 spike=0.51
- EGBE.CA: score=10.62 buy_ready=False sector_rank=6 price=0.49 support=0.47 resistance=0.51 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=43.64 liquidity=104409.68 spike=2.06
- EGCH.CA: score=15.6 buy_ready=False sector_rank=17 price=10.51 support=9.66 resistance=11.94 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=46.34 liquidity=23587383.31 spike=0.51
- EGSA.CA: score=14.4 buy_ready=False sector_rank=1 price=9.0 support=8.7 resistance=9.03 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=74.36 liquidity=0.0 spike=0.0
- EGTS.CA: score=18.26 buy_ready=False sector_rank=13 price=12.95 support=10.19 resistance=14.45 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=57.51 liquidity=13442229.3 spike=0.63
- EHDR.CA: score=12.05 buy_ready=False sector_rank=14 price=2.11 support=1.8 resistance=2.32 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=59.42 liquidity=3889187.68 spike=0.42
- ELEC.CA: score=17.4 buy_ready=False sector_rank=5 price=1.68 support=1.34 resistance=1.96 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=65.38 liquidity=28295479.76 spike=0.54
- ELKA.CA: score=17.5 buy_ready=False sector_rank=14 price=1.46 support=1.21 resistance=1.63 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=13698930.7 spike=1.17
- ELNA.CA: score=10.45 buy_ready=False sector_rank=14 price=41.28 support=33.46 resistance=44.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.84 liquidity=291395.51 spike=0.38
- ELSH.CA: score=17.42 buy_ready=False sector_rank=14 price=10.97 support=8.57 resistance=11.8 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=66.83 liquidity=18287034.33 spike=1.13
- ELWA.CA: score=-0.29 buy_ready=False sector_rank=14 price=1.17 support=1.16 resistance=1.59 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=14.71 liquidity=553776.19 spike=0.43
- EMFD.CA: score=14.26 buy_ready=False sector_rank=13 price=12.79 support=10.6 resistance=12.96 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=88.08 liquidity=60591217.92 spike=0.86
- ENGC.CA: score=22.16 buy_ready=False sector_rank=14 price=38.1 support=26.91 resistance=43.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=64.79 liquidity=10878311.56 spike=0.57
- EOSB.CA: score=8.28 buy_ready=False sector_rank=14 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=103007.8 spike=1.01
- EPCO.CA: score=10.47 buy_ready=False sector_rank=14 price=8.58 support=7.0 resistance=9.98 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=62.5 liquidity=2311880.98 spike=0.37
- EPPK.CA: score=8.16 buy_ready=False sector_rank=14 price=9.78 support=9.78 resistance=9.78 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ETEL.CA: score=26.1 buy_ready=False sector_rank=1 price=142.11 support=115.0 resistance=147.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=70.31 liquidity=543879557.37 spike=1.85
- ETRS.CA: score=15.52 buy_ready=False sector_rank=14 price=10.83 support=9.51 resistance=11.3 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=64.38 liquidity=3361198.78 spike=0.22
- EXPA.CA: score=19.39 buy_ready=False sector_rank=6 price=14.51 support=12.43 resistance=15.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=56.56 liquidity=16811141.17 spike=0.78
- FAIT.CA: score=12.59 buy_ready=False sector_rank=6 price=46.09 support=40.0 resistance=47.46 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=68.74 liquidity=1200967.13 spike=0.49
- FAITA.CA: score=15.52 buy_ready=False sector_rank=6 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.94 liquidity=25383.67 spike=1.05
- FERC.CA: score=12.65 buy_ready=False sector_rank=17 price=64.5 support=52.63 resistance=72.69 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.83 liquidity=5045383.5 spike=0.63
- FWRY.CA: score=16.38 buy_ready=False sector_rank=12 price=16.95 support=15.27 resistance=18.65 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=47.81 liquidity=78525692.33 spike=0.67
- GBCO.CA: score=13.48 buy_ready=False sector_rank=21 price=22.63 support=20.9 resistance=30.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=41.51 liquidity=64177636.64 spike=0.54
- GDWA.CA: score=15.52 buy_ready=False sector_rank=14 price=0.54 support=0.46 resistance=0.6 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=57.27 liquidity=9359790.08 spike=0.8
- GGCC.CA: score=16.16 buy_ready=False sector_rank=14 price=0.55 support=0.49 resistance=0.65 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=54.39 liquidity=16756534.76 spike=0.83
- GIHD.CA: score=17.16 buy_ready=False sector_rank=14 price=50.11 support=32.1 resistance=57.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.26 liquidity=14683232.38 spike=0.84
- GMCI.CA: score=11.27 buy_ready=False sector_rank=14 price=1.76 support=1.34 resistance=1.75 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=73.33 liquidity=113125.76 spike=0.29
- GRCA.CA: score=10.67 buy_ready=False sector_rank=14 price=31.69 support=22.57 resistance=37.32 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=66.39 liquidity=4513987.06 spike=0.39
- GSSC.CA: score=8.3 buy_ready=False sector_rank=14 price=263.52 support=211.52 resistance=296.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=65.97 liquidity=1138406.35 spike=0.49
- GTWL.CA: score=17.16 buy_ready=False sector_rank=14 price=131.53 support=73.02 resistance=158.99 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.01 liquidity=205605326.55 spike=0.75
- HDBK.CA: score=20.87 buy_ready=False sector_rank=6 price=107.82 support=83.01 resistance=111.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.32 liquidity=38464892.71 spike=1.24
- HELI.CA: score=19.26 buy_ready=False sector_rank=13 price=6.71 support=5.72 resistance=7.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=57.27 liquidity=46215541.28 spike=0.61
- HRHO.CA: score=17.83 buy_ready=False sector_rank=16 price=24.09 support=21.87 resistance=26.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=50.21 liquidity=41145455.27 spike=0.82
- ICID.CA: score=11.7 buy_ready=False sector_rank=14 price=17.38 support=14.26 resistance=17.98 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=54.01 liquidity=2541181.82 spike=0.6
- IDRE.CA: score=14.95 buy_ready=False sector_rank=14 price=41.45 support=29.11 resistance=47.25 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=73.55 liquidity=8645392.46 spike=1.07
- IFAP.CA: score=10.77 buy_ready=False sector_rank=20 price=16.28 support=15.12 resistance=19.4 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=46.86 liquidity=6084161.86 spike=0.91
- INFI.CA: score=24.16 buy_ready=False sector_rank=14 price=162.06 support=93.44 resistance=162.5 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=90.93 liquidity=168426362.5 spike=4.43
- IRON.CA: score=16.32 buy_ready=False sector_rank=17 price=24.53 support=23.13 resistance=27.61 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=47.23 liquidity=11498486.88 spike=1.36
- ISMA.CA: score=16.04 buy_ready=False sector_rank=14 price=20.24 support=14.11 resistance=23.44 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.88 liquidity=7875343.43 spike=0.65
- ISMQ.CA: score=15.72 buy_ready=False sector_rank=17 price=7.0 support=5.68 resistance=7.34 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=68.8 liquidity=13465515.0 spike=1.06
- ISPH.CA: score=18.69 buy_ready=False sector_rank=11 price=10.51 support=9.02 resistance=10.82 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=57.37 liquidity=53124309.6 spike=0.78
- JUFO.CA: score=18.99 buy_ready=False sector_rank=9 price=23.56 support=21.01 resistance=25.51 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=52.27 liquidity=14216574.88 spike=0.53
- KABO.CA: score=15.77 buy_ready=False sector_rank=15 price=6.91 support=5.58 resistance=7.99 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=55.0 liquidity=9612369.5 spike=0.47
- KWIN.CA: score=13.5 buy_ready=False sector_rank=14 price=66.99 support=44.02 resistance=85.83 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=63.73 liquidity=5341581.46 spike=0.42
- KZPC.CA: score=10.71 buy_ready=False sector_rank=14 price=12.3 support=11.56 resistance=14.77 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=45.87 liquidity=5545983.99 spike=0.53
- LCSW.CA: score=22.4 buy_ready=False sector_rank=3 price=39.8 support=28.0 resistance=42.14 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=73.33 liquidity=10020883.61 spike=0.43
- LUTS.CA: score=17.16 buy_ready=False sector_rank=14 price=0.71 support=0.47 resistance=0.84 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=66.41 liquidity=53233685.7 spike=0.78
- MAAL.CA: score=17.92 buy_ready=False sector_rank=14 price=6.52 support=4.88 resistance=8.25 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=54.98 liquidity=34536928.9 spike=1.38
- MASR.CA: score=16.16 buy_ready=False sector_rank=14 price=6.62 support=5.6 resistance=8.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=51.91 liquidity=19654177.24 spike=0.55
- MBSC.CA: score=21.78 buy_ready=False sector_rank=3 price=355.0 support=262.0 resistance=397.9 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=75.07 liquidity=158907585.0 spike=2.19
- MCQE.CA: score=20.44 buy_ready=False sector_rank=3 price=179.31 support=145.0 resistance=205.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=63.59 liquidity=56907255.31 spike=1.02
- MCRO.CA: score=18.16 buy_ready=False sector_rank=14 price=1.34 support=1.07 resistance=1.48 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.42 liquidity=24392127.81 spike=0.48
- MENA.CA: score=20.98 buy_ready=False sector_rank=13 price=6.47 support=5.45 resistance=7.9 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=68.82 liquidity=9733325.34 spike=1.49
- MEPA.CA: score=12.29 buy_ready=False sector_rank=14 price=1.33 support=1.14 resistance=1.6 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=58.33 liquidity=6130449.0 spike=0.34
- MFPC.CA: score=8.6 buy_ready=False sector_rank=17 price=38.84 support=37.23 resistance=47.96 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=27.09 liquidity=38817045.71 spike=0.44
- MFSC.CA: score=7.64 buy_ready=False sector_rank=14 price=34.04 support=28.55 resistance=42.4 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=53.18 liquidity=1482782.44 spike=0.64
- MHOT.CA: score=17.16 buy_ready=False sector_rank=2 price=16.14 support=13.0 resistance=17.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=65.61 liquidity=4759669.68 spike=0.78
- MICH.CA: score=18.24 buy_ready=False sector_rank=14 price=45.84 support=37.35 resistance=48.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=79.49 liquidity=11958968.44 spike=1.54
- MILS.CA: score=16.46 buy_ready=False sector_rank=14 price=142.6 support=94.24 resistance=163.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.75 liquidity=9299231.6 spike=0.82
- MIPH.CA: score=21.08 buy_ready=False sector_rank=11 price=799.36 support=610.0 resistance=820.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.1 liquidity=5428453.66 spike=2.48
- MOED.CA: score=13.26 buy_ready=False sector_rank=14 price=0.47 support=0.39 resistance=0.57 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=55.0 liquidity=7104778.09 spike=0.49
- MOIL.CA: score=13.59 buy_ready=False sector_rank=4 price=0.69 support=0.6 resistance=0.71 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.61 liquidity=187687.26 spike=0.92
- MOIN.CA: score=15.7 buy_ready=False sector_rank=14 price=31.48 support=25.7 resistance=35.5 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=63.99 liquidity=6537640.38 spike=0.66
- MOSC.CA: score=9.94 buy_ready=False sector_rank=14 price=270.03 support=198.01 resistance=303.1 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=66.27 liquidity=2778068.63 spike=0.48
- MPCI.CA: score=17.58 buy_ready=False sector_rank=14 price=343.84 support=238.6 resistance=382.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.21 liquidity=147629077.79 spike=1.21
- MPCO.CA: score=17.69 buy_ready=False sector_rank=20 price=1.96 support=1.55 resistance=2.58 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=56.07 liquidity=65860230.96 spike=0.62
- MPRC.CA: score=23.2 buy_ready=False sector_rank=14 price=37.75 support=27.0 resistance=40.7 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=68.09 liquidity=57092986.75 spike=2.52
- MTIE.CA: score=14.02 buy_ready=False sector_rank=21 price=6.59 support=6.05 resistance=7.85 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=39.33 liquidity=30689703.2 spike=1.27
- NAHO.CA: score=7.17 buy_ready=False sector_rank=14 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=53.85 liquidity=5245.91 spike=0.42
- NCCW.CA: score=18.16 buy_ready=False sector_rank=14 price=5.63 support=4.05 resistance=6.34 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.6 liquidity=18710004.85 spike=0.94
- NEDA.CA: score=1.31 buy_ready=False sector_rank=14 price=2.46 support=2.26 resistance=2.6 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=29.41 liquidity=153968.94 spike=0.76
- NHPS.CA: score=11.51 buy_ready=False sector_rank=14 price=59.17 support=50.0 resistance=69.97 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.37 liquidity=5347311.07 spike=0.65
- NINH.CA: score=13.49 buy_ready=False sector_rank=14 price=15.49 support=12.36 resistance=18.5 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.28 liquidity=5332122.62 spike=0.48
- NIPH.CA: score=21.75 buy_ready=False sector_rank=11 price=307.0 support=205.0 resistance=365.5 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=70.19 liquidity=251136745.0 spike=1.53
- OBRI.CA: score=12.93 buy_ready=False sector_rank=14 price=22.99 support=18.11 resistance=26.75 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=57.82 liquidity=6768462.84 spike=0.8
- OCDI.CA: score=15.96 buy_ready=False sector_rank=13 price=25.39 support=21.0 resistance=26.8 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=59.69 liquidity=6700877.86 spike=0.21
- OCPH.CA: score=9.17 buy_ready=False sector_rank=14 price=196.95 support=147.96 resistance=224.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=68.21 liquidity=3012350.2 spike=0.55
- ODIN.CA: score=14.66 buy_ready=False sector_rank=14 price=2.08 support=1.7 resistance=2.33 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.33 liquidity=6501697.04 spike=0.79
- OFH.CA: score=19.16 buy_ready=False sector_rank=14 price=0.74 support=0.61 resistance=0.81 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.14 liquidity=13142018.55 spike=0.61
- OIH.CA: score=16.09 buy_ready=False sector_rank=18 price=1.65 support=1.5 resistance=1.84 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=49.06 liquidity=27919760.15 spike=0.61
- OLFI.CA: score=13.27 buy_ready=False sector_rank=9 price=20.53 support=17.86 resistance=21.24 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=63.55 liquidity=4279417.05 spike=0.44
- ORAS.CA: score=5.0 buy_ready=False sector_rank=19 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=18.26 buy_ready=False sector_rank=13 price=10.25 support=8.5 resistance=10.71 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.38 liquidity=81960814.25 spike=0.76
- ORWE.CA: score=17.16 buy_ready=False sector_rank=15 price=25.5 support=22.2 resistance=26.87 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=68.55 liquidity=24681832.5 spike=0.96
- PHAR.CA: score=19.69 buy_ready=False sector_rank=11 price=103.3 support=90.2 resistance=113.97 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=57.54 liquidity=51410862.02 spike=0.73
- PHDC.CA: score=16.26 buy_ready=False sector_rank=13 price=11.44 support=10.33 resistance=13.3 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=46.99 liquidity=61839546.93 spike=0.48
- PHTV.CA: score=10.54 buy_ready=False sector_rank=14 price=328.78 support=300.0 resistance=349.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.17 liquidity=1377588.19 spike=0.91
- POUL.CA: score=11.99 buy_ready=False sector_rank=9 price=7.57 support=7.51 resistance=10.4 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=27.09 liquidity=106719621.7 spike=0.9
- PRCL.CA: score=18.8 buy_ready=False sector_rank=3 price=18.5 support=16.65 resistance=23.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=39.1 liquidity=33039760.5 spike=1.2
- PRDC.CA: score=19.34 buy_ready=False sector_rank=13 price=6.43 support=5.08 resistance=7.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=55.25 liquidity=21109978.79 spike=1.04
- PRMH.CA: score=24.62 buy_ready=False sector_rank=14 price=2.31 support=1.7 resistance=2.66 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=25813309.19 spike=3.23
- RACC.CA: score=10.22 buy_ready=False sector_rank=14 price=7.98 support=6.1 resistance=8.7 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=73.03 liquidity=4063791.07 spike=0.62
- RAKT.CA: score=11.33 buy_ready=False sector_rank=14 price=22.47 support=20.4 resistance=23.16 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=49.33 liquidity=173760.5 spike=0.65
- RAYA.CA: score=18.86 buy_ready=False sector_rank=10 price=5.91 support=5.02 resistance=6.33 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=57.52 liquidity=19934949.57 spike=0.78
- RMDA.CA: score=17.69 buy_ready=False sector_rank=11 price=5.21 support=4.5 resistance=5.72 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=53.99 liquidity=16274570.9 spike=0.53
- ROTO.CA: score=13.08 buy_ready=False sector_rank=14 price=32.59 support=25.0 resistance=36.8 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.85 liquidity=4915940.8 spike=0.48
- RREI.CA: score=12.67 buy_ready=False sector_rank=14 price=2.67 support=1.96 resistance=3.4 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=59.2 liquidity=6512749.63 spike=0.53
- RTVC.CA: score=8.16 buy_ready=False sector_rank=14 price=3.11 support=2.66 resistance=3.4 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=56.0 liquidity=0.0 spike=0.0
- RUBX.CA: score=17.16 buy_ready=False sector_rank=14 price=13.22 support=10.51 resistance=18.49 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=53.32 liquidity=32079864.17 spike=0.49
- SAUD.CA: score=25.39 buy_ready=False sector_rank=6 price=23.8 support=19.3 resistance=24.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=77.37 liquidity=86693496.42 spike=3.95
- SCEM.CA: score=19.4 buy_ready=False sector_rank=3 price=97.65 support=73.9 resistance=106.55 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=81.96 liquidity=34616144.34 spike=0.74
- SCFM.CA: score=10.86 buy_ready=False sector_rank=14 price=223.27 support=153.02 resistance=240.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=74.22 liquidity=4382566.91 spike=1.16
- SCTS.CA: score=8.85 buy_ready=False sector_rank=7 price=478.3 support=410.0 resistance=555.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=36.71 liquidity=1534864.66 spike=0.25
- SDTI.CA: score=20.12 buy_ready=False sector_rank=14 price=84.94 support=75.01 resistance=90.99 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=58.99 liquidity=9960149.63 spike=0.52
- SEIG.CA: score=20.3 buy_ready=False sector_rank=14 price=231.54 support=142.0 resistance=280.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.08 liquidity=11592281.3 spike=1.07
- SIPC.CA: score=19.16 buy_ready=False sector_rank=14 price=5.14 support=3.73 resistance=5.89 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=64.0 liquidity=28240829.77 spike=0.64
- SKPC.CA: score=15.6 buy_ready=False sector_rank=17 price=14.8 support=14.01 resistance=15.9 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=51.76 liquidity=18712572.64 spike=0.49
- SMFR.CA: score=13.48 buy_ready=False sector_rank=14 price=217.18 support=165.0 resistance=264.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=68.65 liquidity=3319161.83 spike=0.42
- SNFC.CA: score=22.76 buy_ready=False sector_rank=14 price=11.39 support=10.08 resistance=11.48 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.32 liquidity=13757081.6 spike=1.3
- SPIN.CA: score=10.94 buy_ready=False sector_rank=15 price=14.83 support=12.0 resistance=16.48 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=55.3 liquidity=2784599.43 spike=0.48
- SPMD.CA: score=14.7 buy_ready=False sector_rank=14 price=0.32 support=0.3 resistance=0.39 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=43.14 liquidity=8535105.81 spike=0.55
- SUGR.CA: score=19.39 buy_ready=False sector_rank=9 price=51.2 support=44.62 resistance=55.99 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=53.85 liquidity=9402572.94 spike=0.46
- SVCE.CA: score=19.64 buy_ready=False sector_rank=14 price=9.3 support=7.01 resistance=10.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=62.4 liquidity=71429906.96 spike=1.24
- SWDY.CA: score=22.06 buy_ready=False sector_rank=5 price=119.76 support=97.0 resistance=123.45 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=69.61 liquidity=76528198.25 spike=1.33
- TALM.CA: score=24.88 buy_ready=False sector_rank=7 price=20.41 support=17.0 resistance=21.5 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=63.8 liquidity=34684182.26 spike=1.78
- TMGH.CA: score=16.26 buy_ready=False sector_rank=13 price=82.38 support=76.5 resistance=93.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=49.36 liquidity=136639994.34 spike=0.52
- TRTO.CA: score=5.16 buy_ready=False sector_rank=14 price=0.06 support=0.05 resistance=0.06 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=3102.78 spike=0.6
- UEFM.CA: score=11.93 buy_ready=False sector_rank=14 price=501.98 support=422.0 resistance=540.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=70.68 liquidity=1769479.54 spike=0.95
- UEGC.CA: score=19.06 buy_ready=False sector_rank=14 price=1.49 support=1.21 resistance=1.6 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=58.14 liquidity=45346973.19 spike=1.45
- UNIP.CA: score=13.57 buy_ready=False sector_rank=14 price=0.31 support=0.25 resistance=0.33 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=64.29 liquidity=5410334.44 spike=0.77
- UNIT.CA: score=6.03 buy_ready=False sector_rank=13 price=16.51 support=15.06 resistance=19.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=48.47 liquidity=769547.62 spike=0.39
- WCDF.CA: score=8.16 buy_ready=False sector_rank=14 price=519.91 support=450.56 resistance=565.0 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=67.97 liquidity=1561809.56 spike=1.22
- WKOL.CA: score=12.26 buy_ready=False sector_rank=14 price=171.63 support=145.33 resistance=309.43 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=60.9 liquidity=6098014.07 spike=0.5
- ZEOT.CA: score=15.91 buy_ready=False sector_rank=14 price=11.09 support=7.9 resistance=12.69 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=61.49 liquidity=6745048.99 spike=0.87
- ZMID.CA: score=19.26 buy_ready=False sector_rank=13 price=6.82 support=5.91 resistance=7.2 source=Yahoo Finance as_of=2026-11-16T22:00:00+00:00 freshness=FRESH RSI=58.85 liquidity=67664236.14 spike=0.86

## Backtesting Lite
- ETEL.CA: 180d return=53.43%, max drawdown=-22.52%, MA20>MA50 days last20=14, as_of=2026-11-16T22:00:00+00:00
- SAUD.CA: 180d return=35.95%, max drawdown=-22.66%, MA20>MA50 days last20=0, as_of=2026-11-16T22:00:00+00:00
- TALM.CA: 180d return=30.83%, max drawdown=-21.27%, MA20>MA50 days last20=11, as_of=2026-11-16T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- SAUD.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Baraka Bank Egypt summary=Evidence rejected for SAUD.CA: source text did not clearly match SAUD.CA / Al Baraka Bank Egypt.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- PRMH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Prime Holding S.A.E summary=Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- INFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ismailia National Co. for Food Industries summary=Evidence rejected for INFI.CA: source text did not clearly match INFI.CA / Ismailia National Co. for Food Industries.
- MPRC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Media Production City summary=Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- SNFC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sharkia National Company for Food Security summary=Evidence rejected for SNFC.CA: source text did not clearly match SNFC.CA / Sharkia National Company for Food Security.

## Warnings
- OpenRouter API error: 404
- Mubasher stock page returned no evidence titles for ETEL.CA.
- No Yahoo or Mubasher evidence found for ETEL.CA.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock page returned no evidence titles for SAUD.CA.
- No Yahoo or Mubasher evidence found for SAUD.CA.
- Evidence rejected for SAUD.CA: source text did not clearly match SAUD.CA / Al Baraka Bank Egypt.
- Mubasher stock page returned no evidence titles for TALM.CA.
- No Yahoo or Mubasher evidence found for TALM.CA.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Mubasher stock page returned no evidence titles for PRMH.CA.
- No Yahoo or Mubasher evidence found for PRMH.CA.
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Mubasher stock page returned no evidence titles for INFI.CA.
- No Yahoo or Mubasher evidence found for INFI.CA.
- Evidence rejected for INFI.CA: source text did not clearly match INFI.CA / Ismailia National Co. for Food Industries.
- Mubasher stock page returned no evidence titles for MPRC.CA.
- No Yahoo or Mubasher evidence found for MPRC.CA.
- Evidence rejected for MPRC.CA: source text did not clearly match MPRC.CA / Egyptian Media Production City.
- Mubasher stock page returned no evidence titles for COMI.CA.
- No Yahoo or Mubasher evidence found for COMI.CA.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Mubasher stock page returned no evidence titles for SNFC.CA.
- No Yahoo or Mubasher evidence found for SNFC.CA.
- Evidence rejected for SNFC.CA: source text did not clearly match SNFC.CA / Sharkia National Company for Food Security.
