# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-01T09:04:20.795509+00:00
Generated Cairo: 2026-07-01 12:04
Run timing: target 08:45 Cairo | generated Cairo 2026-07-01 12:04 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-01 12:00

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 183/190
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 01
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 25.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 52.5% / above MA50 67.5%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=145074352.0 spike=0.25 score=14.96
- GTWL.CA: liquidity=135166848.0 spike=4.15 score=10.13
- RUBX.CA: liquidity=133252896.0 spike=7.05 score=10.13
- BTFH.CA: liquidity=108683320.0 spike=0.59 score=14.31
- DTPP.CA: liquidity=102450336.0 spike=28.26 score=10.13

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: We need to produce a concise Telegram narrative for a personal EGX stock scanner. Must not make a new trade decision, not invent live data, not mention quantities or position sizing. Explain why local scanner selected these prioritized tickets, what liquidity/sector/support/resistance/outlook means for next 1-3 days, and how EGX30/EGX70 market regime changes risk mode, and include uncertainty. Return only valid compact JSON with keys summary and bullets, where bullets is 3 to 5 short strings.

We must not include any extra text, only JSON.

We need to craft summary string and bullets (3-5 short strings). Use info from payload: market regime bearish, defensive no new buy, sector breadth low, 
- Scanner flags several high‑rank stocks with bullish watch outlooks, but the EGX30/EGX70 bearish regime and defensive risk mode keep new buys on hold.
- SCTS.CA shows strong accumulation spike and bullish watch, yet sits 16% below 20‑day support and only 3% below resistance, limiting near‑term upside.
- RAYA.CA enjoys high liquidity and bullish momentum, but liquidity is cooling and price is within 1% of 20‑day resistance, suggesting a possible pause.
- AMES.CA and ELKA.CA display large liquidity spikes and constructive outlooks, but RSI is elevated (78‑89) and they sit far above support, raising overheating concerns.
- Make sure no quantities or position sizing mentioned. We didn't mention quantities. We mentioned percentages (distance) but that's okay? The instruction:

