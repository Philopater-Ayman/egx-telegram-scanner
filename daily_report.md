# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-11-10T14:50:06.719745+00:00
Generated Cairo: 2026-11-10 16:50
Run timing: target 09:15 Cairo | generated Cairo 2026-11-10 16:50 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-11-10 16:46

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 165/186
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, November 10
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 88.24% / above MA50 35.29%
- EGX70 regime: BEARISH / above MA20 91.89% / above MA50 27.03%
- Sector breadth: 42.86%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=630253184.0 spike=1.2 score=23.8
- CCAP.CA: liquidity=545932864.0 spike=1.34 score=19.08
- GTWL.CA: liquidity=417450496.0 spike=1.92 score=22.24
- ORAS.CA: liquidity=327562144.0 spike=1.0 score=4.6
- TMGH.CA: liquidity=322396800.0 spike=1.19 score=19.78

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- MAAL.CA: spike=8.93 liquidity=113367688.0 outlook=NEUTRAL score=41.03 buy_ready=False
- CAED.CA: spike=6.21 liquidity=107853424.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ENGC.CA: spike=6.14 liquidity=61778388.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DTPP.CA: spike=5.72 liquidity=177374480.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BINV.CA: spike=5.22 liquidity=44222660.0 outlook=BULLISH_WATCH score=74.07 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=13.08 5d=12.86% 20d=-2.49% aboveMA50=0.0%
- #2 Industrial Goods & Cables: score=11.35 5d=13.18% 20d=3.44% aboveMA50=50.0%
- #3 Healthcare: score=11.14 5d=12.78% 20d=-0.05% aboveMA50=50.0%
- #4 Tourism & Leisure: score=10.33 5d=7.41% 20d=-2.86% aboveMA50=100.0%
- #5 Fintech & Payments: score=10.28 5d=9.25% 20d=-1.96% aboveMA50=50.0%
- #6 Food, Beverages & Tobacco: score=10.21 5d=9.31% 20d=4.17% aboveMA50=14.29%
- #7 Building Materials: score=9.97 5d=10.19% 20d=0.2% aboveMA50=50.0%
- #8 Education: score=9.54 5d=9.06% 20d=-2.77% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ACAMD.CA: BULLISH_WATCH score=97.03 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ACGC.CA: BULLISH_WATCH score=92.65 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MICH.CA: BULLISH_WATCH score=89.03 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- AFMC.CA: BULLISH_WATCH score=89.03 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- KZPC.CA: BULLISH_WATCH score=89.03 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- EFIH.CA: BULLISH_WATCH score=89 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; close to resistance
- SMFR.CA: BULLISH_WATCH score=87.03 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- RMDA.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=far above support; close to resistance
- SDTI.CA: BULLISH_WATCH score=85.03 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SNFC.CA: BULLISH_WATCH score=85.03 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- FERC.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=20.78 buy_ready=False sector_rank=10 price=248.23 support=171.02 resistance=258.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=56.28 liquidity=21002060.0 spike=1.19
- ABUK.CA: score=12.18 buy_ready=False sector_rank=19 price=74.3 support=73.6 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=22.88 liquidity=264399024.0 spike=2.38
- ACAMD.CA: score=24.98 buy_ready=False sector_rank=10 price=2.05 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=94135008.0 spike=1.79
- ACGC.CA: score=30.4 buy_ready=False sector_rank=12 price=13.91 support=11.6 resistance=13.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=55.01 liquidity=33471972.0 spike=4.9
- ADCI.CA: score=13.81 buy_ready=False sector_rank=10 price=271.49 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=2934212.25 spike=1.24
- ADIB.CA: score=24.36 buy_ready=False sector_rank=13 price=50.14 support=43.16 resistance=50.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.31 liquidity=121278912.0 spike=1.48
- ADPC.CA: score=20.86 buy_ready=False sector_rank=10 price=3.2 support=2.53 resistance=3.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=13543687.0 spike=1.73
- AFDI.CA: score=17.14 buy_ready=False sector_rank=10 price=46.58 support=34.8 resistance=51.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=45.88 liquidity=5139532.5 spike=1.8
- AFMC.CA: score=26.88 buy_ready=False sector_rank=10 price=150.13 support=94.6 resistance=148.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.92 liquidity=33829448.0 spike=1.74
- AJWA.CA: score=24.94 buy_ready=False sector_rank=10 price=267.01 support=190.2 resistance=263.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=68.42 liquidity=57146192.0 spike=1.77
- ALCN.CA: score=24.56 buy_ready=False sector_rank=11 price=33.0 support=27.11 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.1 liquidity=18185388.0 spike=1.58
- ALUM.CA: score=11.84 buy_ready=False sector_rank=10 price=21.55 support=16.02 resistance=22.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=52.95 liquidity=2436854.0 spike=0.78
- AMER.CA: score=22.44 buy_ready=False sector_rank=14 price=4.64 support=3.21 resistance=5.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=120889616.0 spike=2.02
- AMES.CA: score=21.66 buy_ready=False sector_rank=10 price=47.59 support=28.0 resistance=53.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=72.9 liquidity=245408080.0 spike=2.13
- AMIA.CA: score=23.2 buy_ready=False sector_rank=10 price=17.96 support=14.0 resistance=19.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=26055340.0 spike=2.4
- AMOC.CA: score=16.07 buy_ready=False sector_rank=18 price=13.01 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=155493792.0 spike=1.11
- APSW.CA: score=11.94 buy_ready=False sector_rank=10 price=7.95 support=7.1 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=42.13 liquidity=861097.0 spike=1.84
- ARAB.CA: score=23.6 buy_ready=False sector_rank=14 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=99935216.0 spike=1.1
- ARCC.CA: score=25.4 buy_ready=False sector_rank=7 price=70.0 support=58.01 resistance=70.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=28131600.0 spike=0.79
- AREH.CA: score=17.12 buy_ready=False sector_rank=10 price=1.16 support=0.91 resistance=1.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7721761.5 spike=1.0
- ASCM.CA: score=19.92 buy_ready=False sector_rank=10 price=49.77 support=38.2 resistance=53.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.94 liquidity=10113722.0 spike=1.26
- ASPI.CA: score=11.4 buy_ready=False sector_rank=10 price=0.35 support=0.33 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75218696.0 spike=3.69
- ATLC.CA: score=20.01 buy_ready=False sector_rank=15 price=5.21 support=3.93 resistance=5.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=9351193.0 spike=1.13
- ATQA.CA: score=19.52 buy_ready=False sector_rank=19 price=10.3 support=8.25 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=43.07 liquidity=51006384.0 spike=1.05
- AXPH.CA: score=5.24 buy_ready=False sector_rank=10 price=1430.3 support=1361.03 resistance=1450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7655874.0 spike=1.59
- BINV.CA: score=18.4 buy_ready=False sector_rank=17 price=55.46 support=50.62 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=33.43 liquidity=44222660.0 spike=5.22
- BIOC.CA: score=25.28 buy_ready=False sector_rank=10 price=386.01 support=212.05 resistance=415.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=68.1 liquidity=236717840.0 spike=1.94
- BTFH.CA: score=19.58 buy_ready=False sector_rank=15 price=2.46 support=2.05 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=131436488.0 spike=1.09
- CAED.CA: score=11.4 buy_ready=False sector_rank=10 price=108.45 support=100.3 resistance=116.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107853424.0 spike=6.21
- CANA.CA: score=23.4 buy_ready=False sector_rank=13 price=48.75 support=38.1 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=67.9 liquidity=17066172.0 spike=0.92
- CCAP.CA: score=19.08 buy_ready=False sector_rank=17 price=6.1 support=5.55 resistance=6.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=545932864.0 spike=1.34
- CCRS.CA: score=10.04 buy_ready=False sector_rank=10 price=2.26 support=2.1 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28008450.0 spike=2.82
- CEFM.CA: score=20.8 buy_ready=False sector_rank=10 price=127.12 support=97.79 resistance=129.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=51.48 liquidity=5520658.0 spike=2.44
- CERA.CA: score=19.56 buy_ready=False sector_rank=10 price=1.17 support=0.93 resistance=1.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=90659904.0 spike=1.08
- CFGH.CA: score=0.87 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=7408.49 spike=1.23
- CICH.CA: score=15.09 buy_ready=False sector_rank=15 price=10.72 support=9.63 resistance=11.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=4154010.5 spike=1.77
- CIEB.CA: score=20.0 buy_ready=False sector_rank=13 price=23.16 support=21.35 resistance=23.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=51.45 liquidity=10712118.0 spike=1.3
- CIRA.CA: score=27.22 buy_ready=False sector_rank=8 price=38.53 support=32.01 resistance=38.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=58.69 liquidity=24349234.0 spike=1.91
- CLHO.CA: score=23.14 buy_ready=False sector_rank=3 price=14.84 support=12.51 resistance=14.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=83267008.0 spike=1.87
- CNFN.CA: score=26.02 buy_ready=False sector_rank=15 price=4.29 support=3.25 resistance=4.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=52.72 liquidity=15402183.0 spike=1.81
- COMI.CA: score=23.8 buy_ready=False sector_rank=13 price=131.0 support=117.41 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.35 liquidity=630253184.0 spike=1.2
- COPR.CA: score=23.62 buy_ready=False sector_rank=10 price=0.44 support=0.33 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=47.69 liquidity=42807212.0 spike=2.61
- COSG.CA: score=20.18 buy_ready=False sector_rank=10 price=1.4 support=1.11 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.77 liquidity=13055461.0 spike=1.39
- CPCI.CA: score=15.66 buy_ready=False sector_rank=10 price=597.27 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=54.15 liquidity=4263226.5 spike=0.85
- CSAG.CA: score=18.19 buy_ready=False sector_rank=11 price=35.67 support=30.1 resistance=37.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=7646286.5 spike=1.07
- DAPH.CA: score=20.4 buy_ready=False sector_rank=10 price=90.8 support=65.2 resistance=103.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.11 liquidity=18999512.0 spike=0.79
- DEIN.CA: score=9.4 buy_ready=False sector_rank=10 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=16.67 buy_ready=False sector_rank=6 price=24.87 support=20.27 resistance=25.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=62.99 liquidity=3646101.0 spike=1.81
- DSCW.CA: score=19.4 buy_ready=False sector_rank=10 price=1.59 support=1.23 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=13522829.0 spike=0.95
- DTPP.CA: score=11.4 buy_ready=False sector_rank=10 price=58.98 support=50.1 resistance=58.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=177374480.0 spike=5.72
- EALR.CA: score=22.96 buy_ready=False sector_rank=10 price=311.48 support=236.01 resistance=324.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=51.19 liquidity=16644171.0 spike=2.78
- EASB.CA: score=22.28 buy_ready=False sector_rank=10 price=6.82 support=5.03 resistance=7.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=12883824.0 spike=1.94
- EAST.CA: score=22.4 buy_ready=False sector_rank=6 price=33.55 support=27.01 resistance=33.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=69.86 liquidity=32002834.0 spike=0.89
- EBSC.CA: score=13.31 buy_ready=False sector_rank=10 price=1.64 support=1.2 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=52.44 liquidity=3891318.75 spike=1.01
- ECAP.CA: score=16.29 buy_ready=False sector_rank=10 price=29.36 support=24.8 resistance=30.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.34 liquidity=5069074.0 spike=1.91
- EDFM.CA: score=14.0 buy_ready=False sector_rank=10 price=371.77 support=312.92 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:03 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=601839.63 spike=0.5
- EEII.CA: score=29.4 buy_ready=False sector_rank=10 price=2.08 support=1.42 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=62.75 liquidity=35525348.0 spike=3.94
- EFIC.CA: score=23.6 buy_ready=False sector_rank=19 price=170.59 support=121.0 resistance=174.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.24 liquidity=30216194.0 spike=1.09
- EFID.CA: score=21.4 buy_ready=False sector_rank=6 price=20.11 support=16.01 resistance=19.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.99 liquidity=35675084.0 spike=0.96
- EFIH.CA: score=26.66 buy_ready=False sector_rank=5 price=24.89 support=20.3 resistance=24.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.05 liquidity=93674360.0 spike=1.63
- EGAL.CA: score=19.8 buy_ready=False sector_rank=19 price=320.81 support=275.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.83 liquidity=125665208.0 spike=1.19
- EGAS.CA: score=12.37 buy_ready=False sector_rank=18 price=49.2 support=43.0 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=43.71 liquidity=2514340.25 spike=0.65
- EGBE.CA: score=7.7 buy_ready=False sector_rank=13 price=0.49 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=98882.66 spike=1.6
- EGCH.CA: score=18.62 buy_ready=False sector_rank=19 price=11.01 support=9.66 resistance=12.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=61255020.0 spike=1.1
- EGSA.CA: score=13.4 buy_ready=False sector_rank=9 price=9.0 support=8.7 resistance=9.09 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=47.54 liquidity=3123.0 spike=0.43
- EGTS.CA: score=20.4 buy_ready=False sector_rank=14 price=13.94 support=10.19 resistance=15.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.65 liquidity=19971168.0 spike=0.99
- EHDR.CA: score=20.4 buy_ready=False sector_rank=10 price=2.23 support=1.8 resistance=2.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=15042551.0 spike=1.5
- ELEC.CA: score=21.4 buy_ready=False sector_rank=2 price=1.77 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.59 liquidity=24559926.0 spike=0.47
- ELKA.CA: score=24.28 buy_ready=False sector_rank=10 price=1.61 support=1.21 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=53.52 liquidity=18698684.0 spike=1.44
- ELNA.CA: score=11.12 buy_ready=False sector_rank=10 price=43.4 support=33.46 resistance=42.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=78.67 liquidity=719941.5 spike=0.99
- ELSH.CA: score=20.68 buy_ready=False sector_rank=10 price=11.45 support=8.57 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.23 liquidity=17611300.0 spike=1.14
- ELWA.CA: score=9.93 buy_ready=False sector_rank=10 price=1.27 support=1.3 resistance=1.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=10.0 liquidity=4532450.5 spike=5.18
- EMFD.CA: score=21.86 buy_ready=False sector_rank=14 price=12.61 support=10.6 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=94111672.0 spike=1.73
- ENGC.CA: score=11.4 buy_ready=False sector_rank=10 price=40.87 support=36.07 resistance=41.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61778388.0 spike=6.14
- EOSB.CA: score=11.42 buy_ready=False sector_rank=10 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=18743.62 spike=0.21
- EPCO.CA: score=17.94 buy_ready=False sector_rank=10 price=9.39 support=7.0 resistance=9.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=5475620.0 spike=1.03
- EPPK.CA: score=-3.18 buy_ready=False sector_rank=10 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.4 buy_ready=False sector_rank=9 price=135.21 support=115.0 resistance=148.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=222050320.0 spike=0.92
- ETRS.CA: score=23.4 buy_ready=False sector_rank=10 price=11.2 support=9.51 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=12101795.0 spike=0.93
- EXPA.CA: score=19.4 buy_ready=False sector_rank=13 price=14.72 support=12.0 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=18193750.0 spike=0.76
- FAIT.CA: score=16.47 buy_ready=False sector_rank=13 price=44.65 support=40.0 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=2874601.25 spike=1.1
- FAITA.CA: score=13.24 buy_ready=False sector_rank=13 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=64854.28 spike=1.89
- FWRY.CA: score=20.74 buy_ready=False sector_rank=5 price=18.17 support=15.27 resistance=18.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=167740528.0 spike=1.67
- GBCO.CA: score=10.28 buy_ready=False sector_rank=20 price=23.5 support=20.9 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=26.27 liquidity=173290112.0 spike=1.51
- GDWA.CA: score=19.66 buy_ready=False sector_rank=10 price=0.58 support=0.46 resistance=0.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.93 liquidity=13727619.0 spike=1.13
- GGCC.CA: score=19.78 buy_ready=False sector_rank=10 price=0.59 support=0.49 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=38.95 liquidity=25325056.0 spike=1.19
- GIHD.CA: score=9.28 buy_ready=False sector_rank=10 price=53.02 support=50.44 resistance=57.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38071748.0 spike=2.44
- GMCI.CA: score=12.13 buy_ready=False sector_rank=10 price=1.55 support=1.34 resistance=1.61 source=Yahoo Finance as_of=2026-11-08T22:00:00+00:00 freshness=FRESH RSI=51.11 liquidity=649811.13 spike=2.04
- GRCA.CA: score=20.04 buy_ready=False sector_rank=10 price=32.88 support=22.57 resistance=34.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=55.74 liquidity=12074420.0 spike=1.32
- GSSC.CA: score=16.43 buy_ready=False sector_rank=10 price=267.44 support=211.52 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.3 liquidity=3273832.25 spike=2.38
- GTWL.CA: score=22.24 buy_ready=False sector_rank=10 price=139.69 support=73.02 resistance=149.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=417450496.0 spike=1.92
- HDBK.CA: score=21.32 buy_ready=False sector_rank=13 price=102.81 support=83.01 resistance=105.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=46623716.0 spike=1.96
- HELI.CA: score=21.4 buy_ready=False sector_rank=14 price=6.99 support=5.72 resistance=7.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.87 liquidity=112511888.0 spike=1.5
- HRHO.CA: score=11.4 buy_ready=False sector_rank=15 price=26.0 support=24.0 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=210306336.0 spike=4.2
- ICID.CA: score=14.92 buy_ready=False sector_rank=10 price=17.37 support=14.26 resistance=18.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=49.86 liquidity=4519413.0 spike=0.9
- IDRE.CA: score=9.56 buy_ready=False sector_rank=10 price=44.0 support=40.69 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15161395.0 spike=2.58
- IFAP.CA: score=14.7 buy_ready=False sector_rank=16 price=17.63 support=15.12 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=46.85 liquidity=5296557.0 spike=0.77
- INFI.CA: score=20.64 buy_ready=False sector_rank=10 price=126.11 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.66 liquidity=23823012.0 spike=1.12
- IRON.CA: score=7.98 buy_ready=False sector_rank=19 price=24.7 support=23.13 resistance=28.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=6567091.0 spike=0.75
- ISMA.CA: score=23.22 buy_ready=False sector_rank=10 price=21.98 support=14.11 resistance=24.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.74 liquidity=27738222.0 spike=2.91
- ISMQ.CA: score=18.42 buy_ready=False sector_rank=19 price=7.59 support=5.96 resistance=7.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=10563510.0 spike=0.79
- ISPH.CA: score=20.6 buy_ready=False sector_rank=3 price=10.62 support=9.02 resistance=11.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.91 liquidity=66646200.0 spike=1.1
- JUFO.CA: score=21.92 buy_ready=False sector_rank=6 price=24.93 support=21.01 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=28013092.0 spike=1.26
- KABO.CA: score=22.86 buy_ready=False sector_rank=12 price=7.37 support=5.58 resistance=8.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=41819676.0 spike=2.23
- KWIN.CA: score=18.56 buy_ready=False sector_rank=10 price=72.82 support=44.02 resistance=76.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=55.47 liquidity=9080546.0 spike=1.04
- KZPC.CA: score=26.46 buy_ready=False sector_rank=10 price=14.2 support=11.56 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=14671828.0 spike=1.53
- LCSW.CA: score=21.44 buy_ready=False sector_rank=7 price=38.89 support=28.0 resistance=39.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=67.91 liquidity=22610664.0 spike=1.02
- LUTS.CA: score=20.46 buy_ready=False sector_rank=10 price=0.78 support=0.47 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=56.4 liquidity=64081456.0 spike=1.03
- MAAL.CA: score=23.4 buy_ready=False sector_rank=10 price=7.1 support=4.88 resistance=10.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.52 liquidity=113367688.0 spike=8.93
- MASR.CA: score=20.98 buy_ready=False sector_rank=10 price=7.03 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=52659936.0 spike=1.29
- MBSC.CA: score=20.4 buy_ready=False sector_rank=7 price=341.61 support=262.0 resistance=400.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=49.79 liquidity=33242918.0 spike=0.52
- MCQE.CA: score=19.4 buy_ready=False sector_rank=7 price=183.84 support=144.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=41849724.0 spike=0.78
- MCRO.CA: score=24.2 buy_ready=False sector_rank=10 price=1.41 support=1.07 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=124023408.0 spike=2.9
- MENA.CA: score=14.63 buy_ready=False sector_rank=14 price=6.07 support=5.45 resistance=6.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=46.56 liquidity=4086305.0 spike=1.07
- MEPA.CA: score=7.7 buy_ready=False sector_rank=10 price=1.47 support=1.42 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26637014.0 spike=1.65
- MFPC.CA: score=11.86 buy_ready=False sector_rank=19 price=38.14 support=37.23 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=28.34 liquidity=161155600.0 spike=2.22
- MFSC.CA: score=13.87 buy_ready=False sector_rank=10 price=37.5 support=28.55 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=45.66 liquidity=3327358.75 spike=1.57
- MHOT.CA: score=20.24 buy_ready=False sector_rank=4 price=16.18 support=13.0 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=51.63 liquidity=7257657.0 spike=1.29
- MICH.CA: score=27.94 buy_ready=False sector_rank=10 price=45.12 support=35.5 resistance=44.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.46 liquidity=14774463.0 spike=2.27
- MILS.CA: score=21.82 buy_ready=False sector_rank=10 price=151.93 support=94.24 resistance=171.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=49.6 liquidity=14865653.0 spike=1.71
- MIPH.CA: score=15.32 buy_ready=False sector_rank=3 price=804.55 support=610.0 resistance=810.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=921782.88 spike=0.28
- MOED.CA: score=19.86 buy_ready=False sector_rank=10 price=0.52 support=0.39 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.45 liquidity=17091590.0 spike=1.23
- MOIL.CA: score=13.58 buy_ready=False sector_rank=18 price=0.67 support=0.6 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=406677.59 spike=2.66
- MOIN.CA: score=23.56 buy_ready=False sector_rank=10 price=32.86 support=25.7 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=19561496.0 spike=2.58
- MOSC.CA: score=25.4 buy_ready=False sector_rank=10 price=276.5 support=198.01 resistance=286.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=52.26 liquidity=16879070.0 spike=3.77
- MPCI.CA: score=22.4 buy_ready=False sector_rank=10 price=341.01 support=238.6 resistance=347.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=88603584.0 spike=0.83
- MPCO.CA: score=8.76 buy_ready=False sector_rank=16 price=2.24 support=2.04 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=190484496.0 spike=2.18
- MPRC.CA: score=23.84 buy_ready=False sector_rank=10 price=38.95 support=27.0 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=56.85 liquidity=23559748.0 spike=1.22
- MTIE.CA: score=10.26 buy_ready=False sector_rank=20 price=7.48 support=7.19 resistance=7.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75576448.0 spike=3.71
- NAHO.CA: score=-3.59 buy_ready=False sector_rank=10 price=0.13 support=0.13 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6041.12 spike=0.35
- NCCW.CA: score=8.56 buy_ready=False sector_rank=10 price=6.02 support=5.69 resistance=6.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33751676.0 spike=2.08
- NEDA.CA: score=3.13 buy_ready=False sector_rank=10 price=2.46 support=2.26 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:51 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=366377.72 spike=2.18
- NHPS.CA: score=17.44 buy_ready=False sector_rank=10 price=64.89 support=50.0 resistance=69.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=7977449.5 spike=1.03
- NINH.CA: score=18.26 buy_ready=False sector_rank=10 price=17.08 support=12.36 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.27 liquidity=7858356.0 spike=0.69
- NIPH.CA: score=26.4 buy_ready=False sector_rank=3 price=305.54 support=205.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=108063440.0 spike=0.74
- OBRI.CA: score=19.88 buy_ready=False sector_rank=10 price=25.78 support=18.11 resistance=27.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=11740445.0 spike=1.24
- OCDI.CA: score=7.98 buy_ready=False sector_rank=14 price=26.4 support=25.5 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=59049520.0 spike=1.79
- OCPH.CA: score=14.78 buy_ready=False sector_rank=10 price=205.79 support=147.96 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=55.25 liquidity=5141761.5 spike=1.12
- ODIN.CA: score=21.74 buy_ready=False sector_rank=10 price=2.23 support=1.7 resistance=2.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=12475325.0 spike=1.67
- OFH.CA: score=7.52 buy_ready=False sector_rank=10 price=0.79 support=0.76 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33224346.0 spike=1.56
- OIH.CA: score=20.96 buy_ready=False sector_rank=17 price=1.79 support=1.5 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=58004780.0 spike=1.28
- OLFI.CA: score=20.94 buy_ready=False sector_rank=6 price=21.01 support=17.86 resistance=20.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=13773160.0 spike=1.77
- ORAS.CA: score=4.6 buy_ready=False sector_rank=21 price=817.82 support=797.0 resistance=833.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=327562144.0 spike=1.0
- ORHD.CA: score=19.98 buy_ready=False sector_rank=14 price=10.55 support=8.5 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.67 liquidity=148194624.0 spike=1.29
- ORWE.CA: score=20.4 buy_ready=False sector_rank=12 price=26.23 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.15 liquidity=32185798.0 spike=0.92
- PHAR.CA: score=24.48 buy_ready=False sector_rank=3 price=110.14 support=90.2 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=91864088.0 spike=1.54
- PHDC.CA: score=19.4 buy_ready=False sector_rank=14 price=12.12 support=10.33 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.04 liquidity=82426408.0 spike=0.68
- PHTV.CA: score=10.94 buy_ready=False sector_rank=10 price=331.14 support=300.0 resistance=343.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=49.96 liquidity=541632.06 spike=0.39
- POUL.CA: score=22.9 buy_ready=False sector_rank=6 price=10.28 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=244397808.0 spike=2.75
- PRCL.CA: score=20.74 buy_ready=False sector_rank=7 price=22.38 support=16.65 resistance=24.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=28394732.0 spike=1.67
- PRDC.CA: score=10.32 buy_ready=False sector_rank=14 price=7.04 support=6.5 resistance=7.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56314488.0 spike=2.96
- PRMH.CA: score=23.82 buy_ready=False sector_rank=10 price=2.24 support=1.7 resistance=2.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=61.39 liquidity=10953273.0 spike=2.21
- RACC.CA: score=21.4 buy_ready=False sector_rank=10 price=8.29 support=6.1 resistance=9.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.13 liquidity=12506314.0 spike=2.0
- RAKT.CA: score=8.66 buy_ready=False sector_rank=10 price=22.33 support=20.4 resistance=23.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:06 PM market time freshness=DELAYED_CURRENT RSI=53.99 liquidity=377070.63 spike=1.44
- RAYA.CA: score=27.4 buy_ready=False sector_rank=1 price=6.16 support=5.02 resistance=6.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.21 liquidity=79558160.0 spike=3.62
- RMDA.CA: score=26.4 buy_ready=False sector_rank=3 price=5.62 support=4.5 resistance=5.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=29487428.0 spike=0.95
- ROTO.CA: score=17.54 buy_ready=False sector_rank=10 price=34.55 support=25.0 resistance=39.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=8140991.5 spike=0.86
- RREI.CA: score=20.1 buy_ready=False sector_rank=10 price=2.96 support=1.96 resistance=3.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.52 liquidity=14953049.0 spike=1.35
- RTVC.CA: score=9.42 buy_ready=False sector_rank=10 price=3.0 support=2.66 resistance=3.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:49 PM market time freshness=DELAYED_CURRENT RSI=29.13 liquidity=5059232.5 spike=1.98
- RUBX.CA: score=7.02 buy_ready=False sector_rank=10 price=13.99 support=13.47 resistance=14.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83298104.0 spike=1.31
- SAUD.CA: score=23.48 buy_ready=False sector_rank=13 price=22.02 support=19.3 resistance=23.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=58.22 liquidity=23384058.0 spike=1.54
- SCEM.CA: score=25.62 buy_ready=False sector_rank=7 price=99.03 support=73.9 resistance=98.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=63.65 liquidity=50666072.0 spike=1.11
- SCFM.CA: score=18.62 buy_ready=False sector_rank=10 price=225.23 support=153.02 resistance=244.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=48.75 liquidity=6218413.5 spike=2.5
- SCTS.CA: score=14.63 buy_ready=False sector_rank=8 price=509.15 support=410.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=54.96 liquidity=4234994.0 spike=0.72
- SDTI.CA: score=26.94 buy_ready=False sector_rank=10 price=87.11 support=75.01 resistance=89.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.98 liquidity=49017996.0 spike=2.77
- SEIG.CA: score=24.68 buy_ready=False sector_rank=10 price=235.56 support=142.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=56.09 liquidity=14696752.0 spike=1.64
- SIPC.CA: score=23.4 buy_ready=False sector_rank=10 price=5.51 support=3.73 resistance=6.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.68 liquidity=42450356.0 spike=0.85
- SKPC.CA: score=18.42 buy_ready=False sector_rank=19 price=15.2 support=14.01 resistance=15.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.85 liquidity=34119336.0 spike=0.79
- SMFR.CA: score=28.4 buy_ready=False sector_rank=10 price=232.05 support=165.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=27516312.0 spike=4.39
- SNFC.CA: score=25.64 buy_ready=False sector_rank=10 price=11.21 support=10.08 resistance=11.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=49.55 liquidity=17912926.0 spike=2.12
- SPIN.CA: score=16.11 buy_ready=False sector_rank=12 price=15.92 support=12.0 resistance=15.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=56.75 liquidity=5712702.0 spike=0.94
- SPMD.CA: score=19.48 buy_ready=False sector_rank=10 price=0.36 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.16 liquidity=18009018.0 spike=1.04
- SUGR.CA: score=13.06 buy_ready=False sector_rank=6 price=47.53 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.39 liquidity=19732370.0 spike=1.83
- SVCE.CA: score=23.8 buy_ready=False sector_rank=10 price=9.45 support=7.01 resistance=9.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.88 liquidity=85476264.0 spike=1.7
- SWDY.CA: score=27.4 buy_ready=False sector_rank=2 price=121.9 support=97.0 resistance=121.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=62.81 liquidity=41367572.0 spike=0.72
- TALM.CA: score=23.4 buy_ready=False sector_rank=8 price=20.81 support=17.0 resistance=22.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.65 liquidity=20113240.0 spike=0.98
- TMGH.CA: score=19.78 buy_ready=False sector_rank=14 price=86.0 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.48 liquidity=322396800.0 spike=1.19
- TRTO.CA: score=2.01 buy_ready=False sector_rank=10 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:08 PM market time freshness=DELAYED_CURRENT RSI=23.08 liquidity=6085.47 spike=1.3
- UEFM.CA: score=16.21 buy_ready=False sector_rank=10 price=497.44 support=422.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=51.49 liquidity=2125219.25 spike=1.34
- UEGC.CA: score=19.4 buy_ready=False sector_rank=10 price=1.57 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=48.75 liquidity=24241928.0 spike=0.5
- UNIP.CA: score=7.6 buy_ready=False sector_rank=10 price=0.33 support=0.31 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11675473.0 spike=1.6
- UNIT.CA: score=16.92 buy_ready=False sector_rank=14 price=18.44 support=15.06 resistance=18.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=63.25 liquidity=1516007.0 spike=0.73
- WCDF.CA: score=11.61 buy_ready=False sector_rank=10 price=535.62 support=432.5 resistance=599.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=63.54 liquidity=1209640.38 spike=0.75
- WKOL.CA: score=11.31 buy_ready=False sector_rank=10 price=179.35 support=145.33 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=22.96 liquidity=8910362.0 spike=0.78
- ZEOT.CA: score=20.52 buy_ready=False sector_rank=10 price=11.81 support=7.9 resistance=12.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.36 liquidity=9877872.0 spike=1.12
- ZMID.CA: score=22.74 buy_ready=False sector_rank=14 price=7.14 support=5.91 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=170978896.0 spike=2.17

