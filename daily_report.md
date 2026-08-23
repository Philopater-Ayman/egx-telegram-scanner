# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-23T08:25:59.424544+00:00
Generated Cairo: 2026-08-23 11:25
Run timing: target 11:00 Cairo | generated Cairo 2026-08-23 11:25 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-23 11:22

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 176/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, August 23
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 75.0% / above MA50 80.0%
- EGX70 regime: MIXED / above MA20 64.1% / above MA50 82.05%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=177540832.0 spike=0.3 score=25.4
- NIPH.CA: liquidity=152513104.0 spike=0.5 score=6.4
- PHAR.CA: liquidity=141006480.0 spike=0.32 score=21.4
- EMFD.CA: liquidity=134330336.0 spike=2.23 score=22.79
- LUTS.CA: liquidity=131503512.0 spike=0.9 score=5.84

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are mixed with sector breadth at 33%, triggering a defensive risk mode that blocks new buys; the scanner highlights high‑rank tickets but holds them due to cooling liquidity and proximity to resistance.
- Top tickets (ETEL.CA, CCAP.CA, GRCA.CA) show strong rank scores yet sit near 20‑day resistance with liquidity cooling, limiting near‑term upside.
- Sector leadership is narrow – Telecommunications leads, while Education and Transportation display solid 20‑day returns but weak liquidity spikes.
- Mixed EGX30/EGX70 trend and DEFENSIVE_NO_NEW_BUY mode keep bullish outlooks tentative, with low confidence across the board.
- Uncertainty remains from negative 5‑day returns and weak breadth, so prices could stall or reverse despite bullish watch scores.

