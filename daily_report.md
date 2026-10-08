# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-10-08T21:29:02.238127+00:00
Generated Cairo: 2026-10-09 00:29
Run timing: target 19:30 Cairo | generated Cairo 2026-10-09 00:29 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-10-09 00:24

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 185/187
- Top sector: Fintech & Payments

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, October 07
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 21.05% / above MA50 36.84%
- EGX70 regime: BEARISH / above MA20 32.5% / above MA50 35.0%
- Sector breadth: 38.1%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ORAS.CA: liquidity=637229824.0 spike=1.0 score=4.6
- COMI.CA: liquidity=418422272.0 spike=0.76 score=9.24
- CCAP.CA: liquidity=339093696.0 spike=0.44 score=19.07
- FWRY.CA: liquidity=336845728.0 spike=3.11 score=30.62
- AMOC.CA: liquidity=250964784.0 spike=1.81 score=24.51

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with sector breadth at 38%, keeping the risk mode defensive (NO_NEW_BUY); the scanner highlights accumulation spikes in Fintech & Payments (FWRY.CA, EFIH.CA) with a bullish‑watch outlook, but prices sit near resistance, limiting short‑term upside.
- FWRY.CA & EFIH.CA show strong liquidity spikes (accumulation) and bullish‑watch outlook, yet are close to 20‑day resistance, suggesting limited upside in the next 1‑3 days.
- Low sector breadth (38%) and EGX30/EGX70 trading below MA20/MA50 maintain a defensive market regime, blocking new BUY signals despite individual stock strength.
- Other tickers (SIPC.CA, MBSC.CA, AMOC.CA) also display accumulation spikes but are far above support or belong to non‑leading sectors, adding uncertainty to short‑term moves.
- Risk mode remains DEFENSIVE_NO_NEW_BUY; any change depends on a shift in EGX30/EGX70 breadth or sector leadership, which is currently uncertain.

## Top Liquidity Spikes
- DEIN.CA: spike=8.57 liquidity=31.05 outlook=WEAK_OR_RISKY score=34.22 buy_ready=False
- SIPC.CA: spike=3.59 liquidity=183080896.0 outlook=BULLISH_WATCH score=88.22 buy_ready=False
- FWRY.CA: spike=3.11 liquidity=336845728.0 outlook=BULLISH_WATCH score=100 buy_ready=False
- DAPH.CA: spike=2.97 liquidity=110708520.0 outlook=WEAK_OR_RISKY score=20.22 buy_ready=False
- IRON.CA: spike=2.65 liquidity=30631262.0 outlook=BULLISH_WATCH score=79.51 buy_ready=False

