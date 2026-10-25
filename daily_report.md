# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-25T10:10:26.623699+00:00
Generated Cairo: 2026-10-25 13:10
Run timing: target 08:45 Cairo | generated Cairo 2026-10-25 13:10 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-25 13:07

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 82/187
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, October 25
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.88% / above MA50 11.76%
- EGX70 regime: BEARISH / above MA20 0.0% / above MA50 12.5%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=276071680.0 spike=0.52 score=8.66
- ETEL.CA: liquidity=188438192.0 spike=0.79 score=8.82
- GTWL.CA: liquidity=156825024.0 spike=0.94 score=4.42
- COMI.CA: liquidity=115822392.0 spike=0.26 score=14.78
- GBCO.CA: liquidity=112262080.0 spike=1.0 score=3.63

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- EOSB.CA: spike=12.38 liquidity=443093.56 outlook=CONSTRUCTIVE score=61.06 buy_ready=False
- SCTS.CA: spike=7.3 liquidity=14325148.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELNA.CA: spike=4.69 liquidity=1301285.25 outlook=BULLISH_WATCH score=90.06 buy_ready=False
- CPCI.CA: spike=1.57 liquidity=7286898.5 outlook=BULLISH_WATCH score=70.06 buy_ready=False
- EBSC.CA: spike=1.32 liquidity=2702072.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=4.55 5d=1.25% 20d=0.17% aboveMA50=50.0%
- #2 Basic Resources & Chemicals: score=1.86 5d=0.0% 20d=0.0% aboveMA50=20.0%
- #3 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #4 General / Verified EGX Expansion: score=1.06 5d=0.0% 20d=0.0% aboveMA50=5.88%
- #5 Transportation & Logistics: score=0.81 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Technology & Distribution: score=0.73 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Education: score=0.66 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Real Estate: score=0.66 5d=0.0% 20d=0.0% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELNA.CA: BULLISH_WATCH score=90.06 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ABUK.CA: BULLISH_WATCH score=87.86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CPCI.CA: BULLISH_WATCH score=70.06 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20
- MFPC.CA: CONSTRUCTIVE score=69.86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- SDTI.CA: CONSTRUCTIVE score=64.06 liquidity=TRADEABLE sector=IMPROVING risk=below MA20
- EOSB.CA: CONSTRUCTIVE score=61.06 liquidity=THIN sector=IMPROVING risk=liquidity below minimum
- AMOC.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- AJWA.CA: NEUTRAL score=45.06 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; overheated RSI; far above support
- EGSA.CA: NEUTRAL score=43.55 liquidity=THIN sector=LEADING risk=liquidity below minimum; liquidity is cooling; momentum is extended; close to resistance
- ETRS.CA: NEUTRAL score=42.06 liquidity=TRADEABLE sector=IMPROVING risk=below MA20; below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=3.15 buy_ready=False sector_rank=4 price=214.65 support=201.0 resistance=293.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=31.19 liquidity=4722608.5 spike=0.49
- ABUK.CA: score=23.74 buy_ready=False sector_rank=2 price=89.0 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=58.15 liquidity=46958004.0 spike=0.61
- ACAMD.CA: score=15.42 buy_ready=False sector_rank=4 price=1.98 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=48.84 liquidity=19414572.0 spike=0.41
- ACGC.CA: score=0.63 buy_ready=False sector_rank=19 price=12.51 support=12.5 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=2875062.25 spike=0.25
- ADCI.CA: score=-4.75 buy_ready=False sector_rank=4 price=238.06 support=235.4 resistance=254.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=827007.69 spike=0.52
- ADIB.CA: score=7.78 buy_ready=False sector_rank=11 price=44.01 support=43.45 resistance=51.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=62620976.0 spike=0.86
- ADPC.CA: score=4.66 buy_ready=False sector_rank=4 price=2.63 support=2.61 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12007608.0 spike=1.12
- AFDI.CA: score=-3.46 buy_ready=False sector_rank=4 price=39.64 support=39.05 resistance=43.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2111609.25 spike=0.47
- AFMC.CA: score=-1.57 buy_ready=False sector_rank=4 price=106.51 support=105.0 resistance=116.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4002277.0 spike=0.22
- AJWA.CA: score=19.42 buy_ready=False sector_rank=4 price=213.55 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=71.97 liquidity=20392022.0 spike=0.58
- ALCN.CA: score=2.12 buy_ready=False sector_rank=5 price=30.9 support=30.87 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7800817.0 spike=0.35
- ALUM.CA: score=-2.67 buy_ready=False sector_rank=4 price=18.5 support=18.39 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2907086.25 spike=0.75
- AMER.CA: score=4.26 buy_ready=False sector_rank=8 price=3.76 support=3.74 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20447824.0 spike=0.39
- AMES.CA: score=4.42 buy_ready=False sector_rank=4 price=30.78 support=30.56 resistance=33.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17624844.0 spike=0.29
- AMIA.CA: score=9.79 buy_ready=False sector_rank=4 price=16.95 support=17.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=5361062.0 spike=0.32
- AMOC.CA: score=16.76 buy_ready=False sector_rank=12 price=13.03 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=67559456.0 spike=0.53
- APSW.CA: score=3.77 buy_ready=False sector_rank=4 price=7.78 support=7.61 resistance=8.92 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=36.02 liquidity=343409.21 spike=0.59
- ARAB.CA: score=4.26 buy_ready=False sector_rank=8 price=0.23 support=0.23 resistance=0.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44658824.0 spike=0.41
- ARCC.CA: score=4.22 buy_ready=False sector_rank=9 price=60.31 support=60.11 resistance=65.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19356930.0 spike=0.44
- AREH.CA: score=-0.04 buy_ready=False sector_rank=4 price=1.02 support=1.02 resistance=1.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5538201.0 spike=0.69
- ASCM.CA: score=0.25 buy_ready=False sector_rank=4 price=41.96 support=41.5 resistance=46.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5821670.0 spike=0.62
- ASPI.CA: score=4.71 buy_ready=False sector_rank=4 price=0.3 support=0.3 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=28.87 liquidity=6290103.5 spike=0.31
- ATLC.CA: score=1.46 buy_ready=False sector_rank=10 price=4.61 support=4.65 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=30.61 liquidity=3363202.25 spike=0.44
- ATQA.CA: score=6.74 buy_ready=False sector_rank=2 price=9.27 support=9.23 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20346340.0 spike=0.36
- AXPH.CA: score=4.37 buy_ready=False sector_rank=4 price=1204.08 support=1200.12 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=20.51 liquidity=4949542.5 spike=0.81
- BINV.CA: score=9.39 buy_ready=False sector_rank=13 price=57.41 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=2729844.0 spike=0.19
- BIOC.CA: score=4.42 buy_ready=False sector_rank=4 price=238.01 support=236.0 resistance=261.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15813783.0 spike=0.15
- BTFH.CA: score=4.1 buy_ready=False sector_rank=10 price=2.38 support=2.37 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=82509360.0 spike=0.85
- CAED.CA: score=-0.42 buy_ready=False sector_rank=4 price=77.2 support=76.5 resistance=85.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5159285.0 spike=0.62
- CANA.CA: score=8.14 buy_ready=False sector_rank=11 price=40.77 support=38.1 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=4360514.5 spike=0.24
- CCAP.CA: score=8.66 buy_ready=False sector_rank=13 price=6.21 support=5.87 resistance=7.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=276071680.0 spike=0.52
- CCRS.CA: score=-2.91 buy_ready=False sector_rank=4 price=1.7 support=1.66 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2663741.0 spike=0.39
- CEFM.CA: score=-4.99 buy_ready=False sector_rank=4 price=119.64 support=115.04 resistance=125.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=586343.13 spike=0.28
- CERA.CA: score=4.42 buy_ready=False sector_rank=4 price=1.04 support=1.04 resistance=1.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70787744.0 spike=0.57
- CFGH.CA: score=-1.57 buy_ready=False sector_rank=4 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=16.67 liquidity=1202.89 spike=0.24
- CICH.CA: score=4.84 buy_ready=False sector_rank=10 price=10.34 support=9.63 resistance=12.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=35.82 liquidity=1735240.88 spike=0.75
- CIEB.CA: score=5.31 buy_ready=False sector_rank=11 price=22.11 support=21.4 resistance=24.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=40.12 liquidity=2530843.0 spike=0.28
- CIRA.CA: score=1.27 buy_ready=False sector_rank=7 price=33.65 support=33.35 resistance=36.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7003237.5 spike=0.4
- CLHO.CA: score=6.9 buy_ready=False sector_rank=17 price=13.04 support=13.0 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=15.19 liquidity=18315682.0 spike=0.5
- CNFN.CA: score=-1.5 buy_ready=False sector_rank=10 price=3.8 support=3.79 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4402386.5 spike=0.46
- COMI.CA: score=14.78 buy_ready=False sector_rank=11 price=122.77 support=120.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=43.17 liquidity=115822392.0 spike=0.26
- COPR.CA: score=2.97 buy_ready=False sector_rank=4 price=0.37 support=0.36 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8550802.0 spike=0.5
- COSG.CA: score=1.62 buy_ready=False sector_rank=4 price=1.25 support=1.24 resistance=1.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7198728.5 spike=0.6
- CPCI.CA: score=15.85 buy_ready=False sector_rank=4 price=579.4 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=7286898.5 spike=1.57
- CSAG.CA: score=-0.75 buy_ready=False sector_rank=5 price=32.87 support=32.7 resistance=34.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4923606.0 spike=0.73
- DAPH.CA: score=4.42 buy_ready=False sector_rank=4 price=72.8 support=72.14 resistance=80.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12452436.0 spike=0.29
- DEIN.CA: score=7.42 buy_ready=False sector_rank=4 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=0.31 buy_ready=False sector_rank=18 price=21.67 support=22.1 resistance=26.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=19.25 liquidity=1452255.0 spike=0.41
- DSCW.CA: score=2.25 buy_ready=False sector_rank=4 price=1.4 support=1.39 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7830716.0 spike=0.48
- DTPP.CA: score=4.42 buy_ready=False sector_rank=4 price=44.82 support=44.22 resistance=51.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22499298.0 spike=0.52
- EALR.CA: score=-0.39 buy_ready=False sector_rank=4 price=273.85 support=270.0 resistance=367.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=22.46 liquidity=1185551.38 spike=0.34
- EASB.CA: score=-3.17 buy_ready=False sector_rank=4 price=5.74 support=5.65 resistance=6.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2408981.25 spike=0.49
- EAST.CA: score=13.86 buy_ready=False sector_rank=18 price=28.97 support=27.01 resistance=32.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=14257119.0 spike=0.32
- EBSC.CA: score=-2.23 buy_ready=False sector_rank=4 price=1.32 support=1.31 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2702072.0 spike=1.32
- ECAP.CA: score=0.14 buy_ready=False sector_rank=4 price=26.72 support=25.7 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=19.94 liquidity=1712881.25 spike=0.46
- EDFM.CA: score=-0.12 buy_ready=False sector_rank=4 price=379.83 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=34.92 liquidity=451025.41 spike=0.41
- EEII.CA: score=-2.12 buy_ready=False sector_rank=4 price=1.58 support=1.56 resistance=1.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3459328.0 spike=0.47
- EFIC.CA: score=6.74 buy_ready=False sector_rank=2 price=136.36 support=135.1 resistance=149.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15396707.0 spike=0.52
- EFID.CA: score=13.73 buy_ready=False sector_rank=18 price=17.37 support=16.98 resistance=20.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.41 liquidity=9871352.0 spike=0.23
- EFIH.CA: score=12.4 buy_ready=False sector_rank=20 price=21.7 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=47172688.0 spike=0.74
- EGAL.CA: score=10.74 buy_ready=False sector_rank=2 price=293.51 support=275.0 resistance=362.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=28.15 liquidity=67706472.0 spike=0.76
- EGAS.CA: score=-0.25 buy_ready=False sector_rank=12 price=47.89 support=47.0 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=27.5 liquidity=1991098.25 spike=0.28
- EGBE.CA: score=3.82 buy_ready=False sector_rank=11 price=0.49 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=35.14 liquidity=38695.62 spike=0.29
- EGCH.CA: score=6.74 buy_ready=False sector_rank=2 price=10.6 support=10.6 resistance=11.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38108060.0 spike=0.54
- EGSA.CA: score=15.82 buy_ready=False sector_rank=1 price=9.03 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=66.07 liquidity=3332.07 spike=0.57
- EGTS.CA: score=-3.67 buy_ready=False sector_rank=8 price=11.85 support=11.76 resistance=12.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2070409.25 spike=0.08
- EHDR.CA: score=4.6 buy_ready=False sector_rank=4 price=1.99 support=1.96 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11252725.0 spike=1.09
- ELEC.CA: score=3.36 buy_ready=False sector_rank=16 price=1.51 support=1.49 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36961496.0 spike=0.73
- ELKA.CA: score=0.09 buy_ready=False sector_rank=4 price=1.33 support=1.31 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5661673.0 spike=0.43
- ELNA.CA: score=19.73 buy_ready=False sector_rank=4 price=38.82 support=33.46 resistance=36.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1301285.25 spike=4.69
- ELSH.CA: score=3.53 buy_ready=False sector_rank=4 price=9.35 support=9.33 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9106521.0 spike=0.45
- ELWA.CA: score=8.69 buy_ready=False sector_rank=4 price=1.65 support=1.43 resistance=1.7 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=261084.45 spike=0.72
- EMFD.CA: score=4.67 buy_ready=False sector_rank=8 price=11.12 support=11.2 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=26.2 liquidity=5403816.5 spike=0.09
- ENGC.CA: score=-1.94 buy_ready=False sector_rank=4 price=29.81 support=29.76 resistance=31.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3638510.0 spike=0.32
- EOSB.CA: score=16.87 buy_ready=False sector_rank=4 price=1.64 support=1.57 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=443093.56 spike=12.38
- EPCO.CA: score=-0.25 buy_ready=False sector_rank=4 price=7.96 support=7.7 resistance=11.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=26.34 liquidity=1327036.38 spike=0.31
- EPPK.CA: score=-5.16 buy_ready=False sector_rank=4 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=8.82 buy_ready=False sector_rank=1 price=126.58 support=125.32 resistance=132.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=188438192.0 spike=0.79
- ETRS.CA: score=15.29 buy_ready=False sector_rank=4 price=10.01 support=9.61 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=47.61 liquidity=8869515.0 spike=0.87
- EXPA.CA: score=-1.52 buy_ready=False sector_rank=11 price=13.4 support=13.31 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4696862.5 spike=0.12
- FAIT.CA: score=4.6 buy_ready=False sector_rank=11 price=43.06 support=40.4 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=815545.75 spike=0.27
- FAITA.CA: score=10.81 buy_ready=False sector_rank=11 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=57.84 liquidity=25300.3 spike=0.72
- FERC.CA: score=0.14 buy_ready=False sector_rank=2 price=60.37 support=60.26 resistance=63.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3356995.25 spike=1.02
- FWRY.CA: score=11.4 buy_ready=False sector_rank=20 price=17.04 support=17.33 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=53429748.0 spike=0.48
- GBCO.CA: score=3.63 buy_ready=False sector_rank=14 price=22.58 support=22.5 resistance=24.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=112262080.0 spike=1.0
- GDWA.CA: score=1.78 buy_ready=False sector_rank=4 price=0.54 support=0.54 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7360207.0 spike=0.46
- GGCC.CA: score=0.41 buy_ready=False sector_rank=4 price=0.55 support=0.54 resistance=0.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5981372.5 spike=0.38
- GIHD.CA: score=1.75 buy_ready=False sector_rank=4 price=39.17 support=39.01 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7325158.5 spike=0.39
- GMCI.CA: score=5.48 buy_ready=False sector_rank=4 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=45.16 liquidity=59006.64 spike=0.18
- GRCA.CA: score=1.72 buy_ready=False sector_rank=4 price=26.73 support=26.91 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=1291313.63 spike=0.24
- GSSC.CA: score=6.61 buy_ready=False sector_rank=4 price=260.36 support=246.0 resistance=300.0 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=42.04 liquidity=1663179.59 spike=1.26
- GTWL.CA: score=4.42 buy_ready=False sector_rank=4 price=89.24 support=88.0 resistance=103.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156825024.0 spike=0.94
- HDBK.CA: score=7.78 buy_ready=False sector_rank=11 price=89.84 support=90.26 resistance=113.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=22.2 liquidity=10422554.0 spike=0.51
- HELI.CA: score=4.26 buy_ready=False sector_rank=8 price=6.15 support=6.15 resistance=6.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55010380.0 spike=0.84
- HRHO.CA: score=13.1 buy_ready=False sector_rank=10 price=23.64 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=51.87 liquidity=20163416.0 spike=0.16
- ICID.CA: score=-5.1 buy_ready=False sector_rank=4 price=15.6 support=15.3 resistance=16.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=474456.94 spike=0.07
- IDRE.CA: score=-2.42 buy_ready=False sector_rank=4 price=37.13 support=36.7 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3159550.0 spike=0.55
- IFAP.CA: score=-0.82 buy_ready=False sector_rank=15 price=17.42 support=17.17 resistance=20.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=29.22 liquidity=1587580.63 spike=0.29
- INFI.CA: score=4.42 buy_ready=False sector_rank=4 price=110.25 support=110.12 resistance=121.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10502608.0 spike=0.5
- IRON.CA: score=12.88 buy_ready=False sector_rank=2 price=24.58 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=47.35 liquidity=7134404.5 spike=0.67
- ISMA.CA: score=-3.25 buy_ready=False sector_rank=4 price=18.85 support=18.63 resistance=20.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2330824.75 spike=0.33
- ISMQ.CA: score=6.74 buy_ready=False sector_rank=2 price=6.45 support=6.41 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14283959.0 spike=0.83
- ISPH.CA: score=2.9 buy_ready=False sector_rank=17 price=9.42 support=9.35 resistance=10.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46086880.0 spike=0.98
- JUFO.CA: score=6.21 buy_ready=False sector_rank=18 price=22.58 support=22.1 resistance=26.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=4353381.0 spike=0.24
- KABO.CA: score=-3.69 buy_ready=False sector_rank=19 price=6.66 support=6.55 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3550536.25 spike=0.16
- KWIN.CA: score=-4.4 buy_ready=False sector_rank=4 price=56.14 support=55.02 resistance=60.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1180143.25 spike=0.22
- KZPC.CA: score=7.22 buy_ready=False sector_rank=4 price=12.54 support=12.15 resistance=14.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=52.23 liquidity=2799272.75 spike=0.33
- LCSW.CA: score=10.45 buy_ready=False sector_rank=9 price=31.86 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=50.05 liquidity=4236299.0 spike=0.21
- LUTS.CA: score=4.42 buy_ready=False sector_rank=4 price=0.53 support=0.53 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33391348.0 spike=0.62
- MAAL.CA: score=-2.59 buy_ready=False sector_rank=4 price=6.0 support=5.91 resistance=6.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2982428.5 spike=0.14
- MASR.CA: score=4.42 buy_ready=False sector_rank=4 price=6.09 support=6.06 resistance=6.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35885928.0 spike=0.73
- MBSC.CA: score=4.22 buy_ready=False sector_rank=9 price=290.99 support=290.9 resistance=316.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26661110.0 spike=0.28
- MCQE.CA: score=4.22 buy_ready=False sector_rank=9 price=150.2 support=150.06 resistance=164.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35931432.0 spike=0.57
- MCRO.CA: score=8.42 buy_ready=False sector_rank=4 price=1.23 support=1.21 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=25.86 liquidity=24319294.0 spike=0.52
- MENA.CA: score=-4.79 buy_ready=False sector_rank=8 price=5.63 support=5.61 resistance=5.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=943801.44 spike=0.46
- MEPA.CA: score=-3.3 buy_ready=False sector_rank=4 price=1.37 support=1.34 resistance=1.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2273685.25 spike=0.31
- MFPC.CA: score=19.74 buy_ready=False sector_rank=2 price=44.89 support=40.66 resistance=48.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=49.02 liquidity=32716166.0 spike=0.7
- MFSC.CA: score=-4.0 buy_ready=False sector_rank=4 price=35.24 support=34.6 resistance=38.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1579809.13 spike=0.68
- MHOT.CA: score=-2.53 buy_ready=False sector_rank=21 price=14.03 support=14.03 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=28.91 liquidity=1071820.0 spike=0.07
- MICH.CA: score=11.09 buy_ready=False sector_rank=4 price=39.59 support=35.5 resistance=45.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=4663598.0 spike=0.55
- MILS.CA: score=-0.89 buy_ready=False sector_rank=4 price=121.0 support=121.0 resistance=133.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4689776.0 spike=0.63
- MIPH.CA: score=-1.43 buy_ready=False sector_rank=17 price=719.06 support=666.66 resistance=879.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=30.1 liquidity=671851.31 spike=0.16
- MOED.CA: score=4.42 buy_ready=False sector_rank=4 price=0.48 support=0.47 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11332652.0 spike=0.88
- MOIL.CA: score=-1.19 buy_ready=False sector_rank=12 price=0.65 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=58126.52 spike=0.25
- MOIN.CA: score=-2.8 buy_ready=False sector_rank=4 price=27.59 support=27.2 resistance=30.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2777551.5 spike=0.28
- MOSC.CA: score=-4.71 buy_ready=False sector_rank=4 price=235.5 support=230.0 resistance=249.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=868860.88 spike=0.25
- MPCI.CA: score=4.42 buy_ready=False sector_rank=4 price=269.06 support=260.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29568756.0 spike=0.3
- MPCO.CA: score=3.59 buy_ready=False sector_rank=15 price=1.72 support=1.71 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47094568.0 spike=0.48
- MPRC.CA: score=4.42 buy_ready=False sector_rank=4 price=29.91 support=29.51 resistance=33.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10232444.0 spike=0.64
- MTIE.CA: score=6.06 buy_ready=False sector_rank=14 price=6.97 support=7.05 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=8425112.0 spike=0.42
- NAHO.CA: score=5.0 buy_ready=False sector_rank=4 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=20290.14 spike=1.28
- NCCW.CA: score=2.74 buy_ready=False sector_rank=4 price=4.82 support=4.79 resistance=5.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8320375.0 spike=0.3
- NEDA.CA: score=1.6 buy_ready=False sector_rank=4 price=2.6 support=2.47 resistance=2.75 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=175562.39 spike=0.69
- NHPS.CA: score=-0.91 buy_ready=False sector_rank=4 price=53.24 support=52.7 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4666538.0 spike=0.47
- NINH.CA: score=-1.81 buy_ready=False sector_rank=4 price=13.28 support=13.1 resistance=14.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3763016.0 spike=0.34
- NIPH.CA: score=2.9 buy_ready=False sector_rank=17 price=240.1 support=240.0 resistance=266.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55548080.0 spike=0.47
- OBRI.CA: score=0.77 buy_ready=False sector_rank=4 price=22.06 support=22.0 resistance=24.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6344690.0 spike=0.43
- OCDI.CA: score=4.26 buy_ready=False sector_rank=8 price=22.45 support=22.1 resistance=24.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16593037.0 spike=0.45
- OCPH.CA: score=-2.88 buy_ready=False sector_rank=4 price=168.7 support=165.05 resistance=183.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2692934.5 spike=0.92
- ODIN.CA: score=-1.45 buy_ready=False sector_rank=4 price=1.92 support=1.91 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4125125.75 spike=0.67
- OFH.CA: score=4.42 buy_ready=False sector_rank=4 price=0.67 support=0.65 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10428516.0 spike=0.16
- OIH.CA: score=8.66 buy_ready=False sector_rank=13 price=1.69 support=1.7 resistance=2.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=32202110.0 spike=0.47
- OLFI.CA: score=2.07 buy_ready=False sector_rank=18 price=19.34 support=19.4 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=20.32 liquidity=5213098.5 spike=0.35
- ORAS.CA: score=5.6 buy_ready=False sector_rank=3 price=800.0 support=800.0 resistance=839.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73259736.0 spike=1.0
- ORHD.CA: score=4.26 buy_ready=False sector_rank=8 price=9.03 support=9.02 resistance=9.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63255924.0 spike=0.52
- ORWE.CA: score=7.14 buy_ready=False sector_rank=19 price=24.53 support=24.8 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=27.39 liquidity=9382341.0 spike=0.23
- PHAR.CA: score=7.9 buy_ready=False sector_rank=17 price=97.79 support=98.05 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=25.35 liquidity=27793328.0 spike=0.46
- PHDC.CA: score=15.26 buy_ready=False sector_rank=8 price=11.94 support=12.2 resistance=13.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=35.81 liquidity=46760200.0 spike=0.47
- PHTV.CA: score=5.07 buy_ready=False sector_rank=4 price=320.0 support=310.02 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=41.97 liquidity=643155.63 spike=0.65
- POUL.CA: score=2.86 buy_ready=False sector_rank=18 price=9.09 support=9.05 resistance=9.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44970184.0 spike=0.84
- PRCL.CA: score=0.66 buy_ready=False sector_rank=9 price=19.58 support=19.14 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6443671.0 spike=0.63
- PRDC.CA: score=0.15 buy_ready=False sector_rank=8 price=5.81 support=5.8 resistance=6.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5887113.5 spike=0.16
- PRMH.CA: score=-4.16 buy_ready=False sector_rank=4 price=1.8 support=1.8 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1413651.0 spike=0.45
- RACC.CA: score=1.82 buy_ready=False sector_rank=4 price=7.71 support=7.93 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=30.16 liquidity=3391831.25 spike=0.51
- RAKT.CA: score=9.72 buy_ready=False sector_rank=4 price=23.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=66.11 liquidity=292631.39 spike=0.74
- RAYA.CA: score=4.29 buy_ready=False sector_rank=6 price=5.3 support=5.29 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14499281.0 spike=0.49
- RMDA.CA: score=12.9 buy_ready=False sector_rank=17 price=4.85 support=4.8 resistance=5.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=35.1 liquidity=13382495.0 spike=0.5
- ROTO.CA: score=2.26 buy_ready=False sector_rank=4 price=28.84 support=28.72 resistance=31.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7832809.0 spike=0.91
- RREI.CA: score=-1.27 buy_ready=False sector_rank=4 price=2.53 support=2.51 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4302840.5 spike=0.61
- RTVC.CA: score=-2.4 buy_ready=False sector_rank=4 price=3.04 support=3.04 resistance=3.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2893714.0 spike=1.14
- RUBX.CA: score=4.42 buy_ready=False sector_rank=4 price=12.86 support=12.72 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59304536.0 spike=0.64
- SAUD.CA: score=4.03 buy_ready=False sector_rank=11 price=20.57 support=20.2 resistance=24.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=31.68 liquidity=5247275.0 spike=0.41
- SCEM.CA: score=4.22 buy_ready=False sector_rank=9 price=79.25 support=79.02 resistance=83.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16559999.0 spike=0.27
- SCFM.CA: score=-3.64 buy_ready=False sector_rank=4 price=199.31 support=197.2 resistance=222.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1813328.25 spike=1.06
- SCTS.CA: score=9.26 buy_ready=False sector_rank=7 price=518.25 support=485.2 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14325148.0 spike=7.3
- SDTI.CA: score=17.42 buy_ready=False sector_rank=4 price=81.34 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=43.63 liquidity=27558680.0 spike=1.0
- SEIG.CA: score=-4.19 buy_ready=False sector_rank=4 price=162.31 support=157.1 resistance=174.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1389029.25 spike=0.68
- SIPC.CA: score=4.42 buy_ready=False sector_rank=4 price=4.3 support=4.3 resistance=4.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23390206.0 spike=0.41
- SKPC.CA: score=10.74 buy_ready=False sector_rank=2 price=14.54 support=14.4 resistance=17.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=33.65 liquidity=20498222.0 spike=0.29
- SMFR.CA: score=-3.58 buy_ready=False sector_rank=4 price=179.8 support=178.0 resistance=197.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1995658.38 spike=0.64
- SNFC.CA: score=6.62 buy_ready=False sector_rank=4 price=10.73 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=38.15 liquidity=3192241.25 spike=0.38
- SPIN.CA: score=-0.52 buy_ready=False sector_rank=19 price=13.6 support=13.5 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=27.5 liquidity=2719090.5 spike=0.51
- SPMD.CA: score=-0.62 buy_ready=False sector_rank=4 price=0.33 support=0.33 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4951328.0 spike=0.41
- SUGR.CA: score=9.03 buy_ready=False sector_rank=18 price=52.52 support=50.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=54.8 liquidity=4176075.0 spike=0.45
- SVCE.CA: score=4.42 buy_ready=False sector_rank=4 price=7.84 support=7.8 resistance=8.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24143674.0 spike=0.34
- SWDY.CA: score=8.36 buy_ready=False sector_rank=16 price=103.11 support=101.5 resistance=124.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=28282320.0 spike=0.43
- TALM.CA: score=4.26 buy_ready=False sector_rank=7 price=17.72 support=17.52 resistance=19.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12637097.0 spike=0.44
- TMGH.CA: score=15.26 buy_ready=False sector_rank=8 price=84.1 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=94394840.0 spike=0.36
- TRTO.CA: score=-0.57 buy_ready=False sector_rank=4 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=3413.86 spike=0.52
- UEFM.CA: score=-0.95 buy_ready=False sector_rank=4 price=456.84 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=31.37 liquidity=625052.38 spike=0.21
- UEGC.CA: score=4.42 buy_ready=False sector_rank=4 price=1.32 support=1.31 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18847818.0 spike=0.42
- UNIP.CA: score=-2.03 buy_ready=False sector_rank=4 price=0.28 support=0.28 resistance=0.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3545344.5 spike=0.43
- UNIT.CA: score=-4.03 buy_ready=False sector_rank=8 price=16.0 support=16.0 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1702297.63 spike=0.45
- WCDF.CA: score=-1.04 buy_ready=False sector_rank=4 price=485.44 support=432.5 resistance=686.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=17.19 liquidity=535499.44 spike=0.2
- WKOL.CA: score=7.68 buy_ready=False sector_rank=4 price=259.94 support=241.1 resistance=331.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=36.22 liquidity=4258093.0 spike=0.58
- ZEOT.CA: score=-1.21 buy_ready=False sector_rank=4 price=10.18 support=10.03 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4368867.0 spike=0.56
- ZMID.CA: score=4.26 buy_ready=False sector_rank=8 price=6.3 support=6.3 resistance=6.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33057140.0 spike=0.44

