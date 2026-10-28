# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-28T11:40:01.529126+00:00
Generated Cairo: 2026-10-28 14:40
Run timing: target 08:45 Cairo | generated Cairo 2026-10-28 14:40 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-28 14:36

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 172/187
- Top sector: Industrial Goods & Construction

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, October 28
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 21.05% / above MA50 10.53%
- EGX70 regime: BEARISH / above MA20 2.56% / above MA50 2.56%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=267430496.0 spike=0.52 score=17.37
- NIPH.CA: liquidity=249094496.0 spike=2.08 score=5.78
- CCAP.CA: liquidity=244828352.0 spike=0.5 score=12.49
- TMGH.CA: liquidity=225989072.0 spike=0.89 score=13.8
- BIOC.CA: liquidity=189919600.0 spike=1.7 score=3.8

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- SPMD.CA: spike=3.84 liquidity=47278180.0 outlook=WEAK_OR_RISKY score=21 buy_ready=False
- MEPA.CA: spike=3.81 liquidity=38966780.0 outlook=WEAK_OR_RISKY score=23 buy_ready=False
- OCPH.CA: spike=2.8 liquidity=8221395.5 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CAED.CA: spike=2.78 liquidity=24535600.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CANA.CA: spike=2.76 liquidity=44436056.0 outlook=BULLISH_WATCH score=97.93 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #2 Banking & Financials: score=0.93 5d=-0.46% 20d=-4.53% aboveMA50=20.0%
- #3 Food, Beverages & Tobacco: score=-0.92 5d=-3.3% 20d=-5.4% aboveMA50=0.0%
- #4 Healthcare: score=-0.96 5d=-1.87% 20d=-6.44% aboveMA50=0.0%
- #5 Building Materials: score=-1.07 5d=-4.95% 20d=1.2% aboveMA50=0.0%
- #6 Education: score=-1.1 5d=-4.06% 20d=-5.1% aboveMA50=0.0%
- #7 Energy & Petrochemicals: score=-1.8 5d=-4.4% 20d=-8.58% aboveMA50=33.33%
- #8 Basic Resources & Chemicals: score=-2.17 5d=-5.75% 20d=-10.23% aboveMA50=20.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CANA.CA: BULLISH_WATCH score=97.93 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MFPC.CA: BULLISH_WATCH score=76 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=sector is not leading
- ABUK.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- CPCI.CA: CONSTRUCTIVE score=59 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- SDTI.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- ETRS.CA: NEUTRAL score=48 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA20; below MA50; sector is not leading
- AJWA.CA: NEUTRAL score=47 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- ADIB.CA: NEUTRAL score=46.93 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20; below MA50
- EFID.CA: NEUTRAL score=46 liquidity=TRADEABLE sector=NEUTRAL risk=below MA20; below MA50
- JUFO.CA: NEUTRAL score=46 liquidity=TRADEABLE sector=NEUTRAL risk=below MA20; below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=1.89 buy_ready=False sector_rank=17 price=208.21 support=171.02 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=5493725.5 spike=0.62
- ABUK.CA: score=20.59 buy_ready=False sector_rank=8 price=90.88 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=55.94 liquidity=94955624.0 spike=1.23
- ACAMD.CA: score=11.4 buy_ready=False sector_rank=17 price=1.93 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=42271684.0 spike=0.97
- ACGC.CA: score=6.79 buy_ready=False sector_rank=18 price=12.79 support=11.6 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=35.07 liquidity=4390058.0 spike=0.41
- ADCI.CA: score=8.33 buy_ready=False sector_rank=17 price=260.23 support=221.0 resistance=278.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=41.35 liquidity=3570259.75 spike=2.18
- ADIB.CA: score=18.37 buy_ready=False sector_rank=2 price=45.5 support=43.16 resistance=51.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=44.88 liquidity=46312416.0 spike=0.6
- ADPC.CA: score=3.06 buy_ready=False sector_rank=17 price=2.85 support=2.53 resistance=3.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=26.49 liquidity=6655059.5 spike=0.73
- AFDI.CA: score=-0.72 buy_ready=False sector_rank=17 price=42.79 support=34.8 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=23.49 liquidity=1879025.88 spike=0.44
- AFMC.CA: score=7.4 buy_ready=False sector_rank=17 price=110.01 support=94.6 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=19.69 liquidity=13677660.0 spike=0.74
- AJWA.CA: score=9.8 buy_ready=False sector_rank=17 price=201.03 support=177.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=4395761.5 spike=0.13
- ALCN.CA: score=6.75 buy_ready=False sector_rank=10 price=31.04 support=27.11 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=36.81 liquidity=3830106.75 spike=0.18
- ALUM.CA: score=-1.82 buy_ready=False sector_rank=17 price=17.92 support=16.02 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.87 liquidity=1780385.38 spike=0.52
- AMER.CA: score=8.58 buy_ready=False sector_rank=12 price=4.21 support=3.21 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=32.73 liquidity=74328408.0 spike=1.39
- AMES.CA: score=8.4 buy_ready=False sector_rank=17 price=31.86 support=28.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=18.81 liquidity=41326284.0 spike=0.71
- AMIA.CA: score=2.43 buy_ready=False sector_rank=17 price=16.93 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=34.47 liquidity=5028430.0 spike=0.32
- AMOC.CA: score=11.28 buy_ready=False sector_rank=7 price=13.28 support=12.55 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=32.79 liquidity=76770008.0 spike=0.61
- APSW.CA: score=-2.71 buy_ready=False sector_rank=17 price=7.45 support=7.1 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=7.95 liquidity=668384.63 spike=1.11
- ARAB.CA: score=12.8 buy_ready=False sector_rank=12 price=0.24 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=111775144.0 spike=0.97
- ARCC.CA: score=13.57 buy_ready=False sector_rank=5 price=63.28 support=58.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=20281850.0 spike=0.46
- AREH.CA: score=6.91 buy_ready=False sector_rank=17 price=1.03 support=0.91 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=29.31 liquidity=9992892.0 spike=1.26
- ASCM.CA: score=-0.11 buy_ready=False sector_rank=17 price=42.5 support=38.2 resistance=59.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=23.97 liquidity=3487670.5 spike=0.41
- ASPI.CA: score=6.4 buy_ready=False sector_rank=17 price=0.3 support=0.27 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=33.52 liquidity=14641829.0 spike=0.77
- ATLC.CA: score=0.02 buy_ready=False sector_rank=13 price=4.69 support=3.93 resistance=6.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=32.16 liquidity=3271765.75 spike=0.43
- ATQA.CA: score=7.13 buy_ready=False sector_rank=8 price=9.09 support=8.25 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=28.67 liquidity=24095896.0 spike=0.45
- AXPH.CA: score=-1.79 buy_ready=False sector_rank=17 price=1350.13 support=1250.0 resistance=1359.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5669528.5 spike=1.07
- BINV.CA: score=7.49 buy_ready=False sector_rank=16 price=52.0 support=52.57 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=30.58 liquidity=11050889.0 spike=0.77
- BIOC.CA: score=3.8 buy_ready=False sector_rank=17 price=281.2 support=262.0 resistance=298.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=189919600.0 spike=1.7
- BTFH.CA: score=6.74 buy_ready=False sector_rank=13 price=2.25 support=2.05 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=29.06 liquidity=96958440.0 spike=0.94
- CAED.CA: score=5.96 buy_ready=False sector_rank=17 price=87.03 support=80.01 resistance=92.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24535600.0 spike=2.78
- CANA.CA: score=24.89 buy_ready=False sector_rank=2 price=44.62 support=38.1 resistance=48.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=44436056.0 spike=2.76
- CCAP.CA: score=12.49 buy_ready=False sector_rank=16 price=6.04 support=5.8 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=244828352.0 spike=0.5
- CCRS.CA: score=1.6 buy_ready=False sector_rank=17 price=1.6 support=1.3 resistance=2.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=20.77 liquidity=5204124.0 spike=0.76
- CEFM.CA: score=0.99 buy_ready=False sector_rank=17 price=115.44 support=102.2 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=28.92 liquidity=2789390.75 spike=1.4
- CERA.CA: score=6.4 buy_ready=False sector_rank=17 price=1.02 support=0.93 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=24.29 liquidity=73172816.0 spike=0.61
- CFGH.CA: score=-3.6 buy_ready=False sector_rank=17 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=9.09 liquidity=4493.69 spike=0.83
- CICH.CA: score=-2.65 buy_ready=False sector_rank=13 price=10.7 support=9.63 resistance=12.38 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=29.72 liquidity=609685.99 spike=0.35
- CIEB.CA: score=6.15 buy_ready=False sector_rank=2 price=22.5 support=21.35 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=34.94 liquidity=5773137.0 spike=0.68
- CIRA.CA: score=0.61 buy_ready=False sector_rank=6 price=34.31 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=2048105.88 spike=0.13
- CLHO.CA: score=7.62 buy_ready=False sector_rank=4 price=13.62 support=12.51 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=26.9 liquidity=22945404.0 spike=0.61
- CNFN.CA: score=5.85 buy_ready=False sector_rank=13 price=3.74 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=41.59 liquidity=4109923.5 spike=0.45
- COMI.CA: score=17.37 buy_ready=False sector_rank=2 price=120.31 support=118.06 resistance=129.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=267430496.0 spike=0.52
- COPR.CA: score=7.6 buy_ready=False sector_rank=17 price=0.39 support=0.33 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=27.8 liquidity=17890516.0 spike=1.1
- COSG.CA: score=2.56 buy_ready=False sector_rank=17 price=1.23 support=1.11 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=27.16 liquidity=6164253.5 spike=0.55
- CPCI.CA: score=10.95 buy_ready=False sector_rank=17 price=596.04 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=49.32 liquidity=3547372.0 spike=0.69
- CSAG.CA: score=-1.38 buy_ready=False sector_rank=10 price=32.54 support=30.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=31.84 liquidity=1699021.25 spike=0.25
- DAPH.CA: score=6.18 buy_ready=False sector_rank=17 price=76.26 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=9775908.0 spike=0.24
- DEIN.CA: score=5.4 buy_ready=False sector_rank=17 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=-0.2 buy_ready=False sector_rank=3 price=22.45 support=20.27 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=34.73 liquidity=1168004.25 spike=0.36
- DSCW.CA: score=8.88 buy_ready=False sector_rank=17 price=1.48 support=1.23 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=7481896.0 spike=0.46
- DTPP.CA: score=6.4 buy_ready=False sector_rank=17 price=43.25 support=36.0 resistance=334.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=4.24 liquidity=21197424.0 spike=0.53
- EALR.CA: score=-1.07 buy_ready=False sector_rank=17 price=257.39 support=236.01 resistance=355.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=19.38 liquidity=2528883.25 spike=0.82
- EASB.CA: score=7.23 buy_ready=False sector_rank=17 price=6.02 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=4833626.5 spike=0.97
- EAST.CA: score=17.63 buy_ready=False sector_rank=3 price=31.87 support=27.01 resistance=31.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=34974896.0 spike=0.75
- EBSC.CA: score=5.47 buy_ready=False sector_rank=17 price=1.51 support=1.2 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=30.21 liquidity=5714583.5 spike=2.68
- ECAP.CA: score=-1.66 buy_ready=False sector_rank=17 price=26.35 support=24.8 resistance=31.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=27.39 liquidity=1937556.25 spike=0.58
- EDFM.CA: score=-2.15 buy_ready=False sector_rank=17 price=367.21 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=31.06 liquidity=447697.09 spike=0.39
- EEII.CA: score=7.27 buy_ready=False sector_rank=17 price=1.61 support=1.42 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=21.11 liquidity=9873652.0 spike=1.5
- EFIC.CA: score=7.13 buy_ready=False sector_rank=8 price=139.92 support=121.0 resistance=178.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=34.89 liquidity=19869246.0 spike=0.85
- EFID.CA: score=15.63 buy_ready=False sector_rank=3 price=17.7 support=16.01 resistance=19.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=33365736.0 spike=0.84
- EFIH.CA: score=12.73 buy_ready=False sector_rank=14 price=22.01 support=20.3 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=35.63 liquidity=32680922.0 spike=0.49
- EGAL.CA: score=8.13 buy_ready=False sector_rank=8 price=303.5 support=275.0 resistance=359.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=32.11 liquidity=54953408.0 spike=0.58
- EGAS.CA: score=-0.94 buy_ready=False sector_rank=7 price=46.72 support=43.0 resistance=58.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=29.49 liquidity=1780042.5 spike=0.36
- EGBE.CA: score=1.41 buy_ready=False sector_rank=2 price=0.51 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=33.0 liquidity=41763.44 spike=0.41
- EGCH.CA: score=7.13 buy_ready=False sector_rank=8 price=10.54 support=10.0 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=26.69 liquidity=34094856.0 spike=0.59
- EGSA.CA: score=2.87 buy_ready=False sector_rank=11 price=8.81 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=46.05 liquidity=881.0 spike=0.19
- EGTS.CA: score=6.8 buy_ready=False sector_rank=12 price=12.14 support=10.19 resistance=18.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=22.96 liquidity=12592680.0 spike=0.62
- EHDR.CA: score=2.39 buy_ready=False sector_rank=17 price=1.96 support=1.8 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=5985462.5 spike=0.65
- ELEC.CA: score=7.02 buy_ready=False sector_rank=9 price=1.49 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=23481810.0 spike=0.47
- ELKA.CA: score=9.5 buy_ready=False sector_rank=17 price=1.37 support=1.21 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=8097286.5 spike=0.62
- ELNA.CA: score=7.84 buy_ready=False sector_rank=17 price=38.05 support=33.46 resistance=39.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=67.13 liquidity=440940.28 spike=0.88
- ELSH.CA: score=6.4 buy_ready=False sector_rank=17 price=9.73 support=8.57 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=17105122.0 spike=0.96
- ELWA.CA: score=7.44 buy_ready=False sector_rank=17 price=1.65 support=1.43 resistance=1.66 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=40835.85 spike=0.14
- EMFD.CA: score=7.8 buy_ready=False sector_rank=12 price=11.6 support=10.6 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=30.06 liquidity=48236792.0 spike=0.91
- ENGC.CA: score=2.72 buy_ready=False sector_rank=17 price=33.18 support=30.54 resistance=33.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12200749.0 spike=1.16
- EOSB.CA: score=7.42 buy_ready=False sector_rank=17 price=1.61 support=1.56 resistance=1.72 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=16315.74 spike=0.25
- EPCO.CA: score=-1.96 buy_ready=False sector_rank=17 price=7.72 support=7.0 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=29.96 liquidity=1636923.88 spike=0.38
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=17 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=7.87 buy_ready=False sector_rank=11 price=123.39 support=115.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=29.32 liquidity=172577792.0 spike=0.63
- ETRS.CA: score=15.56 buy_ready=False sector_rank=17 price=10.4 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=42.48 liquidity=30910194.0 spike=2.58
- EXPA.CA: score=12.37 buy_ready=False sector_rank=2 price=13.78 support=12.0 resistance=16.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=29.42 liquidity=12993014.0 spike=0.37
- FAIT.CA: score=9.28 buy_ready=False sector_rank=2 price=43.05 support=40.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=38.64 liquidity=2911391.75 spike=0.99
- FAITA.CA: score=13.39 buy_ready=False sector_rank=2 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=52.8 liquidity=19177.11 spike=0.56
- FERC.CA: score=1.81 buy_ready=False sector_rank=8 price=61.01 support=57.55 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6533778.0 spike=2.07
- FWRY.CA: score=6.73 buy_ready=False sector_rank=14 price=17.0 support=16.45 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=33.19 liquidity=79861224.0 spike=0.68
- GBCO.CA: score=6.4 buy_ready=False sector_rank=20 price=23.14 support=22.02 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=16.75 liquidity=31080256.0 spike=0.26
- GDWA.CA: score=6.4 buy_ready=False sector_rank=17 price=0.53 support=0.48 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=26.89 liquidity=11890273.0 spike=0.91
- GGCC.CA: score=6.4 buy_ready=False sector_rank=17 price=0.54 support=0.49 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=26.75 liquidity=13437672.0 spike=0.8
- GIHD.CA: score=6.4 buy_ready=False sector_rank=17 price=39.07 support=32.1 resistance=71.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=16.47 liquidity=12367268.0 spike=0.88
- GMCI.CA: score=0.76 buy_ready=False sector_rank=17 price=1.48 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=558284.13 spike=1.9
- GRCA.CA: score=4.2 buy_ready=False sector_rank=17 price=26.26 support=22.57 resistance=39.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=18.79 liquidity=6881922.5 spike=1.46
- GSSC.CA: score=-3.15 buy_ready=False sector_rank=17 price=246.77 support=211.52 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=32.95 liquidity=445822.75 spike=0.39
- GTWL.CA: score=7.4 buy_ready=False sector_rank=17 price=96.98 support=73.02 resistance=199.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=20.15 liquidity=174512096.0 spike=1.0
- HDBK.CA: score=15.37 buy_ready=False sector_rank=2 price=95.46 support=83.01 resistance=112.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=12030700.0 spike=0.53
- HELI.CA: score=7.8 buy_ready=False sector_rank=12 price=6.26 support=5.72 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=45090656.0 spike=0.68
- HRHO.CA: score=6.74 buy_ready=False sector_rank=13 price=23.82 support=22.8 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=27.88 liquidity=13793480.0 spike=0.11
- ICID.CA: score=8.45 buy_ready=False sector_rank=17 price=16.95 support=14.26 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=41.09 liquidity=6046255.0 spike=0.87
- IDRE.CA: score=-3.89 buy_ready=False sector_rank=17 price=33.9 support=32.1 resistance=35.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3706070.25 spike=0.66
- IFAP.CA: score=0.33 buy_ready=False sector_rank=21 price=16.48 support=15.51 resistance=19.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=3930882.25 spike=0.8
- INFI.CA: score=2.4 buy_ready=False sector_rank=17 price=114.67 support=105.5 resistance=118.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20056048.0 spike=0.98
- IRON.CA: score=4.25 buy_ready=False sector_rank=8 price=25.27 support=23.53 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=25.42 liquidity=7121251.5 spike=0.69
- ISMA.CA: score=7.42 buy_ready=False sector_rank=17 price=18.68 support=14.11 resistance=27.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=28.54 liquidity=10729377.0 spike=1.51
- ISMQ.CA: score=6.95 buy_ready=False sector_rank=8 price=6.65 support=5.96 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=30.85 liquidity=9814622.0 spike=0.61
- ISPH.CA: score=7.62 buy_ready=False sector_rank=4 price=9.86 support=9.14 resistance=12.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=30.34 liquidity=34730456.0 spike=0.77
- JUFO.CA: score=13.63 buy_ready=False sector_rank=3 price=23.03 support=21.01 resistance=26.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=40.33 liquidity=15412012.0 spike=0.92
- KABO.CA: score=6.4 buy_ready=False sector_rank=18 price=6.5 support=5.58 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=32.4 liquidity=18983640.0 spike=0.77
- KWIN.CA: score=-0.35 buy_ready=False sector_rank=17 price=52.05 support=44.02 resistance=82.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=22.21 liquidity=3249599.75 spike=0.71
- KZPC.CA: score=5.8 buy_ready=False sector_rank=17 price=12.57 support=11.56 resistance=13.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=45.72 liquidity=3403963.25 spike=0.47
- LCSW.CA: score=6.45 buy_ready=False sector_rank=5 price=35.32 support=33.45 resistance=35.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52864612.0 spike=2.44
- LUTS.CA: score=3.2 buy_ready=False sector_rank=17 price=0.63 support=0.58 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75825528.0 spike=1.4
- MAAL.CA: score=6.4 buy_ready=False sector_rank=17 price=6.26 support=4.88 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=21.55 liquidity=12306130.0 spike=0.98
- MASR.CA: score=11.4 buy_ready=False sector_rank=17 price=6.39 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=25949060.0 spike=0.52
- MBSC.CA: score=8.57 buy_ready=False sector_rank=5 price=297.74 support=262.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=37996412.0 spike=0.35
- MCQE.CA: score=7.57 buy_ready=False sector_rank=5 price=163.04 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=32.16 liquidity=31242032.0 spike=0.43
- MCRO.CA: score=6.48 buy_ready=False sector_rank=17 price=1.24 support=1.07 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=34.15 liquidity=47775620.0 spike=1.04
- MENA.CA: score=-1.04 buy_ready=False sector_rank=12 price=5.7 support=5.45 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=29.82 liquidity=2167809.25 spike=0.84
- MEPA.CA: score=11.4 buy_ready=False sector_rank=17 price=1.24 support=1.14 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=22.09 liquidity=38966780.0 spike=3.81
- MFPC.CA: score=19.13 buy_ready=False sector_rank=8 price=45.83 support=40.66 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=48.09 liquidity=71803080.0 spike=1.5
- MFSC.CA: score=-2.49 buy_ready=False sector_rank=17 price=32.79 support=28.55 resistance=47.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=22.52 liquidity=1112214.63 spike=0.51
- MHOT.CA: score=-2.82 buy_ready=False sector_rank=19 price=14.09 support=13.0 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=31.47 liquidity=777756.38 spike=0.09
- MICH.CA: score=5.37 buy_ready=False sector_rank=17 price=40.53 support=35.5 resistance=44.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=42.12 liquidity=2973106.25 spike=0.4
- MILS.CA: score=4.75 buy_ready=False sector_rank=17 price=118.5 support=96.02 resistance=201.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=20.26 liquidity=8268640.0 spike=1.04
- MIPH.CA: score=5.45 buy_ready=False sector_rank=4 price=749.75 support=610.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=37.57 liquidity=1830753.38 spike=0.5
- MOED.CA: score=7.16 buy_ready=False sector_rank=17 price=0.46 support=0.39 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=18.93 liquidity=17669512.0 spike=1.38
- MOIL.CA: score=3.38 buy_ready=False sector_rank=7 price=0.65 support=0.6 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=98042.62 spike=0.45
- MOIN.CA: score=1.49 buy_ready=False sector_rank=17 price=28.0 support=25.7 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=25.78 liquidity=4089550.25 spike=0.48
- MOSC.CA: score=5.67 buy_ready=False sector_rank=17 price=241.19 support=198.01 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=33.39 liquidity=6609420.5 spike=1.83
- MPCI.CA: score=2.82 buy_ready=False sector_rank=17 price=291.16 support=271.01 resistance=296.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=113807856.0 spike=1.21
- MPCO.CA: score=6.4 buy_ready=False sector_rank=21 price=1.77 support=1.55 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=45685436.0 spike=0.52
- MPRC.CA: score=6.18 buy_ready=False sector_rank=17 price=31.39 support=27.0 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=29.37 liquidity=9777383.0 spike=0.63
- MTIE.CA: score=10.58 buy_ready=False sector_rank=20 price=7.01 support=6.05 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=38.56 liquidity=9182334.0 spike=0.43
- NAHO.CA: score=2.41 buy_ready=False sector_rank=17 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=38.1 liquidity=12526.98 spike=0.72
- NCCW.CA: score=6.4 buy_ready=False sector_rank=17 price=4.94 support=4.05 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=26.49 liquidity=11541987.0 spike=0.55
- NEDA.CA: score=0.24 buy_ready=False sector_rank=17 price=2.6 support=2.47 resistance=2.71 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=257215.39 spike=1.29
- NHPS.CA: score=0.53 buy_ready=False sector_rank=17 price=54.08 support=50.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=17.16 liquidity=4129302.75 spike=0.49
- NINH.CA: score=4.78 buy_ready=False sector_rank=17 price=14.84 support=14.21 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21294090.0 spike=2.19
- NIPH.CA: score=5.78 buy_ready=False sector_rank=4 price=254.98 support=240.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=249094496.0 spike=2.08
- OBRI.CA: score=1.97 buy_ready=False sector_rank=17 price=21.39 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=29.51 liquidity=5568059.5 spike=0.38
- OCDI.CA: score=11.8 buy_ready=False sector_rank=12 price=23.51 support=21.0 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=38.37 liquidity=32729230.0 spike=0.88
- OCPH.CA: score=4.22 buy_ready=False sector_rank=17 price=179.5 support=174.01 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8221395.5 spike=2.8
- ODIN.CA: score=-1.56 buy_ready=False sector_rank=17 price=1.92 support=1.7 resistance=2.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=25.95 liquidity=2036732.0 spike=0.36
- OFH.CA: score=6.4 buy_ready=False sector_rank=17 price=0.69 support=0.61 resistance=0.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=25.66 liquidity=20834324.0 spike=0.58
- OIH.CA: score=7.49 buy_ready=False sector_rank=16 price=1.61 support=1.5 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=33.85 liquidity=25820120.0 spike=0.48
- OLFI.CA: score=8.63 buy_ready=False sector_rank=3 price=19.01 support=17.86 resistance=22.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=26.61 liquidity=10346646.0 spike=0.7
- ORAS.CA: score=7.6 buy_ready=False sector_rank=1 price=816.14 support=813.0 resistance=834.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117784400.0 spike=1.0
- ORHD.CA: score=8.8 buy_ready=False sector_rank=12 price=9.55 support=8.5 resistance=12.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=23.47 liquidity=54615128.0 spike=0.45
- ORWE.CA: score=6.4 buy_ready=False sector_rank=18 price=23.07 support=22.62 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=22.45 liquidity=31584090.0 spike=0.82
- PHAR.CA: score=8.92 buy_ready=False sector_rank=4 price=98.47 support=90.2 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=27.68 liquidity=68982688.0 spike=1.15
- PHDC.CA: score=6.8 buy_ready=False sector_rank=12 price=11.47 support=11.0 resistance=13.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=32.56 liquidity=49641248.0 spike=0.53
- PHTV.CA: score=3.25 buy_ready=False sector_rank=17 price=324.34 support=300.0 resistance=360.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=38.93 liquidity=846326.19 spike=0.9
- POUL.CA: score=15.63 buy_ready=False sector_rank=3 price=9.45 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=32631642.0 spike=0.56
- PRCL.CA: score=13.67 buy_ready=False sector_rank=5 price=19.68 support=16.65 resistance=27.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=35.37 liquidity=14197534.0 spike=1.55
- PRDC.CA: score=13.8 buy_ready=False sector_rank=12 price=6.02 support=5.08 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=36.34 liquidity=13864896.0 spike=0.4
- PRMH.CA: score=2.88 buy_ready=False sector_rank=17 price=1.85 support=1.7 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=35.56 liquidity=1480147.38 spike=0.49
- RACC.CA: score=0.03 buy_ready=False sector_rank=17 price=7.15 support=6.1 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=24.07 liquidity=3628395.75 spike=0.5
- RAKT.CA: score=-1.16 buy_ready=False sector_rank=17 price=21.39 support=20.26 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=29.5 liquidity=436746.13 spike=1.0
- RAYA.CA: score=6.16 buy_ready=False sector_rank=15 price=5.46 support=5.02 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=29.33 liquidity=9492845.0 spike=0.42
- RMDA.CA: score=13.62 buy_ready=False sector_rank=4 price=5.07 support=4.5 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=16869578.0 spike=0.67
- ROTO.CA: score=1.51 buy_ready=False sector_rank=17 price=28.98 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=24.75 liquidity=5108607.0 spike=0.65
- RREI.CA: score=7.8 buy_ready=False sector_rank=17 price=2.39 support=1.96 resistance=4.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=16.06 liquidity=14876291.0 spike=1.7
- RTVC.CA: score=2.49 buy_ready=False sector_rank=17 price=2.87 support=2.87 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=21.82 liquidity=4467026.5 spike=1.81
- RUBX.CA: score=7.4 buy_ready=False sector_rank=17 price=12.41 support=10.51 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=31.3 liquidity=36831624.0 spike=0.44
- SAUD.CA: score=4.56 buy_ready=False sector_rank=2 price=20.71 support=19.3 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=33.44 liquidity=3187254.5 spike=0.28
- SCEM.CA: score=13.57 buy_ready=False sector_rank=5 price=83.24 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=46.68 liquidity=25850270.0 spike=0.44
- SCFM.CA: score=-0.79 buy_ready=False sector_rank=17 price=193.79 support=153.02 resistance=264.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=25.27 liquidity=2325560.0 spike=1.24
- SCTS.CA: score=10.78 buy_ready=False sector_rank=6 price=496.64 support=410.0 resistance=588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=4616358.0 spike=1.3
- SDTI.CA: score=10.09 buy_ready=False sector_rank=17 price=80.82 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=4693552.0 spike=0.27
- SEIG.CA: score=-2.9 buy_ready=False sector_rank=17 price=155.51 support=142.0 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=17.59 liquidity=699870.44 spike=0.33
- SIPC.CA: score=12.4 buy_ready=False sector_rank=17 price=4.52 support=3.73 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=37.81 liquidity=41425140.0 spike=0.7
- SKPC.CA: score=12.13 buy_ready=False sector_rank=8 price=14.63 support=14.01 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=35.68 liquidity=25712938.0 spike=0.41
- SMFR.CA: score=-2.43 buy_ready=False sector_rank=17 price=180.01 support=165.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=21.8 liquidity=1174299.88 spike=0.4
- SNFC.CA: score=6.21 buy_ready=False sector_rank=17 price=10.27 support=10.08 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=29.85 liquidity=9247708.0 spike=1.28
- SPIN.CA: score=-1.43 buy_ready=False sector_rank=18 price=14.17 support=12.0 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=32.49 liquidity=2171509.0 spike=0.38
- SPMD.CA: score=16.4 buy_ready=False sector_rank=17 price=0.33 support=0.3 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=47278180.0 spike=3.84
- SUGR.CA: score=9.46 buy_ready=False sector_rank=3 price=49.67 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=47.21 liquidity=4830152.0 spike=0.55
- SVCE.CA: score=6.4 buy_ready=False sector_rank=17 price=8.38 support=7.01 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=30.96 liquidity=24420048.0 spike=0.36
- SWDY.CA: score=15.42 buy_ready=False sector_rank=9 price=113.7 support=97.0 resistance=124.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=39.41 liquidity=73698704.0 spike=1.2
- TALM.CA: score=8.62 buy_ready=False sector_rank=6 price=19.17 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=21.88 liquidity=28615080.0 spike=1.03
- TMGH.CA: score=13.8 buy_ready=False sector_rank=12 price=81.16 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=39.04 liquidity=225989072.0 spike=0.89
- TRTO.CA: score=-2.35 buy_ready=False sector_rank=17 price=0.05 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=8224.53 spike=1.12
- UEFM.CA: score=-2.23 buy_ready=False sector_rank=17 price=447.39 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=25.87 liquidity=1365437.0 spike=0.48
- UEGC.CA: score=11.4 buy_ready=False sector_rank=17 price=1.4 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=43.12 liquidity=30625986.0 spike=0.67
- UNIP.CA: score=1.48 buy_ready=False sector_rank=17 price=0.28 support=0.25 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=27.17 liquidity=5080992.5 spike=0.63
- UNIT.CA: score=7.2 buy_ready=False sector_rank=12 price=17.0 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=43.79 liquidity=2406096.75 spike=0.64
- WCDF.CA: score=-2.93 buy_ready=False sector_rank=17 price=481.03 support=432.5 resistance=652.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=16.19 liquidity=669088.69 spike=0.29
- WKOL.CA: score=0.75 buy_ready=False sector_rank=17 price=232.17 support=218.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=27.15 liquidity=4353827.0 spike=0.57
- ZEOT.CA: score=5.93 buy_ready=False sector_rank=17 price=10.27 support=8.0 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=36.3 liquidity=3527401.25 spike=0.44
- ZMID.CA: score=6.8 buy_ready=False sector_rank=12 price=6.32 support=5.91 resistance=7.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=29.71 liquidity=48726180.0 spike=0.72

