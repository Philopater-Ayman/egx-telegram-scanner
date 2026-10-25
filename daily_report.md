# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-10-25T11:20:23.405213+00:00
Generated Cairo: 2026-10-25 14:20
Run timing: target 09:15 Cairo | generated Cairo 2026-10-25 14:20 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-10-25 14:17

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 42/186
- Top sector: Telecommunications

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, October 25
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 18.18% / above MA50 18.18%
- EGX70 regime: BEARISH / above MA20 0.0% / above MA50 22.22%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=381290528.0 spike=0.72 score=10.81
- ETEL.CA: liquidity=268075408.0 spike=1.13 score=9.18
- COMI.CA: liquidity=189190112.0 spike=0.42 score=15.27
- GBCO.CA: liquidity=154009616.0 spike=1.37 score=7.14
- TMGH.CA: liquidity=153843216.0 spike=0.59 score=15.36

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- EOSB.CA: spike=12.4 liquidity=443913.56 outlook=CONSTRUCTIVE score=61.27 buy_ready=False
- ELNA.CA: spike=10.99 liquidity=3047253.5 outlook=BULLISH_WATCH score=90.27 buy_ready=False
- SCTS.CA: spike=8.58 liquidity=16826168.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CPCI.CA: spike=2.33 liquidity=10826606.0 outlook=BULLISH_WATCH score=70.27 buy_ready=False
- NAHO.CA: spike=1.74 liquidity=27555.11 outlook=NEUTRAL score=35.27 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=4.81 5d=1.25% 20d=0.17% aboveMA50=50.0%
- #2 Basic Resources & Chemicals: score=2.64 5d=0.0% 20d=0.0% aboveMA50=20.0%
- #3 Investment Holding: score=2.03 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #4 Energy & Petrochemicals: score=2.02 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #5 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Transportation & Logistics: score=1.3 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 General / Verified EGX Expansion: score=1.27 5d=0.0% 20d=0.0% aboveMA50=3.96%
- #8 Industrial Goods & Cables: score=1.26 5d=0.0% 20d=0.0% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ABUK.CA: BULLISH_WATCH score=93.64 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- ELNA.CA: BULLISH_WATCH score=90.27 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MFPC.CA: BULLISH_WATCH score=81.64 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- CPCI.CA: BULLISH_WATCH score=70.27 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20
- EOSB.CA: CONSTRUCTIVE score=61.27 liquidity=THIN sector=IMPROVING risk=liquidity below minimum
- AMOC.CA: CONSTRUCTIVE score=60.02 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- BINV.CA: NEUTRAL score=48.03 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20; overheated RSI
- EGSA.CA: NEUTRAL score=43.81 liquidity=THIN sector=LEADING risk=liquidity below minimum; liquidity is cooling; momentum is extended; close to resistance
- IRON.CA: NEUTRAL score=42.64 liquidity=TRADEABLE sector=LEADING risk=below MA20; below MA50
- NAHO.CA: NEUTRAL score=35.27 liquidity=THIN sector=IMPROVING risk=liquidity below minimum; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=0.66 buy_ready=False sector_rank=7 price=197.48 support=195.0 resistance=223.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6149029.0 spike=0.64
- ABUK.CA: score=24.2 buy_ready=False sector_rank=2 price=89.85 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=58.15 liquidity=81885584.0 spike=1.07
- ACAMD.CA: score=15.51 buy_ready=False sector_rank=7 price=1.96 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=48.84 liquidity=32278698.0 spike=0.68
- ACGC.CA: score=2.7 buy_ready=False sector_rank=19 price=12.4 support=12.5 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=4005405.5 spike=0.36
- ADCI.CA: score=-4.09 buy_ready=False sector_rank=7 price=232.36 support=230.0 resistance=254.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1404305.75 spike=0.88
- ADIB.CA: score=9.11 buy_ready=False sector_rank=17 price=44.15 support=43.45 resistance=51.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=102836056.0 spike=1.42
- ADPC.CA: score=5.25 buy_ready=False sector_rank=7 price=2.62 support=2.53 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14721720.0 spike=1.37
- AFDI.CA: score=-3.05 buy_ready=False sector_rank=7 price=38.62 support=38.1 resistance=43.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2442709.25 spike=0.54
- AFMC.CA: score=-0.24 buy_ready=False sector_rank=7 price=100.67 support=98.0 resistance=116.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5247185.0 spike=0.29
- AJWA.CA: score=4.51 buy_ready=False sector_rank=7 price=191.41 support=191.0 resistance=221.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23030606.0 spike=0.65
- ALCN.CA: score=4.52 buy_ready=False sector_rank=6 price=29.13 support=27.11 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13226420.0 spike=0.6
- ALUM.CA: score=-1.83 buy_ready=False sector_rank=7 price=17.79 support=17.5 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3665555.5 spike=0.94
- AMER.CA: score=4.36 buy_ready=False sector_rank=14 price=3.46 support=3.4 resistance=4.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27852160.0 spike=0.54
- AMES.CA: score=4.51 buy_ready=False sector_rank=7 price=29.22 support=29.0 resistance=33.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24204506.0 spike=0.4
- AMIA.CA: score=4.51 buy_ready=False sector_rank=7 price=16.21 support=15.33 resistance=17.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11598828.0 spike=0.7
- AMOC.CA: score=17.81 buy_ready=False sector_rank=4 price=13.0 support=12.18 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=96128264.0 spike=0.76
- APSW.CA: score=3.9 buy_ready=False sector_rank=7 price=7.48 support=7.61 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=36.02 liquidity=394410.13 spike=0.67
- ARAB.CA: score=4.36 buy_ready=False sector_rank=14 price=0.22 support=0.2 resistance=0.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69182632.0 spike=0.63
- ARCC.CA: score=4.31 buy_ready=False sector_rank=16 price=59.15 support=58.12 resistance=65.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27250858.0 spike=0.63
- AREH.CA: score=2.37 buy_ready=False sector_rank=7 price=0.98 support=0.94 resistance=1.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7866814.5 spike=0.98
- ASCM.CA: score=2.65 buy_ready=False sector_rank=7 price=40.17 support=40.0 resistance=46.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8142861.5 spike=0.86
- ASPI.CA: score=4.51 buy_ready=False sector_rank=7 price=0.28 support=0.27 resistance=0.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11166767.0 spike=0.54
- ATLC.CA: score=0.59 buy_ready=False sector_rank=9 price=4.17 support=4.14 resistance=4.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6106931.5 spike=0.81
- ATQA.CA: score=7.06 buy_ready=False sector_rank=2 price=8.85 support=8.43 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31689364.0 spike=0.56
- AXPH.CA: score=2.77 buy_ready=False sector_rank=7 price=1178.26 support=1135.0 resistance=1260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7744100.0 spike=1.26
- BINV.CA: score=13.15 buy_ready=False sector_rank=3 price=57.29 support=52.11 resistance=65.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=37.96 liquidity=4341522.0 spike=0.3
- BIOC.CA: score=4.51 buy_ready=False sector_rank=7 price=226.53 support=213.0 resistance=261.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21214088.0 spike=0.2
- BTFH.CA: score=5.47 buy_ready=False sector_rank=9 price=2.14 support=2.05 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=144717232.0 spike=1.49
- CAED.CA: score=0.3 buy_ready=False sector_rank=7 price=73.67 support=70.0 resistance=85.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5790087.5 spike=0.7
- CANA.CA: score=1.25 buy_ready=False sector_rank=17 price=39.87 support=39.24 resistance=42.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6973278.5 spike=0.39
- CCAP.CA: score=10.81 buy_ready=False sector_rank=3 price=6.26 support=5.87 resistance=7.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=381290528.0 spike=0.72
- CCRS.CA: score=-0.3 buy_ready=False sector_rank=7 price=1.59 support=1.55 resistance=1.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5193259.0 spike=0.76
- CEFM.CA: score=-4.43 buy_ready=False sector_rank=7 price=110.86 support=103.05 resistance=125.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1064253.63 spike=0.5
- CERA.CA: score=4.51 buy_ready=False sector_rank=7 price=1.04 support=1.01 resistance=1.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=84518144.0 spike=0.68
- CFGH.CA: score=-1.49 buy_ready=False sector_rank=7 price=0.11 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=16.67 liquidity=1202.89 spike=0.24
- CICH.CA: score=-3.49 buy_ready=False sector_rank=9 price=10.24 support=10.15 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2020967.75 spike=0.88
- CIEB.CA: score=0.37 buy_ready=False sector_rank=17 price=21.52 support=21.5 resistance=22.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6100468.0 spike=0.67
- CIRA.CA: score=3.15 buy_ready=False sector_rank=13 price=32.83 support=32.01 resistance=36.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8793402.0 spike=0.5
- CLHO.CA: score=8.46 buy_ready=False sector_rank=10 price=13.29 support=13.0 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=15.19 liquidity=29913694.0 spike=0.82
- CNFN.CA: score=1.43 buy_ready=False sector_rank=9 price=3.59 support=3.55 resistance=4.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6946077.0 spike=0.73
- COMI.CA: score=15.27 buy_ready=False sector_rank=17 price=122.99 support=120.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=43.17 liquidity=189190112.0 spike=0.42
- COPR.CA: score=4.51 buy_ready=False sector_rank=7 price=0.36 support=0.33 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12529421.0 spike=0.74
- COSG.CA: score=4.51 buy_ready=False sector_rank=7 price=1.13 support=1.11 resistance=1.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11039295.0 spike=0.91
- CPCI.CA: score=20.17 buy_ready=False sector_rank=7 price=577.94 support=502.25 resistance=619.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=10826606.0 spike=2.33
- CSAG.CA: score=2.47 buy_ready=False sector_rank=6 price=30.15 support=30.1 resistance=34.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7666104.5 spike=1.14
- DAPH.CA: score=4.51 buy_ready=False sector_rank=7 price=68.36 support=65.2 resistance=80.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16356335.0 spike=0.39
- DEIN.CA: score=7.51 buy_ready=False sector_rank=7 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=7 October 09:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37.26 spike=0.01
- DOMT.CA: score=-3.56 buy_ready=False sector_rank=15 price=20.62 support=20.27 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2106617.0 spike=0.59
- DSCW.CA: score=4.51 buy_ready=False sector_rank=7 price=1.27 support=1.23 resistance=1.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13575426.0 spike=0.84
- DTPP.CA: score=4.51 buy_ready=False sector_rank=7 price=42.19 support=41.81 resistance=51.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28346176.0 spike=0.65
- EALR.CA: score=-3.04 buy_ready=False sector_rank=7 price=241.22 support=240.0 resistance=283.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2452227.5 spike=0.71
- EASB.CA: score=-2.61 buy_ready=False sector_rank=7 price=5.21 support=5.03 resistance=6.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2881838.0 spike=0.58
- EAST.CA: score=4.33 buy_ready=False sector_rank=15 price=28.83 support=28.3 resistance=30.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22340686.0 spike=0.5
- EBSC.CA: score=-0.94 buy_ready=False sector_rank=7 price=1.28 support=1.25 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3312722.75 spike=1.62
- ECAP.CA: score=-3.19 buy_ready=False sector_rank=7 price=25.54 support=25.0 resistance=27.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2299731.0 spike=0.61
- EDFM.CA: score=0.08 buy_ready=False sector_rank=7 price=375.69 support=335.2 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=34.92 liquidity=568979.19 spike=0.51
- EEII.CA: score=-0.16 buy_ready=False sector_rank=7 price=1.52 support=1.51 resistance=1.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5330401.5 spike=0.73
- EFIC.CA: score=7.06 buy_ready=False sector_rank=2 price=129.5 support=121.0 resistance=149.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21884930.0 spike=0.75
- EFID.CA: score=4.33 buy_ready=False sector_rank=15 price=16.86 support=16.5 resistance=18.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14789053.0 spike=0.34
- EFIH.CA: score=11.66 buy_ready=False sector_rank=20 price=21.44 support=20.2 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=70742816.0 spike=1.11
- EGAL.CA: score=11.12 buy_ready=False sector_rank=2 price=292.3 support=275.0 resistance=362.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=28.15 liquidity=92009424.0 spike=1.03
- EGAS.CA: score=-1.24 buy_ready=False sector_rank=4 price=44.92 support=43.55 resistance=49.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3952791.0 spike=0.56
- EGBE.CA: score=4.35 buy_ready=False sector_rank=17 price=0.48 support=0.5 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=35.14 liquidity=74874.51 spike=0.56
- EGCH.CA: score=7.06 buy_ready=False sector_rank=2 price=10.36 support=10.0 resistance=11.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53093356.0 spike=0.75
- EGSA.CA: score=15.93 buy_ready=False sector_rank=1 price=9.03 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=66.07 liquidity=3332.07 spike=0.57
- EGTS.CA: score=-2.46 buy_ready=False sector_rank=14 price=11.28 support=11.15 resistance=12.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3187280.0 spike=0.12
- EHDR.CA: score=5.43 buy_ready=False sector_rank=7 price=1.86 support=1.8 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15015979.0 spike=1.46
- ELEC.CA: score=4.5 buy_ready=False sector_rank=8 price=1.43 support=1.36 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48876756.0 spike=0.97
- ELKA.CA: score=3.58 buy_ready=False sector_rank=7 price=1.28 support=1.28 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9071698.0 spike=0.69
- ELNA.CA: score=21.56 buy_ready=False sector_rank=7 price=38.82 support=33.46 resistance=36.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=3047253.5 spike=10.99
- ELSH.CA: score=4.51 buy_ready=False sector_rank=7 price=8.62 support=8.6 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13698177.0 spike=0.68
- ELWA.CA: score=8.77 buy_ready=False sector_rank=7 price=1.65 support=1.43 resistance=1.7 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=261084.45 spike=0.72
- EMFD.CA: score=4.36 buy_ready=False sector_rank=14 price=10.8 support=10.6 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14367331.0 spike=0.23
- ENGC.CA: score=0.74 buy_ready=False sector_rank=7 price=28.73 support=28.7 resistance=31.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6233887.5 spike=0.55
- EOSB.CA: score=16.95 buy_ready=False sector_rank=7 price=1.64 support=1.57 resistance=1.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=443913.56 spike=12.4
- EPCO.CA: score=-3.43 buy_ready=False sector_rank=7 price=7.24 support=7.0 resistance=8.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2064944.0 spike=0.49
- EPPK.CA: score=-5.07 buy_ready=False sector_rank=7 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=9.18 buy_ready=False sector_rank=1 price=127.01 support=121.01 resistance=132.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=268075408.0 spike=1.13
- ETRS.CA: score=5.05 buy_ready=False sector_rank=7 price=9.64 support=9.51 resistance=10.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12905229.0 spike=1.27
- EXPA.CA: score=2.07 buy_ready=False sector_rank=17 price=12.94 support=12.52 resistance=14.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7801098.5 spike=0.2
- FAIT.CA: score=6.85 buy_ready=False sector_rank=17 price=42.06 support=40.4 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=2581413.25 spike=0.85
- FAITA.CA: score=6.28 buy_ready=False sector_rank=17 price=0.99 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=57.84 liquidity=10637.67 spike=0.3
- FERC.CA: score=2.26 buy_ready=False sector_rank=2 price=55.05 support=53.57 resistance=63.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4485033.5 spike=1.36
- FWRY.CA: score=11.44 buy_ready=False sector_rank=20 price=17.35 support=17.33 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=94346936.0 spike=0.84
- GBCO.CA: score=7.14 buy_ready=False sector_rank=21 price=24.22 support=24.6 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=23.98 liquidity=154009616.0 spike=1.37
- GDWA.CA: score=4.51 buy_ready=False sector_rank=7 price=0.5 support=0.49 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10799332.0 spike=0.68
- GGCC.CA: score=2.56 buy_ready=False sector_rank=7 price=0.54 support=0.5 resistance=0.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8055635.0 spike=0.51
- GIHD.CA: score=4.45 buy_ready=False sector_rank=7 price=36.37 support=34.83 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9943188.0 spike=0.53
- GMCI.CA: score=5.57 buy_ready=False sector_rank=7 price=1.54 support=1.47 resistance=1.77 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=45.16 liquidity=59006.64 spike=0.18
- GRCA.CA: score=-3.47 buy_ready=False sector_rank=7 price=24.66 support=24.0 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2023441.13 spike=0.37
- GSSC.CA: score=-4.83 buy_ready=False sector_rank=7 price=234.92 support=222.22 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=666679.63 spike=0.51
- HDBK.CA: score=4.27 buy_ready=False sector_rank=17 price=85.07 support=83.01 resistance=93.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16580026.0 spike=0.82
- HELI.CA: score=4.84 buy_ready=False sector_rank=14 price=6.19 support=5.96 resistance=6.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81242000.0 spike=1.24
- HRHO.CA: score=13.49 buy_ready=False sector_rank=9 price=23.92 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=51.87 liquidity=37244048.0 spike=0.29
- ICID.CA: score=-2.51 buy_ready=False sector_rank=7 price=15.0 support=14.26 resistance=16.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2979753.5 spike=0.41
- IDRE.CA: score=1.44 buy_ready=False sector_rank=7 price=32.04 support=31.58 resistance=39.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6628967.5 spike=1.15
- IFAP.CA: score=-2.05 buy_ready=False sector_rank=12 price=16.57 support=15.51 resistance=17.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3565745.0 spike=0.65
- INFI.CA: score=4.51 buy_ready=False sector_rank=7 price=99.88 support=99.0 resistance=121.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17390936.0 spike=0.83
- IRON.CA: score=15.63 buy_ready=False sector_rank=2 price=24.57 support=24.25 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=47.35 liquidity=9572483.0 spike=0.89
- ISMA.CA: score=-1.44 buy_ready=False sector_rank=7 price=16.55 support=16.31 resistance=20.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4054495.0 spike=0.57
- ISMQ.CA: score=7.14 buy_ready=False sector_rank=2 price=6.21 support=6.0 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18012980.0 spike=1.04
- ISPH.CA: score=5.04 buy_ready=False sector_rank=10 price=9.48 support=9.14 resistance=10.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60771316.0 spike=1.29
- JUFO.CA: score=3.16 buy_ready=False sector_rank=15 price=21.52 support=21.04 resistance=23.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8831803.0 spike=0.49
- KABO.CA: score=3.69 buy_ready=False sector_rank=19 price=6.06 support=6.02 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10198316.0 spike=0.47
- KWIN.CA: score=-3.17 buy_ready=False sector_rank=7 price=48.89 support=48.5 resistance=60.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2320868.5 spike=0.42
- KZPC.CA: score=-0.52 buy_ready=False sector_rank=7 price=12.1 support=12.0 resistance=13.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4970794.0 spike=0.59
- LCSW.CA: score=1.7 buy_ready=False sector_rank=16 price=30.14 support=29.5 resistance=33.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7388319.0 spike=0.36
- LUTS.CA: score=4.51 buy_ready=False sector_rank=7 price=0.52 support=0.51 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51879992.0 spike=0.96
- MAAL.CA: score=0.28 buy_ready=False sector_rank=7 price=5.26 support=5.26 resistance=6.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5772413.0 spike=0.26
- MASR.CA: score=4.61 buy_ready=False sector_rank=7 price=5.99 support=5.6 resistance=6.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51464436.0 spike=1.05
- MBSC.CA: score=4.31 buy_ready=False sector_rank=16 price=276.53 support=262.0 resistance=316.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38342428.0 spike=0.4
- MCQE.CA: score=4.31 buy_ready=False sector_rank=16 price=150.07 support=145.05 resistance=164.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48843064.0 spike=0.78
- MCRO.CA: score=4.51 buy_ready=False sector_rank=7 price=1.15 support=1.12 resistance=1.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32204280.0 spike=0.69
- MENA.CA: score=-4.26 buy_ready=False sector_rank=14 price=5.59 support=5.58 resistance=5.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1387052.0 spike=0.68
- MEPA.CA: score=-1.19 buy_ready=False sector_rank=7 price=1.24 support=1.23 resistance=1.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4303945.5 spike=0.59
- MFPC.CA: score=22.66 buy_ready=False sector_rank=2 price=45.95 support=40.66 resistance=48.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=49.02 liquidity=61223092.0 spike=1.3
- MFSC.CA: score=-3.7 buy_ready=False sector_rank=7 price=34.49 support=33.05 resistance=38.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1787026.88 spike=0.77
- MHOT.CA: score=-3.98 buy_ready=False sector_rank=18 price=13.17 support=13.0 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1947020.0 spike=0.12
- MICH.CA: score=0.46 buy_ready=False sector_rank=7 price=37.84 support=37.35 resistance=42.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5949903.0 spike=0.7
- MILS.CA: score=5.11 buy_ready=False sector_rank=7 price=106.4 support=106.4 resistance=133.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9920022.0 spike=1.34
- MIPH.CA: score=-4.57 buy_ready=False sector_rank=10 price=683.18 support=610.0 resistance=745.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=977232.69 spike=0.24
- MOED.CA: score=5.63 buy_ready=False sector_rank=7 price=0.42 support=0.42 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20184846.0 spike=1.56
- MOIL.CA: score=-0.03 buy_ready=False sector_rank=4 price=0.64 support=0.63 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=157669.69 spike=0.68
- MOIN.CA: score=-2.35 buy_ready=False sector_rank=7 price=26.97 support=25.88 resistance=30.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3139501.75 spike=0.32
- MOSC.CA: score=-4.43 buy_ready=False sector_rank=7 price=231.9 support=226.38 resistance=249.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1058369.88 spike=0.31
- MPCI.CA: score=4.51 buy_ready=False sector_rank=7 price=247.1 support=239.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42289236.0 spike=0.43
- MPCO.CA: score=4.38 buy_ready=False sector_rank=12 price=1.65 support=1.55 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60626752.0 spike=0.61
- MPRC.CA: score=4.51 buy_ready=False sector_rank=7 price=28.33 support=27.1 resistance=33.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14364089.0 spike=0.89
- MTIE.CA: score=2.4 buy_ready=False sector_rank=21 price=6.57 support=6.51 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12002270.0 spike=0.6
- NAHO.CA: score=6.02 buy_ready=False sector_rank=7 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=27555.11 spike=1.74
- NCCW.CA: score=4.51 buy_ready=False sector_rank=7 price=4.38 support=4.21 resistance=5.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11756073.0 spike=0.43
- NEDA.CA: score=1.68 buy_ready=False sector_rank=7 price=2.6 support=2.47 resistance=2.75 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=175562.39 spike=0.69
- NHPS.CA: score=-0.15 buy_ready=False sector_rank=7 price=50.77 support=50.06 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5337025.0 spike=0.54
- NINH.CA: score=0.74 buy_ready=False sector_rank=7 price=12.8 support=12.36 resistance=14.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6229807.5 spike=0.56
- NIPH.CA: score=4.46 buy_ready=False sector_rank=10 price=228.4 support=220.0 resistance=266.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=76040688.0 spike=0.64
- OBRI.CA: score=4.51 buy_ready=False sector_rank=7 price=20.0 support=19.8 resistance=24.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10601837.0 spike=0.73
- OCDI.CA: score=4.36 buy_ready=False sector_rank=14 price=22.56 support=21.0 resistance=24.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24931084.0 spike=0.67
- OCPH.CA: score=-0.97 buy_ready=False sector_rank=7 price=151.53 support=147.96 resistance=183.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3866184.0 spike=1.33
- ODIN.CA: score=0.53 buy_ready=False sector_rank=7 price=1.85 support=1.8 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6025315.5 spike=0.98
- OFH.CA: score=4.51 buy_ready=False sector_rank=7 price=0.64 support=0.63 resistance=0.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15673403.0 spike=0.24
- OIH.CA: score=5.81 buy_ready=False sector_rank=3 price=1.66 support=1.64 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46755660.0 spike=0.69
- OLFI.CA: score=2.48 buy_ready=False sector_rank=15 price=18.33 support=18.02 resistance=19.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8152008.0 spike=0.55
- ORAS.CA: score=4.6 buy_ready=False sector_rank=5 price=825.96 support=780.0 resistance=839.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=143791872.0 spike=1.0
- ORHD.CA: score=10.36 buy_ready=False sector_rank=14 price=9.32 support=9.5 resistance=41.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=19.52 liquidity=111930208.0 spike=0.92
- ORWE.CA: score=3.69 buy_ready=False sector_rank=19 price=23.63 support=23.5 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17917820.0 spike=0.43
- PHAR.CA: score=4.46 buy_ready=False sector_rank=10 price=95.12 support=91.61 resistance=101.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42020016.0 spike=0.7
- PHDC.CA: score=4.36 buy_ready=False sector_rank=14 price=11.7 support=11.45 resistance=12.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=64460960.0 spike=0.65
- PHTV.CA: score=5.42 buy_ready=False sector_rank=7 price=316.18 support=310.02 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=41.97 liquidity=907099.38 spike=0.92
- POUL.CA: score=4.89 buy_ready=False sector_rank=15 price=9.1 support=8.85 resistance=9.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68351512.0 spike=1.28
- PRCL.CA: score=2.65 buy_ready=False sector_rank=16 price=17.29 support=17.25 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8343323.5 spike=0.81
- PRDC.CA: score=4.36 buy_ready=False sector_rank=14 price=5.58 support=5.45 resistance=6.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10136545.0 spike=0.28
- PRMH.CA: score=-3.82 buy_ready=False sector_rank=7 price=1.76 support=1.7 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1673763.25 spike=0.53
- RACC.CA: score=-1.22 buy_ready=False sector_rank=7 price=7.24 support=7.13 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4272388.0 spike=0.64
- RAKT.CA: score=9.8 buy_ready=False sector_rank=7 price=23.06 support=20.26 resistance=25.08 source=Yahoo Finance as_of=2026-10-21T21:00:00+00:00 freshness=FRESH RSI=66.11 liquidity=292631.39 spike=0.74
- RAYA.CA: score=4.42 buy_ready=False sector_rank=11 price=5.22 support=5.02 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20450788.0 spike=0.7
- RMDA.CA: score=13.46 buy_ready=False sector_rank=10 price=4.76 support=4.8 resistance=5.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=35.1 liquidity=22748088.0 spike=0.85
- ROTO.CA: score=4.83 buy_ready=False sector_rank=7 price=27.16 support=25.0 resistance=31.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10009745.0 spike=1.16
- RREI.CA: score=1.46 buy_ready=False sector_rank=7 price=2.48 support=2.42 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6954535.5 spike=0.99
- RTVC.CA: score=-2.27 buy_ready=False sector_rank=7 price=3.04 support=3.04 resistance=3.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2924114.0 spike=1.15
- RUBX.CA: score=4.51 buy_ready=False sector_rank=7 price=12.5 support=12.5 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88214576.0 spike=0.95
- SAUD.CA: score=6.64 buy_ready=False sector_rank=17 price=20.08 support=20.2 resistance=24.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=31.68 liquidity=8371303.0 spike=0.65
- SCEM.CA: score=4.31 buy_ready=False sector_rank=16 price=75.63 support=75.11 resistance=83.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22170012.0 spike=0.36
- SCFM.CA: score=-2.45 buy_ready=False sector_rank=7 price=192.57 support=185.0 resistance=222.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2325449.75 spike=1.36
- SCTS.CA: score=9.36 buy_ready=False sector_rank=13 price=419.98 support=416.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16826168.0 spike=8.58
- SDTI.CA: score=5.07 buy_ready=False sector_rank=7 price=75.49 support=75.01 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35330952.0 spike=1.28
- SEIG.CA: score=-3.78 buy_ready=False sector_rank=7 price=150.41 support=142.0 resistance=174.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1716641.38 spike=0.84
- SIPC.CA: score=4.51 buy_ready=False sector_rank=7 price=4.1 support=4.09 resistance=4.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30756352.0 spike=0.54
- SKPC.CA: score=11.06 buy_ready=False sector_rank=2 price=14.38 support=14.4 resistance=17.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.65 liquidity=32101744.0 spike=0.46
- SMFR.CA: score=-3.04 buy_ready=False sector_rank=7 price=176.1 support=173.0 resistance=197.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2452095.75 spike=0.79
- SNFC.CA: score=-0.33 buy_ready=False sector_rank=7 price=10.58 support=10.3 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5157213.5 spike=0.61
- SPIN.CA: score=1.94 buy_ready=False sector_rank=19 price=13.62 support=13.5 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=27.5 liquidity=4248229.0 spike=0.8
- SPMD.CA: score=0.37 buy_ready=False sector_rank=7 price=0.32 support=0.31 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5862277.5 spike=0.48
- SUGR.CA: score=-0.51 buy_ready=False sector_rank=15 price=51.08 support=50.6 resistance=54.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5159733.0 spike=0.55
- SVCE.CA: score=4.51 buy_ready=False sector_rank=7 price=7.55 support=7.01 resistance=8.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33733344.0 spike=0.48
- SWDY.CA: score=4.5 buy_ready=False sector_rank=8 price=101.18 support=97.0 resistance=107.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46358244.0 spike=0.71
- TALM.CA: score=4.36 buy_ready=False sector_rank=13 price=17.79 support=17.0 resistance=19.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17269608.0 spike=0.6
- TMGH.CA: score=15.36 buy_ready=False sector_rank=14 price=83.86 support=80.01 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=153843216.0 spike=0.59
- TRTO.CA: score=0.26 buy_ready=False sector_rank=7 price=0.06 support=0.05 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=8965.14 spike=1.37
- UEFM.CA: score=-4.71 buy_ready=False sector_rank=7 price=445.22 support=430.0 resistance=481.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=779602.06 spike=0.27
- UEGC.CA: score=4.51 buy_ready=False sector_rank=7 price=1.26 support=1.21 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26226678.0 spike=0.58
- UNIP.CA: score=0.45 buy_ready=False sector_rank=7 price=0.27 support=0.26 resistance=0.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5943299.0 spike=0.73
- UNIT.CA: score=-3.62 buy_ready=False sector_rank=14 price=15.42 support=15.06 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2021751.88 spike=0.53
- WCDF.CA: score=-0.74 buy_ready=False sector_rank=7 price=477.22 support=432.5 resistance=686.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=17.19 liquidity=754735.13 spike=0.28
- WKOL.CA: score=0.6 buy_ready=False sector_rank=7 price=244.51 support=240.91 resistance=275.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6087165.0 spike=0.83
- ZEOT.CA: score=0.34 buy_ready=False sector_rank=7 price=9.4 support=9.4 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5827038.0 spike=0.74
- ZMID.CA: score=4.36 buy_ready=False sector_rank=14 price=6.15 support=6.01 resistance=6.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44020460.0 spike=0.59

