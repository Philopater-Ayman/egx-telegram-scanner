# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-08-19T16:56:59.344472+00:00
Generated Cairo: 2026-08-19 19:56
Run timing: target 19:30 Cairo | generated Cairo 2026-08-19 19:56 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-08-19 19:53

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 155/189
- Top sector: Agriculture & Food Production

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, August 19
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 63.16% / above MA50 68.42%
- EGX70 regime: MIXED / above MA20 58.33% / above MA50 83.33%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- GTWL.CA: liquidity=748021184.0 spike=5.08 score=10.77
- ZMID.CA: liquidity=622329024.0 spike=2.74 score=8.81
- CCAP.CA: liquidity=549420608.0 spike=0.91 score=27.4
- LUTS.CA: liquidity=489590336.0 spike=5.3 score=10.77
- COMI.CA: liquidity=475622080.0 spike=1.06 score=19.52

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 is bullish while EGX70 is mixed, sector breadth is weak at 33%, and risk mode is defensive; the scanner flagged top accumulation‑spike stocks in leading sectors as watch‑list candidates.
- IFAP.CA and MPCO.CA (Agriculture & Food) show liquidity spikes >4.7x and sit near support/resistance, but extended RSI limits near‑term upside.
- CCAP.CA (Investment Holding) has high liquidity and accumulation spike, yet momentum is extended and it trades close to resistance.
- SKPC.CA (Basic Resources) exhibits the largest liquidity spike (7.6x) and trades just above resistance with overheated RSI, warranting caution.
- Due to the mixed EGX70 trend and weak sector breadth, the risk mode stays defensive, so no new BUY is allowed; tickets remain on HOLD/watch.

