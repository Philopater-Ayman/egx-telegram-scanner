# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-11-08T12:12:18.320950+00:00
Generated Cairo: 2026-11-08 14:12
Run timing: target 08:45 Cairo | generated Cairo 2026-11-08 14:12 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-11-08 14:10

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 171/186
- Top sector: Industrial Goods & Cables

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, November 08
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 64.71% / above MA50 17.65%
- EGX70 regime: BEARISH / above MA20 58.97% / above MA50 5.13%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- AMES.CA: liquidity=369078688.0 spike=5.91 score=9.93
- PHDC.CA: liquidity=241725728.0 spike=2.29 score=21.17
- BIOC.CA: liquidity=204699392.0 spike=2.45 score=7.83
- MFPC.CA: liquidity=166642624.0 spike=2.87 score=8.82
- BTFH.CA: liquidity=147974768.0 spike=1.27 score=15.52

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- SMFR.CA: spike=17.32 liquidity=53077852.0 outlook=CONSTRUCTIVE score=60.33 buy_ready=False
- CFGH.CA: spike=14.31 liquidity=87222.18 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MPRC.CA: spike=6.59 liquidity=98138872.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMES.CA: spike=5.91 liquidity=369078688.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGSA.CA: spike=5.84 liquidity=34460.0 outlook=CONSTRUCTIVE score=63.3 buy_ready=False

