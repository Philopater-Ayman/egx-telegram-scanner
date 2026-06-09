# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-06-09T18:32:27.411749+00:00
Generated Cairo: 2026-06-09 21:32
Run timing: target 19:30 Cairo | generated Cairo 2026-06-09 21:32 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-06-09 21:28

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 181/190
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 09
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.0% / above MA50 70.0%
- EGX70 regime: MIXED / above MA20 60.53% / above MA50 84.21%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=576845760.0 spike=0.66 score=26.4
- COMI.CA: liquidity=476482688.0 spike=0.7 score=18.47
- ZMID.CA: liquidity=440536064.0 spike=2.11 score=25.62
- PHDC.CA: liquidity=403475456.0 spike=0.97 score=19.4
- ELSH.CA: liquidity=338224448.0 spike=2.9 score=24.01

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner stays on HOLD because EGX30 is in a bearish regime and sector breadth is weak (19%). EGX70 shows mixed signals but still negative 5‑day returns. Risk mode is DEFENSIVE_NO_NEW_BUY, so no new entries are permitted despite several tickets showing bullish watch outlooks.
- EGX30 trend bearish, only 10% of stocks above MA20 – limits upside potential.
- EGX70 mixed, but 5‑day median return still negative, adding uncertainty.
- Sector breadth at 19% is too low; leading sectors (Investment Holding, Tourism, Tech) lack broad support.
- Top tickets (MAAL, CCAP, KWIN, etc.) are near resistance or have cooling liquidity, reinforcing the defensive stance.
- Risk mode remains defensive; any new BUY would be blocked until breadth improves.

