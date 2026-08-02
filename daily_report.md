# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-08-02T17:38:57.647303+00:00
Generated Cairo: 2026-08-02 20:38
Run timing: target 19:30 Cairo | generated Cairo 2026-08-02 20:38 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-08-02 20:30

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 163/189
- Top sector: Education

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 42.86% / above MA50 38.1%
- EGX70 regime: MIXED / above MA20 54.05% / above MA50 72.97%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=619470720.0 spike=0.86 score=21.4
- AMOC.CA: liquidity=396186689.4 spike=5.06 score=27.4
- TMGH.CA: liquidity=387810373.56 spike=1.06 score=18.65
- PHAR.CA: liquidity=343604448.0 spike=4.09 score=10.87
- AFMC.CA: liquidity=332427872.0 spike=4.29 score=11.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner highlights accumulation spikes in several stocks with bullish‑watch outlooks, but the EGX30 bearish trend, weak sector breadth (14%) and defensive risk mode keep new buys on hold.
- EGX30 below MA20/MA50 and EGX70 mixed → overall market defensive, risk mode = DEFENSIVE_NO_NEW_BUY.
- Top tickets (WKOL.CA, MOSC.CA, EALR.CA, etc.) show strong liquidity spikes and bullish‑watch scores, yet sit in non‑leading sectors with extended momentum.
- Many are close to resistance (high RSI, small resistance distance) and have limited support upside, suggesting near‑term pull‑back risk.
- Outlook for the next 1‑3 days remains uncertain:3 days depends on whether breadth or liquidity improves; otherwise defensive stance persists.