## Backtesting Lite
- ABUK.CA: 180d return=62.36%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-21T21:00:00+00:00
- MFPC.CA: 180d return=51.02%, max drawdown=-26.33%, MA20>MA50 days last20=20, as_of=2026-10-21T21:00:00+00:00
- ELNA.CA: 180d return=-1.83%, max drawdown=-15.86%, MA20>MA50 days last20=0, as_of=2026-10-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- ELNA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Manufacturing Agricultural Crops S.A.E summary=Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops; El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m; EGX halts trading on El Nasr for Manufacturing Agricultural Crops
  - Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops: https://english.mubasher.info/news/3749421/Consortium-offers-to-acquire-controlling-stake-in-El-Nasr-for-Agricultural-Crops/
  - El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m: https://english.mubasher.info/news/3685533/El-Nasr-for-Agricultural-Crops-to-sell-Sohag-factory-land-for-EGP-650m/
  - EGX halts trading on El Nasr for Manufacturing Agricultural Crops: https://english.mubasher.info/news/3489525/EGX-halts-trading-on-El-Nasr-for-Manufacturing-Agricultural-Crops/
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/
- EOSB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Orouba Securities Brokerage summary=El Orouba Brokerage turns profitable in Q4; El Orouba Securities suffers 598,000 losses in Q3; El Orouba Securities H1 losses down 7%
  - El Orouba Brokerage turns profitable in Q4: https://english.mubasher.info/news/3067539/El-Orouba-Brokerage-turns-profitable-in-Q4/
  - El Orouba Securities suffers 598,000 losses in Q3: https://english.mubasher.info/news/3016624/El-Orouba-Securities-suffers-598-000-losses-in-Q3/
  - El Orouba Securities H1 losses down 7%: https://english.mubasher.info/news/2984110/El-Orouba-Securities-H1-losses-down-7-/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- CPCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Kahira Pharmaceuticals & Chemical Industries Company summary=Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22; Kahira Pharmaceuticals sees EGP 9m block trading deal; Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals
  - Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22: https://english.mubasher.info/news/3910780/Kahira-Pharmaceuticals-net-profits-up-22-5-in-H1-21-22/
  - Kahira Pharmaceuticals sees EGP 9m block trading deal: https://english.mubasher.info/news/3903033/Kahira-Pharmaceuticals-sees-EGP-9m-block-trading-deal/
  - Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals: https://english.mubasher.info/news/3816375/Adel-Taha-Abdel-Wahab-named-Chairman-of-Kahira-Pharmaceuticals/

## Warnings
- OpenRouter API error: 404
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for ELNA.CA matches the company but no source/report date was detected.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
- Evidence for EOSB.CA matches the company but no source/report date was detected.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
