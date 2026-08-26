# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-08-26T06:08:06.446545+00:00
Generated Cairo: 2026-08-26 09:08
Run timing: target 08:45 Cairo | generated Cairo 2026-08-26 09:08 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-26 09:03

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 172/189
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, August 25
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 70.0% / above MA50 75.0%
- EGX70 regime: MIXED / above MA20 51.28% / above MA50 66.67%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=1027575808.0 spike=2.41 score=24.22
- CCAP.CA: liquidity=625838016.0 spike=0.94 score=24.4
- LUTS.CA: liquidity=562408448.0 spike=3.1 score=9.99
- ORAS.CA: liquidity=536636608.0 spike=1.0 score=4.6
- GTWL.CA: liquidity=515080896.0 spike=1.0 score=14.79

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30/EGX70 remain mixed with weak sector breadth (14.29%), keeping risk mode defensive and blocking new buys; scanner flags several accumulation‑spike stocks but marks them HOLD due to overheated RSI, sector lag, or proximity to resistance.
- Tickets were prioritized by highest rank_score and liquidity accumulation spikes, showing constructive or bullish‑watch outlooks despite the overall weak breadth.
- Liquidity spikes suggest short‑term accumulation, but support/resistance distances (e.g., CCRS.CA near resistance, ALUM.CA far above support) imply limited upside and possible pullback over the next 1‑3 days.
- Leading sectors (Investment Holding, Agriculture & Food, Textiles) show strong MA alignment, yet low overall breadth means even these stocks face headwinds from the defensive market regime.
- EGX30/EGX70 mixed trend and defensive risk mode override individual bullish signals, maintaining a HOLD stance with uncertainty about near‑term direction.