## Sector Leaderboard
- #1 Industrial Goods & Cables: score=7.51 5d=6.62% 20d=-5.04% aboveMA50=50.0%
- #2 Telecommunications: score=7.3 5d=2.95% 20d=-7.47% aboveMA50=50.0%
- #3 Education: score=6.18 5d=5.69% 20d=-5.83% aboveMA50=33.33%
- #4 Tourism & Leisure: score=5.97 5d=2.61% 20d=-3.12% aboveMA50=0.0%
- #5 Food, Beverages & Tobacco: score=5.35 5d=2.74% 20d=-1.36% aboveMA50=14.29%
- #6 Building Materials: score=4.34 5d=5.7% 20d=-8.88% aboveMA50=16.67%
- #7 Transportation & Logistics: score=4.25 5d=4.46% 20d=-2.91% aboveMA50=0.0%
- #8 Banking & Financials: score=4.01 5d=1.84% 20d=-3.79% aboveMA50=10.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- TALM.CA: BULLISH_WATCH score=86.18 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KZPC.CA: BULLISH_WATCH score=82.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- SWDY.CA: BULLISH_WATCH score=76.51 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support; close to resistance
- SCEM.CA: BULLISH_WATCH score=75.34 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; close to resistance
- EFIH.CA: BULLISH_WATCH score=73.42 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- SNFC.CA: BULLISH_WATCH score=72.33 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- SAUD.CA: BULLISH_WATCH score=70.01 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; sector is not leading
- POUL.CA: CONSTRUCTIVE score=65.35 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50
- SCTS.CA: CONSTRUCTIVE score=65.18 liquidity=TRADEABLE sector=LEADING risk=below MA50; far above support
- CIRA.CA: CONSTRUCTIVE score=64.18 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA50

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=19.43 buy_ready=False sector_rank=13 price=241.47 support=171.02 resistance=270.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=58.1 liquidity=20411672.0 spike=1.25
- ABUK.CA: score=6.06 buy_ready=False sector_rank=12 price=76.4 support=76.2 resistance=80.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=141384352.0 spike=1.49
- ACAMD.CA: score=15.93 buy_ready=False sector_rank=13 price=1.99 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=43.4 liquidity=29424734.0 spike=0.57
- ACGC.CA: score=9.48 buy_ready=False sector_rank=16 price=13.22 support=11.6 resistance=14.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:51 PM market time freshness=DELAYED_CURRENT RSI=55.65 liquidity=1098943.5 spike=0.15
- ADCI.CA: score=9.82 buy_ready=False sector_rank=13 price=258.77 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:52 PM market time freshness=DELAYED_CURRENT RSI=51.66 liquidity=890456.94 spike=0.46
- ADIB.CA: score=19.6 buy_ready=False sector_rank=8 price=48.58 support=43.16 resistance=50.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=64.18 liquidity=38070612.0 spike=0.45
- ADPC.CA: score=12.7 buy_ready=False sector_rank=13 price=3.05 support=2.53 resistance=3.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:52 PM market time freshness=DELAYED_CURRENT RSI=51.56 liquidity=4764553.5 spike=0.56
- AFDI.CA: score=9.26 buy_ready=False sector_rank=13 price=45.04 support=34.8 resistance=54.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:52 PM market time freshness=DELAYED_CURRENT RSI=45.67 liquidity=2325688.5 spike=0.8
- AFMC.CA: score=18.97 buy_ready=False sector_rank=13 price=138.42 support=94.6 resistance=153.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=60.06 liquidity=17905140.0 spike=1.02
- AJWA.CA: score=9.93 buy_ready=False sector_rank=13 price=244.66 support=223.25 resistance=254.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=112501312.0 spike=3.83
- ALCN.CA: score=16.23 buy_ready=False sector_rank=7 price=31.93 support=27.11 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=8530036.0 spike=0.72
- ALUM.CA: score=9.82 buy_ready=False sector_rank=13 price=20.32 support=16.02 resistance=23.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=54.5 liquidity=1886188.63 spike=0.59
- AMER.CA: score=22.31 buy_ready=False sector_rank=9 price=4.6 support=3.21 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=132785440.0 spike=2.36
- AMES.CA: score=9.93 buy_ready=False sector_rank=13 price=43.71 support=38.6 resistance=44.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=369078688.0 spike=5.91
- AMIA.CA: score=13.36 buy_ready=False sector_rank=13 price=17.99 support=14.0 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=4425642.0 spike=0.37
- AMOC.CA: score=13.26 buy_ready=False sector_rank=19 price=13.04 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=52.35 liquidity=53787080.0 spike=0.37
- APSW.CA: score=9.73 buy_ready=False sector_rank=13 price=7.33 support=7.1 resistance=8.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:51 PM market time freshness=DELAYED_CURRENT RSI=39.11 liquidity=1037821.06 spike=2.38
- ARAB.CA: score=15.59 buy_ready=False sector_rank=9 price=0.25 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=86187984.0 spike=0.83
- ARCC.CA: score=19.74 buy_ready=False sector_rank=6 price=67.58 support=58.01 resistance=73.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=55.08 liquidity=14923332.0 spike=0.4
- AREH.CA: score=11.84 buy_ready=False sector_rank=13 price=1.11 support=0.91 resistance=1.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.06 liquidity=3912611.5 spike=0.51
- ASCM.CA: score=10.46 buy_ready=False sector_rank=13 price=46.21 support=38.2 resistance=58.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=50.13 liquidity=2525266.0 spike=0.3
- ASPI.CA: score=19.63 buy_ready=False sector_rank=13 price=0.32 support=0.27 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.66 liquidity=34418440.0 spike=1.85
- ATLC.CA: score=9.65 buy_ready=False sector_rank=18 price=4.99 support=3.93 resistance=6.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.17 liquidity=4667683.5 spike=0.59
- ATQA.CA: score=16.86 buy_ready=False sector_rank=12 price=9.97 support=8.25 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=38.93 liquidity=64226972.0 spike=1.39
- AXPH.CA: score=11.83 buy_ready=False sector_rank=13 price=1327.98 support=1135.0 resistance=1520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=50.75 liquidity=2896237.75 spike=0.6
- BINV.CA: score=0.92 buy_ready=False sector_rank=17 price=52.99 support=50.62 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:40 PM market time freshness=DELAYED_CURRENT RSI=31.39 liquidity=1928444.88 spike=0.19
- BIOC.CA: score=7.83 buy_ready=False sector_rank=13 price=336.13 support=308.01 resistance=339.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=204699392.0 spike=2.45
- BTFH.CA: score=15.52 buy_ready=False sector_rank=18 price=2.4 support=2.05 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=39.82 liquidity=147974768.0 spike=1.27
- CAED.CA: score=19.77 buy_ready=False sector_rank=13 price=97.66 support=64.0 resistance=118.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.63 liquidity=21619172.0 spike=1.42
- CANA.CA: score=22.6 buy_ready=False sector_rank=8 price=47.07 support=38.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=19709262.0 spike=1.0
- CCAP.CA: score=14.0 buy_ready=False sector_rank=17 price=5.82 support=5.55 resistance=6.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=48.86 liquidity=120902720.0 spike=0.28
- CCRS.CA: score=21.71 buy_ready=False sector_rank=13 price=2.12 support=1.3 resistance=2.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=21130702.0 spike=2.39
- CEFM.CA: score=10.52 buy_ready=False sector_rank=13 price=119.11 support=97.79 resistance=131.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:44 PM market time freshness=DELAYED_CURRENT RSI=49.94 liquidity=1591169.5 spike=0.73
- CERA.CA: score=13.93 buy_ready=False sector_rank=13 price=1.09 support=0.93 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=64495952.0 spike=0.74
- CFGH.CA: score=4.02 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=5 November 02:13 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=87222.18 spike=14.31
- CICH.CA: score=6.31 buy_ready=False sector_rank=18 price=10.7 support=9.63 resistance=12.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=54.74 liquidity=1321440.88 spike=0.57
- CIEB.CA: score=17.76 buy_ready=False sector_rank=8 price=22.41 support=21.35 resistance=24.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=12856680.0 spike=1.58
- CIRA.CA: score=20.57 buy_ready=False sector_rank=3 price=37.11 support=32.01 resistance=39.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=9172944.0 spike=0.71
- CLHO.CA: score=15.54 buy_ready=False sector_rank=15 price=13.64 support=12.51 resistance=15.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=43.94 liquidity=14525731.0 spike=0.39
- CNFN.CA: score=10.33 buy_ready=False sector_rank=18 price=3.94 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.14 liquidity=3343519.5 spike=0.39
- COMI.CA: score=18.6 buy_ready=False sector_rank=8 price=127.28 support=117.41 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=54.8 liquidity=139587744.0 spike=0.26
- COPR.CA: score=18.23 buy_ready=False sector_rank=13 price=0.41 support=0.33 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=45.79 liquidity=24405974.0 spike=1.65
- COSG.CA: score=12.6 buy_ready=False sector_rank=13 price=1.33 support=1.11 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=48.44 liquidity=6668204.0 spike=0.7
- CPCI.CA: score=12.07 buy_ready=False sector_rank=13 price=598.72 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=54.45 liquidity=2140586.5 spike=0.45
- CSAG.CA: score=19.73 buy_ready=False sector_rank=7 price=34.92 support=30.1 resistance=37.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=9347500.0 spike=1.34
- DAPH.CA: score=17.93 buy_ready=False sector_rank=13 price=85.36 support=65.2 resistance=109.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=14589918.0 spike=0.59
- DEIN.CA: score=7.93 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=12.39 buy_ready=False sector_rank=5 price=24.08 support=20.27 resistance=24.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.03 liquidity=2633042.5 spike=1.31
- DSCW.CA: score=19.39 buy_ready=False sector_rank=13 price=1.52 support=1.23 resistance=1.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=50.75 liquidity=22428488.0 spike=1.73
- DTPP.CA: score=10.93 buy_ready=False sector_rank=13 price=48.18 support=36.0 resistance=302.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=33.54 liquidity=12490054.0 spike=0.39
- EALR.CA: score=19.47 buy_ready=False sector_rank=13 price=297.8 support=236.01 resistance=347.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=50.84 liquidity=9898180.0 spike=1.82
- EASB.CA: score=13.43 buy_ready=False sector_rank=13 price=6.52 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=53.74 liquidity=4501268.0 spike=0.73
- EAST.CA: score=19.21 buy_ready=False sector_rank=5 price=32.63 support=27.01 resistance=33.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:51 PM market time freshness=DELAYED_CURRENT RSI=72.56 liquidity=7072658.5 spike=0.18
- EBSC.CA: score=9.35 buy_ready=False sector_rank=13 price=1.53 support=1.2 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=52.44 liquidity=1418390.12 spike=0.45
- ECAP.CA: score=12.05 buy_ready=False sector_rank=13 price=28.32 support=24.8 resistance=30.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=52.64 liquidity=3395927.0 spike=1.36
- EDFM.CA: score=10.01 buy_ready=False sector_rank=13 price=364.73 support=312.92 resistance=382.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=49.04 liquidity=1077952.63 spike=0.95
- EEII.CA: score=11.65 buy_ready=False sector_rank=13 price=1.79 support=1.42 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=49.33 liquidity=3722281.25 spike=0.55
- EFIC.CA: score=23.48 buy_ready=False sector_rank=12 price=167.87 support=121.0 resistance=168.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=59.4 liquidity=66930452.0 spike=2.7
- EFID.CA: score=19.14 buy_ready=False sector_rank=5 price=19.47 support=16.01 resistance=19.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=52.47 liquidity=25061754.0 spike=0.68
- EFIH.CA: score=22.45 buy_ready=False sector_rank=11 price=23.5 support=20.3 resistance=25.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=59731336.0 spike=1.04
- EGAL.CA: score=17.08 buy_ready=False sector_rank=12 price=318.07 support=275.0 resistance=342.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=74.61 liquidity=77328304.0 spike=0.8
- EGAS.CA: score=6.46 buy_ready=False sector_rank=19 price=48.38 support=43.0 resistance=57.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=44.21 liquidity=2203548.0 spike=0.53
- EGBE.CA: score=5.62 buy_ready=False sector_rank=8 price=0.49 support=0.47 resistance=0.54 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=44.9 liquidity=20646.15 spike=0.33
- EGCH.CA: score=16.08 buy_ready=False sector_rank=12 price=10.31 support=9.66 resistance=13.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=43.97 liquidity=29356484.0 spike=0.54
- EGSA.CA: score=18.43 buy_ready=False sector_rank=2 price=9.0 support=8.7 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:48 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=34460.0 spike=5.84
- EGTS.CA: score=19.83 buy_ready=False sector_rank=9 price=13.2 support=10.19 resistance=16.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=30804862.0 spike=1.62
- EHDR.CA: score=14.36 buy_ready=False sector_rank=13 price=2.09 support=1.8 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=8430437.0 spike=0.92
- ELEC.CA: score=22.4 buy_ready=False sector_rank=1 price=1.66 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=31185780.0 spike=0.59
- ELKA.CA: score=15.35 buy_ready=False sector_rank=13 price=1.49 support=1.21 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=53.62 liquidity=6418896.0 spike=0.48
- ELNA.CA: score=10.54 buy_ready=False sector_rank=13 price=41.29 support=33.46 resistance=41.59 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=75.66 liquidity=926217.3 spike=1.34
- ELSH.CA: score=2.66 buy_ready=False sector_rank=13 price=11.11 support=10.25 resistance=11.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7726517.5 spike=0.48
- ELWA.CA: score=4.82 buy_ready=False sector_rank=13 price=1.33 support=1.3 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=12.12 liquidity=2184122.0 spike=2.85
- EMFD.CA: score=19.59 buy_ready=False sector_rank=9 price=12.37 support=10.6 resistance=12.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=60.08 liquidity=28015122.0 spike=0.5
- ENGC.CA: score=15.63 buy_ready=False sector_rank=13 price=35.68 support=26.91 resistance=37.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=7701355.0 spike=0.84
- EOSB.CA: score=9.99 buy_ready=False sector_rank=13 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=55355.02 spike=0.64
- EPCO.CA: score=0.4 buy_ready=False sector_rank=13 price=9.06 support=8.38 resistance=9.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5328520.5 spike=1.07
- EPPK.CA: score=-4.65 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=18.4 buy_ready=False sector_rank=2 price=130.41 support=115.0 resistance=148.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=40.31 liquidity=76006648.0 spike=0.31
- ETRS.CA: score=16.46 buy_ready=False sector_rank=13 price=10.87 support=9.51 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=63.84 liquidity=2531870.75 spike=0.17
- EXPA.CA: score=19.04 buy_ready=False sector_rank=8 price=14.49 support=12.0 resistance=15.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=50.99 liquidity=30450466.0 spike=1.22
- FAIT.CA: score=10.08 buy_ready=False sector_rank=8 price=44.33 support=40.0 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=55.84 liquidity=480907.41 spike=0.18
- FAITA.CA: score=7.0 buy_ready=False sector_rank=8 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=38484.12 spike=1.18
- FERC.CA: score=23.08 buy_ready=False sector_rank=12 price=69.56 support=53.57 resistance=77.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=26592860.0 spike=4.37
- FWRY.CA: score=14.37 buy_ready=False sector_rank=11 price=17.18 support=15.27 resistance=19.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=33726184.0 spike=0.32
- GBCO.CA: score=6.69 buy_ready=False sector_rank=21 price=22.79 support=20.9 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=20.52 liquidity=92278080.0 spike=0.86
- GDWA.CA: score=13.95 buy_ready=False sector_rank=13 price=0.57 support=0.46 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=50.41 liquidity=6018944.0 spike=0.48
- GGCC.CA: score=15.93 buy_ready=False sector_rank=13 price=0.56 support=0.49 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=38.73 liquidity=13802298.0 spike=0.7
- GIHD.CA: score=17.69 buy_ready=False sector_rank=13 price=47.43 support=32.1 resistance=63.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=9759901.0 spike=0.64
- GMCI.CA: score=-0.76 buy_ready=False sector_rank=13 price=1.48 support=1.34 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=307468.59 spike=1.0
- GRCA.CA: score=18.41 buy_ready=False sector_rank=13 price=32.26 support=22.57 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=55.99 liquidity=10778987.0 spike=1.24
- GSSC.CA: score=12.65 buy_ready=False sector_rank=13 price=259.3 support=211.52 resistance=287.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:31 PM market time freshness=DELAYED_CURRENT RSI=45.64 liquidity=1860764.25 spike=1.93
- HDBK.CA: score=19.08 buy_ready=False sector_rank=8 price=99.04 support=83.01 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=53.73 liquidity=28584792.0 spike=1.24
- HELI.CA: score=19.59 buy_ready=False sector_rank=9 price=6.86 support=5.72 resistance=7.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=35999408.0 spike=0.48
- HRHO.CA: score=12.98 buy_ready=False sector_rank=18 price=23.5 support=21.87 resistance=26.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=22496852.0 spike=0.43
- ICID.CA: score=13.33 buy_ready=False sector_rank=13 price=17.4 support=14.26 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:51 PM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=4400614.5 spike=0.84
- IDRE.CA: score=13.65 buy_ready=False sector_rank=13 price=40.73 support=29.11 resistance=50.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=49.45 liquidity=5714517.0 spike=1.0
- IFAP.CA: score=20.51 buy_ready=False sector_rank=10 price=17.81 support=15.12 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=13464570.0 spike=2.05
- INFI.CA: score=19.67 buy_ready=False sector_rank=13 price=122.97 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=44.79 liquidity=27036862.0 spike=1.37
- IRON.CA: score=7.93 buy_ready=False sector_rank=12 price=24.28 support=23.13 resistance=29.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:50 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=3843833.0 spike=0.4
- ISMA.CA: score=14.45 buy_ready=False sector_rank=13 price=20.52 support=14.11 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=51.76 liquidity=6518213.0 spike=0.77
- ISMQ.CA: score=15.43 buy_ready=False sector_rank=12 price=7.38 support=5.96 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=7348119.5 spike=0.51
- ISPH.CA: score=15.54 buy_ready=False sector_rank=15 price=10.17 support=9.02 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=46.45 liquidity=33919280.0 spike=0.6
- JUFO.CA: score=19.14 buy_ready=False sector_rank=5 price=23.57 support=21.01 resistance=25.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=17910832.0 spike=0.83
- KABO.CA: score=14.25 buy_ready=False sector_rank=16 price=7.03 support=5.58 resistance=9.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.32 liquidity=8862253.0 spike=0.42
- KWIN.CA: score=8.03 buy_ready=False sector_rank=13 price=73.77 support=66.5 resistance=76.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19859536.0 spike=2.55
- KZPC.CA: score=27.95 buy_ready=False sector_rank=13 price=14.01 support=11.56 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=22959744.0 spike=3.01
- LCSW.CA: score=7.78 buy_ready=False sector_rank=6 price=38.72 support=35.57 resistance=39.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41905164.0 spike=2.02
- LUTS.CA: score=19.21 buy_ready=False sector_rank=13 price=0.77 support=0.47 resistance=0.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=68124808.0 spike=1.14
- MAAL.CA: score=11.16 buy_ready=False sector_rank=13 price=6.84 support=4.88 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:50 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=4223305.5 spike=0.39
- MASR.CA: score=16.93 buy_ready=False sector_rank=13 price=6.73 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=19293650.0 spike=0.42
- MBSC.CA: score=17.74 buy_ready=False sector_rank=6 price=318.44 support=262.0 resistance=401.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=45.75 liquidity=25929008.0 spike=0.38
- MCQE.CA: score=18.74 buy_ready=False sector_rank=6 price=171.97 support=144.0 resistance=203.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=55.63 liquidity=34211872.0 spike=0.61
- MCRO.CA: score=18.25 buy_ready=False sector_rank=13 price=1.32 support=1.07 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=46506336.0 spike=1.16
- MENA.CA: score=10.41 buy_ready=False sector_rank=9 price=5.89 support=5.45 resistance=6.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:42 PM market time freshness=DELAYED_CURRENT RSI=59.06 liquidity=1820828.63 spike=0.43
- MEPA.CA: score=15.93 buy_ready=False sector_rank=13 price=1.34 support=1.14 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=12156950.0 spike=0.78
- MFPC.CA: score=8.82 buy_ready=False sector_rank=12 price=38.55 support=38.51 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=166642624.0 spike=2.87
- MFSC.CA: score=13.67 buy_ready=False sector_rank=13 price=36.64 support=28.55 resistance=44.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=44.56 liquidity=3837756.0 spike=1.95
- MHOT.CA: score=20.79 buy_ready=False sector_rank=4 price=15.98 support=13.0 resistance=16.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:51 PM market time freshness=DELAYED_CURRENT RSI=50.14 liquidity=10147515.0 spike=1.7
- MICH.CA: score=9.93 buy_ready=False sector_rank=13 price=43.03 support=40.91 resistance=44.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22286530.0 spike=3.94
- MILS.CA: score=15.33 buy_ready=False sector_rank=13 price=139.7 support=94.24 resistance=182.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=47.55 liquidity=7393473.0 spike=0.9
- MIPH.CA: score=9.02 buy_ready=False sector_rank=15 price=777.94 support=610.0 resistance=826.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:43 PM market time freshness=DELAYED_CURRENT RSI=59.83 liquidity=480594.97 spike=0.14
- MOED.CA: score=16.81 buy_ready=False sector_rank=13 price=0.5 support=0.39 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=38.14 liquidity=18956008.0 spike=1.44
- MOIL.CA: score=3.27 buy_ready=False sector_rank=19 price=0.64 support=0.6 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:49 PM market time freshness=DELAYED_CURRENT RSI=44.17 liquidity=9637.19 spike=0.06
- MOIN.CA: score=9.56 buy_ready=False sector_rank=13 price=29.03 support=25.7 resistance=36.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=51.7 liquidity=2626014.75 spike=0.41
- MOSC.CA: score=23.93 buy_ready=False sector_rank=13 price=271.04 support=198.01 resistance=286.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=15189043.0 spike=4.24
- MPCI.CA: score=19.43 buy_ready=False sector_rank=13 price=324.92 support=238.6 resistance=350.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=126688392.0 spike=1.25
- MPCO.CA: score=17.41 buy_ready=False sector_rank=10 price=1.9 support=1.55 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=43901596.0 spike=0.54
- MPRC.CA: score=9.93 buy_ready=False sector_rank=13 price=38.07 support=33.51 resistance=38.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98138872.0 spike=6.59
- MTIE.CA: score=13.0 buy_ready=False sector_rank=21 price=7.04 support=6.05 resistance=8.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=9303573.0 spike=0.46
- NAHO.CA: score=4.95 buy_ready=False sector_rank=13 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=13022.12 spike=0.75
- NCCW.CA: score=11.74 buy_ready=False sector_rank=13 price=5.43 support=4.05 resistance=7.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=5812136.5 spike=0.35
- NEDA.CA: score=0.49 buy_ready=False sector_rank=13 price=2.36 support=2.26 resistance=2.66 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=281873.67 spike=1.64
- NHPS.CA: score=11.33 buy_ready=False sector_rank=13 price=61.04 support=50.0 resistance=73.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=3402795.5 spike=0.49
- NINH.CA: score=12.38 buy_ready=False sector_rank=13 price=15.77 support=12.36 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=53.43 liquidity=4444412.0 spike=0.49
- NIPH.CA: score=18.54 buy_ready=False sector_rank=15 price=280.39 support=205.0 resistance=318.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=122755808.0 spike=0.93
- OBRI.CA: score=12.67 buy_ready=False sector_rank=13 price=24.14 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=46.85 liquidity=4734418.0 spike=0.42
- OCDI.CA: score=19.59 buy_ready=False sector_rank=9 price=24.93 support=21.0 resistance=27.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.69 liquidity=31032734.0 spike=0.96
- OCPH.CA: score=8.2 buy_ready=False sector_rank=13 price=186.36 support=147.96 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=47.57 liquidity=2265690.5 spike=0.65
- ODIN.CA: score=15.53 buy_ready=False sector_rank=13 price=2.13 support=1.7 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.69 liquidity=7462856.5 spike=1.07
- OFH.CA: score=19.45 buy_ready=False sector_rank=13 price=0.75 support=0.61 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=26594268.0 spike=1.26
- OIH.CA: score=18.0 buy_ready=False sector_rank=17 price=1.78 support=1.5 resistance=1.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=27831496.0 spike=0.61
- OLFI.CA: score=17.63 buy_ready=False sector_rank=5 price=20.0 support=17.86 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=41.73 liquidity=8450617.0 spike=1.02
- ORAS.CA: score=4.6 buy_ready=False sector_rank=14 price=805.52 support=800.01 resistance=818.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83934744.0 spike=1.0
- ORHD.CA: score=18.59 buy_ready=False sector_rank=9 price=10.52 support=8.5 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.54 liquidity=70567624.0 spike=0.59
- ORWE.CA: score=16.38 buy_ready=False sector_rank=16 price=24.92 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=42.62 liquidity=16493195.0 spike=0.47
- PHAR.CA: score=18.54 buy_ready=False sector_rank=15 price=102.21 support=90.2 resistance=115.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=51.42 liquidity=29299570.0 spike=0.54
- PHDC.CA: score=21.17 buy_ready=False sector_rank=9 price=12.1 support=10.33 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=43.29 liquidity=241725728.0 spike=2.29
- PHTV.CA: score=8.83 buy_ready=False sector_rank=13 price=322.0 support=300.0 resistance=345.67 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=40.34 liquidity=1637048.0 spike=1.13
- POUL.CA: score=20.16 buy_ready=False sector_rank=5 price=10.02 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=116991536.0 spike=1.51
- PRCL.CA: score=19.1 buy_ready=False sector_rank=6 price=21.95 support=16.65 resistance=26.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=56.77 liquidity=18273966.0 spike=1.18
- PRDC.CA: score=18.29 buy_ready=False sector_rank=9 price=6.36 support=5.08 resistance=7.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=58.66 liquidity=8703806.0 spike=0.43
- PRMH.CA: score=21.96 buy_ready=False sector_rank=13 price=2.02 support=1.7 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=9825875.0 spike=3.1
- RACC.CA: score=10.79 buy_ready=False sector_rank=13 price=7.97 support=6.1 resistance=9.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=4856692.5 spike=0.78
- RAKT.CA: score=4.05 buy_ready=False sector_rank=13 price=22.35 support=20.4 resistance=23.99 source=Yahoo Finance as_of=2026-11-04T22:00:00+00:00 freshness=FRESH RSI=53.99 liquidity=115817.7 spike=0.39
- RAYA.CA: score=14.15 buy_ready=False sector_rank=20 price=5.6 support=5.02 resistance=6.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=11927667.0 spike=0.6
- RMDA.CA: score=22.94 buy_ready=False sector_rank=15 price=5.57 support=4.5 resistance=5.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=63.35 liquidity=58996716.0 spike=2.2
- ROTO.CA: score=20.31 buy_ready=False sector_rank=13 price=33.78 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=41.61 liquidity=19167328.0 spike=2.19
- RREI.CA: score=16.95 buy_ready=False sector_rank=13 price=2.85 support=1.96 resistance=3.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=38.35 liquidity=15669925.0 spike=1.51
- RTVC.CA: score=-0.13 buy_ready=False sector_rank=13 price=2.81 support=2.66 resistance=3.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:43 PM market time freshness=DELAYED_CURRENT RSI=26.26 liquidity=940183.5 spike=0.37
- RUBX.CA: score=14.93 buy_ready=False sector_rank=13 price=13.07 support=10.51 resistance=18.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=15402969.0 spike=0.23
- SAUD.CA: score=22.48 buy_ready=False sector_rank=8 price=21.5 support=19.3 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:52 PM market time freshness=DELAYED_CURRENT RSI=47.69 liquidity=27622140.0 spike=2.44
- SCEM.CA: score=27.1 buy_ready=False sector_rank=6 price=94.26 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=63.84 liquidity=112357024.0 spike=2.18
- SCFM.CA: score=9.88 buy_ready=False sector_rank=13 price=220.12 support=153.02 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=46.77 liquidity=1945135.5 spike=0.87
- SCTS.CA: score=16.36 buy_ready=False sector_rank=3 price=524.78 support=410.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=57.48 liquidity=4963599.5 spike=0.94
- SDTI.CA: score=21.93 buy_ready=False sector_rank=13 price=87.66 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=62.15 liquidity=15490221.0 spike=0.87
- SEIG.CA: score=17.27 buy_ready=False sector_rank=13 price=233.69 support=142.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=59.81 liquidity=5333629.0 spike=0.63
- SIPC.CA: score=6.53 buy_ready=False sector_rank=13 price=5.55 support=4.85 resistance=5.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86180248.0 spike=1.8
- SKPC.CA: score=16.08 buy_ready=False sector_rank=12 price=14.89 support=14.01 resistance=16.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=52.28 liquidity=15640341.0 spike=0.32
- SMFR.CA: score=24.93 buy_ready=False sector_rank=13 price=236.4 support=165.0 resistance=238.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=65.23 liquidity=53077852.0 spike=17.32
- SNFC.CA: score=17.87 buy_ready=False sector_rank=13 price=11.14 support=10.08 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=49.8 liquidity=7942902.0 spike=0.99
- SPIN.CA: score=6.47 buy_ready=False sector_rank=16 price=14.3 support=12.0 resistance=16.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=52.97 liquidity=1085087.88 spike=0.21
- SPMD.CA: score=14.28 buy_ready=False sector_rank=13 price=0.35 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=52.15 liquidity=8346979.0 spike=0.49
- SUGR.CA: score=17.06 buy_ready=False sector_rank=5 price=47.48 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=39.54 liquidity=14336204.0 spike=1.46
- SVCE.CA: score=20.43 buy_ready=False sector_rank=13 price=9.08 support=7.01 resistance=10.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:57 PM market time freshness=DELAYED_CURRENT RSI=49.77 liquidity=80917864.0 spike=1.75
- SWDY.CA: score=28.88 buy_ready=False sector_rank=1 price=118.33 support=97.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=64904628.0 spike=1.24
- TALM.CA: score=21.89 buy_ready=False sector_rank=3 price=20.2 support=17.0 resistance=22.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:52 PM market time freshness=DELAYED_CURRENT RSI=53.3 liquidity=7488009.0 spike=0.33
- TMGH.CA: score=18.59 buy_ready=False sector_rank=9 price=82.96 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:54 PM market time freshness=DELAYED_CURRENT RSI=51.64 liquidity=135596736.0 spike=0.5
- TRTO.CA: score=-4.46 buy_ready=False sector_rank=13 price=0.06 support=0.06 resistance=0.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:48 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6077.05 spike=1.3
- UEFM.CA: score=8.89 buy_ready=False sector_rank=13 price=486.09 support=422.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:47 PM market time freshness=DELAYED_CURRENT RSI=51.51 liquidity=955835.69 spike=0.51
- UEGC.CA: score=17.93 buy_ready=False sector_rank=13 price=1.48 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=46.75 liquidity=16850482.0 spike=0.35
- UNIP.CA: score=10.7 buy_ready=False sector_rank=13 price=0.3 support=0.25 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:57 PM market time freshness=DELAYED_CURRENT RSI=48.31 liquidity=4769904.5 spike=0.65
- UNIT.CA: score=13.04 buy_ready=False sector_rank=9 price=18.14 support=15.06 resistance=18.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=69.35 liquidity=454386.47 spike=0.23
- WCDF.CA: score=11.06 buy_ready=False sector_rank=13 price=517.84 support=432.5 resistance=623.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=50.91 liquidity=2370386.25 spike=1.38
- WKOL.CA: score=8.93 buy_ready=False sector_rank=13 price=177.18 support=145.33 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:56 PM market time freshness=DELAYED_CURRENT RSI=28.45 liquidity=10529003.0 spike=0.95
- ZEOT.CA: score=19.67 buy_ready=False sector_rank=13 price=11.48 support=7.9 resistance=12.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:57 PM market time freshness=DELAYED_CURRENT RSI=59.72 liquidity=11255029.0 spike=1.37
- ZMID.CA: score=19.91 buy_ready=False sector_rank=9 price=6.99 support=5.91 resistance=7.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=83744664.0 spike=1.16

