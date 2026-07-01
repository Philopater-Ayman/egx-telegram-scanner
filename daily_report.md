# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-07-01T15:19:58.123994+00:00
Generated Cairo: 2026-07-01 18:19
Run timing: target 15:30 Cairo | generated Cairo 2026-07-01 18:19 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-07-01 18:17

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 177/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 01
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 40.0% / above MA50 35.0%
- EGX70 regime: BEARISH / above MA20 48.72% / above MA50 66.67%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=732462272.0 spike=1.11 score=5.19
- COMI.CA: liquidity=313894240.0 spike=0.53 score=15.4
- NIPH.CA: liquidity=304737952.0 spike=4.46 score=10.38
- BTFH.CA: liquidity=238822608.0 spike=1.3 score=15.07
- RUBX.CA: liquidity=206904560.0 spike=10.94 score=10.3

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (23.81%). Market risk mode is DEFENSIVE_NO_NEW_BUY, so new long entries are blocked despite several stocks showing bullish watch signals.
- EGX30/EGX70 trends bearish, median 5‑day returns negative, few stocks above MA20/MA50.
- Sector breadth low; only Technology, Automotive & Distribution and Education lead, but overall support is weak.
- Top‑ranked tickets (SCTS, NHPS, LCSW, MTIE, ELKA, RAYA) show bullish outlooks and accumulation spikes, yet market regime disallows new buys.
- Liquidity spikes indicate short‑term interest, but resistance levels are close (e.g., RAYA near 7.81) and RSI elevated on some.
- Uncertainty remains as sector leadership could shift; monitor any reversal in EGX30/EGX70 breadth before considering entries.

