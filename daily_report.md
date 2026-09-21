# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-21T12:45:03.906047+00:00
Generated Cairo: 2026-09-21 15:45
Run timing: target 09:15 Cairo | generated Cairo 2026-09-21 15:45 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-21 15:41

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 168/187
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, September 21
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 27.78% / above MA50 55.56%
- EGX70 regime: BEARISH / above MA20 32.5% / above MA50 52.5%
- Sector breadth: 47.62%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=918258048.0 spike=1.57 score=17.39
- CCAP.CA: liquidity=825709504.0 spike=0.94 score=23.4
- ETEL.CA: liquidity=374448704.0 spike=1.57 score=21.54
- TMGH.CA: liquidity=326362752.0 spike=1.16 score=14.87
- RUBX.CA: liquidity=308824832.0 spike=12.7 score=9.72

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 both BEARISH with sector breadth ~48%; risk mode DEFENSIVE_NO_NEW_BUY, so scanner keeps HOLD despite accumulation spikes in several tickets.
- Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.
- EGX30/EGX70 bearish, sector breadth 47.6%, defensive risk mode; scanner flags accumulation spikes in select stocks but maintains HOLD due to weak breadth and extended momentum.
- Tickets like GBCO.CA, SAUD.CA show ACCUMULATION_SPIKE liquidity and BULLISH_WATCH outlook, but prices sit 4‑12% below 20‑day support and RSI >60, indicating limited near‑term upside.
- Sector breadth is weak (only 48% of stocks above MA20) and leading sectors (Investment Holding, Telecom, Education) are not broadly represented, reinforcing defensive stance.
- EGX30/EGX70 bearish trend and low median 5‑day returns shift risk mode to DEFENSIVE_NO_NEW_BUY, overriding individual bullish signals and keeping confidence LOW.

