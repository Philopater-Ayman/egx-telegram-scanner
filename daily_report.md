# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-17T10:20:43.319461+00:00
Generated Cairo: 2026-06-17 13:20
Run timing: target 08:45 Cairo | generated Cairo 2026-06-17 13:20 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-17 13:17

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
- EGX30 regime: MIXED / above MA20 50.0% / above MA50 55.0%
- EGX70 regime: MIXED / above MA20 51.28% / above MA50 79.49%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- TMGH.CA: liquidity=853364928.0 spike=1.87 score=23.92
- COMI.CA: liquidity=478585792.0 spike=0.79 score=23.04
- PHDC.CA: liquidity=332961248.0 spike=0.8 score=22.18
- ORAS.CA: liquidity=311075648.0 spike=1.0 score=4.6
- CCAP.CA: liquidity=297782336.0 spike=0.34 score=17.68

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because EGX30 and EGX70 are in a mixed regime with weak sector breadth (14.29%). Risk mode is DEFENSIVE_NO_NEW_BUY, so new entries are blocked despite several stocks showing bullish watch signals.
- Liquidity is adequate for top picks (e.g., MTIE, SPMD) but no clear buy‑ready signal.
- Support levels are 4‑7% away; resistance is close (0‑5%) on many tickets, limiting short‑term upside.
- Automotive & Distribution leads sector breadth, yet overall market sentiment remains defensive for the next 1‑3 days.

