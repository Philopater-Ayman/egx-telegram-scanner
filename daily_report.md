# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-11-24T17:35:54.699687+00:00
Generated Cairo: 2026-11-24 19:35
Run timing: target 09:15 Cairo | generated Cairo 2026-11-24 19:35 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-11-24 19:34

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 6
- Tradeable price/liquidity tickers: 184/184
- Top sector: Telecommunications

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 60.0% / above MA50 35.0%
- EGX70 regime: BEARISH / above MA20 35.0% / above MA50 15.0%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=524004365.5 spike=1.09 score=18.67
- ETEL.CA: liquidity=382102834.42 spike=1.35 score=22.1
- TMGH.CA: liquidity=195944604.0 spike=0.94 score=12.84
- AMES.CA: liquidity=158048074.34 spike=0.62 score=16.15
- CCAP.CA: liquidity=147884286.86 spike=0.43 score=13.18

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- FERC.CA: spike=5.82 liquidity=61699542.51 outlook=CONSTRUCTIVE score=55.83 buy_ready=False
- AJWA.CA: spike=3.02 liquidity=142015363.9 outlook=CONSTRUCTIVE score=58.87 buy_ready=False
- SDTI.CA: spike=2.98 liquidity=57313788.0 outlook=BULLISH_WATCH score=72.87 buy_ready=False
- MTIE.CA: spike=2.87 liquidity=72397136.1 outlook=NEUTRAL score=43 buy_ready=False
- NINH.CA: spike=2.44 liquidity=29830028.5 outlook=NEUTRAL score=35.87 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=9.28 5d=-0.94% 20d=6.36% aboveMA50=100.0%
- #2 Transportation & Logistics: score=7.2 5d=0.58% 20d=11.9% aboveMA50=50.0%
- #3 Fintech & Payments: score=6.68 5d=-0.75% 20d=9.3% aboveMA50=50.0%
- #4 Building Materials: score=6.28 5d=-5.45% 20d=21.05% aboveMA50=50.0%
- #5 Food, Beverages & Tobacco: score=5.73 5d=-1.56% 20d=8.6% aboveMA50=57.14%
- #6 Technology & Distribution: score=5.59 5d=-0.68% 20d=9.83% aboveMA50=0.0%
- #7 Energy & Petrochemicals: score=3.85 5d=-2.3% 20d=6.92% aboveMA50=33.33%
- #8 Banking & Financials: score=3.72 5d=-1.71% 20d=3.31% aboveMA50=40.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SUGR.CA: BULLISH_WATCH score=75.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=74.68 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- CSAG.CA: BULLISH_WATCH score=74.2 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support; close to resistance
- ZEOT.CA: BULLISH_WATCH score=72.87 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- SDTI.CA: BULLISH_WATCH score=72.87 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20; sector is not leading
- ETEL.CA: CONSTRUCTIVE score=68.28 liquidity=TRADEABLE sector=LEADING risk=overheated RSI; far above support
- DOMT.CA: CONSTRUCTIVE score=66.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- EGSA.CA: CONSTRUCTIVE score=65.28 liquidity=THIN sector=LEADING risk=liquidity below minimum; close to resistance
- MBSC.CA: CONSTRUCTIVE score=64.28 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended; far above support
- EAST.CA: CONSTRUCTIVE score=62.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- AXPH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- BIOC.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=8.49 buy_ready=False sector_rank=12 price=220.03 support=171.02 resistance=269.99 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=53.53 liquidity=4339871.7 spike=0.23
- ABUK.CA: score=13.33 buy_ready=False sector_rank=16 price=74.41 support=73.6 resistance=92.33 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=35.5 liquidity=22303952.14 spike=0.19
- ACAMD.CA: score=14.31 buy_ready=False sector_rank=12 price=1.94 support=1.86 resistance=2.16 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=53.45 liquidity=76183414.25 spike=1.08
- ACGC.CA: score=15.54 buy_ready=False sector_rank=9 price=13.5 support=11.6 resistance=14.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=65.04 liquidity=8069355.0 spike=1.03
- ADCI.CA: score=6.48 buy_ready=False sector_rank=12 price=258.62 support=221.0 resistance=280.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=56.57 liquidity=1329824.01 spike=0.49
- ADIB.CA: score=15.49 buy_ready=False sector_rank=8 price=46.43 support=43.75 resistance=50.49 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.73 liquidity=16075598.3 spike=0.24
- ADPC.CA: score=7.84 buy_ready=False sector_rank=12 price=2.84 support=2.54 resistance=3.25 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=48.62 liquidity=3689009.37 spike=0.52
- AFDI.CA: score=8.83 buy_ready=False sector_rank=12 price=42.18 support=34.8 resistance=47.5 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=45.92 liquidity=2677417.7 spike=0.95
- AFMC.CA: score=19.15 buy_ready=False sector_rank=12 price=134.25 support=94.19 resistance=166.23 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.99 liquidity=12006783.0 spike=0.39
- AJWA.CA: score=24.19 buy_ready=False sector_rank=12 price=262.7 support=190.2 resistance=294.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=71.26 liquidity=142015363.9 spike=3.02
- ALCN.CA: score=11.18 buy_ready=False sector_rank=2 price=31.5 support=29.72 resistance=33.89 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=55.12 liquidity=2781418.5 spike=0.28
- ALUM.CA: score=8.03 buy_ready=False sector_rank=12 price=18.71 support=16.02 resistance=21.8 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.74 liquidity=1878446.49 spike=0.68
- AMER.CA: score=13.84 buy_ready=False sector_rank=18 price=3.77 support=3.21 resistance=4.74 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=40.54 liquidity=64314476.78 spike=0.87
- AMES.CA: score=16.15 buy_ready=False sector_rank=12 price=37.81 support=28.0 resistance=54.49 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=56.48 liquidity=158048074.34 spike=0.62
- AMIA.CA: score=7.24 buy_ready=False sector_rank=12 price=16.15 support=14.0 resistance=18.77 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=29.43 liquidity=7088896.98 spike=0.53
- AMOC.CA: score=10.54 buy_ready=False sector_rank=7 price=12.51 support=12.35 resistance=15.15 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=26.45 liquidity=84609184.79 spike=0.59
- APSW.CA: score=6.32 buy_ready=False sector_rank=12 price=7.4 support=7.1 resistance=8.07 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=51.43 liquidity=175994.2 spike=0.39
- ARAB.CA: score=13.84 buy_ready=False sector_rank=18 price=0.25 support=0.21 resistance=0.26 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=68.25 liquidity=43067861.75 spike=0.58
- ARCC.CA: score=16.4 buy_ready=False sector_rank=4 price=66.09 support=58.01 resistance=74.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=61.52 liquidity=18467858.13 spike=0.68
- AREH.CA: score=10.9 buy_ready=False sector_rank=12 price=0.99 support=0.91 resistance=1.17 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=6749199.34 spike=0.92
- ASCM.CA: score=9.26 buy_ready=False sector_rank=12 price=43.7 support=38.2 resistance=50.4 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=56.01 liquidity=3112270.35 spike=0.55
- ASPI.CA: score=16.15 buy_ready=False sector_rank=12 price=0.31 support=0.27 resistance=0.36 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=12954366.28 spike=0.57
- ATLC.CA: score=11.83 buy_ready=False sector_rank=14 price=5.19 support=3.93 resistance=6.06 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.92 liquidity=3316550.17 spike=0.29
- ATQA.CA: score=16.33 buy_ready=False sector_rank=16 price=10.05 support=8.25 resistance=11.01 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=37849999.17 spike=0.83
- BINV.CA: score=3.96 buy_ready=False sector_rank=21 price=50.8 support=49.0 resistance=58.5 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=48.8 liquidity=784961.59 spike=0.09
- BTFH.CA: score=13.51 buy_ready=False sector_rank=14 price=2.13 support=2.08 resistance=2.59 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=36.67 liquidity=102308778.94 spike=0.82
- CAED.CA: score=19.15 buy_ready=False sector_rank=12 price=97.02 support=64.0 resistance=116.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=60.29 liquidity=12261581.22 spike=0.44
- CANA.CA: score=9.49 buy_ready=False sector_rank=8 price=32.45 support=29.33 resistance=48.49 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=24.43 liquidity=11928036.18 spike=0.55
- CCAP.CA: score=13.18 buy_ready=False sector_rank=21 price=5.8 support=5.55 resistance=6.35 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=52.5 liquidity=147884286.86 spike=0.43
- CCRS.CA: score=15.12 buy_ready=False sector_rank=12 price=1.93 support=1.3 resistance=2.49 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=64.04 liquidity=6972254.12 spike=0.37
- CEFM.CA: score=9.49 buy_ready=False sector_rank=12 price=120.41 support=97.79 resistance=138.99 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=64.57 liquidity=343048.1 spike=0.12
- CERA.CA: score=16.15 buy_ready=False sector_rank=12 price=1.03 support=0.93 resistance=1.19 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=51.22 liquidity=27912800.43 spike=0.52
- CFGH.CA: score=3.15 buy_ready=False sector_rank=12 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=80.0 liquidity=1738.75 spike=0.43
- CICH.CA: score=4.59 buy_ready=False sector_rank=14 price=10.07 support=9.88 resistance=11.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=39.46 liquidity=1079514.04 spike=0.47
- CIEB.CA: score=14.49 buy_ready=False sector_rank=8 price=23.25 support=21.35 resistance=23.9 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=64.55 liquidity=5003400.0 spike=0.55
- CIRA.CA: score=11.04 buy_ready=False sector_rank=13 price=37.71 support=32.3 resistance=40.11 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=64.92 liquidity=2142116.5 spike=0.13
- CLHO.CA: score=16.18 buy_ready=False sector_rank=11 price=14.13 support=12.51 resistance=15.15 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=27841088.12 spike=0.79
- CNFN.CA: score=5.71 buy_ready=False sector_rank=14 price=3.82 support=3.25 resistance=4.32 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=57.42 liquidity=2194223.24 spike=0.34
- COMI.CA: score=18.67 buy_ready=False sector_rank=8 price=126.5 support=117.41 resistance=131.36 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=63.71 liquidity=524004365.5 spike=1.09
- COPR.CA: score=20.25 buy_ready=False sector_rank=12 price=0.42 support=0.34 resistance=0.45 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.34 liquidity=30517134.55 spike=1.55
- COSG.CA: score=18.33 buy_ready=False sector_rank=12 price=1.33 support=1.11 resistance=1.49 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.32 liquidity=15558674.33 spike=1.09
- CPCI.CA: score=7.15 buy_ready=False sector_rank=12 price=555.61 support=550.84 resistance=597.07 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=37.74 liquidity=1999084.73 spike=0.53
- CSAG.CA: score=24.08 buy_ready=False sector_rank=2 price=38.01 support=30.32 resistance=38.4 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=86.23 liquidity=12748629.46 spike=1.84
- DAPH.CA: score=16.41 buy_ready=False sector_rank=12 price=82.88 support=65.6 resistance=98.1 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=56.78 liquidity=23897535.53 spike=1.13
- DEIN.CA: score=8.15 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=14.46 buy_ready=False sector_rank=5 price=24.63 support=20.47 resistance=26.5 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.4 liquidity=2170863.5 spike=0.77
- DSCW.CA: score=9.88 buy_ready=False sector_rank=12 price=1.44 support=1.31 resistance=1.66 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=52.0 liquidity=5727777.35 spike=0.38
- DTPP.CA: score=16.45 buy_ready=False sector_rank=12 price=58.36 support=36.0 resistance=69.99 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=65.68 liquidity=62596294.69 spike=1.15
- EALR.CA: score=11.42 buy_ready=False sector_rank=12 price=292.35 support=236.01 resistance=337.99 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=62.02 liquidity=3275489.47 spike=0.41
- EASB.CA: score=5.73 buy_ready=False sector_rank=12 price=5.6 support=5.23 resistance=7.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=44.4 liquidity=1582789.57 spike=0.24
- EAST.CA: score=18.29 buy_ready=False sector_rank=5 price=33.21 support=29.05 resistance=35.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=65.77 liquidity=22323063.97 spike=0.46
- EBSC.CA: score=6.91 buy_ready=False sector_rank=12 price=1.47 support=1.2 resistance=1.7 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=55.93 liquidity=757626.25 spike=0.2
- ECAP.CA: score=10.7 buy_ready=False sector_rank=12 price=28.39 support=24.8 resistance=30.4 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=64.31 liquidity=2552459.68 spike=0.98
- EDFM.CA: score=7.42 buy_ready=False sector_rank=12 price=362.76 support=312.0 resistance=378.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=69.95 liquidity=269167.93 spike=0.23
- EEII.CA: score=17.73 buy_ready=False sector_rank=12 price=1.97 support=1.42 resistance=2.29 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=61.86 liquidity=9580565.21 spike=0.61
- EFIC.CA: score=17.33 buy_ready=False sector_rank=16 price=155.48 support=122.0 resistance=174.88 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=62.19 liquidity=10873804.46 spike=0.44
- EFID.CA: score=20.29 buy_ready=False sector_rank=5 price=20.4 support=16.01 resistance=21.35 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=66.71 liquidity=24845832.74 spike=0.61
- EFIH.CA: score=22.4 buy_ready=False sector_rank=3 price=24.8 support=20.31 resistance=26.18 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=67.31 liquidity=34416025.34 spike=0.55
- EGAL.CA: score=16.33 buy_ready=False sector_rank=16 price=302.0 support=271.05 resistance=318.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=66.55 liquidity=24015644.0 spike=0.32
- EGAS.CA: score=9.41 buy_ready=False sector_rank=7 price=49.1 support=43.0 resistance=61.68 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=64.94 liquidity=866860.47 spike=0.2
- EGBE.CA: score=7.5 buy_ready=False sector_rank=8 price=0.49 support=0.47 resistance=0.51 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=48.0 liquidity=10067.44 spike=0.23
- EGCH.CA: score=15.33 buy_ready=False sector_rank=16 price=9.9 support=9.66 resistance=11.3 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.17 liquidity=10012334.91 spike=0.27
- EGSA.CA: score=18.07 buy_ready=False sector_rank=1 price=9.02 support=8.7 resistance=9.06 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=11509.52 spike=1.83
- EGTS.CA: score=14.24 buy_ready=False sector_rank=18 price=12.31 support=10.19 resistance=14.45 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=56.43 liquidity=9397392.77 spike=0.4
- EHDR.CA: score=9.56 buy_ready=False sector_rank=12 price=2.04 support=1.8 resistance=2.28 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.09 liquidity=3413238.18 spike=0.41
- ELEC.CA: score=14.28 buy_ready=False sector_rank=10 price=1.55 support=1.34 resistance=1.78 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.39 liquidity=16264493.6 spike=0.52
- ELKA.CA: score=15.15 buy_ready=False sector_rank=12 price=1.45 support=1.21 resistance=1.63 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.55 liquidity=10735382.75 spike=0.88
- ELNA.CA: score=10.17 buy_ready=False sector_rank=12 price=41.28 support=35.5 resistance=44.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=56.28 liquidity=20268.48 spike=0.04
- ELSH.CA: score=11.85 buy_ready=False sector_rank=12 price=10.36 support=8.57 resistance=11.8 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=60.27 liquidity=5704371.21 spike=0.4
- ELWA.CA: score=0.49 buy_ready=False sector_rank=12 price=1.12 support=1.12 resistance=1.59 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=25.4 liquidity=1340385.77 spike=0.92
- EMFD.CA: score=16.16 buy_ready=False sector_rank=18 price=11.9 support=11.01 resistance=12.96 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=49.63 liquidity=86967803.31 spike=1.16
- ENGC.CA: score=22.15 buy_ready=False sector_rank=12 price=38.01 support=26.91 resistance=43.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=62.41 liquidity=14358352.89 spike=0.69
- EOSB.CA: score=9.38 buy_ready=False sector_rank=12 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=147137.9 spike=1.54
- EPCO.CA: score=7.68 buy_ready=False sector_rank=12 price=8.27 support=7.11 resistance=9.98 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=52.63 liquidity=1534076.81 spike=0.26
- EPPK.CA: score=8.15 buy_ready=False sector_rank=12 price=9.78 support=9.78 resistance=9.78 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ETEL.CA: score=22.1 buy_ready=False sector_rank=1 price=139.98 support=115.0 resistance=147.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=76.82 liquidity=382102834.42 spike=1.35
- ETRS.CA: score=15.06 buy_ready=False sector_rank=12 price=11.1 support=9.63 resistance=11.58 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=66.37 liquidity=4907909.57 spike=0.27
- EXPA.CA: score=10.52 buy_ready=False sector_rank=8 price=14.33 support=12.52 resistance=15.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=65.17 liquidity=4030599.08 spike=0.26
- FAIT.CA: score=13.62 buy_ready=False sector_rank=8 price=45.37 support=40.6 resistance=47.46 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=63.56 liquidity=1127580.58 spike=0.49
- FAITA.CA: score=10.5 buy_ready=False sector_rank=8 price=1.0 support=0.98 resistance=1.03 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.72 liquidity=15522.0 spike=0.5
- FERC.CA: score=22.33 buy_ready=False sector_rank=16 price=64.28 support=54.03 resistance=72.69 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=60.48 liquidity=61699542.51 spike=5.82
- FWRY.CA: score=20.4 buy_ready=False sector_rank=3 price=17.25 support=15.27 resistance=18.5 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=64.48 liquidity=31772464.5 spike=0.28
- GBCO.CA: score=14.54 buy_ready=False sector_rank=20 price=21.66 support=20.9 resistance=24.35 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=51.63 liquidity=38340084.15 spike=0.41
- GDWA.CA: score=8.81 buy_ready=False sector_rank=12 price=0.51 support=0.45 resistance=0.59 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=49.75 liquidity=4665315.55 spike=0.44
- GGCC.CA: score=13.79 buy_ready=False sector_rank=12 price=0.52 support=0.49 resistance=0.62 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=52.24 liquidity=7640274.2 spike=0.39
- GIHD.CA: score=18.15 buy_ready=False sector_rank=12 price=46.94 support=32.1 resistance=57.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.83 liquidity=11670316.34 spike=0.66
- GMCI.CA: score=11.45 buy_ready=False sector_rank=12 price=1.61 support=1.34 resistance=1.75 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=64.52 liquidity=305437.93 spike=0.73
- GRCA.CA: score=15.45 buy_ready=False sector_rank=12 price=30.9 support=22.57 resistance=37.32 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=63.88 liquidity=7303956.51 spike=0.61
- GSSC.CA: score=5.96 buy_ready=False sector_rank=12 price=234.99 support=211.52 resistance=296.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=40.15 liquidity=1816002.76 spike=0.76
- HDBK.CA: score=19.49 buy_ready=False sector_rank=8 price=105.51 support=92.52 resistance=111.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=70.25 liquidity=29382425.39 spike=0.92
- HELI.CA: score=13.12 buy_ready=False sector_rank=18 price=6.3 support=5.72 resistance=7.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=55.02 liquidity=76140334.41 spike=1.14
- HRHO.CA: score=20.53 buy_ready=False sector_rank=14 price=25.68 support=21.87 resistance=26.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=73.25 liquidity=81729554.17 spike=1.01
- ICID.CA: score=6.25 buy_ready=False sector_rank=12 price=16.66 support=14.52 resistance=17.98 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=48.47 liquidity=1106290.63 spike=0.31
- IDRE.CA: score=11.43 buy_ready=False sector_rank=12 price=40.03 support=29.11 resistance=47.25 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.81 liquidity=3282700.08 spike=0.41
- IFAP.CA: score=9.33 buy_ready=False sector_rank=15 price=16.2 support=15.12 resistance=19.4 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=56.17 liquidity=5970396.88 spike=0.87
- INFI.CA: score=17.41 buy_ready=False sector_rank=12 price=154.95 support=93.44 resistance=178.25 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=81.08 liquidity=73236961.11 spike=1.13
- IRON.CA: score=10.28 buy_ready=False sector_rank=16 price=24.5 support=23.13 resistance=27.22 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.81 liquidity=4952724.0 spike=0.61
- ISMA.CA: score=10.6 buy_ready=False sector_rank=12 price=19.67 support=14.11 resistance=22.54 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=56.29 liquidity=4449176.99 spike=0.37
- ISMQ.CA: score=13.33 buy_ready=False sector_rank=16 price=6.58 support=5.68 resistance=7.34 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=44.18 liquidity=10464871.36 spike=0.89
- ISPH.CA: score=16.18 buy_ready=False sector_rank=11 price=10.17 support=9.02 resistance=10.72 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=69.43 liquidity=20887237.69 spike=0.32
- JUFO.CA: score=15.29 buy_ready=False sector_rank=5 price=22.0 support=21.26 resistance=25.51 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=43.7 liquidity=13852784.0 spike=0.52
- KABO.CA: score=19.05 buy_ready=False sector_rank=9 price=7.4 support=5.58 resistance=7.74 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=66.82 liquidity=39508459.91 spike=1.82
- KWIN.CA: score=12.45 buy_ready=False sector_rank=12 price=66.98 support=44.02 resistance=85.83 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=61.63 liquidity=4298441.72 spike=0.32
- KZPC.CA: score=11.0 buy_ready=False sector_rank=12 price=10.61 support=10.25 resistance=14.77 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=36.76 liquidity=6847290.6 spike=0.61
- LCSW.CA: score=19.65 buy_ready=False sector_rank=4 price=40.44 support=29.51 resistance=42.14 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=69.38 liquidity=8248586.96 spike=0.37
- LUTS.CA: score=14.15 buy_ready=False sector_rank=12 price=0.66 support=0.47 resistance=0.84 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=44.25 liquidity=25092772.53 spike=0.36
- MAAL.CA: score=16.04 buy_ready=False sector_rank=12 price=5.95 support=4.88 resistance=7.55 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=40.15 liquidity=9896378.83 spike=0.38
- MASR.CA: score=14.15 buy_ready=False sector_rank=12 price=6.27 support=5.62 resistance=7.11 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=44.26 liquidity=18070547.5 spike=0.54
- MBSC.CA: score=21.4 buy_ready=False sector_rank=4 price=342.73 support=270.0 resistance=397.9 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=68.18 liquidity=38288768.64 spike=0.53
- MCQE.CA: score=19.4 buy_ready=False sector_rank=4 price=175.97 support=145.0 resistance=205.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=61.13 liquidity=40420309.28 spike=0.76
- MCRO.CA: score=16.15 buy_ready=False sector_rank=12 price=1.29 support=1.09 resistance=1.48 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.35 liquidity=33707804.78 spike=0.68
- MENA.CA: score=19.26 buy_ready=False sector_rank=18 price=6.73 support=5.45 resistance=7.9 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=65.12 liquidity=12002564.69 spike=1.21
- MEPA.CA: score=9.33 buy_ready=False sector_rank=12 price=1.3 support=1.14 resistance=1.5 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=3183061.58 spike=0.18
- MFPC.CA: score=8.33 buy_ready=False sector_rank=16 price=36.6 support=36.02 resistance=47.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=29.57 liquidity=28178046.03 spike=0.34
- MFSC.CA: score=7.0 buy_ready=False sector_rank=12 price=34.01 support=28.55 resistance=39.48 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=58.05 liquidity=856201.71 spike=0.41
- MHOT.CA: score=3.47 buy_ready=False sector_rank=19 price=14.95 support=13.13 resistance=17.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=51.08 liquidity=867787.69 spike=0.15
- MICH.CA: score=12.23 buy_ready=False sector_rank=12 price=43.29 support=38.2 resistance=48.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=65.01 liquidity=2079997.96 spike=0.29
- MILS.CA: score=13.04 buy_ready=False sector_rank=12 price=133.35 support=94.24 resistance=163.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.51 liquidity=4890744.82 spike=0.44
- MIPH.CA: score=7.98 buy_ready=False sector_rank=11 price=773.56 support=650.0 resistance=820.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=56.07 liquidity=796766.8 spike=0.4
- MOED.CA: score=12.58 buy_ready=False sector_rank=12 price=0.47 support=0.39 resistance=0.54 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=55.03 liquidity=6430514.68 spike=0.47
- MOIL.CA: score=10.59 buy_ready=False sector_rank=7 price=0.68 support=0.6 resistance=0.71 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=74.81 liquidity=53127.72 spike=0.26
- MOIN.CA: score=12.26 buy_ready=False sector_rank=12 price=31.01 support=25.7 resistance=35.5 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=63.34 liquidity=3114644.42 spike=0.31
- MOSC.CA: score=18.47 buy_ready=False sector_rank=12 price=278.01 support=198.01 resistance=308.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=63.07 liquidity=6318055.48 spike=0.62
- MPCI.CA: score=19.15 buy_ready=False sector_rank=12 price=336.0 support=238.6 resistance=382.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=62.2 liquidity=79297680.0 spike=0.63
- MPCO.CA: score=16.36 buy_ready=False sector_rank=15 price=1.92 support=1.55 resistance=2.58 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=58.12 liquidity=68810168.06 spike=0.66
- MPRC.CA: score=16.92 buy_ready=False sector_rank=12 price=37.0 support=27.0 resistance=40.7 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=65.49 liquidity=6771999.0 spike=0.3
- MTIE.CA: score=16.28 buy_ready=False sector_rank=20 price=6.28 support=6.05 resistance=7.72 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=45.04 liquidity=72397136.1 spike=2.87
- NAHO.CA: score=4.64 buy_ready=False sector_rank=12 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=53.85 liquidity=15163.5 spike=1.24
- NCCW.CA: score=16.15 buy_ready=False sector_rank=12 price=5.28 support=4.05 resistance=6.34 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=53.7 liquidity=12697355.06 spike=0.64
- NEDA.CA: score=8.26 buy_ready=False sector_rank=12 price=2.46 support=2.26 resistance=2.54 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=116215.32 spike=0.58
- NHPS.CA: score=8.61 buy_ready=False sector_rank=12 price=57.52 support=50.0 resistance=69.97 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=55.23 liquidity=2464732.02 spike=0.32
- NINH.CA: score=19.03 buy_ready=False sector_rank=12 price=15.16 support=12.6 resistance=18.5 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=57.54 liquidity=29830028.5 spike=2.44
- NIPH.CA: score=19.18 buy_ready=False sector_rank=11 price=294.51 support=205.0 resistance=365.5 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.75 liquidity=105491423.93 spike=0.62
- OBRI.CA: score=8.29 buy_ready=False sector_rank=12 price=21.8 support=18.11 resistance=26.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=48.37 liquidity=4146120.05 spike=0.53
- OCDI.CA: score=12.84 buy_ready=False sector_rank=18 price=23.32 support=21.35 resistance=26.64 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.38 liquidity=20330095.89 spike=0.73
- OCPH.CA: score=9.66 buy_ready=False sector_rank=12 price=192.87 support=148.15 resistance=224.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=61.17 liquidity=1507857.62 spike=0.26
- ODIN.CA: score=9.72 buy_ready=False sector_rank=12 price=2.05 support=1.7 resistance=2.28 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.26 liquidity=3568967.92 spike=0.43
- OFH.CA: score=17.15 buy_ready=False sector_rank=12 price=0.72 support=0.61 resistance=0.81 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.02 liquidity=13419033.0 spike=0.69
- OIH.CA: score=13.2 buy_ready=False sector_rank=21 price=1.64 support=1.46 resistance=1.84 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.7 liquidity=42691503.83 spike=1.01
- OLFI.CA: score=11.76 buy_ready=False sector_rank=5 price=20.38 support=17.86 resistance=21.24 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=69.64 liquidity=4464442.62 spike=0.52
- ORAS.CA: score=5.0 buy_ready=False sector_rank=17 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=14.84 buy_ready=False sector_rank=18 price=9.98 support=8.61 resistance=10.71 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.52 liquidity=22244211.4 spike=0.24
- ORWE.CA: score=14.75 buy_ready=False sector_rank=9 price=24.7 support=22.2 resistance=26.75 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=55.25 liquidity=7345483.83 spike=0.31
- PHAR.CA: score=15.18 buy_ready=False sector_rank=11 price=101.5 support=90.2 resistance=113.97 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=58.07 liquidity=27869362.5 spike=0.39
- PHDC.CA: score=15.14 buy_ready=False sector_rank=18 price=11.55 support=10.33 resistance=12.8 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=60.77 liquidity=141963743.49 spike=1.15
- PHTV.CA: score=10.37 buy_ready=False sector_rank=12 price=335.0 support=300.0 resistance=349.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=87.69 liquidity=1222750.0 spike=0.93
- POUL.CA: score=12.29 buy_ready=False sector_rank=5 price=7.1 support=7.01 resistance=10.4 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=16.98 liquidity=77268837.46 spike=0.68
- PRCL.CA: score=10.4 buy_ready=False sector_rank=4 price=18.19 support=16.65 resistance=23.06 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=33.97 liquidity=11514361.29 spike=0.41
- PRDC.CA: score=14.84 buy_ready=False sector_rank=18 price=6.19 support=5.08 resistance=7.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=53.6 liquidity=14804152.7 spike=0.84
- PRMH.CA: score=14.03 buy_ready=False sector_rank=12 price=2.1 support=1.7 resistance=2.66 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=61.6 liquidity=5886335.43 spike=0.55
- RACC.CA: score=11.18 buy_ready=False sector_rank=12 price=7.75 support=6.1 resistance=8.55 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=60.73 liquidity=3035938.5 spike=0.49
- RAKT.CA: score=6.25 buy_ready=False sector_rank=12 price=22.47 support=20.4 resistance=23.06 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=87.5 liquidity=98216.37 spike=0.46
- RAYA.CA: score=19.24 buy_ready=False sector_rank=6 price=5.81 support=5.02 resistance=6.33 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=62.0 liquidity=16546624.2 spike=0.6
- RMDA.CA: score=15.18 buy_ready=False sector_rank=11 price=5.05 support=4.5 resistance=5.72 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=51.57 liquidity=11736811.49 spike=0.39
- ROTO.CA: score=9.87 buy_ready=False sector_rank=12 price=30.7 support=25.51 resistance=36.8 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.74 liquidity=3721454.09 spike=0.39
- RREI.CA: score=10.68 buy_ready=False sector_rank=12 price=2.54 support=1.96 resistance=3.06 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=49.11 liquidity=4534730.51 spike=0.39
- RTVC.CA: score=5.15 buy_ready=False sector_rank=12 price=3.11 support=2.66 resistance=3.15 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=97.67 liquidity=0.0 spike=0.0
- RUBX.CA: score=15.15 buy_ready=False sector_rank=12 price=12.65 support=10.51 resistance=15.98 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=53.37 liquidity=17627268.47 spike=0.35
- SAUD.CA: score=12.79 buy_ready=False sector_rank=8 price=22.63 support=19.3 resistance=24.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=72.57 liquidity=2306110.06 spike=0.11
- SCEM.CA: score=21.4 buy_ready=False sector_rank=4 price=98.63 support=73.9 resistance=106.55 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=70.73 liquidity=23232493.11 spike=0.47
- SCFM.CA: score=9.98 buy_ready=False sector_rank=12 price=215.95 support=153.02 resistance=240.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=62.85 liquidity=1834279.27 spike=0.48
- SCTS.CA: score=4.66 buy_ready=False sector_rank=13 price=459.02 support=437.0 resistance=547.9 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=40.27 liquidity=760137.1 spike=0.17
- SDTI.CA: score=22.11 buy_ready=False sector_rank=12 price=84.0 support=75.36 resistance=90.99 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=55.79 liquidity=57313788.0 spike=2.98
- SEIG.CA: score=1.93 buy_ready=False sector_rank=12 price=215.48 support=145.25 resistance=280.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=34.75 liquidity=1784389.84 spike=0.16
- SIPC.CA: score=15.15 buy_ready=False sector_rank=12 price=4.94 support=3.73 resistance=5.89 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=59.4 liquidity=16983097.76 spike=0.41
- SKPC.CA: score=13.33 buy_ready=False sector_rank=16 price=14.18 support=13.85 resistance=15.46 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=41.08 liquidity=14164657.54 spike=0.43
- SMFR.CA: score=12.45 buy_ready=False sector_rank=12 price=212.57 support=165.0 resistance=264.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=63.22 liquidity=3297173.38 spike=0.42
- SNFC.CA: score=14.46 buy_ready=False sector_rank=12 price=11.21 support=10.08 resistance=11.48 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=69.93 liquidity=4312991.46 spike=0.4
- SPIN.CA: score=9.73 buy_ready=False sector_rank=9 price=14.28 support=12.0 resistance=16.48 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=52.83 liquidity=3320842.5 spike=0.64
- SPMD.CA: score=9.02 buy_ready=False sector_rank=12 price=0.32 support=0.3 resistance=0.37 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=45.19 liquidity=4873855.89 spike=0.33
- SUGR.CA: score=19.03 buy_ready=False sector_rank=5 price=51.46 support=44.62 resistance=55.99 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=61.38 liquidity=5738458.88 spike=0.27
- SVCE.CA: score=16.15 buy_ready=False sector_rank=12 price=8.73 support=7.3 resistance=10.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=58.17 liquidity=41608548.43 spike=0.69
- SWDY.CA: score=20.28 buy_ready=False sector_rank=10 price=116.99 support=99.02 resistance=123.45 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=66.04 liquidity=36131541.91 spike=0.66
- TALM.CA: score=10.44 buy_ready=False sector_rank=13 price=20.14 support=17.0 resistance=21.5 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=68.27 liquidity=3538920.13 spike=0.2
- TMGH.CA: score=12.84 buy_ready=False sector_rank=18 price=79.5 support=76.5 resistance=86.48 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.56 liquidity=195944604.0 spike=0.94
- TRTO.CA: score=5.15 buy_ready=False sector_rank=12 price=0.06 support=0.05 resistance=0.06 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=447.42 spike=0.09
- UEFM.CA: score=11.91 buy_ready=False sector_rank=12 price=496.27 support=422.0 resistance=540.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=71.91 liquidity=1762254.73 spike=0.88
- UEGC.CA: score=16.15 buy_ready=False sector_rank=12 price=1.45 support=1.22 resistance=1.59 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=57.69 liquidity=11179993.37 spike=0.39
- UNIP.CA: score=11.48 buy_ready=False sector_rank=12 price=0.3 support=0.25 resistance=0.33 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=5327531.61 spike=0.85
- UNIT.CA: score=0.04 buy_ready=False sector_rank=18 price=15.0 support=14.16 resistance=19.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=32.97 liquidity=1194225.0 spike=0.45
- WCDF.CA: score=6.5 buy_ready=False sector_rank=12 price=501.26 support=450.56 resistance=565.0 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=53.45 liquidity=350882.01 spike=0.29
- WKOL.CA: score=8.55 buy_ready=False sector_rank=12 price=165.72 support=145.33 resistance=194.85 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=54.73 liquidity=2402277.14 spike=0.23
- ZEOT.CA: score=22.59 buy_ready=False sector_rank=12 price=12.36 support=7.9 resistance=13.9 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=68.99 liquidity=31638521.48 spike=2.22
- ZMID.CA: score=13.76 buy_ready=False sector_rank=18 price=6.33 support=5.91 resistance=7.2 source=Yahoo Finance as_of=2026-11-22T22:00:00+00:00 freshness=FRESH RSI=45.55 liquidity=118042003.16 spike=1.46