## Sector Leaderboard
- #1 Fintech & Payments: score=13.79 5d=9.0% 20d=2.24% aboveMA50=100.0%
- #2 Telecommunications: score=8.53 5d=5.34% 20d=7.79% aboveMA50=100.0%
- #3 Education: score=6.75 5d=4.23% 20d=2.76% aboveMA50=66.67%
- #4 Building Materials: score=6.44 5d=11.18% 20d=-12.83% aboveMA50=50.0%
- #5 Automotive & Distribution: score=5.18 5d=3.16% 20d=-1.3% aboveMA50=50.0%
- #6 Investment Holding: score=5.18 5d=-0.15% 20d=8.52% aboveMA50=66.67%
- #7 Non-bank Financial Services: score=4.82 5d=7.98% 20d=-6.73% aboveMA50=40.0%
- #8 Energy & Petrochemicals: score=4.72 5d=2.0% 20d=0.63% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- FWRY.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- EFIH.CA: BULLISH_WATCH score=99 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support; close to resistance
- CIRA.CA: BULLISH_WATCH score=97.75 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- MBSC.CA: BULLISH_WATCH score=89.44 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support
- SIPC.CA: BULLISH_WATCH score=88.22 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- TALM.CA: BULLISH_WATCH score=82.75 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- AMOC.CA: BULLISH_WATCH score=82.72 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- ETEL.CA: BULLISH_WATCH score=80.53 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- GBCO.CA: BULLISH_WATCH score=80.18 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- IRON.CA: BULLISH_WATCH score=79.51 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=6.04 buy_ready=False sector_rank=12 price=261.04 support=230.11 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=24.09 liquidity=6151743.0 spike=0.3
- ABUK.CA: score=18.0 buy_ready=False sector_rank=11 price=89.12 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=43.87 liquidity=93761504.0 spike=0.99
- ACAMD.CA: score=18.89 buy_ready=False sector_rank=12 price=2.05 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=36076280.0 spike=0.84
- ACGC.CA: score=9.85 buy_ready=False sector_rank=20 price=14.33 support=13.11 resistance=15.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.9 liquidity=2749722.75 spike=0.14
- ADCI.CA: score=5.59 buy_ready=False sector_rank=12 price=272.01 support=256.0 resistance=294.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=42.81 liquidity=704704.56 spike=0.31
- ADIB.CA: score=10.26 buy_ready=False sector_rank=10 price=47.75 support=47.45 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=20.97 liquidity=72852176.0 spike=1.01
- ADPC.CA: score=8.89 buy_ready=False sector_rank=12 price=3.53 support=3.4 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=10132785.0 spike=0.66
- AFDI.CA: score=15.12 buy_ready=False sector_rank=12 price=54.07 support=47.7 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=6234218.5 spike=0.88
- AFMC.CA: score=16.89 buy_ready=False sector_rank=12 price=152.8 support=131.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=43.31 liquidity=13572170.0 spike=0.5
- AJWA.CA: score=19.65 buy_ready=False sector_rank=12 price=196.16 support=176.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=79.58 liquidity=45247820.0 spike=2.38
- ALCN.CA: score=22.55 buy_ready=False sector_rank=9 price=34.32 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=20531096.0 spike=0.6
- ALUM.CA: score=2.04 buy_ready=False sector_rank=12 price=23.53 support=21.65 resistance=28.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=26.88 liquidity=2156620.0 spike=0.43
- AMER.CA: score=18.31 buy_ready=False sector_rank=18 price=5.03 support=4.05 resistance=5.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=45464256.0 spike=0.96
- AMES.CA: score=15.89 buy_ready=False sector_rank=12 price=46.37 support=40.15 resistance=64.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=51405512.0 spike=0.39
- AMIA.CA: score=17.93 buy_ready=False sector_rank=12 price=19.18 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=67.0 liquidity=17362642.0 spike=1.02
- AMOC.CA: score=24.51 buy_ready=False sector_rank=8 price=14.5 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=58.76 liquidity=250964784.0 spike=1.81
- APSW.CA: score=10.11 buy_ready=False sector_rank=12 price=8.44 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=1085005.25 spike=1.57
- ARAB.CA: score=22.53 buy_ready=False sector_rank=18 price=0.27 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=126584280.0 spike=1.61
- ARCC.CA: score=23.4 buy_ready=False sector_rank=4 price=71.07 support=60.01 resistance=76.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.84 liquidity=20092410.0 spike=0.7
- AREH.CA: score=6.14 buy_ready=False sector_rank=12 price=1.29 support=1.14 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=5252735.5 spike=0.56
- ASCM.CA: score=10.22 buy_ready=False sector_rank=12 price=57.53 support=53.8 resistance=64.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=35.31 liquidity=3330463.0 spike=0.37
- ASPI.CA: score=9.89 buy_ready=False sector_rank=12 price=0.36 support=0.33 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=24.24 liquidity=14594139.0 spike=0.36
- ATLC.CA: score=7.85 buy_ready=False sector_rank=7 price=6.3 support=5.2 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=34.21 liquidity=3922364.25 spike=0.32
- ATQA.CA: score=18.0 buy_ready=False sector_rank=11 price=12.0 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=44.98 liquidity=55682128.0 spike=0.72
- AXPH.CA: score=3.78 buy_ready=False sector_rank=12 price=1495.64 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=29.19 liquidity=3891342.25 spike=0.59
- BINV.CA: score=19.94 buy_ready=False sector_rank=6 price=58.26 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=41.54 liquidity=8869432.0 spike=0.36
- BIOC.CA: score=18.89 buy_ready=False sector_rank=12 price=324.84 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.25 liquidity=65018844.0 spike=0.68
- BTFH.CA: score=9.93 buy_ready=False sector_rank=7 price=2.77 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=72468120.0 spike=0.78
- CAED.CA: score=14.25 buy_ready=False sector_rank=12 price=117.28 support=103.1 resistance=150.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=38.34 liquidity=7363330.5 spike=0.41
- CANA.CA: score=17.67 buy_ready=False sector_rank=10 price=44.93 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=9430163.0 spike=0.42
- CCAP.CA: score=19.07 buy_ready=False sector_rank=6 price=6.59 support=6.1 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=41.54 liquidity=339093696.0 spike=0.44
- CCRS.CA: score=9.02 buy_ready=False sector_rank=12 price=2.32 support=2.21 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=26.19 liquidity=9127857.0 spike=0.64
- CEFM.CA: score=8.09 buy_ready=False sector_rank=12 price=135.82 support=113.0 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:12 PM market time freshness=DELAYED_CURRENT RSI=39.8 liquidity=3202893.75 spike=0.97
- CERA.CA: score=17.03 buy_ready=False sector_rank=12 price=1.37 support=1.18 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=43.84 liquidity=151765008.0 spike=1.07
- CFGH.CA: score=0.38 buy_ready=False sector_rank=12 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 12:55 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=13721.9 spike=1.74
- CICH.CA: score=7.65 buy_ready=False sector_rank=7 price=11.94 support=10.75 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=1726842.13 spike=0.45
- CIEB.CA: score=6.38 buy_ready=False sector_rank=10 price=24.0 support=23.0 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=6148950.5 spike=0.67
- CIRA.CA: score=22.64 buy_ready=False sector_rank=3 price=39.42 support=36.8 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=40.89 liquidity=39692328.0 spike=1.12
- CLHO.CA: score=16.16 buy_ready=False sector_rank=19 price=15.2 support=13.9 resistance=16.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=38.27 liquidity=27373122.0 spike=0.66
- CNFN.CA: score=18.67 buy_ready=False sector_rank=7 price=4.33 support=3.84 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=39.57 liquidity=14360919.0 spike=1.87
- COMI.CA: score=9.24 buy_ready=False sector_rank=10 price=124.64 support=124.14 resistance=139.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=22.53 liquidity=418422272.0 spike=0.76
- COPR.CA: score=16.89 buy_ready=False sector_rank=12 price=0.48 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=14329979.0 spike=0.57
- COSG.CA: score=8.83 buy_ready=False sector_rank=12 price=1.61 support=1.46 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=8937595.0 spike=0.56
- CPCI.CA: score=10.84 buy_ready=False sector_rank=12 price=602.9 support=530.0 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=84.08 liquidity=3911104.0 spike=1.02
- CSAG.CA: score=9.51 buy_ready=False sector_rank=9 price=36.82 support=34.52 resistance=41.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:12 PM market time freshness=DELAYED_CURRENT RSI=42.17 liquidity=3955159.0 spike=0.48
- DAPH.CA: score=13.83 buy_ready=False sector_rank=12 price=107.08 support=89.1 resistance=133.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=31.4 liquidity=110708520.0 spike=2.97
- DEIN.CA: score=12.89 buy_ready=False sector_rank=12 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=31.05 spike=8.57
- DOMT.CA: score=9.71 buy_ready=False sector_rank=21 price=24.0 support=23.81 resistance=28.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.24 liquidity=10755096.0 spike=2.11
- DSCW.CA: score=6.89 buy_ready=False sector_rank=12 price=1.7 support=1.58 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=5997761.0 spike=0.31
- DTPP.CA: score=17.89 buy_ready=False sector_rank=12 price=302.15 support=250.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.56 liquidity=52522504.0 spike=0.53
- EALR.CA: score=3.8 buy_ready=False sector_rank=12 price=342.16 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=30.06 liquidity=4912222.5 spike=0.5
- EASB.CA: score=9.88 buy_ready=False sector_rank=12 price=7.64 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.81 liquidity=1989678.5 spike=0.19
- EAST.CA: score=7.49 buy_ready=False sector_rank=21 price=28.75 support=27.91 resistance=35.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=17.1 liquidity=40159696.0 spike=0.84
- EBSC.CA: score=-0.25 buy_ready=False sector_rank=12 price=1.77 support=1.61 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=32.91 liquidity=858771.44 spike=0.27
- ECAP.CA: score=3.65 buy_ready=False sector_rank=12 price=30.1 support=29.13 resistance=33.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=29.16 liquidity=2759540.0 spike=0.63
- EDFM.CA: score=16.69 buy_ready=False sector_rank=12 price=410.0 support=354.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=51.1 liquidity=2565514.0 spike=2.12
- EEII.CA: score=14.69 buy_ready=False sector_rank=12 price=2.13 support=2.02 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=8806858.0 spike=0.92
- EFIC.CA: score=9.0 buy_ready=False sector_rank=11 price=163.04 support=147.0 resistance=227.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=22.29 liquidity=15564284.0 spike=0.26
- EFID.CA: score=7.49 buy_ready=False sector_rank=21 price=19.07 support=18.1 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=8.88 liquidity=15174604.0 spike=0.28
- EFIH.CA: score=30.16 buy_ready=False sector_rank=1 price=25.3 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=119781336.0 spike=1.88
- EGAL.CA: score=11.94 buy_ready=False sector_rank=11 price=339.98 support=331.5 resistance=378.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=22.5 liquidity=104605384.0 spike=1.97
- EGAS.CA: score=9.55 buy_ready=False sector_rank=8 price=56.15 support=53.62 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.57 liquidity=3657010.75 spike=0.33
- EGBE.CA: score=10.6 buy_ready=False sector_rank=10 price=0.54 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=141440.25 spike=1.11
- EGCH.CA: score=15.0 buy_ready=False sector_rank=11 price=13.36 support=12.88 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=29302782.0 spike=0.32
- EGSA.CA: score=6.4 buy_ready=False sector_rank=2 price=8.87 support=8.82 resistance=9.1 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=11.76 liquidity=8.87 spike=0.0
- EGTS.CA: score=11.01 buy_ready=False sector_rank=18 price=16.42 support=15.65 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=43.74 liquidity=6696034.0 spike=0.19
- EHDR.CA: score=6.17 buy_ready=False sector_rank=12 price=2.53 support=2.35 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=29.69 liquidity=6277300.5 spike=0.53
- ELEC.CA: score=10.62 buy_ready=False sector_rank=14 price=1.87 support=1.72 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=29.27 liquidity=16595071.0 spike=0.26
- ELKA.CA: score=16.89 buy_ready=False sector_rank=12 price=1.61 support=1.43 resistance=1.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.04 liquidity=13620799.0 spike=0.97
- ELNA.CA: score=0.94 buy_ready=False sector_rank=12 price=35.22 support=33.46 resistance=37.96 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=52196.04 spike=0.28
- ELSH.CA: score=12.49 buy_ready=False sector_rank=12 price=12.13 support=10.8 resistance=13.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=33.97 liquidity=28611752.0 spike=1.3
- ELWA.CA: score=4.57 buy_ready=False sector_rank=12 price=1.59 support=1.43 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=678380.06 spike=0.92
- EMFD.CA: score=9.31 buy_ready=False sector_rank=18 price=12.8 support=11.7 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.19 liquidity=38458516.0 spike=0.47
- ENGC.CA: score=9.89 buy_ready=False sector_rank=12 price=37.0 support=33.33 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.49 liquidity=14276444.0 spike=0.81
- EOSB.CA: score=11.05 buy_ready=False sector_rank=12 price=1.57 support=1.58 resistance=1.64 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=78572.22 spike=1.54
- EPCO.CA: score=2.99 buy_ready=False sector_rank=12 price=9.79 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=25.17 liquidity=3098196.0 spike=0.22
- EPPK.CA: score=-4.69 buy_ready=False sector_rank=12 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.4 buy_ready=False sector_rank=2 price=147.94 support=124.01 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.69 liquidity=127165696.0 spike=0.45
- ETRS.CA: score=19.47 buy_ready=False sector_rank=12 price=10.78 support=9.82 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=42.35 liquidity=12244795.0 spike=1.29
- EXPA.CA: score=9.24 buy_ready=False sector_rank=10 price=15.82 support=15.41 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=16.84 liquidity=14868403.0 spike=0.39
- FAIT.CA: score=10.52 buy_ready=False sector_rank=10 price=45.59 support=38.48 resistance=48.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.93 liquidity=2281312.25 spike=0.73
- FAITA.CA: score=13.4 buy_ready=False sector_rank=10 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 12:50 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=46284.48 spike=1.56
- FERC.CA: score=2.04 buy_ready=False sector_rank=11 price=75.27 support=70.42 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=26.13 liquidity=3032689.0 spike=0.48
- FWRY.CA: score=30.62 buy_ready=False sector_rank=1 price=19.08 support=17.5 resistance=19.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.19 liquidity=336845728.0 spike=3.11
- GBCO.CA: score=23.21 buy_ready=False sector_rank=5 price=31.24 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.07 liquidity=106487056.0 spike=1.07
- GDWA.CA: score=7.08 buy_ready=False sector_rank=12 price=0.67 support=0.61 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=21.08 liquidity=8193812.0 spike=0.36
- GGCC.CA: score=6.48 buy_ready=False sector_rank=12 price=0.72 support=0.65 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=24.38 liquidity=6591457.5 spike=0.44
- GIHD.CA: score=9.2 buy_ready=False sector_rank=12 price=62.34 support=60.9 resistance=78.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=29.07 liquidity=9310697.0 spike=0.41
- GMCI.CA: score=6.21 buy_ready=False sector_rank=12 price=1.64 support=1.49 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=326856.34 spike=0.7
- GRCA.CA: score=4.6 buy_ready=False sector_rank=12 price=37.7 support=32.11 resistance=57.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.49 liquidity=3709670.75 spike=0.19
- GSSC.CA: score=1.46 buy_ready=False sector_rank=12 price=282.98 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=1568603.75 spike=0.42
- GTWL.CA: score=9.89 buy_ready=False sector_rank=12 price=160.01 support=124.5 resistance=244.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=25.05 liquidity=71520304.0 spike=0.48
- HDBK.CA: score=12.24 buy_ready=False sector_rank=10 price=106.09 support=102.03 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=28.02 liquidity=19899652.0 spike=0.66
- HELI.CA: score=9.31 buy_ready=False sector_rank=18 price=7.47 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=26.07 liquidity=28097854.0 spike=0.25
- HRHO.CA: score=22.93 buy_ready=False sector_rank=7 price=26.7 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.05 liquidity=112811784.0 spike=0.86
- ICID.CA: score=12.39 buy_ready=False sector_rank=12 price=18.17 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=44.41 liquidity=2497930.0 spike=0.32
- IDRE.CA: score=8.65 buy_ready=False sector_rank=12 price=50.14 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:13 PM market time freshness=DELAYED_CURRENT RSI=37.9 liquidity=3764239.25 spike=0.26
- IFAP.CA: score=5.37 buy_ready=False sector_rank=13 price=19.4 support=17.17 resistance=21.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=32.55 liquidity=6589111.0 spike=0.81
- INFI.CA: score=19.65 buy_ready=False sector_rank=12 price=129.14 support=104.0 resistance=149.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=19573418.0 spike=1.38
- IRON.CA: score=24.3 buy_ready=False sector_rank=11 price=29.79 support=25.01 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.15 liquidity=30631262.0 spike=2.65
- ISMA.CA: score=2.21 buy_ready=False sector_rank=12 price=25.6 support=22.7 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=31.85 liquidity=2318015.75 spike=0.17
- ISMQ.CA: score=17.0 buy_ready=False sector_rank=11 price=8.25 support=7.6 resistance=9.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=14726316.0 spike=0.74
- ISPH.CA: score=14.16 buy_ready=False sector_rank=19 price=11.65 support=11.22 resistance=13.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.61 liquidity=21800542.0 spike=0.34
- JUFO.CA: score=7.79 buy_ready=False sector_rank=21 price=24.98 support=24.4 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.2 liquidity=18329734.0 spike=1.15
- KABO.CA: score=11.84 buy_ready=False sector_rank=20 price=8.81 support=7.97 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.52 liquidity=7739932.0 spike=0.25
- KWIN.CA: score=4.71 buy_ready=False sector_rank=12 price=76.75 support=72.21 resistance=95.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=27.44 liquidity=4817749.0 spike=0.42
- KZPC.CA: score=8.74 buy_ready=False sector_rank=12 price=13.17 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=32.01 liquidity=5851179.0 spike=0.47
- LCSW.CA: score=24.1 buy_ready=False sector_rank=4 price=34.8 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=57.61 liquidity=25130000.0 spike=1.35
- LUTS.CA: score=16.89 buy_ready=False sector_rank=12 price=0.91 support=0.72 resistance=1.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.66 liquidity=44133560.0 spike=0.53
- MAAL.CA: score=17.27 buy_ready=False sector_rank=12 price=10.9 support=8.45 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=72.35 liquidity=7383571.0 spike=0.32
- MASR.CA: score=21.89 buy_ready=False sector_rank=12 price=7.87 support=6.82 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=49.58 liquidity=59666584.0 spike=0.84
- MBSC.CA: score=25.2 buy_ready=False sector_rank=4 price=376.31 support=288.0 resistance=426.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.1 liquidity=140725760.0 spike=1.9
- MCQE.CA: score=17.68 buy_ready=False sector_rank=4 price=196.74 support=177.02 resistance=240.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=40.35 liquidity=75153696.0 spike=1.64
- MCRO.CA: score=14.89 buy_ready=False sector_rank=12 price=1.51 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.59 liquidity=27537760.0 spike=0.34
- MENA.CA: score=10.82 buy_ready=False sector_rank=18 price=6.7 support=5.8 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=46.21 liquidity=1708372.0 spike=1.4
- MEPA.CA: score=9.65 buy_ready=False sector_rank=12 price=1.72 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=4764783.0 spike=0.36
- MFPC.CA: score=18.0 buy_ready=False sector_rank=11 price=46.59 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.39 liquidity=26493044.0 spike=0.27
- MFSC.CA: score=7.2 buy_ready=False sector_rank=12 price=44.85 support=41.22 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:12 PM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=2308623.25 spike=0.87
- MHOT.CA: score=10.5 buy_ready=False sector_rank=17 price=17.51 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=6987822.5 spike=0.37
- MICH.CA: score=10.29 buy_ready=False sector_rank=12 price=47.04 support=42.01 resistance=50.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=42.65 liquidity=5405720.5 spike=0.54
- MILS.CA: score=4.44 buy_ready=False sector_rank=12 price=183.87 support=165.5 resistance=213.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=33.32 liquidity=4553870.0 spike=0.46
- MIPH.CA: score=12.23 buy_ready=False sector_rank=19 price=829.4 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=47.42 liquidity=3067752.0 spike=0.35
- MOED.CA: score=8.35 buy_ready=False sector_rank=12 price=0.68 support=0.59 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=28.14 liquidity=9462833.0 spike=0.29
- MOIL.CA: score=9.02 buy_ready=False sector_rank=8 price=0.69 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.53 liquidity=136973.08 spike=0.53
- MOIN.CA: score=17.97 buy_ready=False sector_rank=12 price=35.49 support=32.0 resistance=41.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.51 liquidity=15049192.0 spike=1.04
- MOSC.CA: score=0.94 buy_ready=False sector_rank=12 price=278.65 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.76 liquidity=1053731.0 spike=0.28
- MPCI.CA: score=9.89 buy_ready=False sector_rank=12 price=346.01 support=305.45 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=69052720.0 spike=0.67
- MPCO.CA: score=12.78 buy_ready=False sector_rank=13 price=2.39 support=2.25 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=66783352.0 spike=0.35
- MPRC.CA: score=13.18 buy_ready=False sector_rank=12 price=40.23 support=37.65 resistance=42.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=4294061.5 spike=0.21
- MTIE.CA: score=15.72 buy_ready=False sector_rank=5 price=8.06 support=7.5 resistance=8.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.25 liquidity=8651205.0 spike=0.5
- NAHO.CA: score=4.89 buy_ready=False sector_rank=12 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=46.43 liquidity=5811.04 spike=0.15
- NCCW.CA: score=17.89 buy_ready=False sector_rank=12 price=7.02 support=6.44 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=12800883.0 spike=0.2
- NEDA.CA: score=4.92 buy_ready=False sector_rank=12 price=2.61 support=2.48 resistance=2.83 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=36.59 liquidity=35548.2 spike=0.05
- NHPS.CA: score=11.54 buy_ready=False sector_rank=12 price=73.29 support=66.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=45.02 liquidity=4656476.0 spike=0.32
- NINH.CA: score=13.29 buy_ready=False sector_rank=12 price=19.06 support=18.53 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=35.43 liquidity=8400085.0 spike=0.58
- NIPH.CA: score=14.16 buy_ready=False sector_rank=19 price=316.85 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=37717136.0 spike=0.3
- OBRI.CA: score=13.74 buy_ready=False sector_rank=12 price=28.36 support=22.8 resistance=33.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=40.5 liquidity=7847824.0 spike=0.64
- OCDI.CA: score=9.31 buy_ready=False sector_rank=18 price=27.51 support=24.2 resistance=33.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=14881147.0 spike=0.29
- OCPH.CA: score=7.92 buy_ready=False sector_rank=12 price=221.69 support=190.0 resistance=256.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.14 liquidity=2031291.38 spike=0.55
- ODIN.CA: score=9.39 buy_ready=False sector_rank=12 price=2.53 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=4499393.0 spike=0.49
- OFH.CA: score=14.89 buy_ready=False sector_rank=12 price=0.88 support=0.83 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=23496336.0 spike=0.23
- OIH.CA: score=11.07 buy_ready=False sector_rank=6 price=1.88 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=23.64 liquidity=22657394.0 spike=0.24
- OLFI.CA: score=7.49 buy_ready=False sector_rank=21 price=21.09 support=20.82 resistance=23.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=18.49 liquidity=10934591.0 spike=0.62
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=880.1 support=839.0 resistance=894.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=637229824.0 spike=1.0
- ORHD.CA: score=8.31 buy_ready=False sector_rank=18 price=11.99 support=11.59 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=2.67 liquidity=94390768.0 spike=0.58
- ORWE.CA: score=17.1 buy_ready=False sector_rank=20 price=27.1 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=41.12 liquidity=10873100.0 spike=0.28
- PHAR.CA: score=16.16 buy_ready=False sector_rank=19 price=113.97 support=102.0 resistance=128.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=39.97 liquidity=25178564.0 spike=0.34
- PHDC.CA: score=16.31 buy_ready=False sector_rank=18 price=12.81 support=12.36 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=74709600.0 spike=0.68
- PHTV.CA: score=10.34 buy_ready=False sector_rank=12 price=351.81 support=315.1 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:06 PM market time freshness=DELAYED_CURRENT RSI=40.36 liquidity=453466.38 spike=0.35
- POUL.CA: score=7.49 buy_ready=False sector_rank=21 price=9.99 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=1.89 liquidity=16065999.0 spike=0.48
- PRCL.CA: score=3.05 buy_ready=False sector_rank=4 price=25.62 support=22.8 resistance=33.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=28.66 liquidity=1653549.75 spike=0.13
- PRDC.CA: score=16.31 buy_ready=False sector_rank=18 price=7.1 support=6.81 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=29576354.0 spike=0.83
- PRMH.CA: score=1.22 buy_ready=False sector_rank=12 price=2.24 support=2.03 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=18.06 liquidity=2330361.75 spike=0.58
- RACC.CA: score=10.88 buy_ready=False sector_rank=12 price=9.32 support=8.51 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=35.27 liquidity=3995696.0 spike=0.56
- RAKT.CA: score=12.16 buy_ready=False sector_rank=12 price=23.89 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=65.9 liquidity=274496.09 spike=0.87
- RAYA.CA: score=13.68 buy_ready=False sector_rank=16 price=6.6 support=5.72 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.65 liquidity=9128606.0 spike=0.25
- RMDA.CA: score=9.16 buy_ready=False sector_rank=19 price=5.41 support=4.83 resistance=6.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=22.82 liquidity=14428980.0 spike=0.44
- ROTO.CA: score=18.81 buy_ready=False sector_rank=12 price=40.86 support=35.02 resistance=43.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.85 liquidity=9481346.0 spike=1.22
- RREI.CA: score=5.98 buy_ready=False sector_rank=12 price=3.91 support=3.53 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=28.87 liquidity=6090772.5 spike=0.56
- RTVC.CA: score=0.65 buy_ready=False sector_rank=12 price=3.68 support=3.37 resistance=4.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=1763579.75 spike=0.65
- RUBX.CA: score=24.41 buy_ready=False sector_rank=12 price=18.0 support=12.65 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=114043088.0 spike=1.26
- SAUD.CA: score=8.73 buy_ready=False sector_rank=10 price=22.97 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=45.32 liquidity=3489159.75 spike=0.18
- SCEM.CA: score=18.4 buy_ready=False sector_rank=4 price=85.59 support=74.55 resistance=102.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:27 PM market time freshness=DELAYED_CURRENT RSI=36.94 liquidity=38621156.0 spike=0.64
- SCFM.CA: score=-0.47 buy_ready=False sector_rank=12 price=245.34 support=223.11 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=32.37 liquidity=644260.19 spike=0.28
- SCTS.CA: score=2.96 buy_ready=False sector_rank=3 price=549.77 support=520.3 resistance=635.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=564919.75 spike=0.34
- SDTI.CA: score=21.89 buy_ready=False sector_rank=12 price=87.0 support=71.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=74.91 liquidity=25393230.0 spike=0.78
- SEIG.CA: score=8.13 buy_ready=False sector_rank=12 price=233.37 support=200.0 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=45.07 liquidity=1241064.75 spike=0.56
- SIPC.CA: score=28.89 buy_ready=False sector_rank=12 price=6.17 support=4.22 resistance=6.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=183080896.0 spike=3.59
- SKPC.CA: score=9.0 buy_ready=False sector_rank=11 price=16.25 support=15.4 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=54627872.0 spike=0.65
- SMFR.CA: score=10.81 buy_ready=False sector_rank=12 price=232.15 support=205.01 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=44.95 liquidity=1917510.38 spike=0.49
- SNFC.CA: score=22.63 buy_ready=False sector_rank=12 price=11.64 support=10.58 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=16814538.0 spike=1.37
- SPIN.CA: score=7.0 buy_ready=False sector_rank=20 price=16.31 support=15.11 resistance=19.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:25 PM market time freshness=DELAYED_CURRENT RSI=35.33 liquidity=2892692.25 spike=0.45
- SPMD.CA: score=6.43 buy_ready=False sector_rank=12 price=0.39 support=0.36 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=21.88 liquidity=7537964.0 spike=0.1
- SUGR.CA: score=12.26 buy_ready=False sector_rank=21 price=55.76 support=50.5 resistance=64.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.09 liquidity=5769755.0 spike=0.4
- SVCE.CA: score=9.89 buy_ready=False sector_rank=12 price=10.4 support=9.24 resistance=12.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=34.39 liquidity=77740736.0 spike=0.79
- SWDY.CA: score=14.62 buy_ready=False sector_rank=14 price=116.27 support=102.31 resistance=132.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.0 liquidity=50833692.0 spike=0.79
- TALM.CA: score=24.4 buy_ready=False sector_rank=3 price=21.71 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=17823102.0 spike=0.25
- TMGH.CA: score=8.31 buy_ready=False sector_rank=18 price=87.99 support=84.4 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=18.33 liquidity=108044592.0 spike=0.49
- TRTO.CA: score=11.89 buy_ready=False sector_rank=12 price=0.07 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-10-06T21:00:00+00:00 freshness=FRESH RSI=57.69 liquidity=4869.33 spike=0.41
- UEFM.CA: score=17.74 buy_ready=False sector_rank=12 price=520.0 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=6833708.0 spike=2.01
- UEGC.CA: score=10.89 buy_ready=False sector_rank=12 price=1.56 support=1.37 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=12112560.0 spike=0.37
- UNIP.CA: score=14.4 buy_ready=False sector_rank=12 price=0.36 support=0.32 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:26 PM market time freshness=DELAYED_CURRENT RSI=38.02 liquidity=7509543.0 spike=0.6
- UNIT.CA: score=15.39 buy_ready=False sector_rank=18 price=17.71 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.96 liquidity=24849400.0 spike=1.54
- WCDF.CA: score=4.53 buy_ready=False sector_rank=12 price=658.17 support=575.5 resistance=765.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:14 PM market time freshness=DELAYED_CURRENT RSI=24.65 liquidity=1645160.63 spike=0.46
- WKOL.CA: score=1.85 buy_ready=False sector_rank=12 price=293.91 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=22.46 liquidity=2963442.0 spike=0.25
- ZEOT.CA: score=10.03 buy_ready=False sector_rank=12 price=12.6 support=10.6 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.72 liquidity=3140756.0 spike=0.58
- ZMID.CA: score=9.31 buy_ready=False sector_rank=18 price=7.53 support=7.07 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 01:28 PM market time freshness=DELAYED_CURRENT RSI=13.88 liquidity=38107844.0 spike=0.35