## Top Liquidity Spikes
- DTPP.CA: spike=45.8 liquidity=166073664.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NHPS.CA: spike=23.93 liquidity=107228104.0 outlook=BULLISH_WATCH score=85.25 buy_ready=False
- AXPH.CA: spike=14.97 liquidity=21492186.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=10.94 liquidity=206904560.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EBSC.CA: spike=8.26 liquidity=22478382.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=11.03 5d=8.17% 20d=2.67% aboveMA50=100.0%
- #2 Automotive & Distribution: score=10.83 5d=1.53% 20d=10.05% aboveMA50=100.0%
- #3 Education: score=7.07 5d=-1.75% 20d=0.67% aboveMA50=100.0%
- #4 Tourism & Leisure: score=5.7 5d=-4.44% 20d=2.64% aboveMA50=100.0%
- #5 Transportation & Logistics: score=4.91 5d=2.98% 20d=-0.3% aboveMA50=50.0%
- #6 Real Estate: score=3.81 5d=0.09% 20d=-2.39% aboveMA50=76.92%
- #7 Non-bank Financial Services: score=3.68 5d=-0.09% 20d=-1.73% aboveMA50=40.0%
- #8 Banking & Financials: score=3.49 5d=-1.56% 20d=-0.75% aboveMA50=60.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SCTS.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MTIE.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- OCPH.CA: BULLISH_WATCH score=91.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- LCSW.CA: BULLISH_WATCH score=90.26 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NHPS.CA: BULLISH_WATCH score=85.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EEII.CA: BULLISH_WATCH score=85.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CIRA.CA: BULLISH_WATCH score=82.07 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- MENA.CA: BULLISH_WATCH score=79.81 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CNFN.CA: BULLISH_WATCH score=79.68 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ECAP.CA: BULLISH_WATCH score=79.25 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=13.03 buy_ready=False sector_rank=11 price=206.24 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=4725759.5 spike=0.76
- ABUK.CA: score=8.67 buy_ready=False sector_rank=20 price=67.94 support=66.66 resistance=83.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=100987840.0 spike=0.76
- ACAMD.CA: score=18.3 buy_ready=False sector_rank=11 price=2.25 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=45176856.0 spike=0.36
- ACGC.CA: score=18.34 buy_ready=False sector_rank=10 price=9.23 support=8.92 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.66 liquidity=10555991.0 spike=0.31
- ADCI.CA: score=18.04 buy_ready=False sector_rank=11 price=240.97 support=211.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=76.1 liquidity=14193098.0 spike=1.37
- ADIB.CA: score=20.4 buy_ready=False sector_rank=8 price=46.64 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=75135304.0 spike=0.83
- ADPC.CA: score=8.61 buy_ready=False sector_rank=11 price=3.45 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=4307773.0 spike=0.23
- AFDI.CA: score=14.32 buy_ready=False sector_rank=11 price=44.34 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=4022391.75 spike=0.26
- AFMC.CA: score=6.96 buy_ready=False sector_rank=11 price=69.44 support=66.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=1656619.75 spike=0.72
- AJWA.CA: score=13.81 buy_ready=False sector_rank=11 price=179.07 support=132.15 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.37 liquidity=8513433.0 spike=0.31
- ALCN.CA: score=10.23 buy_ready=False sector_rank=5 price=28.34 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.9 liquidity=4266373.0 spike=0.35
- ALUM.CA: score=3.1 buy_ready=False sector_rank=11 price=21.45 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=2800217.0 spike=0.29
- AMER.CA: score=10.52 buy_ready=False sector_rank=6 price=2.42 support=2.28 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=35663152.0 spike=0.5
- AMES.CA: score=10.3 buy_ready=False sector_rank=11 price=60.51 support=60.12 resistance=69.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58644828.0 spike=4.8
- AMIA.CA: score=11.36 buy_ready=False sector_rank=11 price=8.72 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=3055805.25 spike=0.24
- AMOC.CA: score=9.5 buy_ready=False sector_rank=19 price=7.76 support=7.42 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.4 liquidity=26245326.0 spike=0.55
- ANFI.CA: score=6.63 buy_ready=False sector_rank=11 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=4.8 buy_ready=False sector_rank=11 price=8.48 support=8.0 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=36.94 liquidity=497076.97 spike=0.54
- ARAB.CA: score=15.52 buy_ready=False sector_rank=6 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=42145176.0 spike=0.53
- ARCC.CA: score=14.9 buy_ready=False sector_rank=15 price=55.44 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=14691625.0 spike=0.44
- AREH.CA: score=20.3 buy_ready=False sector_rank=11 price=1.56 support=1.34 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=23030056.0 spike=0.65
- ARVA.CA: score=15.32 buy_ready=False sector_rank=11 price=11.03 support=9.82 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.76 liquidity=7016517.5 spike=0.22
- ASCM.CA: score=20.3 buy_ready=False sector_rank=11 price=59.26 support=49.72 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.92 liquidity=34461340.0 spike=0.36
- ASPI.CA: score=18.3 buy_ready=False sector_rank=11 price=0.32 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.69 liquidity=12508170.0 spike=0.17
- ATLC.CA: score=15.17 buy_ready=False sector_rank=7 price=5.27 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.9 liquidity=4702671.5 spike=0.71
- ATQA.CA: score=12.99 buy_ready=False sector_rank=20 price=9.47 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=38879628.0 spike=1.16
- AXPH.CA: score=10.3 buy_ready=False sector_rank=11 price=1212.35 support=1090.02 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21492186.0 spike=14.97
- BINV.CA: score=9.22 buy_ready=False sector_rank=13 price=46.04 support=44.02 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=1251080.13 spike=0.15
- BIOC.CA: score=10.34 buy_ready=False sector_rank=11 price=71.48 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.18 liquidity=2044750.0 spike=0.8
- BTFH.CA: score=15.07 buy_ready=False sector_rank=7 price=2.97 support=2.95 resistance=3.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.07 liquidity=238822608.0 spike=1.3
- CAED.CA: score=15.63 buy_ready=False sector_rank=11 price=71.33 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=5111428.5 spike=1.11
- CANA.CA: score=9.67 buy_ready=False sector_rank=8 price=35.74 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.39 liquidity=2270395.0 spike=0.19
- CCAP.CA: score=5.19 buy_ready=False sector_rank=13 price=5.04 support=4.76 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=732462272.0 spike=1.11
- CCRS.CA: score=16.1 buy_ready=False sector_rank=11 price=2.32 support=2.18 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=7797416.5 spike=0.52
- CEFM.CA: score=6.04 buy_ready=False sector_rank=11 price=100.07 support=95.75 resistance=109.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=35.08 liquidity=740587.5 spike=0.42
- CERA.CA: score=17.3 buy_ready=False sector_rank=11 price=1.22 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=11219169.0 spike=0.66
- CFGH.CA: score=-0.7 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=707.6 spike=0.12
- CICH.CA: score=9.77 buy_ready=False sector_rank=7 price=11.87 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.96 liquidity=2295068.75 spike=0.79
- CIEB.CA: score=14.49 buy_ready=False sector_rank=8 price=23.92 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=4091537.75 spike=0.62
- CIRA.CA: score=21.92 buy_ready=False sector_rank=3 price=28.8 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.05 liquidity=29981598.0 spike=1.76
- CLHO.CA: score=20.38 buy_ready=False sector_rank=9 price=16.5 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=72.12 liquidity=36514660.0 spike=0.95
- CNFN.CA: score=22.47 buy_ready=False sector_rank=7 price=4.76 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=28663984.0 spike=0.68
- COMI.CA: score=15.4 buy_ready=False sector_rank=8 price=127.4 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=313894240.0 spike=0.53
- COPR.CA: score=13.92 buy_ready=False sector_rank=11 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=6620263.0 spike=0.25
- COSG.CA: score=10.3 buy_ready=False sector_rank=11 price=1.52 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=21887884.0 spike=0.41
- CPCI.CA: score=21.07 buy_ready=False sector_rank=11 price=404.91 support=350.04 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.94 liquidity=7752211.0 spike=3.01
- CSAG.CA: score=22.96 buy_ready=False sector_rank=5 price=32.58 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.76 liquidity=12244194.0 spike=0.69
- DAPH.CA: score=16.85 buy_ready=False sector_rank=11 price=82.29 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=4546382.0 spike=0.46
- DEIN.CA: score=6.3 buy_ready=False sector_rank=11 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.4 buy_ready=False sector_rank=12 price=27.23 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.08 liquidity=4157389.5 spike=1.04
- DSCW.CA: score=14.3 buy_ready=False sector_rank=11 price=1.73 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=22641850.0 spike=0.66
- DTPP.CA: score=10.3 buy_ready=False sector_rank=11 price=199.26 support=183.0 resistance=199.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=166073664.0 spike=45.8
- EALR.CA: score=2.89 buy_ready=False sector_rank=11 price=339.92 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=2588578.0 spike=0.85
- EASB.CA: score=21.38 buy_ready=False sector_rank=11 price=7.54 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.71 liquidity=20557628.0 spike=1.54
- EAST.CA: score=14.16 buy_ready=False sector_rank=12 price=37.26 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.07 liquidity=15903049.0 spike=0.41
- EBSC.CA: score=10.3 buy_ready=False sector_rank=11 price=2.1 support=1.74 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22478382.0 spike=8.26
- ECAP.CA: score=19.63 buy_ready=False sector_rank=11 price=32.72 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=9285182.0 spike=1.02
- EDFM.CA: score=0.55 buy_ready=False sector_rank=11 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=17.77 liquidity=246620.14 spike=0.52
- EEII.CA: score=22.88 buy_ready=False sector_rank=11 price=2.5 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=31285400.0 spike=2.29
- EFIC.CA: score=7.23 buy_ready=False sector_rank=20 price=186.24 support=180.02 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.61 liquidity=5860528.5 spike=2.85
- EFID.CA: score=15.16 buy_ready=False sector_rank=12 price=27.37 support=25.5 resistance=29.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.86 liquidity=17269084.0 spike=0.22
- EFIH.CA: score=13.18 buy_ready=False sector_rank=21 price=20.93 support=20.0 resistance=22.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.98 liquidity=32684706.0 spike=0.78
- EGAL.CA: score=8.67 buy_ready=False sector_rank=20 price=285.88 support=272.28 resistance=332.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.65 liquidity=29877492.0 spike=0.49
- EGAS.CA: score=10.54 buy_ready=False sector_rank=19 price=49.63 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=3046260.25 spike=0.36
- EGBE.CA: score=10.4 buy_ready=False sector_rank=8 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.36 liquidity=7978.92 spike=0.09
- EGCH.CA: score=8.67 buy_ready=False sector_rank=20 price=12.25 support=12.13 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.58 liquidity=21150138.0 spike=0.4
- EGSA.CA: score=2.68 buy_ready=False sector_rank=17 price=8.75 support=8.55 resistance=9.09 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=85.71 liquidity=446.25 spike=0.05
- EGTS.CA: score=18.52 buy_ready=False sector_rank=6 price=17.7 support=15.1 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=61890540.0 spike=0.71
- EHDR.CA: score=18.3 buy_ready=False sector_rank=11 price=2.5 support=2.37 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=13270348.0 spike=0.23
- EKHO.CA: score=6.5 buy_ready=False sector_rank=19 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.95 buy_ready=False sector_rank=14 price=2.1 support=2.04 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=11326406.0 spike=0.64
- ELKA.CA: score=24.76 buy_ready=False sector_rank=11 price=1.36 support=1.19 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=120265288.0 spike=2.73
- ELNA.CA: score=-0.03 buy_ready=False sector_rank=11 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=33.8 liquidity=486123.19 spike=1.09
- ELSH.CA: score=13.3 buy_ready=False sector_rank=11 price=11.61 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.76 liquidity=33954560.0 spike=0.18
- ELWA.CA: score=1.49 buy_ready=False sector_rank=11 price=1.95 support=1.95 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.61 liquidity=1191679.75 spike=0.41
- EMFD.CA: score=18.52 buy_ready=False sector_rank=6 price=11.56 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.12 liquidity=58757656.0 spike=0.2
- ENGC.CA: score=18.81 buy_ready=False sector_rank=11 price=36.6 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.74 liquidity=6509244.0 spike=0.44
- EOSB.CA: score=12.33 buy_ready=False sector_rank=11 price=1.48 support=1.39 resistance=1.55 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=28383.44 spike=0.22
- EPCO.CA: score=7.85 buy_ready=False sector_rank=11 price=8.7 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.13 liquidity=2546007.25 spike=0.32
- EPPK.CA: score=9.89 buy_ready=False sector_rank=11 price=14.19 support=11.67 resistance=13.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=80.49 liquidity=587907.44 spike=0.45
- ETEL.CA: score=16.68 buy_ready=False sector_rank=17 price=93.98 support=89.01 resistance=97.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=25011672.0 spike=0.35
- ETRS.CA: score=22.3 buy_ready=False sector_rank=11 price=10.6 support=8.6 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.41 liquidity=78709920.0 spike=0.96
- EXPA.CA: score=10.4 buy_ready=False sector_rank=8 price=18.33 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.56 liquidity=22651058.0 spike=0.72
- FAIT.CA: score=14.88 buy_ready=False sector_rank=8 price=36.98 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=3868023.0 spike=1.31
- FAITA.CA: score=5.42 buy_ready=False sector_rank=8 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=40.63 liquidity=26241.46 spike=0.67
- FERC.CA: score=0.27 buy_ready=False sector_rank=20 price=73.55 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.2 liquidity=2602970.5 spike=0.66
- FWRY.CA: score=13.18 buy_ready=False sector_rank=21 price=18.37 support=17.71 resistance=20.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=103475176.0 spike=0.43
- GBCO.CA: score=22.4 buy_ready=False sector_rank=2 price=32.07 support=25.25 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=89.02 liquidity=33470152.0 spike=0.36
- GDWA.CA: score=11.31 buy_ready=False sector_rank=11 price=0.76 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.5 liquidity=7009877.5 spike=0.48
- GGCC.CA: score=20.52 buy_ready=False sector_rank=11 price=0.49 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=87.0 liquidity=26574294.0 spike=2.11
- GIHD.CA: score=13.51 buy_ready=False sector_rank=11 price=42.06 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.39 liquidity=3208119.0 spike=0.37
- GMCI.CA: score=17.24 buy_ready=False sector_rank=11 price=1.86 support=1.66 resistance=1.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=1364752.12 spike=2.79
- GRCA.CA: score=6.61 buy_ready=False sector_rank=11 price=52.29 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=1307839.25 spike=0.31
- GSSC.CA: score=7.6 buy_ready=False sector_rank=11 price=244.44 support=228.1 resistance=256.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=2295315.0 spike=0.8
- GTWL.CA: score=24.3 buy_ready=False sector_rank=11 price=89.74 support=45.47 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=91.91 liquidity=198041456.0 spike=6.08
- HDBK.CA: score=20.6 buy_ready=False sector_rank=8 price=166.67 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=33022358.0 spike=1.1
- HELI.CA: score=18.52 buy_ready=False sector_rank=6 price=6.43 support=6.28 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=64413432.0 spike=0.58
- HRHO.CA: score=17.47 buy_ready=False sector_rank=7 price=26.96 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.31 liquidity=68994456.0 spike=0.52
- ICID.CA: score=13.25 buy_ready=False sector_rank=11 price=7.98 support=5.5 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.53 liquidity=3946186.75 spike=0.22
- IDRE.CA: score=18.86 buy_ready=False sector_rank=11 price=43.65 support=41.1 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=16758671.0 spike=1.28
- IFAP.CA: score=7.48 buy_ready=False sector_rank=16 price=19.33 support=18.47 resistance=20.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=1610330.5 spike=0.24
- INFI.CA: score=5.59 buy_ready=False sector_rank=11 price=93.41 support=88.51 resistance=104.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.06 liquidity=6212746.5 spike=1.04
- IRON.CA: score=10.17 buy_ready=False sector_rank=20 price=32.21 support=30.51 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=5501174.5 spike=0.71
- ISMA.CA: score=13.3 buy_ready=False sector_rank=11 price=28.15 support=26.22 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.38 liquidity=17405066.0 spike=0.51
- ISMQ.CA: score=18.95 buy_ready=False sector_rank=20 price=9.34 support=7.56 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.4 liquidity=135351088.0 spike=1.14
- ISPH.CA: score=15.38 buy_ready=False sector_rank=9 price=11.61 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=20858842.0 spike=0.19
- JUFO.CA: score=16.68 buy_ready=False sector_rank=12 price=29.99 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.92 liquidity=8522418.0 spike=0.27
- KABO.CA: score=20.34 buy_ready=False sector_rank=10 price=6.33 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.08 liquidity=13916596.0 spike=0.87
- KWIN.CA: score=10.37 buy_ready=False sector_rank=11 price=67.44 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.07 liquidity=6074898.5 spike=0.52
- KZPC.CA: score=2.06 buy_ready=False sector_rank=11 price=8.47 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=8.85 liquidity=2760068.5 spike=0.44
- LCSW.CA: score=26.9 buy_ready=False sector_rank=15 price=28.25 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.63 liquidity=107994776.0 spike=3.56
- LUTS.CA: score=18.3 buy_ready=False sector_rank=11 price=0.74 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=24073904.0 spike=0.5
- MAAL.CA: score=19.3 buy_ready=False sector_rank=11 price=7.25 support=5.44 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=85.87 liquidity=11619887.0 spike=0.65
- MASR.CA: score=20.42 buy_ready=False sector_rank=11 price=7.4 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=67175216.0 spike=1.06
- MBSC.CA: score=8.1 buy_ready=False sector_rank=15 price=242.18 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=8196867.5 spike=0.25
- MCQE.CA: score=10.2 buy_ready=False sector_rank=15 price=172.1 support=166.66 resistance=199.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.8 liquidity=15920868.0 spike=1.15
- MCRO.CA: score=14.3 buy_ready=False sector_rank=11 price=1.2 support=1.17 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=15457899.0 spike=0.45
- MENA.CA: score=17.52 buy_ready=False sector_rank=6 price=6.89 support=6.41 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=6991105.5 spike=0.55
- MEPA.CA: score=4.8 buy_ready=False sector_rank=11 price=1.57 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.92 liquidity=5504812.0 spike=0.5
- MFPC.CA: score=8.67 buy_ready=False sector_rank=20 price=35.72 support=34.22 resistance=43.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.93 liquidity=49545416.0 spike=0.6
- MFSC.CA: score=7.8 buy_ready=False sector_rank=11 price=49.48 support=47.0 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17921326.0 spike=2.25
- MHOT.CA: score=21.28 buy_ready=False sector_rank=4 price=33.98 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.18 liquidity=11601942.0 spike=0.63
- MICH.CA: score=15.55 buy_ready=False sector_rank=11 price=37.54 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.63 liquidity=5252988.5 spike=0.34
- MILS.CA: score=9.4 buy_ready=False sector_rank=11 price=129.64 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=4101866.25 spike=0.44
- MIPH.CA: score=8.77 buy_ready=False sector_rank=9 price=658.44 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=385217.91 spike=0.22
- MOED.CA: score=10.79 buy_ready=False sector_rank=11 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=48.63 liquidity=4493470.0 spike=0.49
- MOIL.CA: score=7.62 buy_ready=False sector_rank=19 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=124751.98 spike=0.63
- MOIN.CA: score=4.85 buy_ready=False sector_rank=11 price=23.73 support=22.6 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.45 liquidity=546637.38 spike=0.54
- MOSC.CA: score=8.71 buy_ready=False sector_rank=11 price=267.72 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=3406330.75 spike=0.36
- MPCI.CA: score=20.92 buy_ready=False sector_rank=11 price=246.0 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.99 liquidity=127311624.0 spike=1.31
- MPCO.CA: score=17.87 buy_ready=False sector_rank=16 price=1.84 support=1.6 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=32336042.0 spike=0.3
- MPRC.CA: score=19.3 buy_ready=False sector_rank=11 price=38.62 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=85.5 liquidity=32627008.0 spike=0.75
- MTIE.CA: score=26.58 buy_ready=False sector_rank=2 price=9.34 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=43029624.0 spike=2.59
- NAHO.CA: score=10.18 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=84760.25 spike=2.9
- NCCW.CA: score=18.3 buy_ready=False sector_rank=11 price=6.16 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=10492195.0 spike=0.31
- NEDA.CA: score=6.26 buy_ready=False sector_rank=11 price=2.75 support=2.68 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=500130.84 spike=1.23
- NHPS.CA: score=29.3 buy_ready=False sector_rank=11 price=68.0 support=61.55 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.04 liquidity=107228104.0 spike=23.93
- NINH.CA: score=21.28 buy_ready=False sector_rank=11 price=18.06 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.37 liquidity=16143680.0 spike=2.99
- NIPH.CA: score=10.38 buy_ready=False sector_rank=9 price=180.06 support=165.0 resistance=181.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=304737952.0 spike=4.46
- OBRI.CA: score=10.3 buy_ready=False sector_rank=11 price=34.94 support=33.12 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80582992.0 spike=5.42
- OCDI.CA: score=18.44 buy_ready=False sector_rank=6 price=25.36 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.98 liquidity=113697808.0 spike=1.46
- OCPH.CA: score=21.9 buy_ready=False sector_rank=11 price=356.52 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.93 liquidity=11507692.0 spike=1.8
- ODIN.CA: score=20.32 buy_ready=False sector_rank=11 price=2.18 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.66 liquidity=11236753.0 spike=1.01
- OFH.CA: score=14.3 buy_ready=False sector_rank=11 price=0.6 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.57 liquidity=12189206.0 spike=0.64
- OIH.CA: score=18.97 buy_ready=False sector_rank=13 price=1.41 support=1.33 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=63213592.0 spike=0.83
- OLFI.CA: score=20.34 buy_ready=False sector_rank=12 price=22.29 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.59 liquidity=23131916.0 spike=1.09
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=720.42 support=720.0 resistance=733.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156812608.0 spike=1.0
- ORHD.CA: score=20.52 buy_ready=False sector_rank=6 price=38.25 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.76 liquidity=76794560.0 spike=0.44
- ORWE.CA: score=10.34 buy_ready=False sector_rank=10 price=22.39 support=21.95 resistance=24.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=13097640.0 spike=0.38
- PHAR.CA: score=20.38 buy_ready=False sector_rank=9 price=88.21 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.96 liquidity=22833844.0 spike=0.64
- PHDC.CA: score=18.52 buy_ready=False sector_rank=6 price=14.58 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=184163824.0 spike=0.48
- PHTV.CA: score=11.81 buy_ready=False sector_rank=11 price=272.72 support=201.55 resistance=277.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=95.04 liquidity=2508755.5 spike=0.18
- POUL.CA: score=22.7 buy_ready=False sector_rank=12 price=38.0 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=44449216.0 spike=1.27
- PRCL.CA: score=6.06 buy_ready=False sector_rank=15 price=33.0 support=30.83 resistance=33.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65773180.0 spike=1.58
- PRDC.CA: score=18.52 buy_ready=False sector_rank=6 price=7.7 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=67772056.0 spike=0.56
- PRMH.CA: score=18.3 buy_ready=False sector_rank=11 price=2.57 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=20797446.0 spike=0.66
- RACC.CA: score=14.05 buy_ready=False sector_rank=11 price=9.85 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.0 liquidity=3753531.75 spike=0.44
- RAKT.CA: score=1.18 buy_ready=False sector_rank=11 price=21.67 support=21.4 resistance=24.1 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=29.78 liquidity=456456.88 spike=1.71
- RAYA.CA: score=24.4 buy_ready=False sector_rank=1 price=7.67 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=70436032.0 spike=0.82
- RMDA.CA: score=17.59 buy_ready=False sector_rank=9 price=5.01 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.17 liquidity=9212136.0 spike=0.12
- ROTO.CA: score=20.3 buy_ready=False sector_rank=11 price=41.48 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.17 liquidity=24024040.0 spike=0.8
- RREI.CA: score=11.27 buy_ready=False sector_rank=11 price=3.47 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=5972465.5 spike=0.36
- RTVC.CA: score=6.9 buy_ready=False sector_rank=11 price=3.79 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=1600428.5 spike=0.3
- RUBX.CA: score=10.3 buy_ready=False sector_rank=11 price=12.35 support=11.22 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=206904560.0 spike=10.94
- SAUD.CA: score=10.08 buy_ready=False sector_rank=8 price=21.09 support=19.99 resistance=22.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.19 liquidity=4686513.0 spike=0.56
- SCEM.CA: score=19.9 buy_ready=False sector_rank=15 price=63.32 support=59.3 resistance=66.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.52 liquidity=10562418.0 spike=0.61
- SCFM.CA: score=2.83 buy_ready=False sector_rank=11 price=238.16 support=226.5 resistance=269.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=2534596.25 spike=0.57
- SCTS.CA: score=29.4 buy_ready=False sector_rank=3 price=626.62 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.45 liquidity=15266653.0 spike=3.88
- SDTI.CA: score=11.87 buy_ready=False sector_rank=11 price=46.44 support=44.35 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=3569111.25 spike=0.31
- SEIG.CA: score=13.34 buy_ready=False sector_rank=11 price=190.54 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.3 liquidity=3036388.25 spike=0.74
- SIPC.CA: score=4.58 buy_ready=False sector_rank=11 price=3.38 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=4282196.5 spike=0.37
- SKPC.CA: score=7.67 buy_ready=False sector_rank=20 price=15.88 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=22193644.0 spike=0.66
- SMFR.CA: score=5.71 buy_ready=False sector_rank=11 price=194.67 support=187.01 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=38.45 liquidity=407025.59 spike=0.2
- SNFC.CA: score=18.3 buy_ready=False sector_rank=11 price=12.08 support=11.68 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.47 liquidity=11049329.0 spike=0.68
- SPIN.CA: score=14.25 buy_ready=False sector_rank=10 price=14.17 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=6671999.0 spike=1.12
- SPMD.CA: score=19.58 buy_ready=False sector_rank=11 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=9278192.0 spike=0.38
- SUGR.CA: score=2.09 buy_ready=False sector_rank=12 price=46.92 support=45.31 resistance=51.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.88 liquidity=2931202.5 spike=0.39
- SVCE.CA: score=8.16 buy_ready=False sector_rank=11 price=9.63 support=8.96 resistance=9.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=150555248.0 spike=2.43
- SWDY.CA: score=17.92 buy_ready=False sector_rank=14 price=87.0 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.08 liquidity=7963421.0 spike=0.46
- TALM.CA: score=17.95 buy_ready=False sector_rank=3 price=15.8 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.76 liquidity=7488742.0 spike=1.03
- TMGH.CA: score=15.52 buy_ready=False sector_rank=6 price=94.97 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=202932544.0 spike=0.56
- TRTO.CA: score=6.3 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=8.79 buy_ready=False sector_rank=11 price=477.14 support=460.0 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=47.04 liquidity=490908.09 spike=0.48
- UEGC.CA: score=20.3 buy_ready=False sector_rank=11 price=1.45 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=10940621.0 spike=0.45
- UNIP.CA: score=13.46 buy_ready=False sector_rank=11 price=0.33 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.44 liquidity=3161587.0 spike=0.13
- UNIT.CA: score=5.13 buy_ready=False sector_rank=6 price=12.95 support=12.0 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.74 liquidity=1607576.5 spike=0.24
- WCDF.CA: score=11.73 buy_ready=False sector_rank=11 price=506.06 support=450.0 resistance=547.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=1427213.63 spike=4.52
- WKOL.CA: score=1.12 buy_ready=False sector_rank=11 price=281.12 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=19.72 liquidity=819982.44 spike=0.3
- ZEOT.CA: score=21.2 buy_ready=False sector_rank=11 price=11.04 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=46621616.0 spike=1.45
- ZMID.CA: score=22.52 buy_ready=False sector_rank=6 price=6.49 support=5.96 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=96645864.0 spike=0.45

