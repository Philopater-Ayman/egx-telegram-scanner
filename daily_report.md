# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-06-28T14:23:43.418088+00:00
Generated Cairo: 2026-06-28 17:23
Run timing: target 15:30 Cairo | generated Cairo 2026-06-28 17:23 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-06-28 17:20

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 172/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 28
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 25.0%
- EGX70 regime: BEARISH / above MA20 29.73% / above MA50 62.16%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ORAS.CA: liquidity=385481760.0 spike=1.0 score=4.6
- CCAP.CA: liquidity=344487808.0 spike=0.5 score=9.57
- PHDC.CA: liquidity=270934208.0 spike=0.66 score=18.64
- COMI.CA: liquidity=251973872.0 spike=0.43 score=14.78
- OCDI.CA: liquidity=238286432.0 spike=3.71 score=24.64

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: Scanner highlighted a few stocks with accumulation spikes and bullish‑watch outlooks, but the overall EGX30/EGX70 bearish trend, weak sector breadth, and defensive risk mode keep new buys disallowed.
- EGX30 and EGX70 are both bearish with low MA20/MA50 breadth, reinforcing a defensive stance.
- Top tickets show liquidity accumulation spikes and sit near support/resistance, giving short‑term bullish watch signals despite limited conviction.
- Sector breadth is only 14% and leading sectors are narrow, adding uncertainty to any upside.
- Risk mode is DEFENSIVE_NO_NEW_BUY; any potential upside remains tentative and could reverse if market weakness persists.