## Top Liquidity Spikes
- DTPP.CA: spike=28.26 liquidity=102450336.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=7.05 liquidity=133252896.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOIN.CA: spike=6.69 liquidity=5141199.3 outlook=WEAK_OR_RISKY score=23.83 buy_ready=False
- GTWL.CA: spike=4.15 liquidity=135166848.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EPPK.CA: spike=4.03 liquidity=3858781.29 outlook=CONSTRUCTIVE score=58.83 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=10.69 5d=8.17% 20d=2.67% aboveMA50=100.0%
- #2 Automotive & Distribution: score=9.3 5d=1.53% 20d=10.05% aboveMA50=100.0%
- #3 Tourism & Leisure: score=5.23 5d=-4.44% 20d=2.64% aboveMA50=100.0%
- #4 Education: score=4.87 5d=-1.75% 20d=0.67% aboveMA50=100.0%
- #5 Transportation & Logistics: score=4.63 5d=2.98% 20d=-0.3% aboveMA50=50.0%
- #6 Healthcare: score=3.35 5d=-0.93% 20d=-0.06% aboveMA50=66.67%
- #7 Non-bank Financial Services: score=3.28 5d=-0.09% 20d=-1.73% aboveMA50=40.0%
- #8 Real Estate: score=3.2 5d=0.09% 20d=-2.39% aboveMA50=76.92%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=95.3 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SCTS.CA: BULLISH_WATCH score=93.87 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ELKA.CA: BULLISH_WATCH score=81.83 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CNFN.CA: BULLISH_WATCH score=79.28 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- IDRE.CA: BULLISH_WATCH score=78.83 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- GMCI.CA: BULLISH_WATCH score=78.83 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- NIPH.CA: BULLISH_WATCH score=78.35 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MHOT.CA: BULLISH_WATCH score=77.23 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- CSAG.CA: BULLISH_WATCH score=74.63 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- MENA.CA: BULLISH_WATCH score=74.2 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=13.12 buy_ready=False sector_rank=9 price=207.47 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=2992822.75 spike=0.48
- ABUK.CA: score=8.57 buy_ready=False sector_rank=20 price=68.21 support=66.66 resistance=83.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=49936740.0 spike=0.37
- ACAMD.CA: score=18.13 buy_ready=False sector_rank=9 price=2.23 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=15372346.0 spike=0.12
- ACGC.CA: score=11.54 buy_ready=False sector_rank=11 price=9.25 support=8.92 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=39.66 liquidity=3480165.0 spike=0.1
- ADCI.CA: score=9.35 buy_ready=False sector_rank=9 price=242.65 support=211.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=76.1 liquidity=2216103.0 spike=0.21
- ADIB.CA: score=19.96 buy_ready=False sector_rank=12 price=47.1 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=29121022.0 spike=0.32
- ADPC.CA: score=5.81 buy_ready=False sector_rank=9 price=3.45 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=1678497.0 spike=0.09
- AFDI.CA: score=11.11 buy_ready=False sector_rank=9 price=44.35 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=976090.0 spike=0.06
- AFMC.CA: score=5.7 buy_ready=False sector_rank=9 price=70.38 support=66.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=566698.25 spike=0.25
- AJWA.CA: score=11.65 buy_ready=False sector_rank=9 price=180.0 support=132.15 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=78.37 liquidity=6520736.5 spike=0.23
- ALCN.CA: score=8.63 buy_ready=False sector_rank=5 price=28.26 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=55.9 liquidity=2776660.5 spike=0.23
- ALUM.CA: score=1.0 buy_ready=False sector_rank=9 price=21.3 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=869845.69 spike=0.09
- AMER.CA: score=10.28 buy_ready=False sector_rank=8 price=2.42 support=2.28 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=19509910.0 spike=0.27
- AMES.CA: score=24.13 buy_ready=False sector_rank=9 price=63.21 support=45.15 resistance=66.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=78.33 liquidity=43246684.0 spike=3.54
- AMIA.CA: score=9.12 buy_ready=False sector_rank=9 price=8.66 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=990848.88 spike=0.08
- AMOC.CA: score=9.37 buy_ready=False sector_rank=16 price=7.75 support=7.42 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=34.4 liquidity=13579108.0 spike=0.28
- ANFI.CA: score=6.46 buy_ready=False sector_rank=9 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=5.67 buy_ready=False sector_rank=9 price=8.34 support=8.0 resistance=9.21 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=36.94 liquidity=1015003.04 spike=1.26
- ARAB.CA: score=15.28 buy_ready=False sector_rank=8 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=20994894.0 spike=0.26
- ARCC.CA: score=11.66 buy_ready=False sector_rank=13 price=55.48 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=6828776.0 spike=0.21
- AREH.CA: score=17.23 buy_ready=False sector_rank=9 price=1.56 support=1.34 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=7097828.0 spike=0.2
- ARVA.CA: score=8.85 buy_ready=False sector_rank=9 price=10.81 support=9.82 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=46.76 liquidity=721323.13 spike=0.02
- ASCM.CA: score=20.13 buy_ready=False sector_rank=9 price=59.68 support=49.72 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=59.92 liquidity=12233310.0 spike=0.13
- ASPI.CA: score=16.22 buy_ready=False sector_rank=9 price=0.32 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=45.69 liquidity=8088682.5 spike=0.11
- ATLC.CA: score=12.94 buy_ready=False sector_rank=7 price=5.24 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=62.9 liquidity=2626959.0 spike=0.4
- ATQA.CA: score=10.69 buy_ready=False sector_rank=20 price=9.53 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=8118521.0 spike=0.24
- AXPH.CA: score=11.26 buy_ready=False sector_rank=9 price=1115.33 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=1123433.0 spike=0.78
- BINV.CA: score=12.34 buy_ready=False sector_rank=17 price=46.5 support=44.02 resistance=48.89 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=52.7 liquidity=5046459.0 spike=0.99
- BIOC.CA: score=5.99 buy_ready=False sector_rank=9 price=71.09 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=46.18 liquidity=855553.06 spike=0.34
- BTFH.CA: score=14.31 buy_ready=False sector_rank=7 price=2.93 support=2.95 resistance=3.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=41.07 liquidity=108683320.0 spike=0.59
- CAED.CA: score=11.4 buy_ready=False sector_rank=9 price=72.24 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=1263510.5 spike=0.27
- CANA.CA: score=7.7 buy_ready=False sector_rank=12 price=35.83 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=46.39 liquidity=736547.69 spike=0.06
- CCAP.CA: score=9.29 buy_ready=False sector_rank=17 price=4.78 support=4.65 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=28.89 liquidity=97914040.0 spike=0.15
- CCRS.CA: score=12.28 buy_ready=False sector_rank=9 price=2.31 support=2.18 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=4147849.0 spike=0.28
- CEFM.CA: score=7.1 buy_ready=False sector_rank=9 price=100.16 support=95.75 resistance=109.49 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=35.08 liquidity=1564098.62 spike=1.2
- CERA.CA: score=9.24 buy_ready=False sector_rank=9 price=1.22 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=2112772.25 spike=0.12
- CFGH.CA: score=-0.87 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=707.6 spike=0.12
- CICH.CA: score=10.78 buy_ready=False sector_rank=7 price=11.94 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=57.96 liquidity=1464099.38 spike=0.5
- CIEB.CA: score=9.16 buy_ready=False sector_rank=12 price=23.85 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=2197660.0 spike=0.33
- CIRA.CA: score=13.81 buy_ready=False sector_rank=4 price=28.86 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=70.05 liquidity=4861664.0 spike=0.29
- CLHO.CA: score=20.34 buy_ready=False sector_rank=6 price=16.44 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=72.12 liquidity=17612102.0 spike=0.46
- CNFN.CA: score=22.31 buy_ready=False sector_rank=7 price=4.84 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=18481766.0 spike=0.44
- COMI.CA: score=14.96 buy_ready=False sector_rank=12 price=127.5 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=145074352.0 spike=0.25
- COPR.CA: score=10.08 buy_ready=False sector_rank=9 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=2949067.75 spike=0.11
- COSG.CA: score=8.75 buy_ready=False sector_rank=9 price=1.53 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=8616083.0 spike=0.16
- CPCI.CA: score=11.58 buy_ready=False sector_rank=9 price=400.74 support=350.04 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=77.94 liquidity=2452025.0 spike=0.95
- CSAG.CA: score=20.35 buy_ready=False sector_rank=5 price=32.31 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=69.76 liquidity=7498068.5 spike=0.43
- DAPH.CA: score=13.94 buy_ready=False sector_rank=9 price=81.95 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=1804973.63 spike=0.18
- DEIN.CA: score=6.13 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=10.0 buy_ready=False sector_rank=10 price=27.32 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=80.08 liquidity=2917491.75 spike=0.73
- DSCW.CA: score=11.8 buy_ready=False sector_rank=9 price=1.74 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=7665265.0 spike=0.22
- DTPP.CA: score=10.13 buy_ready=False sector_rank=9 price=185.62 support=183.99 resistance=199.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=102450336.0 spike=28.26
- EALR.CA: score=0.87 buy_ready=False sector_rank=9 price=342.95 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=739986.0 spike=0.24
- EASB.CA: score=20.21 buy_ready=False sector_rank=9 price=7.52 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=72.71 liquidity=13906634.0 spike=1.04
- EAST.CA: score=14.08 buy_ready=False sector_rank=10 price=37.32 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=42.07 liquidity=10694726.0 spike=0.28
- EBSC.CA: score=5.64 buy_ready=False sector_rank=9 price=1.75 support=1.71 resistance=2.09 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=39.39 liquidity=505783.25 spike=0.23
- ECAP.CA: score=13.35 buy_ready=False sector_rank=9 price=32.9 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=59.15 liquidity=3213625.75 spike=0.35
- EDFM.CA: score=0.38 buy_ready=False sector_rank=9 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=17.77 liquidity=246620.14 spike=0.52
- EEII.CA: score=21.01 buy_ready=False sector_rank=9 price=2.51 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=19631230.0 spike=1.44
- EFIC.CA: score=4.06 buy_ready=False sector_rank=20 price=188.44 support=180.02 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=4.61 liquidity=4312314.0 spike=2.09
- EFID.CA: score=8.77 buy_ready=False sector_rank=10 price=27.36 support=25.5 resistance=29.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=45.86 liquidity=3686677.0 spike=0.05
- EFIH.CA: score=8.7 buy_ready=False sector_rank=21 price=20.33 support=20.0 resistance=22.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=42.98 liquidity=5836967.5 spike=0.14
- EGAL.CA: score=8.57 buy_ready=False sector_rank=20 price=285.44 support=272.28 resistance=332.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=29.65 liquidity=14909228.0 spike=0.25
- EGAS.CA: score=9.14 buy_ready=False sector_rank=16 price=49.8 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=1772203.75 spike=0.21
- EGBE.CA: score=11.52 buy_ready=False sector_rank=12 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=55.36 liquidity=113399.07 spike=1.72
- EGCH.CA: score=8.57 buy_ready=False sector_rank=20 price=12.38 support=12.13 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=24.58 liquidity=10531300.0 spike=0.2
- EGSA.CA: score=2.0 buy_ready=False sector_rank=19 price=8.75 support=8.55 resistance=9.09 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=85.71 liquidity=446.25 spike=0.05
- EGTS.CA: score=14.09 buy_ready=False sector_rank=8 price=17.6 support=15.1 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=5810513.0 spike=0.07
- EHDR.CA: score=14.77 buy_ready=False sector_rank=9 price=2.51 support=2.37 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=6636321.5 spike=0.11
- EKHO.CA: score=6.37 buy_ready=False sector_rank=16 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=6.58 buy_ready=False sector_rank=18 price=2.09 support=2.04 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=3445285.5 spike=0.19
- ELKA.CA: score=22.45 buy_ready=False sector_rank=9 price=1.37 support=1.19 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=73247384.0 spike=1.66
- ELNA.CA: score=-0.2 buy_ready=False sector_rank=9 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=33.8 liquidity=486123.19 spike=1.09
- ELSH.CA: score=9.07 buy_ready=False sector_rank=9 price=11.75 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=25.76 liquidity=5939810.0 spike=0.03
- ELWA.CA: score=4.26 buy_ready=False sector_rank=9 price=1.97 support=1.95 resistance=2.22 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=32.61 liquidity=1126922.76 spike=0.58
- EMFD.CA: score=18.28 buy_ready=False sector_rank=8 price=11.5 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=51.12 liquidity=23191912.0 spike=0.08
- ENGC.CA: score=16.14 buy_ready=False sector_rank=9 price=36.61 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=63.74 liquidity=4008635.5 spike=0.27
- EOSB.CA: score=12.16 buy_ready=False sector_rank=9 price=1.48 support=1.39 resistance=1.55 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=28383.44 spike=0.22
- EPCO.CA: score=6.37 buy_ready=False sector_rank=9 price=8.8 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=40.13 liquidity=1239527.25 spike=0.16
- EPPK.CA: score=17.99 buy_ready=False sector_rank=9 price=13.67 support=11.67 resistance=13.68 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=80.49 liquidity=3858781.29 spike=4.03
- ETEL.CA: score=7.93 buy_ready=False sector_rank=19 price=92.47 support=89.01 resistance=97.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=3930377.0 spike=0.06
- ETRS.CA: score=22.13 buy_ready=False sector_rank=9 price=10.53 support=8.6 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=62.41 liquidity=38165568.0 spike=0.47
- EXPA.CA: score=3.32 buy_ready=False sector_rank=12 price=18.29 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=34.56 liquidity=3352697.0 spike=0.11
- FAIT.CA: score=9.64 buy_ready=False sector_rank=12 price=36.54 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=57.02 liquidity=1671514.75 spike=0.57
- FAITA.CA: score=4.98 buy_ready=False sector_rank=12 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=40.63 liquidity=14194.2 spike=0.43
- FERC.CA: score=-0.84 buy_ready=False sector_rank=20 price=73.62 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=23.2 liquidity=1591718.0 spike=0.4
- FWRY.CA: score=12.87 buy_ready=False sector_rank=21 price=18.4 support=17.71 resistance=20.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=11715307.0 spike=0.05
- GBCO.CA: score=22.4 buy_ready=False sector_rank=2 price=32.02 support=25.25 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=89.02 liquidity=12093796.0 spike=0.13
- GDWA.CA: score=5.44 buy_ready=False sector_rank=9 price=0.77 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=39.5 liquidity=1305521.5 spike=0.09
- GGCC.CA: score=18.13 buy_ready=False sector_rank=9 price=0.48 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=87.0 liquidity=10874405.0 spike=0.86
- GIHD.CA: score=11.92 buy_ready=False sector_rank=9 price=42.51 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=60.39 liquidity=1792751.5 spike=0.21
- GMCI.CA: score=16.78 buy_ready=False sector_rank=9 price=1.86 support=1.66 resistance=1.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=1305059.12 spike=2.67
- GRCA.CA: score=5.43 buy_ready=False sector_rank=9 price=52.3 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=302877.75 spike=0.07
- GSSC.CA: score=5.79 buy_ready=False sector_rank=9 price=245.83 support=228.1 resistance=256.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=657258.31 spike=0.23
- GTWL.CA: score=10.13 buy_ready=False sector_rank=9 price=93.18 support=91.5 resistance=102.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=135166848.0 spike=4.15
- HDBK.CA: score=19.47 buy_ready=False sector_rank=12 price=160.91 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=9505381.0 spike=0.32
- HELI.CA: score=18.28 buy_ready=False sector_rank=8 price=6.45 support=6.28 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=17968810.0 spike=0.16
- HRHO.CA: score=14.31 buy_ready=False sector_rank=7 price=26.7 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=62.31 liquidity=23692854.0 spike=0.18
- ICID.CA: score=11.73 buy_ready=False sector_rank=9 price=8.05 support=5.5 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=78.53 liquidity=2596550.5 spike=0.15
- IDRE.CA: score=20.13 buy_ready=False sector_rank=9 price=44.24 support=41.1 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=11456555.0 spike=0.87
- IFAP.CA: score=6.1 buy_ready=False sector_rank=14 price=19.21 support=18.47 resistance=20.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=317262.0 spike=0.05
- INFI.CA: score=3.68 buy_ready=False sector_rank=9 price=93.59 support=88.51 resistance=104.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=23.06 liquidity=4552628.0 spike=0.76
- IRON.CA: score=8.18 buy_ready=False sector_rank=20 price=32.7 support=30.51 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=1610300.63 spike=0.21
- ISMA.CA: score=7.3 buy_ready=False sector_rank=9 price=28.57 support=26.22 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=32.38 liquidity=4166872.5 spike=0.12
- ISMQ.CA: score=18.57 buy_ready=False sector_rank=20 price=9.4 support=7.56 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=72.4 liquidity=87106016.0 spike=0.73
- ISPH.CA: score=12.69 buy_ready=False sector_rank=6 price=11.56 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=7354917.5 spike=0.07
- JUFO.CA: score=10.3 buy_ready=False sector_rank=10 price=29.65 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=51.92 liquidity=2214888.5 spike=0.07
- KABO.CA: score=14.77 buy_ready=False sector_rank=11 price=6.31 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=63.08 liquidity=4706856.5 spike=0.29
- KWIN.CA: score=6.54 buy_ready=False sector_rank=9 price=67.48 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=40.07 liquidity=2412874.25 spike=0.21
- KZPC.CA: score=0.63 buy_ready=False sector_rank=9 price=8.44 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=8.85 liquidity=1498286.88 spike=0.24
- LCSW.CA: score=21.84 buy_ready=False sector_rank=13 price=27.82 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=55.63 liquidity=14861579.0 spike=0.49
- LUTS.CA: score=18.13 buy_ready=False sector_rank=9 price=0.75 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=11208902.0 spike=0.23
- MAAL.CA: score=12.48 buy_ready=False sector_rank=9 price=7.2 support=5.44 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=85.87 liquidity=3346917.5 spike=0.19
- MASR.CA: score=20.13 buy_ready=False sector_rank=9 price=7.3 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=26036276.0 spike=0.41
- MBSC.CA: score=3.79 buy_ready=False sector_rank=13 price=239.42 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=3952580.5 spike=0.12
- MCQE.CA: score=4.21 buy_ready=False sector_rank=13 price=172.13 support=166.66 resistance=199.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=34.8 liquidity=4372921.0 spike=0.32
- MCRO.CA: score=13.78 buy_ready=False sector_rank=9 price=1.21 support=1.17 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=9644625.0 spike=0.28
- MENA.CA: score=12.89 buy_ready=False sector_rank=8 price=6.83 support=6.41 resistance=7.75 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=51.11 liquidity=2612543.27 spike=0.3
- MEPA.CA: score=1.75 buy_ready=False sector_rank=9 price=1.58 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=26.92 liquidity=2620543.5 spike=0.24
- MFPC.CA: score=8.57 buy_ready=False sector_rank=20 price=35.7 support=34.22 resistance=43.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=15.93 liquidity=29302386.0 spike=0.35
- MFSC.CA: score=6.75 buy_ready=False sector_rank=9 price=50.31 support=47.0 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14395476.0 spike=1.81
- MHOT.CA: score=17.89 buy_ready=False sector_rank=3 price=34.43 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=68.18 liquidity=5801627.0 spike=0.32
- MICH.CA: score=13.47 buy_ready=False sector_rank=9 price=37.97 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=51.63 liquidity=3340806.0 spike=0.22
- MILS.CA: score=7.46 buy_ready=False sector_rank=9 price=130.34 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=2330841.5 spike=0.25
- MIPH.CA: score=5.72 buy_ready=False sector_rank=6 price=656.35 support=630.13 resistance=710.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=49.25 liquidity=375432.19 spike=0.24
- MOED.CA: score=8.71 buy_ready=False sector_rank=9 price=0.69 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=48.63 liquidity=2576861.5 spike=0.28
- MOIL.CA: score=7.43 buy_ready=False sector_rank=16 price=0.47 support=0.46 resistance=0.49 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.94 liquidity=61272.02 spike=0.45
- MOIN.CA: score=14.27 buy_ready=False sector_rank=9 price=24.32 support=22.6 resistance=25.66 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=39.45 liquidity=5141199.3 spike=6.69
- MOSC.CA: score=10.81 buy_ready=False sector_rank=9 price=273.45 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=681128.38 spike=0.07
- MPCI.CA: score=20.13 buy_ready=False sector_rank=9 price=243.52 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=59.99 liquidity=20754672.0 spike=0.21
- MPCO.CA: score=17.78 buy_ready=False sector_rank=14 price=1.84 support=1.6 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=21519976.0 spike=0.2
- MPRC.CA: score=18.12 buy_ready=False sector_rank=9 price=38.0 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=85.5 liquidity=8989061.0 spike=0.21
- MTIE.CA: score=23.4 buy_ready=False sector_rank=2 price=9.09 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=12824710.0 spike=0.77
- NAHO.CA: score=9.52 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 June 01:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=84917.81 spike=2.65
- NCCW.CA: score=13.07 buy_ready=False sector_rank=9 price=6.19 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=4940976.0 spike=0.15
- NEDA.CA: score=5.36 buy_ready=False sector_rank=9 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=223674.42 spike=0.62
- NHPS.CA: score=20.16 buy_ready=False sector_rank=9 price=68.0 support=61.55 resistance=71.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=62.04 liquidity=5548366.5 spike=1.24
- NINH.CA: score=13.05 buy_ready=False sector_rank=9 price=18.01 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=71.37 liquidity=5780285.5 spike=1.07
- NIPH.CA: score=20.68 buy_ready=False sector_rank=6 price=171.25 support=157.01 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=52.9 liquidity=79693944.0 spike=1.17
- OBRI.CA: score=8.87 buy_ready=False sector_rank=9 price=36.15 support=33.12 resistance=36.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42692264.0 spike=2.87
- OCDI.CA: score=17.28 buy_ready=False sector_rank=8 price=24.69 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=76.98 liquidity=10997424.0 spike=0.14
- OCPH.CA: score=11.69 buy_ready=False sector_rank=9 price=355.07 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=51.93 liquidity=1558965.13 spike=0.24
- ODIN.CA: score=14.28 buy_ready=False sector_rank=9 price=2.15 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=53.66 liquidity=4143736.75 spike=0.37
- OFH.CA: score=8.55 buy_ready=False sector_rank=9 price=0.6 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=38.57 liquidity=4413047.0 spike=0.23
- OIH.CA: score=18.29 buy_ready=False sector_rank=17 price=1.41 support=1.33 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=19399310.0 spike=0.25
- OLFI.CA: score=18.95 buy_ready=False sector_rank=10 price=22.3 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=58.59 liquidity=8870339.0 spike=0.42
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=726.37 support=725.0 resistance=733.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88247120.0 spike=1.0
- ORHD.CA: score=20.28 buy_ready=False sector_rank=8 price=37.96 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=59.76 liquidity=14170939.0 spike=0.08
- ORWE.CA: score=3.75 buy_ready=False sector_rank=11 price=22.41 support=21.95 resistance=24.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=3690374.75 spike=0.11
- PHAR.CA: score=12.41 buy_ready=False sector_rank=6 price=87.95 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=55.96 liquidity=2066443.75 spike=0.06
- PHDC.CA: score=18.28 buy_ready=False sector_rank=8 price=14.66 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=46201624.0 spike=0.12
- PHTV.CA: score=10.02 buy_ready=False sector_rank=9 price=271.89 support=201.55 resistance=277.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=95.04 liquidity=890739.75 spike=0.06
- POUL.CA: score=22.08 buy_ready=False sector_rank=10 price=38.19 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=20717606.0 spike=0.59
- PRCL.CA: score=13.33 buy_ready=False sector_rank=13 price=31.03 support=22.86 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=74.2 liquidity=3494998.75 spike=0.08
- PRDC.CA: score=17.43 buy_ready=False sector_rank=8 price=7.45 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=9148986.0 spike=0.08
- PRMH.CA: score=12.15 buy_ready=False sector_rank=9 price=2.51 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=4018265.75 spike=0.13
- RACC.CA: score=6.76 buy_ready=False sector_rank=9 price=9.77 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=58.0 liquidity=1632580.88 spike=0.19
- RAKT.CA: score=1.01 buy_ready=False sector_rank=9 price=21.67 support=21.4 resistance=24.1 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=29.78 liquidity=456456.88 spike=1.71
- RAYA.CA: score=24.4 buy_ready=False sector_rank=1 price=7.73 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=50870080.0 spike=0.59
- RMDA.CA: score=10.37 buy_ready=False sector_rank=6 price=4.97 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=42.17 liquidity=2028994.0 spike=0.03
- ROTO.CA: score=19.95 buy_ready=False sector_rank=9 price=41.8 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=73.17 liquidity=9820925.0 spike=0.33
- RREI.CA: score=6.71 buy_ready=False sector_rank=9 price=3.49 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=1576990.75 spike=0.09
- RTVC.CA: score=6.13 buy_ready=False sector_rank=9 price=3.81 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=42.25 liquidity=999583.31 spike=0.19
- RUBX.CA: score=10.13 buy_ready=False sector_rank=9 price=13.05 support=11.22 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=133252896.0 spike=7.05
- SAUD.CA: score=6.4 buy_ready=False sector_rank=12 price=21.14 support=19.99 resistance=22.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=45.19 liquidity=1440766.75 spike=0.17
- SCEM.CA: score=13.09 buy_ready=False sector_rank=13 price=63.32 support=59.3 resistance=66.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=55.52 liquidity=3255787.25 spike=0.19
- SCFM.CA: score=1.79 buy_ready=False sector_rank=9 price=241.99 support=226.5 resistance=269.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=1657384.38 spike=0.37
- SCTS.CA: score=25.23 buy_ready=False sector_rank=4 price=628.38 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=58.45 liquidity=9457029.0 spike=2.41
- SDTI.CA: score=10.3 buy_ready=False sector_rank=9 price=46.5 support=44.35 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=2168080.5 spike=0.19
- SEIG.CA: score=11.36 buy_ready=False sector_rank=9 price=189.04 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=62.3 liquidity=1226491.63 spike=0.3
- SIPC.CA: score=0.87 buy_ready=False sector_rank=9 price=3.36 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=739312.13 spike=0.06
- SKPC.CA: score=6.94 buy_ready=False sector_rank=20 price=15.98 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=9369664.0 spike=0.28
- SMFR.CA: score=5.61 buy_ready=False sector_rank=9 price=193.51 support=187.01 resistance=214.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=38.45 liquidity=475647.57 spike=0.28
- SNFC.CA: score=11.5 buy_ready=False sector_rank=9 price=12.11 support=11.68 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=53.47 liquidity=3363769.5 spike=0.21
- SPIN.CA: score=8.42 buy_ready=False sector_rank=11 price=14.2 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=1355366.5 spike=0.23
- SPMD.CA: score=14.95 buy_ready=False sector_rank=9 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=4817230.0 spike=0.2
- SUGR.CA: score=0.06 buy_ready=False sector_rank=10 price=46.66 support=45.31 resistance=51.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=19.88 liquidity=980483.25 spike=0.13
- SVCE.CA: score=20.13 buy_ready=False sector_rank=9 price=9.18 support=8.11 resistance=9.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=58.91 liquidity=11228230.0 spike=0.18
- SWDY.CA: score=10.19 buy_ready=False sector_rank=18 price=86.53 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=49.08 liquidity=3060800.0 spike=0.18
- TALM.CA: score=9.46 buy_ready=False sector_rank=4 price=15.82 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=37.76 liquidity=515102.0 spike=0.07
- TMGH.CA: score=15.28 buy_ready=False sector_rank=8 price=94.48 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=29966154.0 spike=0.08
- TRTO.CA: score=6.13 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=6.33 buy_ready=False sector_rank=9 price=470.0 support=460.0 resistance=505.0 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=47.04 liquidity=195050.0 spike=0.22
- UEGC.CA: score=12.07 buy_ready=False sector_rank=9 price=1.42 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=1940143.62 spike=0.08
- UNIP.CA: score=11.31 buy_ready=False sector_rank=9 price=0.33 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=54.44 liquidity=1173837.88 spike=0.05
- UNIT.CA: score=3.87 buy_ready=False sector_rank=8 price=13.06 support=12.0 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=30.74 liquidity=593998.94 spike=0.09
- WCDF.CA: score=5.36 buy_ready=False sector_rank=9 price=518.05 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-29T21:00:00+00:00 freshness=FRESH RSI=37.6 liquidity=230532.24 spike=0.82
- WKOL.CA: score=0.69 buy_ready=False sector_rank=9 price=281.51 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=19.72 liquidity=560013.94 spike=0.21
- ZEOT.CA: score=20.01 buy_ready=False sector_rank=9 price=11.1 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=9876676.0 spike=0.31
- ZMID.CA: score=22.28 buy_ready=False sector_rank=8 price=6.57 support=5.96 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=51683352.0 spike=0.24

