# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-15T07:36:39.563981+00:00
Generated Cairo: 2026-07-15 10:36
Run timing: target 08:45 Cairo | generated Cairo 2026-07-15 10:36 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-15 10:31

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 61
- Data quality issues: 1
- Tradeable price/liquidity tickers: 174/189
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 15
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 63.16% / above MA50 47.37%
- EGX70 regime: BULLISH / above MA20 76.92% / above MA50 74.36%
- Sector breadth: 47.62%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- EMFD.CA: liquidity=77429007.54 spike=0.75 score=22.4
- CCRS.CA: liquidity=52328152.11 spike=4.37 score=33.4
- MCRO.CA: liquidity=46927992.0 spike=1.11 score=25.62
- NIPH.CA: liquidity=44621264.0 spike=0.52 score=7.59
- TMGH.CA: liquidity=43821136.0 spike=0.12 score=26.4

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- SMFR.CA: spike=9.28 liquidity=19092908.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GRCA.CA: spike=4.4 liquidity=13255225.6 outlook=WEAK_OR_RISKY score=32.31 buy_ready=False
- CCRS.CA: spike=4.37 liquidity=52328152.11 outlook=BULLISH_WATCH score=84.31 buy_ready=True
- KZPC.CA: spike=3.9 liquidity=18794022.51 outlook=WEAK_OR_RISKY score=27.31 buy_ready=False
- CAED.CA: spike=3.78 liquidity=24793282.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=9.54 5d=0.12% 20d=16.93% aboveMA50=100.0%
- #2 Telecommunications: score=8.89 5d=1.46% 20d=4.79% aboveMA50=100.0%
- #3 Automotive & Distribution: score=8.86 5d=1.87% 20d=9.76% aboveMA50=100.0%
- #4 Industrial Goods & Cables: score=7.4 5d=1.52% 20d=2.4% aboveMA50=100.0%
- #5 Energy & Petrochemicals: score=7.28 5d=5.48% 20d=2.37% aboveMA50=75.0%
- #6 Transportation & Logistics: score=6.99 5d=0.72% 20d=3.08% aboveMA50=100.0%
- #7 Agriculture & Food Production: score=6.87 5d=2.16% 20d=3.55% aboveMA50=50.0%
- #8 Textiles: score=6.84 5d=2.53% 20d=5.92% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY AFDI.CA
  - Entry: 47.44 | Take profit: 51.24 | Stop loss: 45.54
  - Confidence: LOW | score=29.72 | outlook=BULLISH_WATCH 90.31
  - Reason: WATCH/BUY SETUP: AFDI.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 60.65, support 41.84, resistance 48.89, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY RAYA.CA
  - Entry: 8.1 | Take profit: 8.74 | Stop loss: 7.78
  - Confidence: LOW | score=29.36 | outlook=BULLISH_WATCH 83.54
  - Reason: WATCH/BUY SETUP: RAYA.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.14, support 6.8, resistance 8.49, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY AREH.CA
  - Entry: 1.72 | Take profit: 1.86 | Stop loss: 1.65
  - Confidence: LOW | score=28.4 | outlook=BULLISH_WATCH 73.31
  - Reason: WATCH/BUY SETUP: AREH.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 56.0, support 1.51, resistance 1.76, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ELWA.CA: BULLISH_WATCH score=94.31 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- AFDI.CA: BULLISH_WATCH score=90.31 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ADCI.CA: BULLISH_WATCH score=88.31 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- NCCW.CA: BULLISH_WATCH score=85.31 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- CCRS.CA: BULLISH_WATCH score=84.31 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- RAYA.CA: BULLISH_WATCH score=83.54 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- MTIE.CA: BULLISH_WATCH score=82.86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; close to resistance