## Backtesting Lite
- AJWA.CA: 180d return=160.1%, max drawdown=-13.92%, MA20>MA50 days last20=20, as_of=2026-11-22T22:00:00+00:00
- CSAG.CA: 180d return=30.71%, max drawdown=-31.09%, MA20>MA50 days last20=0, as_of=2026-11-22T22:00:00+00:00
- ZEOT.CA: 180d return=75.33%, max drawdown=-38.04%, MA20>MA50 days last20=0, as_of=2026-11-22T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AJWA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=AJWA For Food Industries Co. Egypt summary=Evidence rejected for AJWA.CA: source text did not clearly match AJWA.CA / AJWA For Food Industries Co. Egypt.
- CSAG.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Canal Shipping Agencies summary=Evidence rejected for CSAG.CA: source text did not clearly match CSAG.CA / Canal Shipping Agencies.
- ZEOT.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Extracted Oil & Derivatives Co. summary=Evidence rejected for ZEOT.CA: source text did not clearly match ZEOT.CA / Extracted Oil & Derivatives Co..
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- FERC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ferchem Misr Fertilizers and Chemicals summary=Evidence rejected for FERC.CA: source text did not clearly match FERC.CA / Ferchem Misr Fertilizers and Chemicals.
- ENGC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Industrial Engineering Company for Construction and Development (ICON) (S.A.E) summary=Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- SDTI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Evidence rejected for SDTI.CA: source text did not clearly match SDTI.CA / SHARM DREAMS Co. for Touristic Investment S.A.E.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.