## Top Liquidity Spikes
- AJWA.CA: spike=14.93 liquidity=155943632.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NCCW.CA: spike=4.7 liquidity=96828760.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CFGH.CA: spike=3.77 liquidity=16954.95 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KWIN.CA: spike=3.75 liquidity=13971208.0 outlook=BULLISH_WATCH score=98.53 buy_ready=False
- ELSH.CA: spike=2.9 liquidity=338224448.0 outlook=CONSTRUCTIVE score=68.53 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=7.99 5d=2.57% 20d=12.11% aboveMA50=66.67%
- #2 Tourism & Leisure: score=7.13 5d=-8.23% 20d=13.34% aboveMA50=100.0%
- #3 Technology & Distribution: score=6.88 5d=-0.67% 20d=2.76% aboveMA50=100.0%
- #4 Real Estate: score=6.68 5d=0.0% 20d=5.37% aboveMA50=76.92%
- #5 Healthcare: score=6.13 5d=2.38% 20d=0.11% aboveMA50=100.0%
- #6 General / Verified EGX Expansion: score=5.53 5d=0.86% 20d=0.0% aboveMA50=82.69%
- #7 Food, Beverages & Tobacco: score=5.31 5d=-0.67% 20d=0.35% aboveMA50=85.71%
- #8 Building Materials: score=5.25 5d=-2.25% 20d=3.24% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KWIN.CA: BULLISH_WATCH score=98.53 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ZMID.CA: BULLISH_WATCH score=93.68 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RAYA.CA: BULLISH_WATCH score=92.88 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EEII.CA: BULLISH_WATCH score=92.53 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MHOT.CA: BULLISH_WATCH score=92.13 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- CERA.CA: BULLISH_WATCH score=89.53 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- RTVC.CA: BULLISH_WATCH score=86.53 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EALR.CA: BULLISH_WATCH score=86.53 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EPCO.CA: BULLISH_WATCH score=86.53 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- SEIG.CA: BULLISH_WATCH score=86.53 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=22.19 buy_ready=False sector_rank=6 price=219.13 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.5 liquidity=29047092.0 spike=2.49
- ABUK.CA: score=9.87 buy_ready=False sector_rank=18 price=81.26 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.89 liquidity=58401896.0 spike=0.45
- ACAMD.CA: score=23.21 buy_ready=False sector_rank=6 price=2.3 support=2.03 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.34 liquidity=39290204.0 spike=0.33
- ACGC.CA: score=21.1 buy_ready=False sector_rank=9 price=9.82 support=8.51 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.49 liquidity=50180144.0 spike=0.91
- ADCI.CA: score=14.23 buy_ready=False sector_rank=6 price=219.65 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=5018235.5 spike=0.74
- ADIB.CA: score=18.47 buy_ready=False sector_rank=14 price=46.34 support=45.0 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.78 liquidity=62278632.0 spike=0.39
- ADPC.CA: score=11.14 buy_ready=False sector_rank=6 price=3.7 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.16 liquidity=6929544.5 spike=0.28
- AFDI.CA: score=21.21 buy_ready=False sector_rank=6 price=43.72 support=38.51 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.42 liquidity=10795229.0 spike=0.6
- AFMC.CA: score=10.35 buy_ready=False sector_rank=6 price=72.95 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=1137738.25 spike=0.09
- AJWA.CA: score=11.21 buy_ready=False sector_rank=6 price=151.21 support=135.0 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=155943632.0 spike=14.93
- ALCN.CA: score=14.33 buy_ready=False sector_rank=20 price=28.72 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.44 liquidity=17267152.0 spike=0.74
- ALUM.CA: score=24.13 buy_ready=False sector_rank=6 price=25.63 support=22.52 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=32141420.0 spike=1.46
- AMER.CA: score=21.4 buy_ready=False sector_rank=4 price=2.81 support=2.32 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=115884112.0 spike=0.99
- AMES.CA: score=7.53 buy_ready=False sector_rank=6 price=50.55 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.81 liquidity=3322637.25 spike=0.43
- AMIA.CA: score=21.21 buy_ready=False sector_rank=6 price=9.09 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=18989712.0 spike=0.63
- AMOC.CA: score=14.03 buy_ready=False sector_rank=11 price=8.27 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=27872044.0 spike=0.33
- ANFI.CA: score=24.65 buy_ready=False sector_rank=6 price=15.52 support=13.5 resistance=16.04 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=62.47 liquidity=39216123.4 spike=1.72
- APSW.CA: score=3.6 buy_ready=False sector_rank=6 price=8.9 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.21 liquidity=391311.16 spike=0.37
- ARAB.CA: score=17.4 buy_ready=False sector_rank=4 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=33652164.0 spike=0.44
- ARCC.CA: score=21.1 buy_ready=False sector_rank=8 price=57.66 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.79 liquidity=18541890.0 spike=0.43
- AREH.CA: score=21.11 buy_ready=False sector_rank=6 price=1.5 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=38953180.0 spike=1.45
- ARVA.CA: score=20.21 buy_ready=False sector_rank=6 price=11.18 support=7.71 resistance=11.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.46 liquidity=23591372.0 spike=0.95
- ASCM.CA: score=18.51 buy_ready=False sector_rank=6 price=56.1 support=46.2 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.21 liquidity=74722968.0 spike=1.15
- ASPI.CA: score=25.53 buy_ready=False sector_rank=6 price=0.35 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.96 liquidity=122598320.0 spike=2.16
- ATLC.CA: score=11.44 buy_ready=False sector_rank=16 price=5.06 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=3318245.5 spike=0.46
- ATQA.CA: score=21.87 buy_ready=False sector_rank=18 price=9.9 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.35 liquidity=21769078.0 spike=0.53
- AXPH.CA: score=15.28 buy_ready=False sector_rank=6 price=1143.25 support=1023.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=48.22 liquidity=4072181.75 spike=0.69
- BINV.CA: score=18.96 buy_ready=False sector_rank=1 price=46.99 support=40.53 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=65.88 liquidity=4555221.5 spike=0.36
- BIOC.CA: score=11.34 buy_ready=False sector_rank=6 price=72.99 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.99 liquidity=2132138.0 spike=0.3
- BTFH.CA: score=13.12 buy_ready=False sector_rank=16 price=3.13 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=187832624.0 spike=0.79
- CAED.CA: score=11.17 buy_ready=False sector_rank=6 price=72.28 support=70.41 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.89 liquidity=6955080.0 spike=0.46
- CANA.CA: score=17.5 buy_ready=False sector_rank=14 price=37.22 support=33.15 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.35 liquidity=8023110.5 spike=0.57
- CCAP.CA: score=26.4 buy_ready=False sector_rank=1 price=5.53 support=4.66 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=576845760.0 spike=0.66
- CCRS.CA: score=21.21 buy_ready=False sector_rank=6 price=2.46 support=2.05 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.32 liquidity=13562367.0 spike=0.49
- CEFM.CA: score=5.5 buy_ready=False sector_rank=6 price=105.09 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.03 liquidity=1286142.75 spike=0.18
- CERA.CA: score=26.11 buy_ready=False sector_rank=6 price=1.21 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=30218930.0 spike=1.95
- CFGH.CA: score=5.23 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=16954.95 spike=3.77
- CICH.CA: score=14.25 buy_ready=False sector_rank=16 price=11.82 support=11.45 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=5628888.5 spike=1.25
- CIEB.CA: score=13.03 buy_ready=False sector_rank=14 price=23.53 support=23.31 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=47.01 liquidity=4561497.0 spike=0.43
- CIRA.CA: score=17.16 buy_ready=False sector_rank=13 price=26.5 support=21.0 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.34 liquidity=8605317.0 spike=0.3
- CLHO.CA: score=19.4 buy_ready=False sector_rank=5 price=14.94 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.9 liquidity=19566352.0 spike=0.56
- CNFN.CA: score=12.86 buy_ready=False sector_rank=16 price=4.57 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=5735299.5 spike=0.33
- COMI.CA: score=18.47 buy_ready=False sector_rank=14 price=132.62 support=129.8 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.93 liquidity=476482688.0 spike=0.7
- COPR.CA: score=20.21 buy_ready=False sector_rank=6 price=0.36 support=0.32 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=12725565.0 spike=0.33
- COSG.CA: score=21.21 buy_ready=False sector_rank=6 price=1.65 support=1.45 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.71 liquidity=38828892.0 spike=0.65
- CPCI.CA: score=9.45 buy_ready=False sector_rank=6 price=363.92 support=340.01 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=86.18 liquidity=1237052.25 spike=0.17
- CSAG.CA: score=16.15 buy_ready=False sector_rank=20 price=31.25 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.62 liquidity=8821906.0 spike=0.47
- DAPH.CA: score=12.25 buy_ready=False sector_rank=6 price=81.15 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.61 liquidity=8042801.0 spike=0.27
- DEIN.CA: score=7.21 buy_ready=False sector_rank=6 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=4.31 buy_ready=False sector_rank=7 price=24.68 support=24.24 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.1 liquidity=2803582.25 spike=1.19
- DSCW.CA: score=17.21 buy_ready=False sector_rank=6 price=1.82 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=18058986.0 spike=0.29
- DTPP.CA: score=5.86 buy_ready=False sector_rank=6 price=124.48 support=123.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.36 liquidity=1650558.88 spike=0.36
- EALR.CA: score=22.09 buy_ready=False sector_rank=6 price=367.07 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=14737155.0 spike=1.44
- EASB.CA: score=10.24 buy_ready=False sector_rank=6 price=5.0 support=4.61 resistance=5.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=70.31 liquidity=1028364.75 spike=0.68
- EAST.CA: score=25.12 buy_ready=False sector_rank=7 price=39.05 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.61 liquidity=11561549.0 spike=0.16
- EBSC.CA: score=12.08 buy_ready=False sector_rank=6 price=1.82 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=869811.56 spike=0.29
- ECAP.CA: score=15.86 buy_ready=False sector_rank=6 price=31.13 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=88.64 liquidity=6972007.5 spike=1.34
- EDFM.CA: score=15.79 buy_ready=False sector_rank=6 price=333.09 support=320.2 resistance=347.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=3054039.75 spike=2.76
- EEII.CA: score=22.81 buy_ready=False sector_rank=6 price=2.48 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=33464620.0 spike=1.8
- EFIC.CA: score=3.48 buy_ready=False sector_rank=18 price=205.14 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=6.06 liquidity=3608324.5 spike=0.9
- EFID.CA: score=19.12 buy_ready=False sector_rank=7 price=28.0 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.78 liquidity=40781576.0 spike=0.53
- EFIH.CA: score=15.94 buy_ready=False sector_rank=21 price=21.12 support=21.0 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.85 liquidity=39097892.0 spike=0.61
- EGAL.CA: score=17.87 buy_ready=False sector_rank=18 price=317.69 support=303.05 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=58144972.0 spike=0.53
- EGAS.CA: score=13.91 buy_ready=False sector_rank=11 price=49.56 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=2882644.25 spike=0.21
- EGBE.CA: score=3.49 buy_ready=False sector_rank=14 price=0.45 support=0.42 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=15015.02 spike=0.11
- EGCH.CA: score=21.87 buy_ready=False sector_rank=18 price=14.7 support=12.26 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=33654884.0 spike=0.29
- EGSA.CA: score=7.05 buy_ready=False sector_rank=15 price=8.81 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=74.7 liquidity=20688.42 spike=1.36
- EGTS.CA: score=7.74 buy_ready=False sector_rank=4 price=19.72 support=18.35 resistance=20.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=185288192.0 spike=1.67
- EHDR.CA: score=20.65 buy_ready=False sector_rank=6 price=2.8 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.08 liquidity=119511568.0 spike=2.22
- EKHO.CA: score=11.03 buy_ready=False sector_rank=11 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=21.67 buy_ready=False sector_rank=12 price=2.16 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=14489786.0 spike=0.5
- ELKA.CA: score=22.21 buy_ready=False sector_rank=6 price=1.28 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=38783916.0 spike=0.94
- ELNA.CA: score=4.28 buy_ready=False sector_rank=6 price=39.54 support=37.11 resistance=42.79 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=31.97 liquidity=64885.14 spike=0.21
- ELSH.CA: score=24.01 buy_ready=False sector_rank=6 price=12.94 support=7.92 resistance=13.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.84 liquidity=338224448.0 spike=2.9
- ELWA.CA: score=10.84 buy_ready=False sector_rank=6 price=2.14 support=1.79 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=91.43 liquidity=630972.5 spike=0.2
- EMFD.CA: score=21.4 buy_ready=False sector_rank=4 price=12.11 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.1 liquidity=231105984.0 spike=0.99
- ENGC.CA: score=24.65 buy_ready=False sector_rank=6 price=35.11 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=32257640.0 spike=2.72
- EOSB.CA: score=9.31 buy_ready=False sector_rank=6 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=100002.08 spike=0.84
- EPCO.CA: score=21.47 buy_ready=False sector_rank=6 price=9.28 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=14165978.0 spike=1.13
- EPPK.CA: score=6.63 buy_ready=False sector_rank=6 price=12.25 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=416659.34 spike=0.35
- ETEL.CA: score=18.31 buy_ready=False sector_rank=15 price=94.24 support=92.17 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=63661512.0 spike=0.57
- ETRS.CA: score=23.33 buy_ready=False sector_rank=6 price=9.35 support=7.37 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.26 liquidity=105233904.0 spike=2.06
- EXPA.CA: score=20.47 buy_ready=False sector_rank=14 price=18.83 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=37554632.0 spike=0.9
- FAIT.CA: score=11.21 buy_ready=False sector_rank=14 price=36.78 support=33.94 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=2734587.0 spike=0.42
- FAITA.CA: score=8.48 buy_ready=False sector_rank=14 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=9295.9 spike=0.18
- FERC.CA: score=1.65 buy_ready=False sector_rank=18 price=77.43 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=1778222.38 spike=0.28
- FWRY.CA: score=12.94 buy_ready=False sector_rank=21 price=18.69 support=18.32 resistance=21.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.25 liquidity=206534064.0 spike=0.7
- GBCO.CA: score=7.34 buy_ready=False sector_rank=17 price=27.93 support=27.13 resistance=28.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=243178528.0 spike=2.13
- GDWA.CA: score=22.09 buy_ready=False sector_rank=6 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=9875625.0 spike=0.97
- GGCC.CA: score=23.85 buy_ready=False sector_rank=6 price=0.43 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=12037739.0 spike=1.82
- GIHD.CA: score=14.66 buy_ready=False sector_rank=6 price=41.76 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.59 liquidity=1445642.75 spike=0.26
- GMCI.CA: score=6.76 buy_ready=False sector_rank=6 price=1.74 support=1.67 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=65.38 liquidity=428150.31 spike=1.06
- GRCA.CA: score=4.1 buy_ready=False sector_rank=6 price=54.22 support=53.16 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.6 liquidity=2886719.5 spike=0.32
- GSSC.CA: score=4.35 buy_ready=False sector_rank=6 price=249.35 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=7.12 liquidity=3138505.0 spike=0.36
- GTWL.CA: score=11.53 buy_ready=False sector_rank=6 price=47.84 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=13.49 liquidity=9720055.0 spike=1.3
- HDBK.CA: score=15.47 buy_ready=False sector_rank=14 price=141.64 support=138.75 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.6 liquidity=10149064.0 spike=0.62
- HELI.CA: score=6.64 buy_ready=False sector_rank=4 price=6.72 support=6.42 resistance=6.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=187183200.0 spike=1.12
- HRHO.CA: score=14.12 buy_ready=False sector_rank=16 price=26.57 support=26.05 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=72057952.0 spike=0.37
- ICID.CA: score=9.79 buy_ready=False sector_rank=6 price=6.92 support=6.12 resistance=6.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35303848.0 spike=2.79
- IDRE.CA: score=20.26 buy_ready=False sector_rank=6 price=44.49 support=39.72 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.96 liquidity=9044451.0 spike=0.26
- IFAP.CA: score=5.75 buy_ready=False sector_rank=10 price=19.37 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=5672497.5 spike=0.36
- INFI.CA: score=18.21 buy_ready=False sector_rank=6 price=101.01 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=14915146.0 spike=0.89
- IRON.CA: score=10.76 buy_ready=False sector_rank=18 price=32.45 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=4883448.0 spike=0.58
- ISMA.CA: score=18.91 buy_ready=False sector_rank=6 price=29.76 support=20.15 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=91.81 liquidity=66115196.0 spike=1.35
- ISMQ.CA: score=23.71 buy_ready=False sector_rank=18 price=8.03 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=93961024.0 spike=1.92
- ISPH.CA: score=23.4 buy_ready=False sector_rank=5 price=12.42 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.73 liquidity=64179828.0 spike=0.42
- JUFO.CA: score=23.94 buy_ready=False sector_rank=7 price=30.52 support=26.51 resistance=30.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.6 liquidity=64735828.0 spike=1.41
- KABO.CA: score=21.1 buy_ready=False sector_rank=9 price=6.31 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=13341119.0 spike=0.68
- KWIN.CA: score=26.21 buy_ready=False sector_rank=6 price=74.53 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.62 liquidity=13971208.0 spike=3.75
- KZPC.CA: score=12.68 buy_ready=False sector_rank=6 price=10.6 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.2 liquidity=3469316.0 spike=0.3
- LCSW.CA: score=15.46 buy_ready=False sector_rank=8 price=27.18 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.55 liquidity=6360365.0 spike=0.4
- LUTS.CA: score=21.21 buy_ready=False sector_rank=6 price=0.63 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.69 liquidity=13653132.0 spike=0.85
- MAAL.CA: score=26.93 buy_ready=False sector_rank=6 price=6.05 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=21883050.0 spike=1.86
- MASR.CA: score=19.21 buy_ready=False sector_rank=6 price=6.94 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.48 liquidity=27619768.0 spike=0.47
- MBSC.CA: score=21.1 buy_ready=False sector_rank=8 price=275.06 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.41 liquidity=44207968.0 spike=0.9
- MCQE.CA: score=19.7 buy_ready=False sector_rank=8 price=187.01 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.24 liquidity=24835860.0 spike=1.3
- MCRO.CA: score=20.21 buy_ready=False sector_rank=6 price=1.26 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=20328212.0 spike=0.23
- MENA.CA: score=16.82 buy_ready=False sector_rank=4 price=6.77 support=5.76 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=3422558.5 spike=0.21
- MEPA.CA: score=21.21 buy_ready=False sector_rank=6 price=1.72 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=15118439.0 spike=0.71
- MFPC.CA: score=9.87 buy_ready=False sector_rank=18 price=42.1 support=42.3 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=39255352.0 spike=0.41
- MFSC.CA: score=7.98 buy_ready=False sector_rank=6 price=46.9 support=33.01 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.62 liquidity=3766371.75 spike=0.25
- MHOT.CA: score=23.74 buy_ready=False sector_rank=2 price=30.93 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=23141522.0 spike=1.17
- MICH.CA: score=17.08 buy_ready=False sector_rank=6 price=36.94 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.8 liquidity=3864996.75 spike=0.43
- MILS.CA: score=18.38 buy_ready=False sector_rank=6 price=142.09 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.66 liquidity=7169588.5 spike=0.26
- MIPH.CA: score=10.61 buy_ready=False sector_rank=5 price=660.66 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.8 liquidity=1211481.13 spike=0.32
- MOED.CA: score=9.2 buy_ready=False sector_rank=6 price=0.69 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=18.28 liquidity=8986135.0 spike=0.68
- MOIL.CA: score=13.16 buy_ready=False sector_rank=11 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=61.43 liquidity=133526.61 spike=0.72
- MOIN.CA: score=10.69 buy_ready=False sector_rank=6 price=25.01 support=23.13 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=477885.69 spike=0.23
- MOSC.CA: score=7.22 buy_ready=False sector_rank=6 price=264.79 support=268.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.91 liquidity=3004170.5 spike=0.22
- MPCI.CA: score=23.33 buy_ready=False sector_rank=6 price=228.0 support=192.01 resistance=233.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.01 liquidity=105695344.0 spike=1.06
- MPCO.CA: score=22.12 buy_ready=False sector_rank=10 price=1.8 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=103089552.0 spike=1.52
- MPRC.CA: score=21.21 buy_ready=False sector_rank=6 price=33.19 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.66 liquidity=18629672.0 spike=0.87
- MTIE.CA: score=18.08 buy_ready=False sector_rank=17 price=9.1 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=11095352.0 spike=0.5
- NAHO.CA: score=5.22 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=8829.92 spike=0.24
- NCCW.CA: score=11.21 buy_ready=False sector_rank=6 price=6.6 support=6.3 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96828760.0 spike=4.7
- NEDA.CA: score=11.54 buy_ready=False sector_rank=6 price=2.8 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=326233.59 spike=0.62
- NHPS.CA: score=14.47 buy_ready=False sector_rank=6 price=69.5 support=67.53 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.84 liquidity=6259210.0 spike=0.58
- NINH.CA: score=10.79 buy_ready=False sector_rank=6 price=17.83 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=1573694.5 spike=0.14
- NIPH.CA: score=21.4 buy_ready=False sector_rank=5 price=166.65 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=99894120.0 spike=0.82
- OBRI.CA: score=8.83 buy_ready=False sector_rank=6 price=36.2 support=34.25 resistance=36.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24231310.0 spike=2.31
- OCDI.CA: score=19.6 buy_ready=False sector_rank=4 price=21.6 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.23 liquidity=46089980.0 spike=1.1
- OCPH.CA: score=11.49 buy_ready=False sector_rank=6 price=361.01 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.47 liquidity=7281843.0 spike=0.66
- ODIN.CA: score=7.21 buy_ready=False sector_rank=6 price=2.17 support=2.06 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15065516.0 spike=1.5
- OFH.CA: score=23.21 buy_ready=False sector_rank=6 price=0.63 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=18336924.0 spike=0.83
- OIH.CA: score=14.4 buy_ready=False sector_rank=1 price=1.4 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=35169524.0 spike=0.29
- OLFI.CA: score=21.12 buy_ready=False sector_rank=7 price=21.77 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=13770916.0 spike=0.62
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=719.96 support=717.0 resistance=740.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=165310816.0 spike=1.0
- ORHD.CA: score=19.4 buy_ready=False sector_rank=4 price=37.05 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.64 liquidity=180110640.0 spike=0.88
- ORWE.CA: score=21.1 buy_ready=False sector_rank=9 price=23.84 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.79 liquidity=34278208.0 spike=0.75
- PHAR.CA: score=18.26 buy_ready=False sector_rank=5 price=86.45 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=8864981.0 spike=0.24
- PHDC.CA: score=19.4 buy_ready=False sector_rank=4 price=15.1 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=403475456.0 spike=0.97
- PHTV.CA: score=14.17 buy_ready=False sector_rank=6 price=208.1 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=4955288.5 spike=0.33
- POUL.CA: score=21.12 buy_ready=False sector_rank=7 price=37.45 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.74 liquidity=12531810.0 spike=0.26
- PRCL.CA: score=25.64 buy_ready=False sector_rank=8 price=25.39 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=81666832.0 spike=2.27
- PRDC.CA: score=17.85 buy_ready=False sector_rank=4 price=6.14 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=72.93 liquidity=6447171.0 spike=0.33
- PRMH.CA: score=18.23 buy_ready=False sector_rank=6 price=2.77 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.52 liquidity=16313417.0 spike=1.01
- RACC.CA: score=13.52 buy_ready=False sector_rank=6 price=9.84 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=4312686.5 spike=0.18
- RAKT.CA: score=9.47 buy_ready=False sector_rank=6 price=23.79 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=54.9 liquidity=262070.65 spike=0.99
- RAYA.CA: score=22.4 buy_ready=False sector_rank=3 price=7.46 support=6.94 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=46052876.0 spike=0.4
- RMDA.CA: score=21.4 buy_ready=False sector_rank=5 price=5.24 support=4.91 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=49367108.0 spike=0.45
- ROTO.CA: score=24.99 buy_ready=False sector_rank=6 price=35.13 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=22968286.0 spike=1.89
- RREI.CA: score=21.21 buy_ready=False sector_rank=6 price=3.53 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.27 liquidity=19857492.0 spike=0.85
- RTVC.CA: score=22.74 buy_ready=False sector_rank=6 price=4.05 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.82 liquidity=8785389.0 spike=1.37
- RUBX.CA: score=15.87 buy_ready=False sector_rank=6 price=10.48 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.0 liquidity=26503606.0 spike=1.83
- SAUD.CA: score=16.01 buy_ready=False sector_rank=14 price=22.16 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.51 liquidity=7542039.0 spike=0.53
- SCEM.CA: score=15.24 buy_ready=False sector_rank=8 price=63.76 support=62.5 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=6138391.0 spike=0.15
- SCFM.CA: score=13.15 buy_ready=False sector_rank=6 price=260.0 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.91 liquidity=8942952.0 spike=0.31
- SCTS.CA: score=12.92 buy_ready=False sector_rank=13 price=632.94 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.82 liquidity=9363555.0 spike=0.86
- SDTI.CA: score=23.59 buy_ready=False sector_rank=6 price=47.52 support=43.4 resistance=46.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.94 liquidity=22604860.0 spike=1.19
- SEIG.CA: score=20.16 buy_ready=False sector_rank=6 price=188.29 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=6609814.5 spike=1.17
- SIPC.CA: score=23.69 buy_ready=False sector_rank=6 price=3.63 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=19097044.0 spike=1.24
- SKPC.CA: score=13.87 buy_ready=False sector_rank=18 price=17.26 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.68 liquidity=31420310.0 spike=0.44
- SMFR.CA: score=5.97 buy_ready=False sector_rank=6 price=207.11 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.74 liquidity=1756829.5 spike=0.23
- SNFC.CA: score=17.55 buy_ready=False sector_rank=6 price=12.13 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=8335544.5 spike=0.31
- SPIN.CA: score=7.8 buy_ready=False sector_rank=9 price=14.09 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.23 liquidity=1703613.63 spike=0.35
- SPMD.CA: score=23.21 buy_ready=False sector_rank=6 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=14562931.0 spike=0.58
- SUGR.CA: score=18.13 buy_ready=False sector_rank=7 price=49.72 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=37.22 liquidity=5010114.0 spike=0.31
- SVCE.CA: score=19.21 buy_ready=False sector_rank=6 price=8.69 support=8.33 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=29038700.0 spike=0.23
- SWDY.CA: score=17.84 buy_ready=False sector_rank=12 price=87.32 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=9167829.0 spike=0.26
- TALM.CA: score=20.56 buy_ready=False sector_rank=13 price=15.98 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.08 liquidity=12166688.0 spike=0.93
- TMGH.CA: score=19.4 buy_ready=False sector_rank=4 price=96.06 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.15 liquidity=311931680.0 spike=0.6
- TRTO.CA: score=7.21 buy_ready=False sector_rank=6 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=211.38 spike=0.44
- UEFM.CA: score=5.82 buy_ready=False sector_rank=6 price=473.74 support=455.6 resistance=505.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=36.58 liquidity=604601.81 spike=0.37
- UEGC.CA: score=21.51 buy_ready=False sector_rank=6 price=1.44 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=28164708.0 spike=1.15
- UNIP.CA: score=20.31 buy_ready=False sector_rank=6 price=0.32 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.69 liquidity=16486509.0 spike=1.05
- UNIT.CA: score=20.17 buy_ready=False sector_rank=4 price=13.88 support=10.89 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.67 liquidity=8770055.0 spike=0.83
- WCDF.CA: score=4.96 buy_ready=False sector_rank=6 price=539.17 support=535.0 resistance=559.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=13.84 liquidity=370948.95 spike=1.19
- WKOL.CA: score=18.85 buy_ready=False sector_rank=6 price=302.82 support=290.0 resistance=339.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=14532273.0 spike=2.32
- ZEOT.CA: score=18.35 buy_ready=False sector_rank=6 price=9.22 support=8.43 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.16 liquidity=5137103.0 spike=0.71
- ZMID.CA: score=25.62 buy_ready=False sector_rank=4 price=6.41 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=440536064.0 spike=2.11

