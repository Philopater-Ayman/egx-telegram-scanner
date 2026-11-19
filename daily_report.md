# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-11-19T17:01:44.101238+00:00
Generated Cairo: 2026-11-19 19:01
Run timing: target 11:00 Cairo | generated Cairo 2026-11-19 19:01 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-11-19 18:59

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 187/187
- Top sector: Telecommunications

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 65.0% / above MA50 35.0%
- EGX70 regime: BEARISH / above MA20 55.0% / above MA50 17.5%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- AMES.CA: liquidity=651854122.0 spike=2.87 score=21.16
- COMI.CA: liquidity=366012032.0 spike=0.74 score=21.18
- HRHO.CA: liquidity=284498946.82 spike=4.53 score=25.5
- CCAP.CA: liquidity=253680742.14 spike=0.68 score=16.76
- GTWL.CA: liquidity=248134759.33 spike=0.88 score=16.42

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- INFI.CA: spike=4.94 liquidity=241749900.0 outlook=CONSTRUCTIVE score=57.06 buy_ready=False
- UNIT.CA: spike=4.91 liquidity=12654630.23 outlook=WEAK_OR_RISKY score=26.36 buy_ready=False
- MENA.CA: spike=4.88 liquidity=39278771.31 outlook=CONSTRUCTIVE score=64.36 buy_ready=False
- HRHO.CA: spike=4.53 liquidity=284498946.82 outlook=BULLISH_WATCH score=72.25 buy_ready=False
- AMES.CA: spike=2.87 liquidity=651854122.0 outlook=NEUTRAL score=46.06 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=8.01 5d=2.58% 20d=-0.18% aboveMA50=100.0%
- #2 Building Materials: score=5.62 5d=-1.53% 20d=3.73% aboveMA50=66.67%
- #3 Banking & Financials: score=5.44 5d=0.21% 20d=2.72% aboveMA50=50.0%
- #4 Food, Beverages & Tobacco: score=5.07 5d=1.24% 20d=1.45% aboveMA50=42.86%
- #5 Energy & Petrochemicals: score=3.86 5d=1.92% 20d=-2.86% aboveMA50=33.33%
- #6 Tourism & Leisure: score=3.05 5d=-1.42% 20d=1.53% aboveMA50=0.0%
- #7 Industrial Goods & Cables: score=2.79 5d=-5.3% 20d=-1.05% aboveMA50=50.0%
- #8 Healthcare: score=2.6 5d=-3.56% 20d=0.87% aboveMA50=16.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ARCC.CA: BULLISH_WATCH score=77.62 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- SAUD.CA: BULLISH_WATCH score=76.44 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- FAIT.CA: BULLISH_WATCH score=76.44 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- CIEB.CA: BULLISH_WATCH score=75.44 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA50
- SUGR.CA: BULLISH_WATCH score=75.07 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- LCSW.CA: BULLISH_WATCH score=73.62 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- COMI.CA: BULLISH_WATCH score=72.44 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- HRHO.CA: BULLISH_WATCH score=72.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CPCI.CA: BULLISH_WATCH score=71.06 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- ENGC.CA: CONSTRUCTIVE score=67.06 liquidity=TRADEABLE sector=IMPROVING risk=far above support; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=14.54 buy_ready=False sector_rank=13 price=230.24 support=171.02 resistance=269.99 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.76 liquidity=6120239.83 spike=0.33
- ABUK.CA: score=8.0 buy_ready=False sector_rank=18 price=76.21 support=73.6 resistance=95.75 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=24.16 liquidity=32047371.56 spike=0.25
- ACAMD.CA: score=15.82 buy_ready=False sector_rank=13 price=1.95 support=1.86 resistance=2.16 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=51.92 liquidity=76067210.61 spike=1.2
- ACGC.CA: score=10.63 buy_ready=False sector_rank=15 price=13.55 support=11.6 resistance=14.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.88 liquidity=2482658.13 spike=0.31
- ADCI.CA: score=9.01 buy_ready=False sector_rank=13 price=262.5 support=221.0 resistance=280.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=51.61 liquidity=590625.0 spike=0.23
- ADIB.CA: score=19.18 buy_ready=False sector_rank=3 price=46.6 support=43.16 resistance=50.49 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=53.31 liquidity=40974260.26 spike=0.53
- ADPC.CA: score=8.27 buy_ready=False sector_rank=13 price=2.94 support=2.53 resistance=3.25 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=54.13 liquidity=2849165.82 spike=0.34
- AFDI.CA: score=7.51 buy_ready=False sector_rank=13 price=43.33 support=34.8 resistance=48.35 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=52.4 liquidity=2090542.6 spike=0.75
- AFMC.CA: score=16.42 buy_ready=False sector_rank=13 price=140.41 support=94.6 resistance=166.95 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=72.37 liquidity=25465460.31 spike=0.86
- AJWA.CA: score=16.42 buy_ready=False sector_rank=13 price=267.26 support=190.2 resistance=274.44 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=85.94 liquidity=17303482.07 spike=0.54
- ALCN.CA: score=12.19 buy_ready=False sector_rank=10 price=32.22 support=27.11 resistance=33.89 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=57.29 liquidity=5316171.32 spike=0.47
- ALUM.CA: score=8.95 buy_ready=False sector_rank=13 price=19.63 support=16.02 resistance=21.8 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=63.3 liquidity=1522188.65 spike=0.52
- AMER.CA: score=16.14 buy_ready=False sector_rank=16 price=4.19 support=3.21 resistance=4.74 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=35163787.76 spike=0.54
- AMES.CA: score=21.16 buy_ready=False sector_rank=13 price=39.5 support=28.0 resistance=54.49 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.54 liquidity=651854122.0 spike=2.87
- AMIA.CA: score=14.42 buy_ready=False sector_rank=13 price=17.0 support=14.0 resistance=18.77 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=52.25 liquidity=12734411.0 spike=0.95
- AMOC.CA: score=15.54 buy_ready=False sector_rank=5 price=13.26 support=12.6 resistance=15.15 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=48.62 liquidity=63736816.58 spike=0.44
- APSW.CA: score=7.56 buy_ready=False sector_rank=13 price=7.4 support=7.1 resistance=8.07 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=48.76 liquidity=800361.81 spike=1.67
- ARAB.CA: score=18.14 buy_ready=False sector_rank=16 price=0.25 support=0.2 resistance=0.27 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=61.4 liquidity=33182514.58 spike=0.42
- ARCC.CA: score=23.25 buy_ready=False sector_rank=2 price=68.45 support=58.01 resistance=74.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=68.92 liquidity=18804309.36 spike=0.69
- AREH.CA: score=9.48 buy_ready=False sector_rank=13 price=1.02 support=0.91 resistance=1.17 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=46.88 liquidity=4057762.9 spike=0.55
- ASCM.CA: score=9.28 buy_ready=False sector_rank=13 price=45.11 support=38.2 resistance=50.4 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=58.37 liquidity=3859566.54 spike=0.61
- ASPI.CA: score=17.42 buy_ready=False sector_rank=13 price=0.32 support=0.27 resistance=0.36 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.16 liquidity=16962584.26 spike=0.73
- ATLC.CA: score=16.5 buy_ready=False sector_rank=12 price=5.47 support=3.93 resistance=6.06 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=65.91 liquidity=10977873.86 spike=0.91
- ATQA.CA: score=13.0 buy_ready=False sector_rank=18 price=10.36 support=8.25 resistance=11.08 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=78.1 liquidity=31899143.42 spike=0.7
- AXPH.CA: score=14.12 buy_ready=False sector_rank=13 price=1471.0 support=1135.0 resistance=1497.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=66.81 liquidity=4692490.0 spike=0.89
- BINV.CA: score=5.72 buy_ready=False sector_rank=20 price=51.02 support=50.6 resistance=62.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.08 liquidity=2953955.99 spike=0.28
- BIOC.CA: score=19.9 buy_ready=False sector_rank=13 price=407.0 support=212.05 resistance=447.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=71.72 liquidity=232202454.0 spike=1.24
- BTFH.CA: score=15.5 buy_ready=False sector_rank=12 price=2.28 support=2.05 resistance=2.73 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=53.97 liquidity=87451300.42 spike=0.71
- CAED.CA: score=18.42 buy_ready=False sector_rank=13 price=101.05 support=64.0 resistance=116.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=61.21 liquidity=21620961.8 spike=0.79
- CANA.CA: score=11.18 buy_ready=False sector_rank=3 price=32.19 support=29.33 resistance=48.49 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=26.91 liquidity=16925211.57 spike=0.77
- CCAP.CA: score=16.76 buy_ready=False sector_rank=20 price=6.06 support=5.55 resistance=6.44 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.62 liquidity=253680742.14 spike=0.68
- CCRS.CA: score=12.85 buy_ready=False sector_rank=13 price=2.01 support=1.3 resistance=2.49 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=68.75 liquidity=7428481.58 spike=0.4
- CEFM.CA: score=6.88 buy_ready=False sector_rank=13 price=126.08 support=97.79 resistance=138.99 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=66.64 liquidity=456283.53 spike=0.15
- CERA.CA: score=15.42 buy_ready=False sector_rank=13 price=1.04 support=0.93 resistance=1.29 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=51.43 liquidity=22797341.0 spike=0.35
- CFGH.CA: score=2.42 buy_ready=False sector_rank=13 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=80.0 liquidity=0.0 spike=0.0
- CICH.CA: score=6.43 buy_ready=False sector_rank=12 price=10.31 support=9.91 resistance=11.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=38.22 liquidity=925157.58 spike=0.4
- CIEB.CA: score=21.7 buy_ready=False sector_rank=3 price=23.21 support=21.35 resistance=23.9 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.28 liquidity=15567294.54 spike=1.76
- CIRA.CA: score=16.76 buy_ready=False sector_rank=9 price=38.52 support=32.01 resistance=40.11 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=74.42 liquidity=6778980.8 spike=0.38
- CLHO.CA: score=18.04 buy_ready=False sector_rank=8 price=13.81 support=12.51 resistance=15.15 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=53.76 liquidity=21322737.32 spike=0.59
- CNFN.CA: score=9.14 buy_ready=False sector_rank=12 price=3.95 support=3.25 resistance=4.32 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.54 liquidity=1635742.42 spike=0.22
- COMI.CA: score=21.18 buy_ready=False sector_rank=3 price=128.0 support=117.41 resistance=131.36 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=69.7 liquidity=366012032.0 spike=0.74
- COPR.CA: score=15.59 buy_ready=False sector_rank=13 price=0.39 support=0.33 resistance=0.45 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=47.76 liquidity=9167161.91 spike=0.48
- COSG.CA: score=9.79 buy_ready=False sector_rank=13 price=1.29 support=1.11 resistance=1.45 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=56.82 liquidity=4366896.26 spike=0.53
- CPCI.CA: score=13.09 buy_ready=False sector_rank=13 price=576.8 support=550.84 resistance=597.07 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=51.21 liquidity=3663256.72 spike=0.86
- CSAG.CA: score=7.04 buy_ready=False sector_rank=10 price=35.84 support=30.1 resistance=37.36 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=77.32 liquidity=3168721.93 spike=0.5
- DAPH.CA: score=15.42 buy_ready=False sector_rank=13 price=85.9 support=65.2 resistance=98.1 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=69.13 liquidity=14755215.06 spike=0.68
- DEIN.CA: score=7.42 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=9.51 buy_ready=False sector_rank=4 price=25.31 support=20.27 resistance=26.5 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=76.14 liquidity=2477469.3 spike=0.96
- DSCW.CA: score=15.32 buy_ready=False sector_rank=13 price=1.52 support=1.23 resistance=1.66 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=55.81 liquidity=7895649.02 spike=0.51
- DTPP.CA: score=12.42 buy_ready=False sector_rank=13 price=60.0 support=36.0 resistance=69.99 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=75.02 liquidity=34145820.0 spike=0.64
- EALR.CA: score=9.42 buy_ready=False sector_rank=13 price=295.8 support=236.01 resistance=337.99 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=63.07 liquidity=1997833.12 spike=0.26
- EASB.CA: score=7.5 buy_ready=False sector_rank=13 price=6.04 support=5.03 resistance=7.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.95 liquidity=1078327.23 spike=0.17
- EAST.CA: score=22.03 buy_ready=False sector_rank=4 price=34.08 support=28.14 resistance=35.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.82 liquidity=44645518.08 spike=0.79
- EBSC.CA: score=8.84 buy_ready=False sector_rank=13 price=1.52 support=1.2 resistance=1.7 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1416050.22 spike=0.36
- ECAP.CA: score=8.71 buy_ready=False sector_rank=13 price=28.14 support=24.8 resistance=30.4 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.35 liquidity=1282593.03 spike=0.43
- EDFM.CA: score=6.69 buy_ready=False sector_rank=13 price=362.76 support=326.73 resistance=378.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=72.68 liquidity=262638.25 spike=0.21
- EEII.CA: score=15.42 buy_ready=False sector_rank=13 price=2.0 support=1.42 resistance=2.29 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=68.93 liquidity=12598756.0 spike=0.86
- EFIC.CA: score=16.74 buy_ready=False sector_rank=18 price=162.0 support=121.0 resistance=174.88 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=64.23 liquidity=9743652.0 spike=0.36
- EFID.CA: score=17.03 buy_ready=False sector_rank=4 price=20.4 support=16.01 resistance=21.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=72.66 liquidity=29545992.65 spike=0.8
- EFIH.CA: score=18.86 buy_ready=False sector_rank=11 price=25.0 support=20.3 resistance=25.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=92.33 liquidity=33043550.0 spike=0.59
- EGAL.CA: score=16.0 buy_ready=False sector_rank=18 price=307.25 support=270.1 resistance=318.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=68.53 liquidity=31958916.0 spike=0.37
- EGAS.CA: score=10.07 buy_ready=False sector_rank=5 price=48.59 support=43.0 resistance=61.68 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=56.86 liquidity=1522810.6 spike=0.35
- EGBE.CA: score=11.19 buy_ready=False sector_rank=3 price=0.5 support=0.47 resistance=0.51 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=38.0 liquidity=10283.7 spike=0.22
- EGCH.CA: score=15.0 buy_ready=False sector_rank=18 price=10.3 support=9.66 resistance=11.94 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=44.93 liquidity=20707429.38 spike=0.48
- EGSA.CA: score=14.4 buy_ready=False sector_rank=1 price=9.0 support=8.7 resistance=9.04 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=74.36 liquidity=3321.0 spike=0.59
- EGTS.CA: score=17.14 buy_ready=False sector_rank=16 price=12.85 support=10.19 resistance=14.45 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=57.02 liquidity=15645402.31 spike=0.72
- EHDR.CA: score=9.96 buy_ready=False sector_rank=13 price=2.07 support=1.8 resistance=2.32 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=58.57 liquidity=4540281.96 spike=0.5
- ELEC.CA: score=16.12 buy_ready=False sector_rank=7 price=1.64 support=1.34 resistance=1.83 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=65.38 liquidity=18246775.96 spike=0.45
- ELKA.CA: score=19.68 buy_ready=False sector_rank=13 price=1.47 support=1.21 resistance=1.63 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.62 liquidity=19565369.63 spike=1.63
- ELNA.CA: score=9.49 buy_ready=False sector_rank=13 price=41.28 support=35.01 resistance=44.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=68.04 liquidity=61631.04 spike=0.08
- ELSH.CA: score=10.44 buy_ready=False sector_rank=13 price=10.9 support=8.57 resistance=11.8 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=65.02 liquidity=4019145.96 spike=0.27
- ELWA.CA: score=-0.85 buy_ready=False sector_rank=13 price=1.21 support=1.16 resistance=1.59 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=19.44 liquidity=730283.42 spike=0.56
- EMFD.CA: score=16.14 buy_ready=False sector_rank=16 price=12.51 support=10.6 resistance=12.96 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=73.71 liquidity=47036700.14 spike=0.67
- ENGC.CA: score=21.66 buy_ready=False sector_rank=13 price=39.0 support=26.91 resistance=43.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=61.96 liquidity=22488297.0 spike=1.12
- EOSB.CA: score=7.44 buy_ready=False sector_rank=13 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=15903.58 spike=0.16
- EPCO.CA: score=10.49 buy_ready=False sector_rank=13 price=8.47 support=7.0 resistance=9.98 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=63.41 liquidity=3067978.09 spike=0.51
- EPPK.CA: score=7.42 buy_ready=False sector_rank=13 price=9.78 support=9.78 resistance=9.78 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ETEL.CA: score=21.4 buy_ready=False sector_rank=1 price=141.95 support=115.0 resistance=147.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=78.7 liquidity=227715759.25 spike=0.77
- ETRS.CA: score=19.8 buy_ready=False sector_rank=13 price=10.73 support=9.51 resistance=11.3 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.88 liquidity=8378090.94 spike=0.56
- EXPA.CA: score=14.06 buy_ready=False sector_rank=3 price=14.68 support=12.43 resistance=15.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=66.44 liquidity=5888735.32 spike=0.28
- FAIT.CA: score=16.33 buy_ready=False sector_rank=3 price=45.59 support=40.0 resistance=47.46 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=63.35 liquidity=2157546.76 spike=0.88
- FAITA.CA: score=15.73 buy_ready=False sector_rank=3 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.94 liquidity=76298.23 spike=2.74
- FERC.CA: score=7.93 buy_ready=False sector_rank=18 price=64.87 support=52.63 resistance=72.69 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=57.65 liquidity=938539.2 spike=0.12
- FWRY.CA: score=15.86 buy_ready=False sector_rank=11 price=16.91 support=15.27 resistance=18.65 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=49.19 liquidity=89348346.97 spike=0.75
- GBCO.CA: score=13.4 buy_ready=False sector_rank=21 price=22.32 support=20.9 resistance=27.8 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=43.57 liquidity=34043758.09 spike=0.31
- GDWA.CA: score=9.99 buy_ready=False sector_rank=13 price=0.54 support=0.46 resistance=0.6 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=57.06 liquidity=4567275.36 spike=0.41
- GGCC.CA: score=17.42 buy_ready=False sector_rank=13 price=0.56 support=0.49 resistance=0.65 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=57.87 liquidity=11073421.62 spike=0.56
- GIHD.CA: score=16.64 buy_ready=False sector_rank=13 price=51.5 support=32.1 resistance=57.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=70.37 liquidity=19555992.0 spike=1.11
- GMCI.CA: score=9.26 buy_ready=False sector_rank=13 price=1.69 support=1.34 resistance=1.75 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=65.67 liquidity=475082.68 spike=1.18
- GRCA.CA: score=12.43 buy_ready=False sector_rank=13 price=31.93 support=22.57 resistance=37.32 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=65.56 liquidity=7007006.64 spike=0.59
- GSSC.CA: score=8.68 buy_ready=False sector_rank=13 price=263.52 support=211.52 resistance=296.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=64.75 liquidity=251925.11 spike=0.11
- GTWL.CA: score=16.42 buy_ready=False sector_rank=13 price=138.6 support=73.02 resistance=158.99 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=70.37 liquidity=248134759.33 spike=0.88
- HDBK.CA: score=18.18 buy_ready=False sector_rank=3 price=108.67 support=83.01 resistance=111.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=77.43 liquidity=26877785.33 spike=0.85
- HELI.CA: score=16.14 buy_ready=False sector_rank=16 price=6.6 support=5.72 resistance=7.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=58.06 liquidity=57540422.77 spike=0.77
- HRHO.CA: score=25.5 buy_ready=False sector_rank=12 price=25.3 support=21.87 resistance=26.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.15 liquidity=284498946.82 spike=4.53
- ICID.CA: score=5.45 buy_ready=False sector_rank=13 price=16.78 support=14.26 resistance=17.98 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=48.21 liquidity=1022103.4 spike=0.25
- IDRE.CA: score=8.5 buy_ready=False sector_rank=13 price=41.56 support=29.11 resistance=47.25 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=70.35 liquidity=3075647.9 spike=0.38
- IFAP.CA: score=7.05 buy_ready=False sector_rank=19 price=16.02 support=15.12 resistance=19.4 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=46.86 liquidity=3162508.29 spike=0.47
- INFI.CA: score=21.42 buy_ready=False sector_rank=13 price=157.5 support=93.44 resistance=178.25 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=83.68 liquidity=241749900.0 spike=4.94
- IRON.CA: score=14.02 buy_ready=False sector_rank=18 price=24.07 support=23.13 resistance=27.61 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=43.8 liquidity=8965689.77 spike=1.03
- ISMA.CA: score=14.68 buy_ready=False sector_rank=13 price=20.5 support=14.11 resistance=22.54 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=61.32 liquidity=7260772.0 spike=0.6
- ISMQ.CA: score=10.39 buy_ready=False sector_rank=18 price=6.93 support=5.68 resistance=7.34 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=71.75 liquidity=5391013.19 spike=0.44
- ISPH.CA: score=18.04 buy_ready=False sector_rank=8 price=10.44 support=9.02 resistance=10.8 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.67 liquidity=20411984.42 spike=0.3
- JUFO.CA: score=14.4 buy_ready=False sector_rank=4 price=23.32 support=21.01 resistance=25.51 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=52.83 liquidity=7370705.66 spike=0.27
- KABO.CA: score=13.22 buy_ready=False sector_rank=15 price=6.88 support=5.58 resistance=7.88 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.5 liquidity=8075296.93 spike=0.41
- KWIN.CA: score=15.42 buy_ready=False sector_rank=13 price=71.06 support=44.02 resistance=85.83 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=67.12 liquidity=11229540.35 spike=0.86
- KZPC.CA: score=14.82 buy_ready=False sector_rank=13 price=11.99 support=11.56 resistance=14.77 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=44.56 liquidity=12815715.09 spike=1.2
- LCSW.CA: score=23.25 buy_ready=False sector_rank=2 price=39.34 support=28.0 resistance=42.14 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=65.31 liquidity=14545650.34 spike=0.63
- LUTS.CA: score=15.42 buy_ready=False sector_rank=13 price=0.69 support=0.47 resistance=0.84 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=57.73 liquidity=66350130.18 spike=0.95
- MAAL.CA: score=15.42 buy_ready=False sector_rank=13 price=6.4 support=4.88 resistance=8.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=52.48 liquidity=22795705.94 spike=0.9
- MASR.CA: score=15.42 buy_ready=False sector_rank=13 price=6.56 support=5.6 resistance=7.27 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=54.46 liquidity=12397297.81 spike=0.35
- MBSC.CA: score=20.25 buy_ready=False sector_rank=2 price=353.0 support=262.0 resistance=397.9 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=81.31 liquidity=68210543.0 spike=0.94
- MCQE.CA: score=21.25 buy_ready=False sector_rank=2 price=176.61 support=145.0 resistance=205.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=62.2 liquidity=38762362.93 spike=0.7
- MCRO.CA: score=17.42 buy_ready=False sector_rank=13 price=1.33 support=1.07 resistance=1.48 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=56.52 liquidity=18488260.11 spike=0.38
- MENA.CA: score=23.14 buy_ready=False sector_rank=16 price=7.4 support=5.45 resistance=7.9 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=84.0 liquidity=39278771.31 spike=4.88
- MEPA.CA: score=11.35 buy_ready=False sector_rank=13 price=1.33 support=1.14 resistance=1.6 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=58.33 liquidity=5921176.15 spike=0.32
- MFPC.CA: score=8.0 buy_ready=False sector_rank=18 price=38.17 support=37.23 resistance=47.96 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=21.53 liquidity=69328434.86 spike=0.8
- MFSC.CA: score=6.9 buy_ready=False sector_rank=13 price=33.99 support=28.55 resistance=42.4 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=54.8 liquidity=1476287.74 spike=0.63
- MHOT.CA: score=7.34 buy_ready=False sector_rank=6 price=15.95 support=13.0 resistance=17.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=67.39 liquidity=1121109.54 spike=0.21
- MICH.CA: score=16.21 buy_ready=False sector_rank=13 price=45.5 support=37.35 resistance=48.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=78.04 liquidity=9306479.0 spike=1.24
- MILS.CA: score=11.92 buy_ready=False sector_rank=13 price=140.09 support=94.24 resistance=163.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=67.39 liquidity=6496533.49 spike=0.57
- MIPH.CA: score=9.92 buy_ready=False sector_rank=8 price=779.92 support=610.0 resistance=820.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=56.43 liquidity=876630.06 spike=0.41
- MOED.CA: score=10.71 buy_ready=False sector_rank=13 price=0.48 support=0.39 resistance=0.57 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=56.22 liquidity=5283968.79 spike=0.36
- MOIL.CA: score=12.67 buy_ready=False sector_rank=5 price=0.69 support=0.6 resistance=0.71 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=63.86 liquidity=129166.55 spike=0.63
- MOIN.CA: score=13.57 buy_ready=False sector_rank=13 price=31.89 support=25.7 resistance=35.5 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=64.92 liquidity=5150585.69 spike=0.53
- MOSC.CA: score=15.54 buy_ready=False sector_rank=13 price=260.16 support=198.01 resistance=303.1 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=58.58 liquidity=6754013.86 spike=1.18
- MPCI.CA: score=19.42 buy_ready=False sector_rank=13 price=357.9 support=238.6 resistance=382.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=69.22 liquidity=62948524.63 spike=0.53
- MPCO.CA: score=16.89 buy_ready=False sector_rank=19 price=2.0 support=1.55 resistance=2.58 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.38 liquidity=97309940.0 spike=0.92
- MPRC.CA: score=17.01 buy_ready=False sector_rank=13 price=38.64 support=27.0 resistance=40.7 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=72.71 liquidity=7587195.72 spike=0.34
- MTIE.CA: score=13.4 buy_ready=False sector_rank=21 price=6.61 support=6.05 resistance=7.85 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=41.96 liquidity=12764498.55 spike=0.55
- NAHO.CA: score=6.43 buy_ready=False sector_rank=13 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=53.85 liquidity=2968.29 spike=0.25
- NCCW.CA: score=17.37 buy_ready=False sector_rank=13 price=5.67 support=4.05 resistance=6.34 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=64.66 liquidity=9944136.85 spike=0.51
- NEDA.CA: score=0.62 buy_ready=False sector_rank=13 price=2.46 support=2.26 resistance=2.58 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=29.41 liquidity=199011.54 spike=0.98
- NHPS.CA: score=9.32 buy_ready=False sector_rank=13 price=60.34 support=50.0 resistance=69.97 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=63.38 liquidity=1892926.14 spike=0.23
- NINH.CA: score=11.09 buy_ready=False sector_rank=13 price=15.83 support=12.36 resistance=18.5 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=57.63 liquidity=3665784.74 spike=0.34
- NIPH.CA: score=20.42 buy_ready=False sector_rank=8 price=321.0 support=205.0 resistance=365.5 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=70.47 liquidity=196546695.0 spike=1.19
- OBRI.CA: score=9.82 buy_ready=False sector_rank=13 price=22.82 support=18.11 resistance=26.75 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=55.88 liquidity=4395999.1 spike=0.53
- OCDI.CA: score=18.3 buy_ready=False sector_rank=16 price=25.6 support=21.0 resistance=26.8 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=64.79 liquidity=32264090.08 spike=1.08
- OCPH.CA: score=9.09 buy_ready=False sector_rank=13 price=202.53 support=147.96 resistance=224.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=65.75 liquidity=3666400.57 spike=0.66
- ODIN.CA: score=11.03 buy_ready=False sector_rank=13 price=2.07 support=1.7 resistance=2.33 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=3601166.46 spike=0.44
- OFH.CA: score=16.42 buy_ready=False sector_rank=13 price=0.73 support=0.61 resistance=0.81 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=58.79 liquidity=10677949.7 spike=0.5
- OIH.CA: score=15.42 buy_ready=False sector_rank=20 price=1.61 support=1.5 resistance=1.84 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=61620275.98 spike=1.33
- OLFI.CA: score=9.32 buy_ready=False sector_rank=4 price=20.29 support=17.86 resistance=21.24 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=66.43 liquidity=2296158.53 spike=0.25
- ORAS.CA: score=5.0 buy_ready=False sector_rank=17 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=17.14 buy_ready=False sector_rank=16 price=10.31 support=8.5 resistance=10.71 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=64.84 liquidity=58590464.25 spike=0.56
- ORWE.CA: score=16.65 buy_ready=False sector_rank=15 price=25.08 support=22.2 resistance=26.85 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=64.02 liquidity=8500790.73 spike=0.33
- PHAR.CA: score=19.16 buy_ready=False sector_rank=8 price=106.01 support=90.2 resistance=113.97 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.5 liquidity=77866360.76 spike=1.06
- PHDC.CA: score=15.14 buy_ready=False sector_rank=16 price=11.5 support=10.33 resistance=13.3 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=51.86 liquidity=83265934.0 spike=0.66
- PHTV.CA: score=8.47 buy_ready=False sector_rank=13 price=328.78 support=300.0 resistance=349.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=56.61 liquidity=45042.86 spike=0.03
- POUL.CA: score=12.03 buy_ready=False sector_rank=4 price=7.7 support=7.51 resistance=10.4 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=28.5 liquidity=64344979.11 spike=0.57
- PRCL.CA: score=19.25 buy_ready=False sector_rank=2 price=18.93 support=16.65 resistance=23.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=45.79 liquidity=17305295.17 spike=0.62
- PRDC.CA: score=18.14 buy_ready=False sector_rank=16 price=6.64 support=5.08 resistance=7.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=62.56 liquidity=11684334.73 spike=0.58
- PRMH.CA: score=22.02 buy_ready=False sector_rank=13 price=2.31 support=1.7 resistance=2.66 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=71.96 liquidity=20623245.21 spike=2.3
- RACC.CA: score=9.3 buy_ready=False sector_rank=13 price=7.89 support=6.1 resistance=8.7 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=70.65 liquidity=3875157.65 spike=0.61
- RAKT.CA: score=5.55 buy_ready=False sector_rank=13 price=22.47 support=20.4 resistance=23.16 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=98.21 liquidity=127652.07 spike=0.49
- RAYA.CA: score=17.32 buy_ready=False sector_rank=14 price=5.73 support=5.02 resistance=6.33 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=55.79 liquidity=20982045.31 spike=0.8
- RMDA.CA: score=17.04 buy_ready=False sector_rank=8 price=5.21 support=4.5 resistance=5.72 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=56.05 liquidity=16196624.09 spike=0.54
- ROTO.CA: score=13.97 buy_ready=False sector_rank=13 price=31.87 support=25.0 resistance=36.8 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=58.4 liquidity=6541222.06 spike=0.63
- RREI.CA: score=11.32 buy_ready=False sector_rank=13 price=2.68 support=1.96 resistance=3.4 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=61.98 liquidity=5898924.03 spike=0.48
- RTVC.CA: score=5.42 buy_ready=False sector_rank=13 price=3.11 support=2.66 resistance=3.4 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=0.0 spike=0.0
- RUBX.CA: score=16.42 buy_ready=False sector_rank=13 price=13.23 support=10.51 resistance=18.44 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=56.69 liquidity=19212750.87 spike=0.32
- SAUD.CA: score=22.18 buy_ready=False sector_rank=3 price=23.0 support=19.3 resistance=24.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=69.44 liquidity=18468379.0 spike=0.84
- SCEM.CA: score=20.25 buy_ready=False sector_rank=2 price=98.0 support=73.9 resistance=106.55 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=83.52 liquidity=27780256.0 spike=0.61
- SCFM.CA: score=6.94 buy_ready=False sector_rank=13 price=220.25 support=153.02 resistance=240.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=68.87 liquidity=1515320.0 spike=0.4
- SCTS.CA: score=7.27 buy_ready=False sector_rank=9 price=479.99 support=410.0 resistance=555.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=44.09 liquidity=1281573.27 spike=0.21
- SDTI.CA: score=17.39 buy_ready=False sector_rank=13 price=82.55 support=75.01 resistance=90.99 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=55.63 liquidity=9962712.22 spike=0.53
- SEIG.CA: score=12.67 buy_ready=False sector_rank=13 price=231.8 support=142.0 resistance=280.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=71.53 liquidity=3249836.04 spike=0.3
- SIPC.CA: score=18.42 buy_ready=False sector_rank=13 price=5.26 support=3.73 resistance=5.89 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=64.43 liquidity=19969212.15 spike=0.46
- SKPC.CA: score=15.0 buy_ready=False sector_rank=18 price=14.72 support=14.01 resistance=15.9 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=51.97 liquidity=16122948.77 spike=0.46
- SMFR.CA: score=7.87 buy_ready=False sector_rank=13 price=214.94 support=165.0 resistance=264.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=67.98 liquidity=1445901.4 spike=0.18
- SNFC.CA: score=13.31 buy_ready=False sector_rank=13 price=11.22 support=10.08 resistance=11.48 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=76.25 liquidity=6886219.06 spike=0.65
- SPIN.CA: score=8.93 buy_ready=False sector_rank=15 price=14.98 support=12.0 resistance=16.48 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=58.42 liquidity=1783698.51 spike=0.31
- SPMD.CA: score=11.06 buy_ready=False sector_rank=13 price=0.33 support=0.3 resistance=0.38 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=46.08 liquidity=5639339.58 spike=0.37
- SUGR.CA: score=23.03 buy_ready=False sector_rank=4 price=51.6 support=44.62 resistance=55.99 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=58.27 liquidity=10203951.3 spike=0.49
- SVCE.CA: score=16.42 buy_ready=False sector_rank=13 price=9.31 support=7.01 resistance=10.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=69.53 liquidity=51302841.1 spike=0.89
- SWDY.CA: score=22.12 buy_ready=False sector_rank=7 price=117.97 support=97.0 resistance=123.45 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=60.14 liquidity=21304438.46 spike=0.38
- TALM.CA: score=13.1 buy_ready=False sector_rank=9 price=20.13 support=17.0 resistance=21.5 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.35 liquidity=4116766.0 spike=0.21
- TMGH.CA: score=15.14 buy_ready=False sector_rank=16 price=82.5 support=76.5 resistance=93.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=57.84 liquidity=151260780.0 spike=0.59
- TRTO.CA: score=4.43 buy_ready=False sector_rank=13 price=0.06 support=0.05 resistance=0.06 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=1230.0 spike=0.24
- UEFM.CA: score=10.61 buy_ready=False sector_rank=13 price=502.82 support=422.0 resistance=540.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=71.08 liquidity=1184141.12 spike=0.62
- UEGC.CA: score=17.42 buy_ready=False sector_rank=13 price=1.51 support=1.21 resistance=1.59 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=64.29 liquidity=23617562.55 spike=0.77
- UNIP.CA: score=7.5 buy_ready=False sector_rank=13 price=0.31 support=0.25 resistance=0.33 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=65.06 liquidity=2077117.18 spike=0.3
- UNIT.CA: score=19.14 buy_ready=False sector_rank=16 price=15.41 support=15.0 resistance=19.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=38.12 liquidity=12654630.23 spike=4.91
- WCDF.CA: score=7.99 buy_ready=False sector_rank=13 price=513.48 support=450.56 resistance=565.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=63.97 liquidity=568935.82 spike=0.45
- WKOL.CA: score=10.73 buy_ready=False sector_rank=13 price=170.96 support=145.33 resistance=282.0 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=61.52 liquidity=5302666.53 spike=0.49
- ZEOT.CA: score=11.21 buy_ready=False sector_rank=13 price=10.97 support=7.9 resistance=12.69 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.51 liquidity=2782485.72 spike=0.37
- ZMID.CA: score=18.14 buy_ready=False sector_rank=16 price=6.71 support=5.91 resistance=7.2 source=Yahoo Finance as_of=2026-11-17T22:00:00+00:00 freshness=FRESH RSI=59.71 liquidity=44531841.23 spike=0.57

