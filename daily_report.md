# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-11-25T18:23:36.070598+00:00
Generated Cairo: 2026-11-25 20:23
Run timing: target 11:00 Cairo | generated Cairo 2026-11-25 20:23 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-11-25 20:21

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 7
- Tradeable price/liquidity tickers: 183/183
- Top sector: Telecommunications

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 60.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 40.0% / above MA50 20.0%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=549259158.52 spike=1.59 score=15.09
- COMI.CA: liquidity=431138637.09 spike=0.98 score=18.98
- TMGH.CA: liquidity=289315408.21 spike=1.36 score=14.21
- ETEL.CA: liquidity=278392938.0 spike=1.01 score=21.42
- HRHO.CA: liquidity=216122705.89 spike=2.46 score=24.37

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- EGBE.CA: spike=7.27 liquidity=447575.0 outlook=WEAK_OR_RISKY score=11.96 buy_ready=False
- MTIE.CA: spike=5.17 liquidity=160938093.67 outlook=NEUTRAL score=45.37 buy_ready=False
- EGSA.CA: spike=4.95 liquidity=38709.0 outlook=NEUTRAL score=44 buy_ready=False
- GRCA.CA: spike=3.24 liquidity=45766734.0 outlook=BULLISH_WATCH score=70.28 buy_ready=False
- AFDI.CA: spike=2.53 liquidity=7572162.93 outlook=CONSTRUCTIVE score=69.28 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=12.58 5d=-0.39% 20d=11.34% aboveMA50=100.0%
- #2 Technology & Distribution: score=9.66 5d=1.69% 20d=14.26% aboveMA50=0.0%
- #3 Fintech & Payments: score=8.52 5d=1.65% 20d=12.81% aboveMA50=50.0%
- #4 Transportation & Logistics: score=8.02 5d=1.47% 20d=12.54% aboveMA50=50.0%
- #5 Building Materials: score=7.44 5d=-1.58% 20d=20.37% aboveMA50=50.0%
- #6 Education: score=7.07 5d=-1.36% 20d=13.81% aboveMA50=66.67%
- #7 Energy & Petrochemicals: score=5.36 5d=-0.29% 20d=9.81% aboveMA50=33.33%
- #8 Food, Beverages & Tobacco: score=5.11 5d=-2.16% 20d=10.59% aboveMA50=57.14%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SDTI.CA: BULLISH_WATCH score=79.28 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- EFIH.CA: BULLISH_WATCH score=75.52 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- RAYA.CA: BULLISH_WATCH score=71.66 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA50; momentum is extended
- PHTV.CA: BULLISH_WATCH score=71.28 liquidity=TRADEABLE sector=IMPROVING risk=overheated RSI; sector is not leading
- CSAG.CA: BULLISH_WATCH score=71.02 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; far above support
- GRCA.CA: BULLISH_WATCH score=70.28 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading; high short-term volatility
- AFDI.CA: CONSTRUCTIVE score=69.28 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; sector is not leading
- ETRS.CA: CONSTRUCTIVE score=68.28 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- CIRA.CA: CONSTRUCTIVE score=68.07 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- FAIT.CA: CONSTRUCTIVE score=66.96 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- NIPH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ADCI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- DEIN.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=7.37 buy_ready=False sector_rank=12 price=220.32 support=171.02 resistance=269.99 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=51.23 liquidity=3058922.98 spike=0.17
- ABUK.CA: score=3.48 buy_ready=False sector_rank=17 price=74.41 support=73.6 resistance=92.33 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=41.06 liquidity=0.0 spike=0.0
- ACAMD.CA: score=14.31 buy_ready=False sector_rank=12 price=1.9 support=1.87 resistance=2.16 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=45.61 liquidity=42257530.87 spike=0.6
- ACGC.CA: score=8.91 buy_ready=False sector_rank=14 price=13.5 support=12.2 resistance=14.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=64.23 liquidity=0.0 spike=0.0
- ADIB.CA: score=14.98 buy_ready=False sector_rank=9 price=46.15 support=44.5 resistance=50.49 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=41.43 liquidity=19422412.74 spike=0.3
- ADPC.CA: score=4.31 buy_ready=False sector_rank=12 price=2.84 support=2.71 resistance=3.25 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=41.67 liquidity=0.0 spike=0.0
- AFDI.CA: score=19.94 buy_ready=False sector_rank=12 price=44.24 support=39.96 resistance=47.5 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=52.22 liquidity=7572162.93 spike=2.53
- AFMC.CA: score=7.31 buy_ready=False sector_rank=12 price=134.25 support=101.56 resistance=166.23 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=52.5 liquidity=0.0 spike=0.0
- AJWA.CA: score=10.31 buy_ready=False sector_rank=12 price=262.7 support=196.0 resistance=294.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=71.61 liquidity=0.0 spike=0.0
- ALCN.CA: score=13.66 buy_ready=False sector_rank=4 price=31.53 support=30.0 resistance=33.89 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=45.1 liquidity=7263786.97 spike=0.77
- ALUM.CA: score=8.75 buy_ready=False sector_rank=12 price=18.77 support=17.0 resistance=21.8 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=51.91 liquidity=2433117.62 spike=0.89
- AMER.CA: score=9.49 buy_ready=False sector_rank=16 price=3.64 support=3.51 resistance=4.74 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=32.79 liquidity=66325723.19 spike=0.88
- AMES.CA: score=4.31 buy_ready=False sector_rank=12 price=37.81 support=29.51 resistance=54.49 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=55.12 liquidity=0.0 spike=0.0
- AMIA.CA: score=3.02 buy_ready=False sector_rank=12 price=15.74 support=15.02 resistance=18.77 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=27.76 liquidity=2712914.88 spike=0.21
- AMOC.CA: score=11.14 buy_ready=False sector_rank=7 price=12.25 support=12.17 resistance=15.15 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=25.3 liquidity=116950051.75 spike=0.81
- APSW.CA: score=4.31 buy_ready=False sector_rank=12 price=7.4 support=7.1 resistance=8.07 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=51.43 liquidity=0.0 spike=0.0
- ARAB.CA: score=14.69 buy_ready=False sector_rank=16 price=0.25 support=0.22 resistance=0.26 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=66.1 liquidity=81014346.55 spike=1.1
- ARCC.CA: score=18.4 buy_ready=False sector_rank=5 price=67.03 support=60.17 resistance=74.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=62.77 liquidity=20107793.09 spike=0.75
- AREH.CA: score=10.11 buy_ready=False sector_rank=12 price=1.02 support=0.96 resistance=1.17 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=45.95 liquidity=5798991.61 spike=0.8
- ASCM.CA: score=6.31 buy_ready=False sector_rank=12 price=43.7 support=41.0 resistance=50.4 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.45 liquidity=0.0 spike=0.0
- ASPI.CA: score=16.31 buy_ready=False sector_rank=12 price=0.31 support=0.28 resistance=0.36 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=55.88 liquidity=18038846.88 spike=0.79
- ATLC.CA: score=13.02 buy_ready=False sector_rank=10 price=5.2 support=4.4 resistance=6.06 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=55.79 liquidity=3571328.67 spike=0.32
- ATQA.CA: score=5.48 buy_ready=False sector_rank=17 price=10.05 support=8.67 resistance=11.01 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=66.93 liquidity=0.0 spike=0.0
- AXPH.CA: score=12.31 buy_ready=False sector_rank=12 price=1415.42 support=1118.02 resistance=1415.42 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=71.88 liquidity=0.0 spike=0.0
- BINV.CA: score=10.71 buy_ready=False sector_rank=21 price=52.77 support=49.0 resistance=57.98 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=53.69 liquidity=4802861.59 spike=0.61
- BIOC.CA: score=12.31 buy_ready=False sector_rank=12 price=387.0 support=225.86 resistance=446.13 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=64.3 liquidity=0.0 spike=0.0
- BTFH.CA: score=14.45 buy_ready=False sector_rank=10 price=2.16 support=2.08 resistance=2.59 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=39.68 liquidity=119087554.73 spike=0.97
- CAED.CA: score=19.31 buy_ready=False sector_rank=12 price=101.25 support=69.0 resistance=116.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=51.75 liquidity=28593303.75 spike=0.98
- CANA.CA: score=16.98 buy_ready=False sector_rank=9 price=33.26 support=29.33 resistance=48.49 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=64.42 liquidity=22402338.39 spike=1.0
- CCAP.CA: score=15.09 buy_ready=False sector_rank=21 price=5.68 support=5.55 resistance=6.35 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=48.54 liquidity=549259158.52 spike=1.59
- CCRS.CA: score=18.31 buy_ready=False sector_rank=12 price=2.0 support=1.53 resistance=2.49 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=64.35 liquidity=18803862.0 spike=0.97
- CEFM.CA: score=9.31 buy_ready=False sector_rank=12 price=120.41 support=103.34 resistance=138.99 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=59.4 liquidity=0.0 spike=0.0
- CERA.CA: score=6.31 buy_ready=False sector_rank=12 price=1.03 support=0.96 resistance=1.19 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- CFGH.CA: score=3.31 buy_ready=False sector_rank=12 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=88.89 liquidity=0.0 spike=0.0
- CICH.CA: score=5.51 buy_ready=False sector_rank=10 price=10.04 support=9.88 resistance=11.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=41.71 liquidity=1065685.76 spike=0.46
- CIEB.CA: score=11.9 buy_ready=False sector_rank=9 price=23.2 support=21.7 resistance=23.95 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=61.02 liquidity=2914523.3 spike=0.33
- CIRA.CA: score=23.96 buy_ready=False sector_rank=6 price=38.45 support=33.3 resistance=40.11 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=64.62 liquidity=22574110.8 spike=1.28
- CLHO.CA: score=7.67 buy_ready=False sector_rank=15 price=14.13 support=12.88 resistance=15.15 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=64.52 liquidity=0.0 spike=0.0
- CNFN.CA: score=13.25 buy_ready=False sector_rank=10 price=3.83 support=3.47 resistance=4.32 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.75 liquidity=8285791.19 spike=1.26
- COMI.CA: score=18.98 buy_ready=False sector_rank=9 price=126.47 support=117.41 resistance=131.36 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=59.03 liquidity=431138637.09 spike=0.98
- COPR.CA: score=21.81 buy_ready=False sector_rank=12 price=0.43 support=0.36 resistance=0.46 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=58.89 liquidity=48315947.61 spike=2.25
- COSG.CA: score=8.31 buy_ready=False sector_rank=12 price=1.33 support=1.17 resistance=1.49 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=56.36 liquidity=0.0 spike=0.0
- CPCI.CA: score=0.31 buy_ready=False sector_rank=12 price=555.61 support=555.01 resistance=597.07 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=33.09 liquidity=0.0 spike=0.0
- CSAG.CA: score=21.98 buy_ready=False sector_rank=4 price=38.11 support=31.0 resistance=39.7 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=84.6 liquidity=12832742.4 spike=1.79
- DAPH.CA: score=16.31 buy_ready=False sector_rank=12 price=82.99 support=69.0 resistance=98.1 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=53.5 liquidity=15952337.39 spike=0.77
- DOMT.CA: score=12.04 buy_ready=False sector_rank=8 price=24.63 support=21.19 resistance=26.5 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=58.33 liquidity=0.0 spike=0.0
- DSCW.CA: score=4.31 buy_ready=False sector_rank=12 price=1.44 support=1.37 resistance=1.66 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.17 liquidity=0.0 spike=0.0
- DTPP.CA: score=8.31 buy_ready=False sector_rank=12 price=58.36 support=41.08 resistance=69.99 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=64.46 liquidity=0.0 spike=0.0
- EALR.CA: score=10.96 buy_ready=False sector_rank=12 price=297.72 support=245.21 resistance=337.99 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=62.92 liquidity=2650898.89 spike=0.33
- EASB.CA: score=2.26 buy_ready=False sector_rank=12 price=5.57 support=5.34 resistance=7.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=24.87 liquidity=2949214.83 spike=0.46
- EAST.CA: score=10.04 buy_ready=False sector_rank=8 price=33.21 support=29.31 resistance=35.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=57.71 liquidity=0.0 spike=0.0
- EBSC.CA: score=7.19 buy_ready=False sector_rank=12 price=1.49 support=1.29 resistance=1.7 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=48.0 liquidity=875071.05 spike=0.24
- ECAP.CA: score=8.31 buy_ready=False sector_rank=12 price=28.39 support=25.12 resistance=30.4 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=62.11 liquidity=0.0 spike=0.0
- EDFM.CA: score=7.31 buy_ready=False sector_rank=12 price=362.76 support=312.0 resistance=378.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=71.24 liquidity=0.0 spike=0.0
- EEII.CA: score=8.31 buy_ready=False sector_rank=12 price=1.97 support=1.55 resistance=2.29 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=61.54 liquidity=0.0 spike=0.0
- EFIC.CA: score=7.48 buy_ready=False sector_rank=17 price=155.48 support=129.0 resistance=174.88 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=61.36 liquidity=0.0 spike=0.0
- EFID.CA: score=10.04 buy_ready=False sector_rank=8 price=20.4 support=17.22 resistance=21.35 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=65.28 liquidity=0.0 spike=0.0
- EFIH.CA: score=22.52 buy_ready=False sector_rank=3 price=25.29 support=20.61 resistance=26.18 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=67.31 liquidity=66453220.33 spike=1.06
- EGAL.CA: score=8.48 buy_ready=False sector_rank=17 price=302.0 support=276.75 resistance=318.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=63.21 liquidity=0.0 spike=0.0
- EGAS.CA: score=10.58 buy_ready=False sector_rank=7 price=49.1 support=43.81 resistance=61.68 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=61.65 liquidity=1440937.66 spike=0.34
- EGBE.CA: score=13.43 buy_ready=False sector_rank=9 price=0.5 support=0.47 resistance=0.51 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=59.02 liquidity=447575.0 spike=7.27
- EGCH.CA: score=5.48 buy_ready=False sector_rank=17 price=9.9 support=9.66 resistance=11.3 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=49.32 liquidity=0.0 spike=0.0
- EGSA.CA: score=16.44 buy_ready=False sector_rank=1 price=9.0 support=8.7 resistance=9.06 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=93.94 liquidity=38709.0 spike=4.95
- EGTS.CA: score=15.53 buy_ready=False sector_rank=16 price=12.41 support=10.7 resistance=14.45 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.21 liquidity=23024669.84 spike=1.02
- EHDR.CA: score=11.43 buy_ready=False sector_rank=12 price=2.06 support=1.86 resistance=2.28 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=58.46 liquidity=5120164.88 spike=0.63
- ELEC.CA: score=4.35 buy_ready=False sector_rank=11 price=1.55 support=1.43 resistance=1.78 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.94 liquidity=0.0 spike=0.0
- ELKA.CA: score=14.01 buy_ready=False sector_rank=12 price=1.42 support=1.33 resistance=1.63 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.88 liquidity=8694808.84 spike=0.73
- ELNA.CA: score=10.31 buy_ready=False sector_rank=12 price=41.28 support=35.5 resistance=44.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=62.54 liquidity=0.0 spike=0.0
- ELSH.CA: score=17.61 buy_ready=False sector_rank=12 price=10.47 support=8.9 resistance=11.8 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=57.31 liquidity=16923467.62 spike=1.15
- ELWA.CA: score=0.41 buy_ready=False sector_rank=12 price=1.09 support=1.08 resistance=1.59 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=27.12 liquidity=1098148.87 spike=0.72
- EMFD.CA: score=14.53 buy_ready=False sector_rank=16 price=12.2 support=11.13 resistance=12.96 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=49.82 liquidity=78990082.17 spike=1.02
- ENGC.CA: score=22.31 buy_ready=False sector_rank=12 price=38.48 support=28.93 resistance=43.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=61.68 liquidity=14689778.31 spike=0.69
- EOSB.CA: score=10.34 buy_ready=False sector_rank=12 price=1.61 support=1.55 resistance=1.69 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=27484.31 spike=0.37
- EPCO.CA: score=4.31 buy_ready=False sector_rank=12 price=8.27 support=7.4 resistance=9.98 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.34 liquidity=0.0 spike=0.0
- EPPK.CA: score=8.31 buy_ready=False sector_rank=12 price=9.78 support=9.78 resistance=9.78 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ETEL.CA: score=21.42 buy_ready=False sector_rank=1 price=141.0 support=116.83 resistance=147.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=76.54 liquidity=278392938.0 spike=1.01
- ETRS.CA: score=18.99 buy_ready=False sector_rank=12 price=11.05 support=10.25 resistance=11.58 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=60.78 liquidity=6673636.57 spike=0.39
- EXPA.CA: score=19.22 buy_ready=False sector_rank=9 price=14.43 support=13.07 resistance=15.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=64.23 liquidity=16433129.66 spike=1.12
- FAIT.CA: score=14.05 buy_ready=False sector_rank=9 price=45.85 support=42.03 resistance=47.46 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=67.67 liquidity=2706479.56 spike=1.18
- FAITA.CA: score=9.0 buy_ready=False sector_rank=9 price=1.0 support=0.98 resistance=1.03 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.72 liquidity=12932.0 spike=0.41
- FERC.CA: score=7.48 buy_ready=False sector_rank=17 price=64.28 support=55.06 resistance=72.69 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=61.04 liquidity=0.0 spike=0.0
- FWRY.CA: score=10.4 buy_ready=False sector_rank=3 price=17.25 support=15.27 resistance=18.5 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=61.75 liquidity=0.0 spike=0.0
- GBCO.CA: score=5.95 buy_ready=False sector_rank=13 price=21.66 support=20.9 resistance=23.94 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.31 liquidity=0.0 spike=0.0
- GDWA.CA: score=4.31 buy_ready=False sector_rank=12 price=0.51 support=0.45 resistance=0.59 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=46.2 liquidity=0.0 spike=0.0
- GGCC.CA: score=16.31 buy_ready=False sector_rank=12 price=0.52 support=0.5 resistance=0.62 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=47.67 liquidity=11511743.19 spike=0.58
- GIHD.CA: score=18.31 buy_ready=False sector_rank=12 price=47.4 support=35.25 resistance=57.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=57.83 liquidity=11287362.36 spike=0.64
- GMCI.CA: score=9.46 buy_ready=False sector_rank=12 price=1.61 support=1.34 resistance=1.75 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=72.73 liquidity=152516.91 spike=0.36
- GRCA.CA: score=25.79 buy_ready=False sector_rank=12 price=34.5 support=24.02 resistance=37.32 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=61.78 liquidity=45766734.0 spike=3.24
- GSSC.CA: score=4.31 buy_ready=False sector_rank=12 price=234.99 support=232.01 resistance=296.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=44.51 liquidity=0.0 spike=0.0
- HDBK.CA: score=16.98 buy_ready=False sector_rank=9 price=103.82 support=92.9 resistance=111.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=68.05 liquidity=15674016.81 spike=0.51
- HELI.CA: score=13.49 buy_ready=False sector_rank=16 price=6.35 support=5.93 resistance=7.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=54547350.08 spike=0.84
- HRHO.CA: score=24.37 buy_ready=False sector_rank=10 price=26.2 support=21.87 resistance=26.5 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=74.6 liquidity=216122705.89 spike=2.46
- ICID.CA: score=5.31 buy_ready=False sector_rank=12 price=16.66 support=15.6 resistance=17.98 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=46.67 liquidity=0.0 spike=0.0
- IDRE.CA: score=10.37 buy_ready=False sector_rank=12 price=39.91 support=30.1 resistance=47.25 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=56.66 liquidity=2059555.54 spike=0.26
- IFAP.CA: score=6.85 buy_ready=False sector_rank=19 price=15.79 support=15.12 resistance=19.4 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=51.1 liquidity=3711218.43 spike=0.55
- INFI.CA: score=7.31 buy_ready=False sector_rank=12 price=154.95 support=103.51 resistance=178.25 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=80.19 liquidity=0.0 spike=0.0
- IRON.CA: score=5.48 buy_ready=False sector_rank=17 price=24.5 support=23.13 resistance=27.22 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.05 liquidity=0.0 spike=0.0
- ISMA.CA: score=6.31 buy_ready=False sector_rank=12 price=19.67 support=16.33 resistance=22.54 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=53.63 liquidity=0.0 spike=0.0
- ISMQ.CA: score=3.48 buy_ready=False sector_rank=17 price=6.58 support=5.98 resistance=7.34 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=43.46 liquidity=0.0 spike=0.0
- ISPH.CA: score=5.67 buy_ready=False sector_rank=15 price=10.17 support=9.02 resistance=10.72 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=65.38 liquidity=0.0 spike=0.0
- JUFO.CA: score=5.04 buy_ready=False sector_rank=8 price=22.0 support=21.54 resistance=25.51 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=41.5 liquidity=0.0 spike=0.0
- KABO.CA: score=6.91 buy_ready=False sector_rank=14 price=7.4 support=6.34 resistance=7.74 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=65.07 liquidity=0.0 spike=0.0
- KWIN.CA: score=16.64 buy_ready=False sector_rank=12 price=68.55 support=49.5 resistance=85.83 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.88 liquidity=8328756.82 spike=0.62
- KZPC.CA: score=-0.69 buy_ready=False sector_rank=12 price=10.61 support=10.25 resistance=14.77 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=33.54 liquidity=0.0 spike=0.0
- LCSW.CA: score=11.4 buy_ready=False sector_rank=5 price=40.44 support=31.2 resistance=42.14 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=69.38 liquidity=0.0 spike=0.0
- LUTS.CA: score=4.31 buy_ready=False sector_rank=12 price=0.66 support=0.53 resistance=0.84 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=41.92 liquidity=0.0 spike=0.0
- MAAL.CA: score=9.69 buy_ready=False sector_rank=12 price=5.94 support=5.65 resistance=7.55 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=34.3 liquidity=32343282.49 spike=1.19
- MASR.CA: score=14.31 buy_ready=False sector_rank=12 price=6.36 support=6.0 resistance=7.11 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=41.71 liquidity=24174424.11 spike=0.78
- MBSC.CA: score=11.4 buy_ready=False sector_rank=5 price=342.73 support=285.5 resistance=397.9 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=65.67 liquidity=0.0 spike=0.0
- MCQE.CA: score=9.4 buy_ready=False sector_rank=5 price=175.97 support=150.0 resistance=205.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=62.15 liquidity=0.0 spike=0.0
- MCRO.CA: score=4.31 buy_ready=False sector_rank=12 price=1.29 support=1.17 resistance=1.48 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- MENA.CA: score=20.53 buy_ready=False sector_rank=16 price=6.65 support=5.5 resistance=7.9 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=62.12 liquidity=9042696.73 spike=0.92
- MEPA.CA: score=6.31 buy_ready=False sector_rank=12 price=1.3 support=1.19 resistance=1.5 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.35 liquidity=0.0 spike=0.0
- MFPC.CA: score=-1.52 buy_ready=False sector_rank=17 price=36.6 support=36.02 resistance=47.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=33.11 liquidity=0.0 spike=0.0
- MFSC.CA: score=6.84 buy_ready=False sector_rank=12 price=34.32 support=31.02 resistance=39.48 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=56.28 liquidity=527807.28 spike=0.27
- MHOT.CA: score=9.03 buy_ready=False sector_rank=18 price=14.98 support=13.16 resistance=17.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.1 liquidity=5718884.47 spike=0.97
- MICH.CA: score=10.31 buy_ready=False sector_rank=12 price=43.29 support=39.0 resistance=48.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=63.82 liquidity=0.0 spike=0.0
- MILS.CA: score=6.31 buy_ready=False sector_rank=12 price=133.35 support=105.03 resistance=163.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=56.15 liquidity=0.0 spike=0.0
- MIPH.CA: score=6.67 buy_ready=False sector_rank=15 price=773.56 support=650.0 resistance=820.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.24 liquidity=0.0 spike=0.0
- MOED.CA: score=12.71 buy_ready=False sector_rank=12 price=0.48 support=0.41 resistance=0.54 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=55.96 liquidity=6393148.18 spike=0.48
- MOIL.CA: score=11.16 buy_ready=False sector_rank=7 price=0.68 support=0.61 resistance=0.71 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=73.02 liquidity=20485.22 spike=0.11
- MOIN.CA: score=12.56 buy_ready=False sector_rank=12 price=30.21 support=26.4 resistance=35.5 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=57.47 liquidity=5243398.49 spike=0.52
- MOSC.CA: score=12.31 buy_ready=False sector_rank=12 price=278.01 support=221.11 resistance=308.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=62.63 liquidity=0.0 spike=0.0
- MPCI.CA: score=9.31 buy_ready=False sector_rank=12 price=336.0 support=256.0 resistance=382.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=58.96 liquidity=0.0 spike=0.0
- MPCO.CA: score=6.14 buy_ready=False sector_rank=19 price=1.92 support=1.67 resistance=2.58 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=56.64 liquidity=0.0 spike=0.0
- MPRC.CA: score=18.82 buy_ready=False sector_rank=12 price=37.13 support=28.06 resistance=40.7 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=62.85 liquidity=6503356.82 spike=0.3
- MTIE.CA: score=18.95 buy_ready=False sector_rank=13 price=6.6 support=6.15 resistance=7.72 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=49.24 liquidity=160938093.67 spike=5.17
- NAHO.CA: score=4.32 buy_ready=False sector_rank=12 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=53.85 liquidity=9875.0 spike=0.93
- NCCW.CA: score=16.31 buy_ready=False sector_rank=12 price=5.3 support=4.49 resistance=6.34 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=49.36 liquidity=11443373.51 spike=0.58
- NEDA.CA: score=8.31 buy_ready=False sector_rank=12 price=2.46 support=2.26 resistance=2.54 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- NHPS.CA: score=6.31 buy_ready=False sector_rank=12 price=57.52 support=51.2 resistance=69.97 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.04 liquidity=0.0 spike=0.0
- NINH.CA: score=6.31 buy_ready=False sector_rank=12 price=15.16 support=12.92 resistance=18.5 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=53.52 liquidity=0.0 spike=0.0
- OBRI.CA: score=7.02 buy_ready=False sector_rank=12 price=21.7 support=19.91 resistance=26.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=44.51 liquidity=2704883.4 spike=0.36
- OCDI.CA: score=13.49 buy_ready=False sector_rank=16 price=23.78 support=21.6 resistance=26.64 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=51.86 liquidity=26717092.35 spike=1.0
- OCPH.CA: score=8.31 buy_ready=False sector_rank=12 price=192.87 support=153.88 resistance=224.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=59.48 liquidity=0.0 spike=0.0
- ODIN.CA: score=9.1 buy_ready=False sector_rank=12 price=2.04 support=1.81 resistance=2.28 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.9 liquidity=2787239.71 spike=0.34
- OFH.CA: score=16.29 buy_ready=False sector_rank=12 price=0.71 support=0.66 resistance=0.81 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=49.61 liquidity=9977481.89 spike=0.52
- OIH.CA: score=12.91 buy_ready=False sector_rank=21 price=1.56 support=1.46 resistance=1.84 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=44.87 liquidity=33692959.88 spike=0.82
- OLFI.CA: score=7.04 buy_ready=False sector_rank=8 price=20.38 support=18.17 resistance=21.24 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=68.37 liquidity=0.0 spike=0.0
- ORAS.CA: score=5.0 buy_ready=False sector_rank=20 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=5.49 buy_ready=False sector_rank=16 price=9.98 support=9.15 resistance=10.71 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=0.0 spike=0.0
- ORWE.CA: score=14.75 buy_ready=False sector_rank=14 price=24.7 support=22.2 resistance=26.75 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=48.8 liquidity=9840381.5 spike=0.45
- PHAR.CA: score=4.67 buy_ready=False sector_rank=15 price=101.5 support=92.11 resistance=113.97 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.27 liquidity=0.0 spike=0.0
- PHDC.CA: score=15.49 buy_ready=False sector_rank=16 price=11.5 support=10.33 resistance=12.8 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=52.41 liquidity=66798083.5 spike=0.54
- PHTV.CA: score=14.39 buy_ready=False sector_rank=12 price=335.0 support=307.0 resistance=349.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=90.05 liquidity=2896075.0 spike=2.09
- POUL.CA: score=2.04 buy_ready=False sector_rank=8 price=7.1 support=7.01 resistance=10.4 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=14.98 liquidity=0.0 spike=0.0
- PRCL.CA: score=0.4 buy_ready=False sector_rank=5 price=18.19 support=16.78 resistance=23.06 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=34.78 liquidity=0.0 spike=0.0
- PRDC.CA: score=15.49 buy_ready=False sector_rank=16 price=6.24 support=5.7 resistance=7.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=52.75 liquidity=13866209.25 spike=0.8
- PRMH.CA: score=12.47 buy_ready=False sector_rank=12 price=2.08 support=1.78 resistance=2.66 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=56.52 liquidity=6158638.49 spike=0.56
- RACC.CA: score=6.31 buy_ready=False sector_rank=12 price=7.75 support=6.9 resistance=8.55 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.26 liquidity=0.0 spike=0.0
- RAKT.CA: score=6.59 buy_ready=False sector_rank=12 price=22.47 support=20.4 resistance=23.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=87.5 liquidity=216004.1 spike=1.03
- RAYA.CA: score=21.58 buy_ready=False sector_rank=2 price=6.01 support=5.02 resistance=6.33 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=65.06 liquidity=62695450.94 spike=2.09
- RMDA.CA: score=4.67 buy_ready=False sector_rank=15 price=5.05 support=4.8 resistance=5.72 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=47.62 liquidity=0.0 spike=0.0
- ROTO.CA: score=7.1 buy_ready=False sector_rank=12 price=30.52 support=27.52 resistance=36.8 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.34 liquidity=2787879.96 spike=0.29
- RREI.CA: score=16.11 buy_ready=False sector_rank=12 price=2.61 support=2.29 resistance=3.06 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=46.73 liquidity=9797073.09 spike=0.9
- RTVC.CA: score=5.31 buy_ready=False sector_rank=12 price=3.11 support=2.66 resistance=3.15 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=97.44 liquidity=0.0 spike=0.0
- RUBX.CA: score=15.31 buy_ready=False sector_rank=12 price=12.5 support=11.59 resistance=15.98 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=47.33 liquidity=21839262.5 spike=0.46
- SAUD.CA: score=15.48 buy_ready=False sector_rank=9 price=22.26 support=19.3 resistance=24.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=67.65 liquidity=4499502.89 spike=0.21
- SCEM.CA: score=11.4 buy_ready=False sector_rank=5 price=98.63 support=77.01 resistance=106.55 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=69.63 liquidity=0.0 spike=0.0
- SCFM.CA: score=8.31 buy_ready=False sector_rank=12 price=215.95 support=168.5 resistance=240.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=55.65 liquidity=0.0 spike=0.0
- SCTS.CA: score=1.3 buy_ready=False sector_rank=6 price=456.84 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=34.41 liquidity=902258.99 spike=0.23
- SDTI.CA: score=20.31 buy_ready=False sector_rank=12 price=85.01 support=79.5 resistance=90.99 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=47.0 liquidity=16238440.59 spike=0.84
- SEIG.CA: score=1.63 buy_ready=False sector_rank=12 price=215.93 support=149.57 resistance=280.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=21.06 liquidity=1320195.98 spike=0.12
- SIPC.CA: score=5.31 buy_ready=False sector_rank=12 price=4.94 support=4.11 resistance=5.89 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=56.32 liquidity=0.0 spike=0.0
- SKPC.CA: score=3.48 buy_ready=False sector_rank=17 price=14.18 support=13.85 resistance=15.46 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=44.2 liquidity=0.0 spike=0.0
- SMFR.CA: score=11.61 buy_ready=False sector_rank=12 price=212.18 support=169.0 resistance=264.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=61.92 liquidity=2295999.7 spike=0.29
- SNFC.CA: score=10.31 buy_ready=False sector_rank=12 price=11.21 support=10.15 resistance=11.48 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=69.93 liquidity=0.0 spike=0.0
- SPIN.CA: score=3.91 buy_ready=False sector_rank=14 price=14.28 support=13.3 resistance=16.48 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=47.48 liquidity=0.0 spike=0.0
- SPMD.CA: score=4.31 buy_ready=False sector_rank=12 price=0.32 support=0.31 resistance=0.37 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=41.84 liquidity=0.0 spike=0.0
- SUGR.CA: score=13.04 buy_ready=False sector_rank=8 price=51.46 support=46.5 resistance=55.99 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=64.3 liquidity=0.0 spike=0.0
- SVCE.CA: score=6.31 buy_ready=False sector_rank=12 price=8.73 support=7.97 resistance=10.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=55.65 liquidity=0.0 spike=0.0
- SWDY.CA: score=8.35 buy_ready=False sector_rank=11 price=116.99 support=103.4 resistance=123.45 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=65.79 liquidity=0.0 spike=0.0
- TALM.CA: score=21.33 buy_ready=False sector_rank=6 price=20.52 support=17.9 resistance=21.5 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=66.04 liquidity=9934183.66 spike=0.57
- TMGH.CA: score=14.21 buy_ready=False sector_rank=16 price=78.06 support=76.5 resistance=86.48 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=44.59 liquidity=289315408.21 spike=1.36
- TRTO.CA: score=5.31 buy_ready=False sector_rank=12 price=0.06 support=0.05 resistance=0.06 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=303.0 spike=0.08
- UEFM.CA: score=10.31 buy_ready=False sector_rank=12 price=496.27 support=422.11 resistance=540.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=69.67 liquidity=0.0 spike=0.0
- UEGC.CA: score=14.31 buy_ready=False sector_rank=12 price=1.42 support=1.3 resistance=1.59 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=16093210.25 spike=0.58
- UNIP.CA: score=10.77 buy_ready=False sector_rank=12 price=0.3 support=0.27 resistance=0.33 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=58.49 liquidity=4461193.98 spike=0.73
- UNIT.CA: score=-0.51 buy_ready=False sector_rank=16 price=15.0 support=14.16 resistance=19.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=28.22 liquidity=0.0 spike=0.0
- WCDF.CA: score=6.31 buy_ready=False sector_rank=12 price=501.26 support=470.0 resistance=565.0 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=54.01 liquidity=0.0 spike=0.0
- WKOL.CA: score=9.61 buy_ready=False sector_rank=12 price=164.35 support=150.01 resistance=194.85 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=49.41 liquidity=3293245.42 spike=0.32
- ZEOT.CA: score=10.31 buy_ready=False sector_rank=12 price=12.36 support=9.58 resistance=13.9 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=68.38 liquidity=0.0 spike=0.0
- ZMID.CA: score=14.87 buy_ready=False sector_rank=16 price=6.23 support=6.05 resistance=7.2 source=Yahoo Finance as_of=2026-11-23T22:00:00+00:00 freshness=FRESH RSI=38.71 liquidity=141293758.91 spike=1.69