## Top Liquidity Spikes
- EGAS.CA: spike=9.68 liquidity=131700792.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ATLC.CA: spike=8.06 liquidity=54332440.0 outlook=BULLISH_WATCH score=80.55 buy_ready=False
- EOSB.CA: spike=7.81 liquidity=446389.14 outlook=CONSTRUCTIVE score=61.17 buy_ready=False
- MFSC.CA: spike=7.75 liquidity=44535960.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ADCI.CA: spike=7.48 liquidity=76351768.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Education: score=12.85 5d=10.29% 20d=11.08% aboveMA50=100.0%
- #2 Energy & Petrochemicals: score=9.72 5d=3.23% 20d=7.49% aboveMA50=50.0%
- #3 Agriculture & Food Production: score=9.67 5d=3.28% 20d=3.81% aboveMA50=100.0%
- #4 Textiles: score=8.29 5d=-2.65% 20d=12.23% aboveMA50=100.0%
- #5 Investment Holding: score=6.59 5d=-0.68% 20d=3.55% aboveMA50=100.0%
- #6 Banking & Financials: score=6.54 5d=-0.26% 20d=2.36% aboveMA50=70.0%
- #7 Telecommunications: score=6.26 5d=-0.45% 20d=6.8% aboveMA50=50.0%
- #8 General / Verified EGX Expansion: score=6.17 5d=-0.07% 20d=6.86% aboveMA50=65.05%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=100 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- IFAP.CA: BULLISH_WATCH score=89.67 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EALR.CA: BULLISH_WATCH score=88.17 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- AXPH.CA: BULLISH_WATCH score=88.17 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- TALM.CA: BULLISH_WATCH score=85 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- WKOL.CA: BULLISH_WATCH score=84.17 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- ORWE.CA: BULLISH_WATCH score=83.29 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CCAP.CA: BULLISH_WATCH score=81.59 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- SAUD.CA: BULLISH_WATCH score=81.54 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- FAIT.CA: BULLISH_WATCH score=81.54 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=11.4 buy_ready=False sector_rank=8 price=306.07 support=279.0 resistance=317.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=124318408.0 spike=4.22
- ABUK.CA: score=19.52 buy_ready=False sector_rank=16 price=73.0 support=67.73 resistance=75.59 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=59.64 liquidity=162141468.0 spike=1.03
- ACAMD.CA: score=19.4 buy_ready=False sector_rank=8 price=2.36 support=2.21 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=47201280.0 spike=0.65
- ACGC.CA: score=21.4 buy_ready=False sector_rank=4 price=10.5 support=9.15 resistance=11.14 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=68.12 liquidity=15821925.0 spike=0.52
- ADCI.CA: score=11.4 buy_ready=False sector_rank=8 price=283.54 support=256.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=76351768.0 spike=7.48
- ADIB.CA: score=21.14 buy_ready=False sector_rank=6 price=52.85 support=46.0 resistance=52.88 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=79.01 liquidity=190469650.45 spike=1.37
- ADPC.CA: score=23.04 buy_ready=False sector_rank=8 price=3.86 support=3.45 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=9635594.0 spike=0.27
- AFDI.CA: score=8.44 buy_ready=False sector_rank=8 price=54.5 support=52.0 resistance=54.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36040040.0 spike=2.02
- AFMC.CA: score=11.4 buy_ready=False sector_rank=8 price=218.55 support=184.78 resistance=221.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=332427872.0 spike=4.29
- AJWA.CA: score=26.2 buy_ready=False sector_rank=8 price=191.12 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 July 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.35 liquidity=75489496.0 spike=2.4
- ALCN.CA: score=20.24 buy_ready=False sector_rank=17 price=29.44 support=28.2 resistance=30.54 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=60.92 liquidity=12469547.75 spike=0.55
- ALUM.CA: score=14.78 buy_ready=False sector_rank=8 price=23.47 support=21.1 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.17 liquidity=1380322.88 spike=0.23
- AMER.CA: score=5.53 buy_ready=False sector_rank=14 price=4.84 support=4.46 resistance=4.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67817712.0 spike=0.59
- AMES.CA: score=21.4 buy_ready=False sector_rank=8 price=124.07 support=57.5 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.57 liquidity=30782356.0 spike=0.3
- AMIA.CA: score=5.58 buy_ready=False sector_rank=8 price=11.83 support=11.26 resistance=11.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9180860.0 spike=0.61
- AMOC.CA: score=27.4 buy_ready=False sector_rank=2 price=8.91 support=7.65 resistance=9.04 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=76.37 liquidity=396186689.4 spike=5.06
- APSW.CA: score=10.88 buy_ready=False sector_rank=8 price=8.72 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.12 liquidity=1479139.0 spike=0.96
- ARAB.CA: score=18.53 buy_ready=False sector_rank=14 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=45240380.0 spike=0.33
- ARCC.CA: score=23.39 buy_ready=False sector_rank=9 price=56.38 support=54.2 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.72 liquidity=17731830.0 spike=0.63
- AREH.CA: score=7.91 buy_ready=False sector_rank=8 price=1.41 support=1.38 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=6513344.0 spike=0.23
- ARVA.CA: score=8.4 buy_ready=False sector_rank=8 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=81.59 liquidity=0.0 spike=0.0
- ASCM.CA: score=8.52 buy_ready=False sector_rank=8 price=65.53 support=62.0 resistance=67.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=112706272.0 spike=2.06
- ASPI.CA: score=18.4 buy_ready=False sector_rank=8 price=0.43 support=0.31 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=28534598.0 spike=0.73
- ATLC.CA: score=25.82 buy_ready=False sector_rank=12 price=5.4 support=5.0 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=54332440.0 spike=8.06
- ATQA.CA: score=22.84 buy_ready=False sector_rank=16 price=9.78 support=9.43 resistance=10.37 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=59.2 liquidity=48011749.75 spike=1.19
- AXPH.CA: score=20.3 buy_ready=False sector_rank=8 price=1246.92 support=1090.02 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=7304428.5 spike=1.8
- BINV.CA: score=12.74 buy_ready=False sector_rank=5 price=48.02 support=45.97 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.06 liquidity=3342524.0 spike=0.46
- BIOC.CA: score=11.4 buy_ready=False sector_rank=8 price=287.71 support=241.15 resistance=287.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=300349440.0 spike=3.8
- BTFH.CA: score=17.22 buy_ready=False sector_rank=12 price=3.06 support=2.91 resistance=3.2 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=267232007.38 spike=1.2
- CAED.CA: score=18.4 buy_ready=False sector_rank=8 price=128.11 support=71.0 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=75.25 liquidity=22572508.0 spike=0.33
- CANA.CA: score=23.4 buy_ready=False sector_rank=6 price=38.23 support=35.2 resistance=39.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.24 liquidity=12740347.0 spike=0.76
- CCAP.CA: score=21.4 buy_ready=False sector_rank=5 price=5.38 support=4.76 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.04 liquidity=619470720.0 spike=0.86
- CCRS.CA: score=21.4 buy_ready=False sector_rank=8 price=2.55 support=2.26 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=64.38 liquidity=14247147.0 spike=0.78
- CEFM.CA: score=22.96 buy_ready=False sector_rank=8 price=141.17 support=98.3 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.8 liquidity=46374184.0 spike=1.78
- CERA.CA: score=17.32 buy_ready=False sector_rank=8 price=1.3 support=1.21 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=7915719.0 spike=0.32
- CFGH.CA: score=9.78 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=52.63 liquidity=37431.45 spike=2.17
- CICH.CA: score=27.82 buy_ready=False sector_rank=12 price=12.6 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=37783712.0 spike=6.91
- CIEB.CA: score=17.68 buy_ready=False sector_rank=6 price=23.77 support=23.55 resistance=24.59 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.99 liquidity=15460055.84 spike=1.64
- CIRA.CA: score=24.42 buy_ready=False sector_rank=1 price=34.95 support=28.04 resistance=36.94 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=74.85 liquidity=56258212.38 spike=1.01
- CLHO.CA: score=20.87 buy_ready=False sector_rank=11 price=16.6 support=15.98 resistance=17.9 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=54.66 liquidity=21621683.1 spike=0.51
- CNFN.CA: score=16.59 buy_ready=False sector_rank=12 price=4.82 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=7773994.0 spike=0.37
- COMI.CA: score=21.4 buy_ready=False sector_rank=6 price=141.0 support=127.25 resistance=142.88 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=67.31 liquidity=282363498.0 spike=0.69
- COPR.CA: score=20.4 buy_ready=False sector_rank=8 price=0.41 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=21515166.0 spike=0.7
- COSG.CA: score=21.4 buy_ready=False sector_rank=8 price=1.67 support=1.5 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=20216560.0 spike=0.45
- CPCI.CA: score=21.12 buy_ready=False sector_rank=8 price=481.83 support=393.0 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=70.5 liquidity=20684390.0 spike=1.86
- CSAG.CA: score=15.98 buy_ready=False sector_rank=17 price=31.63 support=31.35 resistance=34.15 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=41.21 liquidity=19318686.22 spike=1.37
- DAPH.CA: score=8.08 buy_ready=False sector_rank=8 price=99.97 support=94.53 resistance=101.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34903900.0 spike=1.84
- DEIN.CA: score=-3.6 buy_ready=False sector_rank=8 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=9.79 buy_ready=False sector_rank=18 price=26.55 support=26.35 resistance=27.83 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=42.28 liquidity=2266626.53 spike=0.71
- DSCW.CA: score=20.18 buy_ready=False sector_rank=8 price=1.97 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=105934280.0 spike=1.89
- DTPP.CA: score=21.4 buy_ready=False sector_rank=8 price=246.32 support=183.0 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.53 liquidity=35645692.0 spike=0.45
- EALR.CA: score=27.84 buy_ready=False sector_rank=8 price=397.87 support=338.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=87205000.0 spike=3.22
- EASB.CA: score=15.27 buy_ready=False sector_rank=8 price=7.26 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.1 liquidity=5872915.5 spike=0.44
- EAST.CA: score=13.53 buy_ready=False sector_rank=18 price=36.4 support=36.01 resistance=37.88 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=44.1 liquidity=69672514.92 spike=0.87
- EBSC.CA: score=11.85 buy_ready=False sector_rank=8 price=1.9 support=1.74 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=2447851.75 spike=0.29
- ECAP.CA: score=18.45 buy_ready=False sector_rank=8 price=33.92 support=32.12 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=6727993.0 spike=1.16
- EDFM.CA: score=15.77 buy_ready=False sector_rank=8 price=391.28 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.34 liquidity=4365816.5 spike=0.84
- EEII.CA: score=9.47 buy_ready=False sector_rank=8 price=2.61 support=2.47 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.61 liquidity=5068980.5 spike=0.22
- EFIC.CA: score=16.46 buy_ready=False sector_rank=16 price=196.83 support=180.07 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.48 liquidity=10683223.0 spike=0.6
- EFID.CA: score=9.53 buy_ready=False sector_rank=18 price=27.24 support=26.64 resistance=28.99 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=34.41 liquidity=40158215.54 spike=0.88
- EFIH.CA: score=22.68 buy_ready=False sector_rank=13 price=22.65 support=20.3 resistance=24.0 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=55.13 liquidity=53100228.76 spike=0.82
- EGAL.CA: score=17.46 buy_ready=False sector_rank=16 price=296.19 support=283.03 resistance=312.25 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=54.07 liquidity=26223774.25 spike=0.63
- EGAS.CA: score=13.4 buy_ready=False sector_rank=2 price=59.45 support=52.8 resistance=62.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=131700792.0 spike=9.68
- EGBE.CA: score=8.44 buy_ready=False sector_rank=6 price=0.47 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=96.7 liquidity=35528.6 spike=0.52
- EGCH.CA: score=15.46 buy_ready=False sector_rank=16 price=12.9 support=12.24 resistance=13.8 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=47.06 liquidity=62092393.76 spike=0.99
- EGSA.CA: score=1.44 buy_ready=False sector_rank=7 price=8.81 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=27.66 liquidity=18708.99 spike=1.01
- EGTS.CA: score=10.53 buy_ready=False sector_rank=14 price=17.36 support=17.15 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.58 liquidity=15918590.0 spike=0.35
- EHDR.CA: score=21.4 buy_ready=False sector_rank=8 price=2.79 support=2.49 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=14704898.0 spike=0.35
- EKHO.CA: score=7.4 buy_ready=False sector_rank=2 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=18.29 buy_ready=False sector_rank=10 price=2.16 support=2.08 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=17757162.0 spike=0.25
- ELKA.CA: score=19.4 buy_ready=False sector_rank=8 price=1.73 support=1.35 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=73479888.0 spike=0.93
- ELNA.CA: score=9.22 buy_ready=False sector_rank=8 price=37.54 support=37.0 resistance=40.5 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.76 liquidity=1457190.22 spike=2.18
- ELSH.CA: score=19.4 buy_ready=False sector_rank=8 price=14.0 support=11.53 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.8 liquidity=90606456.0 spike=0.62
- ELWA.CA: score=2.13 buy_ready=False sector_rank=8 price=1.76 support=1.74 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.19 liquidity=729757.31 spike=0.48
- EMFD.CA: score=10.53 buy_ready=False sector_rank=14 price=11.25 support=11.08 resistance=12.22 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=26.62 liquidity=47918767.5 spike=0.82
- ENGC.CA: score=21.4 buy_ready=False sector_rank=8 price=41.27 support=36.31 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.04 liquidity=21473878.0 spike=0.82
- EOSB.CA: score=20.85 buy_ready=False sector_rank=8 price=1.55 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=446389.14 spike=7.81
- EPCO.CA: score=21.4 buy_ready=False sector_rank=8 price=10.99 support=8.57 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.67 liquidity=15186911.0 spike=0.51
- EPPK.CA: score=11.89 buy_ready=False sector_rank=8 price=14.94 support=13.52 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=61.16 liquidity=486852.53 spike=0.47
- ETEL.CA: score=22.94 buy_ready=False sector_rank=7 price=103.6 support=92.02 resistance=108.0 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=67.21 liquidity=156601550.49 spike=1.77
- ETRS.CA: score=21.4 buy_ready=False sector_rank=8 price=10.62 support=10.1 resistance=10.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.99 liquidity=32260686.0 spike=0.79
- EXPA.CA: score=20.56 buy_ready=False sector_rank=6 price=20.15 support=18.18 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.57 liquidity=36144308.0 spike=1.08
- FAIT.CA: score=14.54 buy_ready=False sector_rank=6 price=37.24 support=36.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=2860706.25 spike=1.14
- FAITA.CA: score=1.43 buy_ready=False sector_rank=6 price=0.98 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=30799.47 spike=0.73
- FERC.CA: score=15.21 buy_ready=False sector_rank=16 price=76.55 support=73.45 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=5743239.0 spike=0.48
- FWRY.CA: score=15.68 buy_ready=False sector_rank=13 price=18.77 support=18.28 resistance=19.68 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.43 liquidity=68655912.86 spike=0.54
- GBCO.CA: score=18.49 buy_ready=False sector_rank=15 price=30.27 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.99 liquidity=24215752.0 spike=0.37
- GDWA.CA: score=18.4 buy_ready=False sector_rank=8 price=0.81 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.77 liquidity=36806780.0 spike=0.35
- GGCC.CA: score=18.4 buy_ready=False sector_rank=8 price=0.87 support=0.48 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.99 liquidity=14019032.0 spike=0.37
- GIHD.CA: score=23.4 buy_ready=False sector_rank=8 price=57.63 support=41.71 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.67 liquidity=16775387.0 spike=0.32
- GMCI.CA: score=12.09 buy_ready=False sector_rank=8 price=2.06 support=1.75 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=40.68 liquidity=689152.19 spike=0.55
- GRCA.CA: score=21.1 buy_ready=False sector_rank=8 price=59.94 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.56 liquidity=9700260.0 spike=0.58
- GSSC.CA: score=25.66 buy_ready=False sector_rank=8 price=280.99 support=241.32 resistance=300.0 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=71.0 liquidity=44486616.24 spike=3.13
- GTWL.CA: score=14.4 buy_ready=False sector_rank=8 price=101.5 support=82.2 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.45 liquidity=36327448.0 spike=0.28
- HDBK.CA: score=24.4 buy_ready=False sector_rank=6 price=83.0 support=76.9 resistance=86.5 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=63.36 liquidity=303935210.0 spike=7.27
- HELI.CA: score=20.75 buy_ready=False sector_rank=14 price=8.2 support=6.41 resistance=8.6 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=73.26 liquidity=235250958.93 spike=1.11
- HRHO.CA: score=14.82 buy_ready=False sector_rank=12 price=26.2 support=25.95 resistance=27.43 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.46 liquidity=66114025.13 spike=0.77
- ICID.CA: score=20.88 buy_ready=False sector_rank=8 price=8.01 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.31 liquidity=12743275.0 spike=1.74
- IDRE.CA: score=23.4 buy_ready=False sector_rank=8 price=49.12 support=42.22 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.68 liquidity=10122458.0 spike=0.37
- IFAP.CA: score=21.93 buy_ready=False sector_rank=3 price=19.82 support=18.96 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.59 liquidity=7533056.5 spike=0.76
- INFI.CA: score=9.52 buy_ready=False sector_rank=8 price=113.21 support=108.1 resistance=114.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=45854784.0 spike=2.56
- IRON.CA: score=6.53 buy_ready=False sector_rank=16 price=30.62 support=30.14 resistance=32.9 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=2.83 liquidity=6868494.87 spike=1.1
- ISMA.CA: score=19.36 buy_ready=False sector_rank=8 price=30.92 support=26.54 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=69.1 liquidity=7957255.5 spike=0.31
- ISMQ.CA: score=18.46 buy_ready=False sector_rank=16 price=9.14 support=8.96 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=40122812.0 spike=0.43
- ISPH.CA: score=15.87 buy_ready=False sector_rank=11 price=11.37 support=11.2 resistance=11.87 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.78 liquidity=36184740.39 spike=0.74
- JUFO.CA: score=9.53 buy_ready=False sector_rank=18 price=28.67 support=28.48 resistance=31.85 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=19.95 liquidity=20601573.97 spike=0.78
- KABO.CA: score=21.4 buy_ready=False sector_rank=4 price=8.08 support=6.26 resistance=8.9 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=64.41 liquidity=21986503.95 spike=0.45
- KWIN.CA: score=18.4 buy_ready=False sector_rank=8 price=98.35 support=66.1 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.46 liquidity=37505820.0 spike=0.7
- KZPC.CA: score=21.21 buy_ready=False sector_rank=8 price=8.74 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=9973638.0 spike=1.92
- LCSW.CA: score=23.39 buy_ready=False sector_rank=9 price=34.59 support=28.38 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.64 liquidity=23889772.0 spike=0.36
- LUTS.CA: score=6.4 buy_ready=False sector_rank=8 price=0.57 support=0.55 resistance=0.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21416070.0 spike=0.68
- MAAL.CA: score=19.54 buy_ready=False sector_rank=8 price=8.85 support=7.13 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=74.47 liquidity=17675026.0 spike=1.07
- MASR.CA: score=21.4 buy_ready=False sector_rank=8 price=8.05 support=7.24 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=55124556.0 spike=0.67
- MBSC.CA: score=20.39 buy_ready=False sector_rank=9 price=244.5 support=231.51 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.96 liquidity=13446986.0 spike=0.74
- MCQE.CA: score=23.39 buy_ready=False sector_rank=9 price=184.83 support=170.0 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.32 liquidity=14013952.0 spike=0.76
- MCRO.CA: score=18.72 buy_ready=False sector_rank=8 price=1.5 support=1.2 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=159402784.0 spike=1.16
- MENA.CA: score=9.52 buy_ready=False sector_rank=14 price=7.0 support=6.74 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=38.67 liquidity=992924.69 spike=0.13
- MEPA.CA: score=23.4 buy_ready=False sector_rank=8 price=1.88 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=40850048.0 spike=0.81
- MFPC.CA: score=17.7 buy_ready=False sector_rank=16 price=36.62 support=35.19 resistance=38.8 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=47.34 liquidity=102130577.0 spike=1.12
- MFSC.CA: score=11.4 buy_ready=False sector_rank=8 price=55.77 support=46.48 resistance=55.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44535960.0 spike=7.75
- MHOT.CA: score=15.91 buy_ready=False sector_rank=19 price=16.59 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=15199266.0 spike=1.34
- MICH.CA: score=6.4 buy_ready=False sector_rank=8 price=42.16 support=40.5 resistance=42.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16385025.0 spike=0.98
- MILS.CA: score=7.28 buy_ready=False sector_rank=8 price=205.14 support=192.5 resistance=209.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72010696.0 spike=1.44
- MIPH.CA: score=3.67 buy_ready=False sector_rank=11 price=781.2 support=740.45 resistance=784.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6206774.5 spike=1.8
- MOED.CA: score=16.34 buy_ready=False sector_rank=8 price=0.68 support=0.68 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=37552056.0 spike=1.47
- MOIL.CA: score=12.55 buy_ready=False sector_rank=2 price=0.68 support=0.47 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=92.15 liquidity=148245.03 spike=0.19
- MOIN.CA: score=17.99 buy_ready=False sector_rank=8 price=24.48 support=23.03 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=51.08 liquidity=2587747.75 spike=4.88
- MOSC.CA: score=28.4 buy_ready=False sector_rank=8 price=294.91 support=260.01 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=62.23 liquidity=43427676.0 spike=3.56
- MPCI.CA: score=18.4 buy_ready=False sector_rank=8 price=293.28 support=237.12 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=84.45 liquidity=82381920.0 spike=0.84
- MPCO.CA: score=25.14 buy_ready=False sector_rank=3 price=1.94 support=1.77 resistance=2.07 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=53.66 liquidity=114460806.54 spike=1.37
- MPRC.CA: score=21.4 buy_ready=False sector_rank=8 price=45.12 support=37.51 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.11 liquidity=14880556.0 spike=0.48
- MTIE.CA: score=20.55 buy_ready=False sector_rank=15 price=9.63 support=9.09 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=25078212.0 spike=1.03
- NAHO.CA: score=5.41 buy_ready=False sector_rank=8 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9497.88 spike=0.37
- NCCW.CA: score=21.4 buy_ready=False sector_rank=8 price=7.1 support=6.01 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.49 liquidity=23333428.0 spike=0.8
- NEDA.CA: score=6.7 buy_ready=False sector_rank=8 price=2.75 support=2.7 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=302093.53 spike=0.39
- NHPS.CA: score=21.4 buy_ready=False sector_rank=8 price=83.5 support=67.0 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=21346392.0 spike=0.24
- NINH.CA: score=10.38 buy_ready=False sector_rank=8 price=24.54 support=21.65 resistance=24.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=129301336.0 spike=2.99
- NIPH.CA: score=18.39 buy_ready=False sector_rank=11 price=233.58 support=165.0 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.86 liquidity=204534448.0 spike=1.26
- OBRI.CA: score=10.4 buy_ready=False sector_rank=8 price=32.32 support=32.2 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.17 liquidity=40053196.0 spike=0.92
- OCDI.CA: score=20.53 buy_ready=False sector_rank=14 price=28.03 support=24.46 resistance=29.2 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=60.81 liquidity=83285597.1 spike=0.84
- OCPH.CA: score=7.3 buy_ready=False sector_rank=8 price=490.97 support=463.1 resistance=499.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36533896.0 spike=1.45
- ODIN.CA: score=10.12 buy_ready=False sector_rank=8 price=2.92 support=2.84 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56973284.0 spike=2.86
- OFH.CA: score=21.4 buy_ready=False sector_rank=8 price=0.72 support=0.59 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.49 liquidity=45601464.0 spike=0.67
- OIH.CA: score=23.4 buy_ready=False sector_rank=5 price=1.49 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=58099004.0 spike=0.77
- OLFI.CA: score=17.53 buy_ready=False sector_rank=18 price=22.77 support=21.91 resistance=23.95 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=47.3 liquidity=11842062.45 spike=0.34
- ORAS.CA: score=5.0 buy_ready=False sector_rank=20 price=71.05 support=71.05 resistance=71.05 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ORHD.CA: score=21.09 buy_ready=False sector_rank=14 price=39.31 support=37.76 resistance=40.9 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=51.57 liquidity=188363227.36 spike=1.28
- ORWE.CA: score=21.4 buy_ready=False sector_rank=4 price=22.98 support=22.2 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=22942086.0 spike=0.91
- PHAR.CA: score=10.87 buy_ready=False sector_rank=11 price=124.8 support=104.2 resistance=124.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=343604448.0 spike=4.09
- PHDC.CA: score=15.53 buy_ready=False sector_rank=14 price=14.5 support=14.32 resistance=15.38 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=41.03 liquidity=169269520.0 spike=0.72
- PHTV.CA: score=12.81 buy_ready=False sector_rank=8 price=325.42 support=260.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=73.12 liquidity=3411358.5 spike=0.7
- POUL.CA: score=9.53 buy_ready=False sector_rank=18 price=37.73 support=36.5 resistance=41.47 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=32.88 liquidity=16785699.5 spike=0.49
- PRCL.CA: score=6.39 buy_ready=False sector_rank=9 price=36.7 support=34.99 resistance=36.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25672998.0 spike=0.54
- PRDC.CA: score=20.53 buy_ready=False sector_rank=14 price=9.53 support=7.4 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.01 liquidity=67596368.0 spike=0.56
- PRMH.CA: score=15.95 buy_ready=False sector_rank=8 price=2.61 support=2.48 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=9546153.0 spike=0.57
- RACC.CA: score=19.4 buy_ready=False sector_rank=8 price=10.05 support=9.65 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=19011144.0 spike=0.84
- RAKT.CA: score=10.17 buy_ready=False sector_rank=8 price=22.81 support=21.25 resistance=23.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.46 liquidity=366291.66 spike=1.2
- RAYA.CA: score=13.52 buy_ready=False sector_rank=21 price=7.5 support=7.3 resistance=8.49 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=37.37 liquidity=53975797.5 spike=0.41
- RMDA.CA: score=21.75 buy_ready=False sector_rank=11 price=5.28 support=4.91 resistance=5.35 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=71.64 liquidity=43538549.09 spike=1.44
- ROTO.CA: score=7.24 buy_ready=False sector_rank=8 price=44.89 support=42.6 resistance=45.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27822582.0 spike=1.42
- RREI.CA: score=21.4 buy_ready=False sector_rank=8 price=4.62 support=3.45 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=71.0 liquidity=40548696.0 spike=0.63
- RTVC.CA: score=11.86 buy_ready=False sector_rank=8 price=3.78 support=3.7 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=5262818.0 spike=1.1
- RUBX.CA: score=19.4 buy_ready=False sector_rank=8 price=12.42 support=11.22 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.57 liquidity=21573980.0 spike=0.32
- SAUD.CA: score=23.82 buy_ready=False sector_rank=6 price=21.97 support=21.01 resistance=22.75 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=54.51 liquidity=12058607.61 spike=1.21
- SCEM.CA: score=19.67 buy_ready=False sector_rank=9 price=78.42 support=61.28 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.59 liquidity=127679032.0 spike=1.64
- SCFM.CA: score=23.4 buy_ready=False sector_rank=8 price=291.34 support=237.08 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.42 liquidity=24014132.0 spike=0.9
- SCTS.CA: score=14.54 buy_ready=False sector_rank=1 price=613.18 support=599.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.65 liquidity=2139694.0 spike=0.35
- SDTI.CA: score=7.14 buy_ready=False sector_rank=8 price=64.5 support=57.5 resistance=64.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24754418.0 spike=1.37
- SEIG.CA: score=21.4 buy_ready=False sector_rank=8 price=258.35 support=186.05 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=11030962.0 spike=0.4
- SIPC.CA: score=11.4 buy_ready=False sector_rank=8 price=4.6 support=3.99 resistance=4.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=186482224.0 spike=7.34
- SKPC.CA: score=18.38 buy_ready=False sector_rank=16 price=15.71 support=14.8 resistance=16.77 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=43.31 liquidity=74029086.35 spike=1.96
- SMFR.CA: score=21.4 buy_ready=False sector_rank=8 price=239.71 support=193.0 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=66.77 liquidity=18127824.0 spike=0.84
- SNFC.CA: score=11.82 buy_ready=False sector_rank=8 price=11.1 support=11.01 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=12.03 liquidity=13683747.0 spike=1.21
- SPIN.CA: score=21.4 buy_ready=False sector_rank=4 price=15.78 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=68.35 liquidity=18151684.0 spike=0.69
- SPMD.CA: score=21.6 buy_ready=False sector_rank=8 price=0.47 support=0.43 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=30499552.0 spike=1.1
- SUGR.CA: score=10.93 buy_ready=False sector_rank=18 price=46.98 support=46.47 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.02 liquidity=5400061.0 spike=1.0
- SVCE.CA: score=14.4 buy_ready=False sector_rank=8 price=9.22 support=8.96 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.05 liquidity=16459170.0 spike=0.3
- SWDY.CA: score=21.61 buy_ready=False sector_rank=10 price=93.0 support=86.1 resistance=97.5 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=65.15 liquidity=25110930.0 spike=1.16
- TALM.CA: score=24.52 buy_ready=False sector_rank=1 price=17.45 support=15.27 resistance=19.59 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=75.7 liquidity=82446716.6 spike=2.56
- TMGH.CA: score=18.65 buy_ready=False sector_rank=14 price=97.3 support=94.1 resistance=103.87 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.6 liquidity=387810373.56 spike=1.06
- TRTO.CA: score=10.02 buy_ready=False sector_rank=8 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=2951.44 spike=2.31
- UEFM.CA: score=15.27 buy_ready=False sector_rank=8 price=544.19 support=473.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=1866311.13 spike=0.36
- UEGC.CA: score=6.4 buy_ready=False sector_rank=8 price=2.45 support=2.3 resistance=2.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39155404.0 spike=0.72
- UNIP.CA: score=23.4 buy_ready=False sector_rank=8 price=0.39 support=0.32 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=10208793.0 spike=0.37
- UNIT.CA: score=15.53 buy_ready=False sector_rank=14 price=18.27 support=12.8 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=21.87 liquidity=12144528.0 spike=0.41
- WCDF.CA: score=15.93 buy_ready=False sector_rank=8 price=585.67 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=4049852.75 spike=1.24
- WKOL.CA: score=30.4 buy_ready=False sector_rank=8 price=344.57 support=280.05 resistance=363.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.81 liquidity=73996776.0 spike=4.26
- ZEOT.CA: score=21.4 buy_ready=False sector_rank=8 price=12.37 support=10.81 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=22230530.0 spike=0.72
- ZMID.CA: score=18.53 buy_ready=False sector_rank=14 price=7.14 support=6.47 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.92 liquidity=237766528.0 spike=0.89