## Warnings
- OpenRouter API error: 404
- Mubasher stock page returned no evidence titles for AJWA.CA.
- No Yahoo or Mubasher evidence found for AJWA.CA.
- Evidence rejected for AJWA.CA: source text did not clearly match AJWA.CA / AJWA For Food Industries Co. Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock page returned no evidence titles for CSAG.CA.
- No Yahoo or Mubasher evidence found for CSAG.CA.
- Evidence rejected for CSAG.CA: source text did not clearly match CSAG.CA / Canal Shipping Agencies.
- Mubasher stock page returned no evidence titles for ZEOT.CA.
- No Yahoo or Mubasher evidence found for ZEOT.CA.
- Evidence rejected for ZEOT.CA: source text did not clearly match ZEOT.CA / Extracted Oil & Derivatives Co..
- Mubasher stock page returned no evidence titles for EFIH.CA.
- No Yahoo or Mubasher evidence found for EFIH.CA.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Mubasher stock page returned no evidence titles for FERC.CA.
- No Yahoo or Mubasher evidence found for FERC.CA.
- Evidence rejected for FERC.CA: source text did not clearly match FERC.CA / Ferchem Misr Fertilizers and Chemicals.
- Mubasher stock page returned no evidence titles for ENGC.CA.
- No Yahoo or Mubasher evidence found for ENGC.CA.
- Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- Mubasher stock page returned no evidence titles for SDTI.CA.
- No Yahoo or Mubasher evidence found for SDTI.CA.
- Evidence rejected for SDTI.CA: source text did not clearly match SDTI.CA / SHARM DREAMS Co. for Touristic Investment S.A.E.
- Mubasher stock page returned no evidence titles for ETEL.CA.
- No Yahoo or Mubasher evidence found for ETEL.CA.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
