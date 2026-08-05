# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-05T10:32:18.485655+00:00
Generated Cairo: 2026-08-05 13:32
Run timing: target 11:00 Cairo | generated Cairo 2026-08-05 13:32 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-05 13:29

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 154/189
- Top sector: Energy & Petrochemicals

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, August 05
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 70.59% / above MA50 58.82%
- EGX70 regime: BULLISH / above MA20 78.57% / above MA50 96.43%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- PHAR.CA: liquidity=555027840.0 spike=3.65 score=10.32
- ORWE.CA: liquidity=363579808.0 spike=13.22 score=11.4
- PHDC.CA: liquidity=332018976.0 spike=1.44 score=22.08
- HRHO.CA: liquidity=304127424.0 spike=3.66 score=26.4
- COMI.CA: liquidity=285716096.0 spike=0.68 score=23.12

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are both in a bullish trend, but sector breadth is only 33 % and the risk mode is DEFENSIVE_NO_NEW_BUY, so the scanner holds existing positions and highlights tickets that show accumulation spikes, bullish‑watch outlooks, and proximity to key support/resistance levels for the next 1‑3 days.
- IFAP.CA (Agriculture & Food Production) – accumulation spike, liquidity 52.5 M, trading just above 20‑day support (18.96) with a bullish‑watch outlook; sector is ranked 2nd and shows strong breadth.
- EFIH.CA (Fintech & Payments) – tradeable liquidity 88.4 M, modest liquidity spike, price near 20‑day support (21.56) and resistance (24.0), bullish‑watch outlook; sector ranks 3rd with full above‑MA20/MA50 alignment.
- HRHO.CA (Non‑bank Financial Services) – large accumulation spike, liquidity 304 M, price above 20‑day support (25.95) and below resistance (27.43), bullish‑watch outlook; sector not in leading list but shows strong insti
- ALCN.CA (Transportation & Logistics) – tradeable liquidity 35.1 M, price flirting with 20‑day resistance (30.9) after being just below support (28.27), bullish‑watch outlook; sector ranks 6th and uncertainty remains due 

