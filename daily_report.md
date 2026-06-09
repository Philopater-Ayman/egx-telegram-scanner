# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-09T10:05:31.178886+00:00
Generated Cairo: 2026-06-09 13:05
Run timing: target 09:15 Cairo | generated Cairo 2026-06-09 13:05 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-09 13:01

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 183/190
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 09
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 65.0%
- EGX70 regime: MIXED / above MA20 62.5% / above MA50 87.5%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ZMID.CA: liquidity=383814176.0 spike=1.84 score=25.08
- CCAP.CA: liquidity=375163552.0 spike=0.43 score=26.4
- COMI.CA: liquidity=360896192.0 spike=0.53 score=18.48
- ELSH.CA: liquidity=273485920.0 spike=2.34 score=22.85
- PHDC.CA: liquidity=252029824.0 spike=0.6 score=19.4

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlights a defensive market regime – EGX30 is bearish and EGX70 mixed, with sector breadth only 19 % and risk mode set to DEFENSIVE_NO_NEW_BUY. Consequently, no BUY signals are issued despite several stocks showing bullish watch outlooks and decent liquidity. The top tickets are flagged for monitoring because they sit near support or resistance levels, have tradeable or accumulation‑spike liquidity, and belong to the few leading sectors (Investment Holding, Tourism & Leisure, Technology). However, weak breadth and negative short‑term returns keep the overall risk outlook uncertain for the next 1‑3 days.
- EGX30 bearish, EGX70 mixed → risk mode blocks new buys; only hold/watch positions.
- Sector breadth 19 % (below threshold) limits confidence despite Investment Holding sector strength.
- Top tickets (e.g., CCAP.CA, CERA.CA, ZMID.CA) have tradeable liquidity and are near 20‑day support/resistance, but outlooks remain watch‑only.
- Liquidity spikes are moderate; some stocks show cooling or overheating RSI, adding short‑term uncertainty.
- Expect continued volatility; monitor sector breadth and EGX30 trend before considering any entry.

