# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-06-23T18:25:43.547303+00:00
Generated Cairo: 2026-06-23 21:25
Run timing: target 19:30 Cairo | generated Cairo 2026-06-23 21:25 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-06-23 21:18

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 165/190
- Top sector: Healthcare

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 23
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 35.0% / above MA50 45.0%
- EGX70 regime: BEARISH / above MA20 38.24% / above MA50 67.65%
- Sector breadth: 28.57%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=553776576.0 spike=0.7 score=18.5
- COMI.CA: liquidity=497594336.0 spike=0.85 score=21.65
- CNFN.CA: liquidity=398605920.0 spike=24.31 score=11.04
- ASCM.CA: liquidity=377160992.0 spike=5.65 score=10.52
- ORAS.CA: liquidity=349066208.0 spike=1.0 score=4.6

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (≈28%). Risk mode is DEFENSIVE_NO_NEW_BUY, so new entries are blocked despite several stocks showing bullish watch signals. Liquidity spikes and support/resistance levels suggest short‑term upside potential for a few tickets, but the overall market outlook remains uncertain for the next 1‑3 days.
- EGX30/EGX70 trends bearish, MA20/MA50 breadth weak → defensive stance.
- Sector breadth low; only Healthcare, Industrial Goods & Cables, Real Estate lead.
- Top tickets (OCDI, CLHO, ISPH) have accumulation spikes and support ~10‑15% below price, but market risk flags prevent buys.
- Liquidity spikes indicate temporary buying interest, yet resistance near current levels may cap moves.
- Uncertainty remains high; monitor any shift in breadth or regime before considering new positions.