## Top Liquidity Spikes
- MOIN.CA: spike=103.69 liquidity=139657680.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ORWE.CA: spike=13.22 liquidity=363579808.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DOMT.CA: spike=4.33 liquidity=17757678.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- IFAP.CA: spike=4.3 liquidity=52498280.0 outlook=BULLISH_WATCH score=100 buy_ready=False
- LUTS.CA: spike=4.11 liquidity=134715152.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Energy & Petrochemicals: score=11.6 5d=6.92% 20d=18.61% aboveMA50=75.0%
- #2 Agriculture & Food Production: score=11.52 5d=2.79% 20d=4.42% aboveMA50=100.0%
- #3 Fintech & Payments: score=9.98 5d=1.22% 20d=6.04% aboveMA50=100.0%
- #4 Telecommunications: score=8.49 5d=1.72% 20d=8.69% aboveMA50=100.0%
- #5 Building Materials: score=8.01 5d=-1.58% 20d=6.13% aboveMA50=100.0%
- #6 Transportation & Logistics: score=7.93 5d=1.44% 20d=3.7% aboveMA50=50.0%
- #7 Non-bank Financial Services: score=7.45 5d=-0.41% 20d=1.68% aboveMA50=100.0%
- #8 Automotive & Distribution: score=7.05 5d=1.93% 20d=0.48% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- IFAP.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- FWRY.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- EFIH.CA: BULLISH_WATCH score=96.98 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- MPCO.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARCC.CA: BULLISH_WATCH score=95.01 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MBSC.CA: BULLISH_WATCH score=95.01 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- HRHO.CA: BULLISH_WATCH score=94.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- EFIC.CA: BULLISH_WATCH score=87.75 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=86.98 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ALCN.CA: BULLISH_WATCH score=84.93 liquidity=TRADEABLE sector=IMPROVING risk=close to resistance

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.36 buy_ready=False sector_rank=10 price=280.49 support=206.0 resistance=317.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=68.87 liquidity=11064690.0 spike=0.29
- ABUK.CA: score=19.9 buy_ready=False sector_rank=15 price=73.87 support=69.01 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=58.4 liquidity=97928728.0 spike=0.61
- ACAMD.CA: score=19.36 buy_ready=False sector_rank=10 price=2.34 support=2.28 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=21574420.0 spike=0.3
- ACGC.CA: score=23.4 buy_ready=False sector_rank=9 price=11.09 support=9.32 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=62.78 liquidity=15226668.0 spike=0.49
- ADCI.CA: score=2.24 buy_ready=False sector_rank=10 price=275.49 support=274.0 resistance=287.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5872208.5 spike=0.34
- ADIB.CA: score=18.12 buy_ready=False sector_rank=13 price=51.89 support=46.0 resistance=53.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=79.52 liquidity=40424816.0 spike=0.29
- ADPC.CA: score=6.48 buy_ready=False sector_rank=10 price=4.15 support=4.01 resistance=4.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39051936.0 spike=1.06
- AFDI.CA: score=5.48 buy_ready=False sector_rank=10 price=60.0 support=58.15 resistance=60.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9120007.0 spike=0.43
- AFMC.CA: score=9.6 buy_ready=False sector_rank=10 price=246.59 support=201.05 resistance=249.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=273633856.0 spike=2.62
- AJWA.CA: score=23.42 buy_ready=False sector_rank=10 price=191.94 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=50.87 liquidity=33781532.0 spike=1.03
- ALCN.CA: score=26.12 buy_ready=False sector_rank=6 price=30.82 support=28.27 resistance=30.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=58.87 liquidity=35074852.0 spike=1.36
- ALUM.CA: score=10.48 buy_ready=False sector_rank=10 price=24.8 support=24.36 resistance=25.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19280942.0 spike=3.06
- AMER.CA: score=6.38 buy_ready=False sector_rank=12 price=5.9 support=5.59 resistance=6.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=128793272.0 spike=1.09
- AMES.CA: score=21.36 buy_ready=False sector_rank=10 price=121.5 support=57.5 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=93614448.0 spike=0.94
- AMIA.CA: score=12.83 buy_ready=False sector_rank=10 price=12.53 support=8.7 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=2470224.75 spike=0.15
- AMOC.CA: score=24.4 buy_ready=False sector_rank=1 price=9.17 support=7.7 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=60593996.0 spike=0.62
- APSW.CA: score=13.19 buy_ready=False sector_rank=10 price=8.86 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=57.54 liquidity=829413.63 spike=0.5
- ARAB.CA: score=19.2 buy_ready=False sector_rank=12 price=0.24 support=0.22 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=45.21 liquidity=58397312.0 spike=0.45
- ARCC.CA: score=25.5 buy_ready=False sector_rank=5 price=57.34 support=54.2 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=54.02 liquidity=61042332.0 spike=2.05
- AREH.CA: score=9.94 buy_ready=False sector_rank=10 price=1.61 support=1.57 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=82193912.0 spike=2.79
- ARVA.CA: score=8.36 buy_ready=False sector_rank=10 price=12.35 support=10.56 resistance=12.6 source=Yahoo Finance as_of=2026-08-02T21:00:00+00:00 freshness=FRESH RSI=86.22 liquidity=0.0 spike=0.0
- ASCM.CA: score=23.36 buy_ready=False sector_rank=10 price=66.57 support=57.25 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=66.26 liquidity=14444020.0 spike=0.23
- ASPI.CA: score=14.92 buy_ready=False sector_rank=10 price=0.45 support=0.31 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=79.36 liquidity=6557474.0 spike=0.16
- ATLC.CA: score=18.14 buy_ready=False sector_rank=7 price=5.23 support=5.0 resistance=5.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=6742242.0 spike=0.53
- ATQA.CA: score=22.9 buy_ready=False sector_rank=15 price=9.98 support=9.43 resistance=10.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=57.45 liquidity=32211986.0 spike=0.82
- AXPH.CA: score=11.98 buy_ready=False sector_rank=10 price=1261.33 support=1121.56 resistance=1439.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=80.3 liquidity=1614254.38 spike=0.4
- BINV.CA: score=22.99 buy_ready=False sector_rank=14 price=49.04 support=46.01 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=51.13 liquidity=14916380.0 spike=2.0
- BIOC.CA: score=20.52 buy_ready=False sector_rank=10 price=331.44 support=70.61 resistance=345.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=93.5 liquidity=112779096.0 spike=1.08
- BTFH.CA: score=23.4 buy_ready=False sector_rank=7 price=3.2 support=3.0 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=200040832.0 spike=0.85
- CAED.CA: score=17.37 buy_ready=False sector_rank=10 price=121.01 support=71.17 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=71.27 liquidity=6005181.5 spike=0.09
- CANA.CA: score=15.89 buy_ready=False sector_rank=13 price=38.52 support=35.2 resistance=39.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=68.88 liquidity=4762882.0 spike=0.25
- CCAP.CA: score=18.99 buy_ready=False sector_rank=14 price=5.26 support=5.04 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=44.63 liquidity=239444608.0 spike=0.35
- CCRS.CA: score=14.34 buy_ready=False sector_rank=10 price=2.45 support=2.3 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=7979048.5 spike=0.43
- CEFM.CA: score=21.46 buy_ready=False sector_rank=10 price=141.75 support=100.0 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=68.31 liquidity=30803560.0 spike=1.05
- CERA.CA: score=19.62 buy_ready=False sector_rank=10 price=1.33 support=1.23 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=8256301.5 spike=0.34
- CFGH.CA: score=5.38 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-08-02T21:00:00+00:00 freshness=FRESH RSI=43.75 liquidity=11783.2 spike=0.67
- CICH.CA: score=14.59 buy_ready=False sector_rank=7 price=12.89 support=11.6 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=66.27 liquidity=1194474.25 spike=0.15
- CIEB.CA: score=13.46 buy_ready=False sector_rank=13 price=24.24 support=23.75 resistance=24.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=39.75 liquidity=2334930.5 spike=0.25
- CIRA.CA: score=17.94 buy_ready=False sector_rank=19 price=35.8 support=28.2 resistance=37.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=7918418.0 spike=0.13
- CLHO.CA: score=19.32 buy_ready=False sector_rank=17 price=17.51 support=15.98 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=78.92 liquidity=21991384.0 spike=0.42
- CNFN.CA: score=22.16 buy_ready=False sector_rank=7 price=4.93 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=27568074.0 spike=1.38
- COMI.CA: score=23.12 buy_ready=False sector_rank=13 price=139.55 support=129.72 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=61.44 liquidity=285716096.0 spike=0.68
- COPR.CA: score=20.36 buy_ready=False sector_rank=10 price=0.41 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=10513284.0 spike=0.32
- COSG.CA: score=20.17 buy_ready=False sector_rank=10 price=1.69 support=1.56 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=8803850.0 spike=0.2
- CPCI.CA: score=16.05 buy_ready=False sector_rank=10 price=483.96 support=393.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=68.89 liquidity=2688113.0 spike=0.21
- CSAG.CA: score=11.32 buy_ready=False sector_rank=6 price=35.87 support=34.37 resistance=36.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55062208.0 spike=3.46
- DAPH.CA: score=22.26 buy_ready=False sector_rank=10 price=104.13 support=81.0 resistance=103.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=42961628.0 spike=1.95
- DEIN.CA: score=-3.64 buy_ready=False sector_rank=10 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=10.24 buy_ready=False sector_rank=18 price=29.59 support=28.6 resistance=30.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17757678.0 spike=4.33
- DSCW.CA: score=20.36 buy_ready=False sector_rank=10 price=2.05 support=1.74 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=79.41 liquidity=37979764.0 spike=0.53
- DTPP.CA: score=21.36 buy_ready=False sector_rank=10 price=245.8 support=193.4 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=64.84 liquidity=15702006.0 spike=0.24
- EALR.CA: score=19.05 buy_ready=False sector_rank=10 price=373.1 support=341.12 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=55.09 liquidity=5687062.5 spike=0.17
- EASB.CA: score=11.19 buy_ready=False sector_rank=10 price=7.24 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=50.67 liquidity=1829055.88 spike=0.15
- EAST.CA: score=16.24 buy_ready=False sector_rank=18 price=36.5 support=36.01 resistance=37.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=49.39 liquidity=49466556.0 spike=0.61
- EBSC.CA: score=12.82 buy_ready=False sector_rank=10 price=1.92 support=1.85 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1453909.88 spike=0.21
- ECAP.CA: score=20.58 buy_ready=False sector_rank=10 price=33.89 support=32.12 resistance=34.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=66.73 liquidity=6920083.5 spike=1.15
- EDFM.CA: score=12.0 buy_ready=False sector_rank=10 price=399.72 support=323.25 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=71.4 liquidity=633929.88 spike=0.11
- EEII.CA: score=19.72 buy_ready=False sector_rank=10 price=2.7 support=2.54 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=44.64 liquidity=20270176.0 spike=1.18
- EFIC.CA: score=24.16 buy_ready=False sector_rank=15 price=198.72 support=180.07 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=54.94 liquidity=39349472.0 spike=2.13
- EFID.CA: score=10.24 buy_ready=False sector_rank=18 price=30.76 support=29.6 resistance=30.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=170646128.0 spike=3.8
- EFIH.CA: score=26.84 buy_ready=False sector_rank=3 price=24.2 support=21.56 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=88392256.0 spike=1.22
- EGAL.CA: score=17.9 buy_ready=False sector_rank=15 price=295.08 support=290.0 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=56.26 liquidity=23953372.0 spike=0.57
- EGAS.CA: score=23.4 buy_ready=False sector_rank=1 price=59.11 support=48.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=75.45 liquidity=14894736.0 spike=0.61
- EGBE.CA: score=9.19 buy_ready=False sector_rank=13 price=0.49 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=65.38 liquidity=69519.8 spike=0.93
- EGCH.CA: score=23.68 buy_ready=False sector_rank=15 price=14.25 support=12.58 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=120776864.0 spike=1.39
- EGSA.CA: score=9.42 buy_ready=False sector_rank=4 price=8.9 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=43.14 liquidity=16460.25 spike=0.81
- EGTS.CA: score=16.2 buy_ready=False sector_rank=12 price=17.49 support=17.11 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=37.8 liquidity=12338709.0 spike=0.31
- EHDR.CA: score=21.36 buy_ready=False sector_rank=10 price=2.83 support=2.56 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=21287962.0 spike=0.49
- EKHO.CA: score=8.4 buy_ready=False sector_rank=1 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-02T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=20.31 buy_ready=False sector_rank=11 price=2.18 support=2.08 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=37504400.0 spike=0.52
- ELKA.CA: score=19.76 buy_ready=False sector_rank=10 price=1.77 support=1.38 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=53.27 liquidity=91957048.0 spike=1.2
- ELNA.CA: score=0.69 buy_ready=False sector_rank=10 price=37.36 support=36.5 resistance=40.5 source=Yahoo Finance as_of=2026-08-02T21:00:00+00:00 freshness=FRESH RSI=29.59 liquidity=321520.17 spike=0.47
- ELSH.CA: score=19.36 buy_ready=False sector_rank=10 price=14.0 support=13.13 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=31352874.0 spike=0.23
- ELWA.CA: score=2.15 buy_ready=False sector_rank=10 price=1.69 support=1.72 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=5.71 liquidity=783040.06 spike=0.53
- EMFD.CA: score=11.2 buy_ready=False sector_rank=12 price=12.09 support=11.51 resistance=12.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=208591632.0 spike=3.65
- ENGC.CA: score=6.36 buy_ready=False sector_rank=10 price=46.0 support=44.62 resistance=46.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14125840.0 spike=0.48
- EOSB.CA: score=17.96 buy_ready=False sector_rank=10 price=1.55 support=1.51 resistance=1.62 source=Yahoo Finance as_of=2026-08-02T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=120524.9 spike=2.24
- EPCO.CA: score=17.38 buy_ready=False sector_rank=10 price=11.21 support=8.79 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=71.07 liquidity=6014619.0 spike=0.19
- EPPK.CA: score=9.73 buy_ready=False sector_rank=10 price=14.82 support=13.64 resistance=15.93 source=Yahoo Finance as_of=2026-08-02T21:00:00+00:00 freshness=FRESH RSI=57.65 liquidity=366987.65 spike=0.36
- ETEL.CA: score=21.94 buy_ready=False sector_rank=4 price=110.27 support=92.61 resistance=114.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=67.45 liquidity=128318144.0 spike=1.27
- ETRS.CA: score=14.77 buy_ready=False sector_rank=10 price=10.52 support=10.21 resistance=10.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=55.63 liquidity=5408333.5 spike=0.14
- EXPA.CA: score=20.12 buy_ready=False sector_rank=13 price=20.5 support=18.34 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=88.93 liquidity=34113760.0 spike=0.99
- FAIT.CA: score=10.26 buy_ready=False sector_rank=13 price=37.04 support=36.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=50.39 liquidity=1132056.25 spike=0.45
- FAITA.CA: score=6.33 buy_ready=False sector_rank=13 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=4 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=42812.66 spike=1.08
- FERC.CA: score=17.91 buy_ready=False sector_rank=15 price=77.0 support=74.05 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=52.88 liquidity=8013559.5 spike=0.65
- FWRY.CA: score=24.04 buy_ready=False sector_rank=3 price=19.56 support=18.42 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=44.01 liquidity=223083360.0 spike=1.82
- GBCO.CA: score=21.4 buy_ready=False sector_rank=8 price=31.34 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=47.95 liquidity=19696982.0 spike=0.31
- GDWA.CA: score=18.36 buy_ready=False sector_rank=10 price=0.82 support=0.77 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=40.43 liquidity=27435360.0 spike=0.25
- GGCC.CA: score=7.66 buy_ready=False sector_rank=10 price=1.09 support=0.99 resistance=1.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=62642496.0 spike=1.65
- GIHD.CA: score=20.15 buy_ready=False sector_rank=10 price=59.85 support=43.0 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=67.64 liquidity=8787104.0 spike=0.16
- GMCI.CA: score=10.14 buy_ready=False sector_rank=10 price=2.01 support=1.9 resistance=2.26 source=Yahoo Finance as_of=2026-08-02T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=772720.38 spike=0.65
- GRCA.CA: score=15.29 buy_ready=False sector_rank=10 price=57.99 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=3926695.5 spike=0.22
- GSSC.CA: score=17.94 buy_ready=False sector_rank=10 price=282.51 support=248.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=4574937.0 spike=0.25
- GTWL.CA: score=14.36 buy_ready=False sector_rank=10 price=98.76 support=82.2 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=31.71 liquidity=35700432.0 spike=0.3
- HDBK.CA: score=15.74 buy_ready=False sector_rank=13 price=84.0 support=76.9 resistance=85.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=71.62 liquidity=8616222.0 spike=0.2
- HELI.CA: score=18.2 buy_ready=False sector_rank=12 price=8.33 support=6.66 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=78.07 liquidity=61227940.0 spike=0.27
- HRHO.CA: score=26.4 buy_ready=False sector_rank=7 price=27.83 support=25.95 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=50.84 liquidity=304127424.0 spike=3.66
- ICID.CA: score=10.79 buy_ready=False sector_rank=10 price=8.03 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=41.75 liquidity=1430196.5 spike=0.19
- IDRE.CA: score=23.44 buy_ready=False sector_rank=10 price=50.28 support=42.5 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=59.68 liquidity=28122520.0 spike=1.04
- IFAP.CA: score=32.4 buy_ready=False sector_rank=2 price=20.92 support=18.96 resistance=20.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=57.4 liquidity=52498280.0 spike=4.3
- INFI.CA: score=19.33 buy_ready=False sector_rank=10 price=115.39 support=93.52 resistance=124.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=77.84 liquidity=8965081.0 spike=0.35
- IRON.CA: score=9.2 buy_ready=False sector_rank=15 price=34.21 support=33.8 resistance=34.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17346646.0 spike=2.65
- ISMA.CA: score=13.39 buy_ready=False sector_rank=10 price=30.69 support=26.54 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=75.88 liquidity=5021802.0 spike=0.2
- ISMQ.CA: score=18.9 buy_ready=False sector_rank=15 price=9.2 support=8.96 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=37.76 liquidity=30620580.0 spike=0.39
- ISPH.CA: score=5.82 buy_ready=False sector_rank=17 price=13.4 support=13.09 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=130523992.0 spike=1.25
- JUFO.CA: score=6.34 buy_ready=False sector_rank=18 price=33.8 support=32.6 resistance=34.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45571940.0 spike=1.55
- KABO.CA: score=21.4 buy_ready=False sector_rank=9 price=8.1 support=6.57 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=12021132.0 spike=0.24
- KWIN.CA: score=6.36 buy_ready=False sector_rank=10 price=89.39 support=88.5 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28764936.0 spike=0.51
- KZPC.CA: score=25.6 buy_ready=False sector_rank=10 price=8.99 support=8.26 resistance=8.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=57.53 liquidity=17745496.0 spike=3.12
- LCSW.CA: score=23.4 buy_ready=False sector_rank=5 price=35.24 support=29.35 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=72.85 liquidity=12990088.0 spike=0.21
- LUTS.CA: score=11.36 buy_ready=False sector_rank=10 price=0.7 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134715152.0 spike=4.11
- MAAL.CA: score=11.05 buy_ready=False sector_rank=10 price=8.7 support=7.56 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=66.36 liquidity=1689510.13 spike=0.1
- MASR.CA: score=19.36 buy_ready=False sector_rank=10 price=7.97 support=7.4 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=40.78 liquidity=21470880.0 spike=0.27
- MBSC.CA: score=25.3 buy_ready=False sector_rank=5 price=253.92 support=231.51 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=36800076.0 spike=1.95
- MCQE.CA: score=24.18 buy_ready=False sector_rank=5 price=186.13 support=172.1 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=24670682.0 spike=1.39
- MCRO.CA: score=6.36 buy_ready=False sector_rank=10 price=1.49 support=1.49 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96320144.0 spike=0.61
- MENA.CA: score=9.66 buy_ready=False sector_rank=12 price=6.93 support=6.86 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=464269.97 spike=0.07
- MEPA.CA: score=20.95 buy_ready=False sector_rank=10 price=1.86 support=1.61 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=9585873.0 spike=0.17
- MFPC.CA: score=17.9 buy_ready=False sector_rank=15 price=37.11 support=35.37 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=48.83 liquidity=32973576.0 spike=0.35
- MFSC.CA: score=24.26 buy_ready=False sector_rank=10 price=51.19 support=45.05 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=72.35 liquidity=25081294.0 spike=2.45
- MHOT.CA: score=15.6 buy_ready=False sector_rank=16 price=16.95 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=57.61 liquidity=6774751.0 spike=0.58
- MICH.CA: score=8.0 buy_ready=False sector_rank=10 price=48.56 support=48.12 resistance=51.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36525864.0 spike=1.82
- MILS.CA: score=7.42 buy_ready=False sector_rank=10 price=207.01 support=185.1 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83399576.0 spike=1.53
- MIPH.CA: score=10.12 buy_ready=False sector_rank=17 price=781.53 support=656.11 resistance=831.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=77.56 liquidity=791594.63 spike=0.16
- MOED.CA: score=10.36 buy_ready=False sector_rank=10 price=0.67 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=18.6 liquidity=11480099.0 spike=0.41
- MOIL.CA: score=11.54 buy_ready=False sector_rank=1 price=0.67 support=0.5 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=87.57 liquidity=136431.25 spike=0.2
- MOIN.CA: score=11.36 buy_ready=False sector_rank=10 price=36.4 support=30.4 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=139657680.0 spike=103.69
- MOSC.CA: score=16.67 buy_ready=False sector_rank=10 price=296.37 support=268.5 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=48.67 liquidity=3307423.25 spike=0.22
- MPCI.CA: score=6.36 buy_ready=False sector_rank=10 price=312.64 support=305.5 resistance=324.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73359008.0 spike=0.67
- MPCO.CA: score=25.4 buy_ready=False sector_rank=2 price=1.95 support=1.77 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=35253116.0 spike=0.4
- MPRC.CA: score=14.73 buy_ready=False sector_rank=10 price=44.62 support=38.0 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=3363634.5 spike=0.11
- MTIE.CA: score=11.4 buy_ready=False sector_rank=8 price=10.67 support=10.42 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88995424.0 spike=3.93
- NAHO.CA: score=7.37 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1857.3 spike=0.08
- NCCW.CA: score=21.56 buy_ready=False sector_rank=10 price=7.17 support=6.01 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=68.07 liquidity=33339658.0 spike=1.1
- NEDA.CA: score=6.87 buy_ready=False sector_rank=10 price=2.73 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=41.67 liquidity=505882.65 spike=0.62
- NHPS.CA: score=21.36 buy_ready=False sector_rank=10 price=84.0 support=70.01 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=50.45 liquidity=21816240.0 spike=0.27
- NINH.CA: score=21.21 buy_ready=False sector_rank=10 price=23.64 support=17.4 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=70.38 liquidity=9842605.0 spike=0.18
- NIPH.CA: score=5.32 buy_ready=False sector_rank=17 price=265.51 support=265.0 resistance=280.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108153688.0 spike=0.61
- OBRI.CA: score=10.29 buy_ready=False sector_rank=10 price=32.35 support=31.61 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=19.86 liquidity=9925642.0 spike=0.27
- OCDI.CA: score=19.2 buy_ready=False sector_rank=12 price=30.04 support=25.49 resistance=29.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=65.92 liquidity=76761984.0 spike=0.71
- OCPH.CA: score=15.58 buy_ready=False sector_rank=10 price=484.04 support=350.6 resistance=504.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=77.67 liquidity=7220590.5 spike=0.25
- ODIN.CA: score=20.36 buy_ready=False sector_rank=10 price=2.93 support=2.28 resistance=3.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=85.33 liquidity=13661765.0 spike=0.6
- OFH.CA: score=23.44 buy_ready=False sector_rank=10 price=0.79 support=0.62 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=74.19 liquidity=76199656.0 spike=1.04
- OIH.CA: score=6.11 buy_ready=False sector_rank=14 price=1.58 support=1.53 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=91636312.0 spike=1.06
- OLFI.CA: score=24.24 buy_ready=False sector_rank=18 price=24.79 support=22.25 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=61.82 liquidity=24412972.0 spike=0.65
- ORAS.CA: score=4.6 buy_ready=False sector_rank=20 price=703.26 support=695.2 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28608922.0 spike=1.0
- ORHD.CA: score=21.2 buy_ready=False sector_rank=12 price=42.0 support=38.0 resistance=41.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=58.43 liquidity=126749880.0 spike=0.8
- ORWE.CA: score=11.4 buy_ready=False sector_rank=9 price=26.12 support=24.47 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=363579808.0 spike=13.22
- PHAR.CA: score=10.32 buy_ready=False sector_rank=17 price=130.03 support=127.27 resistance=141.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=555027840.0 spike=3.65
- PHDC.CA: score=22.08 buy_ready=False sector_rank=12 price=15.5 support=14.32 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=51.81 liquidity=332018976.0 spike=1.44
- PHTV.CA: score=10.28 buy_ready=False sector_rank=10 price=342.5 support=262.5 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=82.64 liquidity=1913194.5 spike=0.41
- POUL.CA: score=13.24 buy_ready=False sector_rank=18 price=38.26 support=36.5 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=24.85 liquidity=24915936.0 spike=0.75
- PRCL.CA: score=19.4 buy_ready=False sector_rank=5 price=35.62 support=32.76 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=53.37 liquidity=15933601.0 spike=0.36
- PRDC.CA: score=21.2 buy_ready=False sector_rank=12 price=9.3 support=7.7 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=63.17 liquidity=61667120.0 spike=0.51
- PRMH.CA: score=16.65 buy_ready=False sector_rank=10 price=2.73 support=2.52 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=5288992.0 spike=0.32
- RACC.CA: score=19.36 buy_ready=False sector_rank=10 price=10.09 support=9.8 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=10183800.0 spike=0.43
- RAKT.CA: score=7.6 buy_ready=False sector_rank=10 price=22.96 support=21.25 resistance=23.7 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=76.43 liquidity=233686.87 spike=0.73
- RAYA.CA: score=8.86 buy_ready=False sector_rank=21 price=7.54 support=7.3 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=42767796.0 spike=0.33
- RMDA.CA: score=5.6 buy_ready=False sector_rank=17 price=5.78 support=5.76 resistance=6.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77921848.0 spike=1.14
- ROTO.CA: score=22.99 buy_ready=False sector_rank=10 price=45.75 support=40.5 resistance=46.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=67.0 liquidity=9621573.0 spike=0.47
- RREI.CA: score=23.36 buy_ready=False sector_rank=10 price=4.66 support=3.56 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=63.45 liquidity=38570900.0 spike=0.58
- RTVC.CA: score=12.76 buy_ready=False sector_rank=10 price=3.8 support=3.7 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=6019827.5 spike=1.19
- RUBX.CA: score=11.82 buy_ready=False sector_rank=10 price=12.83 support=12.02 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=7460585.5 spike=0.18
- SAUD.CA: score=8.48 buy_ready=False sector_rank=13 price=22.77 support=21.85 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24255870.0 spike=2.18
- SCEM.CA: score=21.74 buy_ready=False sector_rank=5 price=80.82 support=61.28 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=72.08 liquidity=102412808.0 spike=1.17
- SCFM.CA: score=23.36 buy_ready=False sector_rank=10 price=284.07 support=243.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=12343842.0 spike=0.43
- SCTS.CA: score=6.85 buy_ready=False sector_rank=19 price=603.97 support=602.0 resistance=648.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=44.12 liquidity=1828162.13 spike=0.37
- SDTI.CA: score=20.36 buy_ready=False sector_rank=10 price=64.03 support=46.0 resistance=75.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=85.05 liquidity=12611796.0 spike=0.53
- SEIG.CA: score=15.56 buy_ready=False sector_rank=10 price=263.07 support=188.19 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=61.25 liquidity=2199250.5 spike=0.07
- SIPC.CA: score=6.36 buy_ready=False sector_rank=10 price=4.58 support=4.33 resistance=4.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33323928.0 spike=0.68
- SKPC.CA: score=19.76 buy_ready=False sector_rank=15 price=16.29 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=43.03 liquidity=56758216.0 spike=1.43
- SMFR.CA: score=22.12 buy_ready=False sector_rank=10 price=237.1 support=202.0 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=36.35 liquidity=32077350.0 spike=1.38
- SNFC.CA: score=6.65 buy_ready=False sector_rank=10 price=10.88 support=10.7 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=16.1 liquidity=5281335.0 spike=0.45
- SPIN.CA: score=18.15 buy_ready=False sector_rank=9 price=15.71 support=14.49 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=69.16 liquidity=6751020.5 spike=0.26
- SPMD.CA: score=22.54 buy_ready=False sector_rank=10 price=0.48 support=0.43 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=64.41 liquidity=9173097.0 spike=0.27
- SUGR.CA: score=13.46 buy_ready=False sector_rank=18 price=47.83 support=46.47 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=40.22 liquidity=5215764.5 spike=0.93
- SVCE.CA: score=21.36 buy_ready=False sector_rank=10 price=9.36 support=9.06 resistance=9.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=42.42 liquidity=29133598.0 spike=0.83
- SWDY.CA: score=10.49 buy_ready=False sector_rank=11 price=105.63 support=105.01 resistance=109.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74042112.0 spike=3.09
- TALM.CA: score=5.02 buy_ready=False sector_rank=19 price=18.02 support=18.0 resistance=18.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21204498.0 spike=0.53
- TMGH.CA: score=19.2 buy_ready=False sector_rank=12 price=98.84 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=47.64 liquidity=117287560.0 spike=0.32
- TRTO.CA: score=7.36 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-08-03T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=750.86 spike=0.48
- UEFM.CA: score=13.18 buy_ready=False sector_rank=10 price=551.63 support=479.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=63.26 liquidity=1816466.88 spike=0.34
- UEGC.CA: score=23.36 buy_ready=False sector_rank=10 price=2.69 support=1.58 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=70.77 liquidity=31978042.0 spike=0.58
- UNIP.CA: score=17.82 buy_ready=False sector_rank=10 price=0.38 support=0.32 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=61.78 liquidity=6456414.5 spike=0.22
- UNIT.CA: score=14.49 buy_ready=False sector_rank=12 price=18.16 support=13.45 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=5297931.5 spike=0.17
- WCDF.CA: score=15.31 buy_ready=False sector_rank=10 price=588.0 support=505.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=64.76 liquidity=1948392.25 spike=0.53
- WKOL.CA: score=19.25 buy_ready=False sector_rank=10 price=323.65 support=295.51 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=54.67 liquidity=5887156.5 spike=0.27
- ZEOT.CA: score=20.36 buy_ready=False sector_rank=10 price=12.85 support=10.91 resistance=13.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=81.14 liquidity=12922753.0 spike=0.42
- ZMID.CA: score=21.2 buy_ready=False sector_rank=12 price=7.31 support=6.63 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=46.75 liquidity=139691904.0 spike=0.51