## Backtesting Lite
- SWDY.CA: 180d return=51.05%, max drawdown=-25.52%, MA20>MA50 days last20=1, as_of=2026-11-04T22:00:00+00:00
- KZPC.CA: 180d return=33.07%, max drawdown=-27.57%, MA20>MA50 days last20=9, as_of=2026-11-04T22:00:00+00:00
- SCEM.CA: 180d return=49.5%, max drawdown=-29.64%, MA20>MA50 days last20=0, as_of=2026-11-04T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project; Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations
  - Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project: https://english.mubasher.info/news/4684693/Elsewedy-Sinohydro-JV-signs-contract-for-Rabigh-2-IPP-expansion-project/
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=1042 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=676 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- SMFR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Samad Misr EGYFERT.S.A.E summary=Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- MOSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Oils & Soap summary=Misr Oils and Soap not to pay dividends for FY20/21; Misr Oils and Soap&#39;s profit plunges 78% in FY20/21; Misr Oils and Soap swings to loss in 10 months
  - Misr Oils and Soap not to pay dividends for FY20/21: https://english.mubasher.info/news/3856493/Misr-Oils-and-Soap-not-to-pay-dividends-for-FY20-21/
  - Misr Oils and Soap&#39;s profit plunges 78% in FY20/21: https://english.mubasher.info/news/3851183/Misr-Oils-and-Soap-s-profit-plunges-78-in-FY20-21/
  - Misr Oils and Soap swings to loss in 10 months: https://english.mubasher.info/news/3811105/Misr-Oils-and-Soap-swings-to-loss-in-10-months/
