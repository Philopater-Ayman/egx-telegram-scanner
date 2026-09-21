# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-21T11:07:51.356754+00:00
Generated Cairo: 2026-09-21 14:07
Run timing: target 08:45 Cairo | generated Cairo 2026-09-21 14:07 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-21 14:05

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 170/187
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, September 21
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 26.32% / above MA50 57.89%
- EGX70 regime: BEARISH / above MA20 28.21% / above MA50 48.72%
- Sector breadth: 47.62%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=637185920.0 spike=1.09 score=16.14
- CCAP.CA: liquidity=628514688.0 spike=0.72 score=23.4
- RUBX.CA: liquidity=295599488.0 spike=12.16 score=9.62
- ETEL.CA: liquidity=289251584.0 spike=1.21 score=19.82
- MFPC.CA: liquidity=285713696.0 spike=1.9 score=22.2

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner flags several stocks with high rank scores and bullish‑watch outlooks, but the EGX30 and EGX70 remain bearish with weak breadth, keeping risk mode defensive and no new buys allowed.
- Top tickets show strong liquidity (tradeable or accumulation spike) and bullish‑watch scores, yet risk notes flag extended momentum, overheated RSI or prices far above recent support.
- Sector leadership is concentrated in Investment Holding, Education and Telecommunications, but overall sector breadth is only ~48%, limiting broad‑based upside.
- EGX30 and EGX70 trends are bearish with low MA20 breadth, so the market regime shifts risk mode to DEFENSIVE_NO_NEW_BUY, restricting new long entries.
- Given the watch‑only outlook and mixed technical signals, near‑term price action over the next 1‑3 days remains uncertain and could reverse if breadth deteriorates further.

