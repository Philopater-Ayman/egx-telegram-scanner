# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-26T11:33:43.394624+00:00
Generated Cairo: 2026-10-26 14:33
Run timing: target 08:45 Cairo | generated Cairo 2026-10-26 14:33 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-26 14:30

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 151/186
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, October 26
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 6.67% / above MA50 6.67%
- EGX70 regime: BEARISH / above MA20 0.0% / above MA50 2.86%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=1211748608.0 spike=2.78 score=18.07
- CCAP.CA: liquidity=338327520.0 spike=0.67 score=12.98
- ETEL.CA: liquidity=321714496.0 spike=1.29 score=10.37
- ORAS.CA: liquidity=289957216.0 spike=1.0 score=6.6
- MBSC.CA: liquidity=212184528.0 spike=2.2 score=8.8

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- EOSB.CA: spike=8.07 liquidity=440799.75 outlook=NEUTRAL score=49 buy_ready=False
- MENA.CA: spike=5.52 liquidity=10895552.0 outlook=WEAK_OR_RISKY score=17 buy_ready=False
- EPCO.CA: spike=4.13 liquidity=17077002.0 outlook=WEAK_OR_RISKY score=23 buy_ready=False
- ELNA.CA: spike=3.36 liquidity=1444647.25 outlook=BULLISH_WATCH score=91 buy_ready=False
- RREI.CA: spike=3.18 liquidity=22231056.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=2.44 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #2 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #3 Telecommunications: score=-0.53 5d=-3.98% 20d=-4.22% aboveMA50=0.0%
- #4 Banking & Financials: score=-1.22 5d=-2.45% 20d=-8.54% aboveMA50=0.0%
- #5 Energy & Petrochemicals: score=-2.37 5d=-3.2% 20d=-9.79% aboveMA50=0.0%
- #6 Non-bank Financial Services: score=-3.08 5d=-2.57% 20d=-13.95% aboveMA50=0.0%
- #7 Transportation & Logistics: score=-3.29 5d=-6.42% 20d=-9.61% aboveMA50=0.0%
- #8 Education: score=-3.39 5d=-6.05% 20d=-9.42% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELNA.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- BINV.CA: CONSTRUCTIVE score=67.44 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; weak RSI
- EAST.CA: CONSTRUCTIVE score=61 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA50; sector is not leading
- ABUK.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- AJWA.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- EOSB.CA: NEUTRAL score=49 liquidity=THIN sector=LAGGING risk=liquidity below minimum; close to resistance; sector is not leading
- LCSW.CA: WEAK_OR_RISKY score=31 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; below MA50; sector is not leading
- CPCI.CA: WEAK_OR_RISKY score=30 liquidity=TRADEABLE sector=LAGGING risk=below MA20; overheated RSI; sector is not leading
- ETEL.CA: WEAK_OR_RISKY score=25 liquidity=TRADEABLE sector=NEUTRAL risk=below MA20; below MA50; weak RSI
- KZPC.CA: WEAK_OR_RISKY score=25 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; below MA50; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=-4.2 buy_ready=False sector_rank=18 price=183.73 support=180.66 resistance=204.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3402688.75 spike=0.37
- ABUK.CA: score=17.4 buy_ready=False sector_rank=14 price=88.11 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=62953240.0 spike=0.82
- ACAMD.CA: score=11.4 buy_ready=False sector_rank=18 price=1.89 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=37296036.0 spike=0.82
- ACGC.CA: score=2.07 buy_ready=False sector_rank=10 price=12.06 support=12.35 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=22.39 liquidity=4534267.5 spike=0.44
- ADCI.CA: score=0.27 buy_ready=False sector_rank=18 price=230.43 support=230.0 resistance=288.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=15.31 liquidity=2153150.25 spike=1.36
- ADIB.CA: score=7.51 buy_ready=False sector_rank=4 price=44.51 support=43.16 resistance=51.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=33.89 liquidity=73131664.0 spike=0.97
- ADPC.CA: score=2.19 buy_ready=False sector_rank=18 price=2.67 support=2.53 resistance=3.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=13.48 liquidity=5790743.5 spike=0.57
- AFDI.CA: score=-0.32 buy_ready=False sector_rank=18 price=37.45 support=38.01 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=16.59 liquidity=3275915.25 spike=0.75
- AFMC.CA: score=5.98 buy_ready=False sector_rank=18 price=100.0 support=98.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=8.26 liquidity=9582578.0 spike=0.53
- AJWA.CA: score=17.4 buy_ready=False sector_rank=18 price=194.75 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=61.2 liquidity=10324365.0 spike=0.29
- ALCN.CA: score=2.68 buy_ready=False sector_rank=7 price=30.35 support=29.72 resistance=31.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12295923.0 spike=0.57
- ALUM.CA: score=-1.17 buy_ready=False sector_rank=18 price=16.71 support=16.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=14.12 liquidity=2425093.0 spike=0.65
- AMER.CA: score=7.57 buy_ready=False sector_rank=9 price=3.38 support=3.4 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=26.29 liquidity=34292840.0 spike=0.66
- AMES.CA: score=8.4 buy_ready=False sector_rank=18 price=28.8 support=29.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=5.17 liquidity=27372844.0 spike=0.46
- AMIA.CA: score=7.4 buy_ready=False sector_rank=18 price=15.69 support=15.33 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=26.66 liquidity=13520999.0 spike=0.81
- AMOC.CA: score=13.05 buy_ready=False sector_rank=5 price=12.82 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=36.96 liquidity=72215952.0 spike=0.57
- APSW.CA: score=-1.47 buy_ready=False sector_rank=18 price=7.11 support=7.4 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=31.35 liquidity=926279.38 spike=1.6
- ARAB.CA: score=11.57 buy_ready=False sector_rank=9 price=0.22 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=54666576.0 spike=0.5
- ARCC.CA: score=7.4 buy_ready=False sector_rank=16 price=60.06 support=58.12 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=20.33 liquidity=29826158.0 spike=0.68
- AREH.CA: score=3.17 buy_ready=False sector_rank=18 price=0.93 support=0.94 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=12.24 liquidity=6772309.5 spike=0.83
- ASCM.CA: score=2.14 buy_ready=False sector_rank=18 price=39.4 support=40.0 resistance=60.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=13.89 liquidity=5744820.0 spike=0.65
- ASPI.CA: score=6.4 buy_ready=False sector_rank=18 price=0.28 support=0.27 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=17.96 liquidity=12096565.0 spike=0.63
- ATLC.CA: score=2.16 buy_ready=False sector_rank=6 price=4.45 support=3.93 resistance=4.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8953062.0 spike=1.22
- ATQA.CA: score=6.4 buy_ready=False sector_rank=14 price=8.75 support=8.43 resistance=12.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=23.27 liquidity=26057110.0 spike=0.47
- AXPH.CA: score=0.03 buy_ready=False sector_rank=18 price=1168.9 support=1135.0 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=12.16 liquidity=2628542.5 spike=0.45
- BINV.CA: score=18.94 buy_ready=False sector_rank=1 price=55.78 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=31.27 liquidity=32293802.0 spike=2.48
- BIOC.CA: score=7.4 buy_ready=False sector_rank=18 price=225.01 support=213.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=12.31 liquidity=36751564.0 spike=0.34
- BTFH.CA: score=7.59 buy_ready=False sector_rank=6 price=2.13 support=2.05 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=17.86 liquidity=139646832.0 spike=1.41
- CAED.CA: score=-0.18 buy_ready=False sector_rank=18 price=67.21 support=64.0 resistance=72.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7416219.0 spike=0.9
- CANA.CA: score=7.79 buy_ready=False sector_rank=4 price=41.21 support=38.1 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=32.46 liquidity=9278374.0 spike=0.52
- CCAP.CA: score=12.98 buy_ready=False sector_rank=1 price=5.91 support=5.87 resistance=7.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=33.15 liquidity=338327520.0 spike=0.67
- CCRS.CA: score=0.27 buy_ready=False sector_rank=18 price=1.46 support=1.3 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7588789.0 spike=1.14
- CEFM.CA: score=-3.27 buy_ready=False sector_rank=18 price=107.69 support=103.05 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=18.03 liquidity=331590.72 spike=0.16
- CERA.CA: score=6.4 buy_ready=False sector_rank=18 price=0.98 support=1.01 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=18.57 liquidity=82799328.0 spike=0.68
- CFGH.CA: score=-0.25 buy_ready=False sector_rank=18 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=10.0 liquidity=14790.66 spike=2.67
- CICH.CA: score=-2.89 buy_ready=False sector_rank=6 price=10.08 support=9.63 resistance=12.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=17.01 liquidity=340439.91 spike=0.15
- CIEB.CA: score=6.59 buy_ready=False sector_rank=4 price=21.47 support=21.4 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=8975124.0 spike=1.05
- CIRA.CA: score=7.64 buy_ready=False sector_rank=8 price=32.85 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=25.39 liquidity=10381162.0 spike=0.61
- CLHO.CA: score=6.4 buy_ready=False sector_rank=12 price=12.77 support=12.71 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=3.95 liquidity=12787185.0 spike=0.35
- CNFN.CA: score=0.94 buy_ready=False sector_rank=6 price=3.46 support=3.5 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=4169273.25 spike=0.44
- COMI.CA: score=18.07 buy_ready=False sector_rank=4 price=119.98 support=120.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=38.2 liquidity=1211748608.0 spike=2.78
- COPR.CA: score=5.03 buy_ready=False sector_rank=18 price=0.36 support=0.33 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=9.29 liquidity=8633700.0 spike=0.52
- COSG.CA: score=2.97 buy_ready=False sector_rank=18 price=1.14 support=1.11 resistance=1.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=16.22 liquidity=6571940.5 spike=0.57
- CPCI.CA: score=13.08 buy_ready=False sector_rank=18 price=587.0 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=36.68 liquidity=6942991.0 spike=1.37
- CSAG.CA: score=3.87 buy_ready=False sector_rank=7 price=30.63 support=30.1 resistance=38.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=18.45 liquidity=7128780.0 spike=1.03
- DAPH.CA: score=6.4 buy_ready=False sector_rank=18 price=68.5 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=24.85 liquidity=20508648.0 spike=0.49
- DEIN.CA: score=5.4 buy_ready=False sector_rank=18 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=-0.99 buy_ready=False sector_rank=13 price=20.86 support=20.27 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=7.97 liquidity=2608406.5 spike=0.75
- DSCW.CA: score=6.4 buy_ready=False sector_rank=18 price=1.34 support=1.23 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=10540425.0 spike=0.66
- DTPP.CA: score=2.4 buy_ready=False sector_rank=18 price=38.87 support=36.0 resistance=41.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16796112.0 spike=0.4
- EALR.CA: score=-1.91 buy_ready=False sector_rank=18 price=242.6 support=240.0 resistance=362.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=10.26 liquidity=1692360.38 spike=0.5
- EASB.CA: score=-0.01 buy_ready=False sector_rank=18 price=5.37 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=24.69 liquidity=3591248.0 spike=0.74
- EAST.CA: score=16.92 buy_ready=False sector_rank=13 price=30.24 support=27.01 resistance=31.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=77052880.0 spike=1.76
- EBSC.CA: score=-2.53 buy_ready=False sector_rank=18 price=1.27 support=1.25 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=1065006.5 spike=0.51
- ECAP.CA: score=-2.89 buy_ready=False sector_rank=18 price=25.26 support=25.0 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=16.05 liquidity=711751.06 spike=0.2
- EDFM.CA: score=-7.09 buy_ready=False sector_rank=18 price=356.74 support=350.0 resistance=370.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=514989.16 spike=0.46
- EEII.CA: score=-1.25 buy_ready=False sector_rank=18 price=1.49 support=1.5 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=9.76 liquidity=2354411.25 spike=0.35
- EFIC.CA: score=6.4 buy_ready=False sector_rank=14 price=130.09 support=121.0 resistance=179.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=18.7 liquidity=12150157.0 spike=0.43
- EFID.CA: score=8.4 buy_ready=False sector_rank=13 price=17.07 support=16.3 resistance=20.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=35932028.0 spike=0.87
- EFIH.CA: score=6.4 buy_ready=False sector_rank=11 price=21.0 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=32.51 liquidity=47659872.0 spike=0.73
- EGAL.CA: score=6.4 buy_ready=False sector_rank=14 price=289.43 support=275.0 resistance=362.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=22.91 liquidity=58403596.0 spike=0.64
- EGAS.CA: score=1.06 buy_ready=False sector_rank=5 price=43.4 support=43.55 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=18.9 liquidity=4012725.0 spike=0.58
- EGBE.CA: score=-1.4 buy_ready=False sector_rank=4 price=0.47 support=0.48 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=22.89 liquidity=90966.11 spike=0.88
- EGCH.CA: score=6.4 buy_ready=False sector_rank=14 price=10.27 support=10.0 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=18.75 liquidity=35696852.0 spike=0.55
- EGSA.CA: score=7.3 buy_ready=False sector_rank=3 price=8.81 support=8.75 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:15 AM market time freshness=DELAYED_CURRENT RSI=66.07 liquidity=7998.91 spike=1.25
- EGTS.CA: score=8.03 buy_ready=False sector_rank=9 price=10.44 support=10.71 resistance=19.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=10.73 liquidity=37033920.0 spike=1.73
- EHDR.CA: score=4.53 buy_ready=False sector_rank=18 price=1.84 support=1.8 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=17.95 liquidity=8127833.5 spike=0.8
- ELEC.CA: score=6.4 buy_ready=False sector_rank=15 price=1.39 support=1.36 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=44259412.0 spike=0.88
- ELKA.CA: score=6.4 buy_ready=False sector_rank=18 price=1.27 support=1.23 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=21.62 liquidity=12107931.0 spike=0.96
- ELNA.CA: score=16.56 buy_ready=False sector_rank=18 price=36.92 support=33.46 resistance=38.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1444647.25 spike=3.36
- ELSH.CA: score=3.29 buy_ready=False sector_rank=18 price=8.87 support=8.6 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=6891689.5 spike=0.34
- ELWA.CA: score=8.4 buy_ready=False sector_rank=18 price=1.65 support=1.43 resistance=1.67 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=782.1 spike=0.0
- EMFD.CA: score=2.57 buy_ready=False sector_rank=9 price=11.11 support=11.01 resistance=11.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21150434.0 spike=0.36
- ENGC.CA: score=3.36 buy_ready=False sector_rank=18 price=28.23 support=28.12 resistance=41.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=14.83 liquidity=6955957.5 spike=0.64
- EOSB.CA: score=16.84 buy_ready=False sector_rank=18 price=1.61 support=1.57 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=440799.75 spike=8.07
- EPCO.CA: score=11.4 buy_ready=False sector_rank=18 price=7.21 support=7.0 resistance=11.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=17.88 liquidity=17077002.0 spike=4.13
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=18 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=10.37 buy_ready=False sector_rank=3 price=119.02 support=121.01 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=19.29 liquidity=321714496.0 spike=1.29
- ETRS.CA: score=5.06 buy_ready=False sector_rank=18 price=10.18 support=9.63 resistance=10.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24322076.0 spike=2.33
- EXPA.CA: score=7.51 buy_ready=False sector_rank=4 price=12.99 support=12.0 resistance=22.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=14.73 liquidity=28381476.0 spike=0.75
- FAIT.CA: score=-3.62 buy_ready=False sector_rank=4 price=43.0 support=40.6 resistance=43.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2868511.75 spike=0.98
- FAITA.CA: score=3.69 buy_ready=False sector_rank=4 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=47.41 liquidity=56268.66 spike=1.56
- FERC.CA: score=-0.63 buy_ready=False sector_rank=14 price=55.44 support=53.57 resistance=77.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=12.85 liquidity=2971692.5 spike=0.9
- FWRY.CA: score=6.4 buy_ready=False sector_rank=11 price=17.2 support=16.45 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=28.5 liquidity=98065504.0 spike=0.89
- GBCO.CA: score=6.4 buy_ready=False sector_rank=21 price=22.62 support=22.02 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=12.34 liquidity=57885952.0 spike=0.49
- GDWA.CA: score=6.72 buy_ready=False sector_rank=18 price=0.5 support=0.49 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=16.01 liquidity=16835992.0 spike=1.16
- GGCC.CA: score=3.2 buy_ready=False sector_rank=18 price=0.5 support=0.5 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=21.05 liquidity=6801684.0 spike=0.43
- GIHD.CA: score=1.77 buy_ready=False sector_rank=18 price=33.71 support=32.1 resistance=36.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9368042.0 spike=0.64
- GMCI.CA: score=-1.56 buy_ready=False sector_rank=18 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=34.62 liquidity=39066.72 spike=0.12
- GRCA.CA: score=-3.92 buy_ready=False sector_rank=18 price=23.93 support=22.57 resistance=26.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3683414.0 spike=0.71
- GSSC.CA: score=-2.73 buy_ready=False sector_rank=18 price=231.22 support=222.22 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=25.72 liquidity=872061.31 spike=0.71
- HDBK.CA: score=4.15 buy_ready=False sector_rank=4 price=93.25 support=92.52 resistance=97.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27632270.0 spike=1.32
- HELI.CA: score=6.57 buy_ready=False sector_rank=9 price=6.01 support=5.96 resistance=7.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=55193724.0 spike=0.82
- HRHO.CA: score=11.77 buy_ready=False sector_rank=6 price=23.1 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=35.07 liquidity=62174060.0 spike=0.49
- ICID.CA: score=-3.26 buy_ready=False sector_rank=18 price=14.89 support=14.52 resistance=16.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4339866.0 spike=0.61
- IDRE.CA: score=-3.3 buy_ready=False sector_rank=18 price=29.74 support=29.5 resistance=32.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4300991.5 spike=0.75
- IFAP.CA: score=1.09 buy_ready=False sector_rank=19 price=16.47 support=15.51 resistance=20.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=10.73 liquidity=4694578.0 spike=0.89
- INFI.CA: score=4.88 buy_ready=False sector_rank=18 price=98.26 support=99.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=33.57 liquidity=8480745.0 spike=0.42
- IRON.CA: score=8.5 buy_ready=False sector_rank=14 price=23.97 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=37.35 liquidity=7099748.5 spike=0.66
- ISMA.CA: score=5.12 buy_ready=False sector_rank=18 price=16.04 support=16.3 resistance=29.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=15.24 liquidity=8316128.5 spike=1.2
- ISMQ.CA: score=6.4 buy_ready=False sector_rank=14 price=6.16 support=6.0 resistance=8.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=17.7 liquidity=10580139.0 spike=0.6
- ISPH.CA: score=6.4 buy_ready=False sector_rank=12 price=9.45 support=9.14 resistance=12.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=9.99 liquidity=34614620.0 spike=0.75
- JUFO.CA: score=5.22 buy_ready=False sector_rank=13 price=21.86 support=21.01 resistance=26.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=21.97 liquidity=8824731.0 spike=0.53
- KABO.CA: score=8.2 buy_ready=False sector_rank=10 price=6.05 support=6.02 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=23.67 liquidity=38423572.0 spike=1.83
- KWIN.CA: score=-4.5 buy_ready=False sector_rank=18 price=46.18 support=44.02 resistance=54.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3097684.75 spike=0.61
- KZPC.CA: score=6.33 buy_ready=False sector_rank=18 price=11.8 support=12.0 resistance=14.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=40.57 liquidity=3927692.25 spike=0.51
- LCSW.CA: score=8.89 buy_ready=False sector_rank=16 price=30.41 support=28.0 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=6490525.5 spike=0.32
- LUTS.CA: score=6.4 buy_ready=False sector_rank=18 price=0.51 support=0.51 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=8.3 liquidity=47664944.0 spike=0.86
- MAAL.CA: score=4.51 buy_ready=False sector_rank=18 price=5.26 support=5.26 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=9.88 liquidity=8107510.0 spike=0.45
- MASR.CA: score=6.66 buy_ready=False sector_rank=18 price=6.09 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=21.58 liquidity=55440556.0 spike=1.13
- MBSC.CA: score=8.8 buy_ready=False sector_rank=16 price=275.02 support=262.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=31.1 liquidity=212184528.0 spike=2.2
- MCQE.CA: score=8.5 buy_ready=False sector_rank=16 price=145.0 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=11.65 liquidity=132847920.0 spike=2.05
- MCRO.CA: score=2.4 buy_ready=False sector_rank=18 price=1.16 support=1.09 resistance=1.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37321388.0 spike=0.82
- MENA.CA: score=11.57 buy_ready=False sector_rank=9 price=5.64 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=34.16 liquidity=10895552.0 spike=5.52
- MEPA.CA: score=8.1 buy_ready=False sector_rank=18 price=1.17 support=1.2 resistance=1.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=16.85 liquidity=12386744.0 spike=1.85
- MFPC.CA: score=2.4 buy_ready=False sector_rank=14 price=44.77 support=44.01 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46831752.0 spike=0.95
- MFSC.CA: score=-5.34 buy_ready=False sector_rank=18 price=29.56 support=28.55 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2263751.75 spike=0.97
- MHOT.CA: score=1.44 buy_ready=False sector_rank=20 price=13.51 support=13.0 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=16.71 liquidity=5044741.0 spike=0.34
- MICH.CA: score=9.04 buy_ready=False sector_rank=18 price=38.82 support=35.5 resistance=45.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=35.66 liquidity=6640851.0 spike=0.83
- MILS.CA: score=4.83 buy_ready=False sector_rank=18 price=101.81 support=106.4 resistance=201.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=8.96 liquidity=8290558.5 spike=1.07
- MIPH.CA: score=-0.41 buy_ready=False sector_rank=12 price=740.33 support=675.0 resistance=759.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6065080.0 spike=1.56
- MOED.CA: score=2.4 buy_ready=False sector_rank=18 price=0.39 support=0.39 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12075486.0 spike=0.94
- MOIL.CA: score=-1.24 buy_ready=False sector_rank=5 price=0.62 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=23.77 liquidity=250681.45 spike=1.23
- MOIN.CA: score=-0.69 buy_ready=False sector_rank=18 price=25.78 support=25.88 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=19.06 liquidity=2905246.0 spike=0.3
- MOSC.CA: score=-6.11 buy_ready=False sector_rank=18 price=211.23 support=198.01 resistance=237.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1485440.38 spike=0.44
- MPCI.CA: score=7.4 buy_ready=False sector_rank=18 price=250.75 support=239.0 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=10.7 liquidity=85461352.0 spike=0.88
- MPCO.CA: score=6.4 buy_ready=False sector_rank=19 price=1.7 support=1.55 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=18.4 liquidity=81271776.0 spike=0.85
- MPRC.CA: score=7.44 buy_ready=False sector_rank=18 price=27.2 support=27.1 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=9.71 liquidity=24424934.0 spike=1.52
- MTIE.CA: score=6.4 buy_ready=False sector_rank=21 price=6.51 support=6.11 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=18.63 liquidity=19642648.0 spike=1.0
- NAHO.CA: score=-4.54 buy_ready=False sector_rank=18 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38930.57 spike=2.51
- NCCW.CA: score=6.4 buy_ready=False sector_rank=18 price=4.23 support=4.21 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=8.4 liquidity=11335456.0 spike=0.45
- NEDA.CA: score=-0.57 buy_ready=False sector_rank=18 price=2.6 support=2.47 resistance=2.74 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=25040.6 spike=0.11
- NHPS.CA: score=0.18 buy_ready=False sector_rank=18 price=50.6 support=50.06 resistance=79.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=7.11 liquidity=3777863.5 spike=0.43
- NINH.CA: score=1.45 buy_ready=False sector_rank=18 price=12.8 support=12.36 resistance=20.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=5.04 liquidity=5047925.5 spike=0.49
- NIPH.CA: score=7.4 buy_ready=False sector_rank=12 price=222.96 support=220.0 resistance=341.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=24.02 liquidity=109663696.0 spike=0.93
- OBRI.CA: score=5.59 buy_ready=False sector_rank=18 price=19.08 support=19.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=18.63 liquidity=9194781.0 spike=0.63
- OCDI.CA: score=2.87 buy_ready=False sector_rank=9 price=21.95 support=21.35 resistance=23.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41351632.0 spike=1.15
- OCPH.CA: score=-1.08 buy_ready=False sector_rank=18 price=150.89 support=147.96 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=4.7 liquidity=2520311.75 spike=0.85
- ODIN.CA: score=2.54 buy_ready=False sector_rank=18 price=1.79 support=1.8 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=17.74 liquidity=6097617.5 spike=1.02
- OFH.CA: score=6.4 buy_ready=False sector_rank=18 price=0.63 support=0.63 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=12.73 liquidity=12078962.0 spike=0.27
- OIH.CA: score=7.98 buy_ready=False sector_rank=1 price=1.53 support=1.5 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55641952.0 spike=0.96
- OLFI.CA: score=6.54 buy_ready=False sector_rank=13 price=19.0 support=18.02 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=16.32 liquidity=15890474.0 spike=1.07
- ORAS.CA: score=6.6 buy_ready=False sector_rank=2 price=790.81 support=772.0 resistance=819.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=289957216.0 spike=1.0
- ORHD.CA: score=8.57 buy_ready=False sector_rank=9 price=9.2 support=8.5 resistance=41.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=14.58 liquidity=90911096.0 spike=0.76
- ORWE.CA: score=6.54 buy_ready=False sector_rank=10 price=22.96 support=23.31 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=22.42 liquidity=32466498.0 spike=0.83
- PHAR.CA: score=6.4 buy_ready=False sector_rank=12 price=92.58 support=91.61 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=16.55 liquidity=55383156.0 spike=0.93
- PHDC.CA: score=2.57 buy_ready=False sector_rank=9 price=11.28 support=11.0 resistance=11.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47145196.0 spike=0.47
- PHTV.CA: score=-0.96 buy_ready=False sector_rank=18 price=309.8 support=305.0 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=31.97 liquidity=1199098.88 spike=1.22
- POUL.CA: score=13.4 buy_ready=False sector_rank=13 price=9.1 support=8.85 resistance=38.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=35.66 liquidity=51609552.0 spike=0.9
- PRCL.CA: score=3.38 buy_ready=False sector_rank=16 price=17.38 support=17.25 resistance=31.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=22.18 liquidity=6978017.0 spike=0.7
- PRDC.CA: score=6.57 buy_ready=False sector_rank=9 price=5.6 support=5.45 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=17.87 liquidity=14488823.0 spike=0.41
- PRMH.CA: score=-2.37 buy_ready=False sector_rank=18 price=1.74 support=1.7 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=1230715.75 spike=0.4
- RACC.CA: score=7.25 buy_ready=False sector_rank=18 price=7.0 support=7.13 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=22.98 liquidity=9865812.0 spike=1.49
- RAKT.CA: score=9.48 buy_ready=False sector_rank=18 price=23.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-24T21:00:00+00:00 freshness=FRESH RSI=63.62 liquidity=79464.76 spike=0.2
- RAYA.CA: score=6.4 buy_ready=False sector_rank=17 price=5.2 support=5.02 resistance=7.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=15.84 liquidity=13936746.0 spike=0.48
- RMDA.CA: score=6.84 buy_ready=False sector_rank=12 price=4.74 support=4.52 resistance=5.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=24.43 liquidity=31073080.0 spike=1.22
- ROTO.CA: score=2.24 buy_ready=False sector_rank=18 price=27.99 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=15.08 liquidity=5844038.0 spike=0.65
- RREI.CA: score=6.76 buy_ready=False sector_rank=18 price=2.18 support=1.96 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22231056.0 spike=3.18
- RTVC.CA: score=-2.44 buy_ready=False sector_rank=18 price=2.89 support=3.04 resistance=3.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=1163231.75 spike=0.45
- RUBX.CA: score=2.4 buy_ready=False sector_rank=18 price=11.45 support=10.51 resistance=13.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81094624.0 spike=0.99
- SAUD.CA: score=4.39 buy_ready=False sector_rank=4 price=19.81 support=20.0 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=18.94 liquidity=6873736.0 spike=0.57
- SCEM.CA: score=7.4 buy_ready=False sector_rank=16 price=74.76 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=32.38 liquidity=18944646.0 spike=0.31
- SCFM.CA: score=-2.76 buy_ready=False sector_rank=18 price=164.42 support=153.02 resistance=189.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3182146.75 spike=1.83
- SCTS.CA: score=4.05 buy_ready=False sector_rank=8 price=470.45 support=437.0 resistance=499.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7667629.5 spike=2.87
- SDTI.CA: score=2.4 buy_ready=False sector_rank=18 price=76.56 support=75.36 resistance=81.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11519422.0 spike=0.4
- SEIG.CA: score=-2.32 buy_ready=False sector_rank=18 price=149.79 support=142.0 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=13.0 liquidity=1276184.25 spike=0.61
- SIPC.CA: score=11.4 buy_ready=False sector_rank=18 price=3.92 support=4.04 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=38.85 liquidity=23450960.0 spike=0.41
- SKPC.CA: score=6.4 buy_ready=False sector_rank=14 price=14.11 support=14.15 resistance=17.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=27.74 liquidity=28272256.0 spike=0.43
- SMFR.CA: score=-2.5 buy_ready=False sector_rank=18 price=166.9 support=173.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=21.79 liquidity=1098505.38 spike=0.36
- SNFC.CA: score=-0.29 buy_ready=False sector_rank=18 price=10.27 support=10.3 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=29.81 liquidity=3310048.5 spike=0.41
- SPIN.CA: score=-0.11 buy_ready=False sector_rank=10 price=12.48 support=12.0 resistance=13.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6776521.0 spike=1.29
- SPMD.CA: score=1.62 buy_ready=False sector_rank=18 price=0.3 support=0.31 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=5215400.0 spike=0.45
- SUGR.CA: score=7.82 buy_ready=False sector_rank=13 price=49.77 support=50.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=41.55 liquidity=6424334.5 spike=0.71
- SVCE.CA: score=6.4 buy_ready=False sector_rank=18 price=7.83 support=7.01 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=10.45 liquidity=48229288.0 spike=0.69
- SWDY.CA: score=7.74 buy_ready=False sector_rank=15 price=102.16 support=97.0 resistance=124.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=24.23 liquidity=70768760.0 spike=1.17
- TALM.CA: score=7.64 buy_ready=False sector_rank=8 price=18.01 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=19.7 liquidity=14665226.0 spike=0.52
- TMGH.CA: score=13.57 buy_ready=False sector_rank=9 price=82.07 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=36.53 liquidity=188702592.0 spike=0.73
- TRTO.CA: score=2.79 buy_ready=False sector_rank=18 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=65.22 liquidity=14138.36 spike=2.19
- UEFM.CA: score=-2.87 buy_ready=False sector_rank=18 price=432.48 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=23.14 liquidity=725379.0 spike=0.25
- UEGC.CA: score=6.4 buy_ready=False sector_rank=18 price=1.3 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=30.93 liquidity=35501648.0 spike=0.79
- UNIP.CA: score=4.07 buy_ready=False sector_rank=18 price=0.27 support=0.26 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=19.53 liquidity=7668452.5 spike=0.95
- UNIT.CA: score=-0.71 buy_ready=False sector_rank=9 price=16.0 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=1717337.0 spike=0.45
- WCDF.CA: score=-2.91 buy_ready=False sector_rank=18 price=468.8 support=432.5 resistance=686.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=14.36 liquidity=694507.13 spike=0.27
- WKOL.CA: score=-1.13 buy_ready=False sector_rank=18 price=218.33 support=218.0 resistance=249.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6467603.0 spike=0.88
- ZEOT.CA: score=1.63 buy_ready=False sector_rank=18 price=9.11 support=9.01 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=5227432.5 spike=0.66
- ZMID.CA: score=6.57 buy_ready=False sector_rank=9 price=6.15 support=6.01 resistance=8.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=16.6 liquidity=64632452.0 spike=0.88

