# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-17T12:16:35.164421+00:00
Generated Cairo: 2026-06-17 15:16
Run timing: target 11:00 Cairo | generated Cairo 2026-06-17 15:16 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-17 15:13

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 180/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, June 17
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 45.0% / above MA50 60.0%
- EGX70 regime: MIXED / above MA20 53.85% / above MA50 76.92%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=1339123328.0 spike=2.2 score=25.66
- TMGH.CA: liquidity=1297745536.0 spike=2.84 score=25.01
- PHDC.CA: liquidity=603275200.0 spike=1.45 score=22.23
- CCAP.CA: liquidity=524366528.0 spike=0.61 score=17.98
- EMFD.CA: liquidity=398893952.0 spike=1.44 score=24.21

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlights several high‑rank stocks (MTIE, MASR, HDBK, COMI, TMGH, etc.) that show bullish watch outlooks, solid liquidity spikes and price near support or modestly below resistance. However, the overall EGX30/EGX70 regime is mixed with weak breadth (14.29%) and recent negative 5‑day returns, prompting a defensive risk mode that blocks new buys until sector breadth improves.
- Sector breadth is too weak, so the system stays in DEFENSIVE_NO_NEW_BUY despite individual bullish signals.
- Liquidity spikes (e.g., MASR 2.64×, COMI 2.2×) and support levels within 5‑6% suggest short‑term stability for the highlighted tickets.
- Automotive & Distribution leads sector scores, but EGX30/EGX70 mixed trends and sub‑MA20 breadth keep overall risk elevated.
- Outlook remains bullish for the top tickets over the next 1‑3 days, yet uncertainty from market‑wide negative returns could reverse momentum.