## Backtesting Lite
- ACGC.CA: 180d return=66.75%, max drawdown=-21.17%, MA20>MA50 days last20=6, as_of=2026-11-08T22:00:00+00:00
- EEII.CA: 180d return=6.0%, max drawdown=-53.23%, MA20>MA50 days last20=0, as_of=2026-11-08T22:00:00+00:00
- SMFR.CA: 180d return=28.65%, max drawdown=-38.43%, MA20>MA50 days last20=0, as_of=2026-11-08T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ACGC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Cotton Ginning summary=Arab Cotton Ginning’s stock nears significant resistance level; Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24; Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24
  - Arab Cotton Ginning’s stock nears significant resistance level: https://english.mubasher.info/news/4549011/Arab-Cotton-Ginning-s-stock-nears-significant-resistance-level/
  - Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24: https://english.mubasher.info/news/4302757/Arab-Cotton-Ginning-s-standalone-profit-grows-142-YoY-in-9M-23-24/
  - Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24: https://english.mubasher.info/news/4279332/Arab-Cotton-Ginning-s-consolidated-profit-leaps-371-YoY-in-H1-23-24/
- EEII.CA: status=OLD_ACCEPTED latest=2019-01-01 age_days=2870 sources=3 expected=Arab Engineering Industries summary=Shareholder cuts stake in Arab Engineering Industries to 9%; Arab Moltaqa cuts stake in Arab Engineering Industries; Lower sales weigh on Arab Engineering Industries’ profit in 2019
  - Shareholder cuts stake in Arab Engineering Industries to 9%: https://english.mubasher.info/news/4009461/Shareholder-cuts-stake-in-Arab-Engineering-Industries-to-9-/
  - Arab Moltaqa cuts stake in Arab Engineering Industries: https://english.mubasher.info/news/3707590/Arab-Moltaqa-cuts-stake-in-Arab-Engineering-Industries/
  - Lower sales weigh on Arab Engineering Industries’ profit in 2019: https://english.mubasher.info/news/3586813/Lower-sales-weigh-on-Arab-Engineering-Industries-profit-in-2019/