- ELEC.CA: BULLISH_WATCH score=80.4 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- AXPH.CA: BULLISH_WATCH score=80.31 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- SVCE.CA: BULLISH_WATCH score=77.31 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- CCRS.CA: rank=33.4 outlook=BULLISH_WATCH outlook_score=84.31 sector_rank=9 price=2.54 support=2.18 resistance=2.56 liquidity=52328152.11
- AFMC.CA: rank=30.72 outlook=BULLISH_WATCH outlook_score=76.31 sector_rank=9 price=75.25 support=66.0 resistance=76.5 liquidity=9055961.25
- AFDI.CA: rank=29.72 outlook=BULLISH_WATCH outlook_score=90.31 sector_rank=9 price=47.44 support=41.84 resistance=48.89 liquidity=20113325.98
- AXPH.CA: rank=29.45 outlook=BULLISH_WATCH outlook_score=80.31 sector_rank=9 price=1205.55 support=1073.0 resistance=1342.9 liquidity=9050064.22
- RAYA.CA: rank=29.36 outlook=BULLISH_WATCH outlook_score=83.54 sector_rank=1 price=8.1 support=6.8 resistance=8.49 liquidity=7957655.5
- RREI.CA: rank=28.9 outlook=CONSTRUCTIVE outlook_score=66.31 sector_rank=9 price=4.03 support=3.34 resistance=3.93 liquidity=24730144.0
- AREH.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=73.31 sector_rank=9 price=1.72 support=1.51 resistance=1.76 liquidity=13071475.0
- CCAP.CA: rank=28.07 outlook=CONSTRUCTIVE outlook_score=64.17 sector_rank=12 price=5.45 support=4.65 resistance=5.41 liquidity=32182944.0
- TMGH.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=65.26 sector_rank=10 price=98.03 support=92.1 resistance=99.43 liquidity=43821136.0
- MASR.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=61.31 sector_rank=9 price=8.21 support=6.71 resistance=8.2 liquidity=10993655.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=16.89 buy_ready=False sector_rank=9 price=229.9 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=64.75 liquidity=489859.94 spike=0.03
- ABUK.CA: score=8.27 buy_ready=False sector_rank=17 price=73.0 support=72.55 resistance=73.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31817580.0 spike=0.22
- ACAMD.CA: score=20.35 buy_ready=True sector_rank=9 price=2.33 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=3945633.25 spike=0.04
- ACGC.CA: score=19.16 buy_ready=False sector_rank=8 price=9.87 support=8.92 resistance=10.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=759416.88 spike=0.04
- ADCI.CA: score=25.62 buy_ready=True sector_rank=9 price=236.44 support=223.15 resistance=248.0 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=56.21 liquidity=15085108.6 spike=1.61
- ADIB.CA: score=11.37 buy_ready=False sector_rank=14 price=46.62 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:09 AM market time freshness=DELAYED_CURRENT RSI=47.99 liquidity=858744.75 spike=0.01
- ADPC.CA: score=17.41 buy_ready=True sector_rank=9 price=3.86 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=42.45 liquidity=1014958.0 spike=0.06
- AFDI.CA: score=29.72 buy_ready=True sector_rank=9 price=47.44 support=41.84 resistance=48.89 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=60.65 liquidity=20113325.98 spike=1.66
- AFMC.CA: score=30.72 buy_ready=True sector_rank=9 price=75.25 support=66.0 resistance=76.5 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=62.76 liquidity=9055961.25 spike=2.63
- AJWA.CA: score=17.07 buy_ready=False sector_rank=9 price=180.08 support=160.0 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=62.53 liquidity=673272.13 spike=0.04
- ALCN.CA: score=17.56 buy_ready=True sector_rank=6 price=29.63 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=66.22 liquidity=1162299.75 spike=0.06
- ALUM.CA: score=13.99 buy_ready=False sector_rank=9 price=23.03 support=20.55 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=44.03 liquidity=593644.06 spike=0.09
- AMER.CA: score=19.05 buy_ready=False sector_rank=10 price=3.23 support=2.28 resistance=3.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=76.8 liquidity=5645121.0 spike=0.07
- AMES.CA: score=9.4 buy_ready=False sector_rank=9 price=135.04 support=127.0 resistance=137.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24949592.0 spike=0.47
- AMIA.CA: score=18.44 buy_ready=True sector_rank=9 price=8.95 support=8.4 resistance=9.51 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=46.46 liquidity=4043162.41 spike=0.59
- AMOC.CA: score=22.03 buy_ready=True sector_rank=5 price=8.29 support=7.42 resistance=8.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=57.4 liquidity=5631626.5 spike=0.11
- APSW.CA: score=18.22 buy_ready=False sector_rank=9 price=8.51 support=8.0 resistance=8.79 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=46.03 liquidity=2223577.96 spike=2.8
- ARAB.CA: score=16.7 buy_ready=False sector_rank=10 price=0.25 support=0.2 resistance=0.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=79.1 liquidity=3303625.5 spike=0.03
- ARCC.CA: score=9.31 buy_ready=False sector_rank=18 price=54.52 support=53.0 resistance=57.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=45.43 liquidity=1538604.63 spike=0.08
- AREH.CA: score=28.4 buy_ready=True sector_rank=9 price=1.72 support=1.51 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=13071475.0 spike=0.37
- ARVA.CA: score=22.4 buy_ready=False sector_rank=9 price=10.72 support=10.5 resistance=12.95 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=43.38 liquidity=11917242.06 spike=0.76
- ASCM.CA: score=17.04 buy_ready=True sector_rank=9 price=62.41 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=57.24 liquidity=2641145.75 spike=0.03
- ASPI.CA: score=20.08 buy_ready=False sector_rank=9 price=0.31 support=0.3 resistance=0.33 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=37.31 liquidity=21842939.93 spike=1.34
- ATLC.CA: score=16.59 buy_ready=True sector_rank=13 price=5.24 support=4.84 resistance=5.43 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=45.65 liquidity=2954138.95 spike=0.46
- ATQA.CA: score=9.89 buy_ready=False sector_rank=17 price=9.51 support=9.21 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=619048.19 spike=0.02
- AXPH.CA: score=29.45 buy_ready=True sector_rank=9 price=1205.55 support=1073.0 resistance=1342.9 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=64.76 liquidity=9050064.22 spike=3.0
- BINV.CA: score=16.52 buy_ready=False sector_rank=12 price=48.24 support=45.01 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=448435.41 spike=0.07
- BIOC.CA: score=18.76 buy_ready=False sector_rank=9 price=73.43 support=66.75 resistance=76.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=55.63 liquidity=355152.47 spike=0.11
- BTFH.CA: score=14.53 buy_ready=False sector_rank=13 price=3.06 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=41.86 liquidity=2887159.25 spike=0.01
- CAED.CA: score=14.4 buy_ready=False sector_rank=9 price=103.0 support=96.33 resistance=104.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24793282.0 spike=3.78
- CANA.CA: score=13.25 buy_ready=False sector_rank=14 price=35.79 support=34.7 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=38.84 liquidity=729096.13 spike=0.07
- CCAP.CA: score=28.07 buy_ready=True sector_rank=12 price=5.45 support=4.65 resistance=5.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=63.39 liquidity=32182944.0 spike=0.05
- CCRS.CA: score=33.4 buy_ready=True sector_rank=9 price=2.54 support=2.18 resistance=2.56 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=59.15 liquidity=52328152.11 spike=4.37
- CEFM.CA: score=14.61 buy_ready=False sector_rank=9 price=104.46 support=95.75 resistance=110.5 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=55.54 liquidity=1208184.35 spike=0.6
- CERA.CA: score=17.4 buy_ready=True sector_rank=9 price=1.32 support=1.17 resistance=1.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:08 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=1003174.94 spike=0.05
- CFGH.CA: score=12.65 buy_ready=False sector_rank=9 price=0.11 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:02 AM market time freshness=DELAYED_CURRENT RSI=88.89 liquidity=8502.0 spike=1.12
- CICH.CA: score=23.18 buy_ready=False sector_rank=13 price=12.0 support=11.45 resistance=12.8 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=9497280.0 spike=2.52
- CIEB.CA: score=19.42 buy_ready=True sector_rank=14 price=24.4 support=23.3 resistance=24.75 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=57.31 liquidity=3901462.34 spike=0.72
- CIRA.CA: score=24.08 buy_ready=True sector_rank=11 price=32.66 support=26.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=68.96 liquidity=10474150.0 spike=0.41
- CLHO.CA: score=13.96 buy_ready=True sector_rank=20 price=16.23 support=15.21 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=1367115.13 spike=0.04
- CNFN.CA: score=16.02 buy_ready=False sector_rank=13 price=4.92 support=4.4 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=384638.66 spike=0.01
- COMI.CA: score=21.83 buy_ready=True sector_rank=14 price=135.45 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=50.34 liquidity=6314700.0 spike=0.01
- COPR.CA: score=15.39 buy_ready=True sector_rank=9 price=0.38 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=1987278.12 spike=0.08
- COSG.CA: score=20.61 buy_ready=True sector_rank=9 price=1.68 support=1.47 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=59.46 liquidity=2212627.25 spike=0.05
- CPCI.CA: score=18.3 buy_ready=False sector_rank=9 price=465.41 support=360.53 resistance=482.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=85.59 liquidity=4896980.0 spike=0.95
- CSAG.CA: score=17.25 buy_ready=False sector_rank=6 price=32.42 support=30.87 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT RSI=60.11 liquidity=851734.94 spike=0.05
- DAPH.CA: score=23.71 buy_ready=True sector_rank=9 price=84.0 support=77.5 resistance=87.9 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=56.57 liquidity=7314300.0 spike=0.91
- DEIN.CA: score=-0.6 buy_ready=False sector_rank=9 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=14.95 buy_ready=True sector_rank=15 price=27.04 support=24.23 resistance=27.83 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=61.58 liquidity=1613747.25 spike=0.34
- DSCW.CA: score=16.37 buy_ready=False sector_rank=9 price=1.86 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=973419.31 spike=0.03
- DTPP.CA: score=13.74 buy_ready=False sector_rank=9 price=205.01 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=85.86 liquidity=2342513.25 spike=0.06
- EALR.CA: score=17.33 buy_ready=False sector_rank=9 price=367.1 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=55.59 liquidity=929224.69 spike=0.08
- EASB.CA: score=12.87 buy_ready=False sector_rank=9 price=7.15 support=5.84 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=465945.38 spike=0.03
- EAST.CA: score=3.68 buy_ready=False sector_rank=15 price=36.52 support=36.47 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=28.75 liquidity=1345755.63 spike=0.03
- EBSC.CA: score=12.79 buy_ready=False sector_rank=9 price=1.89 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=388726.84 spike=0.06
- ECAP.CA: score=12.74 buy_ready=False sector_rank=9 price=32.37 support=31.3 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=38.47 liquidity=339355.09 spike=0.04
- EDFM.CA: score=17.01 buy_ready=False sector_rank=9 price=364.28 support=310.2 resistance=363.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=74.59 liquidity=606137.25 spike=0.71
- EEII.CA: score=16.89 buy_ready=False sector_rank=9 price=2.75 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=64.89 liquidity=490472.59 spike=0.02
- EFIC.CA: score=6.06 buy_ready=False sector_rank=17 price=195.07 support=180.02 resistance=205.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=27.15 liquidity=1795237.25 spike=0.65
- EFID.CA: score=14.06 buy_ready=False sector_rank=15 price=27.99 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=53.69 liquidity=1728163.5 spike=0.04
- EFIH.CA: score=16.04 buy_ready=False sector_rank=16 price=21.98 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=62.0 liquidity=720223.31 spike=0.02
- EGAL.CA: score=22.27 buy_ready=False sector_rank=17 price=302.0 support=272.28 resistance=314.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=44.64 liquidity=17607872.0 spike=0.37
- EGAS.CA: score=18.86 buy_ready=False sector_rank=5 price=53.55 support=46.51 resistance=54.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=56.62 liquidity=460681.88 spike=0.04
- EGBE.CA: score=12.53 buy_ready=False sector_rank=14 price=0.44 support=-0.34 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=96.19 liquidity=16159.39 spike=-0.35
- EGCH.CA: score=19.07 buy_ready=True sector_rank=17 price=13.63 support=12.13 resistance=13.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=41.8 liquidity=3797161.0 spike=0.08
- EGSA.CA: score=17.97 buy_ready=False sector_rank=2 price=8.97 support=8.67 resistance=9.13 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=70.21 liquidity=9562.02 spike=1.78
- EGTS.CA: score=14.86 buy_ready=False sector_rank=10 price=18.61 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=47.82 liquidity=462056.19 spike=0.01
- EHDR.CA: score=25.51 buy_ready=True sector_rank=9 price=2.79 support=2.37 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=48.35 liquidity=9108587.0 spike=0.25
- EKHO.CA: score=8.4 buy_ready=False sector_rank=5 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=22.22 buy_ready=True sector_rank=4 price=2.16 support=2.04 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=4817675.0 spike=0.2
- ELKA.CA: score=9.4 buy_ready=False sector_rank=9 price=1.82 support=1.78 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19500324.0 spike=0.39
- ELNA.CA: score=17.98 buy_ready=False sector_rank=9 price=39.47 support=35.55 resistance=40.65 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=49.58 liquidity=735839.23 spike=1.42
- ELSH.CA: score=18.23 buy_ready=True sector_rank=9 price=14.69 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=62.52 liquidity=1827361.0 spike=0.01
- ELWA.CA: score=18.01 buy_ready=True sector_rank=9 price=2.05 support=1.87 resistance=2.22 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=45.24 liquidity=2188309.35 spike=1.71
- EMFD.CA: score=22.4 buy_ready=False sector_rank=10 price=11.7 support=11.24 resistance=12.57 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=43.03 liquidity=77429007.54 spike=0.75
- ENGC.CA: score=0.25 buy_ready=False sector_rank=9 price=43.73 support=43.03 resistance=43.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=852616.19 spike=0.03
- EOSB.CA: score=14.43 buy_ready=False sector_rank=9 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=29345.44 spike=0.43
- EPCO.CA: score=22.74 buy_ready=True sector_rank=9 price=10.14 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=61.23 liquidity=4340257.0 spike=0.54
- EPPK.CA: score=14.98 buy_ready=False sector_rank=9 price=14.17 support=11.75 resistance=15.25 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=67.37 liquidity=579397.13 spike=0.62
- ETEL.CA: score=19.39 buy_ready=False sector_rank=2 price=97.45 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=987772.38 spike=0.01
- ETRS.CA: score=15.14 buy_ready=False sector_rank=9 price=10.96 support=9.82 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=49.36 liquidity=742696.56 spike=0.01
- EXPA.CA: score=17.67 buy_ready=True sector_rank=14 price=18.9 support=18.03 resistance=18.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=2157450.0 spike=0.09
- FAIT.CA: score=16.72 buy_ready=True sector_rank=14 price=37.04 support=35.06 resistance=37.7 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=49.4 liquidity=1203688.91 spike=0.57
- FAITA.CA: score=8.69 buy_ready=False sector_rank=14 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=14 July 01:14 PM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=34008.4 spike=1.07
- FERC.CA: score=15.71 buy_ready=True sector_rank=17 price=77.56 support=72.75 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=49.54 liquidity=1444112.88 spike=0.36
- FWRY.CA: score=16.02 buy_ready=False sector_rank=16 price=18.89 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=59.17 liquidity=5700135.5 spike=0.03
- GBCO.CA: score=13.98 buy_ready=False sector_rank=3 price=31.46 support=27.77 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=67.24 liquidity=580478.38 spike=0.01
- GDWA.CA: score=20.84 buy_ready=True sector_rank=9 price=0.84 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=3436563.5 spike=0.16
- GGCC.CA: score=9.4 buy_ready=False sector_rank=9 price=0.67 support=0.64 resistance=0.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12921000.0 spike=0.74
- GIHD.CA: score=16.52 buy_ready=True sector_rank=9 price=49.05 support=40.5 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=67.51 liquidity=2122023.25 spike=0.09
- GMCI.CA: score=15.4 buy_ready=False sector_rank=9 price=2.01 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=66.22 liquidity=999940.83 spike=0.93
- GRCA.CA: score=24.4 buy_ready=False sector_rank=9 price=51.49 support=48.0 resistance=58.74 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=39.59 liquidity=13255225.6 spike=4.4
- GSSC.CA: score=16.77 buy_ready=False sector_rank=9 price=258.38 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=68.43 liquidity=366646.22 spike=0.08
- GTWL.CA: score=21.4 buy_ready=False sector_rank=9 price=109.01 support=46.0 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=89.57 liquidity=11291817.0 spike=0.11
- HDBK.CA: score=3.11 buy_ready=False sector_rank=14 price=77.34 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=7.89 liquidity=596143.75 spike=0.01
- HELI.CA: score=24.4 buy_ready=False sector_rank=10 price=7.5 support=6.34 resistance=7.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=71.2 liquidity=10029855.0 spike=0.07
- HRHO.CA: score=9.03 buy_ready=False sector_rank=13 price=26.49 support=26.09 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=39.4 liquidity=1391011.5 spike=0.01
- ICID.CA: score=22.58 buy_ready=True sector_rank=9 price=8.26 support=6.55 resistance=8.47 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=59.47 liquidity=7938744.04 spike=1.12
- IDRE.CA: score=17.22 buy_ready=False sector_rank=9 price=45.72 support=41.1 resistance=47.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=53.88 liquidity=823427.25 spike=0.06
- IFAP.CA: score=18.78 buy_ready=False sector_rank=7 price=19.67 support=18.47 resistance=20.0 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=59.11 liquidity=3377476.7 spike=0.85
- INFI.CA: score=16.47 buy_ready=False sector_rank=9 price=102.34 support=88.51 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=72.43 liquidity=1066678.38 spike=0.11
- IRON.CA: score=9.65 buy_ready=False sector_rank=17 price=31.98 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=46.91 liquidity=380151.59 spike=0.05
- ISMA.CA: score=7.7 buy_ready=False sector_rank=9 price=27.29 support=26.54 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=17.9 liquidity=300644.22 spike=0.01
- ISMQ.CA: score=20.19 buy_ready=True sector_rank=17 price=9.4 support=8.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=68.94 liquidity=6917288.0 spike=0.05
- ISPH.CA: score=4.78 buy_ready=False sector_rank=20 price=11.49 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=26.94 liquidity=2195423.0 spike=0.04
- JUFO.CA: score=12.27 buy_ready=False sector_rank=15 price=30.08 support=29.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=39.91 liquidity=939068.44 spike=0.04
- KABO.CA: score=15.9 buy_ready=False sector_rank=8 price=7.75 support=6.04 resistance=7.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=86.71 liquidity=4499315.0 spike=0.15
- KWIN.CA: score=13.66 buy_ready=False sector_rank=9 price=72.0 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=35.76 liquidity=2262345.5 spike=0.17
- KZPC.CA: score=25.4 buy_ready=False sector_rank=9 price=8.64 support=8.26 resistance=10.7 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=39.41 liquidity=18794022.51 spike=3.9
- LCSW.CA: score=15.32 buy_ready=False sector_rank=18 price=31.08 support=26.6 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:10 AM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=544625.44 spike=0.01
- LUTS.CA: score=9.4 buy_ready=False sector_rank=9 price=0.78 support=0.75 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40644424.0 spike=0.8
- MAAL.CA: score=14.84 buy_ready=False sector_rank=9 price=8.5 support=5.75 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=98.37 liquidity=1437921.13 spike=0.09
- MASR.CA: score=26.4 buy_ready=True sector_rank=9 price=8.21 support=6.71 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=66.53 liquidity=10993655.0 spike=0.12
- MBSC.CA: score=11.15 buy_ready=False sector_rank=18 price=236.01 support=222.66 resistance=256.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=39.17 liquidity=1379205.5 spike=0.06
- MCQE.CA: score=12.28 buy_ready=False sector_rank=18 price=176.65 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:11 AM market time freshness=DELAYED_CURRENT RSI=47.89 liquidity=508616.38 spike=0.03
- MCRO.CA: score=25.62 buy_ready=True sector_rank=9 price=1.39 support=1.17 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=46927992.0 spike=1.11
- MENA.CA: score=19.24 buy_ready=True sector_rank=10 price=7.01 support=6.59 resistance=7.59 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=55.38 liquidity=4839150.37 spike=0.73
- MEPA.CA: score=14.7 buy_ready=False sector_rank=9 price=1.67 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=44.74 liquidity=1300209.25 spike=0.12
- MFPC.CA: score=21.49 buy_ready=False sector_rank=17 price=38.36 support=34.22 resistance=38.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=9220217.0 spike=0.09
- MFSC.CA: score=14.36 buy_ready=False sector_rank=9 price=45.71 support=44.0 resistance=56.0 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=51.48 liquidity=4956609.46 spike=0.74
- MHOT.CA: score=4.85 buy_ready=False sector_rank=21 price=16.44 support=16.12 resistance=38.38 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=3.54 liquidity=5453049.54 spike=0.4
- MICH.CA: score=15.86 buy_ready=True sector_rank=9 price=38.5 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=1458433.0 spike=0.09
- MILS.CA: score=16.77 buy_ready=False sector_rank=9 price=135.99 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=365967.31 spike=0.03
- MIPH.CA: score=17.21 buy_ready=False sector_rank=20 price=729.63 support=630.13 resistance=725.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:08 AM market time freshness=DELAYED_CURRENT RSI=54.08 liquidity=623214.63 spike=0.29
- MOED.CA: score=16.66 buy_ready=True sector_rank=9 price=0.73 support=0.65 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=58.48 liquidity=2263242.0 spike=0.18
- MOIL.CA: score=19.62 buy_ready=False sector_rank=5 price=0.55 support=0.46 resistance=0.55 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=76.42 liquidity=1224032.43 spike=3.74
- MOIN.CA: score=12.56 buy_ready=False sector_rank=9 price=23.95 support=22.6 resistance=25.01 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=48.18 liquidity=156345.6 spike=0.21
- MOSC.CA: score=17.36 buy_ready=False sector_rank=9 price=285.0 support=250.0 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=56.35 liquidity=961871.19 spike=0.07
- MPCI.CA: score=20.85 buy_ready=True sector_rank=9 price=243.96 support=215.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=50.37 liquidity=6452238.5 spike=0.07
- MPCO.CA: score=24.4 buy_ready=True sector_rank=7 price=1.93 support=1.7 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=17781986.0 spike=0.22
- MPRC.CA: score=21.4 buy_ready=False sector_rank=9 price=42.16 support=31.72 resistance=43.39 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=88.74 liquidity=41055829.45 spike=0.89
- MTIE.CA: score=24.21 buy_ready=True sector_rank=3 price=9.73 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=62.44 liquidity=4812962.0 spike=0.21
- NAHO.CA: score=8.4 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=2054.95 spike=0.09
- NCCW.CA: score=17.68 buy_ready=True sector_rank=9 price=6.44 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=56.91 liquidity=1284379.25 spike=0.06
- NEDA.CA: score=16.96 buy_ready=False sector_rank=9 price=2.8 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=361328.79 spike=1.1
- NHPS.CA: score=16.77 buy_ready=False sector_rank=9 price=82.9 support=61.55 resistance=83.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=77.61 liquidity=3368447.25 spike=0.08
- NINH.CA: score=13.55 buy_ready=False sector_rank=9 price=18.02 support=17.03 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=58.37 liquidity=2145200.0 spike=0.24
- NIPH.CA: score=7.59 buy_ready=False sector_rank=20 price=188.0 support=186.3 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44621264.0 spike=0.52
- OBRI.CA: score=14.15 buy_ready=False sector_rank=9 price=35.85 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=754907.31 spike=0.02
- OCDI.CA: score=12.87 buy_ready=False sector_rank=10 price=26.86 support=20.55 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=78.93 liquidity=1473123.38 spike=0.01
- OCPH.CA: score=12.34 buy_ready=False sector_rank=9 price=415.0 support=384.8 resistance=435.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21569918.0 spike=2.47
- ODIN.CA: score=17.18 buy_ready=False sector_rank=9 price=2.46 support=2.05 resistance=2.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=68.49 liquidity=778672.63 spike=0.05
- OFH.CA: score=20.92 buy_ready=True sector_rank=9 price=0.64 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=59.0 liquidity=4519668.5 spike=0.22
- OIH.CA: score=16.08 buy_ready=False sector_rank=12 price=1.41 support=1.35 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=5011201.5 spike=0.07
- OLFI.CA: score=16.25 buy_ready=False sector_rank=15 price=22.73 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=58.36 liquidity=922890.31 spike=0.03
- ORAS.CA: score=0.86 buy_ready=False sector_rank=19 price=686.44 support=685.21 resistance=687.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3263144.0 spike=1.0
- ORHD.CA: score=17.08 buy_ready=True sector_rank=10 price=39.18 support=37.0 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=47.05 liquidity=2684027.25 spike=0.02
- ORWE.CA: score=10.11 buy_ready=False sector_rank=8 price=22.59 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=36.84 liquidity=705195.5 spike=0.04
- PHAR.CA: score=7.94 buy_ready=False sector_rank=20 price=86.35 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=38.42 liquidity=349605.41 spike=0.02
- PHDC.CA: score=10.38 buy_ready=False sector_rank=10 price=14.72 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=24.37 liquidity=2983535.5 spike=0.01
- PHTV.CA: score=14.3 buy_ready=False sector_rank=9 price=298.84 support=207.0 resistance=308.49 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=86.72 liquidity=2898747.96 spike=0.22
- POUL.CA: score=13.93 buy_ready=False sector_rank=15 price=38.99 support=35.28 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=65.82 liquidity=593108.56 spike=0.01
- PRCL.CA: score=22.77 buy_ready=False sector_rank=18 price=34.9 support=24.5 resistance=36.99 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=73.47 liquidity=11217663.19 spike=0.26
- PRDC.CA: score=9.4 buy_ready=False sector_rank=10 price=9.24 support=9.06 resistance=9.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38744372.0 spike=0.26
- PRMH.CA: score=16.17 buy_ready=True sector_rank=9 price=2.75 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=44.79 liquidity=1768943.13 spike=0.06
- RACC.CA: score=20.29 buy_ready=True sector_rank=9 price=10.25 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=1891756.75 spike=0.11
- RAKT.CA: score=14.21 buy_ready=False sector_rank=9 price=22.22 support=21.25 resistance=23.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=14 July 12:50 PM market time freshness=DELAYED_CURRENT RSI=50.2 liquidity=807327.31 spike=2.5
- RAYA.CA: score=29.36 buy_ready=True sector_rank=1 price=8.1 support=6.8 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=64.14 liquidity=7957655.5 spike=0.07
- RMDA.CA: score=8.31 buy_ready=False sector_rank=20 price=4.96 support=4.81 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=720782.88 spike=0.04
- ROTO.CA: score=16.21 buy_ready=True sector_rank=9 price=42.1 support=33.99 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=49.68 liquidity=1805519.75 spike=0.05
- RREI.CA: score=28.9 buy_ready=True sector_rank=9 price=4.03 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=24730144.0 spike=1.25
- RTVC.CA: score=16.26 buy_ready=False sector_rank=9 price=3.86 support=3.55 resistance=3.96 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=45.95 liquidity=2858345.36 spike=0.85
- RUBX.CA: score=9.4 buy_ready=False sector_rank=9 price=14.36 support=14.2 resistance=14.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15540360.0 spike=0.28
- SAUD.CA: score=14.6 buy_ready=False sector_rank=14 price=21.54 support=19.99 resistance=22.19 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=47.83 liquidity=2085222.87 spike=0.45
- SCEM.CA: score=10.17 buy_ready=False sector_rank=18 price=61.99 support=60.14 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=51.24 liquidity=400596.88 spike=0.02
- SCFM.CA: score=22.0 buy_ready=False sector_rank=9 price=256.69 support=226.5 resistance=269.0 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=55.4 liquidity=5957004.89 spike=1.32
- SCTS.CA: score=18.08 buy_ready=True sector_rank=11 price=616.15 support=540.0 resistance=649.0 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=60.17 liquidity=1998174.53 spike=0.43
- SDTI.CA: score=17.65 buy_ready=True sector_rank=9 price=47.05 support=45.55 resistance=49.5 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=44.6 liquidity=3249131.8 spike=0.69
- SEIG.CA: score=16.3 buy_ready=False sector_rank=9 price=250.0 support=181.01 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=85.19 liquidity=2903687.5 spike=0.14
- SIPC.CA: score=19.34 buy_ready=True sector_rank=9 price=3.52 support=3.25 resistance=3.6 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=48.1 liquidity=5940887.01 spike=0.99
- SKPC.CA: score=13.87 buy_ready=False sector_rank=17 price=16.53 support=15.58 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=49.12 liquidity=2601360.75 spike=0.08
- SMFR.CA: score=14.4 buy_ready=False sector_rank=9 price=254.8 support=253.0 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19092908.0 spike=9.28
- SNFC.CA: score=10.89 buy_ready=False sector_rank=9 price=11.67 support=11.26 resistance=12.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=45.0 liquidity=1488058.63 spike=0.13
- SPIN.CA: score=19.53 buy_ready=False sector_rank=8 price=14.63 support=13.3 resistance=14.8 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=80.45 liquidity=6134051.82 spike=0.7
- SPMD.CA: score=16.86 buy_ready=False sector_rank=9 price=0.44 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:15 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=463249.53 spike=0.03
- SUGR.CA: score=9.78 buy_ready=False sector_rank=15 price=47.06 support=45.31 resistance=49.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:14 AM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=452425.69 spike=0.09
- SVCE.CA: score=26.4 buy_ready=True sector_rank=9 price=9.31 support=8.56 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=14 July 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=16865726.0 spike=0.24
- SWDY.CA: score=19.27 buy_ready=True sector_rank=4 price=89.76 support=84.3 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=2872319.75 spike=0.22
- TALM.CA: score=11.48 buy_ready=False sector_rank=11 price=15.78 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=38.86 liquidity=2399552.5 spike=0.21
- TMGH.CA: score=26.4 buy_ready=True sector_rank=10 price=98.03 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:12 AM market time freshness=DELAYED_CURRENT RSI=53.98 liquidity=43821136.0 spike=0.12
- TRTO.CA: score=10.4 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=68.03 spike=0.32
- UEFM.CA: score=17.12 buy_ready=False sector_rank=9 price=500.78 support=460.0 resistance=529.0 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=58.73 liquidity=721123.2 spike=0.49
- UEGC.CA: score=9.4 buy_ready=False sector_rank=9 price=2.14 support=2.09 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11752971.0 spike=0.51
- UNIP.CA: score=20.15 buy_ready=True sector_rank=9 price=0.34 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=1748811.75 spike=0.1
- UNIT.CA: score=16.24 buy_ready=False sector_rank=10 price=19.61 support=12.0 resistance=20.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=73.26 liquidity=1841167.38 spike=0.09
- WCDF.CA: score=14.12 buy_ready=False sector_rank=9 price=523.93 support=504.0 resistance=544.99 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=45.1 liquidity=399758.58 spike=1.16
- WKOL.CA: score=24.44 buy_ready=True sector_rank=9 price=315.0 support=273.1 resistance=334.5 source=Yahoo Finance as_of=2026-07-12T21:00:00+00:00 freshness=FRESH RSI=64.53 liquidity=7681905.0 spike=1.18
- ZEOT.CA: score=16.7 buy_ready=True sector_rank=9 price=11.59 support=9.26 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:16 AM market time freshness=DELAYED_CURRENT RSI=48.89 liquidity=2302480.25 spike=0.05
- ZMID.CA: score=26.4 buy_ready=False sector_rank=10 price=7.26 support=6.11 resistance=7.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:13 AM market time freshness=DELAYED_CURRENT RSI=71.82 liquidity=11402778.0 spike=0.05