## Top Liquidity Spikes
- AJWA.CA: spike=9.64 liquidity=100722488.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NCCW.CA: spike=3.75 liquidity=77267184.0 outlook=CONSTRUCTIVE score=68.42 buy_ready=False
- ELSH.CA: spike=2.34 liquidity=273485920.0 outlook=CONSTRUCTIVE score=62.42 buy_ready=False
- CFGH.CA: spike=2.34 liquidity=10512.3 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ENGC.CA: spike=2.13 liquidity=25304064.0 outlook=BULLISH_WATCH score=84.42 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=7.73 5d=2.57% 20d=12.11% aboveMA50=66.67%
- #2 Tourism & Leisure: score=6.82 5d=-8.23% 20d=13.34% aboveMA50=100.0%
- #3 Technology & Distribution: score=6.72 5d=-0.67% 20d=2.76% aboveMA50=100.0%
- #4 Real Estate: score=6.38 5d=-0.41% 20d=5.37% aboveMA50=76.92%
- #5 Healthcare: score=5.96 5d=2.38% 20d=0.11% aboveMA50=100.0%
- #6 Automotive & Distribution: score=5.64 5d=-1.33% 20d=-5.43% aboveMA50=100.0%
- #7 General / Verified EGX Expansion: score=5.42 5d=1.06% 20d=0.01% aboveMA50=82.69%
- #8 Food, Beverages & Tobacco: score=4.94 5d=-0.67% 20d=0.35% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CERA.CA: BULLISH_WATCH score=95.42 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ANFI.CA: BULLISH_WATCH score=94.42 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ZMID.CA: BULLISH_WATCH score=93.38 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RAYA.CA: BULLISH_WATCH score=92.72 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MHOT.CA: BULLISH_WATCH score=91.82 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- GBCO.CA: BULLISH_WATCH score=86.64 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EPCO.CA: BULLISH_WATCH score=86.42 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- SEIG.CA: BULLISH_WATCH score=86.42 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- KWIN.CA: BULLISH_WATCH score=86.42 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ROTO.CA: BULLISH_WATCH score=84.42 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=7.43 buy_ready=False sector_rank=7 price=227.88 support=211.65 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19017282.0 spike=1.63
- ABUK.CA: score=9.77 buy_ready=False sector_rank=18 price=81.44 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=18.89 liquidity=29732344.0 spike=0.23
- ACAMD.CA: score=23.39 buy_ready=False sector_rank=7 price=2.29 support=2.03 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 June 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.34 liquidity=133482416.0 spike=1.11
- ACGC.CA: score=20.86 buy_ready=False sector_rank=12 price=9.89 support=8.51 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=60.49 liquidity=36863888.0 spike=0.67
- ADCI.CA: score=12.45 buy_ready=False sector_rank=7 price=218.58 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=3281264.0 spike=0.49
- ADIB.CA: score=18.48 buy_ready=False sector_rank=15 price=46.41 support=45.0 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=46.78 liquidity=39500984.0 spike=0.25
- ADPC.CA: score=8.55 buy_ready=False sector_rank=7 price=3.7 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=23.16 liquidity=4378437.0 spike=0.18
- AFDI.CA: score=16.33 buy_ready=False sector_rank=7 price=44.0 support=38.51 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=65.42 liquidity=5162999.5 spike=0.28
- AFMC.CA: score=9.49 buy_ready=False sector_rank=7 price=72.73 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=322278.25 spike=0.02
- AJWA.CA: score=11.17 buy_ready=False sector_rank=7 price=146.0 support=135.0 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100722488.0 spike=9.64
- ALCN.CA: score=10.84 buy_ready=False sector_rank=20 price=28.86 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=43.44 liquidity=6699946.5 spike=0.29
- ALUM.CA: score=23.53 buy_ready=False sector_rank=7 price=26.01 support=22.52 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=25971418.0 spike=1.18
- AMER.CA: score=21.4 buy_ready=False sector_rank=4 price=2.8 support=2.32 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=96597448.0 spike=0.82
- AMES.CA: score=6.7 buy_ready=False sector_rank=7 price=51.02 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=30.81 liquidity=2536629.0 spike=0.33
- AMIA.CA: score=21.17 buy_ready=False sector_rank=7 price=9.08 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=12926183.0 spike=0.43
- AMOC.CA: score=13.96 buy_ready=False sector_rank=9 price=8.27 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=20447070.0 spike=0.24
- ANFI.CA: score=25.03 buy_ready=False sector_rank=7 price=15.52 support=13.5 resistance=16.04 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=59.56 liquidity=39216123.4 spike=1.93
- APSW.CA: score=3.51 buy_ready=False sector_rank=7 price=8.88 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=29.21 liquidity=337841.84 spike=0.32
- ARAB.CA: score=17.4 buy_ready=False sector_rank=4 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=17495064.0 spike=0.23
- ARCC.CA: score=18.54 buy_ready=False sector_rank=10 price=58.01 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=66.79 liquidity=7598228.0 spike=0.18
- AREH.CA: score=20.17 buy_ready=False sector_rank=7 price=1.52 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=22544184.0 spike=0.84
- ARVA.CA: score=20.17 buy_ready=False sector_rank=7 price=11.21 support=7.71 resistance=11.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=80.46 liquidity=16631056.0 spike=0.67
- ASCM.CA: score=18.17 buy_ready=False sector_rank=7 price=56.02 support=46.2 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=75.21 liquidity=34617532.0 spike=0.53
- ASPI.CA: score=24.49 buy_ready=False sector_rank=7 price=0.35 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=56.96 liquidity=94638456.0 spike=1.66
- ATLC.CA: score=10.66 buy_ready=False sector_rank=17 price=5.02 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=2626670.5 spike=0.36
- ATQA.CA: score=21.77 buy_ready=False sector_rank=18 price=9.97 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=54.35 liquidity=13407301.0 spike=0.32
- AXPH.CA: score=14.9 buy_ready=False sector_rank=7 price=1152.84 support=1023.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=48.22 liquidity=3732443.25 spike=0.64
- BINV.CA: score=15.86 buy_ready=False sector_rank=1 price=46.31 support=40.53 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=65.88 liquidity=1461008.88 spike=0.12
- BIOC.CA: score=10.65 buy_ready=False sector_rank=7 price=73.13 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT RSI=60.99 liquidity=1486457.88 spike=0.21
- BTFH.CA: score=12.04 buy_ready=False sector_rank=17 price=3.07 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=72501224.0 spike=0.31
- CAED.CA: score=10.23 buy_ready=False sector_rank=7 price=72.63 support=70.41 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=32.89 liquidity=6065826.0 spike=0.4
- CANA.CA: score=15.22 buy_ready=False sector_rank=15 price=37.27 support=33.15 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=75.35 liquidity=5733625.0 spike=0.4
- CCAP.CA: score=26.4 buy_ready=False sector_rank=1 price=5.54 support=4.66 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=375163552.0 spike=0.43
- CCRS.CA: score=17.43 buy_ready=False sector_rank=7 price=2.48 support=2.05 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=51.32 liquidity=6266233.5 spike=0.23
- CEFM.CA: score=4.69 buy_ready=False sector_rank=7 price=106.06 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=34.03 liquidity=519005.66 spike=0.07
- CERA.CA: score=25.25 buy_ready=False sector_rank=7 price=1.2 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=23863354.0 spike=1.54
- CFGH.CA: score=2.86 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=10512.3 spike=2.34
- CICH.CA: score=11.22 buy_ready=False sector_rank=17 price=11.89 support=11.45 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=3180906.25 spike=0.71
- CIEB.CA: score=11.34 buy_ready=False sector_rank=15 price=23.54 support=23.31 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=47.01 liquidity=2856934.5 spike=0.27
- CIRA.CA: score=13.82 buy_ready=False sector_rank=16 price=26.51 support=21.0 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=41.34 liquidity=5336076.0 spike=0.19
- CLHO.CA: score=19.38 buy_ready=False sector_rank=5 price=15.0 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=40.9 liquidity=13624978.0 spike=0.39
- CNFN.CA: score=10.19 buy_ready=False sector_rank=17 price=4.58 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=3157835.5 spike=0.18
- COMI.CA: score=18.48 buy_ready=False sector_rank=15 price=132.66 support=129.8 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=45.93 liquidity=360896192.0 spike=0.53
- COPR.CA: score=18.72 buy_ready=False sector_rank=7 price=0.36 support=0.32 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=8556657.0 spike=0.22
- COSG.CA: score=21.17 buy_ready=False sector_rank=7 price=1.65 support=1.45 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=65.71 liquidity=25423124.0 spike=0.42
- CPCI.CA: score=8.71 buy_ready=False sector_rank=7 price=363.36 support=340.01 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=86.18 liquidity=542344.75 spike=0.07
- CSAG.CA: score=12.36 buy_ready=False sector_rank=20 price=31.3 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=52.62 liquidity=5224834.5 spike=0.28
- DAPH.CA: score=9.63 buy_ready=False sector_rank=7 price=81.8 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=21.61 liquidity=5458989.0 spike=0.18
- DEIN.CA: score=7.17 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=5.55 buy_ready=False sector_rank=8 price=25.06 support=24.24 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=25.1 liquidity=1572436.38 spike=0.67
- DSCW.CA: score=19.17 buy_ready=False sector_rank=7 price=1.83 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=10592827.0 spike=0.17
- DTPP.CA: score=5.35 buy_ready=False sector_rank=7 price=125.04 support=123.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=31.36 liquidity=1180111.88 spike=0.25
- EALR.CA: score=6.19 buy_ready=False sector_rank=7 price=373.65 support=352.93 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10314986.0 spike=1.01
- EASB.CA: score=10.12 buy_ready=False sector_rank=7 price=5.01 support=4.61 resistance=5.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=70.31 liquidity=948299.44 spike=0.63
- EAST.CA: score=19.35 buy_ready=False sector_rank=8 price=39.87 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=61.61 liquidity=4378027.0 spike=0.06
- EBSC.CA: score=11.59 buy_ready=False sector_rank=7 price=1.85 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=424864.78 spike=0.14
- ECAP.CA: score=12.27 buy_ready=False sector_rank=7 price=31.73 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=88.64 liquidity=4103847.0 spike=0.79
- EDFM.CA: score=15.28 buy_ready=False sector_rank=7 price=338.53 support=320.2 resistance=347.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=2173450.25 spike=1.97
- EEII.CA: score=22.11 buy_ready=False sector_rank=7 price=2.49 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=27294950.0 spike=1.47
- EFIC.CA: score=2.06 buy_ready=False sector_rank=18 price=205.68 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=6.06 liquidity=2293123.75 spike=0.57
- EFID.CA: score=18.98 buy_ready=False sector_rank=8 price=28.1 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=59.78 liquidity=23005288.0 spike=0.3
- EFIH.CA: score=15.72 buy_ready=False sector_rank=21 price=21.18 support=21.0 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=43.85 liquidity=18763598.0 spike=0.29
- EGAL.CA: score=17.77 buy_ready=False sector_rank=18 price=318.75 support=303.05 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=36782408.0 spike=0.33
- EGAS.CA: score=12.01 buy_ready=False sector_rank=9 price=49.71 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=1041825.94 spike=0.08
- EGBE.CA: score=3.58 buy_ready=False sector_rank=15 price=0.44 support=0.42 resistance=0.47 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=31.41 liquidity=97103.89 spike=0.75
- EGCH.CA: score=21.77 buy_ready=False sector_rank=18 price=14.7 support=12.26 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=16365638.0 spike=0.14
- EGSA.CA: score=8.7 buy_ready=False sector_rank=13 price=8.83 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=74.7 liquidity=11854.4 spike=0.78
- EGTS.CA: score=7.22 buy_ready=False sector_rank=4 price=19.6 support=18.35 resistance=20.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156490224.0 spike=1.41
- EHDR.CA: score=18.17 buy_ready=False sector_rank=7 price=2.68 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=83.08 liquidity=32162418.0 spike=0.6
- EKHO.CA: score=10.96 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=19.55 buy_ready=False sector_rank=14 price=2.16 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=7966619.5 spike=0.28
- ELKA.CA: score=22.17 buy_ready=False sector_rank=7 price=1.27 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=21500516.0 spike=0.52
- ELNA.CA: score=4.23 buy_ready=False sector_rank=7 price=39.54 support=37.11 resistance=42.79 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=31.97 liquidity=64885.14 spike=0.21
- ELSH.CA: score=22.85 buy_ready=False sector_rank=7 price=13.39 support=7.92 resistance=13.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=86.84 liquidity=273485920.0 spike=2.34
- ELWA.CA: score=10.74 buy_ready=False sector_rank=7 price=2.14 support=1.79 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=91.43 liquidity=570501.81 spike=0.18
- EMFD.CA: score=21.4 buy_ready=False sector_rank=4 price=12.05 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=74.1 liquidity=108195368.0 spike=0.47
- ENGC.CA: score=23.43 buy_ready=False sector_rank=7 price=34.97 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=25304064.0 spike=2.13
- EOSB.CA: score=9.27 buy_ready=False sector_rank=7 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=100002.08 spike=0.84
- EPCO.CA: score=21.17 buy_ready=False sector_rank=7 price=9.31 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=12403433.0 spike=0.99
- EPPK.CA: score=10.56 buy_ready=False sector_rank=7 price=12.5 support=11.67 resistance=13.6 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=51.79 liquidity=1530000.0 spike=1.43
- ETEL.CA: score=18.68 buy_ready=False sector_rank=13 price=94.0 support=92.17 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=45869040.0 spike=0.41
- ETRS.CA: score=6.97 buy_ready=False sector_rank=7 price=9.4 support=9.0 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=71668880.0 spike=1.4
- EXPA.CA: score=20.48 buy_ready=False sector_rank=15 price=19.0 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=25499784.0 spike=0.61
- FAIT.CA: score=11.52 buy_ready=False sector_rank=15 price=37.34 support=33.94 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=1040813.81 spike=0.16
- FAITA.CA: score=8.49 buy_ready=False sector_rank=15 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=8800.4 spike=0.17
- FERC.CA: score=0.89 buy_ready=False sector_rank=18 price=77.4 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=1120404.13 spike=0.18
- FWRY.CA: score=12.72 buy_ready=False sector_rank=21 price=18.67 support=18.32 resistance=21.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=38.25 liquidity=89012576.0 spike=0.3
- GBCO.CA: score=22.0 buy_ready=False sector_rank=6 price=27.57 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=156007072.0 spike=1.37
- GDWA.CA: score=16.8 buy_ready=False sector_rank=7 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=4632581.0 spike=0.45
- GGCC.CA: score=21.59 buy_ready=False sector_rank=7 price=0.43 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=8762079.0 spike=1.33
- GIHD.CA: score=13.75 buy_ready=False sector_rank=7 price=41.85 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=53.59 liquidity=585740.13 spike=0.11
- GMCI.CA: score=11.44 buy_ready=False sector_rank=7 price=1.78 support=1.67 resistance=1.84 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=65.38 liquidity=274689.6 spike=0.84
- GRCA.CA: score=2.46 buy_ready=False sector_rank=7 price=54.16 support=53.16 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=27.6 liquidity=1294227.0 spike=0.14
- GSSC.CA: score=3.07 buy_ready=False sector_rank=7 price=249.08 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=7.12 liquidity=1903446.63 spike=0.22
- GTWL.CA: score=8.52 buy_ready=False sector_rank=7 price=47.79 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=13.49 liquidity=7347377.0 spike=0.98
- HDBK.CA: score=10.6 buy_ready=False sector_rank=15 price=142.17 support=138.75 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=58.6 liquidity=5114827.0 spike=0.31
- HELI.CA: score=21.4 buy_ready=False sector_rank=4 price=6.63 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=106601096.0 spike=0.64
- HRHO.CA: score=14.04 buy_ready=False sector_rank=17 price=26.47 support=26.05 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=26059394.0 spike=0.14
- ICID.CA: score=20.61 buy_ready=False sector_rank=7 price=6.42 support=4.43 resistance=6.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=87.56 liquidity=15395879.0 spike=1.22
- IDRE.CA: score=12.83 buy_ready=False sector_rank=7 price=44.07 support=39.72 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=50.96 liquidity=3663288.25 spike=0.11
- IFAP.CA: score=2.82 buy_ready=False sector_rank=11 price=19.45 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=2885485.5 spike=0.18
- INFI.CA: score=18.17 buy_ready=False sector_rank=7 price=102.05 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=12417035.0 spike=0.74
- IRON.CA: score=8.99 buy_ready=False sector_rank=18 price=32.48 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=3217172.75 spike=0.39
- ISMA.CA: score=18.27 buy_ready=False sector_rank=7 price=29.67 support=20.15 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=91.81 liquidity=51438136.0 spike=1.05
- ISMQ.CA: score=22.73 buy_ready=False sector_rank=18 price=8.0 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=72463256.0 spike=1.48
- ISPH.CA: score=23.38 buy_ready=False sector_rank=5 price=12.4 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=64.73 liquidity=44062900.0 spike=0.29
- JUFO.CA: score=23.0 buy_ready=False sector_rank=8 price=30.43 support=26.51 resistance=30.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=71.6 liquidity=46295996.0 spike=1.01
- KABO.CA: score=16.71 buy_ready=False sector_rank=12 price=6.3 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=5852386.0 spike=0.3
- KWIN.CA: score=16.82 buy_ready=False sector_rank=7 price=73.23 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=44.62 liquidity=4974859.0 spike=1.34
- KZPC.CA: score=11.6 buy_ready=False sector_rank=7 price=10.6 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=44.2 liquidity=2434054.25 spike=0.21
- LCSW.CA: score=12.5 buy_ready=False sector_rank=10 price=27.4 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=45.55 liquidity=3561467.0 spike=0.22
- LUTS.CA: score=21.17 buy_ready=False sector_rank=7 price=0.63 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=71.69 liquidity=10039718.0 spike=0.63
- MAAL.CA: score=25.17 buy_ready=False sector_rank=7 price=6.04 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11814076.0 spike=1.0
- MASR.CA: score=19.17 buy_ready=False sector_rank=7 price=6.93 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.48 liquidity=17003250.0 spike=0.29
- MBSC.CA: score=20.94 buy_ready=False sector_rank=10 price=276.11 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=51.41 liquidity=28469904.0 spike=0.58
- MCQE.CA: score=18.94 buy_ready=False sector_rank=10 price=188.52 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=52.24 liquidity=13446167.0 spike=0.7
- MCRO.CA: score=20.17 buy_ready=False sector_rank=7 price=1.26 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=11344778.0 spike=0.13
- MENA.CA: score=14.98 buy_ready=False sector_rank=4 price=6.8 support=5.76 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=1576703.75 spike=0.1
- MEPA.CA: score=21.17 buy_ready=False sector_rank=7 price=1.72 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=12508143.0 spike=0.59
- MFPC.CA: score=9.77 buy_ready=False sector_rank=18 price=42.08 support=42.3 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=27772458.0 spike=0.29
- MFSC.CA: score=7.07 buy_ready=False sector_rank=7 price=46.93 support=33.01 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=25.62 liquidity=2905054.75 spike=0.19
- MHOT.CA: score=23.4 buy_ready=False sector_rank=2 price=30.86 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=18920646.0 spike=0.96
- MICH.CA: score=16.2 buy_ready=False sector_rank=7 price=36.84 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=60.8 liquidity=3027277.25 spike=0.34
- MILS.CA: score=16.0 buy_ready=False sector_rank=7 price=144.13 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=48.66 liquidity=4831837.0 spike=0.17
- MIPH.CA: score=10.29 buy_ready=False sector_rank=5 price=663.62 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=39.8 liquidity=910730.19 spike=0.24
- MOED.CA: score=5.73 buy_ready=False sector_rank=7 price=0.69 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=18.28 liquidity=5566512.0 spike=0.42
- MOIL.CA: score=13.04 buy_ready=False sector_rank=9 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=61.43 liquidity=71188.75 spike=0.38
- MOIN.CA: score=11.6 buy_ready=False sector_rank=7 price=24.99 support=23.13 resistance=26.4 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=1429452.98 spike=0.8
- MOSC.CA: score=5.95 buy_ready=False sector_rank=7 price=265.77 support=268.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=20.91 liquidity=1783734.0 spike=0.13
- MPCI.CA: score=23.17 buy_ready=False sector_rank=7 price=228.95 support=192.01 resistance=233.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=68.01 liquidity=94872072.0 spike=0.95
- MPCO.CA: score=21.42 buy_ready=False sector_rank=11 price=1.8 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=83866552.0 spike=1.24
- MPRC.CA: score=18.59 buy_ready=False sector_rank=7 price=33.64 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=73.66 liquidity=7422709.5 spike=0.35
- MTIE.CA: score=18.06 buy_ready=False sector_rank=6 price=9.16 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=6805799.5 spike=0.31
- NAHO.CA: score=5.18 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=7798.24 spike=0.21
- NCCW.CA: score=25.17 buy_ready=False sector_rank=7 price=6.55 support=5.13 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=79.77 liquidity=77267184.0 spike=3.75
- NEDA.CA: score=11.49 buy_ready=False sector_rank=7 price=2.8 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=326233.59 spike=0.62
- NHPS.CA: score=15.15 buy_ready=False sector_rank=7 price=70.16 support=67.53 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=44.84 liquidity=3980189.5 spike=0.37
- NINH.CA: score=10.36 buy_ready=False sector_rank=7 price=17.9 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=1192531.13 spike=0.1
- NIPH.CA: score=21.38 buy_ready=False sector_rank=5 price=168.09 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=74085432.0 spike=0.61
- OBRI.CA: score=9.2 buy_ready=False sector_rank=7 price=34.88 support=33.63 resistance=39.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=30.2 liquidity=8030548.5 spike=0.76
- OCDI.CA: score=16.4 buy_ready=False sector_rank=4 price=21.0 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=45.23 liquidity=11684094.0 spike=0.28
- OCPH.CA: score=8.87 buy_ready=False sector_rank=7 price=363.29 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=32.47 liquidity=4699696.0 spike=0.43
- ODIN.CA: score=15.57 buy_ready=False sector_rank=7 price=2.08 support=1.89 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=4401885.5 spike=0.44
- OFH.CA: score=23.17 buy_ready=False sector_rank=7 price=0.63 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=14983275.0 spike=0.68
- OIH.CA: score=14.4 buy_ready=False sector_rank=1 price=1.41 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=22397556.0 spike=0.19
- OLFI.CA: score=15.28 buy_ready=False sector_rank=8 price=21.57 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=6307579.5 spike=0.28
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=730.77 support=717.0 resistance=740.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=105847984.0 spike=1.0
- ORHD.CA: score=19.4 buy_ready=False sector_rank=4 price=37.0 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=65.64 liquidity=116279304.0 spike=0.57
- ORWE.CA: score=20.86 buy_ready=False sector_rank=12 price=23.73 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=69.79 liquidity=15948696.0 spike=0.35
- PHAR.CA: score=13.26 buy_ready=False sector_rank=5 price=86.42 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=3879359.5 spike=0.11
- PHDC.CA: score=19.4 buy_ready=False sector_rank=4 price=15.2 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=252029824.0 spike=0.6
- PHTV.CA: score=13.54 buy_ready=False sector_rank=7 price=207.63 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=4367333.5 spike=0.29
- POUL.CA: score=16.89 buy_ready=False sector_rank=8 price=37.01 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=60.74 liquidity=5915353.0 spike=0.12
- PRCL.CA: score=24.72 buy_ready=False sector_rank=10 price=25.34 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=68153824.0 spike=1.89
- PRDC.CA: score=15.4 buy_ready=False sector_rank=4 price=6.09 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=72.93 liquidity=4000858.5 spike=0.2
- PRMH.CA: score=18.17 buy_ready=False sector_rank=7 price=2.79 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=83.52 liquidity=11456101.0 spike=0.71
- RACC.CA: score=11.69 buy_ready=False sector_rank=7 price=9.87 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=2522557.25 spike=0.11
- RAKT.CA: score=9.43 buy_ready=False sector_rank=7 price=23.79 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=54.9 liquidity=262070.65 spike=0.99
- RAYA.CA: score=22.4 buy_ready=False sector_rank=3 price=7.5 support=6.94 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=33224446.0 spike=0.29
- RMDA.CA: score=21.38 buy_ready=False sector_rank=5 price=5.28 support=4.91 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=38086532.0 spike=0.35
- ROTO.CA: score=24.53 buy_ready=False sector_rank=7 price=34.85 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=20407752.0 spike=1.68
- RREI.CA: score=18.7 buy_ready=False sector_rank=7 price=3.57 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=60.27 liquidity=5533987.5 spike=0.24
- RTVC.CA: score=17.14 buy_ready=False sector_rank=7 price=3.99 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=50.82 liquidity=3973822.0 spike=0.62
- RUBX.CA: score=15.35 buy_ready=False sector_rank=7 price=10.51 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=17.0 liquidity=23061628.0 spike=1.59
- SAUD.CA: score=12.56 buy_ready=False sector_rank=15 price=22.17 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=49.51 liquidity=4073991.5 spike=0.29
- SCEM.CA: score=13.14 buy_ready=False sector_rank=10 price=63.91 support=62.5 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=4198588.5 spike=0.1
- SCFM.CA: score=9.68 buy_ready=False sector_rank=7 price=264.06 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=25.91 liquidity=5512710.0 spike=0.19
- SCTS.CA: score=11.49 buy_ready=False sector_rank=16 price=627.47 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=17.82 liquidity=8010874.0 spike=0.73
- SDTI.CA: score=22.14 buy_ready=False sector_rank=7 price=46.47 support=43.4 resistance=46.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=60.94 liquidity=8973690.0 spike=0.47
- SEIG.CA: score=18.82 buy_ready=False sector_rank=7 price=187.97 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=5655580.0 spike=1.0
- SIPC.CA: score=23.21 buy_ready=False sector_rank=7 price=3.67 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=15816982.0 spike=1.02
- SKPC.CA: score=13.77 buy_ready=False sector_rank=18 price=17.27 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=35.68 liquidity=22265914.0 spike=0.31
- SMFR.CA: score=5.83 buy_ready=False sector_rank=7 price=207.19 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=30.74 liquidity=1657532.25 spike=0.22
- SNFC.CA: score=12.92 buy_ready=False sector_rank=7 price=12.03 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=3749368.5 spike=0.14
- SPIN.CA: score=7.14 buy_ready=False sector_rank=12 price=14.09 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=43.23 liquidity=1276476.75 spike=0.26
- SPMD.CA: score=21.27 buy_ready=False sector_rank=7 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=8104932.0 spike=0.32
- SUGR.CA: score=17.16 buy_ready=False sector_rank=8 price=49.94 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=37.22 liquidity=4181761.0 spike=0.26
- SVCE.CA: score=19.17 buy_ready=False sector_rank=7 price=8.76 support=8.33 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=17777922.0 spike=0.14
- SWDY.CA: score=15.07 buy_ready=False sector_rank=14 price=87.37 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=6489868.5 spike=0.18
- TALM.CA: score=20.48 buy_ready=False sector_rank=16 price=16.0 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=51.08 liquidity=10979131.0 spike=0.84
- TMGH.CA: score=21.4 buy_ready=False sector_rank=4 price=96.9 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=60.15 liquidity=170909712.0 spike=0.33
- TRTO.CA: score=7.17 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=211.38 spike=0.44
- UEFM.CA: score=5.52 buy_ready=False sector_rank=7 price=474.63 support=455.6 resistance=505.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=36.58 liquidity=356881.06 spike=0.22
- UEGC.CA: score=21.17 buy_ready=False sector_rank=7 price=1.45 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=14818130.0 spike=0.6
- UNIP.CA: score=20.17 buy_ready=False sector_rank=7 price=0.32 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=67.69 liquidity=11604003.0 spike=0.74
- UNIT.CA: score=17.68 buy_ready=False sector_rank=4 price=14.24 support=10.89 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=65.67 liquidity=6281836.5 spike=0.59
- WCDF.CA: score=4.92 buy_ready=False sector_rank=7 price=539.17 support=535.0 resistance=559.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=13.84 liquidity=370948.95 spike=1.19
- WKOL.CA: score=7.47 buy_ready=False sector_rank=7 price=311.29 support=291.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10340458.0 spike=1.65
- ZEOT.CA: score=15.53 buy_ready=False sector_rank=7 price=9.31 support=8.43 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=58.16 liquidity=2361870.75 spike=0.33
- ZMID.CA: score=25.08 buy_ready=False sector_rank=4 price=6.44 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=383814176.0 spike=1.84

