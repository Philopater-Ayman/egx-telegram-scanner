# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-10-21T11:43:56.186495+00:00
Generated Cairo: 2026-10-21 14:43
Run timing: target 09:15 Cairo | generated Cairo 2026-10-21 14:43 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-10-21 14:41

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 177/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, October 21
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 27.78% / above MA50 22.22%
- EGX70 regime: BEARISH / above MA20 10.26% / above MA50 10.26%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- TMGH.CA: liquidity=898184256.0 spike=4.22 score=8.95
- COMI.CA: liquidity=437458048.0 spike=0.91 score=16.82
- PHDC.CA: liquidity=253940528.0 spike=2.85 score=19.65
- ETEL.CA: liquidity=237884848.0 spike=1.01 score=22.42
- CCAP.CA: liquidity=234610272.0 spike=0.43 score=17.35

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- TMGH.CA: spike=4.22 liquidity=898184256.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PHDC.CA: spike=2.85 liquidity=253940528.0 outlook=NEUTRAL score=42 buy_ready=False
- SCTS.CA: spike=2.53 liquidity=2269687.75 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EAST.CA: spike=2.5 liquidity=93128488.0 outlook=CONSTRUCTIVE score=61.54 buy_ready=False
- RAKT.CA: spike=2.34 liquidity=840102.25 outlook=NEUTRAL score=47 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=7.29 5d=-0.73% 20d=3.03% aboveMA50=100.0%
- #2 Fintech & Payments: score=4.42 5d=1.2% 20d=2.1% aboveMA50=50.0%
- #3 Energy & Petrochemicals: score=1.76 5d=0.74% 20d=-5.0% aboveMA50=33.33%
- #4 Building Materials: score=1.5 5d=1.56% 20d=-4.12% aboveMA50=0.0%
- #5 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Investment Holding: score=0.88 5d=-0.56% 20d=-10.24% aboveMA50=66.67%
- #7 Industrial Goods & Cables: score=0.57 5d=0.0% 20d=-5.75% aboveMA50=0.0%
- #8 Food, Beverages & Tobacco: score=0.54 5d=2.3% 20d=-10.17% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- AMOC.CA: BULLISH_WATCH score=87.76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=84.42 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MFPC.CA: BULLISH_WATCH score=82 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=sector is not leading
- ETEL.CA: BULLISH_WATCH score=80.29 liquidity=TRADEABLE sector=LEADING risk=below MA20
- KZPC.CA: BULLISH_WATCH score=76 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- ABUK.CA: BULLISH_WATCH score=70 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=close to resistance; sector is not leading
- BINV.CA: CONSTRUCTIVE score=63.88 liquidity=TRADEABLE sector=IMPROVING risk=below MA20
- EGSA.CA: CONSTRUCTIVE score=63.29 liquidity=THIN sector=LEADING risk=liquidity below minimum; momentum is extended; close to resistance
- EAST.CA: CONSTRUCTIVE score=61.54 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; sector is not leading
- CPCI.CA: CONSTRUCTIVE score=59 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=11.36 buy_ready=False sector_rank=19 price=229.12 support=201.0 resistance=309.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.03 liquidity=8138599.0 spike=0.76
- ABUK.CA: score=21.82 buy_ready=False sector_rank=13 price=94.59 support=80.5 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.0 liquidity=114438336.0 spike=1.51
- ACAMD.CA: score=17.22 buy_ready=False sector_rank=19 price=2.03 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=29456808.0 spike=0.62
- ACGC.CA: score=11.99 buy_ready=False sector_rank=14 price=13.26 support=12.5 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=8301026.5 spike=0.76
- ADCI.CA: score=3.95 buy_ready=False sector_rank=19 price=256.19 support=241.55 resistance=288.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.1 liquidity=723605.69 spike=0.4
- ADIB.CA: score=8.82 buy_ready=False sector_rank=12 price=46.92 support=43.45 resistance=52.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=52500652.0 spike=0.73
- ADPC.CA: score=5.52 buy_ready=False sector_rank=19 price=3.06 support=2.85 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.63 liquidity=8293871.5 spike=0.67
- AFDI.CA: score=4.92 buy_ready=False sector_rank=19 price=47.0 support=41.0 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.97 liquidity=1692456.25 spike=0.36
- AFMC.CA: score=1.76 buy_ready=False sector_rank=19 price=123.58 support=113.12 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=3540016.0 spike=0.19
- AJWA.CA: score=17.22 buy_ready=False sector_rank=19 price=220.85 support=176.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=81.26 liquidity=63413864.0 spike=2.0
- ALCN.CA: score=17.04 buy_ready=False sector_rank=9 price=32.41 support=30.19 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=13225935.0 spike=0.54
- ALUM.CA: score=4.84 buy_ready=False sector_rank=19 price=20.75 support=18.01 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=35.98 liquidity=2612893.25 spike=0.65
- AMER.CA: score=13.95 buy_ready=False sector_rank=11 price=4.23 support=3.8 resistance=5.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.78 liquidity=31089840.0 spike=0.59
- AMES.CA: score=9.22 buy_ready=False sector_rank=19 price=35.29 support=32.8 resistance=53.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.81 liquidity=29586764.0 spike=0.46
- AMIA.CA: score=8.04 buy_ready=False sector_rank=19 price=17.94 support=17.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.81 liquidity=4820676.5 spike=0.27
- AMOC.CA: score=20.7 buy_ready=False sector_rank=3 price=13.62 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.83 liquidity=61554212.0 spike=0.5
- APSW.CA: score=2.58 buy_ready=False sector_rank=19 price=7.85 support=7.72 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.57 liquidity=351226.09 spike=0.59
- ARAB.CA: score=18.95 buy_ready=False sector_rank=11 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=68.33 liquidity=53340608.0 spike=0.49
- ARCC.CA: score=14.6 buy_ready=False sector_rank=4 price=66.33 support=60.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=59.35 liquidity=16127680.0 spike=0.37
- AREH.CA: score=7.71 buy_ready=False sector_rank=19 price=1.13 support=1.09 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=5488756.0 spike=0.68
- ASCM.CA: score=8.38 buy_ready=False sector_rank=19 price=48.04 support=44.25 resistance=61.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.55 liquidity=14443337.0 spike=1.58
- ASPI.CA: score=12.22 buy_ready=False sector_rank=19 price=0.32 support=0.3 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.54 liquidity=20200616.0 spike=0.9
- ATLC.CA: score=5.93 buy_ready=False sector_rank=18 price=5.05 support=4.72 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=2628478.5 spike=0.37
- ATQA.CA: score=15.38 buy_ready=False sector_rank=13 price=10.58 support=10.15 resistance=13.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.42 liquidity=99450328.0 spike=1.79
- AXPH.CA: score=3.95 buy_ready=False sector_rank=19 price=1303.15 support=1200.12 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.68 liquidity=5729274.0 spike=0.9
- BINV.CA: score=17.99 buy_ready=False sector_rank=6 price=58.05 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.7 liquidity=18450814.0 spike=1.32
- BIOC.CA: score=13.22 buy_ready=False sector_rank=19 price=273.44 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=18210058.0 spike=0.17
- BTFH.CA: score=14.3 buy_ready=False sector_rank=18 price=2.64 support=2.55 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=73324984.0 spike=0.75
- CAED.CA: score=1.78 buy_ready=False sector_rank=19 price=91.8 support=90.01 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.63 liquidity=3552670.5 spike=0.44
- CANA.CA: score=4.9 buy_ready=False sector_rank=12 price=43.98 support=41.26 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26154008.0 spike=1.54
- CCAP.CA: score=17.35 buy_ready=False sector_rank=6 price=6.26 support=5.87 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.9 liquidity=234610272.0 spike=0.43
- CCRS.CA: score=0.28 buy_ready=False sector_rank=19 price=2.0 support=1.78 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.22 liquidity=3053751.75 spike=0.42
- CEFM.CA: score=4.28 buy_ready=False sector_rank=19 price=128.24 support=113.0 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=42.08 liquidity=1051986.25 spike=0.5
- CERA.CA: score=12.3 buy_ready=False sector_rank=19 price=1.23 support=1.18 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=125568136.0 spike=1.04
- CFGH.CA: score=-2.78 buy_ready=False sector_rank=19 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=16.67 liquidity=318.0 spike=0.06
- CICH.CA: score=2.89 buy_ready=False sector_rank=18 price=10.83 support=9.63 resistance=12.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.59 liquidity=586245.19 spike=0.22
- CIEB.CA: score=7.46 buy_ready=False sector_rank=12 price=22.65 support=21.4 resistance=25.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.92 liquidity=4644729.5 spike=0.5
- CIRA.CA: score=9.36 buy_ready=False sector_rank=15 price=35.91 support=33.15 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.19 liquidity=5683489.0 spike=0.31
- CLHO.CA: score=7.34 buy_ready=False sector_rank=17 price=13.89 support=13.0 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.65 liquidity=23659710.0 spike=0.65
- CNFN.CA: score=13.18 buy_ready=False sector_rank=18 price=4.08 support=3.72 resistance=4.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=53.8 liquidity=8877857.0 spike=1.0
- COMI.CA: score=16.82 buy_ready=False sector_rank=12 price=128.34 support=120.0 resistance=133.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.85 liquidity=437458048.0 spike=0.91
- COPR.CA: score=13.22 buy_ready=False sector_rank=19 price=0.43 support=0.41 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.4 liquidity=10007030.0 spike=0.59
- COSG.CA: score=8.47 buy_ready=False sector_rank=19 price=1.38 support=1.29 resistance=1.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.32 liquidity=6250483.5 spike=0.47
- CPCI.CA: score=11.73 buy_ready=False sector_rank=19 price=592.51 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=3507170.0 spike=0.78
- CSAG.CA: score=8.28 buy_ready=False sector_rank=9 price=34.9 support=33.68 resistance=39.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.08 liquidity=4239067.0 spike=0.63
- DAPH.CA: score=12.22 buy_ready=False sector_rank=19 price=84.7 support=82.0 resistance=115.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.61 liquidity=26736064.0 spike=0.63
- DEIN.CA: score=6.22 buy_ready=False sector_rank=19 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-1.22 buy_ready=False sector_rank=8 price=23.31 support=22.5 resistance=26.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=34.96 liquidity=566909.44 spike=0.15
- DSCW.CA: score=9.24 buy_ready=False sector_rank=19 price=1.54 support=1.45 resistance=1.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.25 liquidity=7015306.5 spike=0.43
- DTPP.CA: score=13.22 buy_ready=False sector_rank=19 price=237.19 support=225.0 resistance=349.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.32 liquidity=30701388.0 spike=0.61
- EALR.CA: score=-0.95 buy_ready=False sector_rank=19 price=296.87 support=270.0 resistance=381.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.58 liquidity=1827051.38 spike=0.47
- EASB.CA: score=-3.95 buy_ready=False sector_rank=19 price=6.55 support=6.52 resistance=7.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2830700.0 spike=0.52
- EAST.CA: score=20.22 buy_ready=False sector_rank=8 price=30.01 support=27.01 resistance=32.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.38 liquidity=93128488.0 spike=2.5
- EBSC.CA: score=3.61 buy_ready=False sector_rank=19 price=1.52 support=1.33 resistance=2.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=1389116.62 spike=0.66
- ECAP.CA: score=13.53 buy_ready=False sector_rank=19 price=28.0 support=25.7 resistance=32.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=8764498.0 spike=2.27
- EDFM.CA: score=3.65 buy_ready=False sector_rank=19 price=387.66 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=49.98 liquidity=430838.13 spike=0.39
- EEII.CA: score=1.37 buy_ready=False sector_rank=19 price=1.8 support=1.71 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.15 liquidity=4150735.5 spike=0.51
- EFIC.CA: score=14.8 buy_ready=False sector_rank=13 price=158.17 support=140.0 resistance=187.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=27051672.0 spike=0.92
- EFID.CA: score=15.22 buy_ready=False sector_rank=8 price=18.7 support=16.98 resistance=20.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=23855754.0 spike=0.53
- EFIH.CA: score=22.77 buy_ready=False sector_rank=2 price=23.9 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.13 liquidity=26689020.0 spike=0.41
- EGAL.CA: score=8.8 buy_ready=False sector_rank=13 price=303.22 support=275.0 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=61103108.0 spike=0.76
- EGAS.CA: score=8.05 buy_ready=False sector_rank=3 price=51.19 support=47.0 resistance=60.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=2350100.75 spike=0.31
- EGBE.CA: score=3.84 buy_ready=False sector_rank=12 price=0.5 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=42.5 liquidity=19239.89 spike=0.15
- EGCH.CA: score=7.8 buy_ready=False sector_rank=13 price=11.48 support=10.67 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.28 liquidity=60518184.0 spike=0.84
- EGSA.CA: score=19.01 buy_ready=False sector_rank=1 price=9.03 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=66.07 liquidity=13545.0 spike=2.3
- EGTS.CA: score=7.95 buy_ready=False sector_rank=11 price=12.94 support=12.06 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=20.75 liquidity=15104206.0 spike=0.44
- EHDR.CA: score=12.44 buy_ready=False sector_rank=19 price=2.23 support=2.07 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.21 liquidity=11450205.0 spike=1.11
- ELEC.CA: score=6.03 buy_ready=False sector_rank=7 price=1.69 support=1.67 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=85240056.0 spike=1.9
- ELKA.CA: score=12.11 buy_ready=False sector_rank=19 price=1.48 support=1.38 resistance=1.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9889096.0 spike=0.76
- ELNA.CA: score=6.53 buy_ready=False sector_rank=19 price=35.22 support=33.46 resistance=35.8 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=170605.69 spike=1.07
- ELSH.CA: score=14.48 buy_ready=False sector_rank=19 price=10.54 support=10.0 resistance=12.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.73 liquidity=31326708.0 spike=1.63
- ELWA.CA: score=2.29 buy_ready=False sector_rank=19 price=1.65 support=1.43 resistance=1.73 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=79.17 liquidity=65668.35 spike=0.17
- EMFD.CA: score=13.95 buy_ready=False sector_rank=11 price=12.03 support=11.2 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.64 liquidity=40489224.0 spike=0.69
- ENGC.CA: score=9.79 buy_ready=False sector_rank=19 price=32.76 support=30.0 resistance=43.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=7563566.0 spike=0.58
- EOSB.CA: score=5.23 buy_ready=False sector_rank=19 price=1.57 support=1.57 resistance=1.64 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=3331.54 spike=0.09
- EPCO.CA: score=4.73 buy_ready=False sector_rank=19 price=8.8 support=7.7 resistance=11.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=2509983.75 spike=0.56
- EPPK.CA: score=-6.36 buy_ready=False sector_rank=19 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=22.42 buy_ready=False sector_rank=1 price=139.91 support=129.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.8 liquidity=237884848.0 spike=1.01
- ETRS.CA: score=15.38 buy_ready=False sector_rank=19 price=10.68 support=9.61 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.46 liquidity=10778449.0 spike=1.08
- EXPA.CA: score=7.82 buy_ready=False sector_rank=12 price=14.42 support=12.0 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.71 liquidity=13619523.0 spike=0.39
- FAIT.CA: score=5.88 buy_ready=False sector_rank=12 price=44.12 support=38.48 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=2060203.0 spike=0.71
- FAITA.CA: score=5.82 buy_ready=False sector_rank=12 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=52.22 liquidity=4080.07 spike=0.12
- FERC.CA: score=0.1 buy_ready=False sector_rank=13 price=65.9 support=60.51 resistance=79.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=2296434.0 spike=0.64
- FWRY.CA: score=16.77 buy_ready=False sector_rank=2 price=18.42 support=17.5 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.52 liquidity=31525422.0 spike=0.28
- GBCO.CA: score=13.18 buy_ready=False sector_rank=16 price=26.37 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.42 liquidity=140654352.0 spike=1.31
- GDWA.CA: score=10.26 buy_ready=False sector_rank=19 price=0.6 support=0.57 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.13 liquidity=8038852.0 spike=0.46
- GGCC.CA: score=13.22 buy_ready=False sector_rank=19 price=0.62 support=0.61 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.89 liquidity=11852758.0 spike=0.72
- GIHD.CA: score=7.22 buy_ready=False sector_rank=19 price=46.92 support=45.46 resistance=78.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=16.76 liquidity=15960668.0 spike=0.86
- GMCI.CA: score=2.38 buy_ready=False sector_rank=19 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=55.26 liquidity=151012.4 spike=0.41
- GRCA.CA: score=9.08 buy_ready=False sector_rank=19 price=30.07 support=26.91 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=4854083.5 spike=0.76
- GSSC.CA: score=4.0 buy_ready=False sector_rank=19 price=262.36 support=246.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=50.1 liquidity=771951.5 spike=0.53
- HDBK.CA: score=8.12 buy_ready=False sector_rank=12 price=98.94 support=90.26 resistance=119.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=22966578.0 spike=1.15
- HELI.CA: score=14.15 buy_ready=False sector_rank=11 price=7.1 support=6.63 resistance=8.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.48 liquidity=80304664.0 spike=1.1
- HRHO.CA: score=12.3 buy_ready=False sector_rank=18 price=24.89 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.85 liquidity=50933032.0 spike=0.38
- ICID.CA: score=10.93 buy_ready=False sector_rank=19 price=17.45 support=16.0 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=4702351.0 spike=0.6
- IDRE.CA: score=4.13 buy_ready=False sector_rank=19 price=40.83 support=38.17 resistance=56.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.09 liquidity=1904600.63 spike=0.3
- IFAP.CA: score=3.16 buy_ready=False sector_rank=21 price=18.19 support=17.17 resistance=20.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.64 liquidity=1359115.63 spike=0.23
- INFI.CA: score=17.22 buy_ready=False sector_rank=19 price=125.71 support=104.0 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=16813462.0 spike=0.83
- IRON.CA: score=13.92 buy_ready=False sector_rank=13 price=27.04 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.8 liquidity=16006057.0 spike=1.56
- ISMA.CA: score=6.6 buy_ready=False sector_rank=19 price=21.06 support=18.91 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=4380252.0 spike=0.6
- ISMQ.CA: score=10.58 buy_ready=False sector_rank=13 price=7.44 support=6.61 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.83 liquidity=7776931.0 spike=0.43
- ISPH.CA: score=7.34 buy_ready=False sector_rank=17 price=10.56 support=10.03 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.42 liquidity=30815230.0 spike=0.68
- JUFO.CA: score=13.22 buy_ready=False sector_rank=8 price=23.82 support=22.1 resistance=27.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=10412528.0 spike=0.63
- KABO.CA: score=10.09 buy_ready=False sector_rank=14 price=7.79 support=6.32 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=6406743.0 spike=0.29
- KWIN.CA: score=-1.09 buy_ready=False sector_rank=19 price=63.07 support=58.12 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.02 liquidity=1681972.25 spike=0.23
- KZPC.CA: score=18.88 buy_ready=False sector_rank=19 price=13.26 support=12.15 resistance=14.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=10485812.0 spike=1.33
- LCSW.CA: score=16.81 buy_ready=False sector_rank=4 price=33.3 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.56 liquidity=8212909.0 spike=0.41
- LUTS.CA: score=12.22 buy_ready=False sector_rank=19 price=0.67 support=0.63 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.47 liquidity=23857894.0 spike=0.44
- MAAL.CA: score=4.86 buy_ready=False sector_rank=19 price=7.5 support=7.0 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=23.03 liquidity=6638423.5 spike=0.26
- MASR.CA: score=13.22 buy_ready=False sector_rank=19 price=7.1 support=6.66 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.27 liquidity=23395556.0 spike=0.47
- MBSC.CA: score=14.6 buy_ready=False sector_rank=4 price=328.4 support=288.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=58.15 liquidity=63085848.0 spike=0.68
- MCQE.CA: score=13.6 buy_ready=False sector_rank=4 price=170.25 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.98 liquidity=31568412.0 spike=0.52
- MCRO.CA: score=12.22 buy_ready=False sector_rank=19 price=1.35 support=1.21 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.68 liquidity=21568000.0 spike=0.4
- MENA.CA: score=4.71 buy_ready=False sector_rank=11 price=5.94 support=5.57 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=757853.25 spike=0.37
- MEPA.CA: score=6.87 buy_ready=False sector_rank=19 price=1.54 support=1.47 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.95 liquidity=4643912.0 spike=0.61
- MFPC.CA: score=21.1 buy_ready=False sector_rank=13 price=47.51 support=40.66 resistance=50.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=97902104.0 spike=2.15
- MFSC.CA: score=-1.71 buy_ready=False sector_rank=19 price=36.87 support=33.1 resistance=49.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=22.86 liquidity=1062482.5 spike=0.56
- MHOT.CA: score=6.09 buy_ready=False sector_rank=10 price=15.62 support=15.08 resistance=19.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=3098915.5 spike=0.17
- MICH.CA: score=11.96 buy_ready=False sector_rank=19 price=43.0 support=35.5 resistance=45.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.72 liquidity=6732353.5 spike=0.77
- MILS.CA: score=1.03 buy_ready=False sector_rank=19 price=146.57 support=134.01 resistance=201.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.1 liquidity=2807851.5 spike=0.37
- MIPH.CA: score=8.38 buy_ready=False sector_rank=17 price=748.1 support=666.66 resistance=941.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.45 liquidity=5043088.5 spike=0.98
- MOED.CA: score=7.21 buy_ready=False sector_rank=19 price=0.56 support=0.52 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.35 liquidity=4988800.5 spike=0.36
- MOIL.CA: score=0.71 buy_ready=False sector_rank=3 price=0.66 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=28.3 liquidity=8887.45 spike=0.03
- MOIN.CA: score=1.94 buy_ready=False sector_rank=19 price=29.86 support=28.71 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.4 liquidity=3712793.25 spike=0.4
- MOSC.CA: score=6.33 buy_ready=False sector_rank=19 price=260.16 support=228.05 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=3101829.75 spike=0.94
- MPCI.CA: score=13.22 buy_ready=False sector_rank=19 price=302.3 support=271.0 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=55794844.0 spike=0.53
- MPCO.CA: score=12.84 buy_ready=False sector_rank=21 price=2.04 support=1.79 resistance=2.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=103694504.0 spike=1.02
- MPRC.CA: score=13.22 buy_ready=False sector_rank=19 price=34.34 support=32.01 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=10546661.0 spike=0.64
- MTIE.CA: score=13.68 buy_ready=False sector_rank=16 price=7.5 support=7.05 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=29999594.0 spike=1.56
- NAHO.CA: score=3.23 buy_ready=False sector_rank=19 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=10816.25 spike=0.46
- NCCW.CA: score=7.22 buy_ready=False sector_rank=19 price=5.43 support=5.05 resistance=7.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.72 liquidity=13658976.0 spike=0.4
- NEDA.CA: score=0.42 buy_ready=False sector_rank=19 price=2.6 support=2.47 resistance=2.77 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=197217.79 spike=0.32
- NHPS.CA: score=4.1 buy_ready=False sector_rank=19 price=61.94 support=56.13 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.87 liquidity=6878435.5 spike=0.49
- NINH.CA: score=2.56 buy_ready=False sector_rank=19 price=14.99 support=14.13 resistance=20.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=18.23 liquidity=5332022.5 spike=0.48
- NIPH.CA: score=13.34 buy_ready=False sector_rank=17 price=268.82 support=230.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=76653184.0 spike=0.56
- OBRI.CA: score=8.81 buy_ready=False sector_rank=19 price=25.48 support=22.8 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=6590187.0 spike=0.45
- OCDI.CA: score=15.95 buy_ready=False sector_rank=11 price=26.29 support=22.6 resistance=29.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=28143832.0 spike=0.75
- OCPH.CA: score=3.44 buy_ready=False sector_rank=19 price=190.43 support=185.93 resistance=246.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=38.84 liquidity=1220384.63 spike=0.38
- ODIN.CA: score=6.58 buy_ready=False sector_rank=19 price=2.21 support=1.91 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.09 liquidity=4353806.5 spike=0.59
- OFH.CA: score=13.22 buy_ready=False sector_rank=19 price=0.76 support=0.69 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.58 liquidity=31721500.0 spike=0.37
- OIH.CA: score=14.35 buy_ready=False sector_rank=6 price=1.78 support=1.7 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=57994228.0 spike=0.77
- OLFI.CA: score=4.18 buy_ready=False sector_rank=8 price=19.91 support=19.4 resistance=22.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=19.09 liquidity=5966562.0 spike=0.4
- ORAS.CA: score=4.6 buy_ready=False sector_rank=5 price=856.63 support=851.0 resistance=880.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=79849048.0 spike=1.0
- ORHD.CA: score=9.95 buy_ready=False sector_rank=11 price=10.32 support=9.5 resistance=43.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=27.92 liquidity=147515280.0 spike=1.0
- ORWE.CA: score=13.69 buy_ready=False sector_rank=14 price=25.81 support=25.01 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.48 liquidity=26922920.0 spike=0.64
- PHAR.CA: score=13.34 buy_ready=False sector_rank=17 price=103.19 support=98.05 resistance=119.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.61 liquidity=32726478.0 spike=0.52
- PHDC.CA: score=19.65 buy_ready=False sector_rank=11 price=12.95 support=12.2 resistance=13.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.24 liquidity=253940528.0 spike=2.85
- PHTV.CA: score=6.47 buy_ready=False sector_rank=19 price=338.52 support=310.02 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.24 liquidity=923427.31 spike=1.16
- POUL.CA: score=17.46 buy_ready=False sector_rank=8 price=9.8 support=9.12 resistance=38.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=100067096.0 spike=2.12
- PRCL.CA: score=15.56 buy_ready=False sector_rank=4 price=22.49 support=19.02 resistance=31.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.6 liquidity=19451428.0 spike=1.98
- PRDC.CA: score=5.69 buy_ready=False sector_rank=11 price=6.53 support=6.22 resistance=6.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64762356.0 spike=1.87
- PRMH.CA: score=3.13 buy_ready=False sector_rank=19 price=2.0 support=1.8 resistance=2.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.34 liquidity=906239.56 spike=0.28
- RACC.CA: score=5.01 buy_ready=False sector_rank=19 price=8.4 support=7.93 resistance=9.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.51 liquidity=2783968.25 spike=0.44
- RAKT.CA: score=11.74 buy_ready=False sector_rank=19 price=23.06 support=20.26 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.41 liquidity=840102.25 spike=2.34
- RAYA.CA: score=11.88 buy_ready=False sector_rank=20 price=5.86 support=5.36 resistance=7.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.6 liquidity=10909524.0 spike=0.33
- RMDA.CA: score=13.34 buy_ready=False sector_rank=17 price=5.16 support=4.8 resistance=6.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=15792571.0 spike=0.57
- ROTO.CA: score=3.9 buy_ready=False sector_rank=19 price=34.41 support=33.3 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.79 liquidity=1671960.5 spike=0.2
- RREI.CA: score=10.62 buy_ready=False sector_rank=19 price=3.2 support=3.21 resistance=4.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.07 liquidity=8091344.5 spike=1.15
- RTVC.CA: score=4.09 buy_ready=False sector_rank=19 price=3.25 support=3.1 resistance=3.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=1865404.0 spike=0.74
- RUBX.CA: score=18.22 buy_ready=False sector_rank=19 price=18.05 support=13.9 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.73 liquidity=83904616.0 spike=0.89
- SAUD.CA: score=13.82 buy_ready=False sector_rank=12 price=21.24 support=20.2 resistance=25.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=11619399.0 spike=0.84
- SCEM.CA: score=18.6 buy_ready=False sector_rank=4 price=86.33 support=74.55 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.17 liquidity=19412446.0 spike=0.31
- SCFM.CA: score=-2.17 buy_ready=False sector_rank=19 price=222.91 support=200.22 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.89 liquidity=604723.44 spike=0.35
- SCTS.CA: score=-0.99 buy_ready=False sector_rank=15 price=443.25 support=433.2 resistance=470.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2269687.75 spike=2.53
- SDTI.CA: score=16.22 buy_ready=False sector_rank=19 price=83.41 support=76.1 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.74 liquidity=18323448.0 spike=0.66
- SEIG.CA: score=-5.01 buy_ready=False sector_rank=19 price=188.35 support=186.1 resistance=200.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1766744.0 spike=0.87
- SIPC.CA: score=13.22 buy_ready=False sector_rank=19 price=5.33 support=4.22 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=26935768.0 spike=0.48
- SKPC.CA: score=12.8 buy_ready=False sector_rank=13 price=15.63 support=14.4 resistance=18.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.26 liquidity=40757772.0 spike=0.58
- SMFR.CA: score=4.84 buy_ready=False sector_rank=19 price=199.91 support=180.11 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=2611426.75 spike=0.84
- SNFC.CA: score=5.66 buy_ready=False sector_rank=19 price=11.06 support=10.8 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=2432244.5 spike=0.26
- SPIN.CA: score=2.53 buy_ready=False sector_rank=14 price=14.0 support=13.5 resistance=17.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.82 liquidity=4844478.5 spike=0.96
- SPMD.CA: score=8.36 buy_ready=False sector_rank=19 price=0.37 support=0.34 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=52.21 liquidity=4136815.75 spike=0.29
- SUGR.CA: score=11.02 buy_ready=False sector_rank=8 price=55.51 support=50.5 resistance=59.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.8 liquidity=2803023.75 spike=0.3
- SVCE.CA: score=13.22 buy_ready=False sector_rank=19 price=9.21 support=8.41 resistance=11.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.16 liquidity=32349038.0 spike=0.45
- SWDY.CA: score=14.23 buy_ready=False sector_rank=7 price=110.44 support=101.5 resistance=126.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=25352436.0 spike=0.39
- TALM.CA: score=13.31 buy_ready=False sector_rank=15 price=19.59 support=18.28 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.8 liquidity=9627798.0 spike=0.31
- TMGH.CA: score=8.95 buy_ready=False sector_rank=11 price=89.23 support=89.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=898184256.0 spike=4.22
- TRTO.CA: score=-1.77 buy_ready=False sector_rank=19 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-19T21:00:00+00:00 freshness=FRESH RSI=78.95 liquidity=2707.83 spike=0.37
- UEFM.CA: score=3.1 buy_ready=False sector_rank=19 price=472.89 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.68 liquidity=879119.44 spike=0.29
- UEGC.CA: score=14.22 buy_ready=False sector_rank=19 price=1.52 support=1.34 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.65 liquidity=27004670.0 spike=0.56
- UNIP.CA: score=8.98 buy_ready=False sector_rank=19 price=0.31 support=0.29 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.25 liquidity=6752683.0 spike=0.83
- UNIT.CA: score=7.54 buy_ready=False sector_rank=11 price=17.24 support=15.6 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.72 liquidity=1592567.63 spike=0.41
- WCDF.CA: score=-1.77 buy_ready=False sector_rank=19 price=499.71 support=432.5 resistance=686.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=28.73 liquidity=1003694.0 spike=0.37
- WKOL.CA: score=7.22 buy_ready=False sector_rank=19 price=275.52 support=241.1 resistance=343.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.91 liquidity=4993293.5 spike=0.69
- ZEOT.CA: score=9.24 buy_ready=False sector_rank=19 price=11.28 support=9.75 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.32 liquidity=6019613.0 spike=0.77
- ZMID.CA: score=13.95 buy_ready=False sector_rank=11 price=6.96 support=6.4 resistance=8.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=34966428.0 spike=0.42

