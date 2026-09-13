# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-13T10:41:06.796315+00:00
Generated Cairo: 2026-09-13 13:41
Run timing: target 08:45 Cairo | generated Cairo 2026-09-13 13:41 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-13 13:36

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 39
- Data quality issues: 1
- Tradeable price/liquidity tickers: 175/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, September 13
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 55.0% / above MA50 70.0%
- EGX70 regime: BEARISH / above MA20 41.67% / above MA50 66.67%
- Sector breadth: 38.1%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=1163377920.0 spike=1.62 score=29.64
- MPCO.CA: liquidity=380004480.0 spike=2.81 score=11.86
- MASR.CA: liquidity=224627696.0 spike=2.69 score=28.52
- AMES.CA: liquidity=216624144.0 spike=0.98 score=12.14
- COMI.CA: liquidity=187822448.0 spike=0.36 score=18.8

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner highlighted accumulation‑spike stocks with bullish‑watch outlooks while EGX30 stays constructive and EGX70 turns bearish, keeping risk mode selective.
- Top picks (CCAP, MASR, POUL, EPCO) scored high on rank_score and showed ACCUMULATION_SPIKE liquidity, suggesting near‑term institutional interest.

## Top Liquidity Spikes
- EGSA.CA: spike=106.08 liquidity=859107.49 outlook=CONSTRUCTIVE score=52 buy_ready=False
- POUL.CA: spike=3.6 liquidity=76261320.0 outlook=BULLISH_WATCH score=71.54 buy_ready=True
- EPCO.CA: spike=3.13 liquidity=63259212.0 outlook=BULLISH_WATCH score=90.86 buy_ready=True
- DTPP.CA: spike=3.08 liquidity=106918512.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MPCO.CA: spike=2.81 liquidity=380004480.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=89.84 5d=5.07% 20d=9.91% aboveMA50=100.0%
- #2 Investment Holding: score=11.94 5d=5.25% 20d=16.51% aboveMA50=100.0%
- #3 Textiles: score=8.13 5d=2.67% 20d=14.48% aboveMA50=75.0%
- #4 Fintech & Payments: score=6.4 5d=2.88% 20d=1.73% aboveMA50=100.0%
- #5 Basic Resources & Chemicals: score=5.67 5d=-1.64% 20d=6.93% aboveMA50=80.0%
- #6 Energy & Petrochemicals: score=5.15 5d=0.22% 20d=1.51% aboveMA50=75.0%
- #7 Industrial Goods & Cables: score=4.98 5d=-1.04% 20d=6.99% aboveMA50=50.0%
- #8 Banking & Financials: score=4.5 5d=0.12% 20d=2.4% aboveMA50=80.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EPCO.CA: BULLISH_WATCH score=90.86 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=88 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- CCAP.CA: BULLISH_WATCH score=87 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- EFIC.CA: BULLISH_WATCH score=81.67 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EGCH.CA: BULLISH_WATCH score=81.67 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EGAS.CA: BULLISH_WATCH score=81.15 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=80.13 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- RMDA.CA: BULLISH_WATCH score=79.12 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- FWRY.CA: BULLISH_WATCH score=76.4 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ACGC.CA: BULLISH_WATCH score=76.13 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support

