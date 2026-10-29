# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-10-29T18:37:19.085862+00:00
Generated Cairo: 2026-10-29 21:37
Run timing: target 15:30 Cairo | generated Cairo 2026-10-29 21:37 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-10-29 21:34

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 164/185
- Top sector: Industrial Goods & Construction

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, October 29
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.53% / above MA50 10.53%
- EGX70 regime: BEARISH / above MA20 10.26% / above MA50 5.13%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=523792672.0 spike=1.02 score=15.06
- CCAP.CA: liquidity=510474304.0 spike=1.05 score=12.5
- BTFH.CA: liquidity=370839392.0 spike=3.59 score=8.5
- TMGH.CA: liquidity=283576256.0 spike=1.1 score=11.9
- FWRY.CA: liquidity=238786320.0 spike=1.98 score=9.1

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- EDFM.CA: spike=5.48 liquidity=5882044.5 outlook=WEAK_OR_RISKY score=22 buy_ready=False
- BTFH.CA: spike=3.59 liquidity=370839392.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RTVC.CA: spike=3.45 liquidity=8683089.0 outlook=WEAK_OR_RISKY score=17 buy_ready=False
- MILS.CA: spike=3.17 liquidity=23889248.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SCFM.CA: spike=3.17 liquidity=5657597.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #2 Banking & Financials: score=0.04 5d=-2.32% 20d=-5.23% aboveMA50=20.0%
- #3 Building Materials: score=-0.01 5d=-4.1% 20d=0.14% aboveMA50=16.67%
- #4 Energy & Petrochemicals: score=-0.07 5d=-2.42% 20d=-9.28% aboveMA50=33.33%
- #5 Healthcare: score=-0.34 5d=-2.58% 20d=-7.08% aboveMA50=0.0%
- #6 Industrial Goods & Cables: score=-0.69 5d=-4.63% 20d=-6.58% aboveMA50=0.0%
- #7 Food, Beverages & Tobacco: score=-1.03 5d=-3.87% 20d=-6.67% aboveMA50=14.29%
- #8 Education: score=-1.12 5d=-2.55% 20d=-8.73% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- LCSW.CA: BULLISH_WATCH score=83 liquidity=TRADEABLE sector=NEUTRAL risk=far above support
- AMOC.CA: BULLISH_WATCH score=71 liquidity=ACCUMULATION_SPIKE sector=NEUTRAL risk=overheated RSI
- ABUK.CA: BULLISH_WATCH score=70 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA20; sector is not leading
- CANA.CA: CONSTRUCTIVE score=69.04 liquidity=TRADEABLE sector=LEADING risk=far above support; close to resistance
- CPCI.CA: CONSTRUCTIVE score=66 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=far above support; close to resistance; sector is not leading
- AJWA.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- ICID.CA: CONSTRUCTIVE score=61 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; far above support; sector is not leading
- SDTI.CA: CONSTRUCTIVE score=56 liquidity=TRADEABLE sector=LAGGING risk=weak RSI; sector is not leading
- RMDA.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=NEUTRAL risk=below MA50
- SUGR.CA: CONSTRUCTIVE score=53 liquidity=ACCUMULATION_SPIKE sector=NEUTRAL risk=below MA20; below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CEFM.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=8.41 buy_ready=False sector_rank=11 price=216.33 support=171.02 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.7 liquidity=15391429.0 spike=1.75
- ABUK.CA: score=19.94 buy_ready=False sector_rank=15 price=88.22 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=180504400.0 spike=2.23
- ACAMD.CA: score=11.91 buy_ready=False sector_rank=11 price=1.94 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=35138768.0 spike=0.81
- ACGC.CA: score=3.73 buy_ready=False sector_rank=17 price=13.3 support=11.6 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.08 liquidity=6333339.0 spike=0.62
- ADCI.CA: score=10.58 buy_ready=False sector_rank=11 price=271.18 support=221.0 resistance=278.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.98 liquidity=3553720.0 spike=2.06
- ADIB.CA: score=18.02 buy_ready=False sector_rank=2 price=46.18 support=43.16 resistance=50.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.28 liquidity=37331596.0 spike=0.48
- ADPC.CA: score=3.45 buy_ready=False sector_rank=11 price=3.01 support=2.8 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11664791.0 spike=1.27
- AFDI.CA: score=-0.12 buy_ready=False sector_rank=11 price=42.96 support=34.8 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.31 liquidity=1974462.25 spike=0.47
- AFMC.CA: score=6.51 buy_ready=False sector_rank=11 price=123.83 support=109.91 resistance=127.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47868604.0 spike=2.8
- AJWA.CA: score=16.32 buy_ready=False sector_rank=11 price=206.01 support=177.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.47 liquidity=8407940.0 spike=0.24
- ALCN.CA: score=8.47 buy_ready=False sector_rank=14 price=31.57 support=27.11 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.74 liquidity=5866459.0 spike=0.29
- ALUM.CA: score=-1.74 buy_ready=False sector_rank=11 price=18.16 support=16.02 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.58 liquidity=1351827.25 spike=0.41
- AMER.CA: score=12.7 buy_ready=False sector_rank=12 price=4.34 support=3.21 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.92 liquidity=41307032.0 spike=0.74
- AMES.CA: score=8.91 buy_ready=False sector_rank=11 price=33.03 support=28.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.18 liquidity=56845680.0 spike=0.99
- AMIA.CA: score=1.34 buy_ready=False sector_rank=11 price=17.2 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.7 liquidity=3428164.0 spike=0.22
- AMOC.CA: score=20.41 buy_ready=False sector_rank=4 price=14.0 support=12.55 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=216560544.0 spike=1.72
- APSW.CA: score=-2.1 buy_ready=False sector_rank=11 price=7.45 support=7.1 resistance=8.92 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=24.35 liquidity=714663.58 spike=1.14
- ARAB.CA: score=12.7 buy_ready=False sector_rank=12 price=0.24 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=63704276.0 spike=0.53
- ARCC.CA: score=10.0 buy_ready=False sector_rank=3 price=64.0 support=58.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.18 liquidity=16904968.0 spike=0.38
- AREH.CA: score=3.05 buy_ready=False sector_rank=11 price=1.06 support=0.91 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.81 liquidity=6140925.5 spike=0.76
- ASCM.CA: score=0.18 buy_ready=False sector_rank=11 price=43.49 support=38.2 resistance=59.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.02 liquidity=3270743.25 spike=0.38
- ASPI.CA: score=6.91 buy_ready=False sector_rank=11 price=0.3 support=0.27 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.6 liquidity=16016507.0 spike=0.83
- ATLC.CA: score=1.97 buy_ready=False sector_rank=9 price=4.96 support=3.93 resistance=6.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.23 liquidity=4473823.5 spike=0.59
- ATQA.CA: score=6.48 buy_ready=False sector_rank=15 price=9.02 support=8.25 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.65 liquidity=32967454.0 spike=0.62
- AXPH.CA: score=9.22 buy_ready=False sector_rank=11 price=1391.85 support=1135.0 resistance=1588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.01 liquidity=4309254.5 spike=0.83
- BINV.CA: score=-1.23 buy_ready=False sector_rank=18 price=52.52 support=51.0 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=22.62 liquidity=1369178.13 spike=0.1
- BIOC.CA: score=13.25 buy_ready=False sector_rank=11 price=290.7 support=212.05 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=134294560.0 spike=1.17
- BTFH.CA: score=8.5 buy_ready=False sector_rank=9 price=2.37 support=2.22 resistance=2.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=370839392.0 spike=3.59
- CAED.CA: score=8.45 buy_ready=False sector_rank=11 price=89.66 support=64.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.62 liquidity=11846666.0 spike=1.27
- CANA.CA: score=21.02 buy_ready=False sector_rank=2 price=46.5 support=38.1 resistance=46.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.88 liquidity=15903828.0 spike=0.9
- CCAP.CA: score=12.5 buy_ready=False sector_rank=18 price=6.1 support=5.8 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.5 liquidity=510474304.0 spike=1.05
- CCRS.CA: score=3.18 buy_ready=False sector_rank=11 price=1.66 support=1.3 resistance=2.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.71 liquidity=6272891.5 spike=0.94
- CERA.CA: score=6.91 buy_ready=False sector_rank=11 price=1.06 support=0.93 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.64 liquidity=85455168.0 spike=0.71
- CFGH.CA: score=-3.09 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=10.0 liquidity=0.0 spike=0.0
- CICH.CA: score=2.57 buy_ready=False sector_rank=9 price=10.61 support=9.63 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=3209438.5 spike=1.93
- CIEB.CA: score=8.02 buy_ready=False sector_rank=2 price=22.54 support=21.35 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=3000152.25 spike=0.35
- CIRA.CA: score=8.75 buy_ready=False sector_rank=8 price=35.9 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.14 liquidity=17156732.0 spike=1.1
- CLHO.CA: score=7.86 buy_ready=False sector_rank=5 price=13.57 support=12.51 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.19 liquidity=12331357.0 spike=0.33
- CNFN.CA: score=10.92 buy_ready=False sector_rank=9 price=3.73 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.07 liquidity=8415516.0 spike=0.91
- COMI.CA: score=15.06 buy_ready=False sector_rank=2 price=119.84 support=118.06 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=523792672.0 spike=1.02
- COPR.CA: score=7.91 buy_ready=False sector_rank=11 price=0.4 support=0.33 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.22 liquidity=10001230.0 spike=0.6
- COSG.CA: score=4.94 buy_ready=False sector_rank=11 price=1.28 support=1.11 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.83 liquidity=8036845.0 spike=0.73
- CPCI.CA: score=16.91 buy_ready=False sector_rank=11 price=613.48 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.35 liquidity=7841862.5 spike=1.58
- CSAG.CA: score=5.85 buy_ready=False sector_rank=14 price=33.8 support=30.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.25 liquidity=7883623.5 spike=1.18
- DAPH.CA: score=6.91 buy_ready=False sector_rank=11 price=79.04 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.83 liquidity=14463327.0 spike=0.36
- DEIN.CA: score=5.91 buy_ready=False sector_rank=11 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=4.39 buy_ready=False sector_rank=7 price=22.65 support=20.27 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=1801969.63 spike=0.59
- DSCW.CA: score=9.41 buy_ready=False sector_rank=11 price=1.5 support=1.23 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.06 liquidity=7503284.0 spike=0.47
- DTPP.CA: score=6.91 buy_ready=False sector_rank=11 price=44.05 support=36.0 resistance=334.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.47 liquidity=18671712.0 spike=0.48
- EALR.CA: score=1.58 buy_ready=False sector_rank=11 price=265.37 support=236.01 resistance=355.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.62 liquidity=4048173.75 spike=1.31
- EASB.CA: score=7.74 buy_ready=False sector_rank=11 price=6.08 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=4834365.0 spike=0.95
- EAST.CA: score=17.59 buy_ready=False sector_rank=7 price=32.17 support=27.01 resistance=32.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.24 liquidity=27131802.0 spike=0.59
- EBSC.CA: score=10.21 buy_ready=False sector_rank=11 price=1.48 support=1.2 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.11 liquidity=5538682.5 spike=2.38
- ECAP.CA: score=-1.37 buy_ready=False sector_rank=11 price=26.78 support=24.8 resistance=31.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.8 liquidity=1720368.88 spike=0.52
- EDFM.CA: score=8.79 buy_ready=False sector_rank=11 price=376.05 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.8 liquidity=5882044.5 spike=5.48
- EEII.CA: score=6.61 buy_ready=False sector_rank=11 price=1.66 support=1.42 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.11 liquidity=9000725.0 spike=1.35
- EFIC.CA: score=9.74 buy_ready=False sector_rank=15 price=141.76 support=121.0 resistance=178.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.76 liquidity=8260322.5 spike=0.35
- EFID.CA: score=14.59 buy_ready=False sector_rank=7 price=17.8 support=16.01 resistance=19.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=30930442.0 spike=0.77
- EFIH.CA: score=8.14 buy_ready=False sector_rank=10 price=22.57 support=20.3 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.44 liquidity=40891140.0 spike=0.61
- EGAL.CA: score=7.48 buy_ready=False sector_rank=15 price=303.08 support=275.0 resistance=359.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.15 liquidity=35997684.0 spike=0.37
- EGAS.CA: score=0.37 buy_ready=False sector_rank=4 price=46.96 support=43.0 resistance=58.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.37 liquidity=2394160.5 spike=0.5
- EGBE.CA: score=6.07 buy_ready=False sector_rank=2 price=0.51 support=0.47 resistance=0.54 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=37.38 liquidity=51331.5 spike=0.49
- EGCH.CA: score=6.48 buy_ready=False sector_rank=15 price=10.55 support=10.0 resistance=13.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.91 liquidity=42394540.0 spike=0.75
- EGSA.CA: score=2.62 buy_ready=False sector_rank=13 price=8.81 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=46.05 liquidity=1066.01 spike=0.22
- EGTS.CA: score=6.76 buy_ready=False sector_rank=12 price=12.37 support=10.19 resistance=17.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.32 liquidity=20934914.0 spike=1.03
- EHDR.CA: score=4.95 buy_ready=False sector_rank=11 price=2.04 support=1.8 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.34 liquidity=8042625.0 spike=0.88
- ELEC.CA: score=7.72 buy_ready=False sector_rank=6 price=1.52 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=27920232.0 spike=0.56
- ELKA.CA: score=3.65 buy_ready=False sector_rank=11 price=1.44 support=1.36 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17902266.0 spike=1.37
- ELNA.CA: score=7.67 buy_ready=False sector_rank=11 price=37.78 support=33.46 resistance=39.99 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=70.13 liquidity=564433.18 spike=1.1
- ELSH.CA: score=6.91 buy_ready=False sector_rank=11 price=10.15 support=8.57 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.86 liquidity=12098331.0 spike=0.66
- ELWA.CA: score=6.73 buy_ready=False sector_rank=11 price=1.57 support=1.43 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=326845.75 spike=1.25
- EMFD.CA: score=7.7 buy_ready=False sector_rank=12 price=11.9 support=10.6 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=29551242.0 spike=0.55
- ENGC.CA: score=4.97 buy_ready=False sector_rank=11 price=35.98 support=33.05 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21410170.0 spike=2.03
- EOSB.CA: score=9.3 buy_ready=False sector_rank=11 price=1.61 support=1.56 resistance=1.72 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=114907.31 spike=1.64
- EPCO.CA: score=-0.45 buy_ready=False sector_rank=11 price=7.87 support=7.0 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.48 liquidity=2639534.75 spike=0.61
- EPPK.CA: score=-6.67 buy_ready=False sector_rank=11 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=7.62 buy_ready=False sector_rank=13 price=120.34 support=115.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.13 liquidity=193248608.0 spike=0.7
- ETRS.CA: score=15.73 buy_ready=False sector_rank=11 price=10.4 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=18289108.0 spike=1.41
- EXPA.CA: score=7.18 buy_ready=False sector_rank=2 price=14.03 support=12.0 resistance=16.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.62 liquidity=5165397.0 spike=0.15
- FAIT.CA: score=7.8 buy_ready=False sector_rank=2 price=43.34 support=40.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.34 liquidity=1788643.88 spike=0.6
- FAITA.CA: score=13.02 buy_ready=False sector_rank=2 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=6660.08 spike=0.2
- FERC.CA: score=2.05 buy_ready=False sector_rank=15 price=62.94 support=53.57 resistance=77.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.75 liquidity=4771424.0 spike=1.4
- FWRY.CA: score=9.1 buy_ready=False sector_rank=10 price=16.98 support=16.45 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.48 liquidity=238786320.0 spike=1.98
- GBCO.CA: score=6.4 buy_ready=False sector_rank=20 price=23.07 support=22.02 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.01 liquidity=34933672.0 spike=0.29
- GDWA.CA: score=4.49 buy_ready=False sector_rank=11 price=0.56 support=0.53 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23055252.0 spike=1.79
- GGCC.CA: score=6.91 buy_ready=False sector_rank=11 price=0.55 support=0.49 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.21 liquidity=12869852.0 spike=0.76
- GIHD.CA: score=6.91 buy_ready=False sector_rank=11 price=40.18 support=32.1 resistance=68.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.81 liquidity=10784537.0 spike=0.79
- GMCI.CA: score=-0.84 buy_ready=False sector_rank=11 price=1.41 support=1.45 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=510854.38 spike=1.87
- GRCA.CA: score=4.16 buy_ready=False sector_rank=11 price=26.24 support=22.57 resistance=39.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.19 liquidity=5152613.0 spike=1.05
- GSSC.CA: score=-2.29 buy_ready=False sector_rank=11 price=255.37 support=211.52 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.97 liquidity=801389.31 spike=0.77
- HDBK.CA: score=15.02 buy_ready=False sector_rank=2 price=97.1 support=83.01 resistance=112.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=20301224.0 spike=0.9
- HELI.CA: score=8.04 buy_ready=False sector_rank=12 price=6.42 support=5.72 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.01 liquidity=78489992.0 spike=1.17
- HRHO.CA: score=7.5 buy_ready=False sector_rank=9 price=23.57 support=22.8 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.7 liquidity=31309932.0 spike=0.26
- ICID.CA: score=12.41 buy_ready=False sector_rank=11 price=17.71 support=14.26 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=4504115.0 spike=0.61
- IDRE.CA: score=3.63 buy_ready=False sector_rank=11 price=36.58 support=33.3 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9363763.0 spike=1.68
- IFAP.CA: score=0.59 buy_ready=False sector_rank=21 price=16.75 support=15.51 resistance=19.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.18 liquidity=4190435.0 spike=0.86
- INFI.CA: score=11.56 buy_ready=False sector_rank=11 price=115.02 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.91 liquidity=8652222.0 spike=0.42
- IRON.CA: score=6.48 buy_ready=False sector_rank=15 price=24.57 support=23.53 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.06 liquidity=10121224.0 spike=0.97
- ISMA.CA: score=6.21 buy_ready=False sector_rank=11 price=19.15 support=14.11 resistance=27.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.88 liquidity=8819695.0 spike=1.24
- ISMQ.CA: score=5.98 buy_ready=False sector_rank=15 price=6.65 support=5.96 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.43 liquidity=9503390.0 spike=0.61
- ISPH.CA: score=8.4 buy_ready=False sector_rank=5 price=9.94 support=9.14 resistance=12.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.91 liquidity=57145944.0 spike=1.27
- JUFO.CA: score=14.29 buy_ready=False sector_rank=7 price=23.24 support=21.01 resistance=26.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=31361836.0 spike=1.85
- KABO.CA: score=6.4 buy_ready=False sector_rank=17 price=6.55 support=5.58 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.0 liquidity=10903609.0 spike=0.43
- KWIN.CA: score=2.84 buy_ready=False sector_rank=11 price=54.97 support=51.83 resistance=57.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8290974.0 spike=1.82
- KZPC.CA: score=7.5 buy_ready=False sector_rank=11 price=12.87 support=11.56 resistance=13.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.59 liquidity=4593706.5 spike=0.66
- LCSW.CA: score=24.94 buy_ready=False sector_rank=3 price=36.47 support=28.0 resistance=35.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.95 liquidity=36325292.0 spike=1.47
- LUTS.CA: score=7.67 buy_ready=False sector_rank=11 price=0.66 support=0.47 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=74776976.0 spike=1.38
- MAAL.CA: score=3.03 buy_ready=False sector_rank=11 price=6.9 support=6.25 resistance=6.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13236181.0 spike=1.06
- MASR.CA: score=4.55 buy_ready=False sector_rank=11 price=6.93 support=6.27 resistance=6.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87741144.0 spike=1.82
- MBSC.CA: score=10.0 buy_ready=False sector_rank=3 price=301.98 support=262.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.38 liquidity=40152420.0 spike=0.38
- MCQE.CA: score=9.0 buy_ready=False sector_rank=3 price=166.73 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.04 liquidity=31174952.0 spike=0.43
- MCRO.CA: score=7.41 buy_ready=False sector_rank=11 price=1.32 support=1.07 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.94 liquidity=57396896.0 spike=1.25
- MENA.CA: score=-2.77 buy_ready=False sector_rank=12 price=5.62 support=5.45 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.81 liquidity=528996.5 spike=0.2
- MEPA.CA: score=10.71 buy_ready=False sector_rank=11 price=1.28 support=1.14 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.35 liquidity=34465512.0 spike=2.9
- MFPC.CA: score=14.64 buy_ready=False sector_rank=15 price=44.97 support=40.66 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=54298256.0 spike=1.08
- MFSC.CA: score=-1.49 buy_ready=False sector_rank=11 price=33.42 support=28.55 resistance=47.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.52 liquidity=1601968.38 spike=0.75
- MHOT.CA: score=0.56 buy_ready=False sector_rank=19 price=14.4 support=13.0 resistance=16.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.81 liquidity=4163955.5 spike=0.54
- MICH.CA: score=5.22 buy_ready=False sector_rank=11 price=40.54 support=35.5 resistance=44.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.63 liquidity=2316235.5 spike=0.33
- MILS.CA: score=7.25 buy_ready=False sector_rank=11 price=125.13 support=117.0 resistance=132.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23889248.0 spike=3.17
- MIPH.CA: score=5.89 buy_ready=False sector_rank=5 price=750.05 support=610.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.39 liquidity=2026222.38 spike=0.56
- MOED.CA: score=7.09 buy_ready=False sector_rank=11 price=0.47 support=0.39 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.81 liquidity=14314264.0 spike=1.09
- MOIL.CA: score=4.01 buy_ready=False sector_rank=4 price=0.65 support=0.6 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=35.81 liquidity=34772.43 spike=0.17
- MOIN.CA: score=2.02 buy_ready=False sector_rank=11 price=28.74 support=25.7 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.98 liquidity=4116968.5 spike=0.49
- MOSC.CA: score=2.77 buy_ready=False sector_rank=11 price=239.22 support=198.01 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.22 liquidity=858918.81 spike=0.23
- MPCI.CA: score=4.57 buy_ready=False sector_rank=11 price=323.81 support=310.1 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=172614320.0 spike=1.83
- MPCO.CA: score=6.4 buy_ready=False sector_rank=21 price=1.8 support=1.55 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.07 liquidity=49966132.0 spike=0.59
- MPRC.CA: score=1.71 buy_ready=False sector_rank=11 price=32.07 support=27.0 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.55 liquidity=4802243.0 spike=0.31
- MTIE.CA: score=9.96 buy_ready=False sector_rank=20 price=7.0 support=6.05 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=8563625.0 spike=0.41
- NAHO.CA: score=2.91 buy_ready=False sector_rank=11 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=38.1 liquidity=4186.11 spike=0.24
- NCCW.CA: score=6.91 buy_ready=False sector_rank=11 price=5.19 support=4.05 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.12 liquidity=17789368.0 spike=0.92
- NEDA.CA: score=1.43 buy_ready=False sector_rank=11 price=2.47 support=2.47 resistance=2.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=386838.53 spike=2.07
- NHPS.CA: score=4.46 buy_ready=False sector_rank=11 price=56.02 support=50.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.51 liquidity=7552152.0 spike=0.92
- NINH.CA: score=5.08 buy_ready=False sector_rank=11 price=15.08 support=12.36 resistance=20.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.01 liquidity=8169459.0 spike=0.82
- NIPH.CA: score=4.9 buy_ready=False sector_rank=5 price=280.8 support=263.0 resistance=305.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=189083840.0 spike=1.52
- OBRI.CA: score=2.91 buy_ready=False sector_rank=11 price=22.93 support=21.21 resistance=23.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13128748.0 spike=0.91
- OCDI.CA: score=12.7 buy_ready=False sector_rank=12 price=23.71 support=21.0 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=14505771.0 spike=0.41
- OCPH.CA: score=4.8 buy_ready=False sector_rank=11 price=184.64 support=147.96 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=5995255.0 spike=1.95
- ODIN.CA: score=6.99 buy_ready=False sector_rank=11 price=2.09 support=1.92 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16644866.0 spike=3.04
- OFH.CA: score=7.11 buy_ready=False sector_rank=11 price=0.7 support=0.61 resistance=0.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.07 liquidity=9205805.0 spike=0.26
- OIH.CA: score=7.4 buy_ready=False sector_rank=18 price=1.66 support=1.5 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=27498930.0 spike=0.55
- OLFI.CA: score=2.25 buy_ready=False sector_rank=7 price=19.13 support=17.86 resistance=22.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.67 liquidity=4665773.0 spike=0.31
- ORAS.CA: score=7.6 buy_ready=False sector_rank=1 price=822.03 support=814.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=122678872.0 spike=1.0
- ORHD.CA: score=8.7 buy_ready=False sector_rank=12 price=9.88 support=8.5 resistance=12.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.84 liquidity=89574592.0 spike=0.75
- ORWE.CA: score=7.4 buy_ready=False sector_rank=17 price=23.33 support=22.62 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.02 liquidity=21168242.0 spike=0.54
- PHAR.CA: score=11.56 buy_ready=False sector_rank=5 price=102.6 support=90.2 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.1 liquidity=132469352.0 spike=2.35
- PHDC.CA: score=6.7 buy_ready=False sector_rank=12 price=11.4 support=11.0 resistance=13.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=28.99 liquidity=45144488.0 spike=0.49
- PHTV.CA: score=-1.77 buy_ready=False sector_rank=11 price=319.1 support=300.0 resistance=360.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=34.94 liquidity=325967.59 spike=0.34
- POUL.CA: score=14.59 buy_ready=False sector_rank=7 price=9.55 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=37747928.0 spike=0.66
- PRCL.CA: score=11.4 buy_ready=False sector_rank=3 price=19.98 support=16.65 resistance=27.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.87 liquidity=21394918.0 spike=2.2
- PRDC.CA: score=8.7 buy_ready=False sector_rank=12 price=6.16 support=5.08 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.97 liquidity=15348420.0 spike=0.45
- PRMH.CA: score=5.25 buy_ready=False sector_rank=11 price=1.88 support=1.7 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=3079179.5 spike=1.13
- RACC.CA: score=0.8 buy_ready=False sector_rank=11 price=7.22 support=6.1 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=3896817.75 spike=0.54
- RAKT.CA: score=-2.64 buy_ready=False sector_rank=11 price=21.39 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=22.22 liquidity=436676.84 spike=1.01
- RAYA.CA: score=6.4 buy_ready=False sector_rank=16 price=5.51 support=5.02 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.78 liquidity=10788009.0 spike=0.51
- RMDA.CA: score=17.86 buy_ready=False sector_rank=5 price=5.2 support=4.5 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.67 liquidity=21496774.0 spike=0.88
- ROTO.CA: score=1.75 buy_ready=False sector_rank=11 price=30.5 support=28.7 resistance=30.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8661747.0 spike=1.09
- RREI.CA: score=6.49 buy_ready=False sector_rank=11 price=2.65 support=2.4 resistance=2.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26117518.0 spike=2.79
- RTVC.CA: score=10.49 buy_ready=False sector_rank=11 price=2.84 support=2.87 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.53 liquidity=8683089.0 spike=3.45
- RUBX.CA: score=7.91 buy_ready=False sector_rank=11 price=12.78 support=10.51 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.38 liquidity=60227252.0 spike=0.72
- SAUD.CA: score=8.48 buy_ready=False sector_rank=2 price=20.5 support=19.3 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.92 liquidity=8460786.0 spike=0.75
- SCEM.CA: score=15.0 buy_ready=False sector_rank=3 price=84.26 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=46.57 liquidity=18258572.0 spike=0.31
- SCFM.CA: score=2.91 buy_ready=False sector_rank=11 price=209.29 support=186.0 resistance=226.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5657597.0 spike=3.17
- SCTS.CA: score=12.99 buy_ready=False sector_rank=8 price=488.19 support=410.0 resistance=588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.96 liquidity=6159013.5 spike=1.64
- SDTI.CA: score=13.13 buy_ready=False sector_rank=11 price=83.87 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.6 liquidity=18571984.0 spike=1.11
- SEIG.CA: score=1.52 buy_ready=False sector_rank=11 price=186.4 support=149.57 resistance=186.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5467555.0 spike=2.57
- SIPC.CA: score=7.91 buy_ready=False sector_rank=11 price=4.68 support=3.73 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=36729404.0 spike=0.62
- SKPC.CA: score=6.48 buy_ready=False sector_rank=15 price=15.03 support=14.01 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.05 liquidity=47694352.0 spike=0.81
- SMFR.CA: score=-1.61 buy_ready=False sector_rank=11 price=186.15 support=165.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.67 liquidity=1484297.88 spike=0.5
- SNFC.CA: score=9.45 buy_ready=False sector_rank=11 price=10.81 support=10.08 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.62 liquidity=16739033.0 spike=2.27
- SPIN.CA: score=-2.22 buy_ready=False sector_rank=17 price=14.32 support=12.0 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.91 liquidity=1379480.13 spike=0.26
- SPMD.CA: score=13.01 buy_ready=False sector_rank=11 price=0.34 support=0.3 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.39 liquidity=21855822.0 spike=1.55
- SUGR.CA: score=15.49 buy_ready=False sector_rank=7 price=49.0 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.85 liquidity=16803546.0 spike=1.95
- SVCE.CA: score=6.91 buy_ready=False sector_rank=11 price=8.66 support=7.01 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.81 liquidity=24739246.0 spike=0.37
- SWDY.CA: score=17.72 buy_ready=False sector_rank=6 price=112.3 support=97.0 resistance=124.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=46251720.0 spike=0.75
- TALM.CA: score=8.55 buy_ready=False sector_rank=8 price=19.32 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.19 liquidity=11892222.0 spike=0.43
- TMGH.CA: score=11.9 buy_ready=False sector_rank=12 price=80.42 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.35 liquidity=283576256.0 spike=1.1
- TRTO.CA: score=-2.09 buy_ready=False sector_rank=11 price=0.05 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-27T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=2011.79 spike=0.28
- UEFM.CA: score=1.17 buy_ready=False sector_rank=11 price=449.63 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=20.51 liquidity=3378823.0 spike=1.44
- UEGC.CA: score=11.91 buy_ready=False sector_rank=11 price=1.42 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.73 liquidity=35841836.0 spike=0.77
- UNIP.CA: score=5.11 buy_ready=False sector_rank=11 price=0.29 support=0.25 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.41 liquidity=8165586.5 spike=1.02
- UNIT.CA: score=8.58 buy_ready=False sector_rank=12 price=17.76 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=1872890.63 spike=0.6
- WCDF.CA: score=2.6 buy_ready=False sector_rank=11 price=498.84 support=432.5 resistance=639.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.74 liquidity=3914823.0 spike=1.89
- WKOL.CA: score=3.54 buy_ready=False sector_rank=11 price=241.28 support=218.0 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.22 liquidity=6627565.0 spike=0.91
- ZEOT.CA: score=5.75 buy_ready=False sector_rank=11 price=10.47 support=8.0 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.66 liquidity=2842294.0 spike=0.36
- ZMID.CA: score=9.1 buy_ready=False sector_rank=12 price=6.6 support=5.91 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.67 liquidity=113815584.0 spike=1.7

