# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-23T10:18:41.714367+00:00
Generated Cairo: 2026-09-23 13:18
Run timing: target 08:45 Cairo | generated Cairo 2026-09-23 13:18 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-23 13:15

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 174/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, September 23
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 26.32% / above MA50 57.89%
- EGX70 regime: BEARISH / above MA20 25.64% / above MA50 43.59%
- Sector breadth: 38.1%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=430022560.0 spike=0.69 score=11.4
- CCAP.CA: liquidity=323950816.0 spike=0.38 score=18.4
- ORHD.CA: liquidity=250196400.0 spike=1.84 score=15.44
- ETEL.CA: liquidity=153972992.0 spike=0.61 score=23.4
- OFH.CA: liquidity=142000928.0 spike=1.14 score=4.49

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth; sector breadth is 38% and risk mode is defensive, so the scanner holds all positions and highlights top tickets based on liquidity, sector strength, and technical levels.
- Top tickets (ATQA.CA, SAUD.CA, ETEL.CA, MPCO.CA) show tradeable liquidity but mixed outlooks—some constructive, some bullish watch—while RSI indicates extended momentum.
- Support/resistance gaps vary: ATQA.CA sits ~18% below its 20‑day support and 5.5% below resistance; ETEL.CA is far above support with resistance slightly below price, limiting upside room.
- Leading sectors Telecommunications, Agriculture & Food Production, and Energy & Petrochemicals have strong above‑MA20/50 percentages, yet overall market breadth remains defensive, limiting new buy signals.
- Given the bearish EGX30/EGX70 regime and defensive risk mode, the scanner maintains HOLD on all tickets; uncertainty remains due to cooling liquidity spikes and mixed technical signals.