## Backtesting Lite
- BINV.CA: 180d return=33.37%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-10-24T21:00:00+00:00
- COMI.CA: 180d return=-2.24%, max drawdown=-18.04%, MA20>MA50 days last20=0, as_of=2026-10-24T21:00:00+00:00
- ABUK.CA: 180d return=55.92%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-24T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- EOSB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Orouba Securities Brokerage summary=El Orouba Brokerage turns profitable in Q4; El Orouba Securities suffers 598,000 losses in Q3; El Orouba Securities H1 losses down 7%
  - El Orouba Brokerage turns profitable in Q4: https://english.mubasher.info/news/3067539/El-Orouba-Brokerage-turns-profitable-in-Q4/
  - El Orouba Securities suffers 598,000 losses in Q3: https://english.mubasher.info/news/3016624/El-Orouba-Securities-suffers-598-000-losses-in-Q3/
  - El Orouba Securities H1 losses down 7%: https://english.mubasher.info/news/2984110/El-Orouba-Securities-H1-losses-down-7-/
- ELNA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Manufacturing Agricultural Crops S.A.E summary=Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops; El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m; EGX halts trading on El Nasr for Manufacturing Agricultural Crops
  - Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops: https://english.mubasher.info/news/3749421/Consortium-offers-to-acquire-controlling-stake-in-El-Nasr-for-Agricultural-Crops/
  - El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m: https://english.mubasher.info/news/3685533/El-Nasr-for-Agricultural-Crops-to-sell-Sohag-factory-land-for-EGP-650m/
  - EGX halts trading on El Nasr for Manufacturing Agricultural Crops: https://english.mubasher.info/news/3489525/EGX-halts-trading-on-El-Nasr-for-Manufacturing-Agricultural-Crops/
- TMGH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talaat Moustafa Group Holding summary=Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.

## Warnings
- OpenRouter API error: 404
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence for EOSB.CA matches the company but no source/report date was detected.
- Evidence for ELNA.CA matches the company but no source/report date was detected.
- Evidence rejected for TMGH.CA: source text did not clearly match TMGH.CA / Talaat Moustafa Group Holding.