## Backtesting Lite
- WKOL.CA: 180d return=18.4%, max drawdown=-28.19%, MA20>MA50 days last20=8, as_of=2026-07-29T21:00:00+00:00
- MOSC.CA: 180d return=50.34%, max drawdown=-24.01%, MA20>MA50 days last20=3, as_of=2026-07-29T21:00:00+00:00
- EALR.CA: 180d return=20.65%, max drawdown=-26.75%, MA20>MA50 days last20=5, as_of=2026-07-29T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- WKOL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Wadi Kom Ombo For Land Reclamation Co. summary=Wadi Kom Ombo amends estimated budget for FY26/27; Wadi Kom Ombo eyes EGP 257.77m in FY26/27 net profits; Wadi Kom Ombo records lower net profits at nearly EGP 2m in Q1-25/26
  - Wadi Kom Ombo amends estimated budget for FY26/27: https://english.mubasher.info/news/4600336/Wadi-Kom-Ombo-amends-estimated-budget-for-FY26-27/
  - Wadi Kom Ombo eyes EGP 257.77m in FY26/27 net profits: https://english.mubasher.info/news/4585452/Wadi-Kom-Ombo-eyes-EGP-257-77m-in-FY26-27-net-profits/
  - Wadi Kom Ombo records lower net profits at nearly EGP 2m in Q1-25/26: https://english.mubasher.info/news/4531526/Wadi-Kom-Ombo-records-lower-net-profits-at-nearly-EGP-2m-in-Q1-25-26/
- MOSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Oils & Soap summary=Misr Oils and Soap not to pay dividends for FY20/21; Misr Oils and Soap&#39;s profit plunges 78% in FY20/21; Misr Oils and Soap swings to loss in 10 months
  - Misr Oils and Soap not to pay dividends for FY20/21: https://english.mubasher.info/news/3856493/Misr-Oils-and-Soap-not-to-pay-dividends-for-FY20-21/
  - Misr Oils and Soap&#39;s profit plunges 78% in FY20/21: https://english.mubasher.info/news/3851183/Misr-Oils-and-Soap-s-profit-plunges-78-in-FY20-21/
  - Misr Oils and Soap swings to loss in 10 months: https://english.mubasher.info/news/3811105/Misr-Oils-and-Soap-swings-to-loss-in-10-months/
- EALR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Company For Land Reclamation summary=El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23; El Arabia for Land Reclamation starts work on Bahariya Oasis project; El Arabia for Land Reclamation H1 losses down 16%
  - El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23: https://english.mubasher.info/news/3938373/El-Arabia-for-Land-Reclamation-targets-EGP-2-5m-profits-in-FY22-23/
  - El Arabia for Land Reclamation starts work on Bahariya Oasis project: https://english.mubasher.info/news/3493569/El-Arabia-for-Land-Reclamation-starts-work-on-Bahariya-Oasis-project/
  - El Arabia for Land Reclamation H1 losses down 16%: https://english.mubasher.info/news/3058199/El-Arabia-for-Land-Reclamation-H1-losses-down-16-/
- CICH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=CI Capital Holding summary=Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- GSSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=General Co. For Silos & Storage summary=General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials; General Company for Silos to set up new firm with EGP 500m capital; General Company for Silos’ EGM nods to EGP 25m capital hike
  - General Company for Silos generates nearly EGP 62m net profits in Q1-25/26 audited financials: https://english.mubasher.info/news/4529067/General-Company-for-Silos-generates-nearly-EGP-62m-net-profits-in-Q1-25-26-audited-financials/
  - General Company for Silos to set up new firm with EGP 500m capital: https://english.mubasher.info/news/4043715/General-Company-for-Silos-to-set-up-new-firm-with-EGP-500m-capital/
  - General Company for Silos’ EGM nods to EGP 25m capital hike: https://english.mubasher.info/news/4018676/General-Company-for-Silos-EGM-nods-to-EGP-25m-capital-hike/

## Warnings
- Evidence for WKOL.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MOSC.CA matches the company but no source/report date was detected.
- Evidence for EALR.CA matches the company but no source/report date was detected.
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Evidence for GSSC.CA matches the company but no source/report date was detected.
