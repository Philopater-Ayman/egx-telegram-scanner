# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-07-30T18:00:37.151921+00:00
Generated Cairo: 2026-07-30 21:00
Run timing: target 19:30 Cairo | generated Cairo 2026-07-30 21:00 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-07-30 20:54

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 174/189
- Top sector: Education

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 40.0% / above MA50 40.0%
- EGX70 regime: BEARISH / above MA20 43.24% / above MA50 70.27%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=581034880.0 spike=0.82 score=16.02
- PHAR.CA: liquidity=464787392.0 spike=7.44 score=11.35
- MPCO.CA: liquidity=450149571.03 spike=5.56 score=30.4
- AMOC.CA: liquidity=391681248.0 spike=6.5 score=11.32
- TMGH.CA: liquidity=383727776.0 spike=1.05 score=16.14

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flags MPCO.CA, TALM.CA, AJWA.CA, MILS.CA as top tickets due to high rank scores, accumulation‑spike liquidity and bullish‑watch outlook, but EGX30/EGX70 remain bearish with low sector breadth, keeping risk mode defensive and no new buys allowed.
- High rank scores (30.4‑26.2) and accumulation‑spike liquidity indicate short‑term buying interest despite the bearish market.
- Bullish‑watch outlook with RSI near overbought (67‑88) suggests possible short‑term upside, though momentum is extended and overheated.
- Prices sit above 20‑day support (11‑54% distance) and close to 20‑day resistance (5‑13% distance), limiting upside room over the next 1‑3 days.
- EGX30/EGX70 bearish trend, sector breadth only 23.8%, and defensive risk mode override ticket‑level signals, maintaining HOLD stance with uncertainty.