## BUY-Ready Candidates
- MASR.CA: rank=28.52 outlook=BULLISH_WATCH outlook_score=70.86 sector_rank=13 price=8.39 support=7.49 resistance=8.79 liquidity=224627696.0
- POUL.CA: rank=28.42 outlook=BULLISH_WATCH outlook_score=71.54 sector_rank=10 price=40.65 support=36.97 resistance=40.99 liquidity=76261320.0
- EPCO.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=90.86 sector_rank=13 price=11.8 support=10.8 resistance=12.89 liquidity=63259212.0
- FWRY.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=76.4 sector_rank=4 price=19.14 support=18.66 resistance=19.69 liquidity=35248200.0
- EFIC.CA: rank=26.27 outlook=BULLISH_WATCH outlook_score=81.67 sector_rank=5 price=213.0 support=192.75 resistance=260.0 liquidity=42862800.0
- SKPC.CA: rank=26.27 outlook=BULLISH_WATCH outlook_score=73.67 sector_rank=5 price=18.22 support=16.55 resistance=19.36 liquidity=91127816.0
- ACGC.CA: rank=25.4 outlook=BULLISH_WATCH outlook_score=76.13 sector_rank=3 price=15.0 support=10.94 resistance=16.09 liquidity=13456273.0
- ORWE.CA: rank=25.4 outlook=BULLISH_WATCH outlook_score=80.13 sector_rank=3 price=27.6 support=24.5 resistance=29.41 liquidity=14035768.0
- COSG.CA: rank=25.14 outlook=BULLISH_WATCH outlook_score=73.86 sector_rank=13 price=1.89 support=1.73 resistance=2.0 liquidity=12999577.0
- KZPC.CA: rank=25.14 outlook=CONSTRUCTIVE outlook_score=63.86 sector_rank=13 price=14.01 support=9.63 resistance=16.74 liquidity=17558718.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.14 buy_ready=False sector_rank=13 price=308.6 support=293.0 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=35.85 liquidity=12374070.0 spike=0.34
- ABUK.CA: score=21.27 buy_ready=False sector_rank=5 price=90.01 support=75.01 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=76.57 liquidity=45657292.0 spike=0.27
- ACAMD.CA: score=22.14 buy_ready=False sector_rank=13 price=2.14 support=1.95 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=34312452.0 spike=0.61
- ACGC.CA: score=25.4 buy_ready=True sector_rank=3 price=15.0 support=10.94 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=69.89 liquidity=13456273.0 spike=0.32
- ADCI.CA: score=12.81 buy_ready=False sector_rank=13 price=289.85 support=280.0 resistance=326.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=1668855.5 spike=0.16
- ADIB.CA: score=21.8 buy_ready=False sector_rank=8 price=52.14 support=51.15 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=44.4 liquidity=19311980.0 spike=0.27
- ADPC.CA: score=18.14 buy_ready=False sector_rank=13 price=3.88 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=10191721.0 spike=0.35
- AFDI.CA: score=6.62 buy_ready=False sector_rank=13 price=53.33 support=53.54 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=29.38 liquidity=3473530.25 spike=0.12
- AFMC.CA: score=16.48 buy_ready=False sector_rank=13 price=164.15 support=157.0 resistance=267.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=20.72 liquidity=88704112.0 spike=1.17
- AJWA.CA: score=13.14 buy_ready=False sector_rank=13 price=179.94 support=175.15 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=27.11 liquidity=12837028.0 spike=0.23
- ALCN.CA: score=23.09 buy_ready=False sector_rank=14 price=31.3 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=18056534.0 spike=0.59
- ALUM.CA: score=12.96 buy_ready=False sector_rank=13 price=27.74 support=26.5 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=57.29 liquidity=1818810.88 spike=0.07
- AMER.CA: score=20.94 buy_ready=False sector_rank=15 price=5.2 support=5.19 resistance=7.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=22917290.0 spike=0.29
- AMES.CA: score=12.14 buy_ready=False sector_rank=13 price=58.02 support=58.52 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=3.47 liquidity=216624144.0 spike=0.98
- AMIA.CA: score=16.26 buy_ready=True sector_rank=13 price=18.77 support=12.62 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=5120375.5 spike=0.07
- AMOC.CA: score=24.06 buy_ready=False sector_rank=6 price=13.7 support=9.59 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=73.78 liquidity=105514960.0 spike=0.55
- APSW.CA: score=7.57 buy_ready=False sector_rank=13 price=8.6 support=8.41 resistance=9.39 source=Yahoo Finance as_of=2026-09-09T21:00:00+00:00 freshness=FRESH RSI=39.78 liquidity=426783.62 spike=0.37
- ARAB.CA: score=18.94 buy_ready=False sector_rank=15 price=0.25 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=68.33 liquidity=29261112.0 spike=0.3
- ARCC.CA: score=17.22 buy_ready=True sector_rank=9 price=75.68 support=71.51 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=61.82 liquidity=3613518.5 spike=0.04
- AREH.CA: score=20.18 buy_ready=False sector_rank=13 price=1.47 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=18285540.0 spike=1.02
- ARVA.CA: score=8.14 buy_ready=False sector_rank=13 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=20.26 buy_ready=False sector_rank=13 price=63.04 support=62.01 resistance=67.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=9118372.0 spike=0.31
- ASPI.CA: score=16.14 buy_ready=False sector_rank=13 price=0.43 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=17787508.0 spike=0.33
- ATLC.CA: score=22.7 buy_ready=False sector_rank=16 price=7.48 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=72.79 liquidity=16597765.0 spike=0.55
- ATQA.CA: score=23.27 buy_ready=False sector_rank=5 price=13.0 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=83.77 liquidity=30567642.0 spike=0.25
- AXPH.CA: score=10.38 buy_ready=False sector_rank=13 price=1668.4 support=1301.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=82.0 liquidity=2233247.0 spike=0.18
- BINV.CA: score=20.41 buy_ready=True sector_rank=2 price=51.78 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=66.11 liquidity=4005103.25 spike=0.36
- BIOC.CA: score=16.14 buy_ready=False sector_rank=13 price=292.45 support=285.0 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=26229656.0 spike=0.15
- BTFH.CA: score=16.7 buy_ready=False sector_rank=16 price=2.92 support=2.94 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=46100372.0 spike=0.41
- CAED.CA: score=16.14 buy_ready=False sector_rank=13 price=128.7 support=123.56 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=17.94 liquidity=11650545.0 spike=0.3
- CANA.CA: score=21.8 buy_ready=False sector_rank=8 price=42.4 support=40.45 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=60.46 liquidity=15364079.0 spike=0.88
- CCAP.CA: score=29.64 buy_ready=False sector_rank=2 price=6.28 support=5.28 resistance=6.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=72.59 liquidity=1163377920.0 spike=1.62
- CCRS.CA: score=17.03 buy_ready=False sector_rank=13 price=2.56 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=5886489.5 spike=0.12
- CEFM.CA: score=14.08 buy_ready=False sector_rank=13 price=148.48 support=133.0 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=34.41 liquidity=5933834.5 spike=0.38
- CERA.CA: score=10.08 buy_ready=False sector_rank=13 price=1.56 support=1.56 resistance=1.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=119193048.0 spike=1.97
- CFGH.CA: score=13.15 buy_ready=False sector_rank=13 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-09-09T21:00:00+00:00 freshness=FRESH RSI=65.0 liquidity=9992.48 spike=0.4
- CICH.CA: score=15.93 buy_ready=True sector_rank=16 price=12.84 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=67.89 liquidity=3229774.5 spike=0.68
- CIEB.CA: score=19.23 buy_ready=True sector_rank=8 price=25.22 support=24.0 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=61.14 liquidity=3430546.0 spike=0.23
- CIRA.CA: score=7.91 buy_ready=False sector_rank=17 price=38.91 support=36.8 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37155360.0 spike=1.12
- CLHO.CA: score=13.25 buy_ready=False sector_rank=11 price=16.27 support=16.0 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=34.44 liquidity=25183252.0 spike=0.31
- CNFN.CA: score=9.07 buy_ready=False sector_rank=16 price=4.73 support=4.73 resistance=4.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=1377032.38 spike=0.09
- COMI.CA: score=18.8 buy_ready=False sector_rank=8 price=136.53 support=135.35 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=53.0 liquidity=187822448.0 spike=0.36
- COPR.CA: score=21.14 buy_ready=False sector_rank=13 price=0.48 support=0.42 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=37.42 liquidity=15197272.0 spike=0.16
- COSG.CA: score=25.14 buy_ready=True sector_rank=13 price=1.89 support=1.73 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=12999577.0 spike=0.23
- CPCI.CA: score=11.94 buy_ready=False sector_rank=13 price=536.8 support=520.0 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=54.08 liquidity=800525.38 spike=0.13
- CSAG.CA: score=17.77 buy_ready=False sector_rank=14 price=39.53 support=38.13 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=47.87 liquidity=6682677.5 spike=0.33
- DAPH.CA: score=21.14 buy_ready=False sector_rank=13 price=125.17 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=59.04 liquidity=10226579.0 spike=0.14
- DEIN.CA: score=11.14 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=18.7 buy_ready=True sector_rank=10 price=28.64 support=27.79 resistance=30.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=48.31 liquidity=5285074.0 spike=0.63
- DSCW.CA: score=15.71 buy_ready=False sector_rank=13 price=1.88 support=1.84 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=7569593.5 spike=0.13
- DTPP.CA: score=12.3 buy_ready=False sector_rank=13 price=340.68 support=298.0 resistance=347.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106918512.0 spike=3.08
- EALR.CA: score=7.95 buy_ready=False sector_rank=13 price=377.96 support=340.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=34.04 liquidity=4803355.5 spike=0.15
- EASB.CA: score=10.36 buy_ready=False sector_rank=13 price=9.32 support=8.63 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29908946.0 spike=2.11
- EAST.CA: score=15.05 buy_ready=False sector_rank=10 price=34.55 support=34.6 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=37.99 liquidity=7636969.0 spike=0.11
- EBSC.CA: score=20.24 buy_ready=True sector_rank=13 price=2.09 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=61.82 liquidity=5094823.5 spike=0.35
- ECAP.CA: score=6.69 buy_ready=False sector_rank=13 price=33.06 support=31.16 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=32.51 liquidity=3541780.75 spike=0.2
- EDFM.CA: score=14.45 buy_ready=True sector_rank=13 price=421.72 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=1309156.38 spike=0.68
- EEII.CA: score=8.57 buy_ready=False sector_rank=13 price=2.31 support=2.33 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=18.22 liquidity=5428411.5 spike=0.18
- EFIC.CA: score=26.27 buy_ready=True sector_rank=5 price=213.0 support=192.75 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=50.18 liquidity=42862800.0 spike=0.46
- EFID.CA: score=21.42 buy_ready=False sector_rank=10 price=31.09 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=42.89 liquidity=20155220.0 spike=0.36
- EFIH.CA: score=22.4 buy_ready=False sector_rank=4 price=23.44 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=23943908.0 spike=0.28
- EGAL.CA: score=21.27 buy_ready=False sector_rank=5 price=371.95 support=321.01 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=76.39 liquidity=19125248.0 spike=0.11
- EGAS.CA: score=17.33 buy_ready=True sector_rank=6 price=58.45 support=55.21 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=58.41 liquidity=3272264.0 spike=0.27
- EGBE.CA: score=6.83 buy_ready=False sector_rank=8 price=0.51 support=0.51 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=16.67 liquidity=27083.19 spike=0.16
- EGCH.CA: score=24.27 buy_ready=True sector_rank=5 price=14.07 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=52.96 liquidity=96664376.0 spike=0.74
- EGSA.CA: score=22.26 buy_ready=False sector_rank=1 price=9.07 support=8.65 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 01:06 PM market time freshness=DELAYED_CURRENT RSI=93.18 liquidity=859107.49 spike=106.08
- EGTS.CA: score=20.44 buy_ready=False sector_rank=15 price=17.22 support=16.17 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=61.59 liquidity=39842464.0 spike=1.25
- EHDR.CA: score=15.92 buy_ready=False sector_rank=13 price=2.93 support=2.81 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=47.92 liquidity=4774432.5 spike=0.15
- EKHO.CA: score=10.06 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.01 buy_ready=False sector_rank=7 price=2.05 support=2.04 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=65723488.0 spike=1.01
- ELKA.CA: score=18.14 buy_ready=False sector_rank=13 price=1.74 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=11812078.0 spike=0.22
- ELNA.CA: score=9.9 buy_ready=False sector_rank=13 price=35.74 support=35.17 resistance=38.99 source=Yahoo Finance as_of=2026-09-09T21:00:00+00:00 freshness=FRESH RSI=37.63 liquidity=892499.32 spike=1.93
- ELSH.CA: score=20.14 buy_ready=False sector_rank=13 price=13.41 support=12.97 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=28094130.0 spike=0.67
- ELWA.CA: score=12.79 buy_ready=False sector_rank=13 price=1.8 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=2567757.75 spike=1.04
- EMFD.CA: score=21.94 buy_ready=False sector_rank=15 price=14.8 support=11.51 resistance=15.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=93.04 liquidity=141242640.0 spike=0.91
- ENGC.CA: score=12.12 buy_ready=False sector_rank=13 price=43.72 support=41.8 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=47.2 liquidity=3973507.5 spike=0.2
- EOSB.CA: score=15.18 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=32211.69 spike=0.55
- EPCO.CA: score=27.4 buy_ready=True sector_rank=13 price=11.8 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=63259212.0 spike=3.13
- EPPK.CA: score=-1.44 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=24.4 buy_ready=False sector_rank=1 price=126.18 support=109.5 resistance=131.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=77.01 liquidity=68156080.0 spike=0.36
- ETRS.CA: score=17.24 buy_ready=False sector_rank=13 price=11.05 support=10.7 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=59.06 liquidity=6094418.5 spike=0.25
- EXPA.CA: score=23.8 buy_ready=True sector_rank=8 price=21.25 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=17546428.0 spike=0.47
- FAIT.CA: score=12.77 buy_ready=False sector_rank=8 price=47.11 support=39.1 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=81.94 liquidity=1973601.25 spike=0.22
- FAITA.CA: score=9.63 buy_ready=False sector_rank=8 price=0.98 support=0.98 resistance=1.02 source=Yahoo Finance as_of=2026-09-09T21:00:00+00:00 freshness=FRESH RSI=46.51 liquidity=72261.03 spike=1.38
- FERC.CA: score=18.57 buy_ready=False sector_rank=5 price=78.19 support=76.7 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=5302787.5 spike=0.24
- FWRY.CA: score=26.4 buy_ready=True sector_rank=4 price=19.14 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=49.66 liquidity=35248200.0 spike=0.25
- GBCO.CA: score=21.15 buy_ready=False sector_rank=20 price=30.34 support=27.51 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=57.05 liquidity=12026411.0 spike=0.23
- GDWA.CA: score=17.14 buy_ready=False sector_rank=13 price=0.79 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=50.32 liquidity=17837372.0 spike=0.41
- GGCC.CA: score=21.14 buy_ready=False sector_rank=13 price=0.91 support=0.83 resistance=1.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=41.8 liquidity=25902348.0 spike=0.56
- GIHD.CA: score=22.14 buy_ready=False sector_rank=13 price=75.0 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=85.13 liquidity=26409146.0 spike=0.82
- GMCI.CA: score=8.5 buy_ready=False sector_rank=13 price=1.88 support=1.83 resistance=1.97 source=Yahoo Finance as_of=2026-09-09T21:00:00+00:00 freshness=FRESH RSI=41.18 liquidity=359632.72 spike=0.84
- GRCA.CA: score=8.14 buy_ready=False sector_rank=13 price=49.0 support=48.75 resistance=56.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36314900.0 spike=0.49
- GSSC.CA: score=16.54 buy_ready=True sector_rank=13 price=292.54 support=278.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=63.65 liquidity=1393506.38 spike=0.1
- GTWL.CA: score=20.14 buy_ready=False sector_rank=13 price=239.69 support=125.1 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=75.21 liquidity=62872920.0 spike=0.2
- HDBK.CA: score=22.39 buy_ready=True sector_rank=8 price=109.27 support=85.9 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=69.64 liquidity=8594748.0 spike=0.15
- HELI.CA: score=24.94 buy_ready=True sector_rank=15 price=8.0 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=58.76 liquidity=58278264.0 spike=0.37
- HRHO.CA: score=18.7 buy_ready=False sector_rank=16 price=25.71 support=25.33 resistance=27.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=44.92 liquidity=21919996.0 spike=0.21
- ICID.CA: score=21.36 buy_ready=False sector_rank=13 price=18.62 support=10.6 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=70.09 liquidity=8213873.5 spike=0.27
- IDRE.CA: score=13.89 buy_ready=False sector_rank=13 price=53.89 support=51.02 resistance=57.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=59.35 liquidity=2744784.25 spike=0.24
- IFAP.CA: score=15.99 buy_ready=False sector_rank=12 price=20.67 support=20.2 resistance=22.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=55.52 liquidity=4749854.5 spike=0.18
- INFI.CA: score=9.67 buy_ready=False sector_rank=13 price=146.0 support=140.66 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=31.13 liquidity=3530950.75 spike=0.07
- IRON.CA: score=10.04 buy_ready=False sector_rank=5 price=28.12 support=27.84 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=6.08 liquidity=6771317.0 spike=0.48
- ISMA.CA: score=18.34 buy_ready=False sector_rank=13 price=31.68 support=29.0 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=37.52 liquidity=32994462.0 spike=1.1
- ISMQ.CA: score=18.26 buy_ready=False sector_rank=5 price=9.12 support=9.0 resistance=9.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=49.54 liquidity=8987665.0 spike=0.22
- ISPH.CA: score=21.25 buy_ready=False sector_rank=11 price=12.83 support=12.75 resistance=13.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=41707984.0 spike=0.44
- JUFO.CA: score=16.04 buy_ready=False sector_rank=10 price=27.08 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=58.99 liquidity=6628545.5 spike=0.23
- KABO.CA: score=12.28 buy_ready=False sector_rank=3 price=9.98 support=9.52 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93582456.0 spike=1.94
- KWIN.CA: score=18.14 buy_ready=False sector_rank=13 price=90.03 support=84.08 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=41.53 liquidity=16884660.0 spike=0.25
- KZPC.CA: score=25.14 buy_ready=True sector_rank=13 price=14.01 support=9.63 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=45.43 liquidity=17558718.0 spike=0.27
- LCSW.CA: score=15.32 buy_ready=False sector_rank=9 price=34.26 support=32.12 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=3720290.5 spike=0.11
- LUTS.CA: score=16.14 buy_ready=False sector_rank=13 price=0.97 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=30.1 liquidity=99770944.0 spike=0.36
- MAAL.CA: score=13.48 buy_ready=False sector_rank=13 price=8.86 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=55.45 liquidity=2337396.5 spike=0.17
- MASR.CA: score=28.52 buy_ready=True sector_rank=13 price=8.39 support=7.49 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=224627696.0 spike=2.69
- MBSC.CA: score=23.03 buy_ready=True sector_rank=9 price=409.4 support=340.0 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=61.64 liquidity=9427934.0 spike=0.09
- MCQE.CA: score=21.6 buy_ready=False sector_rank=9 price=224.81 support=212.01 resistance=279.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=18172544.0 spike=0.3
- MCRO.CA: score=23.14 buy_ready=True sector_rank=13 price=1.69 support=1.44 resistance=1.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=69.05 liquidity=92288624.0 spike=0.79
- MENA.CA: score=9.57 buy_ready=False sector_rank=15 price=6.69 support=6.58 resistance=7.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=1636202.5 spike=0.28
- MEPA.CA: score=25.14 buy_ready=True sector_rank=13 price=2.07 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=26961088.0 spike=0.75
- MFPC.CA: score=21.27 buy_ready=False sector_rank=5 price=46.99 support=38.3 resistance=48.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=88.62 liquidity=42418888.0 spike=0.31
- MFSC.CA: score=14.32 buy_ready=True sector_rank=13 price=50.41 support=48.88 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=57.66 liquidity=1176268.38 spike=0.19
- MHOT.CA: score=21.61 buy_ready=False sector_rank=18 price=18.35 support=17.72 resistance=19.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=43.13 liquidity=16730214.0 spike=0.9
- MICH.CA: score=17.7 buy_ready=True sector_rank=13 price=50.0 support=47.11 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=4560191.5 spike=0.16
- MILS.CA: score=16.14 buy_ready=False sector_rank=13 price=204.5 support=188.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=26574134.0 spike=0.43
- MIPH.CA: score=15.73 buy_ready=True sector_rank=11 price=792.46 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=59.31 liquidity=2479790.75 spike=0.59
- MOED.CA: score=22.14 buy_ready=True sector_rank=13 price=0.8 support=0.68 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=19431844.0 spike=0.17
- MOIL.CA: score=14.08 buy_ready=False sector_rank=6 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=15499.77 spike=0.07
- MOIN.CA: score=8.14 buy_ready=False sector_rank=13 price=37.0 support=36.76 resistance=39.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20220030.0 spike=0.69
- MOSC.CA: score=7.26 buy_ready=False sector_rank=13 price=306.79 support=300.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=32.25 liquidity=1111221.0 spike=0.09
- MPCI.CA: score=21.14 buy_ready=True sector_rank=13 price=421.22 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=67.23 liquidity=130504440.0 spike=0.73
- MPCO.CA: score=11.86 buy_ready=False sector_rank=12 price=2.77 support=2.56 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=380004480.0 spike=2.81
- MPRC.CA: score=18.14 buy_ready=False sector_rank=13 price=40.36 support=38.6 resistance=48.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=34220072.0 spike=0.79
- MTIE.CA: score=19.15 buy_ready=False sector_rank=20 price=8.46 support=8.25 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=54.93 liquidity=15483410.0 spike=0.28
- NAHO.CA: score=6.16 buy_ready=False sector_rank=13 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=13278.96 spike=0.12
- NCCW.CA: score=11.5 buy_ready=False sector_rank=13 price=8.0 support=7.75 resistance=8.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=117991008.0 spike=2.68
- NEDA.CA: score=11.1 buy_ready=False sector_rank=13 price=2.73 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=959981.88 spike=1.0
- NHPS.CA: score=9.39 buy_ready=False sector_rank=13 price=81.25 support=81.57 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=30.3 liquidity=6249459.0 spike=0.21
- NINH.CA: score=16.69 buy_ready=False sector_rank=13 price=22.33 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=55.42 liquidity=5545053.0 spike=0.18
- NIPH.CA: score=21.25 buy_ready=False sector_rank=11 price=334.48 support=326.51 resistance=444.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=51.93 liquidity=45140396.0 spike=0.16
- OBRI.CA: score=13.83 buy_ready=False sector_rank=13 price=32.21 support=31.81 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=53.1 liquidity=4686901.0 spike=0.2
- OCDI.CA: score=20.94 buy_ready=False sector_rank=15 price=32.3 support=30.03 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=49.94 liquidity=18749008.0 spike=0.17
- OCPH.CA: score=10.47 buy_ready=False sector_rank=13 price=250.38 support=242.0 resistance=308.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=52.43 liquidity=1325252.13 spike=0.08
- ODIN.CA: score=7.21 buy_ready=False sector_rank=13 price=2.79 support=2.55 resistance=3.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=27.38 liquidity=4065851.75 spike=0.09
- OFH.CA: score=21.14 buy_ready=True sector_rank=13 price=1.09 support=0.86 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=30802050.0 spike=0.27
- OIH.CA: score=28.4 buy_ready=False sector_rank=2 price=2.12 support=1.71 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=71.67 liquidity=37824464.0 spike=0.26
- OLFI.CA: score=12.66 buy_ready=False sector_rank=10 price=22.87 support=22.07 resistance=25.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=36.99 liquidity=4242026.0 spike=0.09
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=850.03 support=844.0 resistance=857.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34924912.0 spike=1.0
- ORHD.CA: score=23.4 buy_ready=True sector_rank=15 price=43.25 support=40.28 resistance=43.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=66.18 liquidity=160303072.0 spike=1.23
- ORWE.CA: score=25.4 buy_ready=True sector_rank=3 price=27.6 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=66.99 liquidity=14035768.0 spike=0.23
- PHAR.CA: score=21.25 buy_ready=False sector_rank=11 price=125.85 support=124.5 resistance=155.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=41.06 liquidity=26966654.0 spike=0.1
- PHDC.CA: score=17.94 buy_ready=False sector_rank=15 price=13.99 support=14.4 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=36.43 liquidity=137011280.0 spike=0.64
- PHTV.CA: score=12.87 buy_ready=False sector_rank=13 price=350.06 support=311.27 resistance=413.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=35.41 liquidity=1723467.38 spike=0.76
- POUL.CA: score=28.42 buy_ready=True sector_rank=10 price=40.65 support=36.97 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=67.58 liquidity=76261320.0 spike=3.6
- PRCL.CA: score=18.6 buy_ready=False sector_rank=9 price=32.34 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=47.8 liquidity=11154921.0 spike=0.51
- PRDC.CA: score=17.94 buy_ready=False sector_rank=15 price=8.12 support=8.1 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=40.11 liquidity=14833746.0 spike=0.22
- PRMH.CA: score=16.04 buy_ready=False sector_rank=13 price=2.68 support=2.28 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=74.32 liquidity=2899590.75 spike=0.21
- RACC.CA: score=18.02 buy_ready=False sector_rank=13 price=9.69 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=46.73 liquidity=7872268.0 spike=0.32
- RAKT.CA: score=9.72 buy_ready=False sector_rank=13 price=22.15 support=21.4 resistance=23.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=65.31 liquidity=334070.66 spike=1.12
- RAYA.CA: score=19.14 buy_ready=False sector_rank=21 price=7.14 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=55.78 liquidity=14497366.0 spike=0.22
- RMDA.CA: score=23.51 buy_ready=True sector_rank=11 price=6.4 support=5.77 resistance=6.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=52.86 liquidity=78427840.0 spike=1.13
- ROTO.CA: score=5.99 buy_ready=False sector_rank=13 price=42.56 support=42.6 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=17.03 liquidity=2841425.0 spike=0.17
- RREI.CA: score=21.14 buy_ready=False sector_rank=13 price=4.41 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=40.79 liquidity=18181058.0 spike=0.57
- RTVC.CA: score=16.59 buy_ready=True sector_rank=13 price=4.09 support=3.76 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=37.8 liquidity=3448525.75 spike=0.46
- RUBX.CA: score=18.97 buy_ready=True sector_rank=13 price=12.9 support=12.36 resistance=13.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=57.05 liquidity=3827949.25 spike=0.18
- SAUD.CA: score=13.94 buy_ready=False sector_rank=8 price=23.33 support=22.85 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:17 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=2140703.25 spike=0.12
- SCEM.CA: score=21.6 buy_ready=False sector_rank=9 price=98.15 support=91.19 resistance=112.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=50.59 liquidity=137998256.0 spike=0.64
- SCFM.CA: score=15.6 buy_ready=False sector_rank=13 price=278.36 support=270.55 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=39.51 liquidity=4455559.0 spike=0.36
- SCTS.CA: score=10.4 buy_ready=False sector_rank=17 price=611.21 support=610.0 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=2727850.25 spike=0.52
- SDTI.CA: score=17.87 buy_ready=True sector_rank=13 price=71.75 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=4725420.5 spike=0.23
- SEIG.CA: score=8.73 buy_ready=False sector_rank=13 price=251.27 support=252.1 resistance=291.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=590083.38 spike=0.23
- SIPC.CA: score=11.42 buy_ready=False sector_rank=13 price=6.22 support=5.91 resistance=6.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=144241520.0 spike=2.64
- SKPC.CA: score=26.27 buy_ready=True sector_rank=5 price=18.22 support=16.55 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=91127816.0 spike=0.68
- SMFR.CA: score=13.4 buy_ready=False sector_rank=13 price=249.22 support=246.0 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=36.09 liquidity=2260716.5 spike=0.14
- SNFC.CA: score=15.67 buy_ready=False sector_rank=13 price=10.82 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=3530377.5 spike=0.25
- SPIN.CA: score=17.86 buy_ready=False sector_rank=3 price=18.49 support=15.38 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=54.65 liquidity=4456792.5 spike=0.12
- SPMD.CA: score=12.76 buy_ready=False sector_rank=13 price=0.44 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=4619217.5 spike=0.39
- SUGR.CA: score=25.42 buy_ready=False sector_rank=10 price=63.93 support=49.3 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=73.38 liquidity=40199920.0 spike=0.57
- SVCE.CA: score=20.14 buy_ready=False sector_rank=13 price=12.35 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=75.32 liquidity=76947064.0 spike=0.36
- SWDY.CA: score=21.99 buy_ready=True sector_rank=7 price=128.02 support=106.8 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=67.43 liquidity=31105040.0 spike=0.32
- TALM.CA: score=9.95 buy_ready=False sector_rank=17 price=19.0 support=17.61 resistance=19.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53222460.0 spike=2.14
- TMGH.CA: score=21.94 buy_ready=False sector_rank=15 price=98.03 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=55.97 liquidity=123866328.0 spike=0.44
- TRTO.CA: score=13.17 buy_ready=False sector_rank=13 price=0.07 support=0.04 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=69.81 liquidity=25441.33 spike=0.8
- UEFM.CA: score=17.17 buy_ready=False sector_rank=13 price=530.0 support=440.66 resistance=588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=43.37 liquidity=7461154.5 spike=1.78
- UEGC.CA: score=12.8 buy_ready=False sector_rank=13 price=1.75 support=1.66 resistance=2.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=29.76 liquidity=9657312.0 spike=0.21
- UNIP.CA: score=20.14 buy_ready=False sector_rank=13 price=0.38 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=21375196.0 spike=0.6
- UNIT.CA: score=11.5 buy_ready=False sector_rank=15 price=18.43 support=18.11 resistance=20.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=561389.5 spike=0.06
- WCDF.CA: score=16.04 buy_ready=False sector_rank=13 price=707.45 support=625.0 resistance=729.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=80.7 liquidity=3895025.0 spike=0.98
- WKOL.CA: score=21.03 buy_ready=False sector_rank=13 price=340.01 support=321.9 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=55.68 liquidity=9881881.0 spike=0.45
- ZEOT.CA: score=12.65 buy_ready=False sector_rank=13 price=13.84 support=13.0 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=54.08 liquidity=1501387.25 spike=0.1
- ZMID.CA: score=21.94 buy_ready=False sector_rank=15 price=9.6 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=79.88 liquidity=60784608.0 spike=0.24