## Top Liquidity Spikes
- KZPC.CA: spike=11.21 liquidity=173853408.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOED.CA: spike=7.62 liquidity=325454816.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SKPC.CA: spike=7.59 liquidity=378107264.0 outlook=BULLISH_WATCH score=82.7 buy_ready=False
- LUTS.CA: spike=5.3 liquidity=489590336.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=5.08 liquidity=748021184.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Agriculture & Food Production: score=13.5 5d=-1.35% 20d=16.25% aboveMA50=100.0%
- #2 Investment Holding: score=10.47 5d=5.85% 20d=2.22% aboveMA50=100.0%
- #3 Education: score=10.41 5d=0.0% 20d=18.85% aboveMA50=100.0%
- #4 Banking & Financials: score=9.94 5d=2.74% 20d=9.1% aboveMA50=90.0%
- #5 Basic Resources & Chemicals: score=9.7 5d=3.55% 20d=5.72% aboveMA50=100.0%
- #6 Textiles: score=9.27 5d=3.64% 20d=11.27% aboveMA50=75.0%
- #7 Transportation & Logistics: score=9.11 5d=-0.67% 20d=10.94% aboveMA50=100.0%
- #8 Fintech & Payments: score=8.5 5d=2.91% 20d=5.53% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- IFAP.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- IRON.CA: BULLISH_WATCH score=97.7 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- SCTS.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CCAP.CA: BULLISH_WATCH score=95 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- BINV.CA: BULLISH_WATCH score=95 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20
- CLHO.CA: BULLISH_WATCH score=93.33 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CIRA.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- GSSC.CA: BULLISH_WATCH score=83.42 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MPCO.CA: BULLISH_WATCH score=83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; far above support
- SKPC.CA: BULLISH_WATCH score=82.7 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=20.77 buy_ready=False sector_rank=14 price=330.24 support=234.05 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.9 liquidity=42305604.0 spike=0.72
- ABUK.CA: score=18.4 buy_ready=False sector_rank=5 price=75.91 support=70.6 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.55 liquidity=88081360.0 spike=0.71
- ACAMD.CA: score=16.07 buy_ready=False sector_rank=14 price=2.15 support=2.16 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.88 liquidity=68473096.0 spike=1.15
- ACGC.CA: score=20.64 buy_ready=False sector_rank=6 price=14.16 support=9.75 resistance=14.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=97.49 liquidity=45780036.0 spike=1.12
- ADCI.CA: score=20.9 buy_ready=False sector_rank=14 price=284.23 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.31 liquidity=8134311.0 spike=0.37
- ADIB.CA: score=21.4 buy_ready=False sector_rank=4 price=53.99 support=46.99 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.18 liquidity=43937344.0 spike=0.39
- ADPC.CA: score=19.29 buy_ready=False sector_rank=14 price=4.1 support=3.8 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=62307160.0 spike=1.26
- AFDI.CA: score=20.77 buy_ready=False sector_rank=14 price=62.5 support=47.03 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=68.96 liquidity=12674167.0 spike=0.51
- AFMC.CA: score=5.77 buy_ready=False sector_rank=14 price=238.75 support=230.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87129568.0 spike=0.5
- AJWA.CA: score=24.77 buy_ready=False sector_rank=14 price=196.53 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.17 liquidity=29744302.0 spike=0.67
- ALCN.CA: score=21.5 buy_ready=False sector_rank=7 price=30.89 support=28.8 resistance=32.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.17 liquidity=23472534.0 spike=1.05
- ALUM.CA: score=17.77 buy_ready=False sector_rank=14 price=27.48 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=85.66 liquidity=14245966.0 spike=0.72
- AMER.CA: score=5.33 buy_ready=False sector_rank=15 price=6.05 support=5.92 resistance=6.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92772048.0 spike=0.82
- AMES.CA: score=10.77 buy_ready=False sector_rank=14 price=154.03 support=131.2 resistance=154.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=263547136.0 spike=4.4
- AMIA.CA: score=20.71 buy_ready=False sector_rank=14 price=16.06 support=10.1 resistance=17.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=93.6 liquidity=47696056.0 spike=1.47
- AMOC.CA: score=21.48 buy_ready=False sector_rank=11 price=11.37 support=8.16 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.61 liquidity=193666800.0 spike=1.54
- APSW.CA: score=9.91 buy_ready=False sector_rank=14 price=8.74 support=8.6 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=2066766.5 spike=1.04
- ARAB.CA: score=18.33 buy_ready=False sector_rank=15 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.87 liquidity=42153496.0 spike=0.45
- ARCC.CA: score=18.39 buy_ready=False sector_rank=12 price=72.81 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=82.5 liquidity=42618576.0 spike=0.44
- AREH.CA: score=17.77 buy_ready=False sector_rank=14 price=1.5 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.22 liquidity=16262687.0 spike=0.48
- ARVA.CA: score=5.77 buy_ready=False sector_rank=14 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=18.77 buy_ready=False sector_rank=14 price=63.03 support=60.63 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.56 liquidity=20839012.0 spike=0.35
- ASPI.CA: score=5.77 buy_ready=False sector_rank=14 price=0.53 support=0.51 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24833580.0 spike=0.56
- ATLC.CA: score=20.08 buy_ready=False sector_rank=17 price=5.28 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=10548477.0 spike=0.52
- ATQA.CA: score=24.46 buy_ready=False sector_rank=5 price=11.0 support=9.6 resistance=11.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.82 liquidity=204000464.0 spike=3.03
- AXPH.CA: score=18.02 buy_ready=False sector_rank=14 price=1360.07 support=1121.56 resistance=1460.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=4867773.5 spike=1.19
- BINV.CA: score=25.06 buy_ready=False sector_rank=2 price=48.33 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.14 liquidity=20129468.0 spike=2.83
- BIOC.CA: score=17.77 buy_ready=False sector_rank=14 price=477.41 support=106.61 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=78.12 liquidity=116705704.0 spike=0.49
- BTFH.CA: score=14.88 buy_ready=False sector_rank=17 price=3.01 support=3.05 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=321036800.0 spike=1.4
- CAED.CA: score=9.11 buy_ready=False sector_rank=14 price=168.01 support=141.22 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=178936384.0 spike=2.67
- CANA.CA: score=18.09 buy_ready=False sector_rank=4 price=42.25 support=36.05 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=78.13 liquidity=9687778.0 spike=0.44
- CCAP.CA: score=27.4 buy_ready=False sector_rank=2 price=5.5 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=549420608.0 spike=0.91
- CCRS.CA: score=15.77 buy_ready=False sector_rank=14 price=2.44 support=2.44 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=14849269.0 spike=0.82
- CEFM.CA: score=23.35 buy_ready=False sector_rank=14 price=145.49 support=121.4 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.9 liquidity=81829928.0 spike=2.29
- CERA.CA: score=15.77 buy_ready=False sector_rank=14 price=1.26 support=1.25 resistance=1.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=17618254.0 spike=0.86
- CFGH.CA: score=14.41 buy_ready=False sector_rank=14 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=61.9 liquidity=57920.13 spike=3.29
- CICH.CA: score=10.16 buy_ready=False sector_rank=17 price=12.31 support=11.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=65.24 liquidity=4088526.0 spike=0.54
- CIEB.CA: score=24.26 buy_ready=False sector_rank=4 price=24.51 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=19609534.0 spike=1.43
- CIRA.CA: score=22.4 buy_ready=False sector_rank=3 price=37.5 support=31.35 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.01 liquidity=24215028.0 spike=0.43
- CLHO.CA: score=26.13 buy_ready=False sector_rank=13 price=17.35 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=206484848.0 spike=3.7
- CNFN.CA: score=17.42 buy_ready=False sector_rank=17 price=4.86 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=9340017.0 spike=0.46
- COMI.CA: score=19.52 buy_ready=False sector_rank=4 price=136.81 support=136.7 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=475622080.0 spike=1.06
- COPR.CA: score=9.67 buy_ready=False sector_rank=14 price=0.48 support=0.47 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=166521488.0 spike=2.95
- COSG.CA: score=20.77 buy_ready=False sector_rank=14 price=1.77 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.44 liquidity=27827828.0 spike=0.59
- CPCI.CA: score=13.38 buy_ready=False sector_rank=14 price=528.04 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.55 liquidity=2615497.75 spike=0.3
- CSAG.CA: score=21.4 buy_ready=False sector_rank=7 price=39.22 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=74.6 liquidity=13499057.0 spike=0.53
- DAPH.CA: score=5.77 buy_ready=False sector_rank=14 price=118.23 support=118.11 resistance=129.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14747270.0 spike=0.37
- DEIN.CA: score=-4.23 buy_ready=False sector_rank=14 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=20.37 buy_ready=False sector_rank=10 price=28.52 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.71 liquidity=8970549.0 spike=0.61
- DSCW.CA: score=18.95 buy_ready=False sector_rank=14 price=1.94 support=1.89 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=107851136.0 spike=1.09
- DTPP.CA: score=20.77 buy_ready=False sector_rank=14 price=297.37 support=222.0 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.26 liquidity=63495532.0 spike=0.99
- EALR.CA: score=22.77 buy_ready=False sector_rank=14 price=406.45 support=360.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=33823144.0 spike=0.71
- EASB.CA: score=18.72 buy_ready=False sector_rank=14 price=7.41 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.47 liquidity=7955764.0 spike=0.79
- EAST.CA: score=17.4 buy_ready=False sector_rank=10 price=36.16 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=26030378.0 spike=0.4
- EBSC.CA: score=10.38 buy_ready=False sector_rank=14 price=1.9 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=4616426.0 spike=0.82
- ECAP.CA: score=17.53 buy_ready=False sector_rank=14 price=37.19 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.87 liquidity=6761765.5 spike=0.56
- EDFM.CA: score=9.82 buy_ready=False sector_rank=14 price=409.31 support=352.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=80.52 liquidity=2049008.25 spike=0.35
- EEII.CA: score=25.53 buy_ready=False sector_rank=14 price=3.17 support=2.54 resistance=3.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.73 liquidity=49774268.0 spike=2.38
- EFIC.CA: score=21.4 buy_ready=False sector_rank=5 price=219.95 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.36 liquidity=40337064.0 spike=0.9
- EFID.CA: score=18.4 buy_ready=False sector_rank=10 price=31.82 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=87.63 liquidity=29822024.0 spike=0.33
- EFIH.CA: score=21.52 buy_ready=False sector_rank=8 price=23.84 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.16 liquidity=119557592.0 spike=1.06
- EGAL.CA: score=20.4 buy_ready=False sector_rank=5 price=331.03 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=83.84 liquidity=55667700.0 spike=0.54
- EGAS.CA: score=19.4 buy_ready=False sector_rank=11 price=57.24 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=74.56 liquidity=13006650.0 spike=0.53
- EGBE.CA: score=11.8 buy_ready=False sector_rank=4 price=0.53 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.43 liquidity=201537.05 spike=1.1
- EGCH.CA: score=18.4 buy_ready=False sector_rank=5 price=13.96 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=99424968.0 spike=0.85
- EGSA.CA: score=1.41 buy_ready=False sector_rank=9 price=8.73 support=8.65 resistance=9.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=30.23 liquidity=11214.61 spike=0.52
- EGTS.CA: score=5.33 buy_ready=False sector_rank=15 price=17.52 support=17.16 resistance=18.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10883295.0 spike=0.29
- EHDR.CA: score=20.77 buy_ready=False sector_rank=14 price=2.99 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.29 liquidity=26659000.0 spike=0.56
- EKHO.CA: score=7.4 buy_ready=False sector_rank=11 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.54 buy_ready=False sector_rank=19 price=2.12 support=2.12 resistance=2.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=70675568.0 spike=1.01
- ELKA.CA: score=18.77 buy_ready=False sector_rank=14 price=1.72 support=1.69 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=67834240.0 spike=0.91
- ELNA.CA: score=6.12 buy_ready=False sector_rank=14 price=36.14 support=36.5 resistance=39.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.88 liquidity=1254215.25 spike=2.55
- ELSH.CA: score=15.77 buy_ready=False sector_rank=14 price=13.49 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.04 liquidity=36974088.0 spike=0.46
- ELWA.CA: score=9.18 buy_ready=False sector_rank=14 price=1.66 support=1.65 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=1416169.88 spike=0.96
- EMFD.CA: score=15.33 buy_ready=False sector_rank=15 price=11.6 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=50816012.0 spike=0.85
- ENGC.CA: score=5.77 buy_ready=False sector_rank=14 price=44.99 support=44.31 resistance=50.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20178428.0 spike=0.71
- EOSB.CA: score=12.77 buy_ready=False sector_rank=14 price=1.55 support=1.53 resistance=1.62 source=Yahoo Finance as_of=2026-08-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=497.55 spike=0.01
- EPCO.CA: score=7.61 buy_ready=False sector_rank=14 price=11.57 support=11.41 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52580908.0 spike=1.92
- EPPK.CA: score=1.27 buy_ready=False sector_rank=14 price=13.28 support=12.62 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=18.35 liquidity=505130.63 spike=0.55
- ETEL.CA: score=23.76 buy_ready=False sector_rank=9 price=114.85 support=100.0 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.53 liquidity=158291024.0 spike=1.18
- ETRS.CA: score=17.85 buy_ready=False sector_rank=14 price=11.0 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=79.37 liquidity=31103084.0 spike=1.04
- EXPA.CA: score=21.7 buy_ready=False sector_rank=4 price=20.96 support=19.6 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=73.28 liquidity=41409016.0 spike=1.15
- FAIT.CA: score=15.16 buy_ready=False sector_rank=4 price=40.65 support=36.1 resistance=43.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=91.33 liquidity=5842019.0 spike=1.46
- FAITA.CA: score=13.42 buy_ready=False sector_rank=4 price=0.99 support=0.96 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.79 liquidity=22467.69 spike=0.4
- FERC.CA: score=25.4 buy_ready=False sector_rank=5 price=77.72 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=80359440.0 spike=4.19
- FWRY.CA: score=21.88 buy_ready=False sector_rank=8 price=19.01 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.73 liquidity=146552656.0 spike=1.24
- GBCO.CA: score=13.48 buy_ready=False sector_rank=21 price=29.7 support=29.53 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.71 liquidity=51459712.0 spike=1.0
- GDWA.CA: score=9.77 buy_ready=False sector_rank=14 price=0.79 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=51047180.0 spike=0.47
- GGCC.CA: score=18.99 buy_ready=False sector_rank=14 price=0.93 support=0.8 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.82 liquidity=56536012.0 spike=1.11
- GIHD.CA: score=19.66 buy_ready=False sector_rank=14 price=63.41 support=51.68 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.09 liquidity=8896157.0 spike=0.21
- GMCI.CA: score=8.4 buy_ready=False sector_rank=14 price=1.91 support=1.88 resistance=2.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=1213216.75 spike=1.71
- GRCA.CA: score=22.81 buy_ready=False sector_rank=14 price=56.77 support=54.7 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.08 liquidity=59852804.0 spike=3.02
- GSSC.CA: score=22.77 buy_ready=False sector_rank=14 price=285.0 support=264.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=15839186.0 spike=0.72
- GTWL.CA: score=10.77 buy_ready=False sector_rank=14 price=202.0 support=175.01 resistance=205.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=748021184.0 spike=5.08
- HDBK.CA: score=16.4 buy_ready=False sector_rank=4 price=90.29 support=79.95 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=95.8 liquidity=37473820.0 spike=0.91
- HELI.CA: score=13.33 buy_ready=False sector_rank=15 price=7.65 support=7.5 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.93 liquidity=136243200.0 spike=0.8
- HRHO.CA: score=14.32 buy_ready=False sector_rank=17 price=26.0 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=110218536.0 spike=1.12
- ICID.CA: score=19.77 buy_ready=False sector_rank=14 price=15.63 support=7.83 resistance=16.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=96.8 liquidity=19516410.0 spike=0.95
- IDRE.CA: score=19.71 buy_ready=False sector_rank=14 price=53.05 support=45.28 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=74.97 liquidity=8938331.0 spike=0.31
- IFAP.CA: score=31.4 buy_ready=False sector_rank=1 price=20.78 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.58 liquidity=116017968.0 spike=4.71
- INFI.CA: score=5.77 buy_ready=False sector_rank=14 price=147.78 support=140.66 resistance=158.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26672434.0 spike=0.45
- IRON.CA: score=23.8 buy_ready=False sector_rank=5 price=31.95 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.1 liquidity=17247940.0 spike=1.7
- ISMA.CA: score=20.75 buy_ready=False sector_rank=14 price=35.64 support=27.27 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.16 liquidity=43086612.0 spike=1.49
- ISMQ.CA: score=19.4 buy_ready=False sector_rank=5 price=9.16 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=35341456.0 spike=0.59
- ISPH.CA: score=21.13 buy_ready=False sector_rank=13 price=13.02 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=66652756.0 spike=0.35
- JUFO.CA: score=14.4 buy_ready=False sector_rank=10 price=26.83 support=22.78 resistance=29.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=91.13 liquidity=30173004.0 spike=0.5
- KABO.CA: score=21.4 buy_ready=False sector_rank=6 price=9.05 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=27786770.0 spike=0.67
- KWIN.CA: score=13.77 buy_ready=False sector_rank=14 price=85.24 support=84.08 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.96 liquidity=19226904.0 spike=0.32
- KZPC.CA: score=10.77 buy_ready=False sector_rank=14 price=13.97 support=12.16 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=173853408.0 spike=11.21
- LCSW.CA: score=19.39 buy_ready=False sector_rank=12 price=33.85 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=30677504.0 spike=0.65
- LUTS.CA: score=10.77 buy_ready=False sector_rank=14 price=1.71 support=1.42 resistance=1.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=489590336.0 spike=5.3
- MAAL.CA: score=15.54 buy_ready=False sector_rank=14 price=8.69 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.76 liquidity=6770372.5 spike=0.47
- MASR.CA: score=15.77 buy_ready=False sector_rank=14 price=7.63 support=7.45 resistance=8.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.3 liquidity=70513488.0 spike=0.95
- MBSC.CA: score=18.47 buy_ready=False sector_rank=12 price=370.0 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=81.15 liquidity=78671952.0 spike=1.04
- MCQE.CA: score=22.55 buy_ready=False sector_rank=12 price=217.29 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.22 liquidity=77542408.0 spike=1.58
- MCRO.CA: score=18.77 buy_ready=False sector_rank=14 price=1.47 support=1.38 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=68452888.0 spike=0.39
- MENA.CA: score=15.75 buy_ready=False sector_rank=15 price=7.06 support=6.83 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=5423491.5 spike=0.83
- MEPA.CA: score=18.77 buy_ready=False sector_rank=14 price=1.83 support=1.76 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=14627760.0 spike=0.23
- MFPC.CA: score=22.22 buy_ready=False sector_rank=5 price=39.19 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.65 liquidity=113528904.0 spike=1.41
- MFSC.CA: score=15.44 buy_ready=False sector_rank=14 price=49.02 support=46.0 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=6673668.5 spike=0.57
- MHOT.CA: score=18.29 buy_ready=False sector_rank=16 price=18.31 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.78 liquidity=13917140.0 spike=0.8
- MICH.CA: score=19.77 buy_ready=False sector_rank=14 price=48.48 support=37.83 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.28 liquidity=34425848.0 spike=0.91
- MILS.CA: score=8.95 buy_ready=False sector_rank=14 price=214.87 support=212.7 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=214379648.0 spike=2.59
- MIPH.CA: score=8.73 buy_ready=False sector_rank=13 price=762.83 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=65.18 liquidity=1594417.25 spike=0.37
- MOED.CA: score=10.77 buy_ready=False sector_rank=14 price=0.77 support=0.74 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=325454816.0 spike=7.62
- MOIL.CA: score=4.55 buy_ready=False sector_rank=11 price=0.65 support=0.57 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=145604.97 spike=0.23
- MOIN.CA: score=17.77 buy_ready=False sector_rank=14 price=34.92 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=76.55 liquidity=15313376.0 spike=0.53
- MOSC.CA: score=18.63 buy_ready=False sector_rank=14 price=325.93 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=84.17 liquidity=21524818.0 spike=1.43
- MPCI.CA: score=20.77 buy_ready=False sector_rank=14 price=370.0 support=261.0 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.02 liquidity=96502744.0 spike=0.61
- MPCO.CA: score=27.76 buy_ready=False sector_rank=1 price=2.2 support=1.82 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=180433984.0 spike=1.68
- MPRC.CA: score=19.95 buy_ready=False sector_rank=14 price=41.94 support=43.05 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.42 liquidity=41400964.0 spike=1.59
- MTIE.CA: score=13.58 buy_ready=False sector_rank=21 price=8.53 support=8.68 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=55745788.0 spike=1.05
- NAHO.CA: score=0.46 buy_ready=False sector_rank=14 price=0.14 support=0.14 resistance=0.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=233254.12 spike=3.23
- NCCW.CA: score=10.77 buy_ready=False sector_rank=14 price=5.89 support=5.67 resistance=7.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.18 liquidity=29929526.0 spike=0.88
- NEDA.CA: score=11.55 buy_ready=False sector_rank=14 price=2.84 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=81.08 liquidity=1141409.5 spike=1.32
- NHPS.CA: score=18.77 buy_ready=False sector_rank=14 price=87.0 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.53 liquidity=13855654.0 spike=0.29
- NINH.CA: score=18.77 buy_ready=False sector_rank=14 price=21.91 support=21.12 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.39 liquidity=41944792.0 spike=0.8
- NIPH.CA: score=6.13 buy_ready=False sector_rank=13 price=344.69 support=333.6 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=294207136.0 spike=0.97
- OBRI.CA: score=16.77 buy_ready=False sector_rank=14 price=32.67 support=31.61 resistance=36.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.66 liquidity=24158218.0 spike=0.68
- OCDI.CA: score=20.33 buy_ready=False sector_rank=15 price=32.08 support=26.6 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.8 liquidity=61343416.0 spike=0.45
- OCPH.CA: score=9.79 buy_ready=False sector_rank=14 price=255.14 support=225.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.41 liquidity=8026998.0 spike=0.29
- ODIN.CA: score=5.83 buy_ready=False sector_rank=14 price=3.34 support=3.3 resistance=3.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40616476.0 spike=1.03
- OFH.CA: score=17.77 buy_ready=False sector_rank=14 price=0.91 support=0.69 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=82.93 liquidity=68001632.0 spike=0.76
- OIH.CA: score=21.98 buy_ready=False sector_rank=2 price=1.87 support=1.43 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.67 liquidity=221820224.0 spike=1.79
- OLFI.CA: score=21.4 buy_ready=False sector_rank=10 price=23.82 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.67 liquidity=19436334.0 spike=0.3
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=744.2 support=742.0 resistance=768.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116499440.0 spike=1.0
- ORHD.CA: score=18.33 buy_ready=False sector_rank=15 price=40.49 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.93 liquidity=145406432.0 spike=0.89
- ORWE.CA: score=18.4 buy_ready=False sector_rank=6 price=25.3 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.89 liquidity=28431694.0 spike=0.37
- PHAR.CA: score=21.13 buy_ready=False sector_rank=13 price=128.8 support=90.01 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.18 liquidity=243878176.0 spike=0.58
- PHDC.CA: score=20.33 buy_ready=False sector_rank=15 price=15.11 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.56 liquidity=221449104.0 spike=0.89
- PHTV.CA: score=19.51 buy_ready=False sector_rank=14 price=375.0 support=309.09 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.43 liquidity=5181414.5 spike=1.78
- POUL.CA: score=16.4 buy_ready=False sector_rank=10 price=37.0 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=48.36 liquidity=22782050.0 spike=0.89
- PRCL.CA: score=6.39 buy_ready=False sector_rank=12 price=33.39 support=33.01 resistance=35.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10615582.0 spike=0.28
- PRDC.CA: score=13.33 buy_ready=False sector_rank=15 price=9.16 support=8.7 resistance=9.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.15 liquidity=71464032.0 spike=0.81
- PRMH.CA: score=4.25 buy_ready=False sector_rank=14 price=2.42 support=2.4 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8485617.0 spike=0.67
- RACC.CA: score=22.95 buy_ready=False sector_rank=14 price=10.22 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=73.17 liquidity=21372968.0 spike=1.09
- RAKT.CA: score=9.0 buy_ready=False sector_rank=14 price=22.25 support=21.66 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=808473.5 spike=2.71
- RAYA.CA: score=8.48 buy_ready=False sector_rank=20 price=7.03 support=6.97 resistance=7.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.25 liquidity=67427264.0 spike=0.73
- RMDA.CA: score=21.13 buy_ready=False sector_rank=13 price=6.05 support=4.97 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.78 liquidity=38574484.0 spike=0.32
- ROTO.CA: score=5.77 buy_ready=False sector_rank=14 price=48.07 support=48.0 resistance=51.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13830152.0 spike=0.57
- RREI.CA: score=7.67 buy_ready=False sector_rank=14 price=4.56 support=4.52 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=122380480.0 spike=1.95
- RTVC.CA: score=27.77 buy_ready=False sector_rank=14 price=4.15 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.46 liquidity=21190666.0 spike=3.51
- RUBX.CA: score=18.77 buy_ready=False sector_rank=14 price=12.58 support=12.02 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.51 liquidity=18772896.0 spike=0.85
- SAUD.CA: score=25.4 buy_ready=False sector_rank=4 price=24.47 support=21.4 resistance=24.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.73 liquidity=39615968.0 spike=2.0
- SCEM.CA: score=6.39 buy_ready=False sector_rank=12 price=94.4 support=94.0 resistance=104.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=176754688.0 spike=0.85
- SCFM.CA: score=5.77 buy_ready=False sector_rank=14 price=280.0 support=280.0 resistance=297.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26286628.0 spike=0.81
- SCTS.CA: score=19.19 buy_ready=False sector_rank=3 price=621.78 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=4787245.5 spike=0.46
- SDTI.CA: score=21.31 buy_ready=False sector_rank=14 price=68.55 support=47.15 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.51 liquidity=37459812.0 spike=1.27
- SEIG.CA: score=7.75 buy_ready=False sector_rank=14 price=266.48 support=237.7 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.98 liquidity=1984513.63 spike=0.17
- SIPC.CA: score=5.77 buy_ready=False sector_rank=14 price=4.77 support=4.76 resistance=5.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21306522.0 spike=0.33
- SKPC.CA: score=26.4 buy_ready=False sector_rank=5 price=17.6 support=15.61 resistance=17.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.59 liquidity=378107264.0 spike=7.59
- SMFR.CA: score=20.85 buy_ready=False sector_rank=14 price=263.16 support=225.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.28 liquidity=31936610.0 spike=1.04
- SNFC.CA: score=17.85 buy_ready=False sector_rank=14 price=11.1 support=10.6 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=12410985.0 spike=1.04
- SPIN.CA: score=6.4 buy_ready=False sector_rank=6 price=18.9 support=18.4 resistance=20.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34529356.0 spike=0.74
- SPMD.CA: score=18.77 buy_ready=False sector_rank=14 price=0.46 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.24 liquidity=16945414.0 spike=0.5
- SUGR.CA: score=22.76 buy_ready=False sector_rank=10 price=50.73 support=46.47 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=82.64 liquidity=42769016.0 spike=2.18
- SVCE.CA: score=20.77 buy_ready=False sector_rank=14 price=10.73 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=50596192.0 spike=0.51
- SWDY.CA: score=5.06 buy_ready=False sector_rank=19 price=119.0 support=118.11 resistance=129.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108487616.0 spike=1.27
- TALM.CA: score=22.4 buy_ready=False sector_rank=3 price=19.69 support=15.7 resistance=20.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.93 liquidity=16578186.0 spike=0.39
- TMGH.CA: score=15.33 buy_ready=False sector_rank=15 price=96.01 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.93 liquidity=220649792.0 spike=0.7
- TRTO.CA: score=16.34 buy_ready=False sector_rank=14 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16387.96 spike=1.78
- UEFM.CA: score=12.63 buy_ready=False sector_rank=14 price=539.11 support=530.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=47.02 liquidity=3861591.25 spike=0.55
- UEGC.CA: score=5.77 buy_ready=False sector_rank=14 price=2.07 support=2.06 resistance=2.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36574252.0 spike=0.86
- UNIP.CA: score=10.17 buy_ready=False sector_rank=14 price=0.37 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=105085960.0 spike=3.2
- UNIT.CA: score=20.45 buy_ready=False sector_rank=15 price=19.13 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.15 liquidity=14360685.0 spike=1.06
- WCDF.CA: score=11.61 buy_ready=False sector_rank=14 price=644.02 support=550.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.31 liquidity=1840118.63 spike=0.33
- WKOL.CA: score=22.77 buy_ready=False sector_rank=14 price=334.23 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=13309967.0 spike=0.39
- ZEOT.CA: score=22.77 buy_ready=False sector_rank=14 price=13.89 support=11.51 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=74.37 liquidity=12662419.0 spike=0.45
- ZMID.CA: score=8.81 buy_ready=False sector_rank=15 price=7.88 support=7.41 resistance=7.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=622329024.0 spike=2.74