## Backtesting Lite
- CCAP.CA: 180d return=118.82%, max drawdown=-25.0%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- CERA.CA: 180d return=-36.84%, max drawdown=-46.32%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- MAAL.CA: 180d return=38.05%, max drawdown=-27.25%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- MAAL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Marseille Almasreia Alkhalegeya For Holding Investment SAE summary=Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- NCCW.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Nasr Company for Civil Works summary=Nasr for Civil Works unveils EGP 150m capital increase; Arabia Investments, Nasr Company for Civil Works unveil capital hike; Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda
  - Nasr for Civil Works unveils EGP 150m capital increase: https://english.mubasher.info/news/4550493/Nasr-for-Civil-Works-unveils-EGP-150m-capital-increase/
  - Arabia Investments, Nasr Company for Civil Works unveil capital hike: https://english.mubasher.info/news/4284206/Arabia-Investments-Nasr-Company-for-Civil-Works-unveil-capital-hike/
  - Nasr Company for Civil Works’ consortium signs EUR 46m agreement with Uganda: https://english.mubasher.info/news/4249759/Nasr-Company-for-Civil-Works-consortium-signs-EUR-46m-agreement-with-Uganda/
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=524 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- PRCL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ceramic and Porcelain summary=Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- ROTO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Rowad Tourism Company summary=Shareholder raises stake in Rowad Tourism; Target raises stake in Rowad Tourism to 10.68%; Rowad Tourism sees EGP 22.4m block trading deal
  - Shareholder raises stake in Rowad Tourism: https://english.mubasher.info/news/4043645/Shareholder-raises-stake-in-Rowad-Tourism/
  - Target raises stake in Rowad Tourism to 10.68%: https://english.mubasher.info/news/4031744/Target-raises-stake-in-Rowad-Tourism-to-10-68-/
  - Rowad Tourism sees EGP 22.4m block trading deal: https://english.mubasher.info/news/4031133/Rowad-Tourism-sees-EGP-22-4m-block-trading-deal/

## Warnings
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence for NCCW.CA matches the company but no source/report date was detected.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for ROTO.CA matches the company but no source/report date was detected.