## Top Liquidity Spikes
- KWIN.CA: spike=26.31 liquidity=127989056.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CICH.CA: spike=22.84 liquidity=72834944.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DOMT.CA: spike=12.34 liquidity=23799658.0 outlook=CONSTRUCTIVE score=66.04 buy_ready=False
- ZEOT.CA: spike=12.13 liquidity=200913680.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ECAP.CA: spike=8.72 liquidity=45236596.0 outlook=BULLISH_WATCH score=71.38 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=8.91 5d=1.59% 20d=4.33% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=6.58 5d=3.53% 20d=8.18% aboveMA50=50.0%
- #3 Real Estate: score=5.45 5d=-1.03% 20d=2.03% aboveMA50=84.62%
- #4 Banking & Financials: score=5.1 5d=0.21% 20d=1.05% aboveMA50=80.0%
- #5 Food, Beverages & Tobacco: score=5.04 5d=-0.85% 20d=1.9% aboveMA50=100.0%
- #6 Non-bank Financial Services: score=4.42 5d=0.0% 20d=0.0% aboveMA50=60.0%
- #7 General / Verified EGX Expansion: score=4.38 5d=-0.43% 20d=0.17% aboveMA50=71.15%
- #8 Tourism & Leisure: score=4.26 5d=-3.43% 20d=10.22% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- TMGH.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MASR.CA: BULLISH_WATCH score=93.38 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- UNIT.CA: BULLISH_WATCH score=91.45 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SPMD.CA: BULLISH_WATCH score=91.38 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MOSC.CA: BULLISH_WATCH score=91.38 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CANA.CA: BULLISH_WATCH score=86.1 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- HELI.CA: BULLISH_WATCH score=85.45 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=85.45 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- HDBK.CA: BULLISH_WATCH score=83.1 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=10.7 buy_ready=False sector_rank=7 price=205.63 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=54.01 liquidity=1946188.75 spike=0.29
- ABUK.CA: score=8.68 buy_ready=False sector_rank=21 price=70.47 support=71.06 resistance=90.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=4.08 liquidity=125993040.0 spike=0.9
- ACAMD.CA: score=20.75 buy_ready=False sector_rank=7 price=2.37 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=67058140.0 spike=0.53
- ACGC.CA: score=18.36 buy_ready=False sector_rank=11 price=9.49 support=9.02 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=12644274.0 spike=0.22
- ADCI.CA: score=16.89 buy_ready=False sector_rank=7 price=228.28 support=205.1 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=68.7 liquidity=7837469.0 spike=1.15
- ADIB.CA: score=21.04 buy_ready=False sector_rank=4 price=47.16 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=36670928.0 spike=0.33
- ADPC.CA: score=11.33 buy_ready=False sector_rank=7 price=3.62 support=3.45 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5574625.0 spike=0.22
- AFDI.CA: score=11.13 buy_ready=False sector_rank=7 price=42.46 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=2378931.25 spike=0.15
- AFMC.CA: score=9.3 buy_ready=False sector_rank=7 price=71.35 support=67.0 resistance=77.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=543728.0 spike=0.1
- AJWA.CA: score=7.71 buy_ready=False sector_rank=7 price=193.11 support=178.0 resistance=198.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51448952.0 spike=1.98
- ALCN.CA: score=9.75 buy_ready=False sector_rank=16 price=28.5 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=5038626.0 spike=0.34
- ALUM.CA: score=12.85 buy_ready=False sector_rank=7 price=23.0 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=4098204.75 spike=0.25
- AMER.CA: score=20.18 buy_ready=False sector_rank=3 price=2.5 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=56358884.0 spike=0.56
- AMES.CA: score=4.19 buy_ready=False sector_rank=7 price=48.88 support=48.0 resistance=55.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=1439907.0 spike=0.36
- AMIA.CA: score=15.78 buy_ready=False sector_rank=7 price=9.12 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=7027280.0 spike=0.45
- AMOC.CA: score=10.6 buy_ready=False sector_rank=9 price=7.83 support=7.71 resistance=8.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=11414907.0 spike=0.16
- ANFI.CA: score=24.75 buy_ready=False sector_rank=7 price=34.5 support=13.73 resistance=34.5 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=97.65 liquidity=273902676.0 spike=4.23
- APSW.CA: score=4.09 buy_ready=False sector_rank=7 price=8.53 support=8.24 resistance=9.38 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=28.92 liquidity=1735957.31 spike=2.3
- ARAB.CA: score=20.18 buy_ready=False sector_rank=3 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=36498720.0 spike=0.42
- ARCC.CA: score=16.77 buy_ready=False sector_rank=14 price=56.0 support=53.6 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=50.97 liquidity=8817001.0 spike=0.24
- AREH.CA: score=17.75 buy_ready=False sector_rank=7 price=1.58 support=1.27 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=79.07 liquidity=21927002.0 spike=0.79
- ARVA.CA: score=20.97 buy_ready=False sector_rank=7 price=10.88 support=7.71 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=72.75 liquidity=33484930.0 spike=1.11
- ASCM.CA: score=20.75 buy_ready=False sector_rank=7 price=59.33 support=47.3 resistance=64.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=73.67 liquidity=34709288.0 spike=0.5
- ASPI.CA: score=14.75 buy_ready=False sector_rank=7 price=0.3 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=16995458.0 spike=0.25
- ATLC.CA: score=15.19 buy_ready=False sector_rank=6 price=5.14 support=4.7 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=2422434.75 spike=0.55
- ATQA.CA: score=12.68 buy_ready=False sector_rank=21 price=9.61 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=13805159.0 spike=0.4
- AXPH.CA: score=4.37 buy_ready=False sector_rank=7 price=1105.36 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=28.66 liquidity=621268.25 spike=0.33
- BINV.CA: score=12.91 buy_ready=False sector_rank=17 price=46.79 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=1226137.5 spike=0.11
- BIOC.CA: score=9.19 buy_ready=False sector_rank=7 price=71.41 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=48.88 liquidity=437187.44 spike=0.16
- BTFH.CA: score=14.77 buy_ready=False sector_rank=6 price=3.0 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=98758416.0 spike=0.47
- CAED.CA: score=22.01 buy_ready=False sector_rank=7 price=73.23 support=67.21 resistance=79.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=9774665.0 spike=1.74
- CANA.CA: score=23.32 buy_ready=False sector_rank=4 price=37.52 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=11943935.0 spike=1.14
- CCAP.CA: score=17.68 buy_ready=False sector_rank=17 price=5.06 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=297782336.0 spike=0.34
- CCRS.CA: score=17.99 buy_ready=False sector_rank=7 price=2.47 support=2.27 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=7235361.5 spike=0.3
- CEFM.CA: score=6.38 buy_ready=False sector_rank=7 price=102.15 support=100.53 resistance=115.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=41.26 liquidity=629686.81 spike=0.18
- CERA.CA: score=23.75 buy_ready=False sector_rank=7 price=1.26 support=1.13 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=64699768.0 spike=3.84
- CFGH.CA: score=-0.25 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=161.67 spike=0.03
- CICH.CA: score=10.77 buy_ready=False sector_rank=6 price=12.5 support=11.54 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72834944.0 spike=22.84
- CIEB.CA: score=16.11 buy_ready=False sector_rank=4 price=23.82 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=4072996.25 spike=0.58
- CIRA.CA: score=14.11 buy_ready=False sector_rank=10 price=26.71 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=44.95 liquidity=5540145.5 spike=0.36
- CLHO.CA: score=19.84 buy_ready=False sector_rank=15 price=15.51 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=56.73 liquidity=15408548.0 spike=0.54
- CNFN.CA: score=19.87 buy_ready=False sector_rank=6 price=4.56 support=4.36 resistance=4.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=41.43 liquidity=15868997.0 spike=1.05
- COMI.CA: score=23.04 buy_ready=False sector_rank=4 price=135.82 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=478585792.0 spike=0.79
- COPR.CA: score=20.49 buy_ready=False sector_rank=7 price=0.38 support=0.34 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=65.85 liquidity=57361184.0 spike=1.37
- COSG.CA: score=20.75 buy_ready=False sector_rank=7 price=1.61 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=25556602.0 spike=0.37
- CPCI.CA: score=10.85 buy_ready=False sector_rank=7 price=367.23 support=345.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=71.29 liquidity=2101259.75 spike=0.97
- CSAG.CA: score=11.28 buy_ready=False sector_rank=16 price=31.26 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=50.66 liquidity=3562231.5 spike=0.27
- DAPH.CA: score=15.3 buy_ready=False sector_rank=7 price=81.74 support=76.6 resistance=86.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=4549133.0 spike=0.4
- DEIN.CA: score=6.75 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=21.02 buy_ready=False sector_rank=5 price=25.61 support=23.7 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=30.71 liquidity=23799658.0 spike=12.34
- DSCW.CA: score=20.75 buy_ready=False sector_rank=7 price=1.85 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=32275298.0 spike=0.61
- DTPP.CA: score=1.11 buy_ready=False sector_rank=7 price=116.56 support=114.0 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=16.62 liquidity=355277.25 spike=0.19
- EALR.CA: score=9.77 buy_ready=False sector_rank=7 price=356.47 support=346.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=1013991.38 spike=0.27
- EASB.CA: score=10.75 buy_ready=False sector_rank=7 price=8.63 support=7.33 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37682452.0 spike=8.48
- EAST.CA: score=23.02 buy_ready=False sector_rank=5 price=39.16 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=12928499.0 spike=0.19
- EBSC.CA: score=11.56 buy_ready=False sector_rank=7 price=1.91 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=70.91 liquidity=805750.75 spike=0.3
- ECAP.CA: score=24.75 buy_ready=False sector_rank=7 price=33.23 support=28.7 resistance=32.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=86.18 liquidity=45236596.0 spike=8.72
- EDFM.CA: score=12.45 buy_ready=False sector_rank=7 price=331.68 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=52.43 liquidity=1255408.77 spike=2.22
- EEII.CA: score=17.35 buy_ready=False sector_rank=7 price=2.44 support=2.27 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=6593217.5 spike=0.37
- EFIC.CA: score=-2.02 buy_ready=False sector_rank=21 price=203.24 support=192.01 resistance=218.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=23.12 liquidity=307146.78 spike=0.12
- EFID.CA: score=19.02 buy_ready=False sector_rank=5 price=28.3 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=12966053.0 spike=0.17
- EFIH.CA: score=14.03 buy_ready=False sector_rank=19 price=21.1 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=30603764.0 spike=0.58
- EGAL.CA: score=8.68 buy_ready=False sector_rank=21 price=299.16 support=297.1 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=14908395.0 spike=0.19
- EGAS.CA: score=15.09 buy_ready=False sector_rank=9 price=51.88 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=4490694.0 spike=0.36
- EGBE.CA: score=9.06 buy_ready=False sector_rank=4 price=0.44 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=44.02 liquidity=15445.87 spike=0.14
- EGCH.CA: score=16.68 buy_ready=False sector_rank=21 price=13.7 support=12.9 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=26600830.0 spike=0.28
- EGSA.CA: score=3.0 buy_ready=False sector_rank=13 price=8.78 support=8.44 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 June 01:12 PM market time freshness=DELAYED_CURRENT RSI=26.47 liquidity=12908.61 spike=0.81
- EGTS.CA: score=20.18 buy_ready=False sector_rank=3 price=17.97 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=41.85 liquidity=35237792.0 spike=0.28
- EHDR.CA: score=20.75 buy_ready=False sector_rank=7 price=2.69 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=15443841.0 spike=0.26
- EKHO.CA: score=10.6 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.61 buy_ready=False sector_rank=12 price=2.14 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=6430574.0 spike=0.25
- ELKA.CA: score=21.75 buy_ready=False sector_rank=7 price=1.32 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=28424920.0 spike=0.7
- ELNA.CA: score=13.08 buy_ready=False sector_rank=7 price=39.45 support=37.11 resistance=41.51 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.98 liquidity=592144.51 spike=1.87
- ELSH.CA: score=17.75 buy_ready=False sector_rank=7 price=13.5 support=8.11 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=76.56 liquidity=108172928.0 spike=0.58
- ELWA.CA: score=11.18 buy_ready=False sector_rank=7 price=2.05 support=1.79 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=430918.09 spike=0.14
- EMFD.CA: score=24.22 buy_ready=False sector_rank=3 price=12.6 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=71.01 liquidity=281021728.0 spike=1.02
- ENGC.CA: score=8.21 buy_ready=False sector_rank=7 price=37.75 support=35.75 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31056636.0 spike=2.23
- EOSB.CA: score=16.68 buy_ready=False sector_rank=7 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=229601.28 spike=1.85
- EPCO.CA: score=20.86 buy_ready=False sector_rank=7 price=9.4 support=8.56 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=6109614.5 spike=0.56
- EPPK.CA: score=8.3 buy_ready=False sector_rank=7 price=12.29 support=11.67 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=551934.81 spike=0.5
- ETEL.CA: score=9.99 buy_ready=False sector_rank=13 price=93.0 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.31 liquidity=41528036.0 spike=0.51
- ETRS.CA: score=17.75 buy_ready=False sector_rank=7 price=10.42 support=7.37 resistance=10.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=76.02 liquidity=41928924.0 spike=0.68
- EXPA.CA: score=19.04 buy_ready=False sector_rank=4 price=18.4 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=22024806.0 spike=0.63
- FAIT.CA: score=10.33 buy_ready=False sector_rank=4 price=36.77 support=35.01 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=49.14 liquidity=1291696.75 spike=0.27
- FAITA.CA: score=9.07 buy_ready=False sector_rank=4 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=31561.0 spike=0.69
- FERC.CA: score=-0.06 buy_ready=False sector_rank=21 price=75.07 support=75.0 resistance=79.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=24.38 liquidity=2264637.0 spike=0.56
- FWRY.CA: score=9.03 buy_ready=False sector_rank=19 price=18.92 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=82565776.0 spike=0.28
- GBCO.CA: score=24.4 buy_ready=False sector_rank=1 price=28.5 support=25.25 resistance=28.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=66.73 liquidity=50230164.0 spike=0.47
- GDWA.CA: score=21.48 buy_ready=False sector_rank=7 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=61.94 liquidity=9731101.0 spike=0.69
- GGCC.CA: score=12.85 buy_ready=False sector_rank=7 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=59.38 liquidity=3095156.0 spike=0.4
- GIHD.CA: score=10.02 buy_ready=False sector_rank=7 price=40.74 support=35.15 resistance=43.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=1267123.0 spike=0.36
- GMCI.CA: score=13.17 buy_ready=False sector_rank=7 price=1.77 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=414659.47 spike=0.99
- GRCA.CA: score=4.24 buy_ready=False sector_rank=7 price=54.99 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=30.47 liquidity=3486806.25 spike=0.58
- GSSC.CA: score=3.11 buy_ready=False sector_rank=7 price=248.12 support=228.1 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=21.11 liquidity=2358512.75 spike=0.48
- GTWL.CA: score=8.05 buy_ready=False sector_rank=7 price=47.97 support=45.47 resistance=55.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=2296063.75 spike=0.3
- HDBK.CA: score=25.04 buy_ready=False sector_rank=4 price=147.01 support=138.0 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=59.06 liquidity=11499809.0 spike=0.71
- HELI.CA: score=22.18 buy_ready=False sector_rank=3 price=6.59 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=50.83 liquidity=108561224.0 spike=0.73
- HRHO.CA: score=24.77 buy_ready=False sector_rank=6 price=27.75 support=25.8 resistance=27.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=61.13 liquidity=44746056.0 spike=0.3
- ICID.CA: score=15.68 buy_ready=False sector_rank=7 price=7.17 support=4.5 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=86.6 liquidity=5930006.0 spike=0.36
- IDRE.CA: score=20.75 buy_ready=False sector_rank=7 price=44.26 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=14424255.0 spike=0.64
- IFAP.CA: score=8.88 buy_ready=False sector_rank=2 price=19.13 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=35.91 liquidity=1480016.5 spike=0.2
- INFI.CA: score=8.93 buy_ready=False sector_rank=7 price=97.9 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=24.9 liquidity=6181232.0 spike=0.62
- IRON.CA: score=11.18 buy_ready=False sector_rank=21 price=32.53 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=50.32 liquidity=4503104.0 spike=0.56
- ISMA.CA: score=15.75 buy_ready=False sector_rank=7 price=29.82 support=23.6 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=80.54 liquidity=14244345.0 spike=0.33
- ISMQ.CA: score=20.68 buy_ready=False sector_rank=21 price=8.13 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=39255524.0 spike=0.55
- ISPH.CA: score=19.84 buy_ready=False sector_rank=15 price=12.01 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=59.28 liquidity=17660820.0 spike=0.14
- JUFO.CA: score=18.32 buy_ready=False sector_rank=5 price=30.69 support=26.51 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=69.55 liquidity=7305339.5 spike=0.19
- KABO.CA: score=14.55 buy_ready=False sector_rank=11 price=6.23 support=5.94 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=6191484.5 spike=0.32
- KWIN.CA: score=10.75 buy_ready=False sector_rank=7 price=81.02 support=73.1 resistance=88.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127989056.0 spike=26.31
- KZPC.CA: score=11.75 buy_ready=False sector_rank=7 price=10.61 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=57.42 liquidity=998455.25 spike=0.11
- LCSW.CA: score=20.47 buy_ready=False sector_rank=14 price=27.73 support=26.0 resistance=28.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=42.74 liquidity=11006315.0 spike=1.26
- LUTS.CA: score=17.75 buy_ready=False sector_rank=7 price=0.72 support=0.54 resistance=0.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=83.88 liquidity=26688544.0 spike=0.77
- MAAL.CA: score=20.19 buy_ready=False sector_rank=7 price=6.48 support=4.47 resistance=6.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=78.53 liquidity=17027724.0 spike=1.22
- MASR.CA: score=24.77 buy_ready=False sector_rank=7 price=7.6 support=6.54 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=114611216.0 spike=2.01
- MBSC.CA: score=17.95 buy_ready=False sector_rank=14 price=253.24 support=247.43 resistance=273.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=48.2 liquidity=24190990.0 spike=0.54
- MCQE.CA: score=5.85 buy_ready=False sector_rank=14 price=177.73 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=25.31 liquidity=5898744.5 spike=0.36
- MCRO.CA: score=17.75 buy_ready=False sector_rank=7 price=1.25 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=33131006.0 spike=0.69
- MENA.CA: score=22.18 buy_ready=False sector_rank=3 price=6.96 support=6.12 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=10211629.0 spike=0.59
- MEPA.CA: score=20.68 buy_ready=False sector_rank=7 price=1.72 support=1.63 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=9932527.0 spike=0.58
- MFPC.CA: score=8.72 buy_ready=False sector_rank=21 price=36.8 support=36.9 resistance=45.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=4.77 liquidity=89008704.0 spike=1.02
- MFSC.CA: score=4.81 buy_ready=False sector_rank=7 price=44.33 support=43.0 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=21.46 liquidity=1061919.88 spike=0.09
- MHOT.CA: score=17.27 buy_ready=False sector_rank=8 price=30.26 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=8563493.0 spike=0.39
- MICH.CA: score=16.32 buy_ready=False sector_rank=7 price=37.33 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=3565990.5 spike=0.24
- MILS.CA: score=16.69 buy_ready=False sector_rank=7 price=140.0 support=127.01 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=5935428.0 spike=0.3
- MIPH.CA: score=-0.06 buy_ready=False sector_rank=15 price=699.0 support=660.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3744263.5 spike=1.68
- MOED.CA: score=13.67 buy_ready=False sector_rank=7 price=0.71 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=6921728.0 spike=0.55
- MOIL.CA: score=10.74 buy_ready=False sector_rank=9 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=135661.53 spike=0.83
- MOIN.CA: score=3.41 buy_ready=False sector_rank=7 price=24.45 support=24.1 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=21.12 liquidity=654157.69 spike=0.38
- MOSC.CA: score=22.43 buy_ready=False sector_rank=7 price=281.72 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=53.26 liquidity=17132478.0 spike=1.84
- MPCI.CA: score=20.75 buy_ready=False sector_rank=7 price=223.53 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=62.21 liquidity=48414128.0 spike=0.61
- MPCO.CA: score=23.4 buy_ready=False sector_rank=2 price=1.97 support=1.54 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=50552336.0 spike=0.51
- MPRC.CA: score=15.04 buy_ready=False sector_rank=7 price=31.96 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=6291610.5 spike=0.31
- MTIE.CA: score=27.22 buy_ready=False sector_rank=1 price=9.06 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=25443124.0 spike=1.41
- NAHO.CA: score=4.75 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=669.5 spike=0.02
- NCCW.CA: score=20.75 buy_ready=False sector_rank=7 price=6.15 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=69.02 liquidity=13448629.0 spike=0.48
- NEDA.CA: score=11.17 buy_ready=False sector_rank=7 price=2.81 support=2.65 resistance=2.84 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=61.76 liquidity=379799.59 spike=1.02
- NHPS.CA: score=13.32 buy_ready=False sector_rank=7 price=68.78 support=65.03 resistance=72.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=3571603.75 spike=0.8
- NINH.CA: score=9.46 buy_ready=False sector_rank=7 price=17.53 support=16.8 resistance=19.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=707187.56 spike=0.14
- NIPH.CA: score=17.84 buy_ready=False sector_rank=15 price=161.02 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=14201030.0 spike=0.17
- OBRI.CA: score=15.76 buy_ready=False sector_rank=7 price=35.98 support=33.63 resistance=37.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=6006397.0 spike=0.44
- OCDI.CA: score=19.18 buy_ready=False sector_rank=3 price=21.29 support=20.0 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=15884206.0 spike=0.47
- OCPH.CA: score=8.74 buy_ready=False sector_rank=7 price=345.01 support=337.0 resistance=379.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=26.79 liquidity=4992206.0 spike=0.86
- ODIN.CA: score=18.23 buy_ready=False sector_rank=7 price=2.17 support=1.89 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=5473737.5 spike=0.5
- OFH.CA: score=15.2 buy_ready=False sector_rank=7 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=9443190.0 spike=0.41
- OIH.CA: score=7.39 buy_ready=False sector_rank=17 price=1.35 support=1.33 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=7708859.0 spike=0.09
- OLFI.CA: score=23.02 buy_ready=False sector_rank=5 price=22.08 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=18092406.0 spike=0.91
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=792.04 support=785.01 resistance=799.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=311075648.0 spike=1.0
- ORHD.CA: score=22.18 buy_ready=False sector_rank=3 price=38.1 support=33.51 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=49.64 liquidity=63269988.0 spike=0.35
- ORWE.CA: score=20.36 buy_ready=False sector_rank=11 price=23.2 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=13090032.0 spike=0.31
- PHAR.CA: score=7.17 buy_ready=False sector_rank=15 price=83.98 support=83.02 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=47.88 liquidity=2334665.0 spike=0.08
- PHDC.CA: score=22.18 buy_ready=False sector_rank=3 price=16.19 support=13.4 resistance=16.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=332961248.0 spike=0.8
- PHTV.CA: score=20.64 buy_ready=False sector_rank=7 price=219.5 support=201.55 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=63.1 liquidity=5892282.5 spike=0.35
- POUL.CA: score=19.3 buy_ready=False sector_rank=5 price=35.64 support=34.8 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=41144912.0 spike=1.14
- PRCL.CA: score=19.95 buy_ready=False sector_rank=14 price=25.29 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=62.78 liquidity=22473682.0 spike=0.8
- PRDC.CA: score=7.64 buy_ready=False sector_rank=3 price=8.47 support=7.72 resistance=8.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120578912.0 spike=1.23
- PRMH.CA: score=21.13 buy_ready=False sector_rank=7 price=2.8 support=2.21 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=70.63 liquidity=31585324.0 spike=1.19
- RACC.CA: score=5.91 buy_ready=False sector_rank=7 price=9.77 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=26.88 liquidity=2156266.25 spike=0.21
- RAKT.CA: score=7.25 buy_ready=False sector_rank=7 price=23.03 support=22.0 resistance=24.75 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=48.94 liquidity=520846.5 spike=1.99
- RAYA.CA: score=11.88 buy_ready=False sector_rank=20 price=7.05 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.59 liquidity=18846234.0 spike=0.2
- RMDA.CA: score=17.84 buy_ready=False sector_rank=15 price=5.08 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=52.66 liquidity=12498833.0 spike=0.15
- ROTO.CA: score=10.75 buy_ready=False sector_rank=7 price=39.0 support=35.7 resistance=39.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75278552.0 spike=5.57
- RREI.CA: score=20.75 buy_ready=False sector_rank=7 price=3.68 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=15740622.0 spike=0.74
- RTVC.CA: score=9.23 buy_ready=False sector_rank=7 price=3.82 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=3480242.0 spike=0.62
- RUBX.CA: score=7.42 buy_ready=False sector_rank=7 price=9.96 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=2669011.0 spike=0.23
- SAUD.CA: score=9.42 buy_ready=False sector_rank=4 price=21.71 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=36.8 liquidity=3375110.25 spike=0.31
- SCEM.CA: score=11.92 buy_ready=False sector_rank=14 price=62.0 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=6970671.5 spike=0.32
- SCFM.CA: score=1.87 buy_ready=False sector_rank=7 price=251.18 support=248.1 resistance=296.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=1113575.88 spike=0.09
- SCTS.CA: score=5.61 buy_ready=False sector_rank=10 price=600.09 support=565.25 resistance=668.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=2040110.0 spike=0.38
- SDTI.CA: score=22.75 buy_ready=False sector_rank=7 price=48.59 support=43.4 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=10758340.0 spike=0.73
- SEIG.CA: score=13.39 buy_ready=False sector_rank=7 price=186.52 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=2640372.5 spike=0.56
- SIPC.CA: score=14.49 buy_ready=False sector_rank=7 price=3.51 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=5740157.0 spike=0.45
- SKPC.CA: score=7.68 buy_ready=False sector_rank=21 price=16.13 support=16.16 resistance=17.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=33.46 liquidity=14539259.0 spike=0.28
- SMFR.CA: score=9.18 buy_ready=False sector_rank=7 price=203.87 support=192.0 resistance=218.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=42.73 liquidity=426003.63 spike=0.1
- SNFC.CA: score=14.22 buy_ready=False sector_rank=7 price=12.2 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=47.98 liquidity=5470309.5 spike=0.21
- SPIN.CA: score=1.46 buy_ready=False sector_rank=11 price=13.81 support=13.3 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=1102097.63 spike=0.24
- SPMD.CA: score=25.75 buy_ready=False sector_rank=7 price=0.43 support=0.39 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=52.43 liquidity=88328712.0 spike=3.74
- SUGR.CA: score=10.92 buy_ready=False sector_rank=5 price=48.72 support=48.0 resistance=51.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=2901930.75 spike=0.19
- SVCE.CA: score=20.81 buy_ready=False sector_rank=7 price=9.37 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=94207952.0 spike=1.03
- SWDY.CA: score=12.57 buy_ready=False sector_rank=12 price=86.67 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=4393375.5 spike=0.22
- TALM.CA: score=13.24 buy_ready=False sector_rank=10 price=16.24 support=15.12 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=77.6 liquidity=3666939.75 spike=0.46
- TMGH.CA: score=23.92 buy_ready=False sector_rank=3 price=97.65 support=92.91 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=853364928.0 spike=1.87
- TRTO.CA: score=6.75 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=10.0 buy_ready=False sector_rank=7 price=469.83 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=48.69 liquidity=1511475.88 spike=1.87
- UEGC.CA: score=15.81 buy_ready=False sector_rank=7 price=1.43 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=3056597.75 spike=0.12
- UNIP.CA: score=19.75 buy_ready=False sector_rank=7 price=0.33 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=85.92 liquidity=16021291.0 spike=0.67
- UNIT.CA: score=13.8 buy_ready=False sector_rank=3 price=13.6 support=12.25 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=58.26 liquidity=1623322.63 spike=0.21
- WCDF.CA: score=7.12 buy_ready=False sector_rank=7 price=537.53 support=450.0 resistance=550.0 source=Yahoo Finance as_of=2026-06-15T21:00:00+00:00 freshness=FRESH RSI=45.74 liquidity=466038.54 spike=1.45
- WKOL.CA: score=7.2 buy_ready=False sector_rank=7 price=288.18 support=289.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=1449582.5 spike=0.43
- ZEOT.CA: score=10.75 buy_ready=False sector_rank=7 price=12.96 support=11.0 resistance=13.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=200913680.0 spike=12.13
- ZMID.CA: score=22.18 buy_ready=False sector_rank=3 price=6.24 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=61917420.0 spike=0.29