## Backtesting Lite
- IFAP.CA: 180d return=13.45%, max drawdown=-12.94%, MA20>MA50 days last20=11, as_of=2026-08-17T21:00:00+00:00
- RTVC.CA: 180d return=4.47%, max drawdown=-19.33%, MA20>MA50 days last20=17, as_of=2026-08-17T21:00:00+00:00
- MPCO.CA: 180d return=41.87%, max drawdown=-18.29%, MA20>MA50 days last20=20, as_of=2026-08-17T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- IFAP.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=International Agricultural Products summary=International Agricultural Products stock is testing key psychological barrier – Analysis; International Agricultural Products’ non-consolidated net profits hit EGP 12.5m in Q1-25/26; El Dawlia Fertilizers announces new company of EGP 500m authorised capital
  - International Agricultural Products stock is testing key psychological barrier – Analysis: https://english.mubasher.info/news/4560334/International-Agricultural-Products-stock-is-testing-key-psychological-barrier-Analysis/
  - International Agricultural Products’ non-consolidated net profits hit EGP 12.5m in Q1-25/26: https://english.mubasher.info/news/4525080/International-Agricultural-Products-non-consolidated-net-profits-hit-EGP-12-5m-in-Q1-25-26/
  - El Dawlia Fertilizers announces new company of EGP 500m authorised capital: https://english.mubasher.info/news/3971612/El-Dawlia-Fertilizers-announces-new-company-of-EGP-500m-authorised-capital/