## Top Liquidity Spikes
- CNFN.CA: spike=24.31 liquidity=398605920.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GIHD.CA: spike=18.29 liquidity=57913700.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DOMT.CA: spike=11.6 liquidity=24551274.0 outlook=BULLISH_WATCH score=88.24 buy_ready=False
- MPRC.CA: spike=7.54 liquidity=161637056.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ASCM.CA: spike=5.65 liquidity=377160992.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Healthcare: score=8.31 5d=3.13% 20d=5.12% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=6.37 5d=1.46% 20d=1.89% aboveMA50=50.0%
- #3 Real Estate: score=6.16 5d=1.63% 20d=5.26% aboveMA50=84.62%
- #4 Technology & Distribution: score=6.14 5d=6.14% 20d=-2.88% aboveMA50=100.0%
- #5 Agriculture & Food Production: score=5.45 5d=-1.64% 20d=8.88% aboveMA50=50.0%
- #6 Telecommunications: score=5.44 5d=1.51% 20d=-3.06% aboveMA50=100.0%
- #7 Non-bank Financial Services: score=5.1 5d=3.08% 20d=1.63% aboveMA50=40.0%
- #8 Education: score=5.01 5d=-0.06% 20d=5.23% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- OCDI.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- CLHO.CA: BULLISH_WATCH score=99.31 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- NIPH.CA: BULLISH_WATCH score=99.31 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- PHAR.CA: BULLISH_WATCH score=96.31 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORHD.CA: BULLISH_WATCH score=94.16 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PHDC.CA: BULLISH_WATCH score=92.16 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ATLC.CA: BULLISH_WATCH score=92.1 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- ZMID.CA: BULLISH_WATCH score=91.16 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- ISPH.CA: BULLISH_WATCH score=88.31 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- DOMT.CA: BULLISH_WATCH score=88.24 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=10.34 buy_ready=False sector_rank=12 price=205.8 support=199.25 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=1824633.63 spike=0.29
- ABUK.CA: score=9.33 buy_ready=False sector_rank=20 price=68.6 support=70.5 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=8.05 liquidity=104217432.0 spike=0.7
- ACAMD.CA: score=5.58 buy_ready=False sector_rank=12 price=2.25 support=2.23 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=129613224.0 spike=1.03
- ACGC.CA: score=18.01 buy_ready=False sector_rank=16 price=9.35 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=17991582.0 spike=0.31
- ADCI.CA: score=22.16 buy_ready=False sector_rank=12 price=240.0 support=211.0 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.84 liquidity=18051340.0 spike=2.32
- ADIB.CA: score=15.65 buy_ready=False sector_rank=11 price=45.71 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=55635644.0 spike=0.52
- ADPC.CA: score=5.52 buy_ready=False sector_rank=12 price=3.68 support=3.67 resistance=3.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19242718.0 spike=0.72
- AFDI.CA: score=24.46 buy_ready=False sector_rank=12 price=46.19 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.44 liquidity=40460832.0 spike=2.97
- AFMC.CA: score=7.53 buy_ready=False sector_rank=12 price=70.08 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=2017054.5 spike=0.42
- AJWA.CA: score=17.52 buy_ready=False sector_rank=12 price=179.0 support=130.01 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=84.42 liquidity=22078486.0 spike=0.83
- ALCN.CA: score=6.22 buy_ready=False sector_rank=17 price=28.07 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.02 liquidity=6313710.0 spike=0.44
- ALUM.CA: score=12.36 buy_ready=False sector_rank=12 price=22.87 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=3846140.0 spike=0.34
- AMER.CA: score=12.4 buy_ready=False sector_rank=3 price=2.38 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=54269420.0 spike=0.61
- AMES.CA: score=10.07 buy_ready=False sector_rank=12 price=48.93 support=48.0 resistance=53.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.12 liquidity=2554645.5 spike=0.73
- AMIA.CA: score=-0.48 buy_ready=False sector_rank=12 price=8.65 support=8.6 resistance=8.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4004947.5 spike=0.28
- AMOC.CA: score=11.0 buy_ready=False sector_rank=9 price=7.6 support=7.71 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.2 liquidity=59756724.0 spike=0.85
- ANFI.CA: score=10.79 buy_ready=False sector_rank=12 price=33.12 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=76.32 liquidity=3274408.69 spike=0.04
- APSW.CA: score=0.03 buy_ready=False sector_rank=12 price=8.56 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.33 liquidity=509497.63 spike=0.55
- ARAB.CA: score=22.4 buy_ready=False sector_rank=3 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=61375128.0 spike=0.72
- ARCC.CA: score=14.58 buy_ready=False sector_rank=19 price=55.15 support=54.31 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.83 liquidity=16323056.0 spike=0.46
- AREH.CA: score=19.52 buy_ready=False sector_rank=12 price=1.58 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.85 liquidity=25459960.0 spike=0.82
- ARVA.CA: score=20.52 buy_ready=False sector_rank=12 price=11.11 support=7.81 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=18760130.0 spike=0.57
- ASCM.CA: score=10.52 buy_ready=False sector_rank=12 price=63.31 support=63.01 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=377160992.0 spike=5.65
- ASPI.CA: score=5.52 buy_ready=False sector_rank=12 price=0.31 support=0.31 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19765236.0 spike=0.28
- ATLC.CA: score=26.58 buy_ready=False sector_rank=7 price=5.13 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=14816551.0 spike=2.77
- ATQA.CA: score=13.33 buy_ready=False sector_rank=20 price=9.29 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.49 liquidity=11902703.0 spike=0.35
- AXPH.CA: score=11.38 buy_ready=False sector_rank=12 price=1125.93 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.39 liquidity=861751.69 spike=0.47
- BINV.CA: score=11.96 buy_ready=False sector_rank=13 price=47.33 support=42.9 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=1454436.63 spike=0.14
- BIOC.CA: score=16.69 buy_ready=False sector_rank=12 price=73.19 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.54 liquidity=4673185.0 spike=1.75
- BTFH.CA: score=17.04 buy_ready=False sector_rank=7 price=3.04 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=156608928.0 spike=0.76
- CAED.CA: score=20.59 buy_ready=False sector_rank=12 price=71.27 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.39 liquidity=7393213.5 spike=1.34
- CANA.CA: score=19.52 buy_ready=False sector_rank=11 price=36.84 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.15 liquidity=6866434.5 spike=0.71
- CCAP.CA: score=18.5 buy_ready=False sector_rank=13 price=5.09 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=553776576.0 spike=0.7
- CCRS.CA: score=17.88 buy_ready=False sector_rank=12 price=2.38 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.89 liquidity=9361834.0 spike=0.4
- CEFM.CA: score=1.79 buy_ready=False sector_rank=12 price=101.25 support=100.53 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=27.36 liquidity=1275520.25 spike=0.39
- CERA.CA: score=19.52 buy_ready=False sector_rank=12 price=1.23 support=1.14 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.0 liquidity=10791307.0 spike=0.67
- CFGH.CA: score=-0.48 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- CICH.CA: score=13.52 buy_ready=False sector_rank=7 price=11.9 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=4159690.25 spike=1.16
- CIEB.CA: score=25.05 buy_ready=False sector_rank=11 price=24.37 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.74 liquidity=9574781.0 spike=1.41
- CIRA.CA: score=22.7 buy_ready=False sector_rank=8 price=28.7 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.92 liquidity=34023824.0 spike=1.85
- CLHO.CA: score=29.4 buy_ready=False sector_rank=1 price=16.34 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.29 liquidity=122293064.0 spike=4.78
- CNFN.CA: score=11.04 buy_ready=False sector_rank=7 price=5.12 support=4.72 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=398605920.0 spike=24.31
- COMI.CA: score=21.65 buy_ready=False sector_rank=11 price=134.0 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=497594336.0 spike=0.85
- COPR.CA: score=5.52 buy_ready=False sector_rank=12 price=0.36 support=0.36 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22620510.0 spike=0.52
- COSG.CA: score=18.52 buy_ready=False sector_rank=12 price=1.56 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=22476224.0 spike=0.36
- CPCI.CA: score=12.2 buy_ready=False sector_rank=12 price=373.12 support=346.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=73.6 liquidity=1683292.75 spike=0.82
- CSAG.CA: score=17.48 buy_ready=False sector_rank=17 price=31.21 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.26 liquidity=9577859.0 spike=0.82
- DAPH.CA: score=14.53 buy_ready=False sector_rank=12 price=80.32 support=76.6 resistance=82.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=52.65 liquidity=3014848.0 spike=0.31
- DEIN.CA: score=6.52 buy_ready=False sector_rank=12 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=29.7 buy_ready=False sector_rank=10 price=27.41 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.63 liquidity=24551274.0 spike=11.6
- DSCW.CA: score=16.52 buy_ready=False sector_rank=12 price=1.8 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=22967286.0 spike=0.45
- DTPP.CA: score=1.08 buy_ready=False sector_rank=12 price=116.28 support=114.0 resistance=131.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=10.98 liquidity=559468.81 spike=0.3
- EALR.CA: score=11.92 buy_ready=False sector_rank=12 price=357.58 support=350.15 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.3 liquidity=1407750.13 spike=0.4
- EASB.CA: score=6.94 buy_ready=False sector_rank=12 price=7.41 support=7.31 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12514415.0 spike=1.71
- EAST.CA: score=16.7 buy_ready=False sector_rank=10 price=37.87 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=32618586.0 spike=0.73
- EBSC.CA: score=14.22 buy_ready=False sector_rank=12 price=1.84 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=1708150.0 spike=0.64
- ECAP.CA: score=17.92 buy_ready=False sector_rank=12 price=32.93 support=29.36 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=94.89 liquidity=7839383.0 spike=1.28
- EDFM.CA: score=8.52 buy_ready=False sector_rank=12 price=332.0 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=35.25 liquidity=0.0 spike=0.0
- EEII.CA: score=22.19 buy_ready=False sector_rank=12 price=2.41 support=2.29 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=7673433.0 spike=0.46
- EFIC.CA: score=-1.2 buy_ready=False sector_rank=20 price=199.07 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=23.61 liquidity=472454.56 spike=0.21
- EFID.CA: score=10.7 buy_ready=False sector_rank=10 price=27.58 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.77 liquidity=24421352.0 spike=0.33
- EFIH.CA: score=13.82 buy_ready=False sector_rank=21 price=20.99 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.27 liquidity=18783752.0 spike=0.36
- EGAL.CA: score=9.67 buy_ready=False sector_rank=20 price=286.23 support=294.99 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=13.55 liquidity=88824272.0 spike=1.17
- EGAS.CA: score=12.11 buy_ready=False sector_rank=9 price=51.22 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.92 liquidity=3102603.75 spike=0.25
- EGBE.CA: score=8.75 buy_ready=False sector_rank=11 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=94966.31 spike=0.9
- EGCH.CA: score=4.33 buy_ready=False sector_rank=20 price=12.87 support=12.8 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29574662.0 spike=0.38
- EGSA.CA: score=4.18 buy_ready=False sector_rank=6 price=8.78 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=0.0 spike=0.0
- EGTS.CA: score=15.4 buy_ready=False sector_rank=3 price=17.67 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=34746140.0 spike=0.28
- EHDR.CA: score=18.52 buy_ready=False sector_rank=12 price=2.58 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=37706868.0 spike=0.67
- EKHO.CA: score=11.0 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.4 buy_ready=False sector_rank=2 price=2.12 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=20728082.0 spike=0.9
- ELKA.CA: score=5.52 buy_ready=False sector_rank=12 price=1.24 support=1.23 resistance=1.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35614208.0 spike=0.88
- ELNA.CA: score=7.38 buy_ready=False sector_rank=12 price=37.96 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.56 liquidity=799742.5 spike=2.03
- ELSH.CA: score=5.52 buy_ready=False sector_rank=12 price=12.05 support=11.99 resistance=12.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50211536.0 spike=0.27
- ELWA.CA: score=10.18 buy_ready=False sector_rank=12 price=2.05 support=1.87 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=1664726.63 spike=0.53
- EMFD.CA: score=20.4 buy_ready=False sector_rank=3 price=11.63 support=10.4 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.13 liquidity=99852328.0 spike=0.36
- ENGC.CA: score=17.49 buy_ready=False sector_rank=12 price=36.8 support=32.61 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=74.34 liquidity=4974777.5 spike=0.35
- EOSB.CA: score=12.52 buy_ready=False sector_rank=12 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=12.07 buy_ready=False sector_rank=12 price=9.08 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=4554834.5 spike=0.47
- EPPK.CA: score=11.93 buy_ready=False sector_rank=12 price=12.52 support=11.67 resistance=13.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=414680.53 spike=0.42
- ETEL.CA: score=16.72 buy_ready=False sector_rank=6 price=95.37 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=101111616.0 spike=1.27
- ETRS.CA: score=19.52 buy_ready=False sector_rank=12 price=10.36 support=7.65 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=26298596.0 spike=0.42
- EXPA.CA: score=18.65 buy_ready=False sector_rank=11 price=18.35 support=18.21 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=17168488.0 spike=0.51
- FAIT.CA: score=10.06 buy_ready=False sector_rank=11 price=36.5 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=1407943.88 spike=0.3
- FAITA.CA: score=9.28 buy_ready=False sector_rank=11 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=52788.48 spike=1.29
- FERC.CA: score=13.07 buy_ready=False sector_rank=20 price=76.08 support=75.0 resistance=79.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=12566096.0 spike=3.37
- FWRY.CA: score=8.82 buy_ready=False sector_rank=21 price=18.83 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.04 liquidity=144280240.0 spike=0.5
- GBCO.CA: score=5.1 buy_ready=False sector_rank=15 price=31.02 support=30.27 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68990600.0 spike=0.65
- GDWA.CA: score=14.76 buy_ready=False sector_rank=12 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=8241972.5 spike=0.59
- GGCC.CA: score=20.4 buy_ready=False sector_rank=12 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=8663769.0 spike=1.11
- GIHD.CA: score=10.52 buy_ready=False sector_rank=12 price=44.16 support=42.79 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57913700.0 spike=18.29
- GMCI.CA: score=7.16 buy_ready=False sector_rank=12 price=1.71 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=448050.66 spike=1.1
- GRCA.CA: score=7.48 buy_ready=False sector_rank=12 price=53.16 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.33 liquidity=6565069.0 spike=1.2
- GSSC.CA: score=4.34 buy_ready=False sector_rank=12 price=250.17 support=228.1 resistance=257.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.98 liquidity=3826641.5 spike=0.79
- GTWL.CA: score=13.26 buy_ready=False sector_rank=12 price=47.99 support=45.47 resistance=52.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.56 liquidity=3748816.5 spike=0.55
- HDBK.CA: score=24.65 buy_ready=False sector_rank=11 price=162.84 support=138.0 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.16 liquidity=90038952.0 spike=4.46
- HELI.CA: score=20.4 buy_ready=False sector_rank=3 price=6.42 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=85262976.0 spike=0.6
- HRHO.CA: score=17.04 buy_ready=False sector_rank=7 price=27.0 support=25.8 resistance=27.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=104091528.0 spike=0.71
- ICID.CA: score=12.94 buy_ready=False sector_rank=12 price=7.31 support=4.56 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=86.27 liquidity=3428559.5 spike=0.21
- IDRE.CA: score=20.88 buy_ready=False sector_rank=12 price=44.91 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.46 liquidity=21560324.0 spike=1.18
- IFAP.CA: score=3.13 buy_ready=False sector_rank=5 price=19.04 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=33.05 liquidity=2954782.5 spike=0.44
- INFI.CA: score=8.43 buy_ready=False sector_rank=12 price=93.74 support=93.0 resistance=105.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=12.22 liquidity=8910331.0 spike=0.98
- IRON.CA: score=15.33 buy_ready=False sector_rank=20 price=31.24 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.83 liquidity=9662026.0 spike=1.17
- ISMA.CA: score=15.52 buy_ready=False sector_rank=12 price=29.61 support=25.1 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=81.53 liquidity=13934054.0 spike=0.34
- ISMQ.CA: score=21.33 buy_ready=False sector_rank=20 price=8.15 support=7.31 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.1 liquidity=55034408.0 spike=0.74
- ISPH.CA: score=26.4 buy_ready=False sector_rank=1 price=12.29 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=35792628.0 spike=0.28
- JUFO.CA: score=22.7 buy_ready=False sector_rank=10 price=30.97 support=27.6 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=69.51 liquidity=15878034.0 spike=0.38
- KABO.CA: score=7.81 buy_ready=False sector_rank=16 price=6.09 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=3796433.0 spike=0.19
- KWIN.CA: score=7.38 buy_ready=False sector_rank=12 price=67.31 support=66.1 resistance=70.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11529124.0 spike=1.93
- KZPC.CA: score=16.32 buy_ready=False sector_rank=12 price=10.6 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=3806740.5 spike=0.49
- LCSW.CA: score=23.76 buy_ready=False sector_rank=19 price=27.7 support=26.0 resistance=28.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.08 liquidity=10949329.0 spike=1.09
- LUTS.CA: score=5.52 buy_ready=False sector_rank=12 price=0.73 support=0.73 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37969552.0 spike=0.95
- MAAL.CA: score=17.33 buy_ready=False sector_rank=12 price=6.67 support=4.68 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=80.1 liquidity=7818697.5 spike=0.55
- MASR.CA: score=24.72 buy_ready=False sector_rank=12 price=7.09 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.93 liquidity=61687748.0 spike=1.1
- MBSC.CA: score=14.58 buy_ready=False sector_rank=19 price=244.95 support=247.43 resistance=260.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.73 liquidity=24077012.0 spike=0.55
- MCQE.CA: score=9.58 buy_ready=False sector_rank=19 price=171.93 support=174.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.19 liquidity=11498062.0 spike=0.71
- MCRO.CA: score=9.52 buy_ready=False sector_rank=12 price=1.21 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=19552416.0 spike=0.43
- MENA.CA: score=7.98 buy_ready=False sector_rank=3 price=6.67 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.06 liquidity=2579642.0 spike=0.15
- MEPA.CA: score=14.71 buy_ready=False sector_rank=12 price=1.63 support=1.66 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=9197544.0 spike=0.53
- MFPC.CA: score=9.39 buy_ready=False sector_rank=20 price=35.73 support=36.76 resistance=44.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=6.41 liquidity=95948400.0 spike=1.03
- MFSC.CA: score=10.4 buy_ready=False sector_rank=12 price=50.63 support=46.99 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41543536.0 spike=3.44
- MHOT.CA: score=6.78 buy_ready=False sector_rank=14 price=35.34 support=35.06 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43991332.0 spike=1.84
- MICH.CA: score=23.86 buy_ready=False sector_rank=12 price=38.49 support=35.31 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.78 liquidity=26672900.0 spike=1.67
- MILS.CA: score=2.78 buy_ready=False sector_rank=12 price=130.29 support=130.11 resistance=138.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7267438.5 spike=0.42
- MIPH.CA: score=20.13 buy_ready=False sector_rank=1 price=660.66 support=648.25 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.54 liquidity=3011100.5 spike=1.36
- MOED.CA: score=12.73 buy_ready=False sector_rank=12 price=0.69 support=0.65 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=6212168.5 spike=0.49
- MOIL.CA: score=14.12 buy_ready=False sector_rank=9 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.83 liquidity=231457.81 spike=1.44
- MOIN.CA: score=-0.48 buy_ready=False sector_rank=12 price=24.09 support=24.01 resistance=25.66 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=14.86 liquidity=0.0 spike=0.0
- MOSC.CA: score=11.73 buy_ready=False sector_rank=12 price=269.85 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=3213961.25 spike=0.37
- MPCI.CA: score=26.28 buy_ready=False sector_rank=12 price=246.57 support=202.3 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=233770992.0 spike=2.88
- MPCO.CA: score=21.84 buy_ready=False sector_rank=5 price=1.91 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.6 liquidity=130739856.0 spike=1.33
- MPRC.CA: score=10.52 buy_ready=False sector_rank=12 price=36.3 support=33.9 resistance=36.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=161637056.0 spike=7.54
- MTIE.CA: score=17.57 buy_ready=False sector_rank=15 price=9.03 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=48.87 liquidity=9474058.0 spike=0.54
- NAHO.CA: score=-0.48 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=8379.2 spike=0.24
- NCCW.CA: score=24.46 buy_ready=False sector_rank=12 price=6.45 support=5.22 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.12 liquidity=83904112.0 spike=2.97
- NEDA.CA: score=9.86 buy_ready=False sector_rank=12 price=2.76 support=2.65 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=604060.13 spike=1.37
- NHPS.CA: score=13.3 buy_ready=False sector_rank=12 price=67.34 support=65.03 resistance=71.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=4660767.5 spike=1.06
- NINH.CA: score=20.52 buy_ready=False sector_rank=12 price=17.82 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.32 liquidity=22307566.0 spike=4.96
- NIPH.CA: score=24.6 buy_ready=False sector_rank=1 price=166.31 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=84915128.0 spike=1.1
- OBRI.CA: score=17.52 buy_ready=False sector_rank=12 price=34.17 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.1 liquidity=10586782.0 spike=0.79
- OCDI.CA: score=31.4 buy_ready=False sector_rank=3 price=22.94 support=20.0 resistance=22.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=153183088.0 spike=4.13
- OCPH.CA: score=18.52 buy_ready=False sector_rank=12 price=350.62 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.92 liquidity=25963288.0 spike=4.81
- ODIN.CA: score=18.33 buy_ready=False sector_rank=12 price=2.1 support=1.9 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=5816144.5 spike=0.52
- OFH.CA: score=15.52 buy_ready=False sector_rank=12 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.66 liquidity=17702072.0 spike=0.78
- OIH.CA: score=14.16 buy_ready=False sector_rank=13 price=1.41 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=242667872.0 spike=2.83
- OLFI.CA: score=20.7 buy_ready=False sector_rank=10 price=22.02 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=13044077.0 spike=0.65
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=788.65 support=780.0 resistance=812.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=349066208.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=False sector_rank=3 price=38.88 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.61 liquidity=143363568.0 spike=0.77
- ORWE.CA: score=18.01 buy_ready=False sector_rank=16 price=22.99 support=22.12 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=14011386.0 spike=0.34
- PHAR.CA: score=27.87 buy_ready=False sector_rank=1 price=87.37 support=83.02 resistance=89.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.2 liquidity=9470300.0 spike=0.26
- PHDC.CA: score=22.4 buy_ready=False sector_rank=3 price=15.45 support=14.32 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=280318752.0 spike=0.66
- PHTV.CA: score=20.06 buy_ready=False sector_rank=12 price=242.38 support=201.55 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=23557114.0 spike=1.27
- POUL.CA: score=9.68 buy_ready=False sector_rank=10 price=39.0 support=37.6 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100531536.0 spike=2.99
- PRCL.CA: score=7.76 buy_ready=False sector_rank=19 price=32.18 support=28.66 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=79411568.0 spike=2.59
- PRDC.CA: score=7.44 buy_ready=False sector_rank=3 price=6.98 support=6.67 resistance=7.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=102220864.0 spike=1.02
- PRMH.CA: score=22.52 buy_ready=False sector_rank=12 price=2.7 support=2.23 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.55 liquidity=14706891.0 spike=0.53
- RACC.CA: score=24.02 buy_ready=False sector_rank=12 price=9.93 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.96 liquidity=26941556.0 spike=2.75
- RAKT.CA: score=5.25 buy_ready=False sector_rank=12 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=39.79 liquidity=391641.56 spike=1.17
- RAYA.CA: score=19.4 buy_ready=False sector_rank=4 price=7.1 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.55 liquidity=76594840.0 spike=0.84
- RMDA.CA: score=22.25 buy_ready=False sector_rank=1 price=5.03 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=9854191.0 spike=0.12
- ROTO.CA: score=22.62 buy_ready=False sector_rank=12 price=42.61 support=32.66 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=84.24 liquidity=63325064.0 spike=2.55
- RREI.CA: score=14.31 buy_ready=False sector_rank=12 price=3.54 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=6790005.5 spike=0.33
- RTVC.CA: score=11.32 buy_ready=False sector_rank=12 price=3.8 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=3799065.0 spike=0.75
- RUBX.CA: score=15.9 buy_ready=False sector_rank=12 price=10.31 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=8382268.5 spike=0.76
- SAUD.CA: score=6.35 buy_ready=False sector_rank=11 price=21.58 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.06 liquidity=5695472.0 spike=0.55
- SCEM.CA: score=4.59 buy_ready=False sector_rank=19 price=61.25 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=5013717.5 spike=0.25
- SCFM.CA: score=3.57 buy_ready=False sector_rank=12 price=240.28 support=248.1 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.66 liquidity=3055614.25 spike=0.28
- SCTS.CA: score=3.74 buy_ready=False sector_rank=8 price=590.19 support=565.25 resistance=648.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=28.59 liquidity=2737235.5 spike=0.55
- SDTI.CA: score=17.22 buy_ready=False sector_rank=12 price=46.55 support=43.6 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.18 liquidity=4705363.5 spike=0.33
- SEIG.CA: score=14.16 buy_ready=False sector_rank=12 price=185.35 support=177.32 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=3643927.25 spike=0.81
- SIPC.CA: score=9.76 buy_ready=False sector_rank=12 price=3.46 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=4248937.5 spike=0.34
- SKPC.CA: score=13.33 buy_ready=False sector_rank=20 price=16.02 support=16.13 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=16706172.0 spike=0.33
- SMFR.CA: score=6.18 buy_ready=False sector_rank=12 price=199.48 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=41.88 liquidity=664128.56 spike=0.19
- SNFC.CA: score=14.19 buy_ready=False sector_rank=12 price=12.05 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=5672796.5 spike=0.22
- SPIN.CA: score=2.6 buy_ready=False sector_rank=16 price=13.8 support=13.3 resistance=14.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=23.33 liquidity=2585601.25 spike=0.57
- SPMD.CA: score=6.06 buy_ready=False sector_rank=12 price=0.42 support=0.42 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33729892.0 spike=1.27
- SUGR.CA: score=5.37 buy_ready=False sector_rank=10 price=47.63 support=48.0 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.76 liquidity=5669858.5 spike=0.38
- SVCE.CA: score=18.52 buy_ready=False sector_rank=12 price=9.04 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.4 liquidity=48048720.0 spike=0.54
- SWDY.CA: score=26.02 buy_ready=False sector_rank=2 price=88.22 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.66 liquidity=41393164.0 spike=2.31
- TALM.CA: score=16.11 buy_ready=False sector_rank=8 price=15.73 support=15.32 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=5107192.0 spike=0.66
- TMGH.CA: score=20.4 buy_ready=False sector_rank=3 price=95.0 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=344930144.0 spike=0.7
- TRTO.CA: score=6.52 buy_ready=False sector_rank=12 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=10.14 buy_ready=False sector_rank=12 price=484.15 support=455.6 resistance=489.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=30.31 liquidity=2120895.75 spike=2.75
- UEGC.CA: score=18.52 buy_ready=False sector_rank=12 price=1.4 support=1.31 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=10775863.0 spike=0.44
- UNIP.CA: score=5.52 buy_ready=False sector_rank=12 price=0.32 support=0.29 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23911612.0 spike=1.0
- UNIT.CA: score=6.04 buy_ready=False sector_rank=3 price=13.26 support=12.5 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=30.53 liquidity=637701.19 spike=0.09
- WCDF.CA: score=5.68 buy_ready=False sector_rank=12 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-20T21:00:00+00:00 freshness=FRESH RSI=42.27 liquidity=167032.3 spike=0.63
- WKOL.CA: score=7.23 buy_ready=False sector_rank=12 price=288.18 support=287.66 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.88 liquidity=1712933.25 spike=0.55
- ZEOT.CA: score=21.0 buy_ready=False sector_rank=12 price=11.34 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=84.02 liquidity=36439084.0 spike=1.74
- ZMID.CA: score=23.12 buy_ready=False sector_rank=3 price=6.41 support=5.81 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.87 liquidity=280796480.0 spike=1.36