## Backtesting Lite
- FWRY.CA: 180d return=16.01%, max drawdown=-18.89%, MA20>MA50 days last20=2, as_of=2026-10-06T21:00:00+00:00
- EFIH.CA: 180d return=15.39%, max drawdown=-22.68%, MA20>MA50 days last20=9, as_of=2026-10-06T21:00:00+00:00
- SIPC.CA: 180d return=66.67%, max drawdown=-31.27%, MA20>MA50 days last20=20, as_of=2026-10-06T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- SIPC.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2472 sources=3 expected=Sabaa International Company for Pharmaceutical and Chemical Industry summary=Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue; FRA approves Sabaa Pharmaceutical&#39;s capital raise; Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results
  - Sabaa Pharmaceutical&#39;s shareholders approve capital raise via bonus issue: https://english.mubasher.info/news/3809286/Sabaa-Pharmaceutical-s-shareholders-approve-capital-raise-via-bonus-issue/
  - FRA approves Sabaa Pharmaceutical&#39;s capital raise: https://english.mubasher.info/news/3789753/FRA-approves-Sabaa-Pharmaceutical-s-capital-raise/
  - Sabaa Pharmaceutical&#39;s profit leaps 76% in 2020 initial results: https://english.mubasher.info/news/3779465/Sabaa-Pharmaceutical-s-profit-leaps-76-in-2020-initial-results/
- MBSC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=645 sources=3 expected=Misr Beni Suef Cement summary=Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025; Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25; Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25
  - Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025: https://english.mubasher.info/news/4599415/Misr-Beni-Suef-s-consolidated-net-profits-near-EGP-4bn-in-2025/
  - Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25: https://english.mubasher.info/news/4488249/Misr-Beni-Suef-s-consolidated-net-profits-hit-EGP-953m-in-H1-25/
  - Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25: https://english.mubasher.info/news/4455784/Misr-Beni-Suef-Cement-s-consolidate-profits-fall-to-EGP-574m-in-Q1-25/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- IRON.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Iron and Steel summary=Evidence rejected for IRON.CA: source text did not clearly match IRON.CA / Egyptian Iron and Steel.

## Warnings
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for SIPC.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for IRON.CA: source text did not clearly match IRON.CA / Egyptian Iron and Steel.