## Backtesting Lite
- ABUK.CA: 180d return=62.36%, max drawdown=-26.86%, MA20>MA50 days last20=20, as_of=2026-10-21T21:00:00+00:00
- MFPC.CA: 180d return=51.02%, max drawdown=-26.33%, MA20>MA50 days last20=20, as_of=2026-10-21T21:00:00+00:00
- ELNA.CA: 180d return=-1.83%, max drawdown=-15.86%, MA20>MA50 days last20=0, as_of=2026-10-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ABUK.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Qir Fertilizers summary=Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results; Abu Qir Fertilizers&#39; board approves $5.6m coated urea project; Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26
  - Abu Qir Fertilizers generates EGP 5.6bn net profits in Q1-26 unaudited results: https://english.mubasher.info/news/4604919/Abu-Qir-Fertilizers-generates-EGP-5-6bn-net-profits-in-Q1-26-unaudited-results/
  - Abu Qir Fertilizers&#39; board approves $5.6m coated urea project: https://english.mubasher.info/news/4585599/Abu-Qir-Fertilizers-board-approves-5-6m-coated-urea-project/
  - Abu Qir Fertilizers&#39; profits exceed EGP 5.1bn in H1-25/26: https://english.mubasher.info/news/4554415/Abu-Qir-Fertilizers-profits-exceed-EGP-5-1bn-in-H1-25-26/
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- ELNA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Manufacturing Agricultural Crops S.A.E summary=Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops; El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m; EGX halts trading on El Nasr for Manufacturing Agricultural Crops
  - Consortium offers to acquire controlling stake in El Nasr for Agricultural Crops: https://english.mubasher.info/news/3749421/Consortium-offers-to-acquire-controlling-stake-in-El-Nasr-for-Agricultural-Crops/
  - El Nasr for Agricultural Crops to sell Sohag factory land for EGP 650m: https://english.mubasher.info/news/3685533/El-Nasr-for-Agricultural-Crops-to-sell-Sohag-factory-land-for-EGP-650m/
  - EGX halts trading on El Nasr for Manufacturing Agricultural Crops: https://english.mubasher.info/news/3489525/EGX-halts-trading-on-El-Nasr-for-Manufacturing-Agricultural-Crops/
- CPCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Kahira Pharmaceuticals & Chemical Industries Company summary=Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22; Kahira Pharmaceuticals sees EGP 9m block trading deal; Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals
  - Kahira Pharmaceuticals&#39; net profits up 22.5% in H1-21/22: https://english.mubasher.info/news/3910780/Kahira-Pharmaceuticals-net-profits-up-22-5-in-H1-21-22/
  - Kahira Pharmaceuticals sees EGP 9m block trading deal: https://english.mubasher.info/news/3903033/Kahira-Pharmaceuticals-sees-EGP-9m-block-trading-deal/
  - Adel Taha Abdel Wahab named Chairman of Kahira Pharmaceuticals: https://english.mubasher.info/news/3816375/Adel-Taha-Abdel-Wahab-named-Chairman-of-Kahira-Pharmaceuticals/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- EOSB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Orouba Securities Brokerage summary=El Orouba Brokerage turns profitable in Q4; El Orouba Securities suffers 598,000 losses in Q3; El Orouba Securities H1 losses down 7%
  - El Orouba Brokerage turns profitable in Q4: https://english.mubasher.info/news/3067539/El-Orouba-Brokerage-turns-profitable-in-Q4/
  - El Orouba Securities suffers 598,000 losses in Q3: https://english.mubasher.info/news/3016624/El-Orouba-Securities-suffers-598-000-losses-in-Q3/
  - El Orouba Securities H1 losses down 7%: https://english.mubasher.info/news/2984110/El-Orouba-Securities-H1-losses-down-7-/
- EGSA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Satellites summary=Evidence rejected for EGSA.CA: source text did not clearly match EGSA.CA / Egyptian Satellites.
- IRON.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Iron and Steel summary=Evidence rejected for IRON.CA: source text did not clearly match IRON.CA / Egyptian Iron and Steel.

## Warnings
- OpenRouter API error: 404
- Evidence for ABUK.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
- Evidence for ELNA.CA matches the company but no source/report date was detected.
- Evidence for CPCI.CA matches the company but no source/report date was detected.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for EOSB.CA matches the company but no source/report date was detected.
- Evidence rejected for EGSA.CA: source text did not clearly match EGSA.CA / Egyptian Satellites.
- Evidence rejected for IRON.CA: source text did not clearly match IRON.CA / Egyptian Iron and Steel.