## Backtesting Lite
- GRCA.CA: 180d return=-21.39%, max drawdown=-71.34%, MA20>MA50 days last20=0, as_of=2026-11-23T22:00:00+00:00
- HRHO.CA: 180d return=-2.18%, max drawdown=-24.55%, MA20>MA50 days last20=0, as_of=2026-11-23T22:00:00+00:00
- CIRA.CA: 180d return=125.91%, max drawdown=-19.1%, MA20>MA50 days last20=0, as_of=2026-11-23T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GRCA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Grand Capital for Financial Investments summary=Evidence rejected for GRCA.CA: source text did not clearly match GRCA.CA / Grand Capital for Financial Investments.
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- CIRA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Cairo Investment and Real Estate Development summary=Evidence rejected for CIRA.CA: source text did not clearly match CIRA.CA / Cairo Investment and Real Estate Development.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ENGC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Industrial Engineering Company for Construction and Development (ICON) (S.A.E) summary=Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- CSAG.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Canal Shipping Agencies summary=Evidence rejected for CSAG.CA: source text did not clearly match CSAG.CA / Canal Shipping Agencies.
- COPR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Copper for Commercial Investment & Real Estate Development summary=Evidence rejected for COPR.CA: source text did not clearly match COPR.CA / Copper for Commercial Investment & Real Estate Development.
- RAYA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Raya Holding summary=Evidence rejected for RAYA.CA: source text did not clearly match RAYA.CA / Raya Holding.