- EFIC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=676 sources=3 expected=Egyptian Financial and Industrial summary=EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed; EFIC ordered to pay over EGP 126m as penalties; EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn
  - EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed: https://english.mubasher.info/news/4579891/EFIC-s-consolidated-profits-near-EGP-820m-in-2025-dividends-proposed/
  - EFIC ordered to pay over EGP 126m as penalties: https://english.mubasher.info/news/4535935/EFIC-ordered-to-pay-over-EGP-126m-as-penalties/
  - EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn: https://english.mubasher.info/news/4528902/EFIC-generates-lower-consolidated-net-profits-at-EGP-803m-in-9M-25-net-sales-near-EGP-8bn/
- FERC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=676 sources=3 expected=Ferchem Misr Fertilizers and Chemicals summary=Ferchem Misr’s board greenlights EGP 500m dividends for 2025; Ferchem Misr’s profits soar 4,238% in 2025; Ferchem Misr’s profit leaps 75% in 9M
  - Ferchem Misr’s board greenlights EGP 500m dividends for 2025: https://english.mubasher.info/news/4600298/Ferchem-Misr-s-board-greenlights-EGP-500m-dividends-for-2025/
  - Ferchem Misr’s profits soar 4,238% in 2025: https://english.mubasher.info/news/4564349/Ferchem-Misr-s-profits-soar-4-238-in-2025/
  - Ferchem Misr’s profit leaps 75% in 9M: https://english.mubasher.info/news/3560738/Ferchem-Misr-s-profit-leaps-75-in-9M/
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.

## Warnings
- OpenRouter API error: 404
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- Evidence for MOSC.CA matches the company but no source/report date was detected.
- Evidence for EFIC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for FERC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