## Top Liquidity Spikes
- WKOL.CA: spike=14.19 liquidity=147225600.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EOSB.CA: spike=12.3 liquidity=446389.16 outlook=CONSTRUCTIVE score=67.62 buy_ready=False
- EALR.CA: spike=9.29 liquidity=174521488.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AALR.CA: spike=9.23 liquidity=187338288.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PHAR.CA: spike=7.44 liquidity=464787392.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Education: score=14.83 5d=12.93% 20d=15.32% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=13.07 5d=4.52% 20d=8.39% aboveMA50=50.0%
- #3 Textiles: score=8.52 5d=1.32% 20d=11.88% aboveMA50=75.0%
- #4 Industrial Goods & Cables: score=7.72 5d=0.31% 20d=8.52% aboveMA50=100.0%
- #5 General / Verified EGX Expansion: score=7.62 5d=0.0% 20d=12.42% aboveMA50=71.84%
- #6 Telecommunications: score=7.1 5d=0.82% 20d=10.02% aboveMA50=50.0%
- #7 Building Materials: score=6.97 5d=-0.01% 20d=12.34% aboveMA50=50.0%
- #8 Banking & Financials: score=6.62 5d=-0.35% 20d=6.15% aboveMA50=70.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- AJWA.CA: BULLISH_WATCH score=94.62 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- TALM.CA: BULLISH_WATCH score=93 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- SPIN.CA: BULLISH_WATCH score=91.52 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- SEIG.CA: BULLISH_WATCH score=90.62 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support
- ICID.CA: BULLISH_WATCH score=90.62 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support
- ROTO.CA: BULLISH_WATCH score=88.62 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ETRS.CA: BULLISH_WATCH score=83.62 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SCFM.CA: BULLISH_WATCH score=82.62 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- GSSC.CA: BULLISH_WATCH score=80.62 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=11.4 buy_ready=False sector_rank=5 price=273.78 support=240.49 resistance=289.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=187338288.0 spike=9.23
- ABUK.CA: score=19.64 buy_ready=False sector_rank=17 price=72.8 support=67.04 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.07 liquidity=160525008.0 spike=1.06
- ACAMD.CA: score=21.4 buy_ready=False sector_rank=5 price=2.32 support=2.2 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=72595928.0 spike=0.99
- ACGC.CA: score=22.4 buy_ready=False sector_rank=3 price=10.5 support=9.03 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.04 liquidity=15543014.0 spike=0.51
- ADCI.CA: score=14.47 buy_ready=False sector_rank=5 price=250.07 support=230.0 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=77.43 liquidity=6073987.0 spike=0.59
- ADIB.CA: score=18.4 buy_ready=False sector_rank=8 price=52.11 support=44.9 resistance=52.88 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=79.65 liquidity=104139751.82 spike=0.78
- ADPC.CA: score=21.4 buy_ready=False sector_rank=5 price=3.82 support=3.37 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.2 liquidity=24543562.0 spike=0.72
- AFDI.CA: score=20.88 buy_ready=False sector_rank=5 price=51.33 support=42.6 resistance=52.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=79.14 liquidity=21950298.0 spike=1.24
- AFMC.CA: score=11.4 buy_ready=False sector_rank=5 price=184.0 support=148.0 resistance=184.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=305435584.0 spike=5.0
- AJWA.CA: score=26.76 buy_ready=False sector_rank=5 price=191.12 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.22 liquidity=75489496.0 spike=2.68
- ALCN.CA: score=18.66 buy_ready=False sector_rank=16 price=29.44 support=27.74 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.48 liquidity=12354932.0 spike=0.54
- ALUM.CA: score=10.07 buy_ready=False sector_rank=5 price=22.9 support=20.8 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.21 liquidity=1668694.75 spike=0.27
- AMER.CA: score=20.04 buy_ready=False sector_rank=13 price=4.52 support=2.32 resistance=4.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=91.74 liquidity=68653032.0 spike=0.6
- AMES.CA: score=21.4 buy_ready=False sector_rank=5 price=120.03 support=57.23 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.14 liquidity=24829114.0 spike=0.23
- AMIA.CA: score=20.4 buy_ready=False sector_rank=5 price=11.25 support=8.43 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.14 liquidity=11597337.0 spike=0.78
- AMOC.CA: score=11.32 buy_ready=False sector_rank=10 price=8.9 support=8.55 resistance=9.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=391681248.0 spike=6.5
- APSW.CA: score=13.08 buy_ready=False sector_rank=5 price=8.75 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=682092.44 spike=0.44
- ARAB.CA: score=19.04 buy_ready=False sector_rank=13 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.98 liquidity=68119984.0 spike=0.51
- ARCC.CA: score=20.72 buy_ready=False sector_rank=7 price=55.95 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=32403968.0 spike=1.16
- AREH.CA: score=16.4 buy_ready=False sector_rank=5 price=1.4 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=13027714.0 spike=0.46
- ARVA.CA: score=8.4 buy_ready=False sector_rank=5 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=81.74 liquidity=0.0 spike=0.0
- ASCM.CA: score=18.4 buy_ready=False sector_rank=5 price=62.8 support=57.25 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=53864424.0 spike=0.99
- ASPI.CA: score=18.4 buy_ready=False sector_rank=5 price=0.43 support=0.31 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.64 liquidity=27439312.0 spike=0.7
- ATLC.CA: score=13.08 buy_ready=False sector_rank=15 price=5.15 support=4.97 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=4370816.5 spike=0.62
- ATQA.CA: score=21.46 buy_ready=False sector_rank=17 price=10.05 support=9.35 resistance=10.37 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=76.47 liquidity=115955354.5 spike=2.97
- AXPH.CA: score=14.96 buy_ready=False sector_rank=5 price=1209.64 support=1090.02 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.19 liquidity=3562153.5 spike=0.91
- BINV.CA: score=13.47 buy_ready=False sector_rank=14 price=47.46 support=45.09 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.93 liquidity=4450840.5 spike=0.61
- BIOC.CA: score=11.4 buy_ready=False sector_rank=5 price=239.76 support=210.5 resistance=239.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=265610480.0 spike=4.07
- BTFH.CA: score=17.17 buy_ready=False sector_rank=15 price=3.07 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=269689536.0 spike=1.23
- CAED.CA: score=18.4 buy_ready=False sector_rank=5 price=125.11 support=70.1 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.81 liquidity=22150708.0 spike=0.32
- CANA.CA: score=20.5 buy_ready=False sector_rank=8 price=37.57 support=35.18 resistance=39.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=18199574.0 spike=1.05
- CCAP.CA: score=16.02 buy_ready=False sector_rank=14 price=5.16 support=4.71 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=581034880.0 spike=0.82
- CCRS.CA: score=21.72 buy_ready=False sector_rank=5 price=2.56 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.0 liquidity=20330782.0 spike=1.16
- CEFM.CA: score=24.8 buy_ready=False sector_rank=5 price=134.07 support=96.1 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.78 liquidity=62464212.0 spike=2.7
- CERA.CA: score=19.4 buy_ready=False sector_rank=5 price=1.26 support=1.2 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=10610142.0 spike=0.43
- CFGH.CA: score=-0.7 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37887.92 spike=2.43
- CICH.CA: score=19.44 buy_ready=False sector_rank=15 price=12.26 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=6311972.5 spike=1.21
- CIEB.CA: score=17.03 buy_ready=False sector_rank=8 price=24.09 support=23.37 resistance=24.59 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=54.86 liquidity=7627110.86 spike=0.87
- CIRA.CA: score=23.52 buy_ready=False sector_rank=1 price=35.04 support=27.74 resistance=36.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=84.29 liquidity=56649064.0 spike=1.06
- CLHO.CA: score=19.35 buy_ready=False sector_rank=9 price=16.3 support=15.98 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=21468284.0 spike=0.49
- CNFN.CA: score=18.71 buy_ready=False sector_rank=15 price=4.76 support=4.7 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.82 liquidity=13174510.0 spike=0.63
- COMI.CA: score=21.4 buy_ready=False sector_rank=8 price=140.3 support=126.89 resistance=142.88 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=68.64 liquidity=379429853.65 spike=0.91
- COPR.CA: score=17.4 buy_ready=False sector_rank=5 price=0.4 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=20881788.0 spike=0.69
- COSG.CA: score=19.4 buy_ready=False sector_rank=5 price=1.61 support=1.5 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.18 liquidity=33859500.0 spike=0.76
- CPCI.CA: score=14.27 buy_ready=False sector_rank=5 price=461.39 support=389.0 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=72.51 liquidity=2873199.25 spike=0.25
- CSAG.CA: score=16.3 buy_ready=False sector_rank=16 price=31.63 support=32.0 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=19347458.0 spike=1.32
- DAPH.CA: score=21.2 buy_ready=False sector_rank=5 price=94.99 support=80.06 resistance=99.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.96 liquidity=25148420.0 spike=1.4
- DEIN.CA: score=-3.6 buy_ready=False sector_rank=5 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=9.95 buy_ready=False sector_rank=18 price=26.55 support=26.35 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=2261531.0 spike=0.71
- DSCW.CA: score=21.4 buy_ready=False sector_rank=5 price=1.94 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=48897396.0 spike=0.9
- DTPP.CA: score=21.4 buy_ready=False sector_rank=5 price=247.76 support=153.55 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.3 liquidity=72326968.0 spike=0.93
- EALR.CA: score=11.4 buy_ready=False sector_rank=5 price=391.3 support=365.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=174521488.0 spike=9.29
- EASB.CA: score=17.12 buy_ready=False sector_rank=5 price=7.19 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=7722957.5 spike=0.58
- EAST.CA: score=15.68 buy_ready=False sector_rank=18 price=36.45 support=36.01 resistance=37.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=69719888.0 spike=0.89
- EBSC.CA: score=11.01 buy_ready=False sector_rank=5 price=1.87 support=1.74 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=1609857.25 spike=0.19
- ECAP.CA: score=13.81 buy_ready=False sector_rank=5 price=32.96 support=31.95 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=4405623.5 spike=0.76
- EDFM.CA: score=20.09 buy_ready=False sector_rank=5 price=386.16 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=73.92 liquidity=7566322.0 spike=1.56
- EEII.CA: score=19.4 buy_ready=False sector_rank=5 price=2.6 support=2.37 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=13230788.0 spike=0.58
- EFIC.CA: score=23.54 buy_ready=False sector_rank=17 price=198.97 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.09 liquidity=33041926.0 spike=2.01
- EFID.CA: score=9.68 buy_ready=False sector_rank=18 price=27.24 support=26.64 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.03 liquidity=39667456.0 spike=0.85
- EFIH.CA: score=23.15 buy_ready=False sector_rank=11 price=22.69 support=20.16 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.31 liquidity=52776520.0 spike=0.84
- EGAL.CA: score=17.52 buy_ready=False sector_rank=17 price=296.32 support=275.0 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.2 liquidity=26227108.0 spike=0.62
- EGAS.CA: score=23.74 buy_ready=False sector_rank=10 price=52.77 support=48.5 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=15720700.0 spike=1.21
- EGBE.CA: score=10.74 buy_ready=False sector_rank=8 price=0.48 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=95.96 liquidity=123413.56 spike=2.11
- EGCH.CA: score=15.54 buy_ready=False sector_rank=17 price=12.93 support=12.19 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=62071876.0 spike=1.01
- EGSA.CA: score=6.41 buy_ready=False sector_rank=6 price=8.87 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8866.02 spike=0.48
- EGTS.CA: score=16.04 buy_ready=False sector_rank=13 price=17.39 support=16.75 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.35 liquidity=43603588.0 spike=0.96
- EHDR.CA: score=19.48 buy_ready=False sector_rank=5 price=2.74 support=2.44 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.06 liquidity=42830172.0 spike=1.04
- EKHO.CA: score=5.32 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=20.4 buy_ready=False sector_rank=4 price=2.15 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.53 liquidity=45181528.0 spike=0.65
- ELKA.CA: score=7.54 buy_ready=False sector_rank=5 price=1.69 support=1.69 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120443992.0 spike=1.57
- ELNA.CA: score=11.61 buy_ready=False sector_rank=5 price=37.54 support=36.1 resistance=40.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.52 liquidity=1467421.38 spike=2.37
- ELSH.CA: score=6.4 buy_ready=False sector_rank=5 price=13.45 support=13.31 resistance=14.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=139466384.0 spike=0.97
- ELWA.CA: score=2.2 buy_ready=False sector_rank=5 price=1.75 support=1.74 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=801792.06 spike=0.52
- EMFD.CA: score=16.04 buy_ready=False sector_rank=13 price=11.21 support=11.4 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.1 liquidity=47776040.0 spike=0.79
- ENGC.CA: score=19.4 buy_ready=False sector_rank=5 price=41.27 support=36.0 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.59 liquidity=24768642.0 spike=0.98
- EOSB.CA: score=18.85 buy_ready=False sector_rank=5 price=1.55 support=1.5 resistance=1.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=446389.16 spike=12.3
- EPCO.CA: score=16.43 buy_ready=False sector_rank=5 price=10.5 support=8.57 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=8031109.0 spike=0.27
- EPPK.CA: score=11.73 buy_ready=False sector_rank=5 price=15.07 support=13.03 resistance=15.93 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=58.31 liquidity=334674.55 spike=0.27
- ETEL.CA: score=22.16 buy_ready=False sector_rank=6 price=104.06 support=90.05 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=84.46 liquidity=157998832.0 spike=1.88
- ETRS.CA: score=21.4 buy_ready=False sector_rank=5 price=10.64 support=10.1 resistance=11.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=32485272.0 spike=0.69
- EXPA.CA: score=22.04 buy_ready=False sector_rank=8 price=20.0 support=18.14 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=85.34 liquidity=56573808.0 spike=1.82
- FAIT.CA: score=7.57 buy_ready=False sector_rank=8 price=36.55 support=35.6 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.56 liquidity=1173371.75 spike=0.41
- FAITA.CA: score=1.41 buy_ready=False sector_rank=8 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=29.82 liquidity=8243.91 spike=0.19
- FERC.CA: score=11.29 buy_ready=False sector_rank=17 price=75.9 support=72.91 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.04 liquidity=4763286.0 spike=0.4
- FWRY.CA: score=18.15 buy_ready=False sector_rank=11 price=18.97 support=18.28 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.7 liquidity=69164152.0 spike=0.53
- GBCO.CA: score=19.11 buy_ready=False sector_rank=12 price=29.7 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.45 liquidity=30344868.0 spike=0.43
- GDWA.CA: score=15.4 buy_ready=False sector_rank=5 price=0.8 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.86 liquidity=82640472.0 spike=0.8
- GGCC.CA: score=18.4 buy_ready=False sector_rank=5 price=0.83 support=0.46 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=79.32 liquidity=23597932.0 spike=0.61
- GIHD.CA: score=21.4 buy_ready=False sector_rank=5 price=56.94 support=40.91 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.4 liquidity=18886688.0 spike=0.36
- GMCI.CA: score=9.74 buy_ready=False sector_rank=5 price=1.97 support=1.74 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=336778.34 spike=0.25
- GRCA.CA: score=21.4 buy_ready=False sector_rank=5 price=59.58 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.51 liquidity=10015063.0 spike=0.61
- GSSC.CA: score=25.4 buy_ready=False sector_rank=5 price=284.0 support=241.32 resistance=300.0 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=76.68 liquidity=46065084.0 spike=3.81
- GTWL.CA: score=21.4 buy_ready=False sector_rank=5 price=101.67 support=76.25 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=42657028.0 spike=0.31
- HDBK.CA: score=19.4 buy_ready=False sector_rank=8 price=82.41 support=76.9 resistance=86.5 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=53.14 liquidity=20867943.54 spike=0.74
- HELI.CA: score=20.4 buy_ready=False sector_rank=13 price=8.25 support=6.4 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.57 liquidity=240497440.0 spike=1.18
- HRHO.CA: score=14.71 buy_ready=False sector_rank=15 price=26.3 support=26.25 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.65 liquidity=66092544.0 spike=0.77
- ICID.CA: score=23.78 buy_ready=False sector_rank=5 price=8.2 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=16559684.0 spike=2.19
- IDRE.CA: score=21.4 buy_ready=False sector_rank=5 price=47.68 support=41.8 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.69 liquidity=14850760.0 spike=0.55
- IFAP.CA: score=22.84 buy_ready=False sector_rank=2 price=19.51 support=18.96 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.19 liquidity=11503346.0 spike=1.22
- INFI.CA: score=19.48 buy_ready=False sector_rank=5 price=106.68 support=89.02 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=75.62 liquidity=25850874.0 spike=1.54
- IRON.CA: score=6.5 buy_ready=False sector_rank=17 price=30.62 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.87 liquidity=6819119.5 spike=1.08
- ISMA.CA: score=18.4 buy_ready=False sector_rank=5 price=30.68 support=26.54 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=82.93 liquidity=17621602.0 spike=0.68
- ISMQ.CA: score=5.74 buy_ready=False sector_rank=17 price=9.0 support=8.96 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103418016.0 spike=1.11
- ISPH.CA: score=18.35 buy_ready=False sector_rank=9 price=11.37 support=11.2 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.81 liquidity=36171680.0 spike=0.74
- JUFO.CA: score=9.68 buy_ready=False sector_rank=18 price=28.67 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=19.68 liquidity=20528566.0 spike=0.79
- KABO.CA: score=22.4 buy_ready=False sector_rank=3 price=8.08 support=6.21 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.11 liquidity=21586872.0 spike=0.44
- KWIN.CA: score=18.4 buy_ready=False sector_rank=5 price=97.3 support=66.1 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=89.37 liquidity=40375880.0 spike=0.78
- KZPC.CA: score=11.31 buy_ready=False sector_rank=5 price=8.5 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=3913399.0 spike=0.76
- LCSW.CA: score=21.4 buy_ready=False sector_rank=7 price=34.14 support=27.64 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.69 liquidity=32463642.0 spike=0.48
- LUTS.CA: score=10.4 buy_ready=False sector_rank=5 price=0.54 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.65 liquidity=10794354.0 spike=0.32
- MAAL.CA: score=18.4 buy_ready=False sector_rank=5 price=8.84 support=7.09 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=78.62 liquidity=14073630.0 spike=0.86
- MASR.CA: score=19.4 buy_ready=False sector_rank=5 price=7.94 support=7.24 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.68 liquidity=78978688.0 spike=0.92
- MBSC.CA: score=16.6 buy_ready=False sector_rank=7 price=242.15 support=230.0 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.17 liquidity=8198475.5 spike=0.44
- MCQE.CA: score=20.4 buy_ready=False sector_rank=7 price=182.43 support=168.05 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=15632476.0 spike=0.86
- MCRO.CA: score=20.4 buy_ready=False sector_rank=5 price=1.49 support=1.19 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=111266696.0 spike=0.83
- MENA.CA: score=9.82 buy_ready=False sector_rank=13 price=6.92 support=6.72 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=784035.75 spike=0.1
- MEPA.CA: score=21.4 buy_ready=False sector_rank=5 price=1.8 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=71.7 liquidity=32954272.0 spike=0.68
- MFPC.CA: score=17.8 buy_ready=False sector_rank=17 price=36.6 support=34.95 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.49 liquidity=101219016.0 spike=1.14
- MFSC.CA: score=10.83 buy_ready=False sector_rank=5 price=46.48 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=4426418.0 spike=0.78
- MHOT.CA: score=12.62 buy_ready=False sector_rank=19 price=16.33 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.38 liquidity=6984793.5 spike=0.61
- MICH.CA: score=21.4 buy_ready=False sector_rank=5 price=40.46 support=36.1 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=16379240.0 spike=1.0
- MILS.CA: score=26.22 buy_ready=False sector_rank=5 price=194.06 support=126.31 resistance=205.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.81 liquidity=109072104.0 spike=2.41
- MIPH.CA: score=12.38 buy_ready=False sector_rank=9 price=740.09 support=632.11 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=64.07 liquidity=1025740.5 spike=0.3
- MOED.CA: score=16.5 buy_ready=False sector_rank=5 price=0.68 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.4 liquidity=37167528.0 spike=1.55
- MOIL.CA: score=12.4 buy_ready=False sector_rank=10 price=0.68 support=0.46 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=92.31 liquidity=1084080.12 spike=1.5
- MOIN.CA: score=5.69 buy_ready=False sector_rank=5 price=23.6 support=22.66 resistance=24.76 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=46.41 liquidity=293159.2 spike=0.38
- MOSC.CA: score=18.57 buy_ready=False sector_rank=5 price=285.19 support=260.01 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.47 liquidity=7173033.5 spike=0.59
- MPCI.CA: score=20.96 buy_ready=False sector_rank=5 price=290.01 support=236.1 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=89.58 liquidity=125587568.0 spike=1.28
- MPCO.CA: score=30.4 buy_ready=False sector_rank=2 price=1.97 support=1.76 resistance=2.07 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=67.35 liquidity=450149571.03 spike=5.56
- MPRC.CA: score=20.4 buy_ready=False sector_rank=5 price=45.01 support=37.51 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.44 liquidity=25951764.0 spike=0.85
- MTIE.CA: score=21.75 buy_ready=False sector_rank=12 price=9.46 support=8.92 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.84 liquidity=31138722.0 spike=1.32
- NAHO.CA: score=5.41 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=13223.54 spike=0.46
- NCCW.CA: score=18.66 buy_ready=False sector_rank=5 price=6.9 support=5.94 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.41 liquidity=31711154.0 spike=1.13
- NEDA.CA: score=6.72 buy_ready=False sector_rank=5 price=2.74 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=320087.97 spike=0.42
- NHPS.CA: score=21.4 buy_ready=False sector_rank=5 price=83.19 support=62.1 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=18029816.0 spike=0.21
- NINH.CA: score=18.4 buy_ready=False sector_rank=5 price=21.4 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=76.48 liquidity=15971238.0 spike=0.36
- NIPH.CA: score=18.97 buy_ready=False sector_rank=9 price=223.58 support=160.55 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.42 liquidity=204406032.0 spike=1.31
- OBRI.CA: score=15.52 buy_ready=False sector_rank=5 price=32.4 support=32.4 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.48 liquidity=44464260.0 spike=1.06
- OCDI.CA: score=21.04 buy_ready=False sector_rank=13 price=28.11 support=24.31 resistance=29.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.34 liquidity=83310560.0 spike=0.86
- OCPH.CA: score=18.4 buy_ready=False sector_rank=5 price=463.77 support=348.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=83.04 liquidity=14209707.0 spike=0.57
- ODIN.CA: score=22.94 buy_ready=False sector_rank=5 price=2.76 support=2.07 resistance=2.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=41497364.0 spike=2.27
- OFH.CA: score=21.4 buy_ready=False sector_rank=5 price=0.7 support=0.58 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=73.74 liquidity=41239528.0 spike=0.62
- OIH.CA: score=23.28 buy_ready=False sector_rank=14 price=1.47 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=147533104.0 spike=2.13
- OLFI.CA: score=19.68 buy_ready=False sector_rank=18 price=22.77 support=21.91 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.11 liquidity=11821285.0 spike=0.34
- ORAS.CA: score=4.6 buy_ready=False sector_rank=20 price=714.42 support=702.05 resistance=719.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=138172736.0 spike=1.0
- ORHD.CA: score=21.58 buy_ready=False sector_rank=13 price=39.2 support=37.52 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.77 liquidity=187623728.0 spike=1.27
- ORWE.CA: score=19.4 buy_ready=False sector_rank=3 price=22.63 support=22.2 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.81 liquidity=23915666.0 spike=0.98
- PHAR.CA: score=11.35 buy_ready=False sector_rank=9 price=103.96 support=95.75 resistance=104.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=464787392.0 spike=7.44
- PHDC.CA: score=16.04 buy_ready=False sector_rank=13 price=14.34 support=14.41 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.41 liquidity=168329216.0 spike=0.71
- PHTV.CA: score=12.47 buy_ready=False sector_rank=5 price=321.35 support=260.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=83.89 liquidity=2074411.25 spike=0.42
- POUL.CA: score=9.68 buy_ready=False sector_rank=18 price=37.73 support=37.02 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.27 liquidity=16620577.0 spike=0.49
- PRCL.CA: score=19.4 buy_ready=False sector_rank=7 price=34.93 support=30.6 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.73 liquidity=15089387.0 spike=0.31
- PRDC.CA: score=21.04 buy_ready=False sector_rank=13 price=9.15 support=7.26 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=47903708.0 spike=0.4
- PRMH.CA: score=16.4 buy_ready=False sector_rank=5 price=2.6 support=2.45 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=10455731.0 spike=0.63
- RACC.CA: score=19.4 buy_ready=False sector_rank=5 price=10.0 support=9.55 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.59 liquidity=16223194.0 spike=0.73
- RAKT.CA: score=12.88 buy_ready=False sector_rank=5 price=22.53 support=21.25 resistance=23.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=702689.25 spike=2.39
- RAYA.CA: score=14.35 buy_ready=False sector_rank=21 price=7.48 support=7.12 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.52 liquidity=53781692.0 spike=0.39
- RMDA.CA: score=22.33 buy_ready=False sector_rank=9 price=5.27 support=4.9 resistance=5.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.35 liquidity=42974648.0 spike=1.49
- ROTO.CA: score=21.4 buy_ready=False sector_rank=5 price=42.54 support=40.5 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.75 liquidity=18574926.0 spike=0.93
- RREI.CA: score=11.4 buy_ready=False sector_rank=5 price=4.61 support=4.57 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=206323904.0 spike=3.79
- RTVC.CA: score=20.2 buy_ready=False sector_rank=5 price=3.77 support=3.65 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=10895194.0 spike=2.4
- RUBX.CA: score=18.28 buy_ready=False sector_rank=5 price=12.44 support=11.07 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.66 liquidity=8883718.0 spike=0.13
- SAUD.CA: score=21.88 buy_ready=False sector_rank=8 price=21.97 support=20.5 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=12013617.0 spike=1.24
- SCEM.CA: score=19.68 buy_ready=False sector_rank=7 price=80.51 support=60.14 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=85.83 liquidity=119987232.0 spike=1.64
- SCFM.CA: score=22.52 buy_ready=False sector_rank=5 price=284.16 support=235.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.3 liquidity=38867980.0 spike=1.56
- SCTS.CA: score=14.57 buy_ready=False sector_rank=1 price=608.31 support=543.01 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.64 liquidity=2170644.25 spike=0.31
- SDTI.CA: score=22.12 buy_ready=False sector_rank=5 price=58.18 support=45.85 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=92.97 liquidity=31033786.0 spike=1.86
- SEIG.CA: score=24.96 buy_ready=False sector_rank=5 price=252.45 support=185.0 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=67289360.0 spike=2.78
- SIPC.CA: score=18.68 buy_ready=False sector_rank=5 price=3.99 support=3.27 resistance=4.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=84.27 liquidity=27759890.0 spike=1.14
- SKPC.CA: score=18.74 buy_ready=False sector_rank=17 price=15.8 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.95 liquidity=74540048.0 spike=2.11
- SMFR.CA: score=21.4 buy_ready=False sector_rank=5 price=233.47 support=191.02 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.78 liquidity=16197633.0 spike=0.78
- SNFC.CA: score=15.21 buy_ready=False sector_rank=5 price=11.16 support=11.04 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=8808561.0 spike=0.77
- SPIN.CA: score=22.76 buy_ready=False sector_rank=3 price=15.64 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.14 liquidity=29257656.0 spike=1.18
- SPMD.CA: score=21.4 buy_ready=False sector_rank=5 price=0.45 support=0.42 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=18827666.0 spike=0.69
- SUGR.CA: score=13.9 buy_ready=False sector_rank=18 price=46.49 support=46.01 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.27 liquidity=7451075.0 spike=1.38
- SVCE.CA: score=16.4 buy_ready=False sector_rank=5 price=9.13 support=8.9 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.48 liquidity=19355376.0 spike=0.36
- SWDY.CA: score=18.8 buy_ready=False sector_rank=4 price=93.0 support=85.11 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.22 liquidity=25053372.0 spike=1.2
- TALM.CA: score=27.32 buy_ready=False sector_rank=1 price=17.68 support=15.27 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.76 liquidity=83738488.0 spike=2.96
- TMGH.CA: score=16.14 buy_ready=False sector_rank=13 price=96.0 support=92.6 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=383727776.0 spike=1.05
- TRTO.CA: score=7.4 buy_ready=False sector_rank=5 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=20.32 buy_ready=False sector_rank=5 price=537.5 support=467.2 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=74.27 liquidity=7743882.5 spike=1.59
- UEGC.CA: score=21.4 buy_ready=False sector_rank=5 price=2.32 support=1.36 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=29396986.0 spike=0.55
- UNIP.CA: score=21.4 buy_ready=False sector_rank=5 price=0.38 support=0.32 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.51 liquidity=18300560.0 spike=0.67
- UNIT.CA: score=12.18 buy_ready=False sector_rank=13 price=17.45 support=12.66 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.56 liquidity=3141697.0 spike=0.1
- WCDF.CA: score=16.09 buy_ready=False sector_rank=5 price=583.68 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=2691170.0 spike=0.86
- WKOL.CA: score=11.4 buy_ready=False sector_rank=5 price=328.79 support=311.0 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=147225600.0 spike=14.19
- ZEOT.CA: score=21.54 buy_ready=False sector_rank=5 price=12.33 support=10.8 resistance=12.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=79.82 liquidity=47183520.0 spike=1.57
- ZMID.CA: score=6.86 buy_ready=False sector_rank=13 price=7.2 support=7.17 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=365923744.0 spike=1.41