## Top Liquidity Spikes
- MIPH.CA: spike=18.36 liquidity=77288944.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SAUD.CA: spike=15.96 liquidity=162540000.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=12.16 liquidity=295599488.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ENGC.CA: spike=3.69 liquidity=52561740.0 outlook=NEUTRAL score=49.56 buy_ready=False
- NAHO.CA: spike=2.53 liquidity=123459.38 outlook=WEAK_OR_RISKY score=10.56 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=18.05 5d=14.92% 20d=25.0% aboveMA50=100.0%
- #2 Education: score=9.25 5d=5.08% 20d=8.61% aboveMA50=66.67%
- #3 Telecommunications: score=9.2 5d=1.54% 20d=7.28% aboveMA50=100.0%
- #4 Agriculture & Food Production: score=8.22 5d=3.31% 20d=12.34% aboveMA50=50.0%
- #5 Energy & Petrochemicals: score=8.15 5d=3.7% 20d=2.79% aboveMA50=100.0%
- #6 Basic Resources & Chemicals: score=6.64 5d=1.6% 20d=6.03% aboveMA50=70.0%
- #7 Automotive & Distribution: score=5.63 5d=1.09% 20d=3.36% aboveMA50=50.0%
- #8 Banking & Financials: score=4.9 5d=0.7% 20d=0.78% aboveMA50=70.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CICH.CA: BULLISH_WATCH score=90.96 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EGCH.CA: BULLISH_WATCH score=87.64 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EXPA.CA: BULLISH_WATCH score=86.9 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ATQA.CA: BULLISH_WATCH score=83.64 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- EGAL.CA: BULLISH_WATCH score=82.64 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- FERC.CA: BULLISH_WATCH score=82.64 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- TALM.CA: BULLISH_WATCH score=82.25 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- ALCN.CA: BULLISH_WATCH score=79.91 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- CPCI.CA: BULLISH_WATCH score=79.56 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- GBCO.CA: BULLISH_WATCH score=74.63 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=5.06 buy_ready=False sector_rank=13 price=291.0 support=288.01 resistance=308.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31981238.0 spike=1.22
- ABUK.CA: score=19.4 buy_ready=False sector_rank=6 price=93.91 support=75.01 resistance=96.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=67.11 liquidity=109889480.0 spike=0.62
- ACAMD.CA: score=16.62 buy_ready=False sector_rank=13 price=2.03 support=1.95 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=22853226.0 spike=0.39
- ACGC.CA: score=14.64 buy_ready=False sector_rank=12 price=14.08 support=13.4 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=6909248.5 spike=0.2
- ADCI.CA: score=3.48 buy_ready=False sector_rank=13 price=277.01 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=33.17 liquidity=3858136.75 spike=0.72
- ADIB.CA: score=18.96 buy_ready=False sector_rank=8 price=52.3 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=40.76 liquidity=51477916.0 spike=0.67
- ADPC.CA: score=15.82 buy_ready=False sector_rank=13 price=3.9 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=56.14 liquidity=27985212.0 spike=1.6
- AFDI.CA: score=12.92 buy_ready=False sector_rank=13 price=52.35 support=51.6 resistance=68.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=44.05 liquidity=8297756.0 spike=0.33
- AFMC.CA: score=14.62 buy_ready=False sector_rank=13 price=159.25 support=153.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=43.65 liquidity=17937342.0 spike=0.29
- AJWA.CA: score=12.42 buy_ready=False sector_rank=13 price=179.02 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=49.42 liquidity=7792521.0 spike=0.17
- ALCN.CA: score=22.56 buy_ready=False sector_rank=9 price=32.7 support=30.03 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=60.05 liquidity=33288016.0 spike=0.97
- ALUM.CA: score=9.73 buy_ready=False sector_rank=13 price=25.99 support=25.0 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=37.34 liquidity=5107486.5 spike=0.37
- AMER.CA: score=14.32 buy_ready=False sector_rank=17 price=5.15 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=20716420.0 spike=0.36
- AMES.CA: score=4.62 buy_ready=False sector_rank=13 price=53.45 support=48.45 resistance=54.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=222617488.0 spike=0.86
- AMIA.CA: score=16.82 buy_ready=False sector_rank=13 price=18.4 support=17.12 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=9199538.0 spike=0.17
- AMOC.CA: score=19.4 buy_ready=False sector_rank=5 price=13.61 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=70.26 liquidity=117000016.0 spike=0.66
- APSW.CA: score=5.04 buy_ready=False sector_rank=13 price=8.31 support=8.37 resistance=8.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=1100066.88 spike=1.16
- ARAB.CA: score=14.32 buy_ready=False sector_rank=17 price=0.24 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=41728952.0 spike=0.38
- ARCC.CA: score=17.08 buy_ready=False sector_rank=18 price=71.01 support=71.5 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=41.79 liquidity=18487056.0 spike=0.45
- AREH.CA: score=14.62 buy_ready=False sector_rank=13 price=1.42 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=10200817.0 spike=0.7
- ASCM.CA: score=13.9 buy_ready=False sector_rank=13 price=59.24 support=60.15 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=37.27 liquidity=9272052.0 spike=0.46
- ASPI.CA: score=4.62 buy_ready=False sector_rank=13 price=0.43 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57640080.0 spike=0.94
- ATLC.CA: score=17.82 buy_ready=False sector_rank=10 price=7.0 support=5.22 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=67.73 liquidity=9638841.0 spike=0.35
- ATQA.CA: score=23.74 buy_ready=False sector_rank=6 price=13.4 support=10.87 resistance=13.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=67.21 liquidity=218353376.0 spike=2.17
- AXPH.CA: score=12.75 buy_ready=False sector_rank=13 price=1661.87 support=1481.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=5122307.5 spike=0.49
- BINV.CA: score=24.4 buy_ready=False sector_rank=1 price=57.81 support=47.56 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=71.96 liquidity=17247346.0 spike=0.96
- BIOC.CA: score=9.62 buy_ready=False sector_rank=13 price=264.02 support=272.01 resistance=506.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=24.39 liquidity=39690088.0 spike=0.37
- BTFH.CA: score=16.42 buy_ready=False sector_rank=10 price=2.98 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=90190248.0 spike=1.12
- CAED.CA: score=12.57 buy_ready=False sector_rank=13 price=125.12 support=123.56 resistance=173.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=7944044.5 spike=0.32
- CANA.CA: score=25.76 buy_ready=False sector_rank=8 price=47.31 support=41.11 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=74.0 liquidity=51557520.0 spike=2.4
- CCAP.CA: score=23.4 buy_ready=False sector_rank=1 price=7.13 support=5.71 resistance=7.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=79.6 liquidity=628514688.0 spike=0.72
- CCRS.CA: score=17.62 buy_ready=False sector_rank=13 price=2.62 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=18767764.0 spike=0.34
- CEFM.CA: score=12.17 buy_ready=False sector_rank=13 price=143.39 support=143.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=58.63 liquidity=4542350.5 spike=0.43
- CERA.CA: score=4.62 buy_ready=False sector_rank=13 price=1.37 support=1.36 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83965224.0 spike=0.7
- CFGH.CA: score=7.63 buy_ready=False sector_rank=13 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8911.97 spike=0.45
- CICH.CA: score=25.1 buy_ready=False sector_rank=10 price=13.02 support=12.0 resistance=13.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=69.57 liquidity=14357624.0 spike=2.46
- CIEB.CA: score=18.96 buy_ready=False sector_rank=8 price=24.99 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=50.47 liquidity=11768505.0 spike=0.88
- CIRA.CA: score=20.4 buy_ready=False sector_rank=2 price=38.99 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=77.16 liquidity=38399532.0 spike=1.0
- CLHO.CA: score=8.28 buy_ready=False sector_rank=21 price=15.68 support=15.81 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=31.64 liquidity=51861424.0 spike=0.72
- CNFN.CA: score=11.54 buy_ready=False sector_rank=10 price=4.56 support=4.46 resistance=4.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=7355448.5 spike=0.58
- COMI.CA: score=16.14 buy_ready=False sector_rank=8 price=132.99 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=43.21 liquidity=637185920.0 spike=1.09
- COPR.CA: score=17.62 buy_ready=False sector_rank=13 price=0.49 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=47.74 liquidity=38786468.0 spike=0.71
- COSG.CA: score=17.62 buy_ready=False sector_rank=13 price=1.81 support=1.79 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=27860124.0 spike=0.76
- CPCI.CA: score=15.12 buy_ready=False sector_rank=13 price=557.42 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=59.49 liquidity=3496087.5 spike=0.91
- CSAG.CA: score=9.77 buy_ready=False sector_rank=9 price=37.65 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=39.7 liquidity=4209329.5 spike=0.27
- DAPH.CA: score=4.62 buy_ready=False sector_rank=13 price=112.74 support=110.0 resistance=121.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25851026.0 spike=0.43
- DEIN.CA: score=7.62 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=5.35 buy_ready=False sector_rank=15 price=25.59 support=26.0 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=26.6 liquidity=6402461.0 spike=1.23
- DSCW.CA: score=13.62 buy_ready=False sector_rank=13 price=1.79 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=26759280.0 spike=0.78
- DTPP.CA: score=21.62 buy_ready=False sector_rank=13 price=326.4 support=294.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=60.85 liquidity=54180192.0 spike=0.74
- EALR.CA: score=12.42 buy_ready=False sector_rank=13 price=365.95 support=340.0 resistance=412.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=7792552.0 spike=0.5
- EASB.CA: score=15.1 buy_ready=False sector_rank=13 price=7.8 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=55.21 liquidity=5472780.0 spike=0.33
- EAST.CA: score=8.64 buy_ready=False sector_rank=15 price=31.96 support=32.0 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=78706440.0 spike=1.08
- EBSC.CA: score=10.39 buy_ready=False sector_rank=13 price=2.0 support=1.9 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=2762680.0 spike=0.19
- ECAP.CA: score=9.34 buy_ready=False sector_rank=13 price=31.68 support=31.16 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=49.91 liquidity=4716293.5 spike=0.43
- EDFM.CA: score=9.14 buy_ready=False sector_rank=13 price=399.27 support=399.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=1516727.63 spike=0.84
- EEII.CA: score=13.41 buy_ready=False sector_rank=13 price=2.24 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=38.41 liquidity=9788926.0 spike=0.55
- EFIC.CA: score=15.4 buy_ready=False sector_rank=6 price=185.8 support=192.75 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=46.16 liquidity=43333464.0 spike=0.12
- EFID.CA: score=17.48 buy_ready=False sector_rank=15 price=30.62 support=29.71 resistance=33.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=51.56 liquidity=38835008.0 spike=0.62
- EFIH.CA: score=13.69 buy_ready=False sector_rank=20 price=23.24 support=22.16 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=48.66 liquidity=40669212.0 spike=0.68
- EGAL.CA: score=21.4 buy_ready=False sector_rank=6 price=367.59 support=335.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=27728092.0 spike=0.27
- EGAS.CA: score=17.96 buy_ready=False sector_rank=5 price=57.0 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=50.19 liquidity=8557588.0 spike=0.74
- EGBE.CA: score=4.01 buy_ready=False sector_rank=8 price=0.51 support=0.49 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=31.71 liquidity=50648.77 spike=0.59
- EGCH.CA: score=21.5 buy_ready=False sector_rank=6 price=13.99 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=59.48 liquidity=125697080.0 spike=1.05
- EGSA.CA: score=9.4 buy_ready=False sector_rank=3 price=9.0 support=8.67 resistance=9.1 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=78.18 liquidity=1800.0 spike=0.29
- EGTS.CA: score=16.32 buy_ready=False sector_rank=17 price=16.96 support=16.51 resistance=17.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=46.58 liquidity=19925120.0 spike=0.83
- EHDR.CA: score=14.62 buy_ready=False sector_rank=13 price=2.68 support=2.73 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=14320900.0 spike=0.78
- ELEC.CA: score=14.07 buy_ready=False sector_rank=11 price=1.97 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=57444764.0 spike=0.75
- ELKA.CA: score=14.62 buy_ready=False sector_rank=13 price=1.68 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=15336102.0 spike=0.39
- ELNA.CA: score=-0.91 buy_ready=False sector_rank=13 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=24.57 liquidity=383017.51 spike=1.04
- ELSH.CA: score=14.62 buy_ready=False sector_rank=13 price=12.71 support=12.67 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=40.83 liquidity=30008170.0 spike=0.8
- ELWA.CA: score=0.18 buy_ready=False sector_rank=13 price=1.69 support=1.66 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=23.91 liquidity=551821.44 spike=0.22
- EMFD.CA: score=15.32 buy_ready=False sector_rank=17 price=13.46 support=11.87 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=65.92 liquidity=23155458.0 spike=0.13
- ENGC.CA: score=19.62 buy_ready=False sector_rank=13 price=42.56 support=41.0 resistance=48.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=52.93 liquidity=52561740.0 spike=3.69
- EOSB.CA: score=9.63 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=8211.1 spike=0.11
- EPCO.CA: score=11.12 buy_ready=False sector_rank=13 price=10.95 support=10.8 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=50.51 liquidity=6491198.5 spike=0.4
- EPPK.CA: score=-4.96 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=19.82 buy_ready=False sector_rank=3 price=134.7 support=112.5 resistance=135.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=80.54 liquidity=289251584.0 spike=1.21
- ETRS.CA: score=14.62 buy_ready=False sector_rank=13 price=10.82 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=51.4 liquidity=10314826.0 spike=0.74
- EXPA.CA: score=23.02 buy_ready=False sector_rank=8 price=21.83 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=55.62 liquidity=71732992.0 spike=2.03
- FAIT.CA: score=10.46 buy_ready=False sector_rank=8 price=46.92 support=41.52 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=72.55 liquidity=1500641.88 spike=0.18
- FAITA.CA: score=5.98 buy_ready=False sector_rank=8 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16085.12 spike=0.31
- FERC.CA: score=16.33 buy_ready=False sector_rank=6 price=79.4 support=77.04 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=57.65 liquidity=4927306.5 spike=0.33
- FWRY.CA: score=13.69 buy_ready=False sector_rank=20 price=18.95 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=31352604.0 spike=0.23
- GBCO.CA: score=26.03 buy_ready=False sector_rank=7 price=30.99 support=27.51 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=63.43 liquidity=91949640.0 spike=1.39
- GDWA.CA: score=13.62 buy_ready=False sector_rank=13 price=0.76 support=0.76 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=32399892.0 spike=0.75
- GGCC.CA: score=14.62 buy_ready=False sector_rank=13 price=0.85 support=0.83 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=48.29 liquidity=15953058.0 spike=0.49
- GIHD.CA: score=19.62 buy_ready=False sector_rank=13 price=71.05 support=61.61 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=19316114.0 spike=0.69
- GMCI.CA: score=-1.01 buy_ready=False sector_rank=13 price=1.76 support=1.69 resistance=1.94 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=32.26 liquidity=370314.56 spike=0.77
- GRCA.CA: score=8.62 buy_ready=False sector_rank=13 price=40.01 support=39.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=14.01 liquidity=11841483.0 spike=0.16
- GSSC.CA: score=15.59 buy_ready=False sector_rank=13 price=310.88 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=63.21 liquidity=3963386.0 spike=0.42
- GTWL.CA: score=17.62 buy_ready=False sector_rank=13 price=225.93 support=184.01 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=99527136.0 spike=0.49
- HDBK.CA: score=22.96 buy_ready=False sector_rank=8 price=118.85 support=89.77 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=63.27 liquidity=16159211.0 spike=0.26
- HELI.CA: score=19.32 buy_ready=False sector_rank=17 price=8.03 support=7.34 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=66.86 liquidity=121098760.0 spike=0.72
- HRHO.CA: score=14.18 buy_ready=False sector_rank=10 price=24.9 support=25.04 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=50112816.0 spike=0.51
- ICID.CA: score=16.46 buy_ready=False sector_rank=13 price=17.17 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=58.44 liquidity=8834364.0 spike=0.65
- IDRE.CA: score=6.24 buy_ready=False sector_rank=13 price=55.0 support=54.25 resistance=59.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27804322.0 spike=1.81
- IFAP.CA: score=16.4 buy_ready=False sector_rank=4 price=20.21 support=20.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=50.43 liquidity=13320248.0 spike=0.59
- INFI.CA: score=8.25 buy_ready=False sector_rank=13 price=128.0 support=130.15 resistance=174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=22.03 liquidity=8628280.0 spike=0.29
- IRON.CA: score=5.71 buy_ready=False sector_rank=6 price=27.48 support=26.3 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=5308012.5 spike=0.37
- ISMA.CA: score=5.55 buy_ready=False sector_rank=13 price=29.23 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=31.81 liquidity=5930372.5 spike=0.25
- ISMQ.CA: score=16.4 buy_ready=False sector_rank=6 price=8.84 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=48.67 liquidity=19036616.0 spike=0.7
- ISPH.CA: score=8.28 buy_ready=False sector_rank=21 price=12.02 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=33.88 liquidity=45710412.0 spike=0.66
- JUFO.CA: score=13.5 buy_ready=False sector_rank=15 price=26.89 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=20757142.0 spike=1.01
- KABO.CA: score=17.73 buy_ready=False sector_rank=12 price=9.16 support=8.9 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=48.03 liquidity=19824188.0 spike=0.43
- KWIN.CA: score=9.6 buy_ready=False sector_rank=13 price=86.07 support=85.01 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=19.73 liquidity=9973380.0 spike=0.18
- KZPC.CA: score=11.76 buy_ready=False sector_rank=13 price=13.98 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=69.25 liquidity=4133501.0 spike=0.1
- LCSW.CA: score=14.08 buy_ready=False sector_rank=18 price=31.76 support=32.42 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=11844320.0 spike=0.47
- LUTS.CA: score=4.62 buy_ready=False sector_rank=13 price=0.89 support=0.88 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=61218516.0 spike=0.26
- MAAL.CA: score=16.76 buy_ready=False sector_rank=13 price=8.79 support=8.18 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=40.25 liquidity=21879698.0 spike=2.07
- MASR.CA: score=14.62 buy_ready=False sector_rank=13 price=7.55 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=51.71 liquidity=73091920.0 spike=0.76
- MBSC.CA: score=17.08 buy_ready=False sector_rank=18 price=349.46 support=360.0 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=40.09 liquidity=30011450.0 spike=0.62
- MCQE.CA: score=14.08 buy_ready=False sector_rank=18 price=209.89 support=213.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=15932909.0 spike=0.52
- MCRO.CA: score=19.62 buy_ready=False sector_rank=13 price=1.62 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=72.09 liquidity=46958100.0 spike=0.37
- MENA.CA: score=4.86 buy_ready=False sector_rank=17 price=6.63 support=6.58 resistance=7.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=539286.44 spike=0.28
- MEPA.CA: score=4.62 buy_ready=False sector_rank=13 price=1.89 support=1.84 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18891202.0 spike=0.48
- MFPC.CA: score=22.2 buy_ready=False sector_rank=6 price=49.88 support=39.02 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=81.12 liquidity=285713696.0 spike=1.9
- MFSC.CA: score=9.2 buy_ready=False sector_rank=13 price=49.46 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=55.79 liquidity=1573454.75 spike=0.31
- MHOT.CA: score=6.22 buy_ready=False sector_rank=19 price=17.43 support=17.62 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=37.21 liquidity=3346827.25 spike=0.32
- MICH.CA: score=17.62 buy_ready=False sector_rank=13 price=47.8 support=48.12 resistance=53.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=42.87 liquidity=11994244.0 spike=0.73
- MILS.CA: score=16.96 buy_ready=False sector_rank=13 price=192.74 support=198.0 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=43.67 liquidity=9336181.0 spike=0.32
- MIPH.CA: score=8.28 buy_ready=False sector_rank=21 price=923.2 support=850.03 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=77288944.0 spike=18.36
- MOED.CA: score=4.62 buy_ready=False sector_rank=13 price=0.74 support=0.7 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42586024.0 spike=0.42
- MOIL.CA: score=16.04 buy_ready=False sector_rank=5 price=0.7 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=58.57 liquidity=480268.22 spike=2.08
- MOIN.CA: score=15.94 buy_ready=False sector_rank=13 price=35.59 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=56.19 liquidity=8312099.5 spike=0.27
- MOSC.CA: score=6.49 buy_ready=False sector_rank=13 price=297.85 support=302.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=46.11 liquidity=1866758.75 spike=0.26
- MPCI.CA: score=12.62 buy_ready=False sector_rank=13 price=384.17 support=393.25 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=20.66 liquidity=130621288.0 spike=0.84
- MPCO.CA: score=24.02 buy_ready=False sector_rank=4 price=2.8 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=74.85 liquidity=215909408.0 spike=1.31
- MPRC.CA: score=9.62 buy_ready=False sector_rank=13 price=38.04 support=38.31 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=20065028.0 spike=0.51
- MTIE.CA: score=17.25 buy_ready=False sector_rank=7 price=8.19 support=8.1 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=53.03 liquidity=22868844.0 spike=0.64
- NAHO.CA: score=5.81 buy_ready=False sector_rank=13 price=0.13 support=0.13 resistance=0.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=123459.38 spike=2.53
- NCCW.CA: score=19.62 buy_ready=False sector_rank=13 price=7.42 support=5.77 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=68.81 liquidity=39157424.0 spike=0.61
- NEDA.CA: score=4.94 buy_ready=False sector_rank=13 price=2.72 support=2.7 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=313479.09 spike=0.5
- NHPS.CA: score=5.34 buy_ready=False sector_rank=13 price=74.0 support=75.31 resistance=98.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=11.11 liquidity=5711971.5 spike=0.32
- NINH.CA: score=14.62 buy_ready=False sector_rank=13 price=20.52 support=20.5 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=36.54 liquidity=15936590.0 spike=0.51
- NIPH.CA: score=8.28 buy_ready=False sector_rank=21 price=304.19 support=301.0 resistance=414.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=22.78 liquidity=138776496.0 spike=0.8
- OBRI.CA: score=10.07 buy_ready=False sector_rank=13 price=30.33 support=30.1 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=6443775.5 spike=0.41
- OCDI.CA: score=15.22 buy_ready=False sector_rank=17 price=29.41 support=29.25 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=115671728.0 spike=1.45
- OCPH.CA: score=12.53 buy_ready=False sector_rank=13 price=236.9 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=37.08 liquidity=6910320.0 spike=0.89
- ODIN.CA: score=14.62 buy_ready=False sector_rank=13 price=2.75 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=11053858.0 spike=0.48
- OFH.CA: score=17.62 buy_ready=False sector_rank=13 price=1.04 support=0.92 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=46270568.0 spike=0.37
- OIH.CA: score=24.4 buy_ready=False sector_rank=1 price=2.14 support=1.88 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=74.19 liquidity=58660172.0 spike=0.49
- OLFI.CA: score=16.74 buy_ready=False sector_rank=15 price=22.28 support=22.07 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=40.04 liquidity=33671932.0 spike=2.13
- ORAS.CA: score=4.6 buy_ready=False sector_rank=14 price=834.52 support=833.0 resistance=865.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=115330000.0 spike=1.0
- ORHD.CA: score=17.32 buy_ready=False sector_rank=17 price=42.01 support=40.85 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=56.58 liquidity=80699872.0 spike=0.59
- ORWE.CA: score=17.73 buy_ready=False sector_rank=12 price=27.0 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=64.19 liquidity=40898192.0 spike=0.72
- PHAR.CA: score=8.28 buy_ready=False sector_rank=21 price=114.16 support=117.0 resistance=141.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=27.18 liquidity=66724108.0 spike=0.52
- PHDC.CA: score=9.32 buy_ready=False sector_rank=17 price=13.03 support=13.16 resistance=15.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=21.9 liquidity=99985912.0 spike=0.59
- PHTV.CA: score=8.15 buy_ready=False sector_rank=13 price=346.78 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=522468.03 spike=0.29
- POUL.CA: score=20.02 buy_ready=False sector_rank=15 price=38.74 support=37.03 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=45.03 liquidity=54611600.0 spike=2.27
- PRCL.CA: score=14.08 buy_ready=False sector_rank=18 price=30.65 support=30.9 resistance=35.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=11322299.0 spike=0.59
- PRDC.CA: score=9.32 buy_ready=False sector_rank=17 price=7.71 support=7.68 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=22.91 liquidity=23221698.0 spike=0.36
- PRMH.CA: score=9.13 buy_ready=False sector_rank=13 price=2.58 support=2.28 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=53.09 liquidity=4510880.0 spike=0.42
- RACC.CA: score=10.28 buy_ready=False sector_rank=13 price=9.67 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=59.07 liquidity=5656146.5 spike=0.3
- RAKT.CA: score=7.03 buy_ready=False sector_rank=13 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-19T21:00:00+00:00 freshness=FRESH RSI=49.32 liquidity=342372.48 spike=1.53
- RAYA.CA: score=14.38 buy_ready=False sector_rank=16 price=7.0 support=7.0 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=29529240.0 spike=0.54
- RMDA.CA: score=16.28 buy_ready=False sector_rank=21 price=5.98 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=18100786.0 spike=0.3
- ROTO.CA: score=3.98 buy_ready=False sector_rank=13 price=39.75 support=35.02 resistance=47.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=29.03 liquidity=4359343.5 spike=0.47
- RREI.CA: score=14.62 buy_ready=False sector_rank=13 price=4.23 support=4.24 resistance=4.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=12461206.0 spike=0.61
- RTVC.CA: score=1.09 buy_ready=False sector_rank=13 price=3.82 support=3.85 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=26.87 liquidity=1470206.88 spike=0.31
- RUBX.CA: score=9.62 buy_ready=False sector_rank=13 price=14.92 support=14.5 resistance=17.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=295599488.0 spike=12.16
- SAUD.CA: score=10.96 buy_ready=False sector_rank=8 price=25.98 support=24.43 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=162540000.0 spike=15.96
- SCEM.CA: score=4.08 buy_ready=False sector_rank=18 price=88.49 support=87.02 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52749156.0 spike=0.45
- SCFM.CA: score=7.09 buy_ready=False sector_rank=13 price=265.74 support=265.51 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=39.81 liquidity=2469551.75 spike=0.32
- SCTS.CA: score=9.62 buy_ready=False sector_rank=2 price=591.55 support=566.66 resistance=640.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=37.33 liquidity=1215416.75 spike=0.41
- SDTI.CA: score=18.62 buy_ready=False sector_rank=13 price=77.22 support=67.0 resistance=78.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=75.94 liquidity=17826994.0 spike=0.71
- SEIG.CA: score=0.31 buy_ready=False sector_rank=13 price=231.6 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=34.93 liquidity=685440.5 spike=0.4
- SIPC.CA: score=4.62 buy_ready=False sector_rank=13 price=5.46 support=5.3 resistance=5.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22807748.0 spike=0.32
- SKPC.CA: score=19.4 buy_ready=False sector_rank=6 price=18.14 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=73811080.0 spike=0.57
- SMFR.CA: score=3.47 buy_ready=False sector_rank=13 price=231.51 support=236.0 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=30.98 liquidity=3843530.0 spike=0.45
- SNFC.CA: score=18.78 buy_ready=False sector_rank=13 price=11.3 support=10.26 resistance=11.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=79.5 liquidity=16501158.0 spike=1.08
- SPIN.CA: score=6.27 buy_ready=False sector_rank=12 price=16.8 support=17.01 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=24.71 liquidity=6535832.5 spike=0.41
- SPMD.CA: score=16.62 buy_ready=False sector_rank=13 price=0.42 support=0.43 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=48.05 liquidity=25245964.0 spike=0.38
- SUGR.CA: score=17.48 buy_ready=False sector_rank=15 price=57.52 support=52.98 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=57.07 liquidity=11289364.0 spike=0.17
- SVCE.CA: score=4.62 buy_ready=False sector_rank=13 price=11.32 support=9.6 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=146426560.0 spike=0.75
- SWDY.CA: score=18.07 buy_ready=False sector_rank=11 price=125.03 support=120.22 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=36594480.0 spike=0.52
- TALM.CA: score=23.84 buy_ready=False sector_rank=2 price=21.12 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=69.27 liquidity=74423064.0 spike=1.22
- TMGH.CA: score=14.32 buy_ready=False sector_rank=17 price=93.34 support=93.2 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=41.39 liquidity=230577904.0 spike=0.82
- TRTO.CA: score=8.06 buy_ready=False sector_rank=13 price=0.06 support=0.05 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=33642.75 spike=1.2
- UEFM.CA: score=5.25 buy_ready=False sector_rank=13 price=490.54 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=36.47 liquidity=1630536.75 spike=0.54
- UEGC.CA: score=18.14 buy_ready=False sector_rank=13 price=1.77 support=1.66 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=85286264.0 spike=1.76
- UNIP.CA: score=14.62 buy_ready=False sector_rank=13 price=0.37 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=13281035.0 spike=0.5
- UNIT.CA: score=11.42 buy_ready=False sector_rank=17 price=17.94 support=18.11 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=49.52 liquidity=7095588.0 spike=0.48
- WCDF.CA: score=12.76 buy_ready=False sector_rank=13 price=710.67 support=636.31 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=77.57 liquidity=5773274.5 spike=1.18
- WKOL.CA: score=14.62 buy_ready=False sector_rank=13 price=331.37 support=335.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=50.52 liquidity=12776515.0 spike=0.84
- ZEOT.CA: score=12.23 buy_ready=False sector_rank=13 price=13.15 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=4602084.5 spike=0.68
- ZMID.CA: score=17.32 buy_ready=False sector_rank=17 price=8.4 support=7.9 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=139624256.0 spike=0.63

## Backtesting Lite
- GBCO.CA: 180d return=23.12%, max drawdown=-24.35%, MA20>MA50 days last20=0, as_of=2026-09-19T21:00:00+00:00
- CANA.CA: 180d return=25.92%, max drawdown=-36.46%, MA20>MA50 days last20=20, as_of=2026-09-19T21:00:00+00:00
- CICH.CA: 180d return=48.13%, max drawdown=-14.78%, MA20>MA50 days last20=20, as_of=2026-09-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=628 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- CICH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=CI Capital Holding summary=Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=628 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- ATQA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr National Steel Ataqa summary=Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for ATQA.CA: source text did not clearly match ATQA.CA / Misr National Steel Ataqa.