## Top Liquidity Spikes
- EGSA.CA: spike=51.67 liquidity=881841.98 outlook=WEAK_OR_RISKY score=4 buy_ready=False
- ELWA.CA: spike=2.77 liquidity=3924582.2 outlook=CONSTRUCTIVE score=52.59 buy_ready=False
- ELNA.CA: spike=2.64 liquidity=1047062.72 outlook=WEAK_OR_RISKY score=21.59 buy_ready=False
- EMFD.CA: spike=2.23 liquidity=134330336.0 outlook=BULLISH_WATCH score=77.33 buy_ready=False
- TRTO.CA: spike=2.15 liquidity=21931.35 outlook=NEUTRAL score=43.59 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=42.94 5d=0.56% 20d=4.0% aboveMA50=50.0%
- #2 Education: score=9.73 5d=0.4% 20d=17.32% aboveMA50=100.0%
- #3 Transportation & Logistics: score=9.03 5d=-1.54% 20d=14.23% aboveMA50=100.0%
- #4 Building Materials: score=9.0 5d=-1.94% 20d=20.36% aboveMA50=100.0%
- #5 Fintech & Payments: score=7.3 5d=1.12% 20d=2.14% aboveMA50=100.0%
- #6 Investment Holding: score=7.22 5d=3.83% 20d=1.63% aboveMA50=100.0%
- #7 Banking & Financials: score=7.21 5d=0.24% 20d=9.59% aboveMA50=90.0%
- #8 Textiles: score=6.92 5d=1.59% 20d=6.26% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CIRA.CA: BULLISH_WATCH score=89.73 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- TALM.CA: BULLISH_WATCH score=85.73 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- GRCA.CA: BULLISH_WATCH score=80.59 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ALCN.CA: BULLISH_WATCH score=80.03 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; close to resistance
- LCSW.CA: BULLISH_WATCH score=79.0 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ETEL.CA: BULLISH_WATCH score=78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; close to resistance
- EMFD.CA: BULLISH_WATCH score=77.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- FWRY.CA: BULLISH_WATCH score=77.3 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CCAP.CA: BULLISH_WATCH score=77.22 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- ADIB.CA: BULLISH_WATCH score=77.21 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=22.84 buy_ready=False sector_rank=14 price=333.81 support=235.7 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=53.37 liquidity=14535673.0 spike=0.25
- ABUK.CA: score=23.26 buy_ready=False sector_rank=13 price=76.61 support=70.6 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=54.85 liquidity=13676468.0 spike=0.12
- ACAMD.CA: score=10.84 buy_ready=False sector_rank=14 price=2.1 support=2.09 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=16105490.0 spike=0.27
- ACGC.CA: score=20.4 buy_ready=False sector_rank=8 price=13.41 support=10.12 resistance=13.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=77.37 liquidity=11775156.0 spike=0.27
- ADCI.CA: score=14.33 buy_ready=False sector_rank=14 price=298.32 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=3495131.5 spike=0.16
- ADIB.CA: score=16.04 buy_ready=False sector_rank=7 price=54.0 support=48.62 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=51.58 liquidity=4642699.0 spike=0.04
- ADPC.CA: score=15.08 buy_ready=False sector_rank=14 price=4.05 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=6245369.0 spike=0.12
- AFDI.CA: score=9.51 buy_ready=False sector_rank=14 price=62.56 support=48.35 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:57 AM market time freshness=DELAYED_CURRENT RSI=66.32 liquidity=675177.38 spike=0.03
- AFMC.CA: score=20.84 buy_ready=False sector_rank=14 price=228.9 support=102.11 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=11841223.0 spike=0.07
- AJWA.CA: score=18.84 buy_ready=False sector_rank=14 price=188.0 support=175.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=51.21 liquidity=11101944.0 spike=0.24
- ALCN.CA: score=22.4 buy_ready=False sector_rank=3 price=32.06 support=28.8 resistance=32.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=65.03 liquidity=20869690.0 spike=0.87
- ALUM.CA: score=12.15 buy_ready=False sector_rank=14 price=27.17 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=68.23 liquidity=1312988.13 spike=0.06
- AMER.CA: score=20.33 buy_ready=False sector_rank=16 price=5.71 support=4.14 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=59.61 liquidity=15793099.0 spike=0.16
- AMES.CA: score=20.84 buy_ready=False sector_rank=14 price=143.49 support=110.54 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=69.62 liquidity=16541767.0 spike=0.24
- AMIA.CA: score=14.67 buy_ready=False sector_rank=14 price=16.2 support=10.2 resistance=17.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=94.38 liquidity=6831489.5 spike=0.2
- AMOC.CA: score=21.28 buy_ready=False sector_rank=12 price=11.4 support=8.23 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=72.41 liquidity=10127267.0 spike=0.08
- APSW.CA: score=9.11 buy_ready=False sector_rank=14 price=8.79 support=8.6 resistance=9.39 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=52.67 liquidity=1277855.03 spike=0.89
- ARAB.CA: score=18.33 buy_ready=False sector_rank=16 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=15321152.0 spike=0.2
- ARCC.CA: score=12.16 buy_ready=False sector_rank=4 price=72.78 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=79.63 liquidity=3760869.75 spike=0.04
- AREH.CA: score=7.35 buy_ready=False sector_rank=14 price=1.48 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=54.0 liquidity=1511185.0 spike=0.05
- ARVA.CA: score=5.84 buy_ready=False sector_rank=14 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=6.36 buy_ready=False sector_rank=14 price=64.42 support=60.99 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=34.64 liquidity=2528581.0 spike=0.04
- ASPI.CA: score=5.84 buy_ready=False sector_rank=14 price=0.55 support=0.5 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33629828.0 spike=0.82
- ATLC.CA: score=9.12 buy_ready=False sector_rank=19 price=5.31 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=1673161.0 spike=0.09
- ATQA.CA: score=18.26 buy_ready=False sector_rank=13 price=11.26 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=77.25 liquidity=34500776.0 spike=0.45
- AXPH.CA: score=18.77 buy_ready=False sector_rank=14 price=1459.2 support=1121.56 resistance=1630.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=73.95 liquidity=5929819.5 spike=0.9
- BINV.CA: score=10.8 buy_ready=False sector_rank=6 price=48.44 support=46.01 resistance=50.9 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=54.73 liquidity=1398414.32 spike=0.24
- BIOC.CA: score=5.84 buy_ready=False sector_rank=14 price=481.53 support=433.8 resistance=488.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92770904.0 spike=0.39
- BTFH.CA: score=8.45 buy_ready=False sector_rank=19 price=3.02 support=2.98 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=25440304.0 spike=0.11
- CAED.CA: score=14.77 buy_ready=False sector_rank=14 price=164.48 support=118.0 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=78.03 liquidity=6937394.0 spike=0.12
- CANA.CA: score=9.57 buy_ready=False sector_rank=7 price=41.64 support=36.5 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=76.15 liquidity=1166672.63 spike=0.06
- CCAP.CA: score=25.4 buy_ready=False sector_rank=6 price=5.67 support=5.14 resistance=5.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=62.37 liquidity=177540832.0 spike=0.3
- CCRS.CA: score=3.25 buy_ready=False sector_rank=14 price=2.45 support=2.4 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=2415086.5 spike=0.14
- CEFM.CA: score=20.87 buy_ready=False sector_rank=14 price=150.55 support=121.4 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=63.22 liquidity=6032707.5 spike=0.16
- CERA.CA: score=15.03 buy_ready=False sector_rank=14 price=1.3 support=1.23 resistance=1.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=6197960.5 spike=0.38
- CFGH.CA: score=5.26 buy_ready=False sector_rank=14 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=81.25 liquidity=21716.92 spike=1.2
- CICH.CA: score=13.7 buy_ready=False sector_rank=19 price=12.24 support=11.92 resistance=13.25 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=38.75 liquidity=6253501.56 spike=0.96
- CIEB.CA: score=14.29 buy_ready=False sector_rank=7 price=24.75 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=885825.56 spike=0.06
- CIRA.CA: score=16.18 buy_ready=False sector_rank=2 price=37.12 support=31.61 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=52.16 liquidity=2784852.0 spike=0.05
- CLHO.CA: score=18.72 buy_ready=False sector_rank=10 price=17.55 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=7317949.5 spike=0.12
- CNFN.CA: score=12.47 buy_ready=False sector_rank=19 price=4.93 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=3023248.5 spike=0.15
- COMI.CA: score=14.4 buy_ready=False sector_rank=7 price=137.51 support=135.35 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=28.45 liquidity=16886750.0 spike=0.03
- COPR.CA: score=6.42 buy_ready=False sector_rank=14 price=0.55 support=0.54 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99794976.0 spike=1.29
- COSG.CA: score=20.84 buy_ready=False sector_rank=14 price=1.84 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=69.44 liquidity=44042472.0 spike=0.87
- CPCI.CA: score=11.4 buy_ready=False sector_rank=14 price=545.96 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=67.16 liquidity=2561086.5 spike=0.31
- CSAG.CA: score=17.24 buy_ready=False sector_rank=3 price=41.0 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=73.88 liquidity=4837121.5 spike=0.2
- DAPH.CA: score=22.84 buy_ready=False sector_rank=14 price=116.8 support=92.1 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=59.86 liquidity=13803364.0 spike=0.33
- DEIN.CA: score=-4.16 buy_ready=False sector_rank=14 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=8.98 buy_ready=False sector_rank=17 price=28.19 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=57.91 liquidity=854806.5 spike=0.06
- DSCW.CA: score=16.01 buy_ready=False sector_rank=14 price=1.93 support=1.89 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=44.23 liquidity=7175885.0 spike=0.08
- DTPP.CA: score=15.51 buy_ready=False sector_rank=14 price=301.11 support=225.11 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=71.07 liquidity=6672960.0 spike=0.12
- EALR.CA: score=22.84 buy_ready=False sector_rank=14 price=402.48 support=362.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=48.71 liquidity=10187886.0 spike=0.21
- EASB.CA: score=12.43 buy_ready=False sector_rank=14 price=7.36 support=6.71 resistance=8.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=1591204.5 spike=0.16
- EAST.CA: score=7.17 buy_ready=False sector_rank=17 price=36.23 support=36.0 resistance=37.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=42.21 liquidity=1050587.25 spike=0.02
- EBSC.CA: score=11.52 buy_ready=False sector_rank=14 price=1.93 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=685933.56 spike=0.13
- ECAP.CA: score=13.25 buy_ready=False sector_rank=14 price=37.19 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=57.82 liquidity=413606.16 spike=0.03
- EDFM.CA: score=9.22 buy_ready=False sector_rank=14 price=406.01 support=352.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=65.26 liquidity=384219.13 spike=0.1
- EEII.CA: score=18.87 buy_ready=False sector_rank=14 price=3.05 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=8032816.5 spike=0.34
- EFIC.CA: score=20.55 buy_ready=False sector_rank=13 price=215.38 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=61.75 liquidity=7291168.5 spike=0.16
- EFID.CA: score=11.1 buy_ready=False sector_rank=17 price=33.07 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=83.6 liquidity=3976887.0 spike=0.04
- EFIH.CA: score=21.4 buy_ready=False sector_rank=5 price=24.75 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=65.65 liquidity=18662466.0 spike=0.16
- EGAL.CA: score=19.11 buy_ready=False sector_rank=13 price=333.6 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=70.89 liquidity=7854456.0 spike=0.08
- EGAS.CA: score=8.62 buy_ready=False sector_rank=12 price=58.89 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=30.48 liquidity=2344225.5 spike=0.09
- EGBE.CA: score=9.41 buy_ready=False sector_rank=7 price=0.55 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=69.5 liquidity=14963.03 spike=0.07
- EGCH.CA: score=21.26 buy_ready=False sector_rank=13 price=14.23 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=52.29 liquidity=52942112.0 spike=0.43
- EGSA.CA: score=15.28 buy_ready=False sector_rank=1 price=8.69 support=8.65 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 01:02 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=881841.98 spike=51.67
- EGTS.CA: score=14.51 buy_ready=False sector_rank=16 price=16.99 support=16.63 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=42.76 liquidity=9181176.0 spike=0.27
- EHDR.CA: score=16.87 buy_ready=False sector_rank=14 price=2.99 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=4036434.5 spike=0.09
- EKHO.CA: score=7.28 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=10.38 buy_ready=False sector_rank=11 price=2.1 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=27.78 liquidity=22325982.0 spike=0.36
- ELKA.CA: score=18.84 buy_ready=False sector_rank=14 price=1.75 support=1.69 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=21441428.0 spike=0.31
- ELNA.CA: score=4.16 buy_ready=False sector_rank=14 price=36.45 support=36.1 resistance=39.49 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=30.18 liquidity=1047062.72 spike=2.64
- ELSH.CA: score=4.55 buy_ready=False sector_rank=14 price=13.33 support=13.14 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=24.49 liquidity=3713594.0 spike=0.05
- ELWA.CA: score=15.3 buy_ready=False sector_rank=14 price=1.74 support=1.62 resistance=1.94 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=47.5 liquidity=3924582.2 spike=2.77
- EMFD.CA: score=22.79 buy_ready=False sector_rank=16 price=12.14 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=63.58 liquidity=134330336.0 spike=2.23
- ENGC.CA: score=-1.19 buy_ready=False sector_rank=14 price=48.16 support=45.49 resistance=48.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2973641.0 spike=0.1
- EOSB.CA: score=12.84 buy_ready=False sector_rank=14 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=20 August 11:41 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=278.64 spike=0.01
- EPCO.CA: score=9.76 buy_ready=False sector_rank=14 price=11.4 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=52.75 liquidity=920799.44 spike=0.04
- EPPK.CA: score=1.68 buy_ready=False sector_rank=14 price=12.54 support=12.62 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:51 AM market time freshness=DELAYED_CURRENT RSI=23.4 liquidity=844485.06 spike=0.98
- ETEL.CA: score=26.4 buy_ready=False sector_rank=1 price=118.38 support=102.5 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=29326436.0 spike=0.21
- ETRS.CA: score=14.31 buy_ready=False sector_rank=14 price=11.12 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=58.79 liquidity=1472720.75 spike=0.05
- EXPA.CA: score=11.08 buy_ready=False sector_rank=7 price=20.46 support=19.6 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=50.16 liquidity=1676841.5 spike=0.04
- FAIT.CA: score=11.86 buy_ready=False sector_rank=7 price=42.28 support=36.1 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=72.89 liquidity=463483.16 spike=0.11
- FAITA.CA: score=13.4 buy_ready=False sector_rank=7 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=57.75 liquidity=4570.83 spike=0.12
- FERC.CA: score=13.62 buy_ready=False sector_rank=13 price=78.22 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=51.99 liquidity=3355812.0 spike=0.14
- FWRY.CA: score=23.4 buy_ready=False sector_rank=5 price=19.34 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=47821452.0 spike=0.4
- GBCO.CA: score=4.92 buy_ready=False sector_rank=21 price=29.71 support=29.31 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=2515829.0 spike=0.05
- GDWA.CA: score=4.91 buy_ready=False sector_rank=14 price=0.8 support=0.78 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=33.87 liquidity=5071946.0 spike=0.05
- GGCC.CA: score=14.82 buy_ready=False sector_rank=14 price=0.95 support=0.81 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=55.65 liquidity=5986940.0 spike=0.12
- GIHD.CA: score=12.52 buy_ready=False sector_rank=14 price=61.57 support=56.51 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=3680359.75 spike=0.09
- GMCI.CA: score=0.91 buy_ready=False sector_rank=14 price=1.91 support=1.88 resistance=2.1 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=17.39 liquidity=71053.91 spike=0.14
- GRCA.CA: score=24.04 buy_ready=False sector_rank=14 price=64.13 support=54.7 resistance=66.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=55.3 liquidity=42578336.0 spike=1.6
- GSSC.CA: score=15.52 buy_ready=False sector_rank=14 price=288.98 support=264.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=4684168.5 spike=0.25
- GTWL.CA: score=14.84 buy_ready=False sector_rank=14 price=182.75 support=191.21 resistance=191.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=83145760.0 spike=1.0
- HDBK.CA: score=10.73 buy_ready=False sector_rank=7 price=91.9 support=80.8 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=76.45 liquidity=6329095.0 spike=0.15
- HELI.CA: score=13.33 buy_ready=False sector_rank=16 price=7.82 support=7.5 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=21.26 liquidity=29683064.0 spike=0.18
- HRHO.CA: score=12.5 buy_ready=False sector_rank=19 price=26.46 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=9054542.0 spike=0.09
- ICID.CA: score=19.84 buy_ready=False sector_rank=14 price=17.38 support=7.85 resistance=16.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=98.22 liquidity=22471406.0 spike=1.0
- IDRE.CA: score=12.79 buy_ready=False sector_rank=14 price=53.07 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=1952700.88 spike=0.07
- IFAP.CA: score=12.72 buy_ready=False sector_rank=9 price=20.67 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=3322976.25 spike=0.11
- INFI.CA: score=20.84 buy_ready=False sector_rank=14 price=162.28 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=72.54 liquidity=21660038.0 spike=0.35
- IRON.CA: score=11.59 buy_ready=False sector_rank=13 price=31.0 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=56.8 liquidity=4334905.5 spike=0.4
- ISMA.CA: score=16.12 buy_ready=False sector_rank=14 price=36.54 support=28.11 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=89.06 liquidity=6283394.5 spike=0.21
- ISMQ.CA: score=18.72 buy_ready=False sector_rank=13 price=9.25 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9461027.0 spike=0.17
- ISPH.CA: score=21.4 buy_ready=False sector_rank=10 price=13.5 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=23433816.0 spike=0.12
- JUFO.CA: score=4.73 buy_ready=False sector_rank=17 price=26.88 support=22.78 resistance=29.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=83.06 liquidity=1607340.5 spike=0.03
- KABO.CA: score=21.4 buy_ready=False sector_rank=8 price=9.19 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=69.69 liquidity=18671654.0 spike=0.44
- KWIN.CA: score=22.84 buy_ready=False sector_rank=14 price=101.0 support=84.08 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=54.52 liquidity=41465504.0 spike=0.71
- KZPC.CA: score=5.92 buy_ready=False sector_rank=14 price=14.0 support=13.8 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40652160.0 spike=1.04
- LCSW.CA: score=21.4 buy_ready=False sector_rank=4 price=34.73 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=45.34 liquidity=15990139.0 spike=0.36
- LUTS.CA: score=5.84 buy_ready=False sector_rank=14 price=1.58 support=1.58 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=131503512.0 spike=0.9
- MAAL.CA: score=9.94 buy_ready=False sector_rank=14 price=8.74 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=1099542.5 spike=0.09
- MASR.CA: score=18.84 buy_ready=False sector_rank=14 price=7.72 support=7.45 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=35.42 liquidity=12232068.0 spike=0.18
- MBSC.CA: score=15.31 buy_ready=False sector_rank=4 price=372.85 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=83.28 liquidity=6908852.0 spike=0.09
- MCQE.CA: score=17.91 buy_ready=False sector_rank=4 price=222.97 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=65.47 liquidity=6508708.5 spike=0.12
- MCRO.CA: score=20.84 buy_ready=False sector_rank=14 price=1.56 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=50803448.0 spike=0.29
- MENA.CA: score=8.93 buy_ready=False sector_rank=16 price=7.01 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=600207.13 spike=0.1
- MEPA.CA: score=12.39 buy_ready=False sector_rank=14 price=1.85 support=1.78 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=3558806.5 spike=0.06
- MFPC.CA: score=23.26 buy_ready=False sector_rank=13 price=39.6 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=13992927.0 spike=0.17
- MFSC.CA: score=8.53 buy_ready=False sector_rank=14 price=50.3 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=26.1 liquidity=2691367.0 spike=0.23
- MHOT.CA: score=10.26 buy_ready=False sector_rank=15 price=18.47 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=61.01 liquidity=1652459.88 spike=0.1
- MICH.CA: score=18.73 buy_ready=False sector_rank=14 price=50.11 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=70.61 liquidity=7890411.5 spike=0.19
- MILS.CA: score=22.84 buy_ready=False sector_rank=14 price=222.01 support=165.55 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=57.01 liquidity=33668784.0 spike=0.38
- MIPH.CA: score=12.06 buy_ready=False sector_rank=10 price=784.97 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=54.24 liquidity=658180.0 spike=0.16
- MOED.CA: score=19.84 buy_ready=False sector_rank=14 price=0.8 support=0.65 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=92.27 liquidity=70921992.0 spike=0.95
- MOIL.CA: score=9.39 buy_ready=False sector_rank=12 price=0.67 support=0.58 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=40.7 liquidity=109669.41 spike=0.18
- MOIN.CA: score=14.19 buy_ready=False sector_rank=14 price=34.98 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=70.36 liquidity=3358433.5 spike=0.11
- MOSC.CA: score=9.42 buy_ready=False sector_rank=14 price=332.53 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=77.74 liquidity=1581941.5 spike=0.11
- MPCI.CA: score=20.84 buy_ready=False sector_rank=14 price=391.95 support=278.02 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=70.23 liquidity=62051092.0 spike=0.38
- MPCO.CA: score=21.4 buy_ready=False sector_rank=9 price=2.25 support=1.83 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=67.61 liquidity=29810438.0 spike=0.25
- MPRC.CA: score=11.5 buy_ready=False sector_rank=14 price=42.74 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=42.49 liquidity=2666402.0 spike=0.1
- MTIE.CA: score=7.4 buy_ready=False sector_rank=21 price=8.4 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=34.76 liquidity=15093028.0 spike=0.28
- NAHO.CA: score=9.41 buy_ready=False sector_rank=14 price=0.15 support=0.1 resistance=0.16 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=92.16 liquidity=138298.35 spike=1.72
- NCCW.CA: score=9.07 buy_ready=False sector_rank=14 price=5.94 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=3230736.25 spike=0.1
- NEDA.CA: score=13.37 buy_ready=False sector_rank=14 price=2.76 support=2.7 resistance=2.97 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=50.94 liquidity=1551804.47 spike=1.99
- NHPS.CA: score=20.26 buy_ready=False sector_rank=14 price=90.98 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=61.02 liquidity=9419250.0 spike=0.21
- NINH.CA: score=10.18 buy_ready=False sector_rank=14 price=22.31 support=21.22 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=21.27 liquidity=6347175.5 spike=0.17
- NIPH.CA: score=6.4 buy_ready=False sector_rank=10 price=365.22 support=335.0 resistance=365.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:58 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=152513104.0 spike=0.5
- OBRI.CA: score=10.47 buy_ready=False sector_rank=14 price=32.89 support=31.61 resistance=35.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=3635804.5 spike=0.11
- OCDI.CA: score=20.33 buy_ready=False sector_rank=16 price=33.57 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=63.99 liquidity=10432413.0 spike=0.08
- OCPH.CA: score=4.59 buy_ready=False sector_rank=14 price=266.77 support=242.0 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8754334.0 spike=0.35
- ODIN.CA: score=20.36 buy_ready=False sector_rank=14 price=3.18 support=2.54 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=58.12 liquidity=7528326.5 spike=0.18
- OFH.CA: score=19.84 buy_ready=False sector_rank=14 price=0.93 support=0.69 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=86.77 liquidity=29092254.0 spike=0.38
- OIH.CA: score=20.4 buy_ready=False sector_rank=6 price=1.89 support=1.43 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=88.68 liquidity=13788910.0 spike=0.1
- OLFI.CA: score=9.87 buy_ready=False sector_rank=17 price=23.98 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=55.84 liquidity=1745462.5 spike=0.03
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=785.01 support=764.01 resistance=786.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50237188.0 spike=1.0
- ORHD.CA: score=20.33 buy_ready=False sector_rank=16 price=41.46 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=61.0 liquidity=14820283.0 spike=0.09
- ORWE.CA: score=12.49 buy_ready=False sector_rank=8 price=25.67 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=72.2 liquidity=3085463.75 spike=0.04
- PHAR.CA: score=21.4 buy_ready=False sector_rank=10 price=137.45 support=90.01 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=141006480.0 spike=0.32
- PHDC.CA: score=20.33 buy_ready=False sector_rank=16 price=15.2 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=64.14 liquidity=10621389.0 spike=0.04
- PHTV.CA: score=9.54 buy_ready=False sector_rank=14 price=375.0 support=310.0 resistance=447.99 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=65.28 liquidity=704250.0 spike=0.29
- POUL.CA: score=8.01 buy_ready=False sector_rank=17 price=37.52 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:01 AM market time freshness=DELAYED_CURRENT RSI=45.82 liquidity=2883645.75 spike=0.11
- PRCL.CA: score=9.54 buy_ready=False sector_rank=4 price=33.38 support=32.0 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:57 AM market time freshness=DELAYED_CURRENT RSI=33.61 liquidity=5140850.0 spike=0.16
- PRDC.CA: score=20.33 buy_ready=False sector_rank=16 price=9.34 support=8.7 resistance=9.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=37.64 liquidity=21711836.0 spike=0.3
- PRMH.CA: score=7.35 buy_ready=False sector_rank=14 price=2.43 support=2.36 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=1513955.88 spike=0.13
- RACC.CA: score=13.02 buy_ready=False sector_rank=14 price=9.95 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=7188433.5 spike=0.36
- RAKT.CA: score=0.86 buy_ready=False sector_rank=14 price=22.25 support=21.65 resistance=24.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=22.55 liquidity=366924.75 spike=1.33
- RAYA.CA: score=8.17 buy_ready=False sector_rank=20 price=7.19 support=6.95 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=19.32 liquidity=15782229.0 spike=0.19
- RMDA.CA: score=21.4 buy_ready=False sector_rank=10 price=6.37 support=4.98 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=11202687.0 spike=0.09
- ROTO.CA: score=18.68 buy_ready=False sector_rank=14 price=46.0 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=55.44 liquidity=9847459.0 spike=0.41
- RREI.CA: score=20.84 buy_ready=False sector_rank=14 price=4.57 support=3.76 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=45.4 liquidity=39023484.0 spike=0.58
- RTVC.CA: score=12.18 buy_ready=False sector_rank=14 price=4.14 support=3.73 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=2342430.5 spike=0.3
- RUBX.CA: score=11.45 buy_ready=False sector_rank=14 price=12.54 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=2611383.5 spike=0.13
- SAUD.CA: score=15.57 buy_ready=False sector_rank=7 price=24.39 support=21.4 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=88.45 liquidity=5171401.5 spike=0.23
- SCEM.CA: score=21.4 buy_ready=False sector_rank=4 price=98.64 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=70.54 liquidity=30635682.0 spike=0.15
- SCFM.CA: score=12.81 buy_ready=False sector_rank=14 price=284.02 support=270.51 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=43.62 liquidity=1971510.38 spike=0.07
- SCTS.CA: score=16.08 buy_ready=False sector_rank=2 price=618.21 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:00 AM market time freshness=DELAYED_CURRENT RSI=61.7 liquidity=683054.31 spike=0.07
- SDTI.CA: score=12.42 buy_ready=False sector_rank=14 price=69.0 support=50.3 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:51 AM market time freshness=DELAYED_CURRENT RSI=60.97 liquidity=1582788.75 spike=0.05
- SEIG.CA: score=10.02 buy_ready=False sector_rank=14 price=263.41 support=242.1 resistance=295.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=55.69 liquidity=1180867.05 spike=0.13
- SIPC.CA: score=5.84 buy_ready=False sector_rank=14 price=5.09 support=4.8 resistance=5.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25384664.0 spike=0.41
- SKPC.CA: score=20.26 buy_ready=False sector_rank=13 price=17.92 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=84.15 liquidity=20612610.0 spike=0.3
- SMFR.CA: score=13.92 buy_ready=False sector_rank=14 price=263.42 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=64.94 liquidity=3081605.75 spike=0.11
- SNFC.CA: score=9.03 buy_ready=False sector_rank=14 price=10.96 support=10.6 resistance=11.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:05 AM market time freshness=DELAYED_CURRENT RSI=46.62 liquidity=1194685.88 spike=0.1
- SPIN.CA: score=6.4 buy_ready=False sector_rank=8 price=20.03 support=18.31 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36104200.0 spike=0.78
- SPMD.CA: score=13.72 buy_ready=False sector_rank=14 price=0.47 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=42.47 liquidity=4880356.5 spike=0.16
- SUGR.CA: score=15.71 buy_ready=False sector_rank=17 price=51.2 support=46.47 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=72.94 liquidity=5581768.5 spike=0.26
- SVCE.CA: score=19.12 buy_ready=False sector_rank=14 price=10.46 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=65.56 liquidity=8284016.0 spike=0.08
- SWDY.CA: score=21.38 buy_ready=False sector_rank=11 price=119.97 support=91.8 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=68.64 liquidity=25160934.0 spike=0.27
- TALM.CA: score=18.47 buy_ready=False sector_rank=2 price=19.45 support=15.7 resistance=20.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=61.1 liquidity=3069872.75 spike=0.07
- TMGH.CA: score=18.33 buy_ready=False sector_rank=16 price=97.48 support=95.2 resistance=101.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=45.01 liquidity=16624159.0 spike=0.06
- TRTO.CA: score=17.16 buy_ready=False sector_rank=14 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:59 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=21931.35 spike=2.15
- UEFM.CA: score=9.4 buy_ready=False sector_rank=14 price=540.15 support=531.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:02 AM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=563492.38 spike=0.11
- UEGC.CA: score=11.69 buy_ready=False sector_rank=14 price=2.15 support=1.95 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=34.45 liquidity=7856168.0 spike=0.21
- UNIP.CA: score=18.84 buy_ready=False sector_rank=14 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=35.79 liquidity=11156493.0 spike=0.29
- UNIT.CA: score=12.91 buy_ready=False sector_rank=16 price=18.81 support=17.32 resistance=23.0 source=Yahoo Finance as_of=2026-08-19T21:00:00+00:00 freshness=FRESH RSI=55.67 liquidity=2574186.05 spike=0.23
- WCDF.CA: score=8.41 buy_ready=False sector_rank=14 price=643.89 support=555.55 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:58 AM market time freshness=DELAYED_CURRENT RSI=76.66 liquidity=575663.69 spike=0.12
- WKOL.CA: score=21.74 buy_ready=False sector_rank=14 price=348.97 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=46.35 liquidity=8899605.0 spike=0.26
- ZEOT.CA: score=13.7 buy_ready=False sector_rank=14 price=14.04 support=11.56 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=64.74 liquidity=865275.0 spike=0.03
- ZMID.CA: score=20.33 buy_ready=False sector_rank=16 price=8.01 support=7.06 resistance=8.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=71.63 liquidity=123211200.0 spike=0.5