## Backtesting Lite
- MAAL.CA: 180d return=38.05%, max drawdown=-27.25%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- CCAP.CA: 180d return=118.82%, max drawdown=-25.0%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- KWIN.CA: 180d return=-4.72%, max drawdown=-34.04%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MAAL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Marseille Almasreia Alkhalegeya For Holding Investment SAE summary=Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- KWIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Kahera El Watania Investment summary=ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m; El Kahera El Watania to buy stake in Assiut for Agricultural Development; Tycoon Holding acquires 85% of Alexandria National Investment
  - ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m: https://english.mubasher.info/news/4546852/ADIB-Egypt-s-Cairo-National-unveils-equity-reduction-transaction-worth-over-EGP-3m/
  - El Kahera El Watania to buy stake in Assiut for Agricultural Development: https://english.mubasher.info/news/4009433/El-Kahera-El-Watania-to-buy-stake-in-Assiut-for-Agricultural-Development/
  - Tycoon Holding acquires 85% of Alexandria National Investment: https://english.mubasher.info/news/3844623/Tycoon-Holding-acquires-85-of-Alexandria-National-Investment/
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- PRCL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ceramic and Porcelain summary=Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=524 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- ASPI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Aspire Capital Holding for Financial Investments summary=Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25; PREDCO, Aspire Holding consider establishing mortgage company; Pioneers Holding gets EGX&#39;s approval for capital cut, name change
  - Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25: https://english.mubasher.info/news/4541324/Aspire-Capital-records-higher-consolidated-net-profits-at-over-EGP-42m-in-9M-25/
  - PREDCO, Aspire Holding consider establishing mortgage company: https://english.mubasher.info/news/4185438/PREDCO-Aspire-Holding-consider-establishing-mortgage-company/
  - Pioneers Holding gets EGX&#39;s approval for capital cut, name change: https://english.mubasher.info/news/3861454/Pioneers-Holding-gets-EGX-s-approval-for-capital-cut-name-change/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.

## Warnings
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for KWIN.CA matches the company but no source/report date was detected.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