## Top Liquidity Spikes
- RUBX.CA: spike=14.57 liquidity=134018512.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- LCSW.CA: spike=8.64 liquidity=167336848.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CSAG.CA: spike=7.67 liquidity=91871208.0 outlook=BULLISH_WATCH score=100 buy_ready=False
- GGCC.CA: spike=5.07 liquidity=44713252.0 outlook=BULLISH_WATCH score=81.34 buy_ready=False
- GTWL.CA: spike=4.13 liquidity=64792684.0 outlook=CONSTRUCTIVE score=66.34 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=9.08 5d=4.46% 20d=8.94% aboveMA50=100.0%
- #2 Transportation & Logistics: score=9.06 5d=-0.42% 20d=-1.81% aboveMA50=50.0%
- #3 Technology & Distribution: score=6.13 5d=5.56% 20d=-1.07% aboveMA50=100.0%
- #4 Textiles: score=4.14 5d=-0.53% 20d=-1.79% aboveMA50=75.0%
- #5 Real Estate: score=4.09 5d=-0.15% 20d=2.51% aboveMA50=69.23%
- #6 Non-bank Financial Services: score=3.75 5d=1.74% 20d=1.56% aboveMA50=40.0%
- #7 Education: score=3.38 5d=0.0% 20d=2.38% aboveMA50=33.33%
- #8 Energy & Petrochemicals: score=2.84 5d=-1.59% 20d=0.86% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CSAG.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- SPIN.CA: BULLISH_WATCH score=91.14 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CIRA.CA: BULLISH_WATCH score=84.38 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ECAP.CA: BULLISH_WATCH score=82.34 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- GGCC.CA: BULLISH_WATCH score=81.34 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CNFN.CA: BULLISH_WATCH score=79.75 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ORHD.CA: BULLISH_WATCH score=79.09 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- CICH.CA: BULLISH_WATCH score=78.75 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20
- ENGC.CA: BULLISH_WATCH score=78.34 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EPPK.CA: BULLISH_WATCH score=78.34 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; close to resistance; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=10.06 buy_ready=False sector_rank=12 price=197.13 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=5127856.0 spike=0.89
- ABUK.CA: score=8.38 buy_ready=False sector_rank=21 price=67.78 support=68.01 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.55 liquidity=68992472.0 spike=0.52
- ACAMD.CA: score=17.94 buy_ready=False sector_rank=12 price=2.2 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=60063976.0 spike=0.48
- ACGC.CA: score=18.66 buy_ready=False sector_rank=4 price=9.19 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.16 liquidity=12240127.0 spike=0.23
- ADCI.CA: score=13.58 buy_ready=False sector_rank=12 price=238.57 support=211.0 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=85.03 liquidity=6647678.0 spike=0.74
- ADIB.CA: score=14.78 buy_ready=False sector_rank=14 price=44.48 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=35141832.0 spike=0.35
- ADPC.CA: score=13.94 buy_ready=False sector_rank=12 price=3.4 support=3.43 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=10757808.0 spike=0.46
- AFDI.CA: score=16.64 buy_ready=False sector_rank=12 price=42.66 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.15 liquidity=6702208.5 spike=0.44
- AFMC.CA: score=1.18 buy_ready=False sector_rank=12 price=67.34 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.54 liquidity=1246892.63 spike=0.41
- AJWA.CA: score=12.9 buy_ready=False sector_rank=12 price=178.05 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=82.78 liquidity=5964799.5 spike=0.22
- ALCN.CA: score=13.64 buy_ready=False sector_rank=2 price=27.76 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.15 liquidity=13678663.0 spike=1.12
- ALUM.CA: score=6.05 buy_ready=False sector_rank=12 price=20.71 support=21.5 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.63 liquidity=6109469.0 spike=0.61
- AMER.CA: score=10.64 buy_ready=False sector_rank=5 price=2.3 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=19488076.0 spike=0.25
- AMES.CA: score=0.87 buy_ready=False sector_rank=12 price=46.07 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.52 liquidity=1935090.0 spike=0.61
- AMIA.CA: score=16.01 buy_ready=False sector_rank=12 price=8.69 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=8077353.0 spike=0.58
- AMOC.CA: score=10.14 buy_ready=False sector_rank=8 price=7.43 support=7.53 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.9 liquidity=25723116.0 spike=0.51
- ANFI.CA: score=15.27 buy_ready=False sector_rank=12 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=-0.54 buy_ready=False sector_rank=12 price=8.42 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=13.11 liquidity=526796.69 spike=0.66
- ARAB.CA: score=15.64 buy_ready=False sector_rank=5 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=80536240.0 spike=0.95
- ARCC.CA: score=9.78 buy_ready=False sector_rank=15 price=54.31 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.64 liquidity=20308316.0 spike=0.59
- AREH.CA: score=21.94 buy_ready=False sector_rank=12 price=1.53 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=18969230.0 spike=0.56
- ARVA.CA: score=19.94 buy_ready=False sector_rank=12 price=11.06 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=12762319.0 spike=0.4
- ASCM.CA: score=4.94 buy_ready=False sector_rank=12 price=56.55 support=56.29 resistance=61.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=49098748.0 spike=0.54
- ASPI.CA: score=8.94 buy_ready=False sector_rank=12 price=0.3 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.53 liquidity=20128972.0 spike=0.28
- ATLC.CA: score=13.94 buy_ready=False sector_rank=6 price=5.0 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=3443600.75 spike=0.55
- ATQA.CA: score=13.46 buy_ready=False sector_rank=21 price=9.42 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.18 liquidity=49204060.0 spike=1.54
- AXPH.CA: score=8.75 buy_ready=False sector_rank=12 price=1084.76 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.71 liquidity=814642.13 spike=0.55
- BINV.CA: score=12.44 buy_ready=False sector_rank=17 price=46.01 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=4876017.5 spike=0.48
- BIOC.CA: score=0.83 buy_ready=False sector_rank=12 price=67.38 support=66.75 resistance=72.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4272310.0 spike=1.81
- BTFH.CA: score=14.5 buy_ready=False sector_rank=6 price=2.98 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=124079520.0 spike=0.63
- CAED.CA: score=6.82 buy_ready=False sector_rank=12 price=69.02 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=1881167.5 spike=0.36
- CANA.CA: score=11.94 buy_ready=False sector_rank=14 price=34.9 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.16 liquidity=8155951.0 spike=0.77
- CCAP.CA: score=9.57 buy_ready=False sector_rank=17 price=4.74 support=4.85 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.46 liquidity=344487808.0 spike=0.5
- CCRS.CA: score=9.74 buy_ready=False sector_rank=12 price=2.29 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=6802628.5 spike=0.38
- CEFM.CA: score=1.05 buy_ready=False sector_rank=12 price=98.87 support=100.0 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=23.51 liquidity=1116111.0 spike=0.54
- CERA.CA: score=18.94 buy_ready=False sector_rank=12 price=1.21 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=11670424.0 spike=0.7
- CFGH.CA: score=0.33 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=11255.21 spike=1.69
- CICH.CA: score=15.0 buy_ready=False sector_rank=6 price=11.91 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.48 liquidity=5741792.5 spike=1.88
- CIEB.CA: score=13.81 buy_ready=False sector_rank=14 price=23.49 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.19 liquidity=6908774.5 spike=1.06
- CIRA.CA: score=22.49 buy_ready=False sector_rank=7 price=27.64 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.81 liquidity=18768866.0 spike=1.07
- CLHO.CA: score=21.92 buy_ready=False sector_rank=13 price=16.1 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.34 liquidity=14987397.0 spike=0.42
- CNFN.CA: score=22.5 buy_ready=False sector_rank=6 price=4.66 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.4 liquidity=23938588.0 spike=0.59
- COMI.CA: score=14.78 buy_ready=False sector_rank=14 price=130.25 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.27 liquidity=251973872.0 spike=0.43
- COPR.CA: score=16.94 buy_ready=False sector_rank=12 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=11329465.0 spike=0.33
- COSG.CA: score=9.94 buy_ready=False sector_rank=12 price=1.48 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=15085054.0 spike=0.27
- CPCI.CA: score=13.14 buy_ready=False sector_rank=12 price=370.07 support=347.11 resistance=378.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=72.05 liquidity=1207001.0 spike=0.61
- CSAG.CA: score=28.4 buy_ready=False sector_rank=2 price=32.07 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=91871208.0 spike=7.67
- DAPH.CA: score=17.6 buy_ready=False sector_rank=12 price=78.86 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=9668549.0 spike=0.93
- DEIN.CA: score=5.94 buy_ready=False sector_rank=12 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=13.05 buy_ready=False sector_rank=9 price=26.59 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=73.9 liquidity=2918066.5 spike=0.77
- DSCW.CA: score=13.94 buy_ready=False sector_rank=12 price=1.71 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=28776260.0 spike=0.62
- DTPP.CA: score=0.71 buy_ready=False sector_rank=12 price=115.32 support=114.0 resistance=130.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.44 liquidity=770567.5 spike=0.5
- EALR.CA: score=7.56 buy_ready=False sector_rank=12 price=337.89 support=350.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.67 liquidity=2625380.5 spike=0.81
- EASB.CA: score=6.36 buy_ready=False sector_rank=12 price=7.51 support=7.5 resistance=8.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18673248.0 spike=1.71
- EAST.CA: score=14.13 buy_ready=False sector_rank=9 price=38.09 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.42 liquidity=15803318.0 spike=0.36
- EBSC.CA: score=5.52 buy_ready=False sector_rank=12 price=1.76 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=580987.69 spike=0.22
- ECAP.CA: score=21.34 buy_ready=False sector_rank=12 price=32.19 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=69.97 liquidity=14022508.0 spike=1.7
- EDFM.CA: score=0.32 buy_ready=False sector_rank=12 price=330.59 support=322.11 resistance=355.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=26.96 liquidity=384806.76 spike=0.73
- EEII.CA: score=12.44 buy_ready=False sector_rank=12 price=2.36 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=7507971.0 spike=0.54
- EFIC.CA: score=-1.14 buy_ready=False sector_rank=21 price=192.55 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=15.79 liquidity=1484093.75 spike=0.78
- EFID.CA: score=10.13 buy_ready=False sector_rank=9 price=25.83 support=26.67 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=59168288.0 spike=0.82
- EFIH.CA: score=13.49 buy_ready=False sector_rank=20 price=20.34 support=20.09 resistance=22.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=20061930.0 spike=0.43
- EGAL.CA: score=8.38 buy_ready=False sector_rank=21 price=277.57 support=280.0 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.2 liquidity=30176320.0 spike=0.4
- EGAS.CA: score=17.06 buy_ready=False sector_rank=8 price=50.0 support=48.2 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=8923935.0 spike=0.9
- EGBE.CA: score=12.07 buy_ready=False sector_rank=14 price=0.45 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=182962.7 spike=2.05
- EGCH.CA: score=8.38 buy_ready=False sector_rank=21 price=12.24 support=12.69 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.76 liquidity=22588884.0 spike=0.4
- EGSA.CA: score=4.98 buy_ready=False sector_rank=10 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=31.03 liquidity=17500.0 spike=1.95
- EGTS.CA: score=5.64 buy_ready=False sector_rank=5 price=16.18 support=16.11 resistance=17.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40860176.0 spike=0.42
- EHDR.CA: score=4.94 buy_ready=False sector_rank=12 price=2.42 support=2.41 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27041042.0 spike=0.47
- EKHO.CA: score=10.14 buy_ready=False sector_rank=8 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.79 buy_ready=False sector_rank=18 price=2.09 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=9502625.0 spike=0.47
- ELKA.CA: score=16.94 buy_ready=False sector_rank=12 price=1.21 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=12505865.0 spike=0.31
- ELNA.CA: score=-0.64 buy_ready=False sector_rank=12 price=36.03 support=36.0 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.65 liquidity=427548.56 spike=0.97
- ELSH.CA: score=17.94 buy_ready=False sector_rank=12 price=11.14 support=8.28 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=31729144.0 spike=0.17
- ELWA.CA: score=8.68 buy_ready=False sector_rank=12 price=2.01 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=50.98 liquidity=744317.75 spike=0.23
- EMFD.CA: score=18.64 buy_ready=False sector_rank=5 price=11.27 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.95 liquidity=55824680.0 spike=0.2
- ENGC.CA: score=25.32 buy_ready=False sector_rank=12 price=37.13 support=32.81 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.63 liquidity=34814320.0 spike=2.69
- EOSB.CA: score=11.99 buy_ready=False sector_rank=12 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=50716.64 spike=0.39
- EPCO.CA: score=7.29 buy_ready=False sector_rank=12 price=8.71 support=8.89 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=2349235.25 spike=0.26
- EPPK.CA: score=19.59 buy_ready=False sector_rank=12 price=13.04 support=11.67 resistance=13.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=67.48 liquidity=3154323.5 spike=3.25
- ETEL.CA: score=17.06 buy_ready=False sector_rank=10 price=90.79 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.73 liquidity=42276544.0 spike=0.56
- ETRS.CA: score=6.44 buy_ready=False sector_rank=12 price=10.61 support=10.56 resistance=11.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=119917144.0 spike=1.75
- EXPA.CA: score=9.78 buy_ready=False sector_rank=14 price=18.06 support=18.2 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.55 liquidity=21839082.0 spike=0.67
- FAIT.CA: score=6.9 buy_ready=False sector_rank=14 price=35.1 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.43 liquidity=2118896.25 spike=0.67
- FAITA.CA: score=7.93 buy_ready=False sector_rank=14 price=0.98 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=89982.38 spike=2.53
- FERC.CA: score=2.4 buy_ready=False sector_rank=21 price=74.03 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.06 liquidity=3020295.5 spike=0.8
- FWRY.CA: score=15.49 buy_ready=False sector_rank=20 price=18.42 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=94242136.0 spike=0.36
- GBCO.CA: score=23.4 buy_ready=False sector_rank=1 price=31.0 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=94.21 liquidity=61123688.0 spike=0.67
- GDWA.CA: score=8.0 buy_ready=False sector_rank=12 price=0.76 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=9059430.0 spike=0.65
- GGCC.CA: score=27.94 buy_ready=False sector_rank=12 price=0.46 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=44713252.0 spike=5.07
- GIHD.CA: score=16.34 buy_ready=False sector_rank=12 price=41.47 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.27 liquidity=6408690.0 spike=0.82
- GMCI.CA: score=13.69 buy_ready=False sector_rank=12 price=1.77 support=1.66 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=938192.56 spike=2.41
- GRCA.CA: score=7.21 buy_ready=False sector_rank=12 price=52.35 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.48 liquidity=2276777.75 spike=0.49
- GSSC.CA: score=8.67 buy_ready=False sector_rank=12 price=242.0 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=4158466.25 spike=1.29
- GTWL.CA: score=23.94 buy_ready=False sector_rank=12 price=61.25 support=45.47 resistance=68.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=86.73 liquidity=64792684.0 spike=4.13
- HDBK.CA: score=17.36 buy_ready=False sector_rank=14 price=154.99 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.29 liquidity=33696888.0 spike=1.29
- HELI.CA: score=18.64 buy_ready=False sector_rank=5 price=6.4 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=52582840.0 spike=0.4
- HRHO.CA: score=16.5 buy_ready=False sector_rank=6 price=26.34 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=90883400.0 spike=0.63
- ICID.CA: score=18.94 buy_ready=False sector_rank=12 price=7.77 support=5.0 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=80.91 liquidity=10000981.0 spike=0.61
- IDRE.CA: score=14.49 buy_ready=False sector_rank=12 price=42.1 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=6558287.0 spike=0.41
- IFAP.CA: score=11.79 buy_ready=False sector_rank=11 price=19.08 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=7472686.0 spike=1.14
- INFI.CA: score=3.51 buy_ready=False sector_rank=12 price=89.21 support=92.5 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.57 liquidity=4573064.0 spike=0.58
- IRON.CA: score=7.78 buy_ready=False sector_rank=21 price=30.78 support=30.95 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.08 liquidity=5395821.0 spike=0.73
- ISMA.CA: score=19.94 buy_ready=False sector_rank=12 price=29.29 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=20289264.0 spike=0.54
- ISMQ.CA: score=5.98 buy_ready=False sector_rank=21 price=9.13 support=8.6 resistance=9.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=225875360.0 spike=2.3
- ISPH.CA: score=4.92 buy_ready=False sector_rank=13 price=11.33 support=11.2 resistance=12.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106014608.0 spike=0.93
- JUFO.CA: score=18.13 buy_ready=False sector_rank=9 price=29.72 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.37 liquidity=14364879.0 spike=0.41
- KABO.CA: score=19.86 buy_ready=False sector_rank=4 price=6.18 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.16 liquidity=27527550.0 spike=1.6
- KWIN.CA: score=16.56 buy_ready=False sector_rank=12 price=68.67 support=65.75 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=22216554.0 spike=2.31
- KZPC.CA: score=1.17 buy_ready=False sector_rank=12 price=8.38 support=8.6 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=14.44 liquidity=2229112.75 spike=0.34
- LCSW.CA: score=9.78 buy_ready=False sector_rank=15 price=27.37 support=27.15 resistance=31.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=167336848.0 spike=8.64
- LUTS.CA: score=21.94 buy_ready=False sector_rank=12 price=0.69 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=24604400.0 spike=0.57
- MAAL.CA: score=21.24 buy_ready=False sector_rank=12 price=7.03 support=5.16 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=78.24 liquidity=35242368.0 spike=2.15
- MASR.CA: score=17.94 buy_ready=False sector_rank=12 price=6.74 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=30280314.0 spike=0.56
- MBSC.CA: score=4.78 buy_ready=False sector_rank=15 price=228.58 support=228.11 resistance=242.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30450006.0 spike=0.83
- MCQE.CA: score=9.69 buy_ready=False sector_rank=15 price=167.8 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=17.86 liquidity=9909912.0 spike=0.62
- MCRO.CA: score=8.94 buy_ready=False sector_rank=12 price=1.19 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=20221056.0 spike=0.54
- MENA.CA: score=10.59 buy_ready=False sector_rank=5 price=6.6 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.28 liquidity=1954719.25 spike=0.14
- MEPA.CA: score=7.42 buy_ready=False sector_rank=12 price=1.53 support=1.58 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=8486374.0 spike=0.7
- MFPC.CA: score=8.38 buy_ready=False sector_rank=21 price=34.3 support=35.15 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=8.54 liquidity=75249280.0 spike=0.88
- MFSC.CA: score=20.39 buy_ready=False sector_rank=12 price=48.73 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.14 liquidity=8454644.0 spike=0.93
- MHOT.CA: score=-0.86 buy_ready=False sector_rank=19 price=33.1 support=32.75 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5028930.0 spike=0.19
- MICH.CA: score=14.43 buy_ready=False sector_rank=12 price=35.92 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=7491867.5 spike=0.5
- MILS.CA: score=7.38 buy_ready=False sector_rank=12 price=128.58 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=2440641.0 spike=0.21
- MIPH.CA: score=6.23 buy_ready=False sector_rank=13 price=643.5 support=640.0 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.16 liquidity=1313115.13 spike=0.61
- MOED.CA: score=10.24 buy_ready=False sector_rank=12 price=0.65 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=4304578.5 spike=0.42
- MOIL.CA: score=11.07 buy_ready=False sector_rank=8 price=0.47 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=409217.0 spike=2.26
- MOIN.CA: score=-0.53 buy_ready=False sector_rank=12 price=23.03 support=22.61 resistance=25.66 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=0.97 liquidity=535194.19 spike=0.85
- MOSC.CA: score=8.48 buy_ready=False sector_rank=12 price=250.32 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=3543263.75 spike=0.42
- MPCI.CA: score=4.94 buy_ready=False sector_rank=12 price=223.63 support=222.55 resistance=237.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65040612.0 spike=0.68
- MPCO.CA: score=17.04 buy_ready=False sector_rank=11 price=1.76 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=29170374.0 spike=0.28
- MPRC.CA: score=21.96 buy_ready=False sector_rank=12 price=38.39 support=31.1 resistance=38.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.37 liquidity=95713328.0 spike=2.51
- MTIE.CA: score=22.4 buy_ready=False sector_rank=1 price=8.91 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=10788724.0 spike=0.68
- NAHO.CA: score=5.95 buy_ready=False sector_rank=12 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=9517.62 spike=0.28
- NCCW.CA: score=17.94 buy_ready=False sector_rank=12 price=5.97 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=14214305.0 spike=0.44
- NEDA.CA: score=0.05 buy_ready=False sector_rank=12 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=28.57 liquidity=117806.3 spike=0.32
- NHPS.CA: score=5.88 buy_ready=False sector_rank=12 price=62.64 support=61.62 resistance=68.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=1946836.5 spike=0.49
- NINH.CA: score=18.11 buy_ready=False sector_rank=12 price=17.76 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=8873726.0 spike=2.15
- NIPH.CA: score=12.92 buy_ready=False sector_rank=13 price=157.24 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=34599012.0 spike=0.49
- OBRI.CA: score=3.45 buy_ready=False sector_rank=12 price=31.67 support=31.5 resistance=34.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8517307.0 spike=0.63
- OCDI.CA: score=24.64 buy_ready=False sector_rank=5 price=24.32 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.51 liquidity=238286432.0 spike=3.71
- OCPH.CA: score=7.55 buy_ready=False sector_rank=12 price=342.96 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=2613868.0 spike=0.43
- ODIN.CA: score=13.75 buy_ready=False sector_rank=12 price=2.07 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=5813674.0 spike=0.53
- OFH.CA: score=6.47 buy_ready=False sector_rank=12 price=0.58 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=7532544.0 spike=0.38
- OIH.CA: score=16.57 buy_ready=False sector_rank=17 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=28226116.0 spike=0.34
- OLFI.CA: score=15.13 buy_ready=False sector_rank=9 price=21.29 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=10374293.0 spike=0.52
- ORAS.CA: score=4.6 buy_ready=False sector_rank=16 price=696.08 support=680.0 resistance=732.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=385481760.0 spike=1.0
- ORHD.CA: score=21.3 buy_ready=False sector_rank=5 price=38.29 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.63 liquidity=233770112.0 spike=1.33
- ORWE.CA: score=10.66 buy_ready=False sector_rank=4 price=22.18 support=22.61 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=25148524.0 spike=0.68
- PHAR.CA: score=12.34 buy_ready=False sector_rank=13 price=85.22 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.17 liquidity=5428153.0 spike=0.16
- PHDC.CA: score=18.64 buy_ready=False sector_rank=5 price=14.6 support=14.43 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.93 liquidity=270934208.0 spike=0.66
- PHTV.CA: score=16.94 buy_ready=False sector_rank=12 price=257.48 support=201.55 resistance=256.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=85.23 liquidity=10946975.0 spike=0.54
- POUL.CA: score=22.13 buy_ready=False sector_rank=9 price=37.53 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.39 liquidity=23225302.0 spike=0.62
- PRCL.CA: score=19.78 buy_ready=False sector_rank=15 price=30.49 support=22.02 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.99 liquidity=30351596.0 spike=0.77
- PRDC.CA: score=20.64 buy_ready=False sector_rank=5 price=7.07 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.47 liquidity=49020708.0 spike=0.43
- PRMH.CA: score=4.94 buy_ready=False sector_rank=12 price=2.41 support=2.34 resistance=2.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17488126.0 spike=0.58
- RACC.CA: score=11.54 buy_ready=False sector_rank=12 price=9.57 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=6607713.0 spike=0.69
- RAKT.CA: score=6.73 buy_ready=False sector_rank=12 price=22.43 support=22.0 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=37.86 liquidity=372454.69 spike=1.21
- RAYA.CA: score=20.4 buy_ready=False sector_rank=3 price=7.12 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.38 liquidity=66105372.0 spike=0.75
- RMDA.CA: score=14.92 buy_ready=False sector_rank=13 price=4.85 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=22423380.0 spike=0.28
- ROTO.CA: score=4.94 buy_ready=False sector_rank=12 price=38.93 support=38.71 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14154411.0 spike=0.51
- RREI.CA: score=10.12 buy_ready=False sector_rank=12 price=3.35 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=5180242.0 spike=0.27
- RTVC.CA: score=5.48 buy_ready=False sector_rank=12 price=3.64 support=3.63 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=1543551.0 spike=0.3
- RUBX.CA: score=9.94 buy_ready=False sector_rank=12 price=11.62 support=10.55 resistance=12.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=134018512.0 spike=14.57
- SAUD.CA: score=7.62 buy_ready=False sector_rank=14 price=20.05 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.28 liquidity=7838750.5 spike=0.88
- SCEM.CA: score=12.93 buy_ready=False sector_rank=15 price=61.33 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.29 liquidity=8141007.5 spike=0.43
- SCFM.CA: score=1.98 buy_ready=False sector_rank=12 price=231.35 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=20.9 liquidity=2045407.5 spike=0.34
- SCTS.CA: score=-2.54 buy_ready=False sector_rank=7 price=542.89 support=540.0 resistance=578.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2105810.25 spike=0.6
- SDTI.CA: score=13.25 buy_ready=False sector_rank=12 price=45.87 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.39 liquidity=5318220.0 spike=0.44
- SEIG.CA: score=9.19 buy_ready=False sector_rank=12 price=183.39 support=179.43 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.41 liquidity=1258817.75 spike=0.31
- SIPC.CA: score=8.93 buy_ready=False sector_rank=12 price=3.35 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.09 liquidity=8995283.0 spike=0.78
- SKPC.CA: score=7.38 buy_ready=False sector_rank=21 price=15.67 support=15.9 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.8 liquidity=22871772.0 spike=0.61
- SMFR.CA: score=-0.07 buy_ready=False sector_rank=12 price=189.77 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.3 liquidity=997327.13 spike=0.43
- SNFC.CA: score=11.43 buy_ready=False sector_rank=12 price=12.05 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=5498303.0 spike=0.28
- SPIN.CA: score=25.66 buy_ready=False sector_rank=4 price=14.3 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=20316718.0 spike=3.58
- SPMD.CA: score=16.85 buy_ready=False sector_rank=12 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.01 liquidity=8913001.0 spike=0.37
- SUGR.CA: score=5.36 buy_ready=False sector_rank=9 price=46.3 support=47.03 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=6229526.0 spike=0.76
- SVCE.CA: score=19.94 buy_ready=False sector_rank=12 price=8.86 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=28805918.0 spike=0.4
- SWDY.CA: score=14.28 buy_ready=False sector_rank=18 price=85.54 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.21 liquidity=14937094.0 spike=0.86
- TALM.CA: score=8.58 buy_ready=False sector_rank=7 price=15.65 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=3231722.75 spike=0.4
- TMGH.CA: score=15.64 buy_ready=False sector_rank=5 price=93.99 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.96 liquidity=216568960.0 spike=0.49
- TRTO.CA: score=5.94 buy_ready=False sector_rank=12 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=491.27 spike=0.67
- UEFM.CA: score=6.83 buy_ready=False sector_rank=12 price=467.56 support=465.01 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=62.58 liquidity=890665.75 spike=0.91
- UEGC.CA: score=9.94 buy_ready=False sector_rank=12 price=1.35 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=11956653.0 spike=0.51
- UNIP.CA: score=12.94 buy_ready=False sector_rank=12 price=0.3 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=7999531.0 spike=0.35
- UNIT.CA: score=4.37 buy_ready=False sector_rank=5 price=12.66 support=12.91 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=33.47 liquidity=730338.0 spike=0.11
- WCDF.CA: score=5.38 buy_ready=False sector_rank=12 price=514.97 support=450.0 resistance=547.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=43.92 liquidity=344452.72 spike=1.05
- WKOL.CA: score=0.2 buy_ready=False sector_rank=12 price=274.56 support=284.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=1259175.38 spike=0.43
- ZEOT.CA: score=20.0 buy_ready=False sector_rank=12 price=10.4 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.52 liquidity=26001134.0 spike=1.03
- ZMID.CA: score=22.64 buy_ready=False sector_rank=5 price=6.29 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=187730432.0 spike=0.91