## Top Liquidity Spikes
- KWIN.CA: spike=31.94 liquidity=155374736.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CICH.CA: spike=25.23 liquidity=80484400.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=16.3 liquidity=270097952.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DOMT.CA: spike=13.15 liquidity=25355412.0 outlook=CONSTRUCTIVE score=66.47 buy_ready=False
- ECAP.CA: spike=10.97 liquidity=56869484.0 outlook=BULLISH_WATCH score=71.76 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=9.35 5d=1.59% 20d=4.33% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=7.1 5d=3.53% 20d=8.18% aboveMA50=50.0%
- #3 Education: score=5.95 5d=-0.75% 20d=-1.72% aboveMA50=100.0%
- #4 Real Estate: score=5.82 5d=-1.03% 20d=2.03% aboveMA50=84.62%
- #5 Banking & Financials: score=5.66 5d=0.21% 20d=1.05% aboveMA50=80.0%
- #6 Food, Beverages & Tobacco: score=5.47 5d=-0.85% 20d=1.9% aboveMA50=85.71%
- #7 General / Verified EGX Expansion: score=4.76 5d=-0.4% 20d=0.17% aboveMA50=68.27%
- #8 Textiles: score=4.58 5d=-2.5% 20d=4.93% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- HDBK.CA: BULLISH_WATCH score=94.66 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MASR.CA: BULLISH_WATCH score=93.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- TMGH.CA: BULLISH_WATCH score=92.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CANA.CA: BULLISH_WATCH score=92.66 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MOSC.CA: BULLISH_WATCH score=91.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CIRA.CA: BULLISH_WATCH score=90.95 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- COPR.CA: BULLISH_WATCH score=86.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- COMI.CA: BULLISH_WATCH score=86.66 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- IDRE.CA: BULLISH_WATCH score=85.76 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=13.09 buy_ready=False sector_rank=7 price=205.82 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.01 liquidity=2184834.5 spike=0.33
- ABUK.CA: score=9.54 buy_ready=False sector_rank=21 price=70.5 support=71.06 resistance=90.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.08 liquidity=200255888.0 spike=1.44
- ACAMD.CA: score=20.9 buy_ready=False sector_rank=7 price=2.39 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=82733272.0 spike=0.66
- ACGC.CA: score=18.83 buy_ready=False sector_rank=8 price=9.5 support=9.02 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=21430926.0 spike=0.37
- ADCI.CA: score=20.54 buy_ready=False sector_rank=7 price=227.4 support=205.1 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=68.7 liquidity=12401237.0 spike=1.82
- ADIB.CA: score=19.26 buy_ready=False sector_rank=5 price=46.82 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=63889604.0 spike=0.57
- ADPC.CA: score=14.54 buy_ready=False sector_rank=7 price=3.63 support=3.45 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8634279.0 spike=0.34
- AFDI.CA: score=12.94 buy_ready=False sector_rank=7 price=42.49 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=4040581.0 spike=0.25
- AFMC.CA: score=9.71 buy_ready=False sector_rank=7 price=71.18 support=67.0 resistance=77.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=804695.5 spike=0.14
- AJWA.CA: score=22.74 buy_ready=False sector_rank=7 price=184.84 support=130.01 resistance=188.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=93.13 liquidity=62815116.0 spike=2.42
- ALCN.CA: score=13.41 buy_ready=False sector_rank=12 price=28.56 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=7977539.5 spike=0.54
- ALUM.CA: score=15.04 buy_ready=False sector_rank=7 price=23.08 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=6132988.5 spike=0.38
- AMER.CA: score=19.33 buy_ready=False sector_rank=4 price=2.52 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=79089832.0 spike=0.78
- AMES.CA: score=4.81 buy_ready=False sector_rank=7 price=48.76 support=48.0 resistance=55.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=1910813.0 spike=0.48
- AMIA.CA: score=19.54 buy_ready=False sector_rank=7 price=9.05 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=20715748.0 spike=1.32
- AMOC.CA: score=10.7 buy_ready=False sector_rank=11 price=7.79 support=7.71 resistance=8.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=30321438.0 spike=0.41
- ANFI.CA: score=24.9 buy_ready=False sector_rank=7 price=34.5 support=13.73 resistance=34.5 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=97.65 liquidity=273902676.0 spike=4.23
- APSW.CA: score=4.24 buy_ready=False sector_rank=7 price=8.53 support=8.24 resistance=9.38 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=28.92 liquidity=1735957.31 spike=2.3
- ARAB.CA: score=19.33 buy_ready=False sector_rank=4 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=55222760.0 spike=0.64
- ARCC.CA: score=18.1 buy_ready=False sector_rank=15 price=56.16 support=53.6 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.97 liquidity=16159014.0 spike=0.45
- AREH.CA: score=18.68 buy_ready=False sector_rank=7 price=1.61 support=1.27 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.07 liquidity=38848984.0 spike=1.39
- ARVA.CA: score=22.16 buy_ready=False sector_rank=7 price=10.8 support=7.71 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.75 liquidity=49111648.0 spike=1.63
- ASCM.CA: score=20.9 buy_ready=False sector_rank=7 price=59.58 support=47.3 resistance=64.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=73.67 liquidity=50199344.0 spike=0.73
- ASPI.CA: score=20.9 buy_ready=False sector_rank=7 price=0.31 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=26721470.0 spike=0.39
- ATLC.CA: score=16.42 buy_ready=False sector_rank=10 price=5.18 support=4.7 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=3712877.0 spike=0.85
- ATQA.CA: score=12.66 buy_ready=False sector_rank=21 price=9.62 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=20752344.0 spike=0.6
- AXPH.CA: score=5.5 buy_ready=False sector_rank=7 price=1095.04 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.66 liquidity=1600012.0 spike=0.84
- BINV.CA: score=19.35 buy_ready=False sector_rank=16 price=47.99 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=7374386.0 spike=0.68
- BIOC.CA: score=9.64 buy_ready=False sector_rank=7 price=71.36 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=48.88 liquidity=735040.5 spike=0.26
- BTFH.CA: score=14.71 buy_ready=False sector_rank=10 price=2.99 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=140590560.0 spike=0.68
- CAED.CA: score=22.94 buy_ready=False sector_rank=7 price=73.31 support=67.21 resistance=79.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=11329637.0 spike=2.02
- CANA.CA: score=24.9 buy_ready=False sector_rank=5 price=37.91 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=19067326.0 spike=1.82
- CCAP.CA: score=17.98 buy_ready=False sector_rank=16 price=5.02 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=524366528.0 spike=0.61
- CCRS.CA: score=20.9 buy_ready=False sector_rank=7 price=2.47 support=2.27 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=17638946.0 spike=0.74
- CEFM.CA: score=7.01 buy_ready=False sector_rank=7 price=102.1 support=100.53 resistance=115.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.26 liquidity=1107382.13 spike=0.31
- CERA.CA: score=23.9 buy_ready=False sector_rank=7 price=1.26 support=1.13 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=74549032.0 spike=4.43
- CFGH.CA: score=-0.09 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=6144.56 spike=0.95
- CICH.CA: score=10.71 buy_ready=False sector_rank=10 price=12.49 support=11.54 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80484400.0 spike=25.23
- CIEB.CA: score=17.88 buy_ready=False sector_rank=5 price=23.82 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=5620819.5 spike=0.8
- CIRA.CA: score=22.78 buy_ready=False sector_rank=3 price=27.0 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.95 liquidity=18650382.0 spike=1.2
- CLHO.CA: score=19.93 buy_ready=False sector_rank=18 price=15.57 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.73 liquidity=24259842.0 spike=0.86
- CNFN.CA: score=18.15 buy_ready=False sector_rank=10 price=4.53 support=4.36 resistance=4.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.43 liquidity=18377512.0 spike=1.22
- COMI.CA: score=25.66 buy_ready=False sector_rank=5 price=136.18 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=1339123328.0 spike=2.2
- COPR.CA: score=21.64 buy_ready=False sector_rank=7 price=0.38 support=0.34 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.85 liquidity=78333688.0 spike=1.87
- COSG.CA: score=20.9 buy_ready=False sector_rank=7 price=1.6 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=43893048.0 spike=0.63
- CPCI.CA: score=11.71 buy_ready=False sector_rank=7 price=368.07 support=345.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=71.29 liquidity=2507020.0 spike=1.15
- CSAG.CA: score=16.58 buy_ready=False sector_rank=12 price=31.35 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.66 liquidity=6145104.0 spike=0.47
- DAPH.CA: score=15.34 buy_ready=False sector_rank=7 price=81.11 support=76.6 resistance=86.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=7437407.5 spike=0.66
- DEIN.CA: score=6.9 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=21.19 buy_ready=False sector_rank=6 price=25.63 support=23.7 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.71 liquidity=25355412.0 spike=13.15
- DSCW.CA: score=20.9 buy_ready=False sector_rank=7 price=1.84 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=43945588.0 spike=0.83
- DTPP.CA: score=1.36 buy_ready=False sector_rank=7 price=116.54 support=114.0 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=16.62 liquidity=458959.16 spike=0.24
- EALR.CA: score=10.12 buy_ready=False sector_rank=7 price=355.81 support=346.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=1220494.25 spike=0.33
- EASB.CA: score=10.9 buy_ready=False sector_rank=7 price=8.5 support=7.33 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46937780.0 spike=10.56
- EAST.CA: score=23.19 buy_ready=False sector_rank=6 price=39.1 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=43579132.0 spike=0.64
- EBSC.CA: score=11.96 buy_ready=False sector_rank=7 price=1.9 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=70.91 liquidity=1056277.88 spike=0.39
- ECAP.CA: score=24.9 buy_ready=False sector_rank=7 price=33.49 support=28.7 resistance=32.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.18 liquidity=56869484.0 spike=10.97
- EDFM.CA: score=12.6 buy_ready=False sector_rank=7 price=331.68 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=52.43 liquidity=1255408.77 spike=2.22
- EEII.CA: score=20.13 buy_ready=False sector_rank=7 price=2.43 support=2.27 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=9229679.0 spike=0.51
- EFIC.CA: score=-1.95 buy_ready=False sector_rank=21 price=203.26 support=192.01 resistance=218.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=23.12 liquidity=386268.22 spike=0.16
- EFID.CA: score=19.19 buy_ready=False sector_rank=6 price=28.26 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=37890600.0 spike=0.51
- EFIH.CA: score=18.8 buy_ready=False sector_rank=17 price=21.4 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=74439816.0 spike=1.41
- EGAL.CA: score=8.66 buy_ready=False sector_rank=21 price=298.3 support=297.1 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=34029720.0 spike=0.43
- EGAS.CA: score=16.05 buy_ready=False sector_rank=11 price=51.93 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=5353922.5 spike=0.43
- EGBE.CA: score=9.29 buy_ready=False sector_rank=5 price=0.44 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.02 liquidity=28478.24 spike=0.26
- EGCH.CA: score=16.66 buy_ready=False sector_rank=21 price=13.68 support=12.9 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=43516344.0 spike=0.47
- EGSA.CA: score=3.21 buy_ready=False sector_rank=14 price=8.78 support=8.44 resistance=9.19 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=26.47 liquidity=12906.6 spike=0.93
- EGTS.CA: score=19.33 buy_ready=False sector_rank=4 price=18.21 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.85 liquidity=50602268.0 spike=0.4
- EHDR.CA: score=20.9 buy_ready=False sector_rank=7 price=2.7 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=25596596.0 spike=0.44
- EKHO.CA: score=10.7 buy_ready=False sector_rank=11 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=16.29 buy_ready=False sector_rank=13 price=2.13 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=13176711.0 spike=0.5
- ELKA.CA: score=22.46 buy_ready=False sector_rank=7 price=1.32 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=52212176.0 spike=1.28
- ELNA.CA: score=13.24 buy_ready=False sector_rank=7 price=39.45 support=37.11 resistance=41.51 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.98 liquidity=592144.51 spike=1.87
- ELSH.CA: score=17.9 buy_ready=False sector_rank=7 price=13.22 support=8.11 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.56 liquidity=165717824.0 spike=0.89
- ELWA.CA: score=9.52 buy_ready=False sector_rank=7 price=2.02 support=1.79 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=619048.63 spike=0.2
- EMFD.CA: score=24.21 buy_ready=False sector_rank=4 price=12.5 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.01 liquidity=398893952.0 spike=1.44
- ENGC.CA: score=24.34 buy_ready=False sector_rank=7 price=36.97 support=32.31 resistance=36.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=37886776.0 spike=2.72
- EOSB.CA: score=16.83 buy_ready=False sector_rank=7 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=229601.28 spike=1.85
- EPCO.CA: score=23.32 buy_ready=False sector_rank=7 price=9.27 support=8.56 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=8418998.0 spike=0.77
- EPPK.CA: score=11.87 buy_ready=False sector_rank=7 price=12.64 support=11.67 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=967448.25 spike=0.88
- ETEL.CA: score=10.38 buy_ready=False sector_rank=14 price=93.01 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.31 liquidity=89018736.0 spike=1.09
- ETRS.CA: score=17.9 buy_ready=False sector_rank=7 price=10.29 support=7.37 resistance=10.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=76.02 liquidity=49274112.0 spike=0.8
- EXPA.CA: score=20.06 buy_ready=False sector_rank=5 price=18.3 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=48760400.0 spike=1.4
- FAIT.CA: score=14.01 buy_ready=False sector_rank=5 price=37.51 support=35.01 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=49.14 liquidity=2742209.5 spike=0.57
- FAITA.CA: score=9.62 buy_ready=False sector_rank=5 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=52566.55 spike=1.15
- FERC.CA: score=1.34 buy_ready=False sector_rank=21 price=75.03 support=75.0 resistance=79.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.38 liquidity=3680657.75 spike=0.91
- FWRY.CA: score=9.98 buy_ready=False sector_rank=17 price=18.93 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=173812304.0 spike=0.59
- GBCO.CA: score=24.4 buy_ready=False sector_rank=1 price=28.61 support=25.25 resistance=28.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.73 liquidity=89001560.0 spike=0.82
- GDWA.CA: score=21.9 buy_ready=False sector_rank=7 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.94 liquidity=14053784.0 spike=1.0
- GGCC.CA: score=15.31 buy_ready=False sector_rank=7 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.38 liquidity=5402246.5 spike=0.7
- GIHD.CA: score=12.7 buy_ready=False sector_rank=7 price=40.83 support=35.15 resistance=43.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=1800815.63 spike=0.51
- GMCI.CA: score=13.85 buy_ready=False sector_rank=7 price=1.77 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=509569.81 spike=1.22
- GRCA.CA: score=5.09 buy_ready=False sector_rank=7 price=54.62 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.47 liquidity=4187275.25 spike=0.69
- GSSC.CA: score=3.82 buy_ready=False sector_rank=7 price=248.0 support=228.1 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.11 liquidity=2914378.75 spike=0.59
- GTWL.CA: score=15.47 buy_ready=False sector_rank=7 price=48.78 support=45.47 resistance=55.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=4568902.5 spike=0.6
- HDBK.CA: score=25.76 buy_ready=False sector_rank=5 price=145.42 support=138.0 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=59.06 liquidity=20146002.0 spike=1.25
- HELI.CA: score=22.27 buy_ready=False sector_rank=4 price=6.57 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.83 liquidity=218835392.0 spike=1.47
- HRHO.CA: score=24.71 buy_ready=False sector_rank=10 price=27.58 support=25.8 resistance=27.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.13 liquidity=75999232.0 spike=0.51
- ICID.CA: score=19.9 buy_ready=False sector_rank=7 price=7.44 support=4.5 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=86.6 liquidity=13201654.0 spike=0.81
- IDRE.CA: score=20.9 buy_ready=False sector_rank=7 price=44.39 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=18331326.0 spike=0.81
- IFAP.CA: score=12.27 buy_ready=False sector_rank=2 price=19.25 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.91 liquidity=4867539.5 spike=0.64
- INFI.CA: score=9.69 buy_ready=False sector_rank=7 price=96.78 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.9 liquidity=9787726.0 spike=0.99
- IRON.CA: score=10.35 buy_ready=False sector_rank=21 price=32.48 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.32 liquidity=5685264.5 spike=0.71
- ISMA.CA: score=15.9 buy_ready=False sector_rank=7 price=30.67 support=23.6 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.54 liquidity=31319276.0 spike=0.73
- ISMQ.CA: score=20.9 buy_ready=False sector_rank=21 price=8.06 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=79053120.0 spike=1.12
- ISPH.CA: score=19.93 buy_ready=False sector_rank=18 price=12.06 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.28 liquidity=44206540.0 spike=0.35
- JUFO.CA: score=21.19 buy_ready=False sector_rank=6 price=31.32 support=26.51 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.55 liquidity=29766512.0 spike=0.76
- KABO.CA: score=20.83 buy_ready=False sector_rank=8 price=6.3 support=5.94 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=10295267.0 spike=0.52
- KWIN.CA: score=10.9 buy_ready=False sector_rank=7 price=78.18 support=73.1 resistance=88.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=155374736.0 spike=31.94
- KZPC.CA: score=13.41 buy_ready=False sector_rank=7 price=10.57 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.42 liquidity=2503804.25 spike=0.29
- LCSW.CA: score=22.06 buy_ready=False sector_rank=15 price=27.83 support=26.0 resistance=28.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.74 liquidity=17375918.0 spike=1.98
- LUTS.CA: score=17.9 buy_ready=False sector_rank=7 price=0.72 support=0.54 resistance=0.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=83.88 liquidity=33774112.0 spike=0.97
- MAAL.CA: score=7.1 buy_ready=False sector_rank=7 price=6.69 support=6.28 resistance=6.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22245010.0 spike=1.6
- MASR.CA: score=26.18 buy_ready=False sector_rank=7 price=7.44 support=6.54 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=150110880.0 spike=2.64
- MBSC.CA: score=18.1 buy_ready=False sector_rank=15 price=252.01 support=247.43 resistance=273.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.2 liquidity=33107214.0 spike=0.75
- MCQE.CA: score=10.1 buy_ready=False sector_rank=15 price=177.79 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.31 liquidity=10166852.0 spike=0.62
- MCRO.CA: score=18.04 buy_ready=False sector_rank=7 price=1.24 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=51301924.0 spike=1.07
- MENA.CA: score=21.33 buy_ready=False sector_rank=4 price=6.87 support=6.12 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=13428929.0 spike=0.78
- MEPA.CA: score=20.9 buy_ready=False sector_rank=7 price=1.72 support=1.63 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=12291116.0 spike=0.71
- MFPC.CA: score=9.44 buy_ready=False sector_rank=21 price=36.7 support=36.9 resistance=45.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.77 liquidity=121619944.0 spike=1.39
- MFSC.CA: score=5.9 buy_ready=False sector_rank=7 price=44.19 support=43.0 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.46 liquidity=1992563.0 spike=0.16
- MHOT.CA: score=18.79 buy_ready=False sector_rank=9 price=30.11 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=11636875.0 spike=0.53
- MICH.CA: score=22.01 buy_ready=False sector_rank=7 price=37.69 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=9110025.0 spike=0.62
- MILS.CA: score=20.9 buy_ready=False sector_rank=7 price=139.0 support=127.01 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=10749415.0 spike=0.54
- MIPH.CA: score=4.82 buy_ready=False sector_rank=18 price=700.01 support=660.0 resistance=701.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6272197.5 spike=2.81
- MOED.CA: score=16.29 buy_ready=False sector_rank=7 price=0.7 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=9382447.0 spike=0.75
- MOIL.CA: score=11.1 buy_ready=False sector_rank=11 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=181219.53 spike=1.11
- MOIN.CA: score=0.84 buy_ready=False sector_rank=7 price=24.25 support=24.1 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=21.12 liquidity=936742.88 spike=0.55
- MOSC.CA: score=23.36 buy_ready=False sector_rank=7 price=282.08 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.26 liquidity=20755114.0 spike=2.23
- MPCI.CA: score=21.24 buy_ready=False sector_rank=7 price=223.92 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.21 liquidity=92846256.0 spike=1.17
- MPCO.CA: score=23.4 buy_ready=False sector_rank=2 price=1.95 support=1.54 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=75264744.0 spike=0.76
- MPRC.CA: score=18.9 buy_ready=False sector_rank=7 price=31.99 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=10808075.0 spike=0.54
- MTIE.CA: score=27.68 buy_ready=False sector_rank=1 price=9.11 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=29639586.0 spike=1.64
- NAHO.CA: score=4.9 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=669.5 spike=0.02
- NCCW.CA: score=20.9 buy_ready=False sector_rank=7 price=6.21 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.02 liquidity=18065264.0 spike=0.65
- NEDA.CA: score=11.3 buy_ready=False sector_rank=7 price=2.77 support=2.65 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=393751.94 spike=0.8
- NHPS.CA: score=14.86 buy_ready=False sector_rank=7 price=68.96 support=65.03 resistance=72.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=4791192.5 spike=1.08
- NINH.CA: score=9.98 buy_ready=False sector_rank=7 price=17.62 support=16.8 resistance=19.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=1078861.0 spike=0.22
- NIPH.CA: score=17.93 buy_ready=False sector_rank=18 price=161.52 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=21866362.0 spike=0.27
- OBRI.CA: score=19.55 buy_ready=False sector_rank=7 price=35.93 support=33.63 resistance=37.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=9649744.0 spike=0.71
- OCDI.CA: score=18.33 buy_ready=False sector_rank=4 price=21.3 support=20.0 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=28879424.0 spike=0.85
- OCPH.CA: score=11.71 buy_ready=False sector_rank=7 price=340.0 support=337.0 resistance=379.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.79 liquidity=9529612.0 spike=1.64
- ODIN.CA: score=20.59 buy_ready=False sector_rank=7 price=2.19 support=1.89 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=7690339.0 spike=0.71
- OFH.CA: score=15.9 buy_ready=False sector_rank=7 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=13944159.0 spike=0.6
- OIH.CA: score=9.98 buy_ready=False sector_rank=16 price=1.38 support=1.33 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=28248734.0 spike=0.32
- OLFI.CA: score=23.85 buy_ready=False sector_rank=6 price=22.07 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=26482302.0 spike=1.33
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=796.99 support=785.01 resistance=799.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=385997408.0 spike=1.0
- ORHD.CA: score=21.33 buy_ready=False sector_rank=4 price=38.19 support=33.51 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.64 liquidity=146972608.0 spike=0.81
- ORWE.CA: score=20.83 buy_ready=False sector_rank=8 price=23.48 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=25333338.0 spike=0.61
- PHAR.CA: score=11.12 buy_ready=False sector_rank=18 price=84.2 support=83.02 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.88 liquidity=6188266.0 spike=0.22
- PHDC.CA: score=22.23 buy_ready=False sector_rank=4 price=16.21 support=13.4 resistance=16.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=603275200.0 spike=1.45
- PHTV.CA: score=24.59 buy_ready=False sector_rank=7 price=220.02 support=201.55 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.1 liquidity=9689227.0 spike=0.58
- POUL.CA: score=17.35 buy_ready=False sector_rank=6 price=35.45 support=34.8 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=56894384.0 spike=1.58
- PRCL.CA: score=20.88 buy_ready=False sector_rank=15 price=25.56 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.78 liquidity=38955476.0 spike=1.39
- PRDC.CA: score=8.29 buy_ready=False sector_rank=4 price=8.7 support=7.72 resistance=8.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=194895824.0 spike=1.98
- PRMH.CA: score=21.78 buy_ready=False sector_rank=7 price=2.78 support=2.21 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.63 liquidity=38085920.0 spike=1.44
- RACC.CA: score=7.0 buy_ready=False sector_rank=7 price=9.79 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=26.88 liquidity=3095099.25 spike=0.3
- RAKT.CA: score=7.4 buy_ready=False sector_rank=7 price=23.03 support=22.0 resistance=24.75 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=48.94 liquidity=520846.5 spike=1.99
- RAYA.CA: score=12.7 buy_ready=False sector_rank=20 price=7.3 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.59 liquidity=107032032.0 spike=1.13
- RMDA.CA: score=17.93 buy_ready=False sector_rank=18 price=5.05 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.66 liquidity=23710108.0 spike=0.28
- ROTO.CA: score=10.9 buy_ready=False sector_rank=7 price=42.64 support=35.7 resistance=42.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=143452864.0 spike=10.62
- RREI.CA: score=21.0 buy_ready=False sector_rank=7 price=3.7 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=22401034.0 spike=1.05
- RTVC.CA: score=10.67 buy_ready=False sector_rank=7 price=3.84 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=4761945.0 spike=0.85
- RUBX.CA: score=9.57 buy_ready=False sector_rank=7 price=9.92 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=4665425.0 spike=0.41
- SAUD.CA: score=13.4 buy_ready=False sector_rank=5 price=22.04 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.8 liquidity=7132540.5 spike=0.65
- SCEM.CA: score=15.1 buy_ready=False sector_rank=15 price=61.91 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=13785382.0 spike=0.63
- SCFM.CA: score=3.41 buy_ready=False sector_rank=7 price=250.6 support=248.1 resistance=296.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=2506754.25 spike=0.21
- SCTS.CA: score=8.14 buy_ready=False sector_rank=3 price=599.53 support=565.25 resistance=668.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=2761557.0 spike=0.52
- SDTI.CA: score=22.9 buy_ready=False sector_rank=7 price=47.98 support=43.4 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=13291878.0 spike=0.91
- SEIG.CA: score=14.18 buy_ready=False sector_rank=7 price=183.21 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=3273254.5 spike=0.69
- SIPC.CA: score=13.61 buy_ready=False sector_rank=7 price=3.5 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=7705216.5 spike=0.61
- SKPC.CA: score=7.66 buy_ready=False sector_rank=21 price=16.18 support=16.16 resistance=17.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.46 liquidity=21915670.0 spike=0.42
- SMFR.CA: score=6.86 buy_ready=False sector_rank=7 price=203.62 support=192.0 resistance=218.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=42.73 liquidity=958278.0 spike=0.23
- SNFC.CA: score=18.9 buy_ready=False sector_rank=7 price=12.27 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.98 liquidity=15208547.0 spike=0.58
- SPIN.CA: score=13.47 buy_ready=False sector_rank=8 price=14.0 support=13.3 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=10645266.0 spike=2.32
- SPMD.CA: score=10.9 buy_ready=False sector_rank=7 price=0.45 support=0.42 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=133983936.0 spike=5.67
- SUGR.CA: score=14.02 buy_ready=False sector_rank=6 price=48.82 support=48.0 resistance=51.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=4830756.5 spike=0.32
- SVCE.CA: score=21.66 buy_ready=False sector_rank=7 price=9.4 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=126085048.0 spike=1.38
- SWDY.CA: score=14.79 buy_ready=False sector_rank=13 price=86.75 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=6501753.0 spike=0.33
- TALM.CA: score=19.94 buy_ready=False sector_rank=3 price=15.96 support=15.12 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=77.6 liquidity=8441467.0 spike=1.06
- TMGH.CA: score=25.01 buy_ready=False sector_rank=4 price=96.86 support=92.91 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=1297745536.0 spike=2.84
- TRTO.CA: score=6.9 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=10.32 buy_ready=False sector_rank=7 price=470.05 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=48.69 liquidity=1557998.75 spike=1.93
- UEGC.CA: score=22.9 buy_ready=False sector_rank=7 price=1.46 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=12482279.0 spike=0.49
- UNIP.CA: score=19.9 buy_ready=False sector_rank=7 price=0.33 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=85.92 liquidity=20961134.0 spike=0.88
- UNIT.CA: score=13.99 buy_ready=False sector_rank=4 price=13.82 support=12.25 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=58.26 liquidity=2665437.75 spike=0.34
- WCDF.CA: score=6.26 buy_ready=False sector_rank=7 price=531.95 support=450.0 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=45.74 liquidity=355234.47 spike=0.97
- WKOL.CA: score=8.23 buy_ready=False sector_rank=7 price=287.66 support=289.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=2321979.0 spike=0.69
- ZEOT.CA: score=10.9 buy_ready=False sector_rank=7 price=12.03 support=11.0 resistance=13.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=270097952.0 spike=16.3
- ZMID.CA: score=21.33 buy_ready=False sector_rank=4 price=6.21 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=142249632.0 spike=0.67

## Backtesting Lite
- MTIE.CA: 180d return=40.36%, max drawdown=-20.49%, MA20>MA50 days last20=20, as_of=2026-06-15T21:00:00+00:00
- MASR.CA: 180d return=80.16%, max drawdown=-11.03%, MA20>MA50 days last20=20, as_of=2026-06-15T21:00:00+00:00
- HDBK.CA: 180d return=134.47%, max drawdown=-12.66%, MA20>MA50 days last20=15, as_of=2026-06-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=532 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- TMGH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talaat Moustafa Group Holding summary=Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- ECAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Ezz Ceramics & Porcelain Co. summary=Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=532 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.

## Warnings
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