## Backtesting Lite
- SCTS.CA: 180d return=237.76%, max drawdown=-25.28%, MA20>MA50 days last20=16, as_of=2026-06-29T21:00:00+00:00
- RAYA.CA: 180d return=168.53%, max drawdown=-12.86%, MA20>MA50 days last20=20, as_of=2026-06-29T21:00:00+00:00
- AMES.CA: 180d return=34.15%, max drawdown=-54.31%, MA20>MA50 days last20=20, as_of=2026-06-29T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SCTS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Suez Canal Company for Technology Settling summary=Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26; Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends; Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24
  - Suez Canal Technology’s consolidated net profits cross EGP 1.5bn in H1-25/26: https://english.mubasher.info/news/4600018/Suez-Canal-Technology-s-consolidated-net-profits-cross-EGP-1-5bn-in-H1-25-26/
  - Suez Canal Technology’s shareholders greenlight EGP 11/shr dividends: https://english.mubasher.info/news/4463096/Suez-Canal-Technology-s-shareholders-greenlight-EGP-11-shr-dividends/
  - Suez Canal Technology logs EGP 1.3bn consolidated profits in FY23/24: https://english.mubasher.info/news/4366060/Suez-Canal-Technology-logs-EGP-1-3bn-consolidated-profits-in-FY23-24/
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- AMES.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria New Medical Center summary=Alexandria New Medical Center secures FRA nod for EGP 120m capital increase; UAE&#39;s ADCB, shareholder exit Alexandria New Medical Center; Tawasol, LimeVest up stakes in Alexandria New Medical Center
  - Alexandria New Medical Center secures FRA nod for EGP 120m capital increase: https://english.mubasher.info/news/4595375/Alexandria-New-Medical-Center-secures-FRA-nod-for-EGP-120m-capital-increase/
  - UAE&#39;s ADCB, shareholder exit Alexandria New Medical Center: https://english.mubasher.info/news/4018908/UAE-s-ADCB-shareholder-exit-Alexandria-New-Medical-Center/
  - Tawasol, LimeVest up stakes in Alexandria New Medical Center: https://english.mubasher.info/news/4018718/Tawasol-LimeVest-up-stakes-in-Alexandria-New-Medical-Center/
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- ELKA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Cairo for Housing and Development Company (S.A.E) summary=Cairo for Housing’s consolidated profits near EGP 599m in 2025; Cairo Housing stock tests important demand zone; Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium
  - Cairo for Housing’s consolidated profits near EGP 599m in 2025: https://english.mubasher.info/news/4579798/Cairo-for-Housing-s-consolidated-profits-near-EGP-599m-in-2025/
  - Cairo Housing stock tests important demand zone: https://english.mubasher.info/news/4547365/Cairo-Housing-stock-tests-important-demand-zone/
  - Cairo Housing unveils EGP 398m capital hike via H1-25’s share premium: https://english.mubasher.info/news/4540047/Cairo-Housing-unveils-EGP-398m-capital-hike-via-H1-25-s-share-premium/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=546 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/

## Warnings
- Evidence for SCTS.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AMES.CA matches the company but no source/report date was detected.
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence for ELKA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
