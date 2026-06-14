# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-14T08:58:50.770501+00:00
Generated Cairo: 2026-06-14 11:58
Run timing: target 08:45 Cairo | generated Cairo 2026-06-14 11:58 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-14 11:54

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 185/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 14
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 20.0% / above MA50 50.0%
- EGX70 regime: BEARISH / above MA20 47.5% / above MA50 77.5%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=404307104.0 spike=0.6 score=19.68
- CCAP.CA: liquidity=299522496.0 spike=0.36 score=18.3
- TMGH.CA: liquidity=180794432.0 spike=0.41 score=14.62
- ABUK.CA: liquidity=143893888.0 spike=1.21 score=8.81
- ANFI.CA: liquidity=143236051.08 spike=3.32 score=23.53

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (4.76%). Defensive risk mode blocks new buys despite a few stocks showing constructive or bullish‑watch outlooks. Liquidity is cooling on most candidates, and key support levels are relatively far, while RSI levels indicate overbought conditions on several tickets.
- Bearish EGX30/EGX70 trends and low sector breadth keep risk mode at DEFENSIVE_NO_NEW_BUY.
- Top‑ranked tickets (GBCO, EMFD, ANFI, ORWE, ISMQ) show constructive or bullish‑watch outlooks but face cooling liquidity and high RSI, limiting near‑term upside.
- Support levels are 7‑12% away for most, with resistance only a few percent above, suggesting limited price movement in the next 1‑3 days.
- Leading sectors (Automotive & Distribution, Textiles, Real Estate) have mixed returns and modest above‑MA20 percentages, adding uncertainty to sector‑driven moves.