## Top Liquidity Spikes
- MAAL.CA: spike=4.53 liquidity=53189612.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGTS.CA: spike=3.19 liquidity=71711832.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=2.73 liquidity=104697736.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- POUL.CA: spike=2.28 liquidity=58845364.0 outlook=WEAK_OR_RISKY score=26 buy_ready=False
- ORHD.CA: spike=1.84 liquidity=250196400.0 outlook=NEUTRAL score=42 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=9.98 5d=2.98% 20d=9.42% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=8.38 5d=5.68% 20d=12.05% aboveMA50=50.0%
- #3 Energy & Petrochemicals: score=7.89 5d=4.48% 20d=3.4% aboveMA50=100.0%
- #4 Investment Holding: score=7.56 5d=0.93% 20d=13.09% aboveMA50=66.67%
- #5 Banking & Financials: score=6.05 5d=2.82% 20d=4.7% aboveMA50=50.0%
- #6 Transportation & Logistics: score=5.65 5d=5.21% 20d=1.09% aboveMA50=50.0%
- #7 Tourism & Leisure: score=5.23 5d=-2.68% 20d=-3.23% aboveMA50=100.0%
- #8 Fintech & Payments: score=4.68 5d=-0.27% 20d=-2.71% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- AMOC.CA: BULLISH_WATCH score=83.89 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- SAUD.CA: BULLISH_WATCH score=82.05 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- EXPA.CA: BULLISH_WATCH score=76.05 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- HDBK.CA: BULLISH_WATCH score=72.05 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- GSSC.CA: BULLISH_WATCH score=71.52 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- KZPC.CA: BULLISH_WATCH score=71.52 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- HELI.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading
- FWRY.CA: CONSTRUCTIVE score=69.68 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ATQA.CA: CONSTRUCTIVE score=69.37 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended; sector is not leading
- ORWE.CA: CONSTRUCTIVE score=66.59 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CICH.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=17.21 buy_ready=False sector_rank=16 price=292.93 support=288.01 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=41.82 liquidity=16439710.0 spike=0.65
- ABUK.CA: score=22.75 buy_ready=False sector_rank=9 price=92.55 support=75.01 resistance=96.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=59.62 liquidity=87903600.0 spike=0.48
- ACAMD.CA: score=16.21 buy_ready=False sector_rank=16 price=2.0 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=16167544.0 spike=0.29
- ACGC.CA: score=9.87 buy_ready=False sector_rank=13 price=13.95 support=13.55 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=48.89 liquidity=2231031.5 spike=0.07
- ADCI.CA: score=4.44 buy_ready=False sector_rank=16 price=284.28 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=20.86 liquidity=2230641.5 spike=0.46
- ADIB.CA: score=16.4 buy_ready=False sector_rank=5 price=51.95 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=51672124.0 spike=0.66
- ADPC.CA: score=16.21 buy_ready=False sector_rank=16 price=3.98 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=10769468.0 spike=0.6
- AFDI.CA: score=0.77 buy_ready=False sector_rank=16 price=52.12 support=51.6 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=1562395.0 spike=0.06
- AFMC.CA: score=9.19 buy_ready=False sector_rank=16 price=158.68 support=153.0 resistance=239.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=35.79 liquidity=4981762.5 spike=0.08
- AJWA.CA: score=10.82 buy_ready=False sector_rank=16 price=179.12 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=47.21 liquidity=6611905.5 spike=0.15
- ALCN.CA: score=23.26 buy_ready=False sector_rank=6 price=33.89 support=30.03 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=62.47 liquidity=10537524.0 spike=0.3
- ALUM.CA: score=2.99 buy_ready=False sector_rank=16 price=24.87 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=30.52 liquidity=3786978.0 spike=0.27
- AMER.CA: score=13.76 buy_ready=False sector_rank=20 price=5.19 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=40.37 liquidity=15012661.0 spike=0.27
- AMES.CA: score=8.21 buy_ready=False sector_rank=16 price=50.43 support=48.45 resistance=158.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=9.27 liquidity=33857584.0 spike=0.13
- AMIA.CA: score=5.29 buy_ready=False sector_rank=16 price=18.49 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=33.83 liquidity=3077839.25 spike=0.06
- AMOC.CA: score=22.4 buy_ready=False sector_rank=3 price=13.5 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=56.3 liquidity=39948236.0 spike=0.22
- APSW.CA: score=-0.16 buy_ready=False sector_rank=16 price=8.3 support=8.2 resistance=8.79 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=34.38 liquidity=1113868.33 spike=1.26
- ARAB.CA: score=8.76 buy_ready=False sector_rank=20 price=0.24 support=0.24 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=32.61 liquidity=35818312.0 spike=0.35
- ARCC.CA: score=11.4 buy_ready=False sector_rank=21 price=69.0 support=69.0 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=20.43 liquidity=12885821.0 spike=0.33
- AREH.CA: score=9.19 buy_ready=False sector_rank=16 price=1.42 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=4985221.0 spike=0.34
- ASCM.CA: score=3.82 buy_ready=False sector_rank=16 price=57.68 support=58.16 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=31.4 liquidity=4615574.5 spike=0.24
- ASPI.CA: score=14.21 buy_ready=False sector_rank=16 price=0.42 support=0.41 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=17972392.0 spike=0.29
- ATLC.CA: score=11.69 buy_ready=False sector_rank=12 price=7.02 support=5.35 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=1839286.13 spike=0.06
- ATQA.CA: score=24.75 buy_ready=False sector_rank=9 price=12.98 support=11.0 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=64.31 liquidity=31227168.0 spike=0.28
- AXPH.CA: score=11.99 buy_ready=False sector_rank=16 price=1683.32 support=1501.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=36.72 liquidity=2781340.25 spike=0.3
- BINV.CA: score=1.81 buy_ready=False sector_rank=4 price=56.28 support=56.1 resistance=57.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5414340.0 spike=0.22
- BIOC.CA: score=7.17 buy_ready=False sector_rank=16 price=271.12 support=247.03 resistance=488.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=26.38 liquidity=7957316.5 spike=0.08
- BTFH.CA: score=15.85 buy_ready=False sector_rank=12 price=2.89 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=61034004.0 spike=0.75
- CAED.CA: score=1.62 buy_ready=False sector_rank=16 price=122.48 support=122.6 resistance=173.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=32.49 liquidity=2415748.5 spike=0.1
- CANA.CA: score=20.74 buy_ready=False sector_rank=5 price=46.62 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=70.58 liquidity=7342000.0 spike=0.32
- CCAP.CA: score=18.4 buy_ready=False sector_rank=4 price=7.25 support=5.72 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=323950816.0 spike=0.38
- CCRS.CA: score=14.48 buy_ready=False sector_rank=16 price=2.59 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=5273278.5 spike=0.09
- CEFM.CA: score=7.61 buy_ready=False sector_rank=16 price=143.81 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=43.55 liquidity=398382.13 spike=0.04
- CERA.CA: score=14.21 buy_ready=False sector_rank=16 price=1.38 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=34935884.0 spike=0.28
- CFGH.CA: score=7.22 buy_ready=False sector_rank=16 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=8967.17 spike=0.54
- CIEB.CA: score=15.29 buy_ready=False sector_rank=5 price=24.56 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=8886386.0 spike=0.65
- CIRA.CA: score=19.71 buy_ready=False sector_rank=10 price=40.0 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=75.87 liquidity=10427440.0 spike=0.26
- CLHO.CA: score=8.76 buy_ready=False sector_rank=19 price=15.8 support=15.4 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=12.13 liquidity=20356404.0 spike=0.28
- CNFN.CA: score=2.04 buy_ready=False sector_rank=12 price=4.48 support=4.46 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=30.59 liquidity=3183942.0 spike=0.27
- COMI.CA: score=11.4 buy_ready=False sector_rank=5 price=129.54 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=32.85 liquidity=430022560.0 spike=0.69
- COPR.CA: score=15.11 buy_ready=False sector_rank=16 price=0.49 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=45.4 liquidity=7906829.0 spike=0.17
- COSG.CA: score=14.21 buy_ready=False sector_rank=16 price=1.74 support=1.78 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=14302048.0 spike=0.42
- CPCI.CA: score=11.85 buy_ready=False sector_rank=16 price=564.85 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=60.45 liquidity=638297.69 spike=0.19
- CSAG.CA: score=3.7 buy_ready=False sector_rank=6 price=37.65 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=27.53 liquidity=2441184.75 spike=0.16
- DAPH.CA: score=9.21 buy_ready=False sector_rank=16 price=111.02 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=21.49 liquidity=16365233.0 spike=0.28
- DEIN.CA: score=7.21 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=1.34 buy_ready=False sector_rank=18 price=26.0 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=26.65 liquidity=2447981.75 spike=0.46
- DSCW.CA: score=2.48 buy_ready=False sector_rank=16 price=1.78 support=1.77 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=4269833.5 spike=0.14
- DTPP.CA: score=19.21 buy_ready=False sector_rank=16 price=333.96 support=294.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=57.6 liquidity=53702036.0 spike=0.72
- EALR.CA: score=2.77 buy_ready=False sector_rank=16 price=367.56 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=33.51 liquidity=3566950.25 spike=0.25
- EASB.CA: score=18.01 buy_ready=False sector_rank=16 price=8.12 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=55.61 liquidity=8797800.0 spike=0.52
- EAST.CA: score=6.54 buy_ready=False sector_rank=18 price=31.9 support=31.31 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=11.07 liquidity=8644763.0 spike=0.11
- EBSC.CA: score=0.69 buy_ready=False sector_rank=16 price=1.97 support=1.91 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=30.26 liquidity=1484112.63 spike=0.1
- ECAP.CA: score=5.59 buy_ready=False sector_rank=16 price=31.96 support=31.16 resistance=36.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=46.37 liquidity=1382083.5 spike=0.12
- EDFM.CA: score=4.62 buy_ready=False sector_rank=16 price=391.75 support=390.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=409026.75 spike=0.23
- EEII.CA: score=9.21 buy_ready=False sector_rank=16 price=2.3 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=14586784.0 spike=0.94
- EFIC.CA: score=14.62 buy_ready=False sector_rank=9 price=185.13 support=183.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=9868797.0 spike=0.03
- EFID.CA: score=16.9 buy_ready=False sector_rank=18 price=30.4 support=29.71 resistance=32.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=53.36 liquidity=27320534.0 spike=0.41
- EFIH.CA: score=18.87 buy_ready=False sector_rank=8 price=23.47 support=22.16 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=32185386.0 spike=0.54
- EGAL.CA: score=18.75 buy_ready=False sector_rank=9 price=363.5 support=345.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=52.02 liquidity=15407921.0 spike=0.15
- EGAS.CA: score=13.72 buy_ready=False sector_rank=3 price=57.33 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=3320821.5 spike=0.28
- EGBE.CA: score=1.45 buy_ready=False sector_rank=5 price=0.5 support=0.49 resistance=0.55 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=52386.68 spike=0.73
- EGCH.CA: score=18.75 buy_ready=False sector_rank=9 price=13.8 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=31247364.0 spike=0.26
- EGSA.CA: score=11.4 buy_ready=False sector_rank=1 price=9.0 support=8.68 resistance=9.1 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=3654.0 spike=0.59
- EGTS.CA: score=8.14 buy_ready=False sector_rank=20 price=18.71 support=18.4 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=71711832.0 spike=3.19
- EHDR.CA: score=1.49 buy_ready=False sector_rank=16 price=2.65 support=2.65 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=2284726.25 spike=0.12
- ELEC.CA: score=8.37 buy_ready=False sector_rank=15 price=1.96 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=18257942.0 spike=0.23
- ELKA.CA: score=3.25 buy_ready=False sector_rank=16 price=1.65 support=1.64 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=13.16 liquidity=4041947.5 spike=0.11
- ELNA.CA: score=-1.64 buy_ready=False sector_rank=16 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=24.57 liquidity=154827.13 spike=0.42
- ELSH.CA: score=9.82 buy_ready=False sector_rank=16 price=12.52 support=12.55 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=5613697.5 spike=0.15
- ELWA.CA: score=-0.06 buy_ready=False sector_rank=16 price=1.68 support=1.66 resistance=1.99 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=28.95 liquidity=730020.46 spike=0.36
- EMFD.CA: score=16.76 buy_ready=False sector_rank=20 price=13.29 support=12.1 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=32599908.0 spike=0.2
- ENGC.CA: score=14.21 buy_ready=False sector_rank=16 price=42.13 support=41.0 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=49.72 liquidity=15660486.0 spike=0.97
- EOSB.CA: score=9.68 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=76532.79 spike=1.2
- EPCO.CA: score=6.62 buy_ready=False sector_rank=16 price=10.66 support=10.6 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=2413324.5 spike=0.15
- EPPK.CA: score=-5.37 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.4 buy_ready=False sector_rank=1 price=139.05 support=112.5 resistance=136.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=85.57 liquidity=153972992.0 spike=0.61
- ETRS.CA: score=6.24 buy_ready=False sector_rank=16 price=10.78 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=35.51 liquidity=2028923.13 spike=0.14
- EXPA.CA: score=23.4 buy_ready=False sector_rank=5 price=21.9 support=19.96 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=25000534.0 spike=0.7
- FAIT.CA: score=10.74 buy_ready=False sector_rank=5 price=46.51 support=41.52 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=67.5 liquidity=1335179.63 spike=0.16
- FAITA.CA: score=6.42 buy_ready=False sector_rank=5 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=41.18 liquidity=16085.14 spike=0.33
- FERC.CA: score=11.08 buy_ready=False sector_rank=9 price=77.9 support=77.3 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=4333932.5 spike=0.29
- FWRY.CA: score=20.87 buy_ready=False sector_rank=8 price=19.1 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=48.24 liquidity=78361928.0 spike=0.57
- GBCO.CA: score=22.7 buy_ready=False sector_rank=11 price=31.4 support=27.51 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=34748256.0 spike=0.5
- GDWA.CA: score=8.21 buy_ready=False sector_rank=16 price=0.74 support=0.75 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=13.22 liquidity=25288120.0 spike=0.58
- GGCC.CA: score=13.98 buy_ready=False sector_rank=16 price=0.8 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9767444.0 spike=0.3
- GIHD.CA: score=19.21 buy_ready=False sector_rank=16 price=75.12 support=61.61 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=50.29 liquidity=10649363.0 spike=0.38
- GMCI.CA: score=-0.78 buy_ready=False sector_rank=16 price=1.72 support=1.69 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=591021.0 spike=1.21
- GRCA.CA: score=8.21 buy_ready=False sector_rank=16 price=41.05 support=38.7 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=20.93 liquidity=19201222.0 spike=0.3
- GSSC.CA: score=12.29 buy_ready=False sector_rank=16 price=306.85 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=61.87 liquidity=1079803.0 spike=0.12
- GTWL.CA: score=19.21 buy_ready=False sector_rank=16 price=233.01 support=201.3 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=53493684.0 spike=0.27
- HDBK.CA: score=23.01 buy_ready=False sector_rank=5 price=114.88 support=90.51 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=52.79 liquidity=9611079.0 spike=0.16
- HELI.CA: score=20.76 buy_ready=False sector_rank=20 price=8.14 support=7.34 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=82384264.0 spike=0.48
- HRHO.CA: score=8.85 buy_ready=False sector_rank=12 price=24.51 support=24.83 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=32391262.0 spike=0.32
- ICID.CA: score=17.63 buy_ready=False sector_rank=16 price=16.98 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=14519897.0 spike=1.21
- IDRE.CA: score=14.12 buy_ready=False sector_rank=16 price=53.85 support=51.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=47.86 liquidity=4916112.5 spike=0.3
- IFAP.CA: score=14.65 buy_ready=False sector_rank=2 price=20.35 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=40.05 liquidity=6252338.0 spike=0.27
- INFI.CA: score=5.75 buy_ready=False sector_rank=16 price=126.48 support=123.0 resistance=168.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=19.11 liquidity=6545830.5 spike=0.23
- IRON.CA: score=2.71 buy_ready=False sector_rank=9 price=27.04 support=26.3 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=24.29 liquidity=2963945.5 spike=0.21
- ISMA.CA: score=6.46 buy_ready=False sector_rank=16 price=29.59 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=35.67 liquidity=2247237.5 spike=0.1
- ISMQ.CA: score=7.93 buy_ready=False sector_rank=9 price=8.69 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=32.39 liquidity=7185936.0 spike=0.28
- ISPH.CA: score=6.11 buy_ready=False sector_rank=19 price=12.1 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=7350398.0 spike=0.1
- JUFO.CA: score=8.95 buy_ready=False sector_rank=18 price=26.99 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=49.83 liquidity=4053176.25 spike=0.19
- KABO.CA: score=10.63 buy_ready=False sector_rank=13 price=9.12 support=8.9 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=45.27 liquidity=2993708.75 spike=0.07
- KWIN.CA: score=9.21 buy_ready=False sector_rank=16 price=90.98 support=82.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=18.91 liquidity=24539428.0 spike=0.46
- KZPC.CA: score=10.41 buy_ready=False sector_rank=16 price=13.7 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=1197248.25 spike=0.03
- LCSW.CA: score=1.0 buy_ready=False sector_rank=21 price=32.45 support=31.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=25.24 liquidity=2597381.5 spike=0.11
- LUTS.CA: score=17.21 buy_ready=False sector_rank=16 price=0.89 support=0.83 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=40.2 liquidity=11466415.0 spike=0.06
- MAAL.CA: score=9.21 buy_ready=False sector_rank=16 price=9.93 support=9.03 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53189612.0 spike=4.53
- MASR.CA: score=14.21 buy_ready=False sector_rank=16 price=7.65 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=15449755.0 spike=0.16
- MBSC.CA: score=11.4 buy_ready=False sector_rank=21 price=342.0 support=340.66 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=20.64 liquidity=20532972.0 spike=0.42
- MCQE.CA: score=8.0 buy_ready=False sector_rank=21 price=206.91 support=207.1 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=23.89 liquidity=9595556.0 spike=0.31
- MCRO.CA: score=19.21 buy_ready=False sector_rank=16 price=1.65 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=26863486.0 spike=0.22
- MENA.CA: score=4.32 buy_ready=False sector_rank=20 price=6.59 support=6.58 resistance=7.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=38.32 liquidity=561283.13 spike=0.3
- MEPA.CA: score=7.63 buy_ready=False sector_rank=16 price=1.87 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=46.91 liquidity=3422147.0 spike=0.09
- MFPC.CA: score=17.75 buy_ready=False sector_rank=9 price=48.0 support=39.02 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=76.27 liquidity=39212096.0 spike=0.22
- MFSC.CA: score=6.42 buy_ready=False sector_rank=16 price=48.96 support=48.5 resistance=58.9 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=44.06 liquidity=2212355.48 spike=0.46
- MHOT.CA: score=11.19 buy_ready=False sector_rank=7 price=18.21 support=16.61 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=27.1 liquidity=6102946.0 spike=0.63
- MICH.CA: score=10.44 buy_ready=False sector_rank=16 price=46.51 support=47.51 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=6229210.0 spike=0.39
- MILS.CA: score=8.01 buy_ready=False sector_rank=16 price=189.34 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=3804526.75 spike=0.14
- MIPH.CA: score=-0.68 buy_ready=False sector_rank=19 price=848.03 support=811.11 resistance=915.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5563246.0 spike=0.69
- MOED.CA: score=8.21 buy_ready=False sector_rank=16 price=0.72 support=0.7 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=22.78 liquidity=10746133.0 spike=0.14
- MOIL.CA: score=14.66 buy_ready=False sector_rank=3 price=0.7 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=220064.0 spike=1.02
- MOIN.CA: score=9.81 buy_ready=False sector_rank=16 price=35.56 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=54.45 liquidity=2598041.0 spike=0.08
- MOSC.CA: score=-0.49 buy_ready=False sector_rank=16 price=301.3 support=290.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=32.83 liquidity=301297.38 spike=0.04
- MPCI.CA: score=12.21 buy_ready=False sector_rank=16 price=390.08 support=371.11 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=16.95 liquidity=47872848.0 spike=0.33
- MPCO.CA: score=23.4 buy_ready=False sector_rank=2 price=2.73 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=72.25 liquidity=111427280.0 spike=0.65
- MPRC.CA: score=9.21 buy_ready=False sector_rank=16 price=39.0 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=30.87 liquidity=18116242.0 spike=0.45
- MTIE.CA: score=7.47 buy_ready=False sector_rank=11 price=8.23 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=7776084.5 spike=0.24
- NAHO.CA: score=-5.57 buy_ready=False sector_rank=16 price=0.13 support=0.13 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60967.32 spike=1.08
- NCCW.CA: score=21.21 buy_ready=False sector_rank=16 price=7.53 support=5.77 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=63.95 liquidity=64406924.0 spike=0.98
- NEDA.CA: score=7.02 buy_ready=False sector_rank=16 price=2.77 support=2.7 resistance=2.89 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=56.25 liquidity=655251.81 spike=1.08
- NHPS.CA: score=4.81 buy_ready=False sector_rank=16 price=80.61 support=73.63 resistance=80.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22548632.0 spike=1.3
- NINH.CA: score=1.75 buy_ready=False sector_rank=16 price=20.23 support=20.3 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=2539614.75 spike=0.08
- NIPH.CA: score=3.76 buy_ready=False sector_rank=19 price=334.19 support=333.12 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=80879600.0 spike=0.54
- OBRI.CA: score=1.94 buy_ready=False sector_rank=16 price=29.65 support=29.51 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=3727815.75 spike=0.24
- OCDI.CA: score=13.76 buy_ready=False sector_rank=20 price=28.81 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=42.29 liquidity=16204998.0 spike=0.2
- OCPH.CA: score=2.14 buy_ready=False sector_rank=16 price=235.25 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=1935379.38 spike=0.29
- ODIN.CA: score=5.59 buy_ready=False sector_rank=16 price=2.77 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=6378046.0 spike=0.29
- OFH.CA: score=4.49 buy_ready=False sector_rank=16 price=1.11 support=1.07 resistance=1.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=142000928.0 spike=1.14
- OIH.CA: score=19.4 buy_ready=False sector_rank=4 price=2.14 support=1.91 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=45649792.0 spike=0.38
- OLFI.CA: score=8.67 buy_ready=False sector_rank=18 price=22.64 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=4769060.5 spike=0.27
- ORAS.CA: score=4.6 buy_ready=False sector_rank=14 price=838.01 support=837.02 resistance=847.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43293616.0 spike=1.0
- ORHD.CA: score=15.44 buy_ready=False sector_rank=20 price=41.0 support=40.85 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=250196400.0 spike=1.84
- ORWE.CA: score=19.64 buy_ready=False sector_rank=13 price=27.55 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=52.06 liquidity=20424214.0 spike=0.36
- PHAR.CA: score=8.76 buy_ready=False sector_rank=19 price=114.43 support=111.55 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=26.6 liquidity=17588516.0 spike=0.16
- PHDC.CA: score=8.76 buy_ready=False sector_rank=20 price=13.42 support=12.91 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=22.14 liquidity=29781588.0 spike=0.18
- PHTV.CA: score=7.73 buy_ready=False sector_rank=16 price=346.85 support=311.27 resistance=378.89 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=49.26 liquidity=523049.81 spike=0.32
- POUL.CA: score=16.46 buy_ready=False sector_rank=18 price=38.55 support=37.15 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=21 September 01:28 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=58845364.0 spike=2.28
- PRCL.CA: score=6.95 buy_ready=False sector_rank=21 price=31.19 support=30.61 resistance=34.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=3551252.5 spike=0.19
- PRDC.CA: score=8.76 buy_ready=False sector_rank=20 price=7.55 support=7.51 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=9.33 liquidity=19661072.0 spike=0.33
- PRMH.CA: score=5.05 buy_ready=False sector_rank=16 price=2.56 support=2.32 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=846553.5 spike=0.08
- RACC.CA: score=6.3 buy_ready=False sector_rank=16 price=9.55 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=50.44 liquidity=2092773.38 spike=0.12
- RAKT.CA: score=3.29 buy_ready=False sector_rank=16 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=81607.68 spike=0.37
- RAYA.CA: score=13.96 buy_ready=False sector_rank=17 price=7.1 support=6.8 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=28557214.0 spike=0.53
- RMDA.CA: score=16.76 buy_ready=False sector_rank=19 price=6.02 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13280339.0 spike=0.23
- ROTO.CA: score=1.17 buy_ready=False sector_rank=16 price=39.99 support=35.02 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=24.67 liquidity=1957171.13 spike=0.23
- RREI.CA: score=11.31 buy_ready=False sector_rank=16 price=4.11 support=4.2 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=40.62 liquidity=7106876.0 spike=0.4
- RTVC.CA: score=1.54 buy_ready=False sector_rank=16 price=3.85 support=3.79 resistance=4.36 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=27.69 liquidity=2331309.69 spike=0.56
- RUBX.CA: score=7.67 buy_ready=False sector_rank=16 price=16.94 support=15.44 resistance=16.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=104697736.0 spike=2.73
- SAUD.CA: score=23.4 buy_ready=False sector_rank=5 price=24.64 support=22.7 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=65.55 liquidity=13523858.0 spike=0.74
- SCEM.CA: score=8.4 buy_ready=False sector_rank=21 price=86.02 support=87.02 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=14308576.0 spike=0.13
- SCFM.CA: score=-0.06 buy_ready=False sector_rank=16 price=269.43 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=34.9 liquidity=727386.88 spike=0.1
- SCTS.CA: score=2.38 buy_ready=False sector_rank=10 price=575.7 support=566.66 resistance=640.0 source=Yahoo Finance as_of=2026-09-20T21:00:00+00:00 freshness=FRESH RSI=22.63 liquidity=1671832.84 spike=0.62
- SDTI.CA: score=9.56 buy_ready=False sector_rank=16 price=77.7 support=67.0 resistance=79.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=75.63 liquidity=3353167.0 spike=0.13
- SEIG.CA: score=-0.16 buy_ready=False sector_rank=16 price=233.99 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=29.74 liquidity=630201.06 spike=0.37
- SIPC.CA: score=17.21 buy_ready=False sector_rank=16 price=5.46 support=4.1 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=14906356.0 spike=0.21
- SKPC.CA: score=18.75 buy_ready=False sector_rank=9 price=17.69 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=52.39 liquidity=27546010.0 spike=0.21
- SMFR.CA: score=1.23 buy_ready=False sector_rank=16 price=231.51 support=226.1 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=26.93 liquidity=2022378.5 spike=0.25
- SNFC.CA: score=11.62 buy_ready=False sector_rank=16 price=11.5 support=10.26 resistance=11.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=79.25 liquidity=3408617.75 spike=0.22
- SPIN.CA: score=4.62 buy_ready=False sector_rank=13 price=17.14 support=16.1 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=24.6 liquidity=4983162.0 spike=0.36
- SPMD.CA: score=14.21 buy_ready=False sector_rank=16 price=0.43 support=0.41 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=47.24 liquidity=26600866.0 spike=0.36
- SUGR.CA: score=9.12 buy_ready=False sector_rank=18 price=58.14 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=2223289.0 spike=0.03
- SVCE.CA: score=17.21 buy_ready=False sector_rank=16 price=11.2 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=26661336.0 spike=0.13
- SWDY.CA: score=17.37 buy_ready=False sector_rank=15 price=125.37 support=122.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=13490556.0 spike=0.19
- TALM.CA: score=20.71 buy_ready=False sector_rank=10 price=20.9 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=17987790.0 spike=0.27
- TMGH.CA: score=13.76 buy_ready=False sector_rank=20 price=93.06 support=93.08 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=37.73 liquidity=109034064.0 spike=0.38
- TRTO.CA: score=7.22 buy_ready=False sector_rank=16 price=0.06 support=0.05 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=12730.4 spike=0.45
- UEFM.CA: score=-0.74 buy_ready=False sector_rank=16 price=477.16 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=32.59 liquidity=1056273.25 spike=0.35
- UEGC.CA: score=4.21 buy_ready=False sector_rank=16 price=1.64 support=1.61 resistance=1.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29357702.0 spike=0.58
- UNIP.CA: score=8.26 buy_ready=False sector_rank=16 price=0.37 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=4048192.5 spike=0.17
- UNIT.CA: score=4.59 buy_ready=False sector_rank=20 price=17.94 support=17.12 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=47.79 liquidity=830185.56 spike=0.06
- WCDF.CA: score=9.76 buy_ready=False sector_rank=16 price=702.8 support=636.31 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=67.72 liquidity=547864.25 spike=0.11
- WKOL.CA: score=10.91 buy_ready=False sector_rank=16 price=333.01 support=325.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=45.17 liquidity=3702454.0 spike=0.25
- ZEOT.CA: score=6.86 buy_ready=False sector_rank=16 price=13.02 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=37.68 liquidity=2654597.75 spike=0.41
- ZMID.CA: score=16.76 buy_ready=False sector_rank=20 price=8.35 support=7.9 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=68158288.0 spike=0.32

## Backtesting Lite
- ATQA.CA: 180d return=35.29%, max drawdown=-20.73%, MA20>MA50 days last20=20, as_of=2026-09-20T21:00:00+00:00
- SAUD.CA: 180d return=76.78%, max drawdown=-19.12%, MA20>MA50 days last20=20, as_of=2026-09-20T21:00:00+00:00
- ETEL.CA: 180d return=98.54%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-20T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=630 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=630 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/

## Warnings
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence for ABUK.CA matches the company but no source/report date was detected.