- SMFR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Samad Misr EGYFERT.S.A.E summary=Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- MICH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Chemical Industries Co. summary=Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26; Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis; Misr Chemical Industries posts 10% decrease in H1-25/26 net profits
  - Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26: https://english.mubasher.info/news/4597505/Misr-Chemical-Industries-net-profits-decline-to-EGP-397m-in-9M-25-26/
  - Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis: https://english.mubasher.info/news/4586207/Surpassing-Misr-Chemical-stock-s-current-levels-would-lead-to-historical-levels-Analysis/
  - Misr Chemical Industries posts 10% decrease in H1-25/26 net profits: https://english.mubasher.info/news/4554378/Misr-Chemical-Industries-posts-10-decrease-in-H1-25-26-net-profits/
- SWDY.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Elsewedy Electric summary=Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project; Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26; Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations
  - Elsewedy-Sinohydro JV signs contract for Rabigh 2 IPP expansion project: https://english.mubasher.info/news/4684693/Elsewedy-Sinohydro-JV-signs-contract-for-Rabigh-2-IPP-expansion-project/
  - Elsewedy Electric’s consolidated revenues total EGP 75.2bn in Q1-26: https://english.mubasher.info/news/4614341/Elsewedy-Electric-s-consolidated-revenues-total-EGP-75-2bn-in-Q1-26/
  - Elsewedy Electric accelerates power transformation project in KSA with 6 high-voltage substations: https://english.mubasher.info/news/4593166/Elsewedy-Electric-accelerates-power-transformation-project-in-KSA-with-6-high-voltage-substations/
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=678 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- SDTI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=SHARM DREAMS Co. for Touristic Investment S.A.E summary=Sharm Dreams stock maintains strong uptrend - Analysis; Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis; Sharm Dreams stock hits historic level halting driving buying force
  - Sharm Dreams stock maintains strong uptrend - Analysis: https://english.mubasher.info/news/4577977/Sharm-Dreams-stock-maintains-strong-uptrend-Analysis/
  - Sharm Dreams stock is experiencing sideways movement amid anticipation of next trend – Analysis: https://english.mubasher.info/news/4547831/Sharm-Dreams-stock-is-experiencing-sideways-movement-amid-anticipation-of-next-trend-Analysis/
  - Sharm Dreams stock hits historic level halting driving buying force: https://english.mubasher.info/news/4529096/Sharm-Dreams-stock-hits-historic-level-halting-driving-buying-force/

## Warnings
- OpenRouter API error: 404
- Evidence for ACGC.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for EEII.CA matches the company but appears old; latest detected date is 2019-01-01.
- Evidence rejected for SMFR.CA: source text did not clearly match SMFR.CA / Samad Misr EGYFERT.S.A.E.
- Evidence for MICH.CA matches the company but no source/report date was detected.
- Evidence for SWDY.CA matches the company but no source/report date was detected.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence for SDTI.CA matches the company but no source/report date was detected.
