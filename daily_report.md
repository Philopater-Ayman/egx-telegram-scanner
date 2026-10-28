# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-10-28T18:27:44.193432+00:00
Generated Cairo: 2026-10-28 21:27
Run timing: target 15:30 Cairo | generated Cairo 2026-10-28 21:27 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-10-28 21:24

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 169/186
- Top sector: Industrial Goods & Construction

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, October 28
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 21.05% / above MA50 10.53%
- EGX70 regime: BEARISH / above MA20 2.7% / above MA50 2.7%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=365701504.0 spike=0.71 score=17.41
- CCAP.CA: liquidity=344863904.0 spike=0.7 score=12.89
- TMGH.CA: liquidity=267198912.0 spike=1.05 score=14.04
- NIPH.CA: liquidity=252955856.0 spike=2.11 score=5.86
- BIOC.CA: liquidity=195765248.0 spike=1.75 score=3.9

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- SPMD.CA: spike=3.9 liquidity=47986008.0 outlook=WEAK_OR_RISKY score=15 buy_ready=False
- MEPA.CA: spike=3.9 liquidity=39937228.0 outlook=WEAK_OR_RISKY score=23 buy_ready=False
- OCPH.CA: spike=2.97 liquidity=8731326.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- LCSW.CA: spike=2.89 liquidity=62739412.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CAED.CA: spike=2.88 liquidity=25437130.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #2 Banking & Financials: score=1.02 5d=-0.46% 20d=-4.53% aboveMA50=20.0%
- #3 Food, Beverages & Tobacco: score=-0.8 5d=-3.3% 20d=-5.4% aboveMA50=0.0%
- #4 Healthcare: score=-0.9 5d=-1.87% 20d=-6.44% aboveMA50=0.0%
- #5 Education: score=-1.01 5d=-4.06% 20d=-5.1% aboveMA50=0.0%
- #6 Building Materials: score=-1.03 5d=-4.95% 20d=1.2% aboveMA50=0.0%
- #7 Energy & Petrochemicals: score=-1.73 5d=-4.4% 20d=-8.58% aboveMA50=33.33%
- #8 Basic Resources & Chemicals: score=-2.04 5d=-5.75% 20d=-10.23% aboveMA50=20.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CANA.CA: BULLISH_WATCH score=98.02 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ABUK.CA: BULLISH_WATCH score=82 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=sector is not leading
- MFPC.CA: BULLISH_WATCH score=76 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=sector is not leading
- CPCI.CA: CONSTRUCTIVE score=59 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- SDTI.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- EAST.CA: CONSTRUCTIVE score=52 liquidity=TRADEABLE sector=NEUTRAL risk=below MA50; momentum is extended
- ETRS.CA: NEUTRAL score=48 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA20; below MA50; sector is not leading
- ADIB.CA: NEUTRAL score=47.02 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20; below MA50
- AJWA.CA: NEUTRAL score=47 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- EFID.CA: NEUTRAL score=46 liquidity=TRADEABLE sector=NEUTRAL risk=below MA20; below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=1.96 buy_ready=False sector_rank=17 price=208.2 support=171.02 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=5555755.0 spike=0.63
- ABUK.CA: score=21.32 buy_ready=False sector_rank=8 price=91.0 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.94 liquidity=120959632.0 spike=1.57
- ACAMD.CA: score=11.54 buy_ready=False sector_rank=17 price=1.93 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=46510740.0 spike=1.07
- ACGC.CA: score=7.02 buy_ready=False sector_rank=18 price=12.76 support=11.6 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.07 liquidity=4620187.5 spike=0.44
- ADCI.CA: score=8.62 buy_ready=False sector_rank=17 price=260.25 support=221.0 resistance=278.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.35 liquidity=3701356.0 spike=2.26
- ADIB.CA: score=18.41 buy_ready=False sector_rank=2 price=45.55 support=43.16 resistance=51.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.88 liquidity=48445388.0 spike=0.63
- ADPC.CA: score=3.16 buy_ready=False sector_rank=17 price=2.85 support=2.53 resistance=3.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=26.49 liquidity=6762979.5 spike=0.74
- AFDI.CA: score=-0.23 buy_ready=False sector_rank=17 price=42.89 support=34.8 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=23.49 liquidity=2368645.25 spike=0.56
- AFMC.CA: score=7.4 buy_ready=False sector_rank=17 price=110.09 support=94.6 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=19.69 liquidity=14249078.0 spike=0.77
- AJWA.CA: score=10.51 buy_ready=False sector_rank=17 price=200.88 support=177.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=5108502.5 spike=0.15
- ALCN.CA: score=7.37 buy_ready=False sector_rank=10 price=31.09 support=27.11 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.81 liquidity=4372904.5 spike=0.21
- ALUM.CA: score=-1.7 buy_ready=False sector_rank=17 price=17.92 support=16.02 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.87 liquidity=1903449.25 spike=0.55
- AMER.CA: score=3.86 buy_ready=False sector_rank=11 price=4.3 support=3.98 resistance=4.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78410400.0 spike=1.46
- AMES.CA: score=8.4 buy_ready=False sector_rank=17 price=32.06 support=28.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.81 liquidity=43587296.0 spike=0.75
- AMIA.CA: score=3.06 buy_ready=False sector_rank=17 price=16.87 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.47 liquidity=5664611.5 spike=0.36
- AMOC.CA: score=11.31 buy_ready=False sector_rank=7 price=13.4 support=12.55 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.79 liquidity=84789032.0 spike=0.67
- APSW.CA: score=-2.53 buy_ready=False sector_rank=17 price=7.45 support=7.1 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=7.95 liquidity=714060.25 spike=1.18
- ARAB.CA: score=12.98 buy_ready=False sector_rank=11 price=0.24 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=117753672.0 spike=1.02
- ARCC.CA: score=13.59 buy_ready=False sector_rank=6 price=63.52 support=58.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=20985062.0 spike=0.48
- AREH.CA: score=7.08 buy_ready=False sector_rank=17 price=1.04 support=0.91 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.31 liquidity=10582021.0 spike=1.34
- ASCM.CA: score=0.37 buy_ready=False sector_rank=17 price=42.27 support=38.2 resistance=59.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.97 liquidity=3974672.5 spike=0.46
- ASPI.CA: score=6.4 buy_ready=False sector_rank=17 price=0.29 support=0.27 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.52 liquidity=15288283.0 spike=0.8
- ATLC.CA: score=0.68 buy_ready=False sector_rank=15 price=4.77 support=3.93 resistance=6.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.16 liquidity=3906366.5 spike=0.52
- ATQA.CA: score=7.18 buy_ready=False sector_rank=8 price=9.09 support=8.25 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.67 liquidity=33737156.0 spike=0.64
- AXPH.CA: score=-1.69 buy_ready=False sector_rank=17 price=1347.95 support=1250.0 resistance=1359.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5752778.0 spike=1.08
- BINV.CA: score=2.89 buy_ready=False sector_rank=13 price=51.0 support=51.0 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11888244.0 spike=0.83
- BIOC.CA: score=3.9 buy_ready=False sector_rank=17 price=281.13 support=262.0 resistance=298.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=195765248.0 spike=1.75
- BTFH.CA: score=6.87 buy_ready=False sector_rank=15 price=2.25 support=2.05 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.06 liquidity=107789592.0 spike=1.05
- CAED.CA: score=6.16 buy_ready=False sector_rank=17 price=86.96 support=80.01 resistance=92.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25437130.0 spike=2.88
- CANA.CA: score=25.03 buy_ready=False sector_rank=2 price=44.88 support=38.1 resistance=48.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=45357904.0 spike=2.81
- CCAP.CA: score=12.89 buy_ready=False sector_rank=13 price=6.03 support=5.8 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=344863904.0 spike=0.7
- CCRS.CA: score=1.76 buy_ready=False sector_rank=17 price=1.59 support=1.3 resistance=2.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.77 liquidity=5360048.5 spike=0.79
- CEFM.CA: score=1.27 buy_ready=False sector_rank=17 price=115.87 support=102.2 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.92 liquidity=2926148.25 spike=1.47
- CERA.CA: score=6.4 buy_ready=False sector_rank=17 price=1.02 support=0.93 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.29 liquidity=79856320.0 spike=0.67
- CFGH.CA: score=-3.6 buy_ready=False sector_rank=17 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=9.09 liquidity=4493.69 spike=0.83
- CICH.CA: score=-2.74 buy_ready=False sector_rank=15 price=10.84 support=9.63 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.72 liquidity=486926.13 spike=0.28
- CIEB.CA: score=6.4 buy_ready=False sector_rank=2 price=22.47 support=21.35 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.94 liquidity=5993079.5 spike=0.71
- CIRA.CA: score=0.74 buy_ready=False sector_rank=5 price=34.32 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=2145980.5 spike=0.13
- CLHO.CA: score=7.64 buy_ready=False sector_rank=4 price=13.62 support=12.51 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.9 liquidity=23518924.0 spike=0.62
- CNFN.CA: score=6.18 buy_ready=False sector_rank=15 price=3.7 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.59 liquidity=4405467.5 spike=0.48
- COMI.CA: score=17.41 buy_ready=False sector_rank=2 price=120.3 support=118.06 resistance=129.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=365701504.0 spike=0.71
- COPR.CA: score=7.64 buy_ready=False sector_rank=17 price=0.4 support=0.33 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.8 liquidity=18263562.0 spike=1.12
- COSG.CA: score=2.75 buy_ready=False sector_rank=17 price=1.23 support=1.11 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.16 liquidity=6353421.0 spike=0.57
- CPCI.CA: score=11.15 buy_ready=False sector_rank=17 price=597.17 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.32 liquidity=3751810.75 spike=0.73
- CSAG.CA: score=0.19 buy_ready=False sector_rank=10 price=32.25 support=30.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.84 liquidity=3185476.25 spike=0.47
- DAPH.CA: score=6.4 buy_ready=False sector_rank=17 price=76.39 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=10046441.0 spike=0.24
- DEIN.CA: score=5.4 buy_ready=False sector_rank=17 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=-0.04 buy_ready=False sector_rank=3 price=22.44 support=20.27 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.73 liquidity=1278407.88 spike=0.39
- DSCW.CA: score=9.79 buy_ready=False sector_rank=17 price=1.47 support=1.23 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=8385212.0 spike=0.51
- DTPP.CA: score=6.4 buy_ready=False sector_rank=17 price=43.09 support=36.0 resistance=334.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=4.24 liquidity=24233930.0 spike=0.61
- EALR.CA: score=-1.01 buy_ready=False sector_rank=17 price=257.67 support=236.01 resistance=355.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.38 liquidity=2587823.5 spike=0.84
- EASB.CA: score=8.1 buy_ready=False sector_rank=17 price=6.0 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=5499382.5 spike=1.1
- EAST.CA: score=17.68 buy_ready=False sector_rank=3 price=31.98 support=27.01 resistance=31.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=45146456.0 spike=0.97
- EBSC.CA: score=5.72 buy_ready=False sector_rank=17 price=1.52 support=1.2 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.21 liquidity=5836105.0 spike=2.74
- ECAP.CA: score=-1.54 buy_ready=False sector_rank=17 price=26.49 support=24.8 resistance=31.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.39 liquidity=2055728.38 spike=0.62
- EDFM.CA: score=-2.14 buy_ready=False sector_rank=17 price=367.23 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.06 liquidity=464554.69 spike=0.4
- EEII.CA: score=7.46 buy_ready=False sector_rank=17 price=1.61 support=1.42 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.11 liquidity=10040632.0 spike=1.53
- EFIC.CA: score=7.18 buy_ready=False sector_rank=8 price=139.84 support=121.0 resistance=178.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.89 liquidity=22410272.0 spike=0.95
- EFID.CA: score=15.68 buy_ready=False sector_rank=3 price=17.71 support=16.01 resistance=19.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=36780140.0 spike=0.93
- EFIH.CA: score=12.77 buy_ready=False sector_rank=14 price=22.01 support=20.3 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.63 liquidity=36854948.0 spike=0.56
- EGAL.CA: score=8.18 buy_ready=False sector_rank=8 price=304.0 support=275.0 resistance=359.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.11 liquidity=58015552.0 spike=0.61
- EGAS.CA: score=-0.79 buy_ready=False sector_rank=7 price=46.72 support=43.0 resistance=58.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.49 liquidity=1902975.0 spike=0.39
- EGBE.CA: score=1.46 buy_ready=False sector_rank=2 price=0.51 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.0 liquidity=50712.65 spike=0.49
- EGCH.CA: score=7.18 buy_ready=False sector_rank=8 price=10.61 support=10.0 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.69 liquidity=37294228.0 spike=0.64
- EGSA.CA: score=2.9 buy_ready=False sector_rank=12 price=8.81 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=46.05 liquidity=881.0 spike=0.19
- EGTS.CA: score=6.94 buy_ready=False sector_rank=11 price=12.02 support=10.19 resistance=18.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=22.96 liquidity=12936360.0 spike=0.64
- EHDR.CA: score=2.7 buy_ready=False sector_rank=17 price=1.95 support=1.8 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=6303139.0 spike=0.68
- ELEC.CA: score=7.06 buy_ready=False sector_rank=9 price=1.49 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=26606544.0 spike=0.53
- ELKA.CA: score=10.85 buy_ready=False sector_rank=17 price=1.37 support=1.21 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=9450231.0 spike=0.73
- ELNA.CA: score=7.23 buy_ready=False sector_rank=17 price=37.78 support=33.46 resistance=39.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.13 liquidity=569312.63 spike=1.13
- ELSH.CA: score=6.4 buy_ready=False sector_rank=17 price=9.68 support=8.57 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=17438618.0 spike=0.98
- ELWA.CA: score=7.44 buy_ready=False sector_rank=17 price=1.65 support=1.43 resistance=1.66 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=40835.85 spike=0.14
- EMFD.CA: score=7.94 buy_ready=False sector_rank=11 price=11.65 support=10.6 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.06 liquidity=50407964.0 spike=0.95
- ENGC.CA: score=3.52 buy_ready=False sector_rank=17 price=33.89 support=30.54 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16408544.0 spike=1.56
- EOSB.CA: score=7.42 buy_ready=False sector_rank=17 price=1.61 support=1.56 resistance=1.72 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=16315.74 spike=0.25
- EPCO.CA: score=-1.77 buy_ready=False sector_rank=17 price=7.73 support=7.0 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.96 liquidity=1825188.88 spike=0.42
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=17 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=7.9 buy_ready=False sector_rank=12 price=123.96 support=115.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.32 liquidity=194858800.0 spike=0.71
- ETRS.CA: score=15.8 buy_ready=False sector_rank=17 price=10.4 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.48 liquidity=32295030.0 spike=2.7
- EXPA.CA: score=12.41 buy_ready=False sector_rank=2 price=13.7 support=12.0 resistance=16.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.42 liquidity=13641565.0 spike=0.39
- FAIT.CA: score=9.39 buy_ready=False sector_rank=2 price=43.07 support=40.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.64 liquidity=2961265.25 spike=1.01
- FAITA.CA: score=13.43 buy_ready=False sector_rank=2 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.8 liquidity=19377.11 spike=0.57
- FERC.CA: score=2.28 buy_ready=False sector_rank=8 price=61.02 support=57.55 resistance=61.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6799001.0 spike=2.15
- FWRY.CA: score=6.77 buy_ready=False sector_rank=14 price=17.0 support=16.45 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.19 liquidity=86885480.0 spike=0.74
- GBCO.CA: score=6.4 buy_ready=False sector_rank=20 price=23.03 support=22.02 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.75 liquidity=35172324.0 spike=0.29
- GDWA.CA: score=6.4 buy_ready=False sector_rank=17 price=0.53 support=0.48 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.89 liquidity=12663286.0 spike=0.97
- GGCC.CA: score=6.4 buy_ready=False sector_rank=17 price=0.54 support=0.49 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.75 liquidity=16410318.0 spike=0.98
- GIHD.CA: score=6.4 buy_ready=False sector_rank=17 price=39.02 support=32.1 resistance=71.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.47 liquidity=12868886.0 spike=0.92
- GMCI.CA: score=0.76 buy_ready=False sector_rank=17 price=1.48 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=558284.13 spike=1.9
- GRCA.CA: score=5.16 buy_ready=False sector_rank=17 price=26.01 support=22.57 resistance=39.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=18.79 liquidity=7561786.5 spike=1.6
- GSSC.CA: score=-3.07 buy_ready=False sector_rank=17 price=246.56 support=211.52 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=32.95 liquidity=534119.5 spike=0.47
- HDBK.CA: score=15.41 buy_ready=False sector_rank=2 price=95.42 support=83.01 resistance=112.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.19 liquidity=13159689.0 spike=0.58
- HELI.CA: score=7.94 buy_ready=False sector_rank=11 price=6.25 support=5.72 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=51079432.0 spike=0.77
- HRHO.CA: score=6.77 buy_ready=False sector_rank=15 price=23.82 support=22.8 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.88 liquidity=15806658.0 spike=0.13
- ICID.CA: score=14.9 buy_ready=False sector_rank=17 price=17.0 support=14.26 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.09 liquidity=15623790.0 spike=2.25
- IDRE.CA: score=-3.25 buy_ready=False sector_rank=17 price=34.31 support=32.1 resistance=35.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4354650.5 spike=0.78
- IFAP.CA: score=0.58 buy_ready=False sector_rank=21 price=16.46 support=15.51 resistance=19.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=4181770.25 spike=0.85
- INFI.CA: score=2.42 buy_ready=False sector_rank=17 price=114.11 support=105.5 resistance=118.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20613166.0 spike=1.01
- IRON.CA: score=5.7 buy_ready=False sector_rank=8 price=24.99 support=23.53 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=25.42 liquidity=8516766.0 spike=0.83
- ISMA.CA: score=7.52 buy_ready=False sector_rank=17 price=18.72 support=14.11 resistance=27.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.54 liquidity=11068843.0 spike=1.56
- ISMQ.CA: score=7.18 buy_ready=False sector_rank=8 price=6.6 support=5.96 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.85 liquidity=10458870.0 spike=0.65
- ISPH.CA: score=7.64 buy_ready=False sector_rank=4 price=9.88 support=9.14 resistance=12.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.34 liquidity=36077592.0 spike=0.8
- JUFO.CA: score=13.68 buy_ready=False sector_rank=3 price=23.04 support=21.01 resistance=26.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.33 liquidity=16821066.0 spike=1.0
- KABO.CA: score=6.4 buy_ready=False sector_rank=18 price=6.47 support=5.58 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.4 liquidity=21909672.0 spike=0.89
- KWIN.CA: score=-0.29 buy_ready=False sector_rank=17 price=52.04 support=44.02 resistance=82.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.21 liquidity=3311761.25 spike=0.72
- KZPC.CA: score=7.01 buy_ready=False sector_rank=17 price=12.6 support=11.56 resistance=13.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.72 liquidity=4610834.0 spike=0.63
- LCSW.CA: score=7.37 buy_ready=False sector_rank=6 price=35.58 support=33.45 resistance=35.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62739412.0 spike=2.89
- LUTS.CA: score=3.36 buy_ready=False sector_rank=17 price=0.64 support=0.58 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80302344.0 spike=1.48
- MAAL.CA: score=6.4 buy_ready=False sector_rank=17 price=6.26 support=4.88 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.55 liquidity=12476854.0 spike=1.0
- MASR.CA: score=11.4 buy_ready=False sector_rank=17 price=6.36 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=27313602.0 spike=0.55
- MBSC.CA: score=8.59 buy_ready=False sector_rank=6 price=297.69 support=262.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=42623772.0 spike=0.4
- MCQE.CA: score=7.59 buy_ready=False sector_rank=6 price=163.09 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.16 liquidity=33707800.0 spike=0.47
- MCRO.CA: score=6.64 buy_ready=False sector_rank=17 price=1.24 support=1.07 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.15 liquidity=51302912.0 spike=1.12
- MENA.CA: score=-0.87 buy_ready=False sector_rank=11 price=5.7 support=5.45 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.82 liquidity=2184852.0 spike=0.84
- MEPA.CA: score=11.4 buy_ready=False sector_rank=17 price=1.25 support=1.14 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.09 liquidity=39937228.0 spike=3.9
- MFPC.CA: score=19.48 buy_ready=False sector_rank=8 price=46.0 support=40.66 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.09 liquidity=79438808.0 spike=1.65
- MFSC.CA: score=-2.49 buy_ready=False sector_rank=17 price=32.79 support=28.55 resistance=47.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=22.52 liquidity=1113089.38 spike=0.51
- MHOT.CA: score=-2.6 buy_ready=False sector_rank=19 price=14.03 support=13.0 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.47 liquidity=1004460.94 spike=0.12
- MICH.CA: score=5.9 buy_ready=False sector_rank=17 price=40.57 support=35.5 resistance=44.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.12 liquidity=3500144.25 spike=0.47
- MILS.CA: score=5.63 buy_ready=False sector_rank=17 price=118.68 support=96.02 resistance=201.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=20.26 liquidity=8974918.0 spike=1.13
- MIPH.CA: score=5.55 buy_ready=False sector_rank=4 price=749.82 support=610.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.57 liquidity=1909503.0 spike=0.52
- MOED.CA: score=7.3 buy_ready=False sector_rank=17 price=0.46 support=0.39 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.93 liquidity=18518828.0 spike=1.45
- MOIL.CA: score=3.42 buy_ready=False sector_rank=7 price=0.65 support=0.6 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=108685.12 spike=0.5
- MOIN.CA: score=1.62 buy_ready=False sector_rank=17 price=27.96 support=25.7 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.78 liquidity=4221703.0 spike=0.5
- MOSC.CA: score=5.68 buy_ready=False sector_rank=17 price=241.01 support=198.01 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.39 liquidity=6616371.5 spike=1.83
- MPCI.CA: score=2.88 buy_ready=False sector_rank=17 price=289.43 support=271.01 resistance=296.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116727784.0 spike=1.24
- MPCO.CA: score=6.4 buy_ready=False sector_rank=21 price=1.78 support=1.55 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=49920236.0 spike=0.57
- MPRC.CA: score=6.4 buy_ready=False sector_rank=17 price=31.3 support=27.0 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.37 liquidity=10297716.0 spike=0.66
- MTIE.CA: score=11.07 buy_ready=False sector_rank=20 price=7.02 support=6.05 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.56 liquidity=9668183.0 spike=0.46
- NAHO.CA: score=2.41 buy_ready=False sector_rank=17 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=38.1 liquidity=12526.98 spike=0.72
- NCCW.CA: score=6.4 buy_ready=False sector_rank=17 price=4.99 support=4.05 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.49 liquidity=12040068.0 spike=0.58
- NEDA.CA: score=0.24 buy_ready=False sector_rank=17 price=2.6 support=2.47 resistance=2.71 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=257215.39 spike=1.29
- NHPS.CA: score=0.66 buy_ready=False sector_rank=17 price=54.07 support=50.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.16 liquidity=4263670.5 spike=0.51
- NINH.CA: score=4.92 buy_ready=False sector_rank=17 price=14.8 support=14.21 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22008104.0 spike=2.26
- NIPH.CA: score=5.86 buy_ready=False sector_rank=4 price=254.25 support=240.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=252955856.0 spike=2.11
- OBRI.CA: score=2.61 buy_ready=False sector_rank=17 price=21.64 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.51 liquidity=6207410.0 spike=0.42
- OCDI.CA: score=11.98 buy_ready=False sector_rank=11 price=23.55 support=21.0 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.37 liquidity=37808704.0 spike=1.02
- OCPH.CA: score=5.07 buy_ready=False sector_rank=17 price=180.47 support=174.01 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8731326.0 spike=2.97
- ODIN.CA: score=-1.52 buy_ready=False sector_rank=17 price=1.92 support=1.7 resistance=2.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.95 liquidity=2075279.88 spike=0.37
- OFH.CA: score=6.4 buy_ready=False sector_rank=17 price=0.69 support=0.61 resistance=0.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.66 liquidity=21400284.0 spike=0.59
- OIH.CA: score=7.89 buy_ready=False sector_rank=13 price=1.61 support=1.5 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.85 liquidity=30397446.0 spike=0.56
- OLFI.CA: score=8.68 buy_ready=False sector_rank=3 price=18.91 support=17.86 resistance=22.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.61 liquidity=11602744.0 spike=0.78
- ORAS.CA: score=7.6 buy_ready=False sector_rank=1 price=818.54 support=813.0 resistance=834.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=124457496.0 spike=1.0
- ORHD.CA: score=8.94 buy_ready=False sector_rank=11 price=9.52 support=8.5 resistance=12.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.47 liquidity=58062384.0 spike=0.48
- ORWE.CA: score=6.4 buy_ready=False sector_rank=18 price=23.1 support=22.62 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=22.45 liquidity=33562956.0 spike=0.87
- PHAR.CA: score=9.08 buy_ready=False sector_rank=4 price=98.09 support=90.2 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.68 liquidity=73187584.0 spike=1.22
- PHDC.CA: score=6.94 buy_ready=False sector_rank=11 price=11.46 support=11.0 resistance=13.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.56 liquidity=57419352.0 spike=0.62
- PHTV.CA: score=4.11 buy_ready=False sector_rank=17 price=325.14 support=300.0 resistance=360.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.93 liquidity=1185748.25 spike=1.26
- POUL.CA: score=15.68 buy_ready=False sector_rank=3 price=9.45 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=37295632.0 spike=0.65
- PRCL.CA: score=14.15 buy_ready=False sector_rank=6 price=19.57 support=16.65 resistance=27.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.37 liquidity=16355228.0 spike=1.78
- PRDC.CA: score=13.94 buy_ready=False sector_rank=11 price=6.02 support=5.08 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.34 liquidity=15322491.0 spike=0.44
- PRMH.CA: score=2.98 buy_ready=False sector_rank=17 price=1.84 support=1.7 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.56 liquidity=1580662.63 spike=0.53
- RACC.CA: score=0.18 buy_ready=False sector_rank=17 price=7.13 support=6.1 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.07 liquidity=3781513.25 spike=0.52
- RAKT.CA: score=-1.16 buy_ready=False sector_rank=17 price=21.39 support=20.26 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=29.5 liquidity=436790.13 spike=1.0
- RAYA.CA: score=6.54 buy_ready=False sector_rank=16 price=5.46 support=5.02 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.33 liquidity=9860517.0 spike=0.44
- RMDA.CA: score=13.64 buy_ready=False sector_rank=4 price=5.07 support=4.5 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=17904834.0 spike=0.71
- ROTO.CA: score=3.32 buy_ready=False sector_rank=17 price=29.0 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.75 liquidity=6917249.0 spike=0.89
- RREI.CA: score=8.04 buy_ready=False sector_rank=17 price=2.39 support=1.96 resistance=4.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=16.06 liquidity=15891842.0 spike=1.82
- RTVC.CA: score=3.3 buy_ready=False sector_rank=17 price=2.87 support=2.87 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.82 liquidity=4916836.0 spike=1.99
- RUBX.CA: score=7.4 buy_ready=False sector_rank=17 price=12.47 support=10.51 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.3 liquidity=38358816.0 spike=0.45
- SAUD.CA: score=4.72 buy_ready=False sector_rank=2 price=20.76 support=19.3 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.44 liquidity=3312608.5 spike=0.29
- SCEM.CA: score=13.59 buy_ready=False sector_rank=6 price=82.91 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.68 liquidity=27039008.0 spike=0.46
- SCFM.CA: score=-0.73 buy_ready=False sector_rank=17 price=193.97 support=153.02 resistance=264.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=25.27 liquidity=2354938.25 spike=1.26
- SCTS.CA: score=11.25 buy_ready=False sector_rank=5 price=495.89 support=410.0 resistance=588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=4897271.0 spike=1.38
- SDTI.CA: score=11.77 buy_ready=False sector_rank=17 price=80.4 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=6369093.0 spike=0.37
- SEIG.CA: score=-2.88 buy_ready=False sector_rank=17 price=155.34 support=142.0 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=17.59 liquidity=722829.19 spike=0.34
- SIPC.CA: score=12.4 buy_ready=False sector_rank=17 price=4.53 support=3.73 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.81 liquidity=42011224.0 spike=0.71
- SKPC.CA: score=12.18 buy_ready=False sector_rank=8 price=14.64 support=14.01 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.68 liquidity=27240806.0 spike=0.44
- SMFR.CA: score=-2.34 buy_ready=False sector_rank=17 price=180.06 support=165.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.8 liquidity=1264604.0 spike=0.43
- SNFC.CA: score=7.28 buy_ready=False sector_rank=17 price=10.38 support=10.08 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.85 liquidity=10410843.0 spike=1.44
- SPIN.CA: score=-1.39 buy_ready=False sector_rank=18 price=14.17 support=12.0 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.49 liquidity=2213817.0 spike=0.39
- SPMD.CA: score=16.4 buy_ready=False sector_rank=17 price=0.34 support=0.3 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=47986008.0 spike=3.9
- SUGR.CA: score=9.93 buy_ready=False sector_rank=3 price=49.58 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.21 liquidity=5251572.0 spike=0.6
- SVCE.CA: score=6.4 buy_ready=False sector_rank=17 price=8.38 support=7.01 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.96 liquidity=26312728.0 spike=0.39
- SWDY.CA: score=15.64 buy_ready=False sector_rank=9 price=113.05 support=97.0 resistance=124.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.41 liquidity=79069552.0 spike=1.29
- TALM.CA: score=8.78 buy_ready=False sector_rank=5 price=19.09 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.88 liquidity=30366130.0 spike=1.09
- TMGH.CA: score=14.04 buy_ready=False sector_rank=11 price=81.21 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.04 liquidity=267198912.0 spike=1.05
- TRTO.CA: score=-2.35 buy_ready=False sector_rank=17 price=0.05 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-26T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=8224.53 spike=1.12
- UEFM.CA: score=-2.15 buy_ready=False sector_rank=17 price=446.22 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.87 liquidity=1451269.25 spike=0.51
- UEGC.CA: score=11.4 buy_ready=False sector_rank=17 price=1.4 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.12 liquidity=33296074.0 spike=0.73
- UNIP.CA: score=1.89 buy_ready=False sector_rank=17 price=0.28 support=0.25 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.17 liquidity=5492327.0 spike=0.68
- UNIT.CA: score=7.4 buy_ready=False sector_rank=11 price=17.0 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=43.79 liquidity=2451571.75 spike=0.66
- WCDF.CA: score=-2.93 buy_ready=False sector_rank=17 price=481.06 support=432.5 resistance=652.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.19 liquidity=671028.69 spike=0.29
- WKOL.CA: score=1.12 buy_ready=False sector_rank=17 price=232.95 support=218.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.15 liquidity=4718038.0 spike=0.62
- ZEOT.CA: score=6.13 buy_ready=False sector_rank=17 price=10.28 support=8.0 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.3 liquidity=3730954.5 spike=0.46
- ZMID.CA: score=6.94 buy_ready=False sector_rank=11 price=6.32 support=5.91 resistance=7.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.71 liquidity=52918836.0 spike=0.78

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
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..

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
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