## Top Liquidity Spikes
- EBSC.CA: spike=9.61 liquidity=53502448.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CCRS.CA: spike=8.52 liquidity=249452464.0 outlook=CONSTRUCTIVE score=66.48 buy_ready=False
- NINH.CA: spike=6.86 liquidity=221071616.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EAST.CA: spike=6.26 liquidity=321316480.0 outlook=WEAK_OR_RISKY score=33.16 buy_ready=False
- EOSB.CA: spike=5.39 liquidity=300617.33 outlook=CONSTRUCTIVE score=59.48 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=11.29 5d=6.53% 20d=6.33% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=10.58 5d=2.27% 20d=12.71% aboveMA50=100.0%
- #3 Textiles: score=9.7 5d=-1.27% 20d=15.95% aboveMA50=100.0%
- #4 Building Materials: score=9.07 5d=-2.52% 20d=21.3% aboveMA50=100.0%
- #5 Transportation & Logistics: score=7.89 5d=-0.73% 20d=16.23% aboveMA50=100.0%
- #6 Healthcare: score=7.76 5d=-0.84% 20d=13.41% aboveMA50=100.0%
- #7 Industrial Goods & Cables: score=7.0 5d=-0.62% 20d=12.86% aboveMA50=50.0%
- #8 Banking & Financials: score=6.9 5d=-0.79% 20d=4.84% aboveMA50=90.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CLHO.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- IFAP.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- BINV.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- RUBX.CA: BULLISH_WATCH score=88.48 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- KABO.CA: BULLISH_WATCH score=86.7 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- RTVC.CA: BULLISH_WATCH score=84.48 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- COMI.CA: BULLISH_WATCH score=82.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- EMFD.CA: BULLISH_WATCH score=80.51 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; close to resistance; sector is not leading
- PRDC.CA: BULLISH_WATCH score=80.51 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- NHPS.CA: BULLISH_WATCH score=78.48 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=22.79 buy_ready=False sector_rank=12 price=315.93 support=236.15 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.48 liquidity=25253380.0 spike=0.41
- ABUK.CA: score=21.38 buy_ready=False sector_rank=9 price=76.23 support=70.88 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.75 liquidity=44847804.0 spike=0.42
- ACAMD.CA: score=12.55 buy_ready=False sector_rank=12 price=2.08 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=23.46 liquidity=106544040.0 spike=1.88
- ACGC.CA: score=21.98 buy_ready=False sector_rank=3 price=14.12 support=10.12 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=79.8 liquidity=61106560.0 spike=1.29
- ADCI.CA: score=13.45 buy_ready=False sector_rank=12 price=292.58 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=2661764.0 spike=0.13
- ADIB.CA: score=19.4 buy_ready=False sector_rank=8 price=53.58 support=50.1 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=26145106.0 spike=0.32
- ADPC.CA: score=15.79 buy_ready=False sector_rank=12 price=3.85 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.51 liquidity=25970290.0 spike=0.51
- AFDI.CA: score=10.73 buy_ready=False sector_rank=12 price=58.82 support=58.11 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86954640.0 spike=3.47
- AFMC.CA: score=20.79 buy_ready=False sector_rank=12 price=228.02 support=124.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=59.83 liquidity=35307304.0 spike=0.21
- AJWA.CA: score=15.79 buy_ready=False sector_rank=12 price=180.97 support=180.01 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=18810070.0 spike=0.39
- ALCN.CA: score=18.79 buy_ready=False sector_rank=5 price=30.63 support=28.8 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=9389099.0 spike=0.37
- ALUM.CA: score=27.15 buy_ready=False sector_rank=12 price=29.11 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=70131784.0 spike=3.18
- AMER.CA: score=18.8 buy_ready=False sector_rank=11 price=5.78 support=4.44 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.97 liquidity=31420846.0 spike=0.34
- AMES.CA: score=17.79 buy_ready=False sector_rank=12 price=147.22 support=110.54 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.79 liquidity=58402212.0 spike=0.79
- AMIA.CA: score=19.99 buy_ready=False sector_rank=12 price=19.63 support=10.35 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=96.74 liquidity=54149912.0 spike=1.1
- AMOC.CA: score=17.69 buy_ready=False sector_rank=14 price=10.93 support=8.23 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=76.88 liquidity=152156336.0 spike=1.09
- APSW.CA: score=5.88 buy_ready=False sector_rank=12 price=8.58 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=43.7 liquidity=1091964.38 spike=0.67
- ARAB.CA: score=19.4 buy_ready=False sector_rank=11 price=0.25 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=65.85 liquidity=106562768.0 spike=1.3
- ARCC.CA: score=18.4 buy_ready=False sector_rank=4 price=76.48 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.51 liquidity=69490032.0 spike=0.7
- AREH.CA: score=10.07 buy_ready=False sector_rank=12 price=1.46 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=25.81 liquidity=9274226.0 spike=0.3
- ARVA.CA: score=5.79 buy_ready=False sector_rank=12 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=13.79 buy_ready=False sector_rank=12 price=63.0 support=61.0 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=20.84 liquidity=19539262.0 spike=0.36
- ASPI.CA: score=20.79 buy_ready=False sector_rank=12 price=0.51 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.07 liquidity=19358894.0 spike=0.47
- ATLC.CA: score=15.58 buy_ready=False sector_rank=19 price=5.44 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=6016194.0 spike=0.3
- ATQA.CA: score=18.58 buy_ready=False sector_rank=9 price=11.33 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=90159168.0 spike=1.1
- AXPH.CA: score=14.34 buy_ready=False sector_rank=12 price=1551.61 support=1121.56 resistance=1630.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=81.95 liquidity=6547354.0 spike=0.79
- BINV.CA: score=16.92 buy_ready=False sector_rank=1 price=48.7 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=2515149.0 spike=0.4
- BIOC.CA: score=20.79 buy_ready=False sector_rank=12 price=450.65 support=142.5 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=55.1 liquidity=67010476.0 spike=0.27
- BTFH.CA: score=8.56 buy_ready=False sector_rank=19 price=2.95 support=2.96 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=69287424.0 spike=0.33
- CAED.CA: score=20.79 buy_ready=False sector_rank=12 price=152.29 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=71.12 liquidity=43428180.0 spike=0.83
- CANA.CA: score=15.24 buy_ready=False sector_rank=8 price=41.71 support=36.62 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:09 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=3839626.25 spike=0.19
- CCAP.CA: score=24.4 buy_ready=False sector_rank=1 price=5.78 support=5.14 resistance=5.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.72 liquidity=625838016.0 spike=0.94
- CCRS.CA: score=27.79 buy_ready=False sector_rank=12 price=2.83 support=2.4 resistance=2.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=249452464.0 spike=8.52
- CEFM.CA: score=20.69 buy_ready=False sector_rank=12 price=145.89 support=122.1 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.21 liquidity=7900786.5 spike=0.24
- CERA.CA: score=12.17 buy_ready=False sector_rank=12 price=1.28 support=1.23 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=6374714.0 spike=0.41
- CFGH.CA: score=-4.2 buy_ready=False sector_rank=12 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11395.81 spike=0.55
- CICH.CA: score=9.22 buy_ready=False sector_rank=19 price=12.19 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=37.18 liquidity=4660313.5 spike=0.65
- CIEB.CA: score=23.4 buy_ready=False sector_rank=8 price=24.99 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=57.91 liquidity=10633906.0 spike=0.83
- CIRA.CA: score=18.75 buy_ready=False sector_rank=13 price=35.49 support=33.56 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=52.58 liquidity=16902446.0 spike=0.33
- CLHO.CA: score=24.14 buy_ready=False sector_rank=6 price=17.54 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.24 liquidity=136305936.0 spike=2.37
- CNFN.CA: score=14.56 buy_ready=False sector_rank=19 price=4.81 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=11779260.0 spike=0.59
- COMI.CA: score=24.22 buy_ready=False sector_rank=8 price=140.92 support=135.35 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=46.78 liquidity=1027575808.0 spike=2.41
- COPR.CA: score=20.93 buy_ready=False sector_rank=12 price=0.54 support=0.39 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.69 liquidity=92951344.0 spike=1.07
- COSG.CA: score=21.79 buy_ready=False sector_rank=12 price=1.8 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=76964416.0 spike=1.5
- CPCI.CA: score=10.81 buy_ready=False sector_rank=12 price=540.32 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=69.71 liquidity=2016266.75 spike=0.24
- CSAG.CA: score=13.51 buy_ready=False sector_rank=5 price=40.23 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=75.25 liquidity=5106344.5 spike=0.21
- DAPH.CA: score=18.79 buy_ready=False sector_rank=12 price=110.0 support=92.1 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=58.15 liquidity=25946954.0 spike=0.66
- DEIN.CA: score=-4.21 buy_ready=False sector_rank=12 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=7.81 buy_ready=False sector_rank=17 price=27.88 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=28.54 liquidity=4948891.0 spike=0.32
- DSCW.CA: score=15.79 buy_ready=False sector_rank=12 price=1.88 support=1.86 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=37857532.0 spike=0.42
- DTPP.CA: score=18.79 buy_ready=False sector_rank=12 price=297.18 support=235.59 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.08 liquidity=30216548.0 spike=0.56
- EALR.CA: score=22.79 buy_ready=False sector_rank=12 price=402.8 support=363.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.64 liquidity=10245576.0 spike=0.21
- EASB.CA: score=10.57 buy_ready=False sector_rank=12 price=8.17 support=7.27 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25814376.0 spike=3.39
- EAST.CA: score=20.86 buy_ready=False sector_rank=17 price=35.4 support=35.8 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.29 liquidity=321316480.0 spike=6.26
- EBSC.CA: score=10.79 buy_ready=False sector_rank=12 price=2.14 support=1.91 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53502448.0 spike=9.61
- ECAP.CA: score=10.79 buy_ready=False sector_rank=12 price=33.9 support=33.51 resistance=36.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44359236.0 spike=3.65
- EDFM.CA: score=11.62 buy_ready=False sector_rank=12 price=403.82 support=375.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=56.63 liquidity=825386.13 spike=0.26
- EEII.CA: score=20.79 buy_ready=False sector_rank=12 price=2.89 support=2.54 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=60.45 liquidity=19002208.0 spike=0.73
- EFIC.CA: score=18.54 buy_ready=False sector_rank=9 price=200.0 support=184.0 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=62.37 liquidity=50417804.0 spike=1.08
- EFID.CA: score=19.86 buy_ready=False sector_rank=17 price=31.79 support=26.64 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=69.44 liquidity=31645714.0 spike=0.35
- EFIH.CA: score=18.47 buy_ready=False sector_rank=15 price=23.49 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.73 liquidity=79021096.0 spike=0.68
- EGAL.CA: score=23.44 buy_ready=False sector_rank=9 price=350.29 support=292.0 resistance=359.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=81.16 liquidity=272225504.0 spike=2.53
- EGAS.CA: score=12.42 buy_ready=False sector_rank=14 price=57.51 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=43.54 liquidity=3908567.75 spike=0.16
- EGBE.CA: score=11.45 buy_ready=False sector_rank=8 price=0.54 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.68 liquidity=45167.2 spike=0.22
- EGCH.CA: score=11.38 buy_ready=False sector_rank=9 price=13.35 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=33.53 liquidity=72598144.0 spike=0.58
- EGSA.CA: score=0.87 buy_ready=False sector_rank=10 price=8.69 support=8.65 resistance=9.0 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=28.0 liquidity=2693.9 spike=0.27
- EGTS.CA: score=15.8 buy_ready=False sector_rank=11 price=16.84 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=21028010.0 spike=0.59
- EHDR.CA: score=18.79 buy_ready=False sector_rank=12 price=2.9 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.83 liquidity=20802978.0 spike=0.53
- EKHO.CA: score=6.51 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=10.4 buy_ready=False sector_rank=7 price=2.06 support=2.06 resistance=2.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=52134368.0 spike=0.94
- ELKA.CA: score=18.79 buy_ready=False sector_rank=12 price=1.71 support=1.69 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.0 liquidity=23216260.0 spike=0.35
- ELNA.CA: score=4.85 buy_ready=False sector_rank=12 price=37.01 support=36.1 resistance=39.24 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=44.41 liquidity=58845.9 spike=0.16
- ELSH.CA: score=10.79 buy_ready=False sector_rank=12 price=13.03 support=12.97 resistance=15.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=13150762.0 spike=0.18
- ELWA.CA: score=19.87 buy_ready=False sector_rank=12 price=1.83 support=1.62 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=5714727.5 spike=3.18
- EMFD.CA: score=24.2 buy_ready=False sector_rank=11 price=12.19 support=11.08 resistance=12.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=69.54 liquidity=129931608.0 spike=1.7
- ENGC.CA: score=18.07 buy_ready=False sector_rank=12 price=45.92 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.63 liquidity=9277697.0 spike=0.33
- EOSB.CA: score=18.09 buy_ready=False sector_rank=12 price=1.57 support=1.5 resistance=1.62 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=300617.33 spike=5.39
- EPCO.CA: score=18.79 buy_ready=False sector_rank=12 price=11.05 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=18726116.0 spike=0.8
- EPPK.CA: score=1.49 buy_ready=False sector_rank=12 price=13.07 support=12.3 resistance=15.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 12:59 PM market time freshness=DELAYED_CURRENT RSI=33.64 liquidity=696374.81 spike=0.78
- ETEL.CA: score=22.87 buy_ready=False sector_rank=10 price=116.16 support=102.75 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.2 liquidity=61224324.0 spike=0.45
- ETRS.CA: score=18.15 buy_ready=False sector_rank=12 price=10.87 support=10.21 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=62.64 liquidity=7359645.5 spike=0.23
- EXPA.CA: score=19.4 buy_ready=False sector_rank=8 price=20.01 support=19.7 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.13 liquidity=32819760.0 spike=0.86
- FAIT.CA: score=13.73 buy_ready=False sector_rank=8 price=41.68 support=36.1 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=71.51 liquidity=2333016.5 spike=0.53
- FAITA.CA: score=13.44 buy_ready=False sector_rank=8 price=0.99 support=0.97 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=42016.46 spike=0.83
- FERC.CA: score=20.38 buy_ready=False sector_rank=9 price=78.29 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.64 liquidity=11840049.0 spike=0.65
- FWRY.CA: score=20.81 buy_ready=False sector_rank=15 price=18.85 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=298125984.0 spike=2.67
- GBCO.CA: score=13.15 buy_ready=False sector_rank=20 price=28.4 support=29.31 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.54 liquidity=136441232.0 spike=3.07
- GDWA.CA: score=9.79 buy_ready=False sector_rank=12 price=0.77 support=0.78 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=35639392.0 spike=0.45
- GGCC.CA: score=18.79 buy_ready=False sector_rank=12 price=0.9 support=0.81 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=40.73 liquidity=10851411.0 spike=0.23
- GIHD.CA: score=20.79 buy_ready=False sector_rank=12 price=62.56 support=56.51 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=15886581.0 spike=0.49
- GMCI.CA: score=2.65 buy_ready=False sector_rank=12 price=1.91 support=1.88 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:01 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=835436.56 spike=1.51
- GRCA.CA: score=21.77 buy_ready=False sector_rank=12 price=76.72 support=54.7 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=85.39 liquidity=92966168.0 spike=1.99
- GSSC.CA: score=18.46 buy_ready=False sector_rank=12 price=289.23 support=266.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.13 liquidity=7664128.5 spike=0.41
- GTWL.CA: score=14.79 buy_ready=False sector_rank=12 price=210.05 support=211.0 resistance=211.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=515080896.0 spike=1.0
- HDBK.CA: score=17.4 buy_ready=False sector_rank=8 price=92.4 support=80.8 resistance=93.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.44 liquidity=24119534.0 spike=0.61
- HELI.CA: score=10.8 buy_ready=False sector_rank=11 price=7.36 support=7.48 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=22.76 liquidity=74098552.0 spike=0.46
- HRHO.CA: score=10.32 buy_ready=False sector_rank=19 price=25.88 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=24.16 liquidity=173252960.0 spike=1.88
- ICID.CA: score=17.79 buy_ready=False sector_rank=12 price=16.94 support=7.85 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=94.28 liquidity=11534474.0 spike=0.45
- IDRE.CA: score=16.34 buy_ready=False sector_rank=12 price=51.99 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=62.24 liquidity=7551576.0 spike=0.36
- IFAP.CA: score=23.4 buy_ready=False sector_rank=2 price=20.91 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=26223960.0 spike=0.86
- INFI.CA: score=17.79 buy_ready=False sector_rank=12 price=159.0 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=75.04 liquidity=39252648.0 spike=0.57
- IRON.CA: score=15.38 buy_ready=False sector_rank=9 price=30.63 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=39.33 liquidity=10467519.0 spike=0.91
- ISMA.CA: score=6.91 buy_ready=False sector_rank=12 price=36.88 support=34.01 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44390692.0 spike=1.56
- ISMQ.CA: score=16.38 buy_ready=False sector_rank=9 price=9.09 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=25059756.0 spike=0.45
- ISPH.CA: score=21.4 buy_ready=False sector_rank=6 price=13.08 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=44.09 liquidity=43915268.0 spike=0.23
- JUFO.CA: score=17.86 buy_ready=False sector_rank=17 price=26.61 support=22.78 resistance=28.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.15 liquidity=14910224.0 spike=0.27
- KABO.CA: score=24.4 buy_ready=False sector_rank=3 price=9.12 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=63.06 liquidity=35636312.0 spike=0.91
- KWIN.CA: score=9.45 buy_ready=False sector_rank=12 price=110.61 support=101.01 resistance=118.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=153364704.0 spike=2.83
- KZPC.CA: score=19.17 buy_ready=False sector_rank=12 price=13.11 support=8.42 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.81 liquidity=76948264.0 spike=1.69
- LCSW.CA: score=19.4 buy_ready=False sector_rank=4 price=34.44 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=20673720.0 spike=0.54
- LUTS.CA: score=9.99 buy_ready=False sector_rank=12 price=1.62 support=1.37 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=562408448.0 spike=3.1
- MAAL.CA: score=9.55 buy_ready=False sector_rank=12 price=9.32 support=8.75 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33287144.0 spike=2.88
- MASR.CA: score=16.21 buy_ready=False sector_rank=12 price=7.57 support=7.45 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=81039728.0 spike=1.21
- MBSC.CA: score=18.4 buy_ready=False sector_rank=4 price=382.34 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=82.58 liquidity=23228218.0 spike=0.28
- MCQE.CA: score=21.4 buy_ready=False sector_rank=4 price=237.48 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=68.43 liquidity=50826964.0 spike=0.93
- MCRO.CA: score=18.79 buy_ready=False sector_rank=12 price=1.51 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=30315152.0 spike=0.18
- MENA.CA: score=6.84 buy_ready=False sector_rank=11 price=6.97 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:11 PM market time freshness=DELAYED_CURRENT RSI=54.72 liquidity=1040613.06 spike=0.17
- MEPA.CA: score=17.01 buy_ready=False sector_rank=12 price=1.81 support=1.78 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=8213636.0 spike=0.21
- MFPC.CA: score=20.38 buy_ready=False sector_rank=9 price=39.54 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.84 liquidity=55960560.0 spike=0.64
- MFSC.CA: score=11.6 buy_ready=False sector_rank=12 price=49.61 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=52.44 liquidity=2806208.5 spike=0.25
- MHOT.CA: score=13.91 buy_ready=False sector_rank=16 price=17.88 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.6 liquidity=5545387.0 spike=0.32
- MICH.CA: score=21.49 buy_ready=False sector_rank=12 price=49.5 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=56051396.0 spike=1.35
- MILS.CA: score=20.79 buy_ready=False sector_rank=12 price=221.49 support=167.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=66.06 liquidity=47727276.0 spike=0.57
- MIPH.CA: score=10.44 buy_ready=False sector_rank=6 price=766.83 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=41.63 liquidity=1042066.0 spike=0.25
- MOED.CA: score=16.79 buy_ready=False sector_rank=12 price=0.77 support=0.65 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=79.15 liquidity=84062912.0 spike=0.92
- MOIL.CA: score=8.53 buy_ready=False sector_rank=14 price=0.67 support=0.63 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:06 PM market time freshness=DELAYED_CURRENT RSI=50.52 liquidity=26457.88 spike=0.05
- MOIN.CA: score=16.44 buy_ready=False sector_rank=12 price=33.82 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=59.48 liquidity=5648875.5 spike=0.18
- MOSC.CA: score=17.89 buy_ready=False sector_rank=12 price=332.51 support=282.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=79.55 liquidity=15190647.0 spike=1.05
- MPCI.CA: score=20.81 buy_ready=False sector_rank=12 price=401.56 support=284.0 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.15 liquidity=167530640.0 spike=1.01
- MPCO.CA: score=23.4 buy_ready=False sector_rank=2 price=2.27 support=1.84 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=68.6 liquidity=80156040.0 spike=0.64
- MPRC.CA: score=18.79 buy_ready=False sector_rank=12 price=42.0 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=13316054.0 spike=0.47
- MTIE.CA: score=14.01 buy_ready=False sector_rank=20 price=8.62 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=34813692.0 spike=0.54
- NAHO.CA: score=7.88 buy_ready=False sector_rank=12 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=86105.46 spike=0.96
- NCCW.CA: score=15.79 buy_ready=False sector_rank=12 price=5.88 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=52.87 liquidity=11898868.0 spike=0.38
- NEDA.CA: score=8.38 buy_ready=False sector_rank=12 price=2.72 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:09 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=589376.88 spike=0.66
- NHPS.CA: score=22.45 buy_ready=False sector_rank=12 price=93.42 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=65.8 liquidity=97788576.0 spike=2.83
- NINH.CA: score=10.79 buy_ready=False sector_rank=12 price=25.6 support=22.15 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=221071616.0 spike=6.86
- NIPH.CA: score=19.4 buy_ready=False sector_rank=6 price=369.02 support=209.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.64 liquidity=165076704.0 spike=0.5
- OBRI.CA: score=15.55 buy_ready=False sector_rank=12 price=32.14 support=31.61 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=49.04 liquidity=8758759.0 spike=0.26
- OCDI.CA: score=20.8 buy_ready=False sector_rank=11 price=32.15 support=27.7 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.55 liquidity=128164712.0 spike=0.96
- OCPH.CA: score=12.1 buy_ready=False sector_rank=12 price=256.07 support=225.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.61 liquidity=5306197.5 spike=0.23
- ODIN.CA: score=21.17 buy_ready=False sector_rank=12 price=3.17 support=2.54 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=50977052.0 spike=1.19
- OFH.CA: score=7.91 buy_ready=False sector_rank=12 price=1.0 support=0.95 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=152441424.0 spike=2.06
- OIH.CA: score=24.2 buy_ready=False sector_rank=1 price=1.95 support=1.43 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=85.45 liquidity=176572864.0 spike=1.4
- OLFI.CA: score=14.11 buy_ready=False sector_rank=17 price=23.12 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=42.45 liquidity=9249187.0 spike=0.15
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=805.14 support=781.02 resistance=812.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=536636608.0 spike=1.0
- ORHD.CA: score=20.8 buy_ready=False sector_rank=11 price=42.07 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.03 liquidity=76641600.0 spike=0.48
- ORWE.CA: score=22.4 buy_ready=False sector_rank=3 price=26.01 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=72.05 liquidity=35223788.0 spike=0.45
- PHAR.CA: score=21.4 buy_ready=False sector_rank=6 price=131.36 support=92.85 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=49.64 liquidity=138726080.0 spike=0.3
- PHDC.CA: score=15.8 buy_ready=False sector_rank=11 price=14.72 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=148812464.0 spike=0.63
- PHTV.CA: score=11.79 buy_ready=False sector_rank=12 price=345.36 support=312.0 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=57.84 liquidity=2878504.5 spike=1.06
- POUL.CA: score=14.86 buy_ready=False sector_rank=17 price=37.63 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.1 liquidity=16656378.0 spike=0.62
- PRCL.CA: score=15.19 buy_ready=False sector_rank=4 price=33.85 support=32.0 resistance=37.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=5788781.5 spike=0.19
- PRDC.CA: score=20.8 buy_ready=False sector_rank=11 price=9.19 support=8.7 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=57692952.0 spike=0.9
- PRMH.CA: score=10.79 buy_ready=False sector_rank=12 price=2.45 support=2.32 resistance=2.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55886308.0 spike=4.63
- RACC.CA: score=15.79 buy_ready=False sector_rank=12 price=9.71 support=9.8 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=18340980.0 spike=0.96
- RAKT.CA: score=-0.03 buy_ready=False sector_rank=12 price=22.25 support=21.65 resistance=24.0 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=9.2 liquidity=180514.25 spike=0.65
- RAYA.CA: score=8.88 buy_ready=False sector_rank=21 price=7.22 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=23.71 liquidity=80891032.0 spike=1.09
- RMDA.CA: score=19.4 buy_ready=False sector_rank=6 price=6.07 support=5.08 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=27803062.0 spike=0.23
- ROTO.CA: score=18.79 buy_ready=False sector_rank=12 price=45.23 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=51.25 liquidity=18292424.0 spike=0.75
- RREI.CA: score=18.79 buy_ready=False sector_rank=12 price=4.3 support=4.26 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=50.6 liquidity=26346176.0 spike=0.38
- RTVC.CA: score=22.59 buy_ready=False sector_rank=12 price=4.12 support=3.73 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=69.66 liquidity=14164240.0 spike=1.9
- RUBX.CA: score=24.79 buy_ready=False sector_rank=12 price=13.0 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=58.63 liquidity=15036423.0 spike=0.8
- SAUD.CA: score=19.94 buy_ready=False sector_rank=8 price=23.32 support=21.4 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=71.81 liquidity=8535413.0 spike=0.38
- SCEM.CA: score=21.4 buy_ready=False sector_rank=4 price=95.47 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.94 liquidity=119298456.0 spike=0.56
- SCFM.CA: score=12.45 buy_ready=False sector_rank=12 price=282.64 support=272.0 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=56.42 liquidity=3654624.25 spike=0.17
- SCTS.CA: score=17.04 buy_ready=False sector_rank=13 price=623.5 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=79.83 liquidity=7283015.0 spike=0.78
- SDTI.CA: score=20.59 buy_ready=False sector_rank=12 price=67.01 support=52.36 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=61.38 liquidity=60392892.0 spike=1.9
- SEIG.CA: score=9.81 buy_ready=False sector_rank=12 price=264.04 support=242.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:09 PM market time freshness=DELAYED_CURRENT RSI=50.58 liquidity=1022016.06 spike=0.11
- SIPC.CA: score=20.79 buy_ready=False sector_rank=12 price=4.83 support=3.82 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=54.76 liquidity=16369569.0 spike=0.26
- SKPC.CA: score=18.38 buy_ready=False sector_rank=9 price=17.24 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=79.36 liquidity=31501366.0 spike=0.44
- SMFR.CA: score=18.14 buy_ready=False sector_rank=12 price=261.83 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=72.82 liquidity=9350392.0 spike=0.34
- SNFC.CA: score=20.35 buy_ready=False sector_rank=12 price=10.68 support=10.3 resistance=11.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=45.1 liquidity=29402924.0 spike=2.28
- SPIN.CA: score=20.31 buy_ready=False sector_rank=3 price=18.62 support=15.3 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=70.84 liquidity=7911262.0 spike=0.17
- SPMD.CA: score=14.45 buy_ready=False sector_rank=12 price=0.46 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=35.19 liquidity=5656411.5 spike=0.2
- SUGR.CA: score=21.06 buy_ready=False sector_rank=17 price=57.41 support=46.47 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=87.62 liquidity=98587040.0 spike=2.1
- SVCE.CA: score=20.79 buy_ready=False sector_rank=12 price=10.85 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=70.6 liquidity=75878280.0 spike=0.77
- SWDY.CA: score=22.0 buy_ready=False sector_rank=7 price=127.36 support=91.8 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.62 liquidity=130283968.0 spike=1.3
- TALM.CA: score=5.75 buy_ready=False sector_rank=13 price=18.42 support=18.13 resistance=19.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39502364.0 spike=0.89
- TMGH.CA: score=13.8 buy_ready=False sector_rank=11 price=97.96 support=95.2 resistance=100.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=33.62 liquidity=129925224.0 spike=0.49
- TRTO.CA: score=14.8 buy_ready=False sector_rank=12 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance as_of=2026-08-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=4720.71 spike=0.42
- UEFM.CA: score=10.27 buy_ready=False sector_rank=12 price=542.87 support=531.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:10 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=1480664.25 spike=0.32
- UEGC.CA: score=6.65 buy_ready=False sector_rank=12 price=1.98 support=1.96 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51853352.0 spike=1.43
- UNIP.CA: score=18.79 buy_ready=False sector_rank=12 price=0.37 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=23555158.0 spike=0.66
- UNIT.CA: score=12.08 buy_ready=False sector_rank=11 price=18.91 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=55.06 liquidity=1272631.0 spike=0.1
- WCDF.CA: score=8.45 buy_ready=False sector_rank=12 price=642.73 support=571.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:07 PM market time freshness=DELAYED_CURRENT RSI=76.03 liquidity=657072.19 spike=0.15
- WKOL.CA: score=18.77 buy_ready=False sector_rank=12 price=345.16 support=310.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=5980972.0 spike=0.17
- ZEOT.CA: score=19.4 buy_ready=False sector_rank=12 price=13.42 support=11.7 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=6609061.5 spike=0.25
- ZMID.CA: score=20.8 buy_ready=False sector_rank=11 price=7.92 support=7.06 resistance=8.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.79 liquidity=107459664.0 spike=0.45