## Backtesting Lite
- CCRS.CA: 180d return=58.75%, max drawdown=-34.85%, MA20>MA50 days last20=20, as_of=2026-07-12T21:00:00+00:00
- AFMC.CA: 180d return=5.0%, max drawdown=-29.11%, MA20>MA50 days last20=10, as_of=2026-07-12T21:00:00+00:00
- AFDI.CA: 180d return=31.81%, max drawdown=-16.45%, MA20>MA50 days last20=20, as_of=2026-07-12T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CCRS.CA: status=RECENT_ACCEPTED latest=2026-07-07 age_days=8 sources=3 expected=Gulf Canadian Company for Arab Real Estate Investment summary=Recent evidence for Gulf Canadian Company for Arab Real Estate Investment (CCRS.CA) includes financial statements and reports, disclosures, and market data from the Egyptian Exchange and financial news sites. The company reported turning profitable in Q1 2026 and held its Annual General Meeting in April 2026.
  - Gulf Canadian Company for Arab Real Estate Investment (EGX:CCRS) Financials & Income Statement (March 31, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ8ddOkX11dhnxPXuInlppdwahKLfCcno3kX1tg7VDsZ1gvMy8xpyrT2rOjmuhvej5RFN1F4Xh2yYNtBE8k0wzOKvAKZBg5fUFHCFcfmuqBqODkX-fO4xGWFqDf8c0R7BRS7pLDjhga8G5B0fsTg==
  - Gulf Canadian Company for Arab Real Estate Investment (EGX:CCRS) Statistics & Valuation Metrics (July 07, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmGwsFZbQ1Xobfp06-SC8ihlfi6aZU_hpktq3DhdU74q5Cd1T6XzCpaEyLPtAzIzI5H_KMoctgf0ciSecTXp_i90jV6ozHLHjAWqPQcstFeS2RGO7YTXsaIoh5TSbq2y_F6TuqkDmasIFUGvFptQ==
  - The Egyptian Exchange - Gulf Canadian Real Estate Investment Co. (CCRS.CA) - Disclosure Form (Undated): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEYoUW3ZcLcM1bCrgLHBMAYWjVVKCNW3OWhPrZEC9srk6jRw-VQLeXZRpUCrSvoZqE67EOgl-tEfNNEFGq2CBcXw3vqBWZoBc5lB9YY_DaKVUalK_4l7aSUWuMHz8lRsJzQi_BCf2dOyfj0ppMYLcpKlE=
- AFMC.CA: status=RECENT_ACCEPTED latest=2026-05-18 age_days=58 sources=3 expected=Alexandria Flour Mills summary=Alexandria Flour Mills (AFMC.CA) has released its financial results for the period ending June 30, 2025, and an external auditor's report for Q1 2026. Current market data and company statistics are also available.
  - Alexandria Flour Mills (AFMC.CA) Reports its Financial Results for the Period Ending 30/06/2025 (September 09, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpp0XM80NmWaOJV_Ha1vK7ZSCY0BncFniNIgLwv29gmCN8RGYE3tIBkIsIdLivU2_6hePc8gzdR12QEUzBZ85s4PqdJx2YMY0_IGpnbhWyg1mXAsehMVmUz6KfnruILoHKEnRCOZx8r2K5qQv7mw==
  - Alexandria Flour Mills (EGX:AFMC) Statistics & Valuation Metrics (Undated): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRk_b7Anfkotqj9ltswRPmA07yDTbmDZLl_503eGO7EzQDMW9CX0crAA7ScULn0EplhFT7nxPR8t39aDJLXwZJjXsls9G5ahY-VrxQZKOzr-F4EV2s3Kn5zDEUaIxTtjn5n1aHJbvtk0yjz9vSpg==
  - Alexandria Flour Mills (AFMC.CA) - External Auditor's Report (May 18, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZjcZXTofgcsOG-rOBfolnWiB5XsJsXiQ-JZ2R4uiva4eOlHJElaUJMQpBRKELPM-ncq2i69WzeF_DjKUvYInjxhsmHOPa6s1bOJtzOn5CQxDtz6JKs2Zapq96nT6YO7_Y5rqtOXwP2LDgUWwMusTARdw==
- AFDI.CA: status=RECENT_ACCEPTED latest=2026-07-12 age_days=3 sources=3 expected=Al Ahly for Development & Investment summary=Al Ahly for Development & Investment (AFDI.CA) has released financial statements for the period ending September 30, 2025, and its consolidated profits for Q3 2025. Current stock statistics are also available.
  - Al Ahly for Development & Investment (EGX:AFDI) Financials & Income Statement (September 30, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNazuq2f3x19WB1J7lzFKG5fztL_vUnvI9HoQpJ0oXtwTdPSIfEhtaV89M8HeCIBycV_W1nXN_pEdaYeWDYNPxf268abyGYbrVnIT_EORVaAaXy_3MVHA6lzdnDUMqTbJP4aAjzNPl0ALikwFugg==
  - El Ahli Investment and Development (AFDI) - Mubasher Info (July 12, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2EnwWxwR4rEqdFmOl0JHmFcwWeOPNL1i53fZ2hJ-s9L2NX1o_UmlQqw73jSJHeO2q049l5H2PHi7tNrIW3G7oMPUOrki1b76wRFCMHlTKxx4kQBsjZ_A7XhtHAKibJxmJZtklMOSUuvftKC-iAbCYWpNvhg7RxQ==
  - El Ahly for Development's consolidated profits fall 89.3% YoY in 9 months (February 03, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqktmJyvc71O65zN0qnxZbCO5XROijJjDGpvF1Jy8lM7cfqqGjIrlGTX3R8gDPxdsFVe544foF3P23I-Pld2m-MZkG3FAiCRyhWHrjOM8q6BeooLbbmlyOJ2pGVeCGXu3mCNWOcyR6ZzzS_J6fECth7g==
- AXPH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=2 expected=Alexandria Co. For Pharmaceuticals & Chemical Industries summary=Alexandria Co. For Pharmaceuticals & Chemical Industries (AXPH.CA) has recent financial data available, including revenue and net income for the latest quarters.
  - Alexandria Pharma - EGX:AXPH Financials - Investing.com (Latest Quarter Revenue and Net Income): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHElH-hbMOM-i3xxWs9CvXv6sVcwIPAlHiCF4R1VgqLi-wejAZ5wRKg6TvZAetdHe91Lvn0RJskQbUjOUokzH0TDIBWX0AsRPZVLjG-1nSd8TiF4vtYRrGhKtVAZ8cttwtd_nViSPnUcIDONaAfwlF89Qric3USKXHIqCTv2g==
  - Alexandria Company for Pharmaceuticals and Chemical Industries Income Statement – EGX:AXPH - TradingView (Latest Quarter Revenue): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZjLco2YUqJJx2EZE5g7Fe6y3V6Sc2E_cJqlWGMepfP3lOtrTJMO39h1AbEZ43FZzgDAnOpdckjYYLPp2SAjXTrDE94-PXr_-qTMv5V_r-eV7ewnnpOK59uodSc60InFurSxw_Pk8sI3frzWaJ8ovvkoJuf4fQd4ykNZ4qMz01y2_xmQ==
- RAYA.CA: status=RECENT_ACCEPTED latest=2026-07-01 age_days=14 sources=3 expected=Raya Holding summary=Raya Holding (RAYA.CA) has released various disclosures, including board meeting decisions and financial statements, with recent updates up to July 2026. The company also has recent financial performance data available.
  - DISCLOSURES - Raya Corp (Various dates, latest July 01, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpaofkihGDbQOohzcNcyv6HuCwt79t8Vi2Y_TaSLJIkn83dQgM3qF61g_MYd_aylyxYYt_k7s-KfJKQMLGPh8zD7CFfxLNwFfz5bWNgABn8s__4tUehCiyz7TM
  - Release from Raya Holding For financial Investments (RAYA.CA) Concerning the Board of Directors & the Executive Managers (August 06, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOUPO6O_hNe_uLHQX3spAXzClR2NYrjxo8Ae9KQ2A5lsCjMq8ZISRswGUkG2Q5KnWyOq-aRJOQLtz03tJIOxySteGKcALHB4V19Ieww9TwEnLSvcIbeSlcwiQ2ChUP5ORSA4rU6tXGk2AJ-MqKAw==
  - EGX:RAYA Financials | Raya Hld - Investing.com (Latest Quarter Revenue and Net Income): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cZl1hJxG5VJHtDNoE2sE97DLup2AJZMp2msykb8dZD-czNRvEBHEZ4TLzVHQ6vGboEdXitDRbiLPU9gSTu5Ca9MJBYV8Ihq-EfanWC6OLtvsrm9zi2PB5L_1q46akj5O_iEyiN_OlPwYrYGGRtA_fV7J7fYuObXIJev0Dw==
- RREI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Arab Real Estate Investment Co. summary=Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
- AREH.CA: status=RECENT_ACCEPTED latest=2026-07-05 age_days=10 sources=3 expected=Real Estate Egyptian Consortium S.A.E summary=Real Estate Egyptian Consortium S.A.E (AREH.CA) has actively released financial results for Q1 2026, board meeting decisions, and various disclosures to shareholders, with updates spanning from June to July 2026.
  - Egyptian Real Estate Group (AREH.CA) Reports its Financial Results for the Period from 01/01/2026 to 31/03/2026 (June 02, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyqfftjwbnHWKJlxcGiCnShaq3M0VzxG4b5ZBmt1xk5_biF76N3IgWt8NLI_Z1noyPzbBdIWysD6PZRdq1rzRV8OtadHZjGIUi7i-eRO40THa84CLULBZMRmChSwzZshUpxncxCGES8qWUgpRjn40=
  - Egyptian Real Estate Group (AREH.CA) - Decisions of the BoD Meeting (June 02, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyqfftjwbnHWKJlxcGiCnShaq3M0VzxG4b5ZBmt1xk5_biF76N3IgWt8NLI_Z1noyPzbBdIWysD6PZRdq1rzRV8OtadHZjGIUi7i-eRO40THa84CLULBZMRmChSwzZshUpxncxCGES8qWUgpRjn40=
  - Egyptian Real Estate Group (AREH.CA) - Release Regarding the Periodic Disclosure to Shareholders (July 05, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlLl4Ao5sNa2MXdYvKIwLMK1nRfKGg8WFFXs4kKBX25VH2E7VJGpKYD4NEMnDyzZC-RqJJmYoa1LOGV2kae3qm_Q0Ld47mMIYPi6py5-pQudWaS3-JIB6V6K4huJfwf779nhVeIOmfnBhXZGAzS0ypl
- CCAP.CA: status=RECENT_ACCEPTED latest=2026-07-01 age_days=14 sources=3 expected=Qalaa Holdings summary=Qalaa Holdings (CCAP.CA) has released its consolidated financial results for FY2023, Q3 2025, and Q2 2025. The company is also actively pursuing an increased stake in Taqa Arabia, with disclosures made in June 2026.
  - Qalaa Holdings Consolidated Financial Results for FY23, Q3 2025, and Q2 2025 (March 19, 2026 and February 02, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHf0HivMpq1yrhiHbvmSPV59nnX2e4bYk8GsTFJEMB2ZHLXuQp1w7M71ykBsYWkOSDEQPmCcknLTuJ6jxLgFLJ2t6QfqG6YQjA3WrYG3IBjWi8X4txU4XteGew4v4qAHYrtkzQ=
  - Qalaa Holdings (CCAP.CA) Stock Price Quote - Cbonds (July 01, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWzVZYgIbdAH8RcfxSS5hRwQF5A6FYAKS-F994chM4GQkFk4mINgFMv6Nt2qxJ9u3DV4br38_gUmsUs7jK1wdx0Uy5nYnH-kWTG4ycDqy1ZzhQmRwXseJ3G0-b75YGmXZs
  - Egypt: Qalaa Holdings eyes 55% stake in Taqa Arabia through future purchase rights (June 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgKVve5ndlc5DZ0ZnwD9ZioBNKiUE9hsXuHS6nj0SUZC_1da_2jaioFIhggFbUOWFDnFIY22wanSFWp3tziPFubRTieS6Td7RBk1qipF8h3JooP8FVSEfBAd56pZRLQTG5cYdLWuBdFz8oGCTA_gt58lX7k2Aj_LSGslCaj_hM_3bm0lXz7lUzhfJAAe6iR9ddjSbj8qYw3RrqG8Ayu_buxQo0GB_PRB52ILZHU2HzxjF4R0kpUFcILTPB__4mQeV7Fw==

## Warnings
- OpenRouter API error: 429
- Evidence for AXPH.CA matches the company but no source/report date was detected.
- Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