## Backtesting Lite
- LCSW.CA: 180d return=51.98%, max drawdown=-17.84%, MA20>MA50 days last20=0, as_of=2026-10-27T21:00:00+00:00
- CANA.CA: 180d return=10.11%, max drawdown=-36.46%, MA20>MA50 days last20=20, as_of=2026-10-27T21:00:00+00:00
- AMOC.CA: 180d return=100.49%, max drawdown=-16.73%, MA20>MA50 days last20=20, as_of=2026-10-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=666 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- ADIB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Dhabi Islamic Bank Egypt summary=ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26; ADIB Egypt stock approaches breakout above EGP 41; ADIB Egypt’s stock holds uptrend despite corrections
  - ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26: https://english.mubasher.info/news/4607278/ADIB-Egypt-s-consolidated-profits-leap-to-EGP-3-6bn-in-Q1-26/
  - ADIB Egypt stock approaches breakout above EGP 41: https://english.mubasher.info/news/4591391/ADIB-Egypt-stock-approaches-breakout-above-EGP-41/
  - ADIB Egypt’s stock holds uptrend despite corrections: https://english.mubasher.info/news/4562331/ADIB-Egypt-s-stock-holds-uptrend-despite-corrections/
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project; Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations
  - Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project: https://english.mubasher.info/news/4684693/Elsewedy-Sinohydro-JV-signs-contract-for-Rabigh-2-IPP-expansion-project/
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.

## Warnings
- OpenRouter API error: 404
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
