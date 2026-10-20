# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-20T10:26:25.143891+00:00
Generated Cairo: 2026-10-20 13:26
Run timing: target 08:45 Cairo | generated Cairo 2026-10-20 13:26 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-20 13:23

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 166/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, October 20
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 23.53% / above MA50 17.65%
- EGX70 regime: BEARISH / above MA20 5.56% / above MA50 8.33%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=389237248.0 spike=0.69 score=17.3
- COMI.CA: liquidity=244064368.0 spike=0.48 score=13.52
- ELEC.CA: liquidity=209010320.0 spike=5.92 score=12.18
- AMOC.CA: liquidity=180082736.0 spike=1.52 score=4.8
- GBCO.CA: liquidity=150512064.0 spike=1.48 score=5.0

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- ELEC.CA: spike=5.92 liquidity=209010320.0 outlook=WEAK_OR_RISKY score=2.95 buy_ready=False
- WKOL.CA: spike=5.3 liquidity=32898390.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- POUL.CA: spike=2.67 liquidity=107313568.0 outlook=WEAK_OR_RISKY score=29 buy_ready=False
- AALR.CA: spike=2.13 liquidity=23521730.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGSA.CA: spike=1.91 liquidity=13545.0 outlook=NEUTRAL score=43.69 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=7.69 5d=-1.18% 20d=2.23% aboveMA50=100.0%
- #2 Industrial Goods & Cables: score=2.95 5d=-1.25% 20d=-7.17% aboveMA50=0.0%
- #3 Fintech & Payments: score=1.77 5d=-2.96% 20d=-1.96% aboveMA50=50.0%
- #4 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Investment Holding: score=0.75 5d=0.0% 20d=-14.64% aboveMA50=66.67%
- #6 Building Materials: score=0.46 5d=-0.07% 20d=-4.75% aboveMA50=0.0%
- #7 Automotive & Distribution: score=0.09 5d=-1.98% 20d=-7.01% aboveMA50=0.0%
- #8 Energy & Petrochemicals: score=-0.59 5d=0.0% 20d=-4.29% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=93.69 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=81.77 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KZPC.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- BINV.CA: BULLISH_WATCH score=70.75 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MFPC.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- CPCI.CA: CONSTRUCTIVE score=65 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- ACAMD.CA: CONSTRUCTIVE score=54 liquidity=TRADEABLE sector=LAGGING risk=below MA50; sector is not leading
- ARAB.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; momentum is extended; far above support; sector is not leading
- TALM.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading
- SNFC.CA: CONSTRUCTIVE score=53 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; below MA20; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=4.66 buy_ready=False sector_rank=17 price=231.3 support=228.0 resistance=243.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23521730.0 spike=2.13
- ABUK.CA: score=4.1 buy_ready=False sector_rank=16 price=92.86 support=87.5 resistance=93.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=135917984.0 spike=1.85
- ACAMD.CA: score=16.4 buy_ready=False sector_rank=17 price=2.03 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=41091804.0 spike=0.88
- ACGC.CA: score=4.15 buy_ready=False sector_rank=20 price=13.0 support=12.5 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1751172.13 spike=0.15
- ADCI.CA: score=2.82 buy_ready=False sector_rank=17 price=258.36 support=241.55 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=37.61 liquidity=418463.56 spike=0.21
- ADIB.CA: score=7.52 buy_ready=False sector_rank=15 price=45.5 support=43.45 resistance=53.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=29.62 liquidity=15987886.0 spike=0.22
- ADPC.CA: score=0.42 buy_ready=False sector_rank=17 price=3.12 support=2.85 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=4018893.0 spike=0.3
- AFDI.CA: score=3.5 buy_ready=False sector_rank=17 price=47.87 support=41.0 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=37.69 liquidity=1095039.38 spike=0.22
- AFMC.CA: score=10.73 buy_ready=False sector_rank=17 price=127.76 support=113.12 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=43.01 liquidity=8328149.5 spike=0.44
- AJWA.CA: score=11.09 buy_ready=False sector_rank=17 price=222.42 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=80.01 liquidity=6688236.5 spike=0.21
- ALCN.CA: score=9.12 buy_ready=False sector_rank=10 price=32.26 support=30.19 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=5970409.0 spike=0.22
- ALUM.CA: score=-1.76 buy_ready=False sector_rank=17 price=19.98 support=18.01 resistance=26.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=30.1 liquidity=1844184.75 spike=0.44
- AMER.CA: score=3.2 buy_ready=False sector_rank=14 price=4.3 support=4.19 resistance=4.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62433480.0 spike=1.24
- AMES.CA: score=13.4 buy_ready=False sector_rank=17 price=35.99 support=32.8 resistance=54.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=37.03 liquidity=15513910.0 spike=0.2
- AMIA.CA: score=7.27 buy_ready=False sector_rank=17 price=18.02 support=17.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=41.29 liquidity=1872761.63 spike=0.1
- AMOC.CA: score=4.8 buy_ready=False sector_rank=8 price=13.84 support=13.06 resistance=13.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=180082736.0 spike=1.52
- APSW.CA: score=1.87 buy_ready=False sector_rank=17 price=7.88 support=7.72 resistance=8.92 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=45.81 liquidity=465306.13 spike=0.74
- ARAB.CA: score=17.72 buy_ready=False sector_rank=14 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=68.6 liquidity=45632356.0 spike=0.42
- ARCC.CA: score=14.18 buy_ready=False sector_rank=6 price=66.78 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=57.83 liquidity=14022482.0 spike=0.32
- AREH.CA: score=4.12 buy_ready=False sector_rank=17 price=1.15 support=1.09 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=2715340.0 spike=0.33
- ASCM.CA: score=6.74 buy_ready=False sector_rank=17 price=47.64 support=44.25 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=25.14 liquidity=10572434.0 spike=1.17
- ASPI.CA: score=11.4 buy_ready=False sector_rank=17 price=0.32 support=0.3 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=40.96 liquidity=11520343.0 spike=0.46
- ATLC.CA: score=7.03 buy_ready=False sector_rank=11 price=5.16 support=4.72 resistance=7.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=43.49 liquidity=4087419.5 spike=0.55
- ATQA.CA: score=12.4 buy_ready=False sector_rank=16 price=10.9 support=10.15 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=37.42 liquidity=33104200.0 spike=0.5
- AXPH.CA: score=-0.64 buy_ready=False sector_rank=17 price=1318.33 support=1200.12 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=25.29 liquidity=1964064.75 spike=0.3
- BINV.CA: score=12.39 buy_ready=False sector_rank=5 price=59.17 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=3091197.25 spike=0.21
- BIOC.CA: score=12.4 buy_ready=False sector_rank=17 price=285.05 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=63.3 liquidity=23735284.0 spike=0.22
- BTFH.CA: score=11.94 buy_ready=False sector_rank=11 price=2.7 support=2.55 resistance=3.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=21856752.0 spike=0.22
- CAED.CA: score=6.8 buy_ready=False sector_rank=17 price=94.53 support=90.01 resistance=132.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=40.5 liquidity=4404582.5 spike=0.54
- CANA.CA: score=7.52 buy_ready=False sector_rank=15 price=41.14 support=38.1 resistance=49.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=28.65 liquidity=17936464.0 spike=0.98
- CCAP.CA: score=17.3 buy_ready=False sector_rank=5 price=6.3 support=5.87 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=389237248.0 spike=0.69
- CCRS.CA: score=0.87 buy_ready=False sector_rank=17 price=2.0 support=1.88 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8413182.0 spike=1.03
- CEFM.CA: score=3.17 buy_ready=False sector_rank=17 price=128.77 support=113.0 resistance=148.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=50.13 liquidity=768910.0 spike=0.33
- CERA.CA: score=11.4 buy_ready=False sector_rank=17 price=1.23 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=57393396.0 spike=0.47
- CFGH.CA: score=-3.6 buy_ready=False sector_rank=17 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=16.67 liquidity=4237.99 spike=0.71
- CICH.CA: score=2.59 buy_ready=False sector_rank=11 price=10.82 support=9.63 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=42.43 liquidity=648152.19 spike=0.19
- CIEB.CA: score=0.19 buy_ready=False sector_rank=15 price=22.63 support=21.4 resistance=25.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=31.74 liquidity=3676047.25 spike=0.38
- CIRA.CA: score=-0.26 buy_ready=False sector_rank=18 price=36.51 support=33.15 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=34.31 liquidity=2344465.5 spike=0.11
- CLHO.CA: score=6.75 buy_ready=False sector_rank=13 price=13.96 support=13.0 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=32.66 liquidity=12282490.0 spike=0.32
- CNFN.CA: score=11.74 buy_ready=False sector_rank=11 price=4.05 support=3.72 resistance=4.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=50.31 liquidity=7795235.5 spike=0.89
- COMI.CA: score=13.52 buy_ready=False sector_rank=15 price=124.92 support=120.0 resistance=133.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=37.67 liquidity=244064368.0 spike=0.48
- COPR.CA: score=7.99 buy_ready=False sector_rank=17 price=0.44 support=0.41 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=45.68 liquidity=5592889.0 spike=0.3
- COSG.CA: score=4.95 buy_ready=False sector_rank=17 price=1.4 support=1.29 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=3553733.25 spike=0.25
- CPCI.CA: score=9.53 buy_ready=False sector_rank=17 price=587.36 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=55.79 liquidity=2134993.0 spike=0.47
- CSAG.CA: score=14.02 buy_ready=False sector_rank=10 price=34.2 support=33.68 resistance=39.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=9852315.0 spike=1.51
- DAPH.CA: score=11.4 buy_ready=False sector_rank=17 price=84.64 support=82.0 resistance=121.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=38.36 liquidity=15829813.0 spike=0.37
- DEIN.CA: score=5.4 buy_ready=False sector_rank=17 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=2.76 buy_ready=False sector_rank=9 price=23.22 support=22.5 resistance=26.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=36.81 liquidity=600221.5 spike=0.14
- DSCW.CA: score=2.49 buy_ready=False sector_rank=17 price=1.55 support=1.45 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=34.69 liquidity=6085720.5 spike=0.36
- DTPP.CA: score=12.4 buy_ready=False sector_rank=17 price=246.0 support=225.0 resistance=349.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=37.54 liquidity=16252864.0 spike=0.31
- EALR.CA: score=4.7 buy_ready=False sector_rank=17 price=300.24 support=270.0 resistance=384.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=6839943.5 spike=1.73
- EASB.CA: score=-2.88 buy_ready=False sector_rank=17 price=7.06 support=6.05 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4722520.0 spike=0.92
- EAST.CA: score=9.34 buy_ready=False sector_rank=9 price=28.72 support=27.01 resistance=32.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=42.84 liquidity=5186014.0 spike=0.13
- EBSC.CA: score=-4.25 buy_ready=False sector_rank=17 price=1.6 support=1.44 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2751708.0 spike=1.3
- ECAP.CA: score=-2.5 buy_ready=False sector_rank=17 price=27.99 support=25.7 resistance=32.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=24.82 liquidity=1098039.13 spike=0.27
- EDFM.CA: score=3.18 buy_ready=False sector_rank=17 price=386.09 support=335.2 resistance=425.0 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=57.38 liquidity=783376.6 spike=0.66
- EEII.CA: score=-2.96 buy_ready=False sector_rank=17 price=1.86 support=1.71 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=24.62 liquidity=635105.06 spike=0.07
- EFIC.CA: score=11.4 buy_ready=False sector_rank=16 price=153.99 support=140.0 resistance=194.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=24369756.0 spike=0.8
- EFID.CA: score=11.59 buy_ready=False sector_rank=9 price=18.51 support=16.98 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=40.46 liquidity=7435579.5 spike=0.16
- EFIH.CA: score=20.71 buy_ready=False sector_rank=3 price=23.8 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=57.73 liquidity=19158874.0 spike=0.29
- EGAL.CA: score=7.4 buy_ready=False sector_rank=16 price=301.81 support=275.0 resistance=373.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=27.81 liquidity=55729284.0 spike=0.71
- EGAS.CA: score=0.24 buy_ready=False sector_rank=8 price=51.19 support=47.0 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=30.81 liquidity=1480225.88 spike=0.18
- EGBE.CA: score=2.57 buy_ready=False sector_rank=15 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=49.37 liquidity=54522.36 spike=0.42
- EGCH.CA: score=6.4 buy_ready=False sector_rank=16 price=11.8 support=10.67 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=24.69 liquidity=58255696.0 spike=0.77
- EGSA.CA: score=11.23 buy_ready=False sector_rank=1 price=9.03 support=8.75 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:22 AM market time freshness=DELAYED_CURRENT RSI=34.48 liquidity=13545.0 spike=1.91
- EGTS.CA: score=0.86 buy_ready=False sector_rank=14 price=13.25 support=12.06 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=18.84 liquidity=4134632.5 spike=0.12
- EHDR.CA: score=4.17 buy_ready=False sector_rank=17 price=2.28 support=2.07 resistance=2.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=40.21 liquidity=2772981.25 spike=0.25
- ELEC.CA: score=12.18 buy_ready=False sector_rank=2 price=1.79 support=1.65 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=209010320.0 spike=5.92
- ELKA.CA: score=10.02 buy_ready=False sector_rank=17 price=1.47 support=1.38 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8620433.0 spike=0.65
- ELNA.CA: score=6.14 buy_ready=False sector_rank=17 price=35.22 support=33.46 resistance=36.39 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=201352.75 spike=1.27
- ELSH.CA: score=12.4 buy_ready=False sector_rank=17 price=10.57 support=10.0 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=40.52 liquidity=11204785.0 spike=0.57
- ELWA.CA: score=6.41 buy_ready=False sector_rank=17 price=1.65 support=1.43 resistance=1.73 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=61.29 liquidity=6147.9 spike=0.01
- EMFD.CA: score=12.72 buy_ready=False sector_rank=14 price=12.0 support=11.2 resistance=13.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=42.02 liquidity=44198676.0 spike=0.77
- ENGC.CA: score=-0.61 buy_ready=False sector_rank=17 price=32.09 support=30.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=2988814.25 spike=0.19
- EOSB.CA: score=5.38 buy_ready=False sector_rank=17 price=1.57 support=1.57 resistance=1.64 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=57774.43 spike=1.46
- EPCO.CA: score=1.52 buy_ready=False sector_rank=17 price=8.8 support=8.32 resistance=9.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7696331.0 spike=1.71
- EPPK.CA: score=-7.18 buy_ready=False sector_rank=17 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=141.95 support=129.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=55.92 liquidity=92428808.0 spike=0.38
- ETRS.CA: score=5.67 buy_ready=False sector_rank=17 price=10.41 support=9.61 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=51.1 liquidity=3270637.75 spike=0.32
- EXPA.CA: score=6.52 buy_ready=False sector_rank=15 price=14.49 support=12.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=20.17 liquidity=16976584.0 spike=0.45
- FAIT.CA: score=4.29 buy_ready=False sector_rank=15 price=43.09 support=38.48 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=46.28 liquidity=1769417.38 spike=0.62
- FAITA.CA: score=5.37 buy_ready=False sector_rank=15 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=51.09 liquidity=49125.48 spike=1.4
- FERC.CA: score=-4.38 buy_ready=False sector_rank=16 price=67.73 support=64.8 resistance=68.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3215557.25 spike=0.87
- FWRY.CA: score=14.71 buy_ready=False sector_rank=3 price=18.36 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=19855538.0 spike=0.18
- GBCO.CA: score=5.0 buy_ready=False sector_rank=7 price=27.92 support=27.8 resistance=30.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=150512064.0 spike=1.48
- GDWA.CA: score=11.4 buy_ready=False sector_rank=17 price=0.61 support=0.57 resistance=0.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=35.96 liquidity=12172318.0 spike=0.66
- GGCC.CA: score=12.27 buy_ready=False sector_rank=17 price=0.64 support=0.61 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=42.64 liquidity=9870227.0 spike=0.6
- GIHD.CA: score=6.4 buy_ready=False sector_rank=17 price=47.82 support=45.46 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=16.63 liquidity=13762007.0 spike=0.73
- GMCI.CA: score=1.46 buy_ready=False sector_rank=17 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=46.67 liquidity=62907.46 spike=0.17
- GRCA.CA: score=0.37 buy_ready=False sector_rank=17 price=30.0 support=26.91 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=31.72 liquidity=1969330.0 spike=0.28
- GSSC.CA: score=3.42 buy_ready=False sector_rank=17 price=264.29 support=246.0 resistance=322.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=46.32 liquidity=1021099.38 spike=0.63
- HDBK.CA: score=6.52 buy_ready=False sector_rank=15 price=95.23 support=90.26 resistance=120.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=27.11 liquidity=10134519.0 spike=0.5
- HELI.CA: score=12.72 buy_ready=False sector_rank=14 price=6.91 support=6.63 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=36.18 liquidity=54055552.0 spike=0.7
- HRHO.CA: score=13.94 buy_ready=False sector_rank=11 price=24.93 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=19407348.0 spike=0.14
- ICID.CA: score=7.75 buy_ready=False sector_rank=17 price=16.99 support=16.0 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=46.24 liquidity=2352360.75 spike=0.29
- IDRE.CA: score=3.39 buy_ready=False sector_rank=17 price=41.29 support=38.17 resistance=59.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=35.82 liquidity=1986711.88 spike=0.26
- IFAP.CA: score=-1.72 buy_ready=False sector_rank=21 price=18.2 support=17.17 resistance=20.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=29.5 liquidity=1884398.13 spike=0.29
- INFI.CA: score=16.42 buy_ready=False sector_rank=17 price=129.5 support=104.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=59.7 liquidity=19676038.0 spike=1.01
- IRON.CA: score=4.82 buy_ready=False sector_rank=16 price=26.08 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=51.47 liquidity=3420461.5 spike=0.33
- ISMA.CA: score=7.44 buy_ready=False sector_rank=17 price=21.71 support=18.91 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=38.92 liquidity=6035690.5 spike=0.84
- ISMQ.CA: score=8.38 buy_ready=False sector_rank=16 price=7.45 support=6.61 resistance=9.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=40.32 liquidity=6976723.0 spike=0.38
- ISPH.CA: score=6.75 buy_ready=False sector_rank=13 price=10.65 support=10.03 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=31.32 liquidity=19513834.0 spike=0.42
- JUFO.CA: score=1.71 buy_ready=False sector_rank=9 price=23.4 support=22.1 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=32.71 liquidity=4556588.5 spike=0.26
- KABO.CA: score=8.62 buy_ready=False sector_rank=20 price=7.15 support=6.32 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=36.89 liquidity=6224160.0 spike=0.28
- KWIN.CA: score=-0.31 buy_ready=False sector_rank=17 price=65.86 support=58.12 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=24.96 liquidity=3292171.25 spike=0.43
- KZPC.CA: score=13.36 buy_ready=False sector_rank=17 price=13.3 support=12.15 resistance=14.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=43.56 liquidity=5961686.5 spike=0.77
- LCSW.CA: score=8.82 buy_ready=False sector_rank=6 price=32.52 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=59.66 liquidity=4631492.0 spike=0.23
- LUTS.CA: score=12.4 buy_ready=False sector_rank=17 price=0.71 support=0.63 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=36.52 liquidity=19106722.0 spike=0.34
- MAAL.CA: score=7.4 buy_ready=False sector_rank=17 price=7.96 support=7.0 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=21.8 liquidity=15810135.0 spike=0.62
- MASR.CA: score=12.4 buy_ready=False sector_rank=17 price=7.1 support=6.66 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=49.63 liquidity=11579254.0 spike=0.22
- MBSC.CA: score=14.18 buy_ready=False sector_rank=6 price=337.03 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=57.93 liquidity=55969012.0 spike=0.62
- MCQE.CA: score=4.18 buy_ready=False sector_rank=6 price=171.62 support=163.21 resistance=177.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37514384.0 spike=0.63
- MCRO.CA: score=11.4 buy_ready=False sector_rank=17 price=1.34 support=1.21 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=38.6 liquidity=30337390.0 spike=0.57
- MENA.CA: score=7.4 buy_ready=False sector_rank=14 price=5.99 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=3031393.25 spike=1.82
- MEPA.CA: score=5.9 buy_ready=False sector_rank=17 price=1.55 support=1.47 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=4502457.0 spike=0.54
- MFPC.CA: score=17.72 buy_ready=False sector_rank=16 price=46.01 support=40.66 resistance=50.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=65131652.0 spike=1.16
- MFSC.CA: score=-3.08 buy_ready=False sector_rank=17 price=37.99 support=33.1 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=20.49 liquidity=517885.53 spike=0.26
- MHOT.CA: score=10.46 buy_ready=False sector_rank=12 price=15.78 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=42.45 liquidity=8521159.0 spike=0.5
- MICH.CA: score=2.84 buy_ready=False sector_rank=17 price=42.85 support=40.4 resistance=43.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10627782.0 spike=1.22
- MILS.CA: score=1.75 buy_ready=False sector_rank=17 price=150.37 support=134.01 resistance=203.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=32.37 liquidity=4350245.5 spike=0.57
- MIPH.CA: score=3.47 buy_ready=False sector_rank=13 price=742.47 support=666.66 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=41.33 liquidity=719801.31 spike=0.08
- MOED.CA: score=-0.17 buy_ready=False sector_rank=17 price=0.57 support=0.52 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=33.74 liquidity=3428746.25 spike=0.21
- MOIL.CA: score=-1.2 buy_ready=False sector_rank=8 price=0.67 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=29.7 liquidity=34516.27 spike=0.12
- MOIN.CA: score=3.18 buy_ready=False sector_rank=17 price=30.13 support=28.71 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=29.55 liquidity=5783294.0 spike=0.6
- MOSC.CA: score=3.33 buy_ready=False sector_rank=17 price=258.04 support=228.05 resistance=312.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=928891.88 spike=0.31
- MPCI.CA: score=12.4 buy_ready=False sector_rank=17 price=307.03 support=271.0 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=35.87 liquidity=81501264.0 spike=0.77
- MPCO.CA: score=7.4 buy_ready=False sector_rank=21 price=2.01 support=1.79 resistance=2.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=25.53 liquidity=68286416.0 spike=0.62
- MPRC.CA: score=11.21 buy_ready=False sector_rank=17 price=35.04 support=32.01 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=38.75 liquidity=8810600.0 spike=0.52
- MTIE.CA: score=14.16 buy_ready=False sector_rank=7 price=7.53 support=7.05 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=36.49 liquidity=29197232.0 spike=1.56
- NAHO.CA: score=3.59 buy_ready=False sector_rank=17 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=51165.92 spike=1.57
- NCCW.CA: score=6.4 buy_ready=False sector_rank=17 price=5.59 support=5.05 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=10277653.0 spike=0.29
- NEDA.CA: score=-0.47 buy_ready=False sector_rank=17 price=2.6 support=2.47 resistance=2.79 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=134323.8 spike=0.21
- NHPS.CA: score=-1.99 buy_ready=False sector_rank=17 price=61.59 support=56.13 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=31.28 liquidity=1609600.75 spike=0.11
- NINH.CA: score=0.68 buy_ready=False sector_rank=17 price=15.28 support=14.13 resistance=21.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=20.16 liquidity=4283082.5 spike=0.36
- NIPH.CA: score=12.75 buy_ready=False sector_rank=13 price=282.45 support=230.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=49.31 liquidity=126566544.0 spike=0.93
- OBRI.CA: score=4.92 buy_ready=False sector_rank=17 price=25.52 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=53.77 liquidity=3523989.75 spike=0.24
- OCDI.CA: score=3.88 buy_ready=False sector_rank=14 price=26.17 support=24.6 resistance=26.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62831060.0 spike=1.58
- OCPH.CA: score=3.04 buy_ready=False sector_rank=17 price=193.22 support=185.93 resistance=246.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=42.37 liquidity=1638916.25 spike=0.48
- ODIN.CA: score=5.62 buy_ready=False sector_rank=17 price=2.24 support=1.91 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=40.18 liquidity=3220442.75 spike=0.42
- OFH.CA: score=12.4 buy_ready=False sector_rank=17 price=0.75 support=0.69 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=10586017.0 spike=0.12
- OIH.CA: score=14.3 buy_ready=False sector_rank=5 price=1.75 support=1.7 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=33815220.0 spike=0.45
- OLFI.CA: score=5.52 buy_ready=False sector_rank=9 price=20.0 support=19.4 resistance=22.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=23.98 liquidity=8363659.0 spike=0.51
- ORAS.CA: score=4.6 buy_ready=False sector_rank=4 price=863.46 support=851.0 resistance=870.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93333216.0 spike=1.0
- ORHD.CA: score=8.72 buy_ready=False sector_rank=14 price=10.09 support=9.5 resistance=43.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=24.44 liquidity=85531864.0 spike=0.59
- ORWE.CA: score=9.8 buy_ready=False sector_rank=20 price=26.4 support=25.01 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=43.06 liquidity=7397464.5 spike=0.17
- PHAR.CA: score=12.75 buy_ready=False sector_rank=13 price=104.96 support=98.05 resistance=119.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=20038490.0 spike=0.31
- PHDC.CA: score=14.72 buy_ready=False sector_rank=14 price=12.3 support=12.2 resistance=13.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=38.25 liquidity=49225332.0 spike=0.56
- PHTV.CA: score=5.6 buy_ready=False sector_rank=17 price=330.0 support=310.02 resistance=370.0 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=41.08 liquidity=1498200.0 spike=1.85
- POUL.CA: score=17.5 buy_ready=False sector_rank=9 price=10.09 support=9.12 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=62.34 liquidity=107313568.0 spike=2.67
- PRCL.CA: score=4.48 buy_ready=False sector_rank=6 price=21.8 support=20.5 resistance=22.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11343997.0 spike=1.15
- PRDC.CA: score=8.05 buy_ready=False sector_rank=14 price=6.12 support=5.72 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=37.88 liquidity=6325454.0 spike=0.18
- PRMH.CA: score=2.58 buy_ready=False sector_rank=17 price=2.03 support=1.8 resistance=2.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=1181899.25 spike=0.34
- RACC.CA: score=-3.21 buy_ready=False sector_rank=17 price=8.51 support=8.1 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4387233.5 spike=0.7
- RAKT.CA: score=1.47 buy_ready=False sector_rank=17 price=22.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=49.81 liquidity=68518.36 spike=0.2
- RAYA.CA: score=7.48 buy_ready=False sector_rank=19 price=5.85 support=5.36 resistance=7.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=42.6 liquidity=6082199.0 spike=0.18
- RMDA.CA: score=12.75 buy_ready=False sector_rank=13 price=5.06 support=4.8 resistance=6.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=12293441.0 spike=0.45
- ROTO.CA: score=-1.11 buy_ready=False sector_rank=17 price=35.3 support=33.3 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=33.75 liquidity=2494727.75 spike=0.29
- RREI.CA: score=1.96 buy_ready=False sector_rank=17 price=3.3 support=3.21 resistance=4.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=5563626.5 spike=0.77
- RTVC.CA: score=2.44 buy_ready=False sector_rank=17 price=3.29 support=3.1 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=35.48 liquidity=1039855.13 spike=0.4
- RUBX.CA: score=2.4 buy_ready=False sector_rank=17 price=17.8 support=16.8 resistance=17.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57723992.0 spike=0.56
- SAUD.CA: score=9.59 buy_ready=False sector_rank=15 price=20.8 support=20.2 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=39.75 liquidity=7073200.0 spike=0.33
- SCEM.CA: score=18.18 buy_ready=False sector_rank=6 price=87.15 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=60.18 liquidity=40909644.0 spike=0.64
- SCFM.CA: score=2.66 buy_ready=False sector_rank=17 price=225.24 support=200.22 resistance=275.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=1255561.38 spike=0.69
- SCTS.CA: score=-2.23 buy_ready=False sector_rank=18 price=473.77 support=420.11 resistance=606.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=27.72 liquidity=368118.44 spike=0.39
- SDTI.CA: score=13.14 buy_ready=False sector_rank=17 price=83.0 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=7740571.5 spike=0.27
- SEIG.CA: score=2.95 buy_ready=False sector_rank=17 price=200.6 support=173.1 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=43.63 liquidity=552148.44 spike=0.27
- SIPC.CA: score=17.4 buy_ready=False sector_rank=17 price=5.6 support=4.22 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=20473912.0 spike=0.36
- SKPC.CA: score=6.4 buy_ready=False sector_rank=16 price=15.55 support=14.4 resistance=18.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=30.63 liquidity=46882724.0 spike=0.66
- SMFR.CA: score=3.42 buy_ready=False sector_rank=17 price=198.85 support=180.11 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=38.09 liquidity=2021715.25 spike=0.64
- SNFC.CA: score=8.31 buy_ready=False sector_rank=17 price=11.17 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=47.88 liquidity=2910949.75 spike=0.29
- SPIN.CA: score=1.0 buy_ready=False sector_rank=20 price=13.99 support=13.5 resistance=17.79 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=25.67 liquidity=4600597.43 spike=0.85
- SPMD.CA: score=13.4 buy_ready=False sector_rank=17 price=0.38 support=0.34 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=51.45 liquidity=11249553.0 spike=0.76
- SUGR.CA: score=9.45 buy_ready=False sector_rank=9 price=55.35 support=50.5 resistance=59.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=53.05 liquidity=2298953.5 spike=0.24
- SVCE.CA: score=12.4 buy_ready=False sector_rank=17 price=9.31 support=8.41 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=42799448.0 spike=0.55
- SWDY.CA: score=17.18 buy_ready=False sector_rank=2 price=110.91 support=101.5 resistance=127.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=37589652.0 spike=0.59
- TALM.CA: score=10.47 buy_ready=False sector_rank=18 price=19.9 support=18.28 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=56.29 liquidity=5068385.0 spike=0.15
- TMGH.CA: score=6.72 buy_ready=False sector_rank=14 price=82.99 support=80.01 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=23.45 liquidity=116025920.0 spike=0.54
- TRTO.CA: score=-0.6 buy_ready=False sector_rank=17 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=4886.31 spike=0.55
- UEFM.CA: score=3.11 buy_ready=False sector_rank=17 price=480.03 support=407.57 resistance=550.0 source=Yahoo Finance as_of=2026-10-18T21:00:00+00:00 freshness=FRESH RSI=62.99 liquidity=1709866.86 spike=0.55
- UEGC.CA: score=15.4 buy_ready=False sector_rank=17 price=1.56 support=1.34 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=18395926.0 spike=0.36
- UNIP.CA: score=4.79 buy_ready=False sector_rank=17 price=0.32 support=0.29 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=42.14 liquidity=3390534.25 spike=0.39
- UNIT.CA: score=3.07 buy_ready=False sector_rank=14 price=16.67 support=15.6 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=346254.75 spike=0.08
- WCDF.CA: score=-2.6 buy_ready=False sector_rank=17 price=502.64 support=432.5 resistance=698.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=22.51 liquidity=996578.63 spike=0.34
- WKOL.CA: score=7.4 buy_ready=False sector_rank=17 price=286.55 support=271.0 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32898390.0 spike=5.3
- ZEOT.CA: score=8.35 buy_ready=False sector_rank=17 price=11.13 support=9.75 resistance=13.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=46.7 liquidity=5945095.5 spike=0.77
- ZMID.CA: score=7.72 buy_ready=False sector_rank=14 price=6.89 support=6.4 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=27.98 liquidity=31072150.0 spike=0.35

## Backtesting Lite
- ETEL.CA: 180d return=78.69%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-18T21:00:00+00:00
- EFIH.CA: 180d return=9.97%, max drawdown=-22.68%, MA20>MA50 days last20=3, as_of=2026-10-18T21:00:00+00:00
- SCEM.CA: 180d return=47.76%, max drawdown=-29.64%, MA20>MA50 days last20=8, as_of=2026-10-18T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=657 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- SIPC.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2484 sources=3 expected=Sabaa International Company for Pharmaceutical and Chemical Industry summary=Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue; FRA approves Sabaa Pharmaceutical&#39;s capital raise; Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results
  - Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue: https://english.mubasher.info/news/3809286/Sabaa-Pharmaceutical-s-shareholders-approve-capital-raise-via-bonus-issue/
  - FRA approves Sabaa Pharmaceutical&#39;s capital raise: https://english.mubasher.info/news/3789753/FRA-approves-Sabaa-Pharmaceutical-s-capital-raise/
  - Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results: https://english.mubasher.info/news/3779465/Sabaa-Pharmaceutical-s-profit-leaps-76-in-2020-initial-results/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.

## Warnings
- OpenRouter API error: 404
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