## Top Liquidity Spikes
- TRTO.CA: spike=8.0 liquidity=5988.11 outlook=WEAK_OR_RISKY score=34.22 buy_ready=False
- LUTS.CA: spike=4.56 liquidity=92985048.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EASB.CA: spike=3.87 liquidity=4081920.5 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ANFI.CA: spike=3.32 liquidity=143236051.08 outlook=CONSTRUCTIVE score=66.22 buy_ready=False
- CFGH.CA: spike=3.0 liquidity=18482.3 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=4.67 5d=1.06% 20d=-4.12% aboveMA50=100.0%
- #2 Textiles: score=4.13 5d=-1.86% 20d=4.28% aboveMA50=75.0%
- #3 Real Estate: score=4.06 5d=-3.97% 20d=1.4% aboveMA50=92.31%
- #4 Investment Holding: score=3.24 5d=-4.1% 20d=7.16% aboveMA50=66.67%
- #5 Energy & Petrochemicals: score=2.88 5d=-1.29% 20d=0.1% aboveMA50=75.0%
- #6 Education: score=2.52 5d=-2.15% 20d=-3.64% aboveMA50=100.0%
- #7 Healthcare: score=2.49 5d=-3.22% 20d=-4.87% aboveMA50=100.0%
- #8 Food, Beverages & Tobacco: score=2.44 5d=-3.69% 20d=-1.35% aboveMA50=85.71%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- HELI.CA: BULLISH_WATCH score=90.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KABO.CA: BULLISH_WATCH score=84.13 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORHD.CA: BULLISH_WATCH score=84.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PHDC.CA: BULLISH_WATCH score=84.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=84.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=84.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ISPH.CA: BULLISH_WATCH score=78.49 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- NIPH.CA: BULLISH_WATCH score=78.49 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- RMDA.CA: BULLISH_WATCH score=78.49 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=76.13 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=10.91 buy_ready=False sector_rank=9 price=207.1 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=56.02 liquidity=1025098.31 spike=0.13
- ABUK.CA: score=8.81 buy_ready=False sector_rank=19 price=73.81 support=75.8 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=143893888.0 spike=1.21
- ACAMD.CA: score=19.89 buy_ready=False sector_rank=9 price=2.35 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=64.18 liquidity=75253624.0 spike=0.58
- ACGC.CA: score=9.22 buy_ready=False sector_rank=2 price=9.38 support=8.89 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=3570965.0 spike=0.06
- ADCI.CA: score=16.6 buy_ready=False sector_rank=9 price=228.0 support=202.22 resistance=228.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=71.49 liquidity=6654789.5 spike=1.03
- ADIB.CA: score=17.68 buy_ready=False sector_rank=10 price=45.49 support=44.01 resistance=49.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=36.64 liquidity=25518414.0 spike=0.17
- ADPC.CA: score=3.89 buy_ready=False sector_rank=9 price=3.58 support=3.45 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=4000635.0 spike=0.16
- AFDI.CA: score=12.72 buy_ready=False sector_rank=9 price=41.5 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=43.03 liquidity=4829426.0 spike=0.27
- AFMC.CA: score=8.56 buy_ready=False sector_rank=9 price=71.22 support=67.0 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=672973.63 spike=0.1
- AJWA.CA: score=14.65 buy_ready=False sector_rank=9 price=154.0 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=86.04 liquidity=5766826.5 spike=0.31
- ALCN.CA: score=12.76 buy_ready=False sector_rank=18 price=28.93 support=25.51 resistance=30.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=9216343.0 spike=0.49
- ALUM.CA: score=9.87 buy_ready=False sector_rank=9 price=23.88 support=23.05 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=46.41 liquidity=1977704.25 spike=0.1
- AMER.CA: score=19.62 buy_ready=False sector_rank=3 price=2.67 support=2.52 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=26161468.0 spike=0.24
- AMES.CA: score=3.72 buy_ready=False sector_rank=9 price=49.76 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=14.17 liquidity=834347.0 spike=0.16
- AMIA.CA: score=16.18 buy_ready=False sector_rank=9 price=9.1 support=8.54 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=6290211.0 spike=0.28
- AMOC.CA: score=10.15 buy_ready=False sector_rank=5 price=7.92 support=7.92 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=29.46 liquidity=28518002.0 spike=0.37
- ANFI.CA: score=23.53 buy_ready=False sector_rank=9 price=21.65 support=13.52 resistance=22.8 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=91.11 liquidity=143236051.08 spike=3.32
- APSW.CA: score=2.29 buy_ready=False sector_rank=9 price=8.65 support=8.24 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:24 AM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=399578.13 spike=0.41
- ARAB.CA: score=21.62 buy_ready=False sector_rank=3 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=51273872.0 spike=0.6
- ARCC.CA: score=19.02 buy_ready=False sector_rank=14 price=56.61 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=50.58 liquidity=11066165.0 spike=0.26
- AREH.CA: score=16.89 buy_ready=False sector_rank=9 price=1.52 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=17284016.0 spike=0.65
- ARVA.CA: score=18.89 buy_ready=False sector_rank=9 price=12.17 support=7.71 resistance=11.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=87.58 liquidity=18963810.0 spike=0.77
- ASCM.CA: score=16.89 buy_ready=False sector_rank=9 price=57.55 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=75.66 liquidity=32661422.0 spike=0.46
- ASPI.CA: score=21.89 buy_ready=False sector_rank=9 price=0.32 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=62.87 liquidity=17878156.0 spike=0.27
- ATLC.CA: score=3.65 buy_ready=False sector_rank=20 price=4.79 support=4.7 resistance=5.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=764191.0 spike=0.14
- ATQA.CA: score=12.39 buy_ready=False sector_rank=19 price=9.41 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=42.56 liquidity=12942513.0 spike=0.35
- AXPH.CA: score=8.25 buy_ready=False sector_rank=9 price=1133.59 support=1111.0 resistance=1190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=38.06 liquidity=366911.09 spike=0.09
- BINV.CA: score=13.61 buy_ready=False sector_rank=4 price=45.4 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=1313142.25 spike=0.12
- BIOC.CA: score=8.85 buy_ready=False sector_rank=9 price=70.14 support=68.34 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=41.63 liquidity=958631.69 spike=0.18
- BTFH.CA: score=11.88 buy_ready=False sector_rank=20 price=3.03 support=2.96 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=42703140.0 spike=0.18
- CAED.CA: score=5.34 buy_ready=False sector_rank=9 price=69.68 support=67.21 resistance=82.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=16.38 liquidity=2450776.25 spike=0.2
- CANA.CA: score=13.13 buy_ready=False sector_rank=10 price=36.36 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=59.43 liquidity=1452453.75 spike=0.1
- CCAP.CA: score=18.3 buy_ready=False sector_rank=4 price=5.2 support=4.82 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=299522496.0 spike=0.36
- CCRS.CA: score=10.21 buy_ready=False sector_rank=9 price=2.4 support=2.21 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=2324250.25 spike=0.09
- CEFM.CA: score=3.34 buy_ready=False sector_rank=9 price=106.07 support=100.53 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=451084.03 spike=0.12
- CERA.CA: score=11.0 buy_ready=False sector_rank=9 price=1.18 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=2111597.75 spike=0.15
- CFGH.CA: score=2.91 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=18482.3 spike=3.0
- CICH.CA: score=-1.5 buy_ready=False sector_rank=20 price=11.63 support=11.1 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=15.82 liquidity=618027.63 spike=0.14
- CIEB.CA: score=9.1 buy_ready=False sector_rank=10 price=23.58 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=2423489.75 spike=0.29
- CIRA.CA: score=4.84 buy_ready=False sector_rank=6 price=26.5 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=32.41 liquidity=1833706.88 spike=0.07
- CLHO.CA: score=11.21 buy_ready=False sector_rank=7 price=15.07 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=3216017.25 spike=0.1
- CNFN.CA: score=1.38 buy_ready=False sector_rank=20 price=4.44 support=4.36 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=1496068.0 spike=0.09
- COMI.CA: score=19.68 buy_ready=False sector_rank=10 price=135.0 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=50.51 liquidity=404307104.0 spike=0.6
- COPR.CA: score=16.89 buy_ready=False sector_rank=9 price=0.35 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=32674302.0 spike=0.82
- COSG.CA: score=19.89 buy_ready=False sector_rank=9 price=1.59 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=24018988.0 spike=0.36
- CPCI.CA: score=10.86 buy_ready=False sector_rank=9 price=359.28 support=340.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=975906.38 spike=0.33
- CSAG.CA: score=12.61 buy_ready=False sector_rank=18 price=31.05 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=45.14 liquidity=6069183.0 spike=0.42
- DAPH.CA: score=-0.57 buy_ready=False sector_rank=9 price=78.21 support=76.6 resistance=92.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=25.25 liquidity=545755.88 spike=0.02
- DEIN.CA: score=5.89 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.08 buy_ready=False sector_rank=8 price=24.33 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=1102731.63 spike=0.42
- DSCW.CA: score=15.89 buy_ready=False sector_rank=9 price=1.77 support=1.71 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=10452357.0 spike=0.2
- DTPP.CA: score=0.47 buy_ready=False sector_rank=9 price=120.28 support=117.01 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=21.72 liquidity=580250.75 spike=0.19
- EALR.CA: score=8.85 buy_ready=False sector_rank=9 price=352.86 support=346.01 resistance=386.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=963058.0 spike=0.2
- EASB.CA: score=3.97 buy_ready=False sector_rank=9 price=5.62 support=5.06 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4081920.5 spike=3.87
- EAST.CA: score=21.98 buy_ready=False sector_rank=8 price=38.45 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=50.78 liquidity=19703980.0 spike=0.29
- EBSC.CA: score=12.52 buy_ready=False sector_rank=9 price=1.78 support=1.64 resistance=2.09 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=62.79 liquidity=628751.17 spike=0.27
- ECAP.CA: score=9.9 buy_ready=False sector_rank=9 price=31.58 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=89.69 liquidity=1009325.13 spike=0.19
- EDFM.CA: score=8.27 buy_ready=False sector_rank=9 price=333.62 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=380456.88 spike=0.56
- EEII.CA: score=12.11 buy_ready=False sector_rank=9 price=2.4 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=2223919.25 spike=0.11
- EFIC.CA: score=-1.25 buy_ready=False sector_rank=19 price=205.0 support=192.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=15.17 liquidity=1361031.25 spike=0.38
- EFID.CA: score=17.98 buy_ready=False sector_rank=8 price=27.95 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=38.41 liquidity=10075933.0 spike=0.13
- EFIH.CA: score=7.4 buy_ready=False sector_rank=21 price=21.01 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=30.35 liquidity=14158751.0 spike=0.25
- EGAL.CA: score=11.39 buy_ready=False sector_rank=19 price=313.85 support=305.01 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=15.38 liquidity=21893706.0 spike=0.21
- EGAS.CA: score=14.13 buy_ready=False sector_rank=5 price=51.0 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=3981636.0 spike=0.33
- EGBE.CA: score=2.7 buy_ready=False sector_rank=10 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=30.82 liquidity=16370.96 spike=0.12
- EGCH.CA: score=16.39 buy_ready=False sector_rank=19 price=13.52 support=13.2 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=47.28 liquidity=27432748.0 spike=0.24
- EGSA.CA: score=4.98 buy_ready=False sector_rank=12 price=8.6 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 June 01:09 PM market time freshness=DELAYED_CURRENT RSI=25.37 liquidity=36452.69 spike=2.27
- EGTS.CA: score=19.62 buy_ready=False sector_rank=3 price=18.41 support=13.61 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=19553428.0 spike=0.16
- EHDR.CA: score=19.89 buy_ready=False sector_rank=9 price=2.74 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=70.71 liquidity=37236308.0 spike=0.7
- EKHO.CA: score=10.15 buy_ready=False sector_rank=5 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=7.7 buy_ready=False sector_rank=17 price=2.11 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=5102154.0 spike=0.19
- ELKA.CA: score=20.89 buy_ready=False sector_rank=9 price=1.25 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=11785919.0 spike=0.27
- ELNA.CA: score=6.39 buy_ready=False sector_rank=9 price=37.64 support=37.11 resistance=41.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=43.61 liquidity=759001.31 spike=1.87
- ELSH.CA: score=16.89 buy_ready=False sector_rank=9 price=13.82 support=8.1 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=78.34 liquidity=81952640.0 spike=0.5
- ELWA.CA: score=7.61 buy_ready=False sector_rank=9 price=2.09 support=1.79 resistance=2.2 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=723056.37 spike=0.3
- EMFD.CA: score=23.62 buy_ready=False sector_rank=3 price=11.54 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=63.49 liquidity=107676736.0 spike=0.45
- ENGC.CA: score=18.29 buy_ready=False sector_rank=9 price=34.91 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=58.88 liquidity=6400874.5 spike=0.47
- EOSB.CA: score=15.37 buy_ready=False sector_rank=9 price=1.48 support=1.34 resistance=1.49 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=299753.28 spike=2.59
- EPCO.CA: score=10.58 buy_ready=False sector_rank=9 price=9.17 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=47.45 liquidity=690698.63 spike=0.06
- EPPK.CA: score=5.02 buy_ready=False sector_rank=9 price=12.17 support=11.67 resistance=13.6 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=51.18 liquidity=132202.71 spike=0.13
- ETEL.CA: score=9.4 buy_ready=False sector_rank=12 price=92.22 support=89.8 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=28.49 liquidity=18884578.0 spike=0.22
- ETRS.CA: score=19.89 buy_ready=False sector_rank=9 price=9.27 support=7.37 resistance=9.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=71.97 liquidity=14231771.0 spike=0.25
- EXPA.CA: score=15.86 buy_ready=False sector_rank=10 price=18.61 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=8182637.5 spike=0.22
- FAIT.CA: score=3.54 buy_ready=False sector_rank=10 price=35.7 support=35.0 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=22.01 liquidity=857774.13 spike=0.14
- FAITA.CA: score=7.68 buy_ready=False sector_rank=10 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=4132.26 spike=0.1
- FERC.CA: score=4.26 buy_ready=False sector_rank=19 price=76.57 support=75.0 resistance=81.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=869940.0 spike=0.15
- FWRY.CA: score=7.4 buy_ready=False sector_rank=21 price=18.42 support=17.71 resistance=20.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=29.48 liquidity=122630920.0 spike=0.45
- GBCO.CA: score=23.87 buy_ready=False sector_rank=1 price=28.32 support=25.25 resistance=29.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=72.17 liquidity=66356236.0 spike=0.56
- GDWA.CA: score=8.93 buy_ready=False sector_rank=9 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=51.89 liquidity=5040454.5 spike=0.38
- GGCC.CA: score=10.5 buy_ready=False sector_rank=9 price=0.41 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=1610052.0 spike=0.21
- GIHD.CA: score=8.45 buy_ready=False sector_rank=9 price=40.88 support=35.15 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=562065.31 spike=0.12
- GMCI.CA: score=4.32 buy_ready=False sector_rank=9 price=1.7 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=39.29 liquidity=355529.51 spike=1.04
- GRCA.CA: score=6.14 buy_ready=False sector_rank=9 price=53.48 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=1248865.75 spike=0.14
- GSSC.CA: score=0.53 buy_ready=False sector_rank=9 price=249.2 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=12.69 liquidity=644071.0 spike=0.1
- GTWL.CA: score=0.64 buy_ready=False sector_rank=9 price=47.26 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=25.6 liquidity=750283.56 spike=0.11
- HDBK.CA: score=7.82 buy_ready=False sector_rank=10 price=140.53 support=138.0 resistance=146.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=3137864.25 spike=0.22
- HELI.CA: score=21.62 buy_ready=False sector_rank=3 price=6.5 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=52.56 liquidity=24452162.0 spike=0.15
- HRHO.CA: score=11.88 buy_ready=False sector_rank=20 price=26.5 support=25.8 resistance=29.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=27576014.0 spike=0.18
- ICID.CA: score=16.89 buy_ready=False sector_rank=9 price=6.92 support=4.5 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=87.25 liquidity=12726762.0 spike=0.82
- IDRE.CA: score=10.5 buy_ready=False sector_rank=9 price=43.09 support=41.01 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=44.29 liquidity=2612373.25 spike=0.08
- IFAP.CA: score=-0.45 buy_ready=False sector_rank=15 price=19.21 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=32.23 liquidity=1542610.88 spike=0.16
- INFI.CA: score=3.9 buy_ready=False sector_rank=9 price=100.13 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=24.0 liquidity=2010912.63 spike=0.13
- IRON.CA: score=5.12 buy_ready=False sector_rank=19 price=32.04 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=50.36 liquidity=2724907.5 spike=0.35
- ISMA.CA: score=18.89 buy_ready=False sector_rank=9 price=30.85 support=22.7 resistance=30.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=90.06 liquidity=24763148.0 spike=0.61
- ISMQ.CA: score=21.99 buy_ready=False sector_rank=19 price=8.49 support=7.27 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=110752504.0 spike=1.8
- ISPH.CA: score=20.0 buy_ready=False sector_rank=7 price=11.89 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=54.32 liquidity=29675452.0 spike=0.22
- JUFO.CA: score=21.93 buy_ready=False sector_rank=8 price=29.86 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=64.57 liquidity=9956231.0 spike=0.22
- KABO.CA: score=16.52 buy_ready=False sector_rank=2 price=6.28 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=60.91 liquidity=3871419.25 spike=0.19
- KWIN.CA: score=10.47 buy_ready=False sector_rank=9 price=71.58 support=69.0 resistance=78.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=2582865.5 spike=0.6
- KZPC.CA: score=11.6 buy_ready=False sector_rank=9 price=10.63 support=10.3 resistance=11.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=53.62 liquidity=1711339.25 spike=0.13
- LCSW.CA: score=8.87 buy_ready=False sector_rank=14 price=26.7 support=26.0 resistance=28.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=49.63 liquidity=1851187.0 spike=0.12
- LUTS.CA: score=9.89 buy_ready=False sector_rank=9 price=0.71 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92985048.0 spike=4.56
- MAAL.CA: score=9.75 buy_ready=False sector_rank=9 price=5.8 support=4.44 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=78.07 liquidity=2862108.75 spike=0.22
- MASR.CA: score=17.89 buy_ready=False sector_rank=9 price=6.8 support=6.54 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=13576203.0 spike=0.22
- MBSC.CA: score=12.02 buy_ready=False sector_rank=14 price=273.42 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=20816888.0 spike=0.44
- MCQE.CA: score=6.86 buy_ready=False sector_rank=14 price=178.59 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=11.65 liquidity=7840361.0 spike=0.43
- MCRO.CA: score=13.89 buy_ready=False sector_rank=9 price=1.23 support=1.2 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=13622401.0 spike=0.23
- MENA.CA: score=17.97 buy_ready=False sector_rank=3 price=6.76 support=5.83 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=6343542.0 spike=0.38
- MEPA.CA: score=13.8 buy_ready=False sector_rank=9 price=1.71 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=3915710.5 spike=0.21
- MFPC.CA: score=8.45 buy_ready=False sector_rank=19 price=38.74 support=39.47 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=24.69 liquidity=85129528.0 spike=1.03
- MFSC.CA: score=4.39 buy_ready=False sector_rank=9 price=45.55 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=19.86 liquidity=1504325.5 spike=0.09
- MHOT.CA: score=8.42 buy_ready=False sector_rank=13 price=29.76 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=1042235.56 spike=0.05
- MICH.CA: score=18.46 buy_ready=False sector_rank=9 price=36.92 support=35.01 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=63.94 liquidity=6575912.5 spike=0.46
- MILS.CA: score=15.51 buy_ready=False sector_rank=9 price=145.07 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=60.02 liquidity=5617048.0 spike=0.3
- MIPH.CA: score=8.67 buy_ready=False sector_rank=7 price=658.7 support=640.0 resistance=717.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=52.05 liquidity=670474.19 spike=0.23
- MOED.CA: score=1.24 buy_ready=False sector_rank=9 price=0.67 support=0.65 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=2356979.0 spike=0.2
- MOIL.CA: score=8.19 buy_ready=False sector_rank=5 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=63.77 liquidity=33497.79 spike=0.17
- MOIN.CA: score=7.1 buy_ready=False sector_rank=9 price=25.01 support=24.02 resistance=26.4 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=55.88 liquidity=213810.49 spike=0.14
- MOSC.CA: score=8.29 buy_ready=False sector_rank=9 price=298.21 support=254.15 resistance=298.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25468134.0 spike=2.7
- MPCI.CA: score=19.89 buy_ready=False sector_rank=9 price=220.11 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=17333954.0 spike=0.2
- MPCO.CA: score=21.01 buy_ready=False sector_rank=15 price=1.78 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=32105626.0 spike=0.43
- MPRC.CA: score=13.08 buy_ready=False sector_rank=9 price=32.64 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=3195550.5 spike=0.15
- MTIE.CA: score=15.85 buy_ready=False sector_rank=1 price=8.97 support=8.65 resistance=9.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3983733.5 spike=0.2
- NAHO.CA: score=3.89 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6412.78 spike=0.2
- NCCW.CA: score=16.72 buy_ready=False sector_rank=9 price=6.44 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=76.78 liquidity=9829791.0 spike=0.37
- NEDA.CA: score=8.59 buy_ready=False sector_rank=9 price=2.75 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=53.57 liquidity=503871.5 spike=1.1
- NHPS.CA: score=4.42 buy_ready=False sector_rank=9 price=68.0 support=65.03 resistance=72.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=528774.63 spike=0.09
- NINH.CA: score=4.33 buy_ready=False sector_rank=9 price=17.24 support=16.8 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=24.12 liquidity=1443738.88 spike=0.17
- NIPH.CA: score=20.0 buy_ready=False sector_rank=7 price=166.15 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=25560894.0 spike=0.25
- OBRI.CA: score=13.94 buy_ready=False sector_rank=9 price=35.74 support=33.63 resistance=39.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=40.93 liquidity=7056121.0 spike=0.6
- OCDI.CA: score=16.62 buy_ready=False sector_rank=3 price=20.5 support=20.0 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=46.58 liquidity=11720607.0 spike=0.31
- OCPH.CA: score=3.63 buy_ready=False sector_rank=9 price=349.83 support=337.0 resistance=404.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=28.14 liquidity=740463.44 spike=0.09
- ODIN.CA: score=14.03 buy_ready=False sector_rank=9 price=2.07 support=1.89 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=62.96 liquidity=2140360.75 spike=0.2
- OFH.CA: score=14.87 buy_ready=False sector_rank=9 price=0.6 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=45.54 liquidity=31800672.0 spike=1.49
- OIH.CA: score=10.3 buy_ready=False sector_rank=4 price=1.38 support=1.33 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=29819028.0 spike=0.3
- OLFI.CA: score=16.98 buy_ready=False sector_rank=8 price=22.5 support=21.0 resistance=22.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=75.88 liquidity=18075382.0 spike=0.98
- ORAS.CA: score=4.6 buy_ready=False sector_rank=11 price=768.76 support=756.01 resistance=779.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=131870400.0 spike=1.0
- ORHD.CA: score=21.62 buy_ready=False sector_rank=3 price=37.18 support=33.0 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=46.85 liquidity=63708168.0 spike=0.35
- ORWE.CA: score=22.65 buy_ready=False sector_rank=2 price=23.3 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=11087264.0 spike=0.25
- PHAR.CA: score=11.8 buy_ready=False sector_rank=7 price=85.14 support=83.02 resistance=92.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=48.57 liquidity=3807033.5 spike=0.12
- PHDC.CA: score=21.62 buy_ready=False sector_rank=3 price=15.18 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=58.71 liquidity=134950016.0 spike=0.37
- PHTV.CA: score=4.03 buy_ready=False sector_rank=9 price=204.97 support=201.55 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=1138834.38 spike=0.08
- POUL.CA: score=13.73 buy_ready=False sector_rank=8 price=36.0 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=47.04 liquidity=5751355.0 spike=0.12
- PRCL.CA: score=19.02 buy_ready=False sector_rank=14 price=24.8 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=59.4 liquidity=11649069.0 spike=0.41
- PRDC.CA: score=16.76 buy_ready=False sector_rank=3 price=6.25 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT RSI=80.77 liquidity=8133960.5 spike=0.09
- PRMH.CA: score=16.56 buy_ready=False sector_rank=9 price=2.68 support=2.19 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=6667628.5 spike=0.45
- RACC.CA: score=9.82 buy_ready=False sector_rank=9 price=9.85 support=9.38 resistance=10.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=1935084.88 spike=0.14
- RAKT.CA: score=1.14 buy_ready=False sector_rank=9 price=23.11 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=34.13 liquidity=253031.4 spike=1.0
- RAYA.CA: score=16.8 buy_ready=False sector_rank=16 price=7.11 support=6.7 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=23496740.0 spike=0.23
- RMDA.CA: score=16.64 buy_ready=False sector_rank=7 price=5.1 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=6641803.0 spike=0.07
- ROTO.CA: score=11.73 buy_ready=False sector_rank=9 price=33.94 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:36 AM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=1846500.38 spike=0.14
- RREI.CA: score=6.57 buy_ready=False sector_rank=9 price=3.45 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=1678812.88 spike=0.07
- RTVC.CA: score=9.85 buy_ready=False sector_rank=9 price=3.85 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=2964696.0 spike=0.44
- RUBX.CA: score=6.9 buy_ready=False sector_rank=9 price=9.94 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=3009208.0 spike=0.22
- SAUD.CA: score=6.57 buy_ready=False sector_rank=10 price=21.71 support=20.82 resistance=23.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=37.87 liquidity=1885194.0 spike=0.13
- SCEM.CA: score=4.17 buy_ready=False sector_rank=14 price=61.39 support=59.3 resistance=69.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=29.59 liquidity=5154880.0 spike=0.13
- SCFM.CA: score=2.16 buy_ready=False sector_rank=9 price=251.35 support=248.1 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=26.94 liquidity=2270977.5 spike=0.17
- SCTS.CA: score=3.94 buy_ready=False sector_rank=6 price=612.79 support=590.01 resistance=689.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=25.78 liquidity=930593.81 spike=0.09
- SDTI.CA: score=13.75 buy_ready=False sector_rank=9 price=46.59 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=62.56 liquidity=1864580.88 spike=0.1
- SEIG.CA: score=10.71 buy_ready=False sector_rank=9 price=183.92 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=53.36 liquidity=826284.94 spike=0.16
- SIPC.CA: score=7.59 buy_ready=False sector_rank=9 price=3.47 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=2701072.0 spike=0.19
- SKPC.CA: score=12.39 buy_ready=False sector_rank=19 price=16.47 support=16.29 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=11253126.0 spike=0.18
- SMFR.CA: score=4.44 buy_ready=False sector_rank=9 price=202.14 support=192.0 resistance=222.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=1555952.38 spike=0.27
- SNFC.CA: score=14.29 buy_ready=False sector_rank=9 price=12.33 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=46.44 liquidity=4399715.0 spike=0.16
- SPIN.CA: score=8.43 buy_ready=False sector_rank=2 price=14.0 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=781101.81 spike=0.17
- SPMD.CA: score=9.39 buy_ready=False sector_rank=9 price=0.41 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=56.19 liquidity=1504411.38 spike=0.06
- SUGR.CA: score=9.8 buy_ready=False sector_rank=8 price=48.9 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=1828622.25 spike=0.12
- SVCE.CA: score=9.38 buy_ready=False sector_rank=9 price=8.45 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=27.69 liquidity=6490100.5 spike=0.07
- SWDY.CA: score=11.73 buy_ready=False sector_rank=17 price=86.38 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=39.98 liquidity=5136781.0 spike=0.21
- TALM.CA: score=7.38 buy_ready=False sector_rank=6 price=16.12 support=15.12 resistance=16.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:38 AM market time freshness=DELAYED_CURRENT RSI=79.26 liquidity=372312.91 spike=0.03
- TMGH.CA: score=14.62 buy_ready=False sector_rank=3 price=95.7 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=180794432.0 spike=0.41
- TRTO.CA: score=10.89 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=5988.11 spike=8.0
- UEFM.CA: score=0.04 buy_ready=False sector_rank=9 price=468.99 support=455.6 resistance=500.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=26.76 liquidity=796813.99 spike=1.18
- UEGC.CA: score=15.31 buy_ready=False sector_rank=9 price=1.39 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:43 AM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=3424317.25 spike=0.13
- UNIP.CA: score=15.55 buy_ready=False sector_rank=9 price=0.32 support=0.28 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=80.39 liquidity=9665956.0 spike=0.49
- UNIT.CA: score=12.4 buy_ready=False sector_rank=3 price=13.94 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=61.5 liquidity=780645.0 spike=0.07
- WCDF.CA: score=-4.33 buy_ready=False sector_rank=9 price=503.92 support=450.0 resistance=544.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=425940.69 spike=1.18
- WKOL.CA: score=6.23 buy_ready=False sector_rank=9 price=292.51 support=290.0 resistance=319.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=1340323.63 spike=0.33
- ZEOT.CA: score=16.59 buy_ready=False sector_rank=9 price=9.24 support=8.41 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=63.78 liquidity=4699378.5 spike=0.75
- ZMID.CA: score=21.62 buy_ready=False sector_rank=3 price=6.27 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:40 AM market time freshness=DELAYED_CURRENT RSI=59.69 liquidity=89019448.0 spike=0.38