## Backtesting Lite
- SCTS.CA: 180d return=237.76%, max drawdown=-25.28%, MA20>MA50 days last20=16, as_of=2026-06-29T21:00:00+00:00
- NHPS.CA: 180d return=5.84%, max drawdown=-40.18%, MA20>MA50 days last20=12, as_of=2026-06-29T21:00:00+00:00
- LCSW.CA: 180d return=4.49%, max drawdown=-15.87%, MA20>MA50 days last20=20, as_of=2026-06-29T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SCTS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Suez Canal Company for Technology Settling summary=Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26; Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends; Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24
  - Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26: https://english.mubasher.info/news/4600018/Suez-Canal-Technology-s-consolidated-net-profits-cross-EGP-1-5bn-in-H1-25-26/
  - Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends: https://english.mubasher.info/news/4463096/Suez-Canal-Technology-s-shareholders-greenlight-EGP-11-shr-dividends/
  - Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24: https://english.mubasher.info/news/4366060/Suez-Canal-Technology-logs-EGP-1-3bn-consolidated-profits-in-FY23-24/
- NHPS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=National Company for Housing Professional Syndicates SAE summary=Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- ELKA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Cairo for Housing and Development Company (S.A.E) summary=Cairo for Housing’s consolidated profits near EGP 599m in 2025; Cairo Housing stock tests important demand zone; Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium
  - Cairo for Housing’s consolidated profits near EGP 599m in 2025: https://english.mubasher.info/news/4579798/Cairo-for-Housing-s-consolidated-profits-near-EGP-599m-in-2025/
  - Cairo Housing stock tests important demand zone: https://english.mubasher.info/news/4547365/Cairo-Housing-stock-tests-important-demand-zone/
  - Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium: https://english.mubasher.info/news/4540047/Cairo-Housing-unveils-EGP-398m-capital-hike-via-H1-25-s-share-premium/
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- GTWL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Golden Textiles & Clothes Wool summary=Golden Textiles profits jump 214%; Golden Textiles OGM OKs 50 piasters/shr dividends; Golden Textiles consolidated profits down 18.5% in FY16
  - Golden Textiles profits jump 214%: https://english.mubasher.info/news/3108548/Golden-Textiles-profits-jump-214-/
  - Golden Textiles OGM OKs 50 piasters/shr dividends: https://english.mubasher.info/news/3103061/Golden-Textiles-OGM-OKs-50-piasters-shr-dividends/
  - Golden Textiles consolidated profits down 18.5% in FY16: https://english.mubasher.info/news/3092552/Golden-Textiles-consolidated-profits-down-18-5-in-FY16/
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/

## Warnings
- Evidence for SCTS.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for NHPS.CA: source text did not clearly match NHPS.CA / National Company for Housing Professional Syndicates SAE.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence for ELKA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence for CSAG.CA matches the company but no source/report date was detected.