## Backtesting Lite
- MTIE.CA: 180d return=40.36%, max drawdown=-20.49%, MA20>MA50 days last20=20, as_of=2026-06-15T21:00:00+00:00
- SPMD.CA: 180d return=29.81%, max drawdown=-15.63%, MA20>MA50 days last20=20, as_of=2026-06-15T21:00:00+00:00
- HDBK.CA: 180d return=134.47%, max drawdown=-12.66%, MA20>MA50 days last20=15, as_of=2026-06-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- SPMD.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Speed Medical Co summary=Speed Medical’s stock reflects strong technical breakthrough; Speed Medical turns to losses in 9M-22; Shareholder ups stake in Speed Medical for EGP 3.5m
  - Speed Medical’s stock reflects strong technical breakthrough: https://english.mubasher.info/news/4546374/Speed-Medical-s-stock-reflects-strong-technical-breakthrough/
  - Speed Medical turns to losses in 9M-22: https://english.mubasher.info/news/4054471/Speed-Medical-turns-to-losses-in-9M-22/
  - Shareholder ups stake in Speed Medical for EGP 3.5m: https://english.mubasher.info/news/4049449/Shareholder-ups-stake-in-Speed-Medical-for-EGP-3-5m/
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=532 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/
- ECAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Ezz Ceramics & Porcelain Co. summary=Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.

## Warnings
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SPMD.CA matches the company but no source/report date was detected.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