## Backtesting Lite
- GBCO.CA: 180d return=31.89%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- EMFD.CA: 180d return=38.05%, max drawdown=-15.54%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- ANFI.CA: 180d return=235.87%, max drawdown=-19.31%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=529 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=529 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- ISMQ.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Iron and Steel for Mines and Quarries summary=Iron and Steel for Mines and Quarries stock stabilizes above key support after correction; Will Iron and Steel for Mines and Quarries stock hit new historical peaks?; Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25
  - Iron and Steel for Mines and Quarries stock stabilizes above key support after correction: https://english.mubasher.info/news/4578786/Iron-and-Steel-for-Mines-and-Quarries-stock-stabilizes-above-key-support-after-correction/
  - Will Iron and Steel for Mines and Quarries stock hit new historical peaks?: https://english.mubasher.info/news/4556956/Will-Iron-and-Steel-for-Mines-and-Quarries-stock-hit-new-historical-peaks-/
  - Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25: https://english.mubasher.info/news/4249734/Iron-and-Steel-for-Mines-and-Quarries-expects-EGP-448m-net-profit-in-FY24-25/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- JUFO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Juhayna Food Industries summary=Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.
- ASPI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Aspire Capital Holding for Financial Investments summary=Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25; PREDCO, Aspire Holding consider establishing mortgage company; Pioneers Holding gets EGX&#39;s approval for capital cut, name change
  - Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25: https://english.mubasher.info/news/4541324/Aspire-Capital-records-higher-consolidated-net-profits-at-over-EGP-42m-in-9M-25/
  - PREDCO, Aspire Holding consider establishing mortgage company: https://english.mubasher.info/news/4185438/PREDCO-Aspire-Holding-consider-establishing-mortgage-company/
  - Pioneers Holding gets EGX&#39;s approval for capital cut, name change: https://english.mubasher.info/news/3861454/Pioneers-Holding-gets-EGX-s-approval-for-capital-cut-name-change/

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ISMQ.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
