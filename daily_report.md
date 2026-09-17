# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-17T11:46:34.726280+00:00
Generated Cairo: 2026-09-17 14:46
Run timing: target 09:15 Cairo | generated Cairo 2026-09-17 14:46 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-17 14:35

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 183/189
- Top sector: Investment Holding

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 38.1% / above MA50 57.14%
- EGX70 regime: BEARISH / above MA20 40.0% / above MA50 60.0%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=682374720.0 spike=1.24 score=10.56
- CCAP.CA: liquidity=405782144.0 spike=0.46 score=23.4
- ETEL.CA: liquidity=248451642.97 spike=1.32 score=20.04
- ELEC.CA: liquidity=224876912.0 spike=3.08 score=12.38
- ZMID.CA: liquidity=163701312.0 spike=0.66 score=19.92

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (19% sector participation), triggering a defensive risk mode that blocks new buys; the scanner’s top tickets rank high on score and show bullish‑watch outlook but sit near resistance with elevated RSI and liquidity spikes, indicating limited upside and heightened pullback risk.
- Prioritized tickets (BINV.CA, WKOL.CA, OIH.CA, MPCO.CA, CCAP.CA) were selected for their highest rank scores and bullish‑watch outlook, reflecting accumulation spikes and strength in leading sectors (Investment Holding, 
- Liquidity spikes and close proximity to 20‑day resistance suggest possible short‑term upside, yet support distances are wide and RSI is overheated, raising the chance of a near‑term pullback over the next 1‑3 days.
- Sector breadth remains low at 19%, and while leading sectors show strong internal returns, the overall EGX30/EGX70 bearish trend keeps the risk mode defensive, so no new BUY signals are permitted.
- Uncertainty is high: confidence is LOW, evidence is mixed, and a shift in market breadth or macro news could quickly alter the outlook, making price action choppy with upside capped by resistance.

## Top Liquidity Spikes
- WKOL.CA: spike=7.0 liquidity=88660648.0 outlook=BULLISH_WATCH score=91.15 buy_ready=False
- BINV.CA: spike=5.8 liquidity=99299872.0 outlook=BULLISH_WATCH score=77 buy_ready=False
- IDRE.CA: spike=5.39 liquidity=55801320.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AALR.CA: spike=5.08 liquidity=127627608.0 outlook=BULLISH_WATCH score=81.15 buy_ready=False
- EALR.CA: spike=4.33 liquidity=72718336.0 outlook=WEAK_OR_RISKY score=23.15 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=17.31 5d=12.95% 20d=24.59% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=11.71 5d=7.45% 20d=8.27% aboveMA50=100.0%
- #3 Telecommunications: score=10.02 5d=1.89% 20d=6.9% aboveMA50=100.0%
- #4 Education: score=6.68 5d=1.67% 20d=4.14% aboveMA50=66.67%
- #5 Textiles: score=4.74 5d=-4.62% 20d=2.87% aboveMA50=100.0%
- #6 Basic Resources & Chemicals: score=4.24 5d=-3.16% 20d=3.23% aboveMA50=70.0%
- #7 Energy & Petrochemicals: score=3.85 5d=-0.22% 20d=1.37% aboveMA50=50.0%
- #8 Automotive & Distribution: score=2.8 5d=-0.07% 20d=-2.83% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- IFAP.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- WKOL.CA: BULLISH_WATCH score=91.15 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- KABO.CA: BULLISH_WATCH score=85.74 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CANA.CA: BULLISH_WATCH score=84.7 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- OIH.CA: BULLISH_WATCH score=83 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; close to resistance
- MPCO.CA: BULLISH_WATCH score=83 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- AALR.CA: BULLISH_WATCH score=81.15 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EGCH.CA: BULLISH_WATCH score=80.24 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- FERC.CA: BULLISH_WATCH score=80.24 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SKPC.CA: BULLISH_WATCH score=77.24 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=22.46 buy_ready=False sector_rank=13 price=318.98 support=295.0 resistance=351.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=69.61 liquidity=127627608.0 spike=5.08
- ABUK.CA: score=18.7 buy_ready=False sector_rank=6 price=89.0 support=75.01 resistance=94.5 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=67.23 liquidity=69726783.0 spike=0.46
- ACAMD.CA: score=18.46 buy_ready=False sector_rank=13 price=2.09 support=1.95 resistance=2.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=32840986.0 spike=0.57
- ACGC.CA: score=20.9 buy_ready=False sector_rank=5 price=14.4 support=12.04 resistance=16.09 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=47.61 liquidity=15803812.38 spike=0.42
- ADCI.CA: score=9.05 buy_ready=False sector_rank=13 price=279.52 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=1590156.38 spike=0.26
- ADIB.CA: score=18.08 buy_ready=False sector_rank=9 price=52.4 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=38.56 liquidity=17373282.0 spike=0.26
- ADPC.CA: score=14.46 buy_ready=False sector_rank=13 price=3.89 support=3.81 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=10004457.0 spike=0.44
- AFDI.CA: score=19.46 buy_ready=False sector_rank=13 price=56.81 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=49.6 liquidity=13721179.0 spike=0.55
- AFMC.CA: score=9.46 buy_ready=False sector_rank=13 price=161.59 support=157.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=21.86 liquidity=12432728.0 spike=0.22
- AJWA.CA: score=11.06 buy_ready=False sector_rank=13 price=180.57 support=175.15 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=6601895.5 spike=0.13
- ALCN.CA: score=16.3 buy_ready=False sector_rank=21 price=31.0 support=30.03 resistance=34.18 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=54.87 liquidity=12396528.0 spike=0.44
- ALUM.CA: score=6.48 buy_ready=False sector_rank=13 price=26.52 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=20.1 liquidity=4024753.75 spike=0.28
- AMER.CA: score=12.92 buy_ready=False sector_rank=11 price=5.46 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=32.45 liquidity=21846232.0 spike=0.35
- AMES.CA: score=8.46 buy_ready=False sector_rank=13 price=52.49 support=51.22 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=2.68 liquidity=44615976.0 spike=0.17
- AMIA.CA: score=13.68 buy_ready=False sector_rank=13 price=18.33 support=15.3 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=35.75 liquidity=6221653.0 spike=0.1
- AMOC.CA: score=18.54 buy_ready=False sector_rank=7 price=13.45 support=10.65 resistance=14.63 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=74.61 liquidity=119563154.6 spike=0.71
- APSW.CA: score=3.95 buy_ready=False sector_rank=13 price=8.42 support=8.37 resistance=9.1 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=44.94 liquidity=487795.86 spike=0.51
- ARAB.CA: score=19.92 buy_ready=False sector_rank=11 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=17880950.0 spike=0.18
- ARCC.CA: score=17.18 buy_ready=False sector_rank=17 price=73.03 support=71.5 resistance=81.85 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=42.22 liquidity=16025556.87 spike=0.39
- AREH.CA: score=7.89 buy_ready=False sector_rank=13 price=1.43 support=1.39 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=3425344.75 spike=0.21
- ARVA.CA: score=4.46 buy_ready=False sector_rank=13 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=11.26 buy_ready=False sector_rank=13 price=60.71 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=36.59 liquidity=6797946.5 spike=0.35
- ASPI.CA: score=17.66 buy_ready=False sector_rank=13 price=0.45 support=0.41 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=38.27 liquidity=61341976.0 spike=1.1
- ATLC.CA: score=16.04 buy_ready=False sector_rank=14 price=6.96 support=5.2 resistance=8.1 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=66.16 liquidity=6625335.4 spike=0.25
- ATQA.CA: score=18.7 buy_ready=False sector_rank=6 price=12.65 support=10.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=66.33 liquidity=17288274.0 spike=0.16
- AXPH.CA: score=17.07 buy_ready=False sector_rank=13 price=1701.0 support=1351.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=56.86 liquidity=5605232.0 spike=0.46
- BINV.CA: score=28.4 buy_ready=False sector_rank=1 price=62.04 support=46.25 resistance=62.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=83.0 liquidity=99299872.0 spike=5.8
- BIOC.CA: score=9.46 buy_ready=False sector_rank=13 price=283.12 support=272.01 resistance=515.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=14.21 liquidity=11122290.0 spike=0.1
- BTFH.CA: score=13.41 buy_ready=False sector_rank=14 price=2.92 support=2.87 resistance=3.09 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=37.93 liquidity=44966412.69 spike=0.51
- CAED.CA: score=7.17 buy_ready=False sector_rank=13 price=129.57 support=123.56 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=29.76 liquidity=4707211.5 spike=0.11
- CANA.CA: score=21.2 buy_ready=False sector_rank=9 price=43.0 support=41.0 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=21906040.0 spike=1.56
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=6.94 support=5.42 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=81.32 liquidity=405782144.0 spike=0.46
- CCRS.CA: score=19.5 buy_ready=False sector_rank=13 price=2.7 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=52549996.0 spike=1.02
- CEFM.CA: score=10.34 buy_ready=False sector_rank=13 price=147.13 support=138.1 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=876837.75 spike=0.06
- CERA.CA: score=19.8 buy_ready=False sector_rank=13 price=1.49 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=57.63 liquidity=114687568.0 spike=1.17
- CFGH.CA: score=5.46 buy_ready=False sector_rank=13 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=613.56 spike=0.03
- CICH.CA: score=11.11 buy_ready=False sector_rank=14 price=12.81 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=1694863.63 spike=0.36
- CIEB.CA: score=11.97 buy_ready=False sector_rank=9 price=24.9 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=3889291.0 spike=0.28
- CIRA.CA: score=21.4 buy_ready=False sector_rank=4 price=39.0 support=32.1 resistance=41.74 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=68.68 liquidity=28008513.0 spike=0.79
- CLHO.CA: score=9.32 buy_ready=False sector_rank=15 price=16.37 support=15.81 resistance=18.45 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=33.81 liquidity=26664341.35 spike=0.36
- CNFN.CA: score=6.02 buy_ready=False sector_rank=14 price=4.62 support=4.46 resistance=4.97 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=38.57 liquidity=2607527.94 spike=0.26
- COMI.CA: score=10.56 buy_ready=False sector_rank=9 price=132.9 support=131.11 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=682374720.0 spike=1.24
- COPR.CA: score=17.46 buy_ready=False sector_rank=13 price=0.5 support=0.46 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=37.33 liquidity=20270778.0 spike=0.23
- COSG.CA: score=10.63 buy_ready=False sector_rank=13 price=1.82 support=1.74 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=3174097.75 spike=0.08
- CPCI.CA: score=7.08 buy_ready=False sector_rank=13 price=546.52 support=525.01 resistance=569.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=26.84 liquidity=2619001.0 spike=0.64
- CSAG.CA: score=13.3 buy_ready=False sector_rank=21 price=36.5 support=36.5 resistance=44.45 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=36.74 liquidity=13538835.5 spike=0.87
- DAPH.CA: score=17.46 buy_ready=False sector_rank=13 price=122.34 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=52.89 liquidity=15757198.0 spike=0.26
- DEIN.CA: score=7.46 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=1.18 buy_ready=False sector_rank=20 price=26.89 support=26.51 resistance=29.47 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=27.87 liquidity=2314260.91 spike=0.43
- DSCW.CA: score=9.95 buy_ready=False sector_rank=13 price=1.84 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=5487399.0 spike=0.14
- DTPP.CA: score=19.96 buy_ready=False sector_rank=13 price=338.7 support=292.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=81392176.0 spike=1.25
- EALR.CA: score=14.46 buy_ready=False sector_rank=13 price=382.61 support=340.0 resistance=426.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=34.06 liquidity=72718336.0 spike=4.33
- EASB.CA: score=13.11 buy_ready=False sector_rank=13 price=8.23 support=7.16 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=56.2 liquidity=1652040.38 spike=0.1
- EAST.CA: score=8.91 buy_ready=False sector_rank=20 price=32.55 support=32.0 resistance=36.7 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=28.11 liquidity=105734343.37 spike=1.52
- EBSC.CA: score=8.95 buy_ready=False sector_rank=13 price=2.04 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=47.87 liquidity=1488886.25 spike=0.1
- ECAP.CA: score=5.53 buy_ready=False sector_rank=13 price=32.54 support=31.16 resistance=39.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=1070238.38 spike=0.09
- EDFM.CA: score=9.84 buy_ready=False sector_rank=13 price=411.48 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=59.07 liquidity=378640.97 spike=0.23
- EEII.CA: score=0.26 buy_ready=False sector_rank=13 price=2.19 support=2.15 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=1796486.25 spike=0.08
- EFIC.CA: score=14.7 buy_ready=False sector_rank=6 price=195.0 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=38058648.0 spike=0.42
- EFID.CA: score=16.91 buy_ready=False sector_rank=20 price=30.8 support=29.71 resistance=33.47 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=39.52 liquidity=56451470.6 spike=1.02
- EFIH.CA: score=19.71 buy_ready=False sector_rank=12 price=23.7 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=40.81 liquidity=27482018.0 spike=0.43
- EGAL.CA: score=20.7 buy_ready=False sector_rank=6 price=364.0 support=321.01 resistance=395.0 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=49.34 liquidity=33513844.0 spike=0.33
- EGAS.CA: score=9.92 buy_ready=False sector_rank=7 price=60.3 support=55.25 resistance=60.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27432934.0 spike=3.19
- EGBE.CA: score=3.16 buy_ready=False sector_rank=9 price=0.5 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:27 AM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=84424.97 spike=0.62
- EGCH.CA: score=20.7 buy_ready=False sector_rank=6 price=13.92 support=13.3 resistance=14.83 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=58.58 liquidity=35292628.99 spike=0.32
- EGSA.CA: score=9.79 buy_ready=False sector_rank=3 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 September 01:08 PM market time freshness=DELAYED_CURRENT RSI=78.18 liquidity=10410.0 spike=1.19
- EGTS.CA: score=10.97 buy_ready=False sector_rank=11 price=17.13 support=16.17 resistance=18.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=46.62 liquidity=4058665.25 spike=0.17
- EHDR.CA: score=7.64 buy_ready=False sector_rank=13 price=2.77 support=2.73 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=3182191.0 spike=0.16
- EKHO.CA: score=6.54 buy_ready=False sector_rank=7 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.38 buy_ready=False sector_rank=16 price=2.03 support=1.93 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=224876912.0 spike=3.08
- ELKA.CA: score=8.21 buy_ready=False sector_rank=13 price=1.74 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=47.17 liquidity=3754066.75 spike=0.09
- ELNA.CA: score=-1.52 buy_ready=False sector_rank=13 price=35.74 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=22.51 liquidity=23302.48 spike=0.05
- ELSH.CA: score=12.85 buy_ready=False sector_rank=13 price=12.91 support=12.67 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=41.01 liquidity=8385658.0 spike=0.22
- ELWA.CA: score=6.06 buy_ready=False sector_rank=13 price=1.7 support=1.62 resistance=1.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=36.36 liquidity=1599076.14 spike=0.65
- EMFD.CA: score=19.92 buy_ready=False sector_rank=11 price=14.1 support=11.55 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=74.05 liquidity=28774308.0 spike=0.17
- ENGC.CA: score=2.94 buy_ready=False sector_rank=13 price=42.79 support=41.0 resistance=50.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=34.08 liquidity=3477791.5 spike=0.28
- EOSB.CA: score=9.7 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=77512.47 spike=1.08
- EPCO.CA: score=11.41 buy_ready=False sector_rank=13 price=11.24 support=10.8 resistance=12.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=47.6 liquidity=1951023.5 spike=0.1
- EPPK.CA: score=-5.12 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=20.04 buy_ready=False sector_rank=3 price=131.3 support=112.1 resistance=135.4 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=86.15 liquidity=248451642.97 spike=1.32
- ETRS.CA: score=10.84 buy_ready=False sector_rank=13 price=10.92 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=49.72 liquidity=3381030.25 spike=0.2
- EXPA.CA: score=15.3 buy_ready=False sector_rank=9 price=21.12 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=5220682.5 spike=0.15
- FAIT.CA: score=12.51 buy_ready=False sector_rank=9 price=47.37 support=39.58 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=68.21 liquidity=2425563.0 spike=0.31
- FAITA.CA: score=0.09 buy_ready=False sector_rank=9 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=9.76 liquidity=14080.99 spike=0.29
- FERC.CA: score=20.7 buy_ready=False sector_rank=6 price=79.31 support=76.9 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=11302110.0 spike=0.61
- FWRY.CA: score=14.71 buy_ready=False sector_rank=12 price=18.9 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=15750043.0 spike=0.12
- GBCO.CA: score=19.59 buy_ready=False sector_rank=8 price=30.55 support=27.51 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=63.69 liquidity=5473464.5 spike=0.1
- GDWA.CA: score=13.46 buy_ready=False sector_rank=13 price=0.77 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=25652328.0 spike=0.64
- GGCC.CA: score=12.66 buy_ready=False sector_rank=13 price=0.87 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=35.36 liquidity=8197759.0 spike=0.21
- GIHD.CA: score=10.61 buy_ready=False sector_rank=13 price=74.04 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=65.35 liquidity=3148069.0 spike=0.11
- GMCI.CA: score=0.78 buy_ready=False sector_rank=13 price=1.75 support=1.69 resistance=1.95 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=23.33 liquidity=841701.0 spike=1.74
- GRCA.CA: score=8.46 buy_ready=False sector_rank=13 price=43.28 support=39.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=27.52 liquidity=19809558.0 spike=0.24
- GSSC.CA: score=4.5 buy_ready=False sector_rank=13 price=318.21 support=291.16 resistance=321.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12882025.0 spike=1.02
- GTWL.CA: score=19.46 buy_ready=False sector_rank=13 price=236.09 support=175.01 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=62.29 liquidity=59228336.0 spike=0.23
- HDBK.CA: score=20.08 buy_ready=False sector_rank=9 price=114.97 support=89.01 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=71.49 liquidity=13267834.0 spike=0.23
- HELI.CA: score=21.92 buy_ready=False sector_rank=11 price=8.41 support=7.34 resistance=8.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=147480112.0 spike=0.94
- HRHO.CA: score=13.4 buy_ready=False sector_rank=14 price=25.49 support=25.04 resistance=26.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=9986917.0 spike=0.1
- ICID.CA: score=10.49 buy_ready=False sector_rank=13 price=18.08 support=15.04 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=1032837.06 spike=0.05
- IDRE.CA: score=9.46 buy_ready=False sector_rank=13 price=56.81 support=53.8 resistance=59.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55801320.0 spike=5.39
- IFAP.CA: score=21.54 buy_ready=False sector_rank=2 price=20.92 support=20.05 resistance=22.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=8141856.0 spike=0.35
- INFI.CA: score=12.46 buy_ready=False sector_rank=13 price=135.3 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=16.41 liquidity=19896910.0 spike=0.63
- IRON.CA: score=10.76 buy_ready=False sector_rank=6 price=27.45 support=26.3 resistance=33.95 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=2.57 liquidity=20717723.38 spike=1.53
- ISMA.CA: score=1.89 buy_ready=False sector_rank=13 price=29.72 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=13.72 liquidity=2426632.5 spike=0.09
- ISMQ.CA: score=9.68 buy_ready=False sector_rank=6 price=8.9 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=3982019.25 spike=0.14
- ISPH.CA: score=11.04 buy_ready=False sector_rank=15 price=12.2 support=11.9 resistance=13.6 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=30.22 liquidity=112154586.05 spike=1.86
- JUFO.CA: score=10.24 buy_ready=False sector_rank=20 price=27.08 support=26.45 resistance=27.98 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=47.8 liquidity=5367093.5 spike=0.29
- KABO.CA: score=20.9 buy_ready=False sector_rank=5 price=9.31 support=8.82 resistance=10.17 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=54.0 liquidity=42303524.71 spike=0.89
- KWIN.CA: score=7.52 buy_ready=False sector_rank=13 price=89.53 support=84.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=8062734.5 spike=0.12
- KZPC.CA: score=17.46 buy_ready=False sector_rank=13 price=14.45 support=12.16 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=72.6 liquidity=11445149.0 spike=0.19
- LCSW.CA: score=14.01 buy_ready=False sector_rank=17 price=33.33 support=32.42 resistance=37.5 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=45.38 liquidity=9837616.68 spike=0.39
- LUTS.CA: score=17.46 buy_ready=False sector_rank=13 price=0.99 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=51.09 liquidity=48809888.0 spike=0.18
- MAAL.CA: score=1.27 buy_ready=False sector_rank=13 price=8.79 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=34.64 liquidity=1813970.75 spike=0.18
- MASR.CA: score=14.46 buy_ready=False sector_rank=13 price=7.89 support=7.49 resistance=8.88 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=57.2 liquidity=50286566.99 spike=0.57
- MBSC.CA: score=17.18 buy_ready=False sector_rank=17 price=377.03 support=355.04 resistance=470.0 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=45.97 liquidity=44326662.9 spike=0.87
- MCQE.CA: score=13.65 buy_ready=False sector_rank=17 price=221.44 support=213.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=40.18 liquidity=6478496.0 spike=0.18
- MCRO.CA: score=16.46 buy_ready=False sector_rank=13 price=1.69 support=1.44 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=79.49 liquidity=37815104.0 spike=0.32
- MENA.CA: score=6.63 buy_ready=False sector_rank=11 price=6.7 support=6.58 resistance=7.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:29 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=1717432.25 spike=0.67
- MEPA.CA: score=13.53 buy_ready=False sector_rank=13 price=1.94 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=58.97 liquidity=4071536.25 spike=0.12
- MFPC.CA: score=20.14 buy_ready=False sector_rank=6 price=48.69 support=38.93 resistance=48.9 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=83.75 liquidity=154583003.93 spike=1.22
- MFSC.CA: score=5.19 buy_ready=False sector_rank=13 price=49.04 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=731232.31 spike=0.15
- MHOT.CA: score=13.95 buy_ready=False sector_rank=10 price=17.97 support=17.62 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=35.64 liquidity=6928098.0 spike=0.65
- MICH.CA: score=12.18 buy_ready=False sector_rank=13 price=49.4 support=47.2 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=4717239.0 spike=0.19
- MILS.CA: score=5.82 buy_ready=False sector_rank=13 price=201.0 support=198.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=26.51 liquidity=3363173.25 spike=0.06
- MIPH.CA: score=13.08 buy_ready=False sector_rank=15 price=831.0 support=700.2 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=62.61 liquidity=3754690.75 spike=0.96
- MOED.CA: score=16.46 buy_ready=False sector_rank=13 price=0.79 support=0.74 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=51.14 liquidity=12858502.0 spike=0.1
- MOIL.CA: score=10.57 buy_ready=False sector_rank=7 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=59.38 liquidity=34526.49 spike=0.17
- MOIN.CA: score=19.46 buy_ready=False sector_rank=13 price=37.65 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=18336418.0 spike=0.64
- MOSC.CA: score=12.08 buy_ready=False sector_rank=13 price=315.0 support=302.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=29.45 liquidity=9278605.0 spike=1.17
- MPCI.CA: score=17.46 buy_ready=False sector_rank=13 price=410.77 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=53.87 liquidity=12761660.0 spike=0.08
- MPCO.CA: score=23.56 buy_ready=False sector_rank=2 price=2.72 support=2.07 resistance=2.92 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=65.61 liquidity=161865112.74 spike=1.08
- MPRC.CA: score=8.06 buy_ready=False sector_rank=13 price=39.44 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=3595045.0 spike=0.09
- MTIE.CA: score=15.12 buy_ready=False sector_rank=8 price=8.4 support=8.1 resistance=8.99 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=45.86 liquidity=15456066.5 spike=0.42
- NAHO.CA: score=7.49 buy_ready=False sector_rank=13 price=0.14 support=0.13 resistance=0.15 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=41.67 liquidity=33459.51 spike=0.53
- NCCW.CA: score=16.46 buy_ready=False sector_rank=13 price=8.1 support=5.59 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=75.87 liquidity=37329640.0 spike=0.61
- NEDA.CA: score=4.79 buy_ready=False sector_rank=13 price=2.72 support=2.7 resistance=2.95 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=40.62 liquidity=334641.6 spike=0.47
- NHPS.CA: score=3.51 buy_ready=False sector_rank=13 price=76.95 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=6.12 liquidity=4050056.0 spike=0.19
- NINH.CA: score=9.46 buy_ready=False sector_rank=13 price=20.72 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=20468168.0 spike=0.67
- NIPH.CA: score=12.32 buy_ready=False sector_rank=15 price=317.05 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=17.14 liquidity=34925956.0 spike=0.18
- OBRI.CA: score=5.96 buy_ready=False sector_rank=13 price=30.61 support=30.1 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=37.87 liquidity=2498305.25 spike=0.13
- OCDI.CA: score=14.92 buy_ready=False sector_rank=11 price=30.11 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=39.58 liquidity=28381222.0 spike=0.35
- OCPH.CA: score=2.34 buy_ready=False sector_rank=13 price=240.55 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=30.76 liquidity=1878366.25 spike=0.23
- ODIN.CA: score=1.95 buy_ready=False sector_rank=13 price=2.77 support=2.55 resistance=3.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=13.51 liquidity=2494768.75 spike=0.09
- OFH.CA: score=19.46 buy_ready=False sector_rank=13 price=1.06 support=0.88 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=19682790.0 spike=0.18
- OIH.CA: score=24.4 buy_ready=False sector_rank=1 price=2.16 support=1.82 resistance=2.17 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=66.0 liquidity=94774773.05 spike=0.81
- OLFI.CA: score=14.87 buy_ready=False sector_rank=20 price=22.51 support=22.07 resistance=25.0 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=41.47 liquidity=23245964.69 spike=1.5
- ORAS.CA: score=5.0 buy_ready=False sector_rank=19 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=19.92 buy_ready=False sector_rank=11 price=43.16 support=40.28 resistance=43.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=49.0 liquidity=114753336.0 spike=0.83
- ORWE.CA: score=20.9 buy_ready=False sector_rank=5 price=27.5 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=57.35 liquidity=29734928.0 spike=0.6
- PHAR.CA: score=12.32 buy_ready=False sector_rank=15 price=117.8 support=117.01 resistance=141.0 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=19.32 liquidity=112166571.31 spike=0.79
- PHDC.CA: score=9.92 buy_ready=False sector_rank=11 price=13.66 support=13.65 resistance=15.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=31.85 liquidity=32156776.0 spike=0.17
- PHTV.CA: score=13.86 buy_ready=False sector_rank=13 price=367.22 support=311.27 resistance=389.0 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=64.27 liquidity=2978521.43 spike=1.71
- POUL.CA: score=11.72 buy_ready=False sector_rank=20 price=37.9 support=36.97 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=47.07 liquidity=7853890.0 spike=0.33
- PRCL.CA: score=16.18 buy_ready=False sector_rank=17 price=32.28 support=30.9 resistance=35.73 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=45.39 liquidity=13267918.78 spike=0.74
- PRDC.CA: score=9.92 buy_ready=False sector_rank=11 price=7.83 support=7.68 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=23.25 liquidity=21392086.0 spike=0.34
- PRMH.CA: score=6.97 buy_ready=False sector_rank=13 price=2.58 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=2509952.5 spike=0.23
- RACC.CA: score=9.15 buy_ready=False sector_rank=13 price=9.83 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=4692012.0 spike=0.24
- RAKT.CA: score=10.52 buy_ready=False sector_rank=13 price=22.65 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=57.94 liquidity=55651.05 spike=0.22
- RAYA.CA: score=14.16 buy_ready=False sector_rank=18 price=7.09 support=6.95 resistance=7.73 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=36.36 liquidity=32447059.56 spike=0.62
- RMDA.CA: score=17.32 buy_ready=False sector_rank=15 price=6.14 support=5.77 resistance=6.55 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=30464413.68 spike=0.57
- ROTO.CA: score=2.83 buy_ready=False sector_rank=13 price=40.81 support=35.02 resistance=51.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=3365009.75 spike=0.32
- RREI.CA: score=19.46 buy_ready=False sector_rank=13 price=4.45 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=17839060.0 spike=0.66
- RTVC.CA: score=0.38 buy_ready=False sector_rank=13 price=3.94 support=3.85 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=922781.06 spike=0.13
- RUBX.CA: score=18.09 buy_ready=False sector_rank=13 price=13.54 support=12.36 resistance=14.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=67.33 liquidity=6629782.5 spike=0.33
- SAUD.CA: score=10.61 buy_ready=False sector_rank=9 price=23.38 support=22.7 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=50.96 liquidity=2534233.0 spike=0.18
- SCEM.CA: score=17.18 buy_ready=False sector_rank=17 price=95.0 support=94.0 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=18227388.0 spike=0.13
- SCFM.CA: score=1.44 buy_ready=False sector_rank=13 price=276.83 support=265.51 resistance=297.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=25.49 liquidity=1982451.88 spike=0.21
- SCTS.CA: score=1.99 buy_ready=False sector_rank=4 price=605.88 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=28.73 liquidity=589791.56 spike=0.12
- SDTI.CA: score=17.46 buy_ready=False sector_rank=13 price=75.0 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=65.18 liquidity=12962685.0 spike=0.64
- SEIG.CA: score=5.38 buy_ready=False sector_rank=13 price=246.1 support=228.13 resistance=274.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=917893.31 spike=0.51
- SIPC.CA: score=19.46 buy_ready=False sector_rank=13 price=5.92 support=4.1 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=65.96 liquidity=12243508.0 spike=0.21
- SKPC.CA: score=20.7 buy_ready=False sector_rank=6 price=18.25 support=16.82 resistance=19.36 source=Yahoo Finance as_of=2026-09-15T21:00:00+00:00 freshness=FRESH RSI=63.27 liquidity=117741900.75 spike=0.84
- SMFR.CA: score=8.72 buy_ready=False sector_rank=13 price=241.6 support=236.0 resistance=276.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=9259908.0 spike=0.97
- SNFC.CA: score=19.46 buy_ready=False sector_rank=13 price=11.17 support=10.26 resistance=11.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=65.24 liquidity=10211819.0 spike=0.76
- SPIN.CA: score=6.47 buy_ready=False sector_rank=5 price=17.54 support=17.01 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=28.41 liquidity=2572573.5 spike=0.13
- SPMD.CA: score=5.42 buy_ready=False sector_rank=13 price=0.45 support=0.44 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96013000.0 spike=1.48
- SUGR.CA: score=15.53 buy_ready=False sector_rank=20 price=60.13 support=50.0 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=6658172.0 spike=0.1
- SVCE.CA: score=19.46 buy_ready=False sector_rank=13 price=11.95 support=10.28 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=58.13 liquidity=81895072.0 spike=0.5
- SWDY.CA: score=17.22 buy_ready=False sector_rank=16 price=126.5 support=115.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=42.64 liquidity=20667322.0 spike=0.23
- TALM.CA: score=18.4 buy_ready=False sector_rank=4 price=22.24 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=80.86 liquidity=54502832.0 spike=0.9
- TMGH.CA: score=14.92 buy_ready=False sector_rank=11 price=94.89 support=94.86 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=40.75 liquidity=76310472.0 spike=0.29
- TRTO.CA: score=7.47 buy_ready=False sector_rank=13 price=0.07 support=0.05 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=67.92 liquidity=10535.58 spike=0.38
- UEFM.CA: score=6.03 buy_ready=False sector_rank=13 price=517.09 support=440.66 resistance=557.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=48.61 liquidity=1567301.88 spike=0.57
- UEGC.CA: score=9.46 buy_ready=False sector_rank=13 price=1.77 support=1.66 resistance=2.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=30.16 liquidity=13476617.0 spike=0.28
- UNIP.CA: score=19.18 buy_ready=False sector_rank=13 price=0.39 support=0.35 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=52.13 liquidity=9716085.0 spike=0.29
- UNIT.CA: score=21.92 buy_ready=False sector_rank=11 price=19.6 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=56.35 liquidity=11147594.0 spike=0.78
- WCDF.CA: score=13.2 buy_ready=False sector_rank=13 price=752.62 support=630.06 resistance=765.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=90.91 liquidity=4223761.5 spike=1.26
- WKOL.CA: score=26.46 buy_ready=False sector_rank=13 price=355.08 support=332.56 resistance=369.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=57.22 liquidity=88660648.0 spike=7.0
- ZEOT.CA: score=3.96 buy_ready=False sector_rank=13 price=13.16 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=28.1 liquidity=1496715.38 spike=0.2
- ZMID.CA: score=19.92 buy_ready=False sector_rank=11 price=9.43 support=7.41 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=163701312.0 spike=0.66

## Backtesting Lite
- BINV.CA: 180d return=68.35%, max drawdown=-17.77%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- WKOL.CA: 180d return=13.4%, max drawdown=-25.83%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- OIH.CA: 180d return=83.05%, max drawdown=-14.56%, MA20>MA50 days last20=20, as_of=2026-09-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- WKOL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Wadi Kom Ombo For Land Reclamation Co. summary=Wadi Kom Ombo amends estimated budget for FY26/27; Wadi Kom Ombo eyes EGP 257.77m in FY26/27 net profits; Wadi Kom Ombo records lower net profits at nearly EGP 2m in Q1-25/26
  - Wadi Kom Ombo amends estimated budget for FY26/27: https://english.mubasher.info/news/4600336/Wadi-Kom-Ombo-amends-estimated-budget-for-FY26-27/
  - Wadi Kom Ombo eyes EGP 257.77m in FY26/27 net profits: https://english.mubasher.info/news/4585452/Wadi-Kom-Ombo-eyes-EGP-257-77m-in-FY26-27-net-profits/
  - Wadi Kom Ombo records lower net profits at nearly EGP 2m in Q1-25/26: https://english.mubasher.info/news/4531526/Wadi-Kom-Ombo-records-lower-net-profits-at-nearly-EGP-2m-in-Q1-25-26/
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=624 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- AALR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=General Company For Land Reclamation, Development & Reconstruction summary=General Land Reclamation expects over EGP 8.6m net profits in FY26/27 estimated budget; General Land Reclamation incurs EGP 29.5m loss in FY18/19; General Land Reclamation turns to losses in 9M
  - General Land Reclamation expects over EGP 8.6m net profits in FY26/27 estimated budget: https://english.mubasher.info/news/4600324/General-Land-Reclamation-expects-over-EGP-8-6m-net-profits-in-FY26-27-estimated-budget/
  - General Land Reclamation incurs EGP 29.5m loss in FY18/19: https://english.mubasher.info/news/3525030/General-Land-Reclamation-incurs-EGP-29-5m-loss-in-FY18-19/
  - General Land Reclamation turns to losses in 9M: https://english.mubasher.info/news/3465326/General-Land-Reclamation-turns-to-losses-in-9M/
- HELI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Heliopolis Housing summary=Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- UNIT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=624 sources=3 expected=United Housing and Development summary=United Housing’s shareholders pass EGP 0.12/shr dividends for 2025; United Housing unveils EGP 5.9bn mixed-use project in Alexandria; United Housing’s consolidated net profits exceed EGP 174.5m in 9M-25
  - United Housing’s shareholders pass EGP 0.12/shr dividends for 2025: https://english.mubasher.info/news/4591202/United-Housing-s-shareholders-pass-EGP-0-12-shr-dividends-for-2025/
  - United Housing unveils EGP 5.9bn mixed-use project in Alexandria: https://english.mubasher.info/news/4540667/United-Housing-unveils-EGP-5-9bn-mixed-use-project-in-Alexandria/
  - United Housing’s consolidated net profits exceed EGP 174.5m in 9M-25: https://english.mubasher.info/news/4530945/United-Housing-s-consolidated-net-profits-exceed-EGP-174-5m-in-9M-25/

## Warnings
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for WKOL.CA matches the company but no source/report date was detected.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for AALR.CA matches the company but no source/report date was detected.
- Evidence rejected for HELI.CA: source text did not clearly match HELI.CA / Heliopolis Housing.
- Evidence for UNIT.CA matches the company but appears old; latest detected date is 2025-01-01.