- RTVC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Remco Tourism Villages Construction summary=Evidence rejected for RTVC.CA: source text did not clearly match RTVC.CA / Remco Tourism Villages Construction.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=595 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- SKPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sidi Kerir Petrochemicals summary=Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=595 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- EEII.CA: status=OLD_ACCEPTED latest=2019-01-01 age_days=2787 sources=3 expected=Arab Engineering Industries summary=Shareholder cuts stake in Arab Engineering Industries to 9%; Arab Moltaqa cuts stake in Arab Engineering Industries; Lower sales weigh on Arab Engineering Industries’ profit in 2019
  - Shareholder cuts stake in Arab Engineering Industries to 9%: https://english.mubasher.info/news/4009461/Shareholder-cuts-stake-in-Arab-Engineering-Industries-to-9-/
  - Arab Moltaqa cuts stake in Arab Engineering Industries: https://english.mubasher.info/news/3707590/Arab-Moltaqa-cuts-stake-in-Arab-Engineering-Industries/
  - Lower sales weigh on Arab Engineering Industries’ profit in 2019: https://english.mubasher.info/news/3586813/Lower-sales-weigh-on-Arab-Engineering-Industries-profit-in-2019/
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=595 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/

## Warnings
- Evidence for IFAP.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for RTVC.CA: source text did not clearly match RTVC.CA / Remco Tourism Villages Construction.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for SKPC.CA: source text did not clearly match SKPC.CA / Sidi Kerir Petrochemicals.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EEII.CA matches the company but appears old; latest detected date is 2019-01-01.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