## Backtesting Lite
- OCDI.CA: 180d return=42.4%, max drawdown=-18.11%, MA20>MA50 days last20=12, as_of=2026-06-21T21:00:00+00:00
- DOMT.CA: 180d return=22.78%, max drawdown=-13.36%, MA20>MA50 days last20=16, as_of=2026-06-21T21:00:00+00:00
- CLHO.CA: 180d return=42.86%, max drawdown=-14.16%, MA20>MA50 days last20=20, as_of=2026-06-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- DOMT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Arabian Food Industries Domty summary=Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn; Selling pressure pushes Domty’s stock toward EGP 23.50–22.85; Domty unveils demerger, establishes Dairy Products Euro Arabian
  - Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn: https://english.mubasher.info/news/4593671/Domty-posts-lower-consolidated-net-profits-at-EGP-161m-in-2025-net-sales-exceed-EGP-9-3bn/
  - Selling pressure pushes Domty’s stock toward EGP 23.50–22.85: https://english.mubasher.info/news/4562323/Selling-pressure-pushes-Domty-s-stock-toward-EGP-23-50-22-85/
  - Domty unveils demerger, establishes Dairy Products Euro Arabian: https://english.mubasher.info/news/4543153/Domty-unveils-demerger-establishes-Dairy-Products-Euro-Arabian/
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- ISPH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Ibn Sina Pharma summary=Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025; EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse; Ibnsina Pharma pens import, distribution deal with OMRON Healthcare
  - Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025: https://english.mubasher.info/news/4563237/Ibnsina-Pharma-s-consolidated-profits-jump-to-EGP-952m-in-2025/
  - EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse: https://english.mubasher.info/news/4552027/EBRD-grants-EGP-1-3bn-loan-to-Ibnsina-Pharma-for-new-warehouse/
  - Ibnsina Pharma pens import, distribution deal with OMRON Healthcare: https://english.mubasher.info/news/4028068/Ibnsina-Pharma-pens-import-distribution-deal-with-OMRON-Healthcare/
- MPCI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Memphis Pharmaceuticals & Chemical Industries summary=Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations; Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
  - Elsewedy Electric’s subsidiary leads expansion of SAL project at Riyadh airport: https://english.mubasher.info/news/4580464/Elsewedy-Electric-s-subsidiary-leads-expansion-of-SAL-project-at-Riyadh-airport/

## Warnings
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for DOMT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Evidence for ISPH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