## Backtesting Lite
- EFIH.CA: 180d return=12.83%, max drawdown=-22.68%, MA20>MA50 days last20=2, as_of=2026-10-19T21:00:00+00:00
- ETEL.CA: 180d return=80.08%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-10-19T21:00:00+00:00
- ABUK.CA: 180d return=73.43%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- EAST.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Eastern Company summary=Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- PHDC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=658 sources=3 expected=Palm Hills Development summary=Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma; Palm Hills records 30% higher profits in 2025, unveils new project in UAE; Strong momentum pushes Palm Hills toward EGP 10.15
  - Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma: https://english.mubasher.info/news/4598123/Palm-Hills-UAE-s-Miran-to-launch-new-development-project-in-Ras-Al-Hikma/
  - Palm Hills records 30% higher profits in 2025, unveils new project in UAE: https://english.mubasher.info/news/4580548/Palm-Hills-records-30-higher-profits-in-2025-unveils-new-project-in-UAE/
  - Strong momentum pushes Palm Hills toward EGP 10.15: https://english.mubasher.info/news/4560871/Strong-momentum-pushes-Palm-Hills-toward-EGP-10-15/
- EGSA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Satellites summary=Evidence rejected for EGSA.CA: source text did not clearly match EGSA.CA / Egyptian Satellites.

## Warnings
- OpenRouter API error: 404
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for EAST.CA: source text did not clearly match EAST.CA / Eastern Company.
- Evidence for PHDC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EGSA.CA: source text did not clearly match EGSA.CA / Egyptian Satellites.