## Backtesting Lite
- MPCO.CA: 180d return=12.57%, max drawdown=-20.56%, MA20>MA50 days last20=20, as_of=2026-07-28T21:00:00+00:00
- TALM.CA: 180d return=10.3%, max drawdown=-12.21%, MA20>MA50 days last20=8, as_of=2026-07-28T21:00:00+00:00
- AJWA.CA: 180d return=44.49%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-07-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=575 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- MILS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=North Cairo Flour Mills summary=North Cairo Mills stock hits historic peak amid clear emergence of buying power; North Cairo Mills approves EGP 0.5/shr dividends for FY19/20; North Cairo Mills reports 37% profit decline in FY19/20 initial results
  - North Cairo Mills stock hits historic peak amid clear emergence of buying power: https://english.mubasher.info/news/4540088/North-Cairo-Mills-stock-hits-historic-peak-amid-clear-emergence-of-buying-power/
  - North Cairo Mills approves EGP 0.5/shr dividends for FY19/20: https://english.mubasher.info/news/3726135/North-Cairo-Mills-approves-EGP-0-5-shr-dividends-for-FY19-20/
  - North Cairo Mills reports 37% profit decline in FY19/20 initial results: https://english.mubasher.info/news/3676432/North-Cairo-Mills-reports-37-profit-decline-in-FY19-20-initial-results/
- GSSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=General Co. For Silos & Storage summary=General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials; General Company for Silos to set up new firm with EGP 500m capital; General Company for Silos’ EGM nods to EGP 25m capital hike
  - General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials: https://english.mubasher.info/news/4529067/General-Company-for-Silos-generates-nearly-EGP-62m-net-profits-in-Q1-25-26-audited-financials/
  - General Company for Silos to set up new firm with EGP 500m capital: https://english.mubasher.info/news/4043715/General-Company-for-Silos-to-set-up-new-firm-with-EGP-500m-capital/
  - General Company for Silos’ EGM nods to EGP 25m capital hike: https://english.mubasher.info/news/4018676/General-Company-for-Silos-EGM-nods-to-EGP-25m-capital-hike/
- SEIG.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=575 sources=3 expected=Saudi Egyptian Investment & Finance Co. S.A.E summary=Saudi Egyptian Investment unveils EGP 2/shr dividends for 2025; Saudi Egyptian Investment and Finance sees 15% higher profit in 2020; Saudi Egyptian Investment records higher profit in 2019
  - Saudi Egyptian Investment unveils EGP 2/shr dividends for 2025: https://english.mubasher.info/news/4590273/Saudi-Egyptian-Investment-unveils-EGP-2-shr-dividends-for-2025/
  - Saudi Egyptian Investment and Finance sees 15% higher profit in 2020: https://english.mubasher.info/news/3766715/Saudi-Egyptian-Investment-and-Finance-sees-15-higher-profit-in-2020/
  - Saudi Egyptian Investment records higher profit in 2019: https://english.mubasher.info/news/3588475/Saudi-Egyptian-Investment-records-higher-profit-in-2019/
- CEFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Middle Egypt Flour Mills summary=Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26; Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend; Middle Egypt Mills reports 23% profit drop in FY19/20
  - Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26: https://english.mubasher.info/news/4601809/Middle-Egypt-Flour-Mills-posts-lower-net-profits-at-EGP-77m-in-9M-25-26/
  - Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend: https://english.mubasher.info/news/3870911/Middle-Egypt-Flour-Mills-shareholders-approve-EGP-3-25-shr-dividend/
  - Middle Egypt Mills reports 23% profit drop in FY19/20: https://english.mubasher.info/news/3703590/Middle-Egypt-Mills-reports-23-profit-drop-in-FY19-20/
- ICID.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=International Co. For Investment & Development summary=ICID stock targets higher levels after breaking EGP 4.10; International Company for Investment reports EGP 13m in 9M-25 consolidated net profits; ICID to sell land plot for EGP 4.39m
  - ICID stock targets higher levels after breaking EGP 4.10: https://english.mubasher.info/news/4595529/ICID-stock-targets-higher-levels-after-breaking-EGP-4-10/
  - International Company for Investment reports EGP 13m in 9M-25 consolidated net profits: https://english.mubasher.info/news/4530420/International-Company-for-Investment-reports-EGP-13m-in-9M-25-consolidated-net-profits/
  - ICID to sell land plot for EGP 4.39m: https://english.mubasher.info/news/4013131/ICID-to-sell-land-plot-for-EGP-4-39m/

## Warnings
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence for MILS.CA matches the company but no source/report date was detected.
- Evidence for GSSC.CA matches the company but no source/report date was detected.
- Evidence for SEIG.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CEFM.CA matches the company but no source/report date was detected.
- Evidence for ICID.CA matches the company but no source/report date was detected.
