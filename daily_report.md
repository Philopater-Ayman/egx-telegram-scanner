# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-21T10:36:27.458839+00:00
Generated Cairo: 2026-10-21 13:36
Run timing: target 08:45 Cairo | generated Cairo 2026-10-21 13:36 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-21 13:33

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 179/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, October 21
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 38.89% / above MA50 22.22%
- EGX70 regime: BEARISH / above MA20 12.82% / above MA50 10.26%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- TMGH.CA: liquidity=757614272.0 spike=3.56 score=8.95
- COMI.CA: liquidity=354354272.0 spike=0.74 score=16.32
- PHDC.CA: liquidity=207894016.0 spike=2.33 score=20.61
- CCAP.CA: liquidity=141761760.0 spike=0.26 score=17.58
- ORHD.CA: liquidity=124400640.0 spike=0.85 score=9.95

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- MENA.CA: spike=4.12 liquidity=8474621.73 outlook=NEUTRAL score=48 buy_ready=False
- TMGH.CA: spike=3.56 liquidity=757614272.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PHDC.CA: spike=2.33 liquidity=207894016.0 outlook=CONSTRUCTIVE score=60 buy_ready=False
- EGSA.CA: spike=1.88 liquidity=13545.0 outlook=CONSTRUCTIVE score=64.07 buy_ready=False
- ECAP.CA: spike=1.86 liquidity=7167113.0 outlook=WEAK_OR_RISKY score=21 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=8.07 5d=-0.73% 20d=3.03% aboveMA50=100.0%
- #2 Fintech & Payments: score=4.24 5d=1.2% 20d=2.1% aboveMA50=50.0%
- #3 Energy & Petrochemicals: score=1.67 5d=0.74% 20d=-5.0% aboveMA50=33.33%
- #4 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #5 Investment Holding: score=1.45 5d=-0.56% 20d=-10.24% aboveMA50=66.67%
- #6 Building Materials: score=1.27 5d=1.56% 20d=-4.12% aboveMA50=0.0%
- #7 Food, Beverages & Tobacco: score=0.33 5d=2.3% 20d=-10.17% aboveMA50=0.0%
- #8 Industrial Goods & Cables: score=0.3 5d=0.0% 20d=-5.75% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ETEL.CA: BULLISH_WATCH score=94.07 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- AMOC.CA: BULLISH_WATCH score=87.67 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=84.24 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- BINV.CA: BULLISH_WATCH score=76.45 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- KZPC.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- MFPC.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- EGSA.CA: CONSTRUCTIVE score=64.07 liquidity=THIN sector=LEADING risk=liquidity below minimum; momentum is extended; close to resistance
- PHDC.CA: CONSTRUCTIVE score=60 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA50; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=59 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- ABUK.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=close to resistance; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=7.99 buy_ready=False sector_rank=18 price=230.5 support=201.0 resistance=309.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=38.03 liquidity=4811326.5 spike=0.45
- ABUK.CA: score=20.68 buy_ready=False sector_rank=12 price=94.51 support=80.5 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=66723468.0 spike=0.88
- ACAMD.CA: score=17.18 buy_ready=False sector_rank=18 price=2.03 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=18456092.0 spike=0.39
- ACGC.CA: score=7.82 buy_ready=False sector_rank=13 price=13.0 support=12.5 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=4312847.0 spike=0.39
- ADCI.CA: score=3.73 buy_ready=False sector_rank=18 price=257.64 support=241.55 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=37.1 liquidity=554645.19 spike=0.31
- ADIB.CA: score=8.32 buy_ready=False sector_rank=14 price=46.77 support=43.45 resistance=52.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=35075664.0 spike=0.49
- ADPC.CA: score=3.66 buy_ready=False sector_rank=18 price=3.07 support=2.85 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=33.63 liquidity=6483074.0 spike=0.53
- AFDI.CA: score=3.74 buy_ready=False sector_rank=18 price=47.87 support=41.0 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=39.97 liquidity=561458.63 spike=0.12
- AFMC.CA: score=0.59 buy_ready=False sector_rank=18 price=124.87 support=113.12 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=2409018.25 spike=0.13
- AJWA.CA: score=15.18 buy_ready=False sector_rank=18 price=224.0 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=81.26 liquidity=22938518.0 spike=0.72
- ALCN.CA: score=14.19 buy_ready=False sector_rank=11 price=32.7 support=30.19 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=7253332.5 spike=0.3
- ALUM.CA: score=4.21 buy_ready=False sector_rank=18 price=20.43 support=18.01 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=35.98 liquidity=2026794.25 spike=0.51
- AMER.CA: score=13.95 buy_ready=False sector_rank=10 price=4.27 support=3.8 resistance=5.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=50.78 liquidity=24138264.0 spike=0.46
- AMES.CA: score=9.18 buy_ready=False sector_rank=18 price=35.69 support=32.8 resistance=53.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=34.81 liquidity=23034232.0 spike=0.36
- AMIA.CA: score=7.01 buy_ready=False sector_rank=18 price=17.9 support=17.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=49.81 liquidity=3826585.75 spike=0.22
- AMOC.CA: score=20.67 buy_ready=False sector_rank=3 price=13.6 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=51.83 liquidity=42725776.0 spike=0.35
- APSW.CA: score=2.51 buy_ready=False sector_rank=18 price=7.85 support=7.72 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=47.57 liquidity=327652.13 spike=0.55
- ARAB.CA: score=18.95 buy_ready=False sector_rank=10 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=68.33 liquidity=31358120.0 spike=0.29
- ARCC.CA: score=14.51 buy_ready=False sector_rank=6 price=66.5 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=59.35 liquidity=13111356.0 spike=0.3
- AREH.CA: score=6.56 buy_ready=False sector_rank=18 price=1.14 support=1.09 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=4376979.5 spike=0.55
- ASCM.CA: score=7.52 buy_ready=False sector_rank=18 price=48.0 support=44.25 resistance=61.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=30.55 liquidity=10732632.0 spike=1.17
- ASPI.CA: score=12.18 buy_ready=False sector_rank=18 price=0.32 support=0.3 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=46.54 liquidity=13945008.0 spike=0.62
- ATLC.CA: score=5.25 buy_ready=False sector_rank=17 price=5.06 support=4.72 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=2007511.0 spike=0.28
- ATQA.CA: score=14.28 buy_ready=False sector_rank=12 price=10.96 support=10.15 resistance=13.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=42.42 liquidity=71969544.0 spike=1.3
- AXPH.CA: score=2.94 buy_ready=False sector_rank=18 price=1294.95 support=1200.12 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=28.68 liquidity=4759326.0 spike=0.74
- BINV.CA: score=19.58 buy_ready=False sector_rank=5 price=59.05 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=51.7 liquidity=11239694.0 spike=0.8
- BIOC.CA: score=13.18 buy_ready=False sector_rank=18 price=274.61 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=14786791.0 spike=0.13
- BTFH.CA: score=14.24 buy_ready=False sector_rank=17 price=2.66 support=2.55 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=58295960.0 spike=0.6
- CAED.CA: score=0.9 buy_ready=False sector_rank=18 price=92.22 support=90.01 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=30.63 liquidity=2716323.75 spike=0.34
- CANA.CA: score=8.32 buy_ready=False sector_rank=14 price=42.32 support=38.1 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=33.47 liquidity=14148250.0 spike=0.83
- CCAP.CA: score=17.58 buy_ready=False sector_rank=5 price=6.3 support=5.87 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=39.9 liquidity=141761760.0 spike=0.26
- CCRS.CA: score=-0.85 buy_ready=False sector_rank=18 price=1.94 support=1.78 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=32.22 liquidity=1974936.13 spike=0.27
- CEFM.CA: score=4.2 buy_ready=False sector_rank=18 price=128.21 support=113.0 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=42.08 liquidity=1016069.31 spike=0.48
- CERA.CA: score=13.18 buy_ready=False sector_rank=18 price=1.24 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=107555432.0 spike=0.89
- CFGH.CA: score=-2.82 buy_ready=False sector_rank=18 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=16.67 liquidity=318.0 spike=0.06
- CICH.CA: score=2.76 buy_ready=False sector_rank=17 price=10.84 support=9.63 resistance=12.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=40.59 liquidity=516436.75 spike=0.19
- CIEB.CA: score=5.29 buy_ready=False sector_rank=14 price=22.51 support=21.4 resistance=25.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=2966190.25 spike=0.32
- CIRA.CA: score=5.73 buy_ready=False sector_rank=21 price=36.15 support=33.15 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=43.19 liquidity=3330188.25 spike=0.18
- CLHO.CA: score=7.25 buy_ready=False sector_rank=16 price=13.91 support=13.0 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=30.65 liquidity=19930070.0 spike=0.55
- CNFN.CA: score=8.61 buy_ready=False sector_rank=17 price=4.05 support=3.72 resistance=4.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=4367928.5 spike=0.49
- COMI.CA: score=16.32 buy_ready=False sector_rank=14 price=128.25 support=120.0 resistance=133.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=42.85 liquidity=354354272.0 spike=0.74
- COPR.CA: score=10.66 buy_ready=False sector_rank=18 price=0.43 support=0.41 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=45.4 liquidity=7479042.5 spike=0.44
- COSG.CA: score=6.86 buy_ready=False sector_rank=18 price=1.38 support=1.29 resistance=1.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=40.32 liquidity=4675360.5 spike=0.36
- CPCI.CA: score=11.43 buy_ready=False sector_rank=18 price=593.0 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=3251690.5 spike=0.72
- CSAG.CA: score=7.42 buy_ready=False sector_rank=11 price=35.06 support=33.68 resistance=39.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=46.08 liquidity=3481219.0 spike=0.52
- DAPH.CA: score=12.18 buy_ready=False sector_rank=18 price=84.85 support=82.0 resistance=115.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=39.61 liquidity=23870286.0 spike=0.56
- DEIN.CA: score=6.18 buy_ready=False sector_rank=18 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-1.41 buy_ready=False sector_rank=7 price=23.29 support=22.5 resistance=26.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=34.96 liquidity=462776.88 spike=0.12
- DSCW.CA: score=8.12 buy_ready=False sector_rank=18 price=1.53 support=1.45 resistance=1.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=37.25 liquidity=5941403.5 spike=0.37
- DTPP.CA: score=3.18 buy_ready=False sector_rank=18 price=232.06 support=229.0 resistance=249.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18915494.0 spike=0.37
- EALR.CA: score=-1.08 buy_ready=False sector_rank=18 price=296.7 support=270.0 resistance=381.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=34.58 liquidity=1736197.0 spike=0.44
- EASB.CA: score=5.53 buy_ready=False sector_rank=18 price=6.71 support=5.6 resistance=8.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=47.66 liquidity=2349723.25 spike=0.43
- EAST.CA: score=17.15 buy_ready=False sector_rank=7 price=29.7 support=27.01 resistance=32.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=50.38 liquidity=37684716.0 spike=1.01
- EBSC.CA: score=3.25 buy_ready=False sector_rank=18 price=1.52 support=1.33 resistance=2.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=1066144.62 spike=0.51
- ECAP.CA: score=11.07 buy_ready=False sector_rank=18 price=28.51 support=25.7 resistance=32.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=7167113.0 spike=1.86
- EDFM.CA: score=3.49 buy_ready=False sector_rank=18 price=387.71 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=49.98 liquidity=313661.13 spike=0.28
- EEII.CA: score=-0.22 buy_ready=False sector_rank=18 price=1.84 support=1.71 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=31.15 liquidity=2598698.5 spike=0.32
- EFIC.CA: score=14.68 buy_ready=False sector_rank=12 price=158.76 support=140.0 resistance=187.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=22007518.0 spike=0.75
- EFID.CA: score=15.13 buy_ready=False sector_rank=7 price=18.6 support=16.98 resistance=20.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=17645932.0 spike=0.39
- EFIH.CA: score=22.7 buy_ready=False sector_rank=2 price=24.0 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=60.13 liquidity=17045832.0 spike=0.26
- EGAL.CA: score=8.68 buy_ready=False sector_rank=12 price=303.97 support=275.0 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=52689320.0 spike=0.66
- EGAS.CA: score=7.55 buy_ready=False sector_rank=3 price=51.33 support=47.0 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=1885354.25 spike=0.25
- EGBE.CA: score=3.34 buy_ready=False sector_rank=14 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=42.5 liquidity=19239.89 spike=0.15
- EGCH.CA: score=7.68 buy_ready=False sector_rank=12 price=11.46 support=10.67 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=31.28 liquidity=51027440.0 spike=0.7
- EGSA.CA: score=18.17 buy_ready=False sector_rank=1 price=9.03 support=8.75 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 October 10:22 AM market time freshness=DELAYED_CURRENT RSI=66.07 liquidity=13545.0 spike=1.88
- EGTS.CA: score=7.95 buy_ready=False sector_rank=10 price=13.15 support=12.06 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=20.75 liquidity=13912486.0 spike=0.4
- EHDR.CA: score=8.76 buy_ready=False sector_rank=18 price=2.24 support=2.07 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=40.21 liquidity=6579296.5 spike=0.64
- ELEC.CA: score=5.3 buy_ready=False sector_rank=8 price=1.68 support=1.67 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=71095880.0 spike=1.59
- ELKA.CA: score=9.86 buy_ready=False sector_rank=18 price=1.49 support=1.38 resistance=1.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7680501.5 spike=0.59
- ELNA.CA: score=6.49 buy_ready=False sector_rank=18 price=35.22 support=33.46 resistance=35.8 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=170605.69 spike=1.07
- ELSH.CA: score=14.14 buy_ready=False sector_rank=18 price=10.7 support=10.0 resistance=12.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=43.73 liquidity=28400142.0 spike=1.48
- ELWA.CA: score=2.25 buy_ready=False sector_rank=18 price=1.65 support=1.43 resistance=1.73 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=79.17 liquidity=65668.35 spike=0.17
- EMFD.CA: score=13.95 buy_ready=False sector_rank=10 price=12.08 support=11.2 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=48.64 liquidity=31110522.0 spike=0.53
- ENGC.CA: score=8.62 buy_ready=False sector_rank=18 price=32.98 support=30.0 resistance=43.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=6444035.5 spike=0.5
- EOSB.CA: score=5.18 buy_ready=False sector_rank=18 price=1.57 support=1.57 resistance=1.64 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3331.54 spike=0.09
- EPCO.CA: score=4.54 buy_ready=False sector_rank=18 price=8.83 support=7.7 resistance=11.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=2357926.0 spike=0.52
- EPPK.CA: score=-6.4 buy_ready=False sector_rank=18 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=141.92 support=129.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=58.8 liquidity=108205056.0 spike=0.46
- ETRS.CA: score=12.17 buy_ready=False sector_rank=18 price=10.55 support=9.61 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=59.46 liquidity=6987159.0 spike=0.7
- EXPA.CA: score=3.29 buy_ready=False sector_rank=14 price=14.15 support=12.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=25.71 liquidity=5967925.5 spike=0.17
- FAIT.CA: score=3.97 buy_ready=False sector_rank=14 price=43.44 support=38.48 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=645042.81 spike=0.22
- FAITA.CA: score=5.33 buy_ready=False sector_rank=14 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=52.22 liquidity=4080.07 spike=0.12
- FERC.CA: score=-0.32 buy_ready=False sector_rank=12 price=65.53 support=60.51 resistance=79.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=1998973.0 spike=0.55
- FWRY.CA: score=16.7 buy_ready=False sector_rank=2 price=18.47 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=55.52 liquidity=22924000.0 spike=0.2
- GBCO.CA: score=12.29 buy_ready=False sector_rank=15 price=27.1 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=41.42 liquidity=79241560.0 spike=0.74
- GDWA.CA: score=7.9 buy_ready=False sector_rank=18 price=0.61 support=0.57 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=42.13 liquidity=5718241.5 spike=0.33
- GGCC.CA: score=12.66 buy_ready=False sector_rank=18 price=0.62 support=0.61 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=44.89 liquidity=9478042.0 spike=0.57
- GIHD.CA: score=7.18 buy_ready=False sector_rank=18 price=47.65 support=45.46 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=16.76 liquidity=11800060.0 spike=0.63
- GMCI.CA: score=2.33 buy_ready=False sector_rank=18 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=55.26 liquidity=151012.4 spike=0.41
- GRCA.CA: score=8.77 buy_ready=False sector_rank=18 price=30.13 support=26.91 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=4590264.0 spike=0.72
- GSSC.CA: score=3.69 buy_ready=False sector_rank=18 price=263.55 support=246.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=50.1 liquidity=505491.22 spike=0.35
- HDBK.CA: score=7.32 buy_ready=False sector_rank=14 price=98.46 support=90.26 resistance=119.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=17937534.0 spike=0.9
- HELI.CA: score=13.95 buy_ready=False sector_rank=10 price=7.01 support=6.63 resistance=8.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=53317524.0 spike=0.73
- HRHO.CA: score=12.24 buy_ready=False sector_rank=17 price=24.84 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=58.85 liquidity=30575450.0 spike=0.23
- ICID.CA: score=6.7 buy_ready=False sector_rank=18 price=17.0 support=16.0 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=3515189.75 spike=0.45
- IDRE.CA: score=3.58 buy_ready=False sector_rank=18 price=41.02 support=38.17 resistance=56.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=41.09 liquidity=1403993.75 spike=0.22
- IFAP.CA: score=2.76 buy_ready=False sector_rank=20 price=18.17 support=17.17 resistance=20.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=37.64 liquidity=1060589.25 spike=0.18
- INFI.CA: score=17.18 buy_ready=False sector_rank=18 price=125.67 support=104.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=12997727.0 spike=0.64
- IRON.CA: score=6.73 buy_ready=False sector_rank=12 price=25.77 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=50.8 liquidity=4051232.5 spike=0.39
- ISMA.CA: score=5.13 buy_ready=False sector_rank=18 price=21.46 support=18.91 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=2952561.75 spike=0.41
- ISMQ.CA: score=8.82 buy_ready=False sector_rank=12 price=7.49 support=6.61 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=46.83 liquidity=6141923.5 spike=0.34
- ISPH.CA: score=7.25 buy_ready=False sector_rank=16 price=10.53 support=10.03 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=33.42 liquidity=21688614.0 spike=0.48
- JUFO.CA: score=10.25 buy_ready=False sector_rank=7 price=24.08 support=22.1 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=7120102.0 spike=0.43
- KABO.CA: score=7.61 buy_ready=False sector_rank=13 price=7.61 support=6.32 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=4094887.0 spike=0.18
- KWIN.CA: score=-1.71 buy_ready=False sector_rank=18 price=63.47 support=58.12 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=31.02 liquidity=1110782.88 spike=0.15
- KZPC.CA: score=12.71 buy_ready=False sector_rank=18 price=13.38 support=12.15 resistance=14.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=4525070.0 spike=0.57
- LCSW.CA: score=12.3 buy_ready=False sector_rank=6 price=33.28 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=62.56 liquidity=3789870.0 spike=0.19
- LUTS.CA: score=12.18 buy_ready=False sector_rank=18 price=0.68 support=0.63 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=37.47 liquidity=16769616.0 spike=0.31
- MAAL.CA: score=-1.69 buy_ready=False sector_rank=18 price=7.39 support=7.3 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5134922.5 spike=0.2
- MASR.CA: score=13.18 buy_ready=False sector_rank=18 price=7.09 support=6.66 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=46.27 liquidity=19085182.0 spike=0.38
- MBSC.CA: score=14.51 buy_ready=False sector_rank=6 price=329.11 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=58.15 liquidity=32749380.0 spike=0.35
- MCQE.CA: score=13.51 buy_ready=False sector_rank=6 price=172.75 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=44.98 liquidity=19939672.0 spike=0.33
- MCRO.CA: score=13.18 buy_ready=False sector_rank=18 price=1.36 support=1.21 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=40.68 liquidity=13007961.0 spike=0.24
- MENA.CA: score=17.42 buy_ready=False sector_rank=10 price=5.99 support=5.57 resistance=7.05 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=45.21 liquidity=8474621.73 spike=4.12
- MEPA.CA: score=5.95 buy_ready=False sector_rank=18 price=1.54 support=1.47 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=47.95 liquidity=3765638.25 spike=0.5
- MFPC.CA: score=18.9 buy_ready=False sector_rank=12 price=47.0 support=40.66 resistance=50.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=50842140.0 spike=1.11
- MFSC.CA: score=-1.86 buy_ready=False sector_rank=18 price=36.11 support=33.1 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=22.86 liquidity=956561.25 spike=0.51
- MHOT.CA: score=5.06 buy_ready=False sector_rank=9 price=15.52 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=2093576.63 spike=0.12
- MICH.CA: score=9.47 buy_ready=False sector_rank=18 price=42.64 support=35.5 resistance=45.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=56.72 liquidity=4294406.0 spike=0.49
- MILS.CA: score=0.61 buy_ready=False sector_rank=18 price=147.43 support=134.01 resistance=201.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=26.1 liquidity=2426153.25 spike=0.32
- MIPH.CA: score=5.56 buy_ready=False sector_rank=16 price=748.53 support=666.66 resistance=941.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=41.45 liquidity=2305977.0 spike=0.45
- MOED.CA: score=6.24 buy_ready=False sector_rank=18 price=0.56 support=0.52 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=37.35 liquidity=4057029.5 spike=0.29
- MOIL.CA: score=0.68 buy_ready=False sector_rank=3 price=0.66 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=28.3 liquidity=8848.04 spike=0.03
- MOIN.CA: score=1.0 buy_ready=False sector_rank=18 price=30.03 support=28.71 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=30.4 liquidity=2815623.25 spike=0.3
- MOSC.CA: score=5.4 buy_ready=False sector_rank=18 price=255.52 support=228.05 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=2219249.75 spike=0.67
- MPCI.CA: score=13.18 buy_ready=False sector_rank=18 price=304.19 support=271.0 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=50539912.0 spike=0.48
- MPCO.CA: score=12.7 buy_ready=False sector_rank=20 price=2.02 support=1.79 resistance=2.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=75607824.0 spike=0.74
- MPRC.CA: score=12.97 buy_ready=False sector_rank=18 price=34.6 support=32.01 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=9789190.0 spike=0.59
- MTIE.CA: score=12.73 buy_ready=False sector_rank=15 price=7.6 support=7.05 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=23452524.0 spike=1.22
- NAHO.CA: score=3.19 buy_ready=False sector_rank=18 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=12513.54 spike=0.53
- NCCW.CA: score=7.18 buy_ready=False sector_rank=18 price=5.43 support=5.05 resistance=7.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=28.72 liquidity=11427086.0 spike=0.33
- NEDA.CA: score=0.38 buy_ready=False sector_rank=18 price=2.6 support=2.47 resistance=2.77 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=197217.79 spike=0.32
- NHPS.CA: score=3.28 buy_ready=False sector_rank=18 price=62.22 support=56.13 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=34.87 liquidity=6099791.0 spike=0.43
- NINH.CA: score=1.21 buy_ready=False sector_rank=18 price=15.01 support=14.13 resistance=20.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=18.23 liquidity=4031102.25 spike=0.36
- NIPH.CA: score=13.25 buy_ready=False sector_rank=16 price=272.17 support=230.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=65198844.0 spike=0.48
- OBRI.CA: score=8.09 buy_ready=False sector_rank=18 price=25.58 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=5910345.0 spike=0.4
- OCDI.CA: score=17.95 buy_ready=False sector_rank=10 price=26.54 support=22.6 resistance=29.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=18890732.0 spike=0.5
- OCPH.CA: score=3.19 buy_ready=False sector_rank=18 price=190.71 support=185.93 resistance=246.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=38.84 liquidity=1009713.25 spike=0.32
- ODIN.CA: score=6.92 buy_ready=False sector_rank=18 price=2.23 support=1.91 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=39.09 liquidity=3743567.0 spike=0.51
- OFH.CA: score=13.18 buy_ready=False sector_rank=18 price=0.75 support=0.69 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=35.58 liquidity=27109084.0 spike=0.32
- OIH.CA: score=14.58 buy_ready=False sector_rank=5 price=1.77 support=1.7 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=36376212.0 spike=0.48
- OLFI.CA: score=2.41 buy_ready=False sector_rank=7 price=19.94 support=19.4 resistance=22.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=19.09 liquidity=4273169.5 spike=0.29
- ORAS.CA: score=4.6 buy_ready=False sector_rank=4 price=855.86 support=855.2 resistance=880.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49604264.0 spike=1.0
- ORHD.CA: score=9.95 buy_ready=False sector_rank=10 price=10.41 support=9.5 resistance=43.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=27.92 liquidity=124400640.0 spike=0.85
- ORWE.CA: score=13.51 buy_ready=False sector_rank=13 price=25.9 support=25.01 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=46.48 liquidity=17760082.0 spike=0.42
- PHAR.CA: score=13.25 buy_ready=False sector_rank=16 price=103.48 support=98.05 resistance=119.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=44.61 liquidity=22903914.0 spike=0.36
- PHDC.CA: score=20.61 buy_ready=False sector_rank=10 price=13.0 support=12.2 resistance=13.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=53.24 liquidity=207894016.0 spike=2.33
- PHTV.CA: score=3.43 buy_ready=False sector_rank=18 price=330.0 support=310.02 resistance=370.0 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=48.24 liquidity=246510.0 spike=0.31
- POUL.CA: score=15.85 buy_ready=False sector_rank=7 price=9.85 support=9.12 resistance=38.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=64113616.0 spike=1.36
- PRCL.CA: score=15.17 buy_ready=False sector_rank=6 price=22.47 support=19.02 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=39.6 liquidity=17935890.0 spike=1.83
- PRDC.CA: score=5.17 buy_ready=False sector_rank=10 price=6.49 support=6.22 resistance=6.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55672800.0 spike=1.61
- PRMH.CA: score=2.97 buy_ready=False sector_rank=18 price=2.0 support=1.8 resistance=2.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=40.34 liquidity=790764.06 spike=0.24
- RACC.CA: score=4.68 buy_ready=False sector_rank=18 price=8.47 support=7.93 resistance=9.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=42.51 liquidity=2503363.5 spike=0.39
- RAKT.CA: score=8.36 buy_ready=False sector_rank=18 price=22.69 support=20.26 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=58.41 liquidity=483519.75 spike=1.35
- RAYA.CA: score=10.14 buy_ready=False sector_rank=19 price=5.93 support=5.36 resistance=7.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=42.6 liquidity=8308077.5 spike=0.25
- RMDA.CA: score=12.17 buy_ready=False sector_rank=16 price=5.18 support=4.8 resistance=6.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=8918787.0 spike=0.32
- ROTO.CA: score=3.11 buy_ready=False sector_rank=18 price=34.72 support=33.3 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=38.79 liquidity=925950.5 spike=0.11
- RREI.CA: score=8.91 buy_ready=False sector_rank=18 price=3.21 support=3.21 resistance=4.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=39.07 liquidity=6725278.0 spike=0.96
- RTVC.CA: score=3.7 buy_ready=False sector_rank=18 price=3.24 support=3.1 resistance=3.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=1523407.63 spike=0.6
- RUBX.CA: score=18.18 buy_ready=False sector_rank=18 price=17.86 support=13.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=57334720.0 spike=0.61
- SAUD.CA: score=11.77 buy_ready=False sector_rank=14 price=21.08 support=20.2 resistance=25.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=8446132.0 spike=0.61
- SCEM.CA: score=18.51 buy_ready=False sector_rank=6 price=86.87 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=64.17 liquidity=15048355.0 spike=0.24
- SCFM.CA: score=-2.34 buy_ready=False sector_rank=18 price=223.94 support=200.22 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=30.89 liquidity=477038.5 spike=0.27
- SCTS.CA: score=-0.42 buy_ready=False sector_rank=21 price=448.35 support=420.11 resistance=600.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=27.29 liquidity=1601862.63 spike=1.79
- SDTI.CA: score=15.98 buy_ready=False sector_rank=18 price=82.95 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=49.74 liquidity=9803993.0 spike=0.35
- SEIG.CA: score=3.73 buy_ready=False sector_rank=18 price=197.16 support=173.1 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=40.85 liquidity=545939.56 spike=0.27
- SIPC.CA: score=18.18 buy_ready=False sector_rank=18 price=5.4 support=4.22 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=17026056.0 spike=0.3
- SKPC.CA: score=12.68 buy_ready=False sector_rank=12 price=15.44 support=14.4 resistance=18.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=48.26 liquidity=32489458.0 spike=0.46
- SMFR.CA: score=4.47 buy_ready=False sector_rank=18 price=200.43 support=180.11 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=2287186.5 spike=0.74
- SNFC.CA: score=4.62 buy_ready=False sector_rank=18 price=11.02 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=1437954.13 spike=0.15
- SPIN.CA: score=0.79 buy_ready=False sector_rank=13 price=14.06 support=13.5 resistance=17.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=34.82 liquidity=3277532.5 spike=0.65
- SPMD.CA: score=7.64 buy_ready=False sector_rank=18 price=0.37 support=0.34 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=52.21 liquidity=3455851.0 spike=0.25
- SUGR.CA: score=9.96 buy_ready=False sector_rank=7 price=55.71 support=50.5 resistance=59.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=58.8 liquidity=1829082.13 spike=0.2
- SVCE.CA: score=13.18 buy_ready=False sector_rank=18 price=9.2 support=8.41 resistance=11.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=44.16 liquidity=25072538.0 spike=0.35
- SWDY.CA: score=14.12 buy_ready=False sector_rank=8 price=110.96 support=101.5 resistance=126.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=21585334.0 spike=0.34
- TALM.CA: score=10.45 buy_ready=False sector_rank=21 price=19.35 support=18.28 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=50.8 liquidity=8053545.5 spike=0.26
- TMGH.CA: score=8.95 buy_ready=False sector_rank=10 price=90.02 support=89.04 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=757614272.0 spike=3.56
- TRTO.CA: score=-1.82 buy_ready=False sector_rank=18 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=2707.83 spike=0.37
- UEFM.CA: score=2.62 buy_ready=False sector_rank=18 price=478.48 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=39.68 liquidity=440522.94 spike=0.15
- UEGC.CA: score=14.18 buy_ready=False sector_rank=18 price=1.53 support=1.34 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=57.65 liquidity=19024786.0 spike=0.4
- UNIP.CA: score=6.77 buy_ready=False sector_rank=18 price=0.31 support=0.29 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=46.25 liquidity=4591296.0 spike=0.56
- UNIT.CA: score=5.18 buy_ready=False sector_rank=10 price=17.2 support=15.6 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=49.72 liquidity=1227070.38 spike=0.31
- WCDF.CA: score=-2.07 buy_ready=False sector_rank=18 price=497.95 support=432.5 resistance=686.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=28.73 liquidity=747591.06 spike=0.28
- WKOL.CA: score=6.06 buy_ready=False sector_rank=18 price=279.07 support=241.1 resistance=343.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=42.91 liquidity=3876030.5 spike=0.53
- ZEOT.CA: score=8.07 buy_ready=False sector_rank=18 price=11.25 support=9.75 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=49.32 liquidity=4888088.0 spike=0.62
- ZMID.CA: score=13.95 buy_ready=False sector_rank=10 price=6.96 support=6.4 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=27341306.0 spike=0.33

## Backtesting Lite
- ETEL.CA: 180d return=80.08%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-19T21:00:00+00:00
- EFIH.CA: 180d return=12.83%, max drawdown=-22.68%, MA20>MA50 days last20=2, as_of=2026-10-19T21:00:00+00:00
- ABUK.CA: 180d return=73.43%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- PHDC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=658 sources=3 expected=Palm Hills Development summary=Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma; Palm Hills records 30% higher profits in 2025, unveils new project in UAE; Strong momentum pushes Palm Hills toward EGP 10.15
  - Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma: https://english.mubasher.info/news/4598123/Palm-Hills-UAE-s-Miran-to-launch-new-development-project-in-Ras-Al-Hikma/
  - Palm Hills records 30% higher profits in 2025, unveils new project in UAE: https://english.mubasher.info/news/4580548/Palm-Hills-records-30-higher-profits-in-2025-unveils-new-project-in-UAE/
  - Strong momentum pushes Palm Hills toward EGP 10.15: https://english.mubasher.info/news/4560871/Strong-momentum-pushes-Palm-Hills-toward-EGP-10-15/
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.

## Warnings
- OpenRouter API error: 404
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for PHDC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