## Backtesting Lite
- CSAG.CA: 180d return=18.29%, max drawdown=-28.0%, MA20>MA50 days last20=20, as_of=2026-06-24T21:00:00+00:00
- GGCC.CA: 180d return=-16.12%, max drawdown=-45.58%, MA20>MA50 days last20=19, as_of=2026-06-24T21:00:00+00:00
- SPIN.CA: 180d return=39.07%, max drawdown=-9.64%, MA20>MA50 days last20=0, as_of=2026-06-24T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- SPIN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Spinning and Weaving summary=Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- ENGC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Industrial Engineering Company for Construction and Development (ICON) (S.A.E) summary=Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- GTWL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Golden Textiles & Clothes Wool summary=Golden Textiles profits jump 214%; Golden Textiles OGM OKs 50 piasters/shr dividends; Golden Textiles consolidated profits down 18.5% in FY16
  - Golden Textiles profits jump 214%: https://english.mubasher.info/news/3108548/Golden-Textiles-profits-jump-214-/
  - Golden Textiles OGM OKs 50 piasters/shr dividends: https://english.mubasher.info/news/3103061/Golden-Textiles-OGM-OKs-50-piasters-shr-dividends/
  - Golden Textiles consolidated profits down 18.5% in FY16: https://english.mubasher.info/news/3092552/Golden-Textiles-consolidated-profits-down-18-5-in-FY16/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=543 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/

## Warnings
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