## Warnings
- OpenRouter API error: 404
- Mubasher stock page returned no evidence titles for GRCA.CA.
- No Yahoo or Mubasher evidence found for GRCA.CA.
- Evidence rejected for GRCA.CA: source text did not clearly match GRCA.CA / Grand Capital for Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock page returned no evidence titles for HRHO.CA.
- No Yahoo or Mubasher evidence found for HRHO.CA.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Mubasher stock page returned no evidence titles for CIRA.CA.
- No Yahoo or Mubasher evidence found for CIRA.CA.
- Evidence rejected for CIRA.CA: source text did not clearly match CIRA.CA / Cairo Investment and Real Estate Development.
- Mubasher stock page returned no evidence titles for EFIH.CA.
- No Yahoo or Mubasher evidence found for EFIH.CA.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Mubasher stock page returned no evidence titles for ENGC.CA.
- No Yahoo or Mubasher evidence found for ENGC.CA.
- Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- Mubasher stock page returned no evidence titles for CSAG.CA.
- No Yahoo or Mubasher evidence found for CSAG.CA.
- Evidence rejected for CSAG.CA: source text did not clearly match CSAG.CA / Canal Shipping Agencies.
- Mubasher stock page returned no evidence titles for COPR.CA.
- No Yahoo or Mubasher evidence found for COPR.CA.
- Evidence rejected for COPR.CA: source text did not clearly match COPR.CA / Copper for Commercial Investment & Real Estate Development.
- Mubasher stock page returned no evidence titles for RAYA.CA.
- No Yahoo or Mubasher evidence found for RAYA.CA.
- Evidence rejected for RAYA.CA: source text did not clearly match RAYA.CA / Raya Holding.