## Backtesting Lite
- CANA.CA: 180d return=2.38%, max drawdown=-36.46%, MA20>MA50 days last20=20, as_of=2026-10-26T21:00:00+00:00
- ABUK.CA: 180d return=46.07%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-26T21:00:00+00:00
- MFPC.CA: 180d return=46.78%, max drawdown=-26.33%, MA20>MA50 days last20=20, as_of=2026-10-26T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=665 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- ADIB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Dhabi Islamic Bank Egypt summary=ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26; ADIB Egypt stock approaches breakout above EGP 41; ADIB Egypt’s stock holds uptrend despite corrections
  - ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26: https://english.mubasher.info/news/4607278/ADIB-Egypt-s-consolidated-profits-leap-to-EGP-3-6bn-in-Q1-26/
  - ADIB Egypt stock approaches breakout above EGP 41: https://english.mubasher.info/news/4591391/ADIB-Egypt-stock-approaches-breakout-above-EGP-41/
  - ADIB Egypt’s stock holds uptrend despite corrections: https://english.mubasher.info/news/4562331/ADIB-Egypt-s-stock-holds-uptrend-despite-corrections/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- SPMD.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Speed Medical Co summary=Speed Medical’s stock reflects strong technical breakthrough; Speed Medical turns to losses in 9M-22; Shareholder ups stake in Speed Medical for EGP 3.5m
  - Speed Medical’s stock reflects strong technical breakthrough: https://english.mubasher.info/news/4546374/Speed-Medical-s-stock-reflects-strong-technical-breakthrough/
  - Speed Medical turns to losses in 9M-22: https://english.mubasher.info/news/4054471/Speed-Medical-turns-to-losses-in-9M-22/
  - Shareholder ups stake in Speed Medical for EGP 3.5m: https://english.mubasher.info/news/4049449/Shareholder-ups-stake-in-Speed-Medical-for-EGP-3-5m/
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/

## Warnings
- OpenRouter API error: 404
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for SPMD.CA matches the company but no source/report date was detected.
- Evidence for POUL.CA matches the company but no source/report date was detected.