## Backtesting Lite
- CCRS.CA: 180d return=110.07%, max drawdown=-34.85%, MA20>MA50 days last20=20, as_of=2026-08-23T21:00:00+00:00
- ALUM.CA: 180d return=61.71%, max drawdown=-21.86%, MA20>MA50 days last20=15, as_of=2026-08-23T21:00:00+00:00
- RUBX.CA: 180d return=40.45%, max drawdown=-18.45%, MA20>MA50 days last20=20, as_of=2026-08-23T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CCRS.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3890 sources=3 expected=Gulf Canadian Company for Arab Real Estate Investment summary=10 EGX-listed firms deny ties to UAE-based Abraaj; Gulf Canadian OGM to discuss 2016 financials Thursday; Gulf Canadian OGM to discuss 2016 results 22 March
  - 10 EGX-listed firms deny ties to UAE-based Abraaj: https://english.mubasher.info/news/3308086/10-EGX-listed-firms-deny-ties-to-UAE-based-Abraaj/
  - Gulf Canadian OGM to discuss 2016 financials Thursday: https://english.mubasher.info/news/3076282/Gulf-Canadian-OGM-to-discuss-2016-financials-Thursday/
  - Gulf Canadian OGM to discuss 2016 results 22 March: https://english.mubasher.info/news/3067564/Gulf-Canadian-OGM-to-discuss-2016-results-22-March/
- ALUM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Aluminum Company (S.A.E) summary=Arab Aluminum’s stock holds steady as bullish pattern breaks; Arab Aluminum profits rise 7% in H1-17; Arab Aluminum OGM approves EGP 1/shr dividends
  - Arab Aluminum’s stock holds steady as bullish pattern breaks: https://english.mubasher.info/news/4564438/Arab-Aluminum-s-stock-holds-steady-as-bullish-pattern-breaks/
  - Arab Aluminum profits rise 7% in H1-17: https://english.mubasher.info/news/3144589/Arab-Aluminum-profits-rise-7-in-H1-17/
  - Arab Aluminum OGM approves EGP 1/shr dividends: https://english.mubasher.info/news/3076498/Arab-Aluminum-OGM-approves-EGP-1-shr-dividends/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- COMI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Commercial International Bank Egypt summary=Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=602 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.

## Warnings
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ALUM.CA matches the company but no source/report date was detected.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence rejected for COMI.CA: source text did not clearly match COMI.CA / Commercial International Bank Egypt.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