## Backtesting Lite
- ETEL.CA: 180d return=91.34%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-08-19T21:00:00+00:00
- CCAP.CA: 180d return=42.49%, max drawdown=-23.12%, MA20>MA50 days last20=19, as_of=2026-08-19T21:00:00+00:00
- GRCA.CA: 180d return=111.6%, max drawdown=-18.71%, MA20>MA50 days last20=17, as_of=2026-08-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- GRCA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Grand Capital for Financial Investments summary=Grand Investment Capital logs lower consolidated net profits in H1-25/26; Grand Investment Capital sees EGP 8m block-trading deal; Grand Investment Capital’s profit hikes 131% in 12M
  - Grand Investment Capital logs lower consolidated net profits in H1-25/26: https://english.mubasher.info/news/4527603/Grand-Investment-Capital-logs-lower-consolidated-net-profits-in-H1-25-26/
  - Grand Investment Capital sees EGP 8m block-trading deal: https://english.mubasher.info/news/3765574/Grand-Investment-Capital-sees-EGP-8m-block-trading-deal/
  - Grand Investment Capital’s profit hikes 131% in 12M: https://english.mubasher.info/news/3481392/Grand-Investment-Capital-s-profit-hikes-131-in-12M/
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- MILS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=North Cairo Flour Mills summary=North Cairo Mills stock hits historic peak amid clear emergence of buying power; North Cairo Mills approves EGP 0.5/shr dividends for FY19/20; North Cairo Mills reports 37% profit decline in FY19/20 initial results
  - North Cairo Mills stock hits historic peak amid clear emergence of buying power: https://english.mubasher.info/news/4540088/North-Cairo-Mills-stock-hits-historic-peak-amid-clear-emergence-of-buying-power/
  - North Cairo Mills approves EGP 0.5/shr dividends for FY19/20: https://english.mubasher.info/news/3726135/North-Cairo-Mills-approves-EGP-0-5-shr-dividends-for-FY19-20/
  - North Cairo Mills reports 37% profit decline in FY19/20 initial results: https://english.mubasher.info/news/3676432/North-Cairo-Mills-reports-37-profit-decline-in-FY19-20-initial-results/
- AALR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=General Company For Land Reclamation, Development & Reconstruction summary=General Land Reclamation expects over EGP 8.6m net profits in FY26/27 estimated budget; General Land Reclamation incurs EGP 29.5m loss in FY18/19; General Land Reclamation turns to losses in 9M
  - General Land Reclamation expects over EGP 8.6m net profits in FY26/27 estimated budget: https://english.mubasher.info/news/4600324/General-Land-Reclamation-expects-over-EGP-8-6m-net-profits-in-FY26-27-estimated-budget/
  - General Land Reclamation incurs EGP 29.5m loss in FY18/19: https://english.mubasher.info/news/3525030/General-Land-Reclamation-incurs-EGP-29-5m-loss-in-FY18-19/
  - General Land Reclamation turns to losses in 9M: https://english.mubasher.info/news/3465326/General-Land-Reclamation-turns-to-losses-in-9M/

## Warnings
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for GRCA.CA matches the company but no source/report date was detected.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for MILS.CA matches the company but no source/report date was detected.
- Evidence for AALR.CA matches the company but no source/report date was detected.