## Backtesting Lite
- HRHO.CA: 180d return=-10.34%, max drawdown=-24.55%, MA20>MA50 days last20=0, as_of=2026-11-17T22:00:00+00:00
- LCSW.CA: 180d return=46.79%, max drawdown=-17.84%, MA20>MA50 days last20=12, as_of=2026-11-17T22:00:00+00:00
- ARCC.CA: 180d return=55.81%, max drawdown=-25.63%, MA20>MA50 days last20=0, as_of=2026-11-17T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- ARCC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Arabian Cement Company summary=Evidence rejected for ARCC.CA: source text did not clearly match ARCC.CA / Arabian Cement Company.
- MENA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Mena Touristic and Real Estate Investment summary=Evidence rejected for MENA.CA: source text did not clearly match MENA.CA / Mena Touristic and Real Estate Investment.
- SUGR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Delta Sugar summary=Evidence rejected for SUGR.CA: source text did not clearly match SUGR.CA / Delta Sugar.
- SAUD.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Baraka Bank Egypt summary=Evidence rejected for SAUD.CA: source text did not clearly match SAUD.CA / Al Baraka Bank Egypt.
- SWDY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Elsewedy Electric summary=Evidence rejected for SWDY.CA: source text did not clearly match SWDY.CA / Elsewedy Electric.
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.