## Backtesting Lite
- IFAP.CA: 180d return=11.24%, max drawdown=-12.94%, MA20>MA50 days last20=1, as_of=2026-08-03T21:00:00+00:00
- EFIH.CA: 180d return=52.61%, max drawdown=-22.68%, MA20>MA50 days last20=11, as_of=2026-08-03T21:00:00+00:00
- HRHO.CA: 180d return=1.14%, max drawdown=-18.92%, MA20>MA50 days last20=4, as_of=2026-08-03T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- IFAP.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=International Agricultural Products summary=International Agricultural Products stock is testing key psychological barrier – Analysis; International Agricultural Products’ non-consolidated net profits hit EGP 12.5m in Q1-25/26; El Dawlia Fertilizers announces new company of EGP 500m authorised capital
  - International Agricultural Products stock is testing key psychological barrier – Analysis: https://english.mubasher.info/news/4560334/International-Agricultural-Products-stock-is-testing-key-psychological-barrier-Analysis/
  - International Agricultural Products’ non-consolidated net profits hit EGP 12.5m in Q1-25/26: https://english.mubasher.info/news/4525080/International-Agricultural-Products-non-consolidated-net-profits-hit-EGP-12-5m-in-Q1-25-26/
  - El Dawlia Fertilizers announces new company of EGP 500m authorised capital: https://english.mubasher.info/news/3971612/El-Dawlia-Fertilizers-announces-new-company-of-EGP-500m-authorised-capital/
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=947 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=581 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=581 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- MBSC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=581 sources=3 expected=Misr Beni Suef Cement summary=Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025; Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25; Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25
  - Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025: https://english.mubasher.info/news/4599415/Misr-Beni-Suef-s-consolidated-net-profits-near-EGP-4bn-in-2025/
  - Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25: https://english.mubasher.info/news/4488249/Misr-Beni-Suef-s-consolidated-net-profits-hit-EGP-953m-in-H1-25/
  - Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25: https://english.mubasher.info/news/4455784/Misr-Beni-Suef-Cement-s-consolidate-profits-fall-to-EGP-574m-in-Q1-25/

## Warnings
- Evidence for IFAP.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