## Top Liquidity Spikes
- MIPH.CA: spike=19.25 liquidity=81043648.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SAUD.CA: spike=16.89 liquidity=172021024.0 outlook=BULLISH_WATCH score=79.63 buy_ready=False
- RUBX.CA: spike=12.7 liquidity=308824832.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ENGC.CA: spike=4.02 liquidity=57307380.0 outlook=NEUTRAL score=49.81 buy_ready=False
- NAHO.CA: spike=3.84 liquidity=187824.81 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=18.25 5d=14.92% 20d=25.26% aboveMA50=100.0%
- #2 Telecommunications: score=9.47 5d=1.54% 20d=7.28% aboveMA50=100.0%
- #3 Education: score=9.23 5d=5.08% 20d=7.28% aboveMA50=66.67%
- #4 Agriculture & Food Production: score=8.47 5d=3.31% 20d=12.34% aboveMA50=50.0%
- #5 Energy & Petrochemicals: score=7.61 5d=3.7% 20d=2.79% aboveMA50=66.67%
- #6 Basic Resources & Chemicals: score=6.64 5d=1.6% 20d=5.38% aboveMA50=70.0%
- #7 Automotive & Distribution: score=6.13 5d=1.96% 20d=3.12% aboveMA50=50.0%
- #8 Transportation & Logistics: score=5.97 5d=1.22% 20d=-2.53% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- GBCO.CA: BULLISH_WATCH score=93.13 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- CICH.CA: BULLISH_WATCH score=92.2 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EGCH.CA: BULLISH_WATCH score=87.64 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ATQA.CA: BULLISH_WATCH score=83.64 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- EGAL.CA: BULLISH_WATCH score=82.64 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- FERC.CA: BULLISH_WATCH score=82.64 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- TALM.CA: BULLISH_WATCH score=82.23 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- ALCN.CA: BULLISH_WATCH score=81.97 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EXPA.CA: BULLISH_WATCH score=81.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- CPCI.CA: BULLISH_WATCH score=79.81 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=5.36 buy_ready=False sector_rank=13 price=290.97 support=288.01 resistance=308.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34653132.0 spike=1.32
- ABUK.CA: score=19.4 buy_ready=False sector_rank=6 price=93.89 support=75.01 resistance=96.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.11 liquidity=124005960.0 spike=0.7
- ACAMD.CA: score=16.72 buy_ready=False sector_rank=13 price=2.04 support=1.95 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=37970376.0 spike=0.65
- ACGC.CA: score=18.1 buy_ready=False sector_rank=12 price=14.02 support=13.4 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=14100547.0 spike=0.4
- ADCI.CA: score=3.77 buy_ready=False sector_rank=13 price=277.22 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.17 liquidity=4044764.5 spike=0.76
- ADIB.CA: score=19.25 buy_ready=False sector_rank=9 price=52.02 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.76 liquidity=57782724.0 spike=0.75
- ADPC.CA: score=18.38 buy_ready=False sector_rank=13 price=3.93 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.14 liquidity=32106586.0 spike=1.83
- AFDI.CA: score=4.72 buy_ready=False sector_rank=13 price=52.11 support=51.94 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11545562.0 spike=0.47
- AFMC.CA: score=14.72 buy_ready=False sector_rank=13 price=158.98 support=153.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.65 liquidity=19623598.0 spike=0.32
- AJWA.CA: score=13.04 buy_ready=False sector_rank=13 price=179.08 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.42 liquidity=8318282.5 spike=0.18
- ALCN.CA: score=24.45 buy_ready=False sector_rank=8 price=33.96 support=30.03 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.05 liquidity=52533312.0 spike=1.53
- ALUM.CA: score=10.71 buy_ready=False sector_rank=13 price=25.51 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=5989424.5 spike=0.43
- AMER.CA: score=14.55 buy_ready=False sector_rank=16 price=5.16 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=22685812.0 spike=0.4
- AMES.CA: score=4.88 buy_ready=False sector_rank=13 price=53.05 support=48.45 resistance=54.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=279848864.0 spike=1.08
- AMIA.CA: score=17.72 buy_ready=False sector_rank=13 price=18.42 support=17.12 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=10461817.0 spike=0.19
- AMOC.CA: score=19.4 buy_ready=False sector_rank=5 price=13.66 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.26 liquidity=131145928.0 spike=0.74
- APSW.CA: score=5.2 buy_ready=False sector_rank=13 price=8.3 support=8.37 resistance=8.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=1120660.88 spike=1.18
- ARAB.CA: score=14.55 buy_ready=False sector_rank=16 price=0.24 support=0.24 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=50598224.0 spike=0.46
- ARCC.CA: score=17.24 buy_ready=False sector_rank=18 price=70.91 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.95 liquidity=21448600.0 spike=0.54
- AREH.CA: score=14.72 buy_ready=False sector_rank=13 price=1.41 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=11402712.0 spike=0.78
- ASCM.CA: score=14.72 buy_ready=False sector_rank=13 price=59.22 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.27 liquidity=10353350.0 spike=0.52
- ASPI.CA: score=5.06 buy_ready=False sector_rank=13 price=0.43 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=71968568.0 spike=1.17
- ATLC.CA: score=20.68 buy_ready=False sector_rank=10 price=7.01 support=5.35 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=11943713.0 spike=0.4
- ATQA.CA: score=24.9 buy_ready=False sector_rank=6 price=13.52 support=10.87 resistance=13.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.21 liquidity=276954368.0 spike=2.75
- AXPH.CA: score=13.58 buy_ready=False sector_rank=13 price=1650.37 support=1481.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=5853540.0 spike=0.56
- BINV.CA: score=24.4 buy_ready=False sector_rank=1 price=59.28 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=73.98 liquidity=19051032.0 spike=0.82
- BIOC.CA: score=9.72 buy_ready=False sector_rank=13 price=262.91 support=272.01 resistance=506.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.39 liquidity=41986356.0 spike=0.4
- BTFH.CA: score=17.5 buy_ready=False sector_rank=10 price=2.96 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=113623224.0 spike=1.41
- CAED.CA: score=13.17 buy_ready=False sector_rank=13 price=125.14 support=123.56 resistance=173.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=8450398.0 spike=0.34
- CANA.CA: score=26.11 buy_ready=False sector_rank=9 price=47.24 support=41.11 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=74.0 liquidity=52186324.0 spike=2.43
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=7.14 support=5.71 resistance=7.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.6 liquidity=825709504.0 spike=0.94
- CCRS.CA: score=19.72 buy_ready=False sector_rank=13 price=2.68 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=27071040.0 spike=0.49
- CEFM.CA: score=13.05 buy_ready=False sector_rank=13 price=142.0 support=143.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=58.63 liquidity=5323992.5 spike=0.5
- CERA.CA: score=4.72 buy_ready=False sector_rank=13 price=1.38 support=1.36 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98058688.0 spike=0.81
- CFGH.CA: score=7.73 buy_ready=False sector_rank=13 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8947.37 spike=0.45
- CICH.CA: score=25.9 buy_ready=False sector_rank=10 price=13.01 support=12.0 resistance=13.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=15216679.0 spike=2.61
- CIEB.CA: score=19.25 buy_ready=False sector_rank=9 price=24.87 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.47 liquidity=12776962.0 spike=0.95
- CIRA.CA: score=19.72 buy_ready=False sector_rank=3 price=39.86 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=77.16 liquidity=44341448.0 spike=1.16
- CLHO.CA: score=8.32 buy_ready=False sector_rank=21 price=15.75 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.27 liquidity=57873672.0 spike=0.8
- CNFN.CA: score=13.98 buy_ready=False sector_rank=10 price=4.58 support=4.46 resistance=4.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.73 liquidity=9298625.0 spike=0.75
- COMI.CA: score=17.39 buy_ready=False sector_rank=9 price=132.91 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.21 liquidity=918258048.0 spike=1.57
- COPR.CA: score=17.72 buy_ready=False sector_rank=13 price=0.49 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.74 liquidity=42763776.0 spike=0.79
- COSG.CA: score=17.72 buy_ready=False sector_rank=13 price=1.8 support=1.79 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=32345598.0 spike=0.89
- CPCI.CA: score=15.56 buy_ready=False sector_rank=13 price=558.97 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.49 liquidity=3835892.0 spike=0.99
- CSAG.CA: score=16.39 buy_ready=False sector_rank=8 price=38.4 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.7 liquidity=7002356.5 spike=0.45
- DAPH.CA: score=4.72 buy_ready=False sector_rank=13 price=112.73 support=110.0 resistance=121.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30751350.0 spike=0.51
- DEIN.CA: score=7.72 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=5.74 buy_ready=False sector_rank=14 price=25.61 support=26.0 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.6 liquidity=6598016.5 spike=1.27
- DSCW.CA: score=13.72 buy_ready=False sector_rank=13 price=1.8 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.48 liquidity=27722984.0 spike=0.87
- DTPP.CA: score=21.72 buy_ready=False sector_rank=13 price=329.89 support=294.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.85 liquidity=57621312.0 spike=0.78
- EALR.CA: score=12.69 buy_ready=False sector_rank=13 price=366.02 support=340.0 resistance=412.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=7967231.5 spike=0.51
- EASB.CA: score=15.31 buy_ready=False sector_rank=13 price=7.8 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.21 liquidity=5581129.0 spike=0.33
- EAST.CA: score=9.02 buy_ready=False sector_rank=14 price=31.51 support=32.0 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=88454168.0 spike=1.21
- EBSC.CA: score=-1.47 buy_ready=False sector_rank=13 price=1.96 support=1.95 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3804871.5 spike=0.26
- ECAP.CA: score=10.23 buy_ready=False sector_rank=13 price=31.56 support=31.16 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.91 liquidity=5501912.5 spike=0.5
- EDFM.CA: score=6.36 buy_ready=False sector_rank=13 price=397.53 support=399.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=1633590.5 spike=0.9
- EEII.CA: score=13.72 buy_ready=False sector_rank=13 price=2.23 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.41 liquidity=10078370.0 spike=0.56
- EFIC.CA: score=15.4 buy_ready=False sector_rank=6 price=185.35 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.16 liquidity=48586704.0 spike=0.14
- EFID.CA: score=17.6 buy_ready=False sector_rank=14 price=30.78 support=29.71 resistance=33.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.2 liquidity=42741600.0 spike=0.65
- EFIH.CA: score=13.9 buy_ready=False sector_rank=19 price=22.97 support=22.16 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.7 liquidity=56603816.0 spike=0.94
- EGAL.CA: score=21.4 buy_ready=False sector_rank=6 price=367.98 support=335.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=29954588.0 spike=0.29
- EGAS.CA: score=16.5 buy_ready=False sector_rank=5 price=56.31 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=12066576.0 spike=1.05
- EGBE.CA: score=4.3 buy_ready=False sector_rank=9 price=0.51 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.71 liquidity=52672.77 spike=0.61
- EGCH.CA: score=21.72 buy_ready=False sector_rank=6 price=14.0 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.48 liquidity=137919776.0 spike=1.16
- EGSA.CA: score=10.4 buy_ready=False sector_rank=2 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=1800.0 spike=0.29
- EGTS.CA: score=16.55 buy_ready=False sector_rank=16 price=16.9 support=16.51 resistance=17.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.58 liquidity=23464328.0 spike=0.98
- EHDR.CA: score=14.72 buy_ready=False sector_rank=13 price=2.68 support=2.73 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=15964589.0 spike=0.87
- ELEC.CA: score=14.1 buy_ready=False sector_rank=11 price=1.98 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=62506712.0 spike=0.81
- ELKA.CA: score=14.72 buy_ready=False sector_rank=13 price=1.67 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=18147414.0 spike=0.46
- ELNA.CA: score=-0.81 buy_ready=False sector_rank=13 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=24.57 liquidity=383017.51 spike=1.04
- ELSH.CA: score=14.72 buy_ready=False sector_rank=13 price=12.79 support=12.67 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.83 liquidity=31539924.0 spike=0.84
- ELWA.CA: score=0.46 buy_ready=False sector_rank=13 price=1.68 support=1.66 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=28.21 liquidity=733889.38 spike=0.32
- EMFD.CA: score=4.55 buy_ready=False sector_rank=16 price=13.26 support=13.23 resistance=13.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35177620.0 spike=0.2
- ENGC.CA: score=19.72 buy_ready=False sector_rank=13 price=42.64 support=41.0 resistance=48.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.93 liquidity=57307380.0 spike=4.02
- EOSB.CA: score=9.73 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=8211.1 spike=0.11
- EPCO.CA: score=13.27 buy_ready=False sector_rank=13 price=10.82 support=10.8 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.51 liquidity=8545562.0 spike=0.53
- EPPK.CA: score=-4.86 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=21.54 buy_ready=False sector_rank=2 price=135.0 support=112.5 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.54 liquidity=374448704.0 spike=1.57
- ETRS.CA: score=14.76 buy_ready=False sector_rank=13 price=10.78 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.4 liquidity=14124883.0 spike=1.02
- EXPA.CA: score=23.47 buy_ready=False sector_rank=9 price=22.0 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=74663744.0 spike=2.11
- FAIT.CA: score=10.89 buy_ready=False sector_rank=9 price=46.89 support=41.52 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.55 liquidity=1637768.5 spike=0.2
- FAITA.CA: score=6.27 buy_ready=False sector_rank=9 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16085.12 spike=0.31
- FERC.CA: score=19.22 buy_ready=False sector_rank=6 price=79.6 support=77.3 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.62 liquidity=5816023.0 spike=0.39
- FWRY.CA: score=13.9 buy_ready=False sector_rank=19 price=18.99 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.12 liquidity=55017732.0 spike=0.39
- GBCO.CA: score=26.6 buy_ready=False sector_rank=7 price=30.74 support=27.51 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.43 liquidity=105209136.0 spike=1.6
- GDWA.CA: score=13.72 buy_ready=False sector_rank=13 price=0.76 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=37544508.0 spike=0.87
- GGCC.CA: score=14.72 buy_ready=False sector_rank=13 price=0.84 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=18092568.0 spike=0.55
- GIHD.CA: score=19.72 buy_ready=False sector_rank=13 price=72.1 support=61.61 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=21606750.0 spike=0.77
- GMCI.CA: score=-0.91 buy_ready=False sector_rank=13 price=1.76 support=1.69 resistance=1.94 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=32.26 liquidity=370314.56 spike=0.77
- GRCA.CA: score=8.72 buy_ready=False sector_rank=13 price=39.87 support=39.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.01 liquidity=12420920.0 spike=0.17
- GSSC.CA: score=16.11 buy_ready=False sector_rank=13 price=305.98 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=63.21 liquidity=4381052.0 spike=0.46
- GTWL.CA: score=17.72 buy_ready=False sector_rank=13 price=227.53 support=184.01 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=110246544.0 spike=0.54
- HDBK.CA: score=23.25 buy_ready=False sector_rank=9 price=118.54 support=89.77 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.27 liquidity=17492418.0 spike=0.29
- HELI.CA: score=19.55 buy_ready=False sector_rank=16 price=8.03 support=7.34 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.86 liquidity=153355888.0 spike=0.92
- HRHO.CA: score=14.68 buy_ready=False sector_rank=10 price=24.9 support=25.04 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=79890880.0 spike=0.81
- ICID.CA: score=16.89 buy_ready=False sector_rank=13 price=17.12 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.44 liquidity=9169633.0 spike=0.68
- IDRE.CA: score=6.58 buy_ready=False sector_rank=13 price=54.88 support=54.21 resistance=59.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29739876.0 spike=1.93
- IFAP.CA: score=16.4 buy_ready=False sector_rank=4 price=20.02 support=20.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.43 liquidity=15690900.0 spike=0.69
- INFI.CA: score=9.72 buy_ready=False sector_rank=13 price=127.26 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=22.03 liquidity=10027261.0 spike=0.34
- IRON.CA: score=6.16 buy_ready=False sector_rank=6 price=27.52 support=26.3 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=5760729.0 spike=0.4
- ISMA.CA: score=6.26 buy_ready=False sector_rank=13 price=29.35 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.81 liquidity=6537105.5 spike=0.28
- ISMQ.CA: score=16.4 buy_ready=False sector_rank=6 price=8.84 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=20669838.0 spike=0.77
- ISPH.CA: score=8.32 buy_ready=False sector_rank=21 price=12.14 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=53117748.0 spike=0.72
- JUFO.CA: score=19.24 buy_ready=False sector_rank=14 price=27.25 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=27112636.0 spike=1.32
- KABO.CA: score=18.1 buy_ready=False sector_rank=12 price=9.07 support=8.9 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.03 liquidity=23438802.0 spike=0.51
- KWIN.CA: score=9.72 buy_ready=False sector_rank=13 price=87.16 support=85.01 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=19.73 liquidity=11240408.0 spike=0.2
- KZPC.CA: score=15.94 buy_ready=False sector_rank=13 price=13.66 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=69.25 liquidity=8211115.5 spike=0.2
- LCSW.CA: score=14.24 buy_ready=False sector_rank=18 price=32.67 support=32.42 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=17169078.0 spike=0.67
- LUTS.CA: score=17.72 buy_ready=False sector_rank=13 price=0.9 support=0.79 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.08 liquidity=67757072.0 spike=0.33
- MAAL.CA: score=16.88 buy_ready=False sector_rank=13 price=8.66 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=22545716.0 spike=2.08
- MASR.CA: score=14.76 buy_ready=False sector_rank=13 price=7.59 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.71 liquidity=98583408.0 spike=1.02
- MBSC.CA: score=17.24 buy_ready=False sector_rank=18 price=350.0 support=360.0 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.09 liquidity=33124956.0 spike=0.69
- MCQE.CA: score=14.24 buy_ready=False sector_rank=18 price=209.93 support=213.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=21759240.0 spike=0.7
- MCRO.CA: score=17.72 buy_ready=False sector_rank=13 price=1.61 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=55662180.0 spike=0.45
- MENA.CA: score=5.13 buy_ready=False sector_rank=16 price=6.6 support=6.58 resistance=7.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=583447.94 spike=0.3
- MEPA.CA: score=17.72 buy_ready=False sector_rank=13 price=1.91 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=20624402.0 spike=0.53
- MFPC.CA: score=20.06 buy_ready=False sector_rank=6 price=49.7 support=39.02 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=79.77 liquidity=304047392.0 spike=1.83
- MFSC.CA: score=6.97 buy_ready=False sector_rank=13 price=48.96 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.79 liquidity=2241475.75 spike=0.45
- MHOT.CA: score=6.69 buy_ready=False sector_rank=20 price=17.4 support=17.62 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.21 liquidity=3793479.25 spike=0.37
- MICH.CA: score=17.72 buy_ready=False sector_rank=13 price=47.74 support=48.12 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.87 liquidity=13460388.0 spike=0.82
- MILS.CA: score=4.72 buy_ready=False sector_rank=13 price=190.09 support=180.01 resistance=203.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10614555.0 spike=0.36
- MIPH.CA: score=8.32 buy_ready=False sector_rank=21 price=941.03 support=850.03 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81043648.0 spike=19.25
- MOED.CA: score=4.72 buy_ready=False sector_rank=13 price=0.73 support=0.7 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45876948.0 spike=0.54
- MOIL.CA: score=17.07 buy_ready=False sector_rank=5 price=0.7 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=586054.5 spike=2.54
- MOIN.CA: score=17.72 buy_ready=False sector_rank=13 price=35.39 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.19 liquidity=10350716.0 spike=0.34
- MOSC.CA: score=6.67 buy_ready=False sector_rank=13 price=299.2 support=302.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.11 liquidity=1941555.5 spike=0.27
- MPCI.CA: score=12.72 buy_ready=False sector_rank=13 price=384.63 support=393.25 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=20.66 liquidity=138004240.0 spike=0.89
- MPCO.CA: score=24.5 buy_ready=False sector_rank=4 price=2.85 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.85 liquidity=255710432.0 spike=1.55
- MPRC.CA: score=9.72 buy_ready=False sector_rank=13 price=38.11 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=21224796.0 spike=0.54
- MTIE.CA: score=17.4 buy_ready=False sector_rank=7 price=8.23 support=8.1 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=24613032.0 spike=0.69
- NAHO.CA: score=-0.09 buy_ready=False sector_rank=13 price=0.14 support=0.13 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=187824.81 spike=3.84
- NCCW.CA: score=19.72 buy_ready=False sector_rank=13 price=7.55 support=5.77 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.81 liquidity=44970100.0 spike=0.7
- NEDA.CA: score=7.45 buy_ready=False sector_rank=13 price=2.77 support=2.7 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=649348.56 spike=1.04
- NHPS.CA: score=7.7 buy_ready=False sector_rank=13 price=73.69 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=11.11 liquidity=7980819.5 spike=0.44
- NINH.CA: score=14.72 buy_ready=False sector_rank=13 price=20.59 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.54 liquidity=17903476.0 spike=0.57
- NIPH.CA: score=8.32 buy_ready=False sector_rank=21 price=307.06 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.78 liquidity=145158368.0 spike=0.83
- OBRI.CA: score=11.36 buy_ready=False sector_rank=13 price=30.14 support=30.1 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=7637651.0 spike=0.48
- OCDI.CA: score=15.49 buy_ready=False sector_rank=16 price=29.4 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=117442736.0 spike=1.47
- OCPH.CA: score=12.92 buy_ready=False sector_rank=13 price=235.83 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=37.08 liquidity=7200286.0 spike=0.93
- ODIN.CA: score=14.72 buy_ready=False sector_rank=13 price=2.74 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=11936011.0 spike=0.52
- OFH.CA: score=17.72 buy_ready=False sector_rank=13 price=1.04 support=0.93 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=55050196.0 spike=0.44
- OIH.CA: score=24.4 buy_ready=False sector_rank=1 price=2.14 support=1.88 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=74.19 liquidity=66204584.0 spike=0.55
- OLFI.CA: score=17.68 buy_ready=False sector_rank=14 price=22.58 support=22.07 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.42 liquidity=40991924.0 spike=2.54
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=835.73 support=830.0 resistance=865.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=159603264.0 spike=1.0
- ORHD.CA: score=17.55 buy_ready=False sector_rank=16 price=41.8 support=40.85 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.58 liquidity=105779016.0 spike=0.77
- ORWE.CA: score=20.1 buy_ready=False sector_rank=12 price=27.4 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=64.19 liquidity=45101856.0 spike=0.8
- PHAR.CA: score=8.32 buy_ready=False sector_rank=21 price=114.01 support=117.0 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.18 liquidity=74017456.0 spike=0.58
- PHDC.CA: score=9.55 buy_ready=False sector_rank=16 price=13.2 support=13.16 resistance=15.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.9 liquidity=135875472.0 spike=0.81
- PHTV.CA: score=8.25 buy_ready=False sector_rank=13 price=346.85 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=525997.94 spike=0.3
- POUL.CA: score=17.5 buy_ready=False sector_rank=14 price=38.55 support=37.03 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.03 liquidity=58845364.0 spike=2.45
- PRCL.CA: score=14.24 buy_ready=False sector_rank=18 price=31.78 support=30.9 resistance=35.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=16021499.0 spike=0.84
- PRDC.CA: score=9.55 buy_ready=False sector_rank=16 price=7.74 support=7.68 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.7 liquidity=31801888.0 spike=0.5
- PRMH.CA: score=9.74 buy_ready=False sector_rank=13 price=2.6 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.09 liquidity=5013611.5 spike=0.47
- RACC.CA: score=10.7 buy_ready=False sector_rank=13 price=9.64 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.47 liquidity=5971340.0 spike=0.33
- RAKT.CA: score=7.13 buy_ready=False sector_rank=13 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=49.32 liquidity=342372.48 spike=1.53
- RAYA.CA: score=14.42 buy_ready=False sector_rank=17 price=7.0 support=7.0 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=33172500.0 spike=0.61
- RMDA.CA: score=16.32 buy_ready=False sector_rank=21 price=6.0 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.31 liquidity=26492682.0 spike=0.44
- ROTO.CA: score=4.94 buy_ready=False sector_rank=13 price=40.0 support=35.02 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=29.03 liquidity=5211467.0 spike=0.56
- RREI.CA: score=14.72 buy_ready=False sector_rank=13 price=4.24 support=4.24 resistance=4.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=14220905.0 spike=0.7
- RTVC.CA: score=2.06 buy_ready=False sector_rank=13 price=3.85 support=3.85 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.87 liquidity=2331719.0 spike=0.49
- RUBX.CA: score=9.72 buy_ready=False sector_rank=13 price=14.99 support=14.5 resistance=17.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=308824832.0 spike=12.7
- SAUD.CA: score=26.25 buy_ready=False sector_rank=9 price=25.36 support=22.7 resistance=24.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.59 liquidity=172021024.0 spike=16.89
- SCEM.CA: score=4.24 buy_ready=False sector_rank=18 price=89.0 support=87.02 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66764904.0 spike=0.57
- SCFM.CA: score=7.42 buy_ready=False sector_rank=13 price=267.18 support=265.51 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.81 liquidity=2691942.0 spike=0.35
- SCTS.CA: score=9.12 buy_ready=False sector_rank=3 price=575.7 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.33 liquidity=1719204.0 spike=0.59
- SDTI.CA: score=18.72 buy_ready=False sector_rank=13 price=77.58 support=67.0 resistance=78.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.94 liquidity=19788654.0 spike=0.78
- SEIG.CA: score=0.88 buy_ready=False sector_rank=13 price=229.32 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.93 liquidity=1152680.5 spike=0.67
- SIPC.CA: score=4.72 buy_ready=False sector_rank=13 price=5.42 support=5.3 resistance=5.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26377998.0 spike=0.37
- SKPC.CA: score=19.4 buy_ready=False sector_rank=6 price=18.1 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=86405832.0 spike=0.66
- SMFR.CA: score=3.86 buy_ready=False sector_rank=13 price=231.6 support=236.0 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=4140411.5 spike=0.49
- SNFC.CA: score=19.32 buy_ready=False sector_rank=13 price=11.33 support=10.26 resistance=11.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.5 liquidity=19799788.0 spike=1.3
- SPIN.CA: score=8.67 buy_ready=False sector_rank=12 price=16.97 support=17.01 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=24.71 liquidity=8571086.0 spike=0.54
- SPMD.CA: score=16.72 buy_ready=False sector_rank=13 price=0.42 support=0.43 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.64 liquidity=27608224.0 spike=0.38
- SUGR.CA: score=17.6 buy_ready=False sector_rank=14 price=57.44 support=52.98 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.07 liquidity=12884201.0 spike=0.2
- SVCE.CA: score=4.72 buy_ready=False sector_rank=13 price=11.3 support=9.6 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=157752128.0 spike=0.81
- SWDY.CA: score=18.1 buy_ready=False sector_rank=11 price=125.43 support=120.22 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=39524888.0 spike=0.56
- TALM.CA: score=22.96 buy_ready=False sector_rank=3 price=21.03 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=68.13 liquidity=81608728.0 spike=1.28
- TMGH.CA: score=14.87 buy_ready=False sector_rank=16 price=93.6 support=93.2 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.39 liquidity=326362752.0 spike=1.16
- TRTO.CA: score=8.3 buy_ready=False sector_rank=13 price=0.06 support=0.05 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=35639.23 spike=1.27
- UEFM.CA: score=5.49 buy_ready=False sector_rank=13 price=488.87 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=36.47 liquidity=1764502.63 spike=0.58
- UEGC.CA: score=18.54 buy_ready=False sector_rank=13 price=1.78 support=1.66 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=92644064.0 spike=1.91
- UNIP.CA: score=14.72 buy_ready=False sector_rank=13 price=0.37 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=14582994.0 spike=0.55
- UNIT.CA: score=14.55 buy_ready=False sector_rank=16 price=18.24 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.52 liquidity=10044039.0 spike=0.68
- WCDF.CA: score=13.43 buy_ready=False sector_rank=13 price=709.59 support=636.31 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=77.57 liquidity=6190512.5 spike=1.26
- WKOL.CA: score=17.72 buy_ready=False sector_rank=13 price=334.18 support=335.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.52 liquidity=13776254.0 spike=0.91
- ZEOT.CA: score=12.77 buy_ready=False sector_rank=13 price=13.15 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=5049698.0 spike=0.75
- ZMID.CA: score=17.55 buy_ready=False sector_rank=16 price=8.4 support=7.9 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=185245824.0 spike=0.84

## Backtesting Lite
- GBCO.CA: 180d return=23.12%, max drawdown=-24.35%, MA20>MA50 days last20=0, as_of=2026-09-19T21:00:00+00:00
- SAUD.CA: 180d return=69.44%, max drawdown=-19.12%, MA20>MA50 days last20=20, as_of=2026-09-19T21:00:00+00:00
- CANA.CA: 180d return=25.92%, max drawdown=-36.46%, MA20>MA50 days last20=20, as_of=2026-09-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=628 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=628 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- CICH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=CI Capital Holding summary=Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=628 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