## Backtesting Lite
- CCAP.CA: 180d return=72.02%, max drawdown=-18.62%, MA20>MA50 days last20=20, as_of=2026-09-09T21:00:00+00:00
- MASR.CA: 180d return=100.01%, max drawdown=-11.03%, MA20>MA50 days last20=11, as_of=2026-09-09T21:00:00+00:00
- POUL.CA: 180d return=51.62%, max drawdown=-10.25%, MA20>MA50 days last20=9, as_of=2026-09-09T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=620 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- EPCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egypt for Poultry summary=Evidence rejected for EPCO.CA: source text did not clearly match EPCO.CA / Egypt for Poultry.
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- EFIC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=620 sources=3 expected=Egyptian Financial and Industrial summary=EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed; EFIC ordered to pay over EGP 126m as penalties; EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn
  - EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed: https://english.mubasher.info/news/4579891/EFIC-s-consolidated-profits-near-EGP-820m-in-2025-dividends-proposed/
  - EFIC ordered to pay over EGP 126m as penalties: https://english.mubasher.info/news/4535935/EFIC-ordered-to-pay-over-EGP-126m-as-penalties/
  - EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn: https://english.mubasher.info/news/4528902/EFIC-generates-lower-consolidated-net-profits-at-EGP-803m-in-9M-25-net-sales-near-EGP-8bn/
- SKPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sidi Kerir Petrochemicals summary=Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.

## Warnings
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini batch evidence failed: 500 INTERNAL. {'error': {'code': 500, 'message': 'An internal error has occurred. Please retry or report in https://developers.generativeai.google/guide/troubleshooting', 'status': 'INTERNAL'}}
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for EPCO.CA: source text did not clearly match EPCO.CA / Egypt for Poultry.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence for EFIC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