## Warnings
- OpenRouter API error: 404
- Mubasher stock page returned no evidence titles for HRHO.CA.
- No Yahoo or Mubasher evidence found for HRHO.CA.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock page returned no evidence titles for LCSW.CA.
- No Yahoo or Mubasher evidence found for LCSW.CA.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Mubasher stock page returned no evidence titles for ARCC.CA.
- No Yahoo or Mubasher evidence found for ARCC.CA.
- Evidence rejected for ARCC.CA: source text did not clearly match ARCC.CA / Arabian Cement Company.
- Mubasher stock page returned no evidence titles for MENA.CA.
- No Yahoo or Mubasher evidence found for MENA.CA.
- Evidence rejected for MENA.CA: source text did not clearly match MENA.CA / Mena Touristic and Real Estate Investment.
- Mubasher stock page returned no evidence titles for SUGR.CA.
- No Yahoo or Mubasher evidence found for SUGR.CA.
- Evidence rejected for SUGR.CA: source text did not clearly match SUGR.CA / Delta Sugar.
- Mubasher stock page returned no evidence titles for SAUD.CA.
- No Yahoo or Mubasher evidence found for SAUD.CA.
- Evidence rejected for SAUD.CA: source text did not clearly match SAUD.CA / Al Baraka Bank Egypt.
- Mubasher stock page returned no evidence titles for SWDY.CA.
- No Yahoo or Mubasher evidence found for SWDY.CA.
- Evidence rejected for SWDY.CA: source text did not clearly match SWDY.CA / Elsewedy Electric.
- Mubasher stock page returned no evidence titles for EAST.CA.
- No Yahoo or Mubasher evidence found for EAST.CA.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
