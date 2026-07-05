# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-05T08:33:58.073759+00:00
Generated Cairo: 2026-07-05 11:33
Run timing: target 08:45 Cairo | generated Cairo 2026-07-05 11:33 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-05 11:29

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 48
- Data quality issues: 0
- Tradeable price/liquidity tickers: 183/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, July 05
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 50.0% / above MA50 40.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 60.0% / above MA50 72.5%
- Sector breadth: 33.33%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- CCAP.CA: liquidity=408325920.0 spike=0.61 score=23.98
- RUBX.CA: liquidity=106712864.0 spike=3.73 score=13.49
- TMGH.CA: liquidity=94591024.0 spike=0.27 score=23.44
- DTPP.CA: liquidity=91742024.0 spike=7.63 score=13.49
- NIPH.CA: liquidity=78461424.0 spike=0.98 score=25.46

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b-20230311:free
- Summary: We need to output JSON with keys summary and bullets (3-5 short strings). Must not make trade decision, just explain why scanner selected prioritized tickets, what liquidity/sector/support/resistance/outlook means for next 1-3 days, and how EGX30/EGX70 market regime changes risk mode, include uncertainty. No quantities or position sizing. No live data mention (but we can reference given data as static). Must be concise Telegram narrative.

We need to summarize: primary ticket NHPS.CA, also EEII.CA, LCSW.CA. Explain selection: price above MA20/MA50, RSI moderate, liquidity above threshold, support/resistance levels, outlook bullish watch, but momentum extended, sector not leading. Market regi
- Scanner flags NHPS.CA, EEII.CA, LCSW.CA as watch/buy setups under selective small‑mid swing regime.
- Do not mention quantities or position sizing.
- price is above its 20‑ and 50‑day averages and sits between support and resistance
- liquidity above threshold
- Scanner highlights NHPS.CA, EEII.CA and LCSW.CA as watch/buy candidates in a selective small‑mid swing environment.

## Top Liquidity Spikes
- CFGH.CA: spike=24.69 liquidity=175361.52 outlook=WEAK_OR_RISKY score=1.73 buy_ready=False
- DTPP.CA: spike=7.63 liquidity=91742024.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOIL.CA: spike=5.11 liquidity=1012750.31 outlook=BULLISH_WATCH score=84.57 buy_ready=True
- WCDF.CA: spike=4.15 liquidity=1416461.93 outlook=WEAK_OR_RISKY score=25.73 buy_ready=False
- RUBX.CA: spike=3.73 liquidity=106712864.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=10.2 5d=2.7% 20d=12.9% aboveMA50=100.0%
- #2 Technology & Distribution: score=8.82 5d=4.05% 20d=3.08% aboveMA50=100.0%
- #3 Education: score=6.83 5d=0.24% 20d=2.86% aboveMA50=100.0%
- #4 Tourism & Leisure: score=6.22 5d=-2.91% 20d=5.66% aboveMA50=100.0%
- #5 Investment Holding: score=4.94 5d=0.4% 20d=-3.42% aboveMA50=66.67%
- #6 Textiles: score=4.23 5d=-0.07% 20d=-3.31% aboveMA50=100.0%
- #7 Transportation & Logistics: score=4.16 5d=2.54% 20d=-0.55% aboveMA50=50.0%
- #8 Banking & Financials: score=3.93 5d=0.55% 20d=-0.73% aboveMA50=70.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY NHPS.CA
  - Entry: 68.09 | Take profit: 75.11 | Stop loss: 65.37
  - Confidence: LOW | score=26.65 | outlook=BULLISH_WATCH 79.73
  - Reason: WATCH/BUY SETUP: NHPS.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 63.93, support 61.55, resistance 75.49, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY EEII.CA
  - Entry: 2.6 | Take profit: 2.8 | Stop loss: 2.5
  - Confidence: LOW | score=25.59 | outlook=BULLISH_WATCH 71.73
  - Reason: WATCH/BUY SETUP: EEII.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 66.04, support 2.3, resistance 2.55, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY LCSW.CA
  - Entry: 28.6 | Take profit: 31.17 | Stop loss: 27.46
  - Confidence: LOW | score=25.29 | outlook=BULLISH_WATCH 74.22
  - Reason: WATCH/BUY SETUP: LCSW.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 61.9, support 26.0, resistance 31.33, and evidence sources. Macro trend is Bullish; market regime is SELECTIVE_SMALL_MID_SWINGS; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SCTS.CA: BULLISH_WATCH score=88.83 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MOIL.CA: BULLISH_WATCH score=84.57 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- CCAP.CA: BULLISH_WATCH score=80.94 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- NHPS.CA: BULLISH_WATCH score=79.73 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading
- MTIE.CA: BULLISH_WATCH score=76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- BINV.CA: BULLISH_WATCH score=74.94 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EXPA.CA: BULLISH_WATCH score=74.93 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- IDRE.CA: BULLISH_WATCH score=74.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- SPMD.CA: BULLISH_WATCH score=74.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- OCPH.CA: BULLISH_WATCH score=74.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- NHPS.CA: rank=26.65 outlook=BULLISH_WATCH outlook_score=79.73 sector_rank=9 price=68.09 support=61.55 resistance=75.49 liquidity=9162629.0
- RAYA.CA: rank=26.4 outlook=CONSTRUCTIVE outlook_score=68.82 sector_rank=2 price=7.84 support=6.7 resistance=7.85 liquidity=33155812.0
- EEII.CA: rank=25.59 outlook=BULLISH_WATCH outlook_score=71.73 sector_rank=9 price=2.6 support=2.3 resistance=2.55 liquidity=30470772.0
- LCSW.CA: rank=25.29 outlook=BULLISH_WATCH outlook_score=74.22 sector_rank=14 price=28.6 support=26.0 resistance=31.33 liquidity=13674715.0
- AMES.CA: rank=24.31 outlook=CONSTRUCTIVE outlook_score=61.73 sector_rank=9 price=62.81 support=45.15 resistance=69.5 liquidity=20853126.0
- CCAP.CA: rank=23.98 outlook=BULLISH_WATCH outlook_score=80.94 sector_rank=5 price=5.17 support=4.65 resistance=5.78 liquidity=408325920.0
- ADIB.CA: rank=23.57 outlook=CONSTRUCTIVE outlook_score=68.93 sector_rank=8 price=47.0 support=44.01 resistance=48.49 liquidity=10176609.0
- ASCM.CA: rank=23.49 outlook=CONSTRUCTIVE outlook_score=68.73 sector_rank=9 price=60.72 support=54.07 resistance=73.73 liquidity=18699558.0
- MASR.CA: rank=23.49 outlook=CONSTRUCTIVE outlook_score=56.73 sector_rank=9 price=7.59 support=6.54 resistance=7.69 liquidity=37993632.0
- MPCI.CA: rank=23.49 outlook=CONSTRUCTIVE outlook_score=50.73 sector_rank=9 price=249.74 support=207.0 resistance=256.0 liquidity=25976398.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=14.47 buy_ready=False sector_rank=9 price=207.37 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=53.77 liquidity=978037.5 spike=0.16
- ABUK.CA: score=11.76 buy_ready=False sector_rank=21 price=68.51 support=66.66 resistance=83.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=19.16 liquidity=13836716.0 spike=0.11
- ACAMD.CA: score=20.58 buy_ready=False sector_rank=9 price=2.27 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=9091165.0 spike=0.07
- ACGC.CA: score=15.13 buy_ready=False sector_rank=6 price=9.3 support=8.92 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=47.71 liquidity=3441756.0 spike=0.11
- ADCI.CA: score=15.36 buy_ready=False sector_rank=9 price=240.02 support=212.0 resistance=248.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=76.12 liquidity=4870173.0 spike=0.45
- ADIB.CA: score=23.57 buy_ready=True sector_rank=8 price=47.0 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=60.13 liquidity=10176609.0 spike=0.14
- ADPC.CA: score=9.35 buy_ready=False sector_rank=9 price=3.49 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=1853971.25 spike=0.11
- AFDI.CA: score=16.24 buy_ready=True sector_rank=9 price=44.66 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:59 AM market time freshness=DELAYED_CURRENT RSI=64.79 liquidity=2745899.5 spike=0.18
- AFMC.CA: score=13.41 buy_ready=False sector_rank=9 price=71.26 support=66.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=2457735.25 spike=1.23
- AJWA.CA: score=9.38 buy_ready=False sector_rank=9 price=180.11 support=132.15 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=77.99 liquidity=887965.13 spike=0.03
- ALCN.CA: score=11.59 buy_ready=False sector_rank=7 price=28.3 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=52.79 liquidity=930696.63 spike=0.08
- ALUM.CA: score=4.28 buy_ready=False sector_rank=9 price=21.76 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=29.46 liquidity=783264.38 spike=0.08
- AMER.CA: score=18.44 buy_ready=False sector_rank=11 price=2.46 support=2.28 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=15222431.0 spike=0.22
- AMES.CA: score=24.31 buy_ready=True sector_rank=9 price=62.81 support=45.15 resistance=69.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=69.19 liquidity=20853126.0 spike=1.41
- AMIA.CA: score=12.37 buy_ready=False sector_rank=9 price=8.7 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=882512.88 spike=0.07
- AMOC.CA: score=18.03 buy_ready=False sector_rank=17 price=7.84 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=10581209.0 spike=0.22
- ANFI.CA: score=9.82 buy_ready=False sector_rank=9 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=8.06 buy_ready=False sector_rank=9 price=8.34 support=8.0 resistance=9.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=572314.75 spike=0.65
- ARAB.CA: score=18.44 buy_ready=False sector_rank=11 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=59731672.0 spike=0.76
- ARCC.CA: score=21.07 buy_ready=True sector_rank=14 price=56.29 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=7778174.0 spike=0.24
- AREH.CA: score=19.2 buy_ready=True sector_rank=9 price=1.58 support=1.34 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=5711093.5 spike=0.16
- ARVA.CA: score=18.59 buy_ready=False sector_rank=9 price=11.03 support=10.1 resistance=13.1 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=37.7 liquidity=7093028.84 spike=0.29
- ASCM.CA: score=23.49 buy_ready=True sector_rank=9 price=60.72 support=54.07 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=57.4 liquidity=18699558.0 spike=0.19
- ASPI.CA: score=12.84 buy_ready=False sector_rank=9 price=0.32 support=0.3 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=54.64 liquidity=1351294.0 spike=0.02
- ATLC.CA: score=14.65 buy_ready=True sector_rank=13 price=5.25 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=65.73 liquidity=1322302.0 spike=0.2
- ATQA.CA: score=16.97 buy_ready=False sector_rank=21 price=9.57 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=9212082.0 spike=0.26
- AXPH.CA: score=18.44 buy_ready=True sector_rank=9 price=1233.3 support=1073.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=67.81 liquidity=2711681.75 spike=1.12
- BINV.CA: score=16.51 buy_ready=True sector_rank=5 price=47.79 support=44.02 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=55.41 liquidity=2530726.0 spike=0.31
- BIOC.CA: score=14.13 buy_ready=False sector_rank=9 price=72.63 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=57.06 liquidity=635288.81 spike=0.25
- BTFH.CA: score=17.32 buy_ready=False sector_rank=13 price=2.99 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=78062920.0 spike=0.42
- CAED.CA: score=14.26 buy_ready=False sector_rank=9 price=71.38 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=60.54 liquidity=763520.44 spike=0.16
- CANA.CA: score=11.63 buy_ready=False sector_rank=8 price=35.95 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=49.64 liquidity=1062795.75 spike=0.09
- CCAP.CA: score=23.98 buy_ready=True sector_rank=5 price=5.17 support=4.65 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=408325920.0 spike=0.61
- CCRS.CA: score=13.35 buy_ready=False sector_rank=9 price=2.35 support=2.18 resistance=2.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=48.39 liquidity=1860723.5 spike=0.13
- CEFM.CA: score=9.27 buy_ready=False sector_rank=9 price=102.59 support=95.75 resistance=109.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=39.12 liquidity=774089.25 spike=0.48
- CERA.CA: score=14.39 buy_ready=True sector_rank=9 price=1.23 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=1898794.5 spike=0.11
- CFGH.CA: score=7.67 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=1 July 01:14 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=175361.52 spike=24.69
- CICH.CA: score=13.11 buy_ready=False sector_rank=13 price=11.96 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=62.28 liquidity=783625.5 spike=0.26
- CIEB.CA: score=18.27 buy_ready=True sector_rank=8 price=24.51 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=61.07 liquidity=4697695.0 spike=0.72
- CIRA.CA: score=17.39 buy_ready=False sector_rank=3 price=28.57 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=1989260.13 spike=0.11
- CLHO.CA: score=16.17 buy_ready=True sector_rank=10 price=16.4 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=2712068.0 spike=0.07
- CNFN.CA: score=16.96 buy_ready=True sector_rank=13 price=4.79 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=64.08 liquidity=1635383.38 spike=0.04
- COMI.CA: score=18.57 buy_ready=False sector_rank=8 price=129.31 support=126.21 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=38.54 liquidity=57881044.0 spike=0.11
- COPR.CA: score=13.19 buy_ready=False sector_rank=9 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=50.77 liquidity=2701809.75 spike=0.11
- COSG.CA: score=21.49 buy_ready=False sector_rank=9 price=1.58 support=1.47 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=23202342.0 spike=0.43
- CPCI.CA: score=13.8 buy_ready=False sector_rank=9 price=401.51 support=350.07 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=88.6 liquidity=1309930.88 spike=0.45
- CSAG.CA: score=17.01 buy_ready=False sector_rank=7 price=32.52 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=87.5 liquidity=4347276.0 spike=0.25
- DAPH.CA: score=13.92 buy_ready=False sector_rank=9 price=82.5 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=65.48 liquidity=427721.56 spike=0.04
- DEIN.CA: score=9.49 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.66 buy_ready=False sector_rank=15 price=27.19 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=83.47 liquidity=1373467.5 spike=0.33
- DSCW.CA: score=10.97 buy_ready=False sector_rank=9 price=1.74 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=3477090.25 spike=0.1
- DTPP.CA: score=13.49 buy_ready=False sector_rank=9 price=222.54 support=212.22 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=91742024.0 spike=7.63
- EALR.CA: score=9.35 buy_ready=False sector_rank=9 price=346.32 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=855274.06 spike=0.31
- EASB.CA: score=13.87 buy_ready=False sector_rank=9 price=7.64 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=73.02 liquidity=2375408.25 spike=0.17
- EAST.CA: score=7.7 buy_ready=False sector_rank=15 price=37.43 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=44.58 liquidity=415594.53 spike=0.01
- EBSC.CA: score=30.25 buy_ready=False sector_rank=9 price=2.03 support=1.71 resistance=2.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=13022581.0 spike=3.38
- ECAP.CA: score=14.35 buy_ready=False sector_rank=9 price=33.15 support=30.0 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=57.61 liquidity=858386.31 spike=0.09
- EDFM.CA: score=4.48 buy_ready=False sector_rank=9 price=318.97 support=320.29 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:09 AM market time freshness=DELAYED_CURRENT RSI=17.77 liquidity=669022.75 spike=1.16
- EEII.CA: score=25.59 buy_ready=True sector_rank=9 price=2.6 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=66.04 liquidity=30470772.0 spike=2.05
- EFIC.CA: score=1.1 buy_ready=False sector_rank=21 price=186.35 support=180.02 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=18.33 liquidity=344504.56 spike=0.15
- EFID.CA: score=12.03 buy_ready=False sector_rank=15 price=27.41 support=25.5 resistance=29.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=48.62 liquidity=3742201.75 spike=0.05
- EFIH.CA: score=17.38 buy_ready=False sector_rank=20 price=21.13 support=20.0 resistance=22.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=56.4 liquidity=8494034.0 spike=0.23
- EGAL.CA: score=6.51 buy_ready=False sector_rank=21 price=287.0 support=272.28 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=30.92 liquidity=4752487.5 spike=0.08
- EGAS.CA: score=14.07 buy_ready=False sector_rank=17 price=49.63 support=46.51 resistance=55.0 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=45.69 liquidity=3042716.11 spike=0.48
- EGBE.CA: score=15.58 buy_ready=False sector_rank=8 price=0.46 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=7603.8 spike=0.1
- EGCH.CA: score=11.76 buy_ready=False sector_rank=21 price=12.58 support=12.13 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=28.44 liquidity=12877155.0 spike=0.25
- EGSA.CA: score=10.78 buy_ready=False sector_rank=18 price=8.75 support=8.55 resistance=9.09 source=Yahoo Finance as_of=2026-07-01T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=0.0 spike=0.0
- EGTS.CA: score=23.44 buy_ready=True sector_rank=11 price=18.5 support=15.1 resistance=21.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=12400453.0 spike=0.15
- EHDR.CA: score=15.03 buy_ready=False sector_rank=9 price=2.53 support=2.37 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=3534058.25 spike=0.06
- EKHO.CA: score=10.03 buy_ready=False sector_rank=17 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-01T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=9.73 buy_ready=False sector_rank=16 price=2.11 support=2.04 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=2609845.75 spike=0.15
- ELKA.CA: score=22.49 buy_ready=True sector_rank=9 price=1.38 support=1.19 resistance=1.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=14383762.0 spike=0.29
- ELNA.CA: score=7.72 buy_ready=False sector_rank=9 price=37.81 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=41.05 liquidity=225687.9 spike=0.52
- ELSH.CA: score=10.96 buy_ready=False sector_rank=9 price=11.84 support=11.1 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=29.7 liquidity=4469092.0 spike=0.02
- ELWA.CA: score=4.68 buy_ready=False sector_rank=9 price=1.95 support=1.94 resistance=2.22 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=34.09 liquidity=1185028.68 spike=0.62
- EMFD.CA: score=20.09 buy_ready=False sector_rank=11 price=11.62 support=11.11 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=54.82 liquidity=8653473.0 spike=0.03
- ENGC.CA: score=14.45 buy_ready=False sector_rank=9 price=36.88 support=33.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=66.52 liquidity=961376.56 spike=0.07
- EOSB.CA: score=15.6 buy_ready=False sector_rank=9 price=1.48 support=1.4 resistance=1.55 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=111155.4 spike=0.95
- EPCO.CA: score=9.04 buy_ready=False sector_rank=9 price=8.75 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=41.78 liquidity=546671.44 spike=0.07
- EPPK.CA: score=13.08 buy_ready=False sector_rank=9 price=14.19 support=11.67 resistance=14.33 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=83.89 liquidity=590346.55 spike=0.68
- ETEL.CA: score=13.99 buy_ready=False sector_rank=18 price=93.17 support=89.01 resistance=96.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=59.3 liquidity=4212610.5 spike=0.06
- ETRS.CA: score=21.49 buy_ready=True sector_rank=9 price=10.74 support=8.75 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=65.67 liquidity=26480042.0 spike=0.31
- EXPA.CA: score=20.6 buy_ready=True sector_rank=8 price=18.69 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=7030037.5 spike=0.23
- FAIT.CA: score=12.13 buy_ready=False sector_rank=8 price=36.56 support=35.01 resistance=38.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=63.81 liquidity=558913.38 spike=0.19
- FAITA.CA: score=9.95 buy_ready=False sector_rank=8 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=59331.12 spike=1.66
- FERC.CA: score=3.35 buy_ready=False sector_rank=21 price=73.55 support=72.75 resistance=80.83 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=26.69 liquidity=2597491.91 spike=0.78
- FWRY.CA: score=16.88 buy_ready=False sector_rank=20 price=18.6 support=17.71 resistance=20.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=46619692.0 spike=0.2
- GBCO.CA: score=24.4 buy_ready=False sector_rank=1 price=31.7 support=25.25 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=80.91 liquidity=10345800.0 spike=0.11
- GDWA.CA: score=9.03 buy_ready=False sector_rank=9 price=0.76 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=1542754.12 spike=0.11
- GGCC.CA: score=17.04 buy_ready=False sector_rank=9 price=0.49 support=0.4 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=97.89 liquidity=5548743.5 spike=0.4
- GIHD.CA: score=15.55 buy_ready=True sector_rank=9 price=42.51 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=63.77 liquidity=2060148.38 spike=0.24
- GMCI.CA: score=19.87 buy_ready=False sector_rank=9 price=1.95 support=1.66 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:07 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=1375044.25 spike=2.5
- GRCA.CA: score=4.8 buy_ready=False sector_rank=9 price=52.29 support=50.2 resistance=60.5 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=32.39 liquidity=1310701.16 spike=0.36
- GSSC.CA: score=11.02 buy_ready=False sector_rank=9 price=249.49 support=228.1 resistance=255.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=40.57 liquidity=525564.25 spike=0.19
- GTWL.CA: score=10.01 buy_ready=False sector_rank=9 price=98.0 support=85.0 resistance=99.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72728584.0 spike=1.76
- HDBK.CA: score=22.57 buy_ready=False sector_rank=8 price=168.77 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=79.45 liquidity=26317910.0 spike=0.84
- HELI.CA: score=21.44 buy_ready=False sector_rank=11 price=6.46 support=6.28 resistance=6.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=11455179.0 spike=0.11
- HRHO.CA: score=18.42 buy_ready=False sector_rank=13 price=26.83 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=9092416.0 spike=0.07
- ICID.CA: score=13.93 buy_ready=False sector_rank=9 price=8.01 support=5.65 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=67.35 liquidity=439859.84 spike=0.03
- IDRE.CA: score=20.21 buy_ready=True sector_rank=9 price=45.06 support=41.1 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=59.73 liquidity=6716507.5 spike=0.54
- IFAP.CA: score=13.05 buy_ready=False sector_rank=12 price=19.44 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=60.39 liquidity=630392.13 spike=0.1
- INFI.CA: score=8.15 buy_ready=False sector_rank=9 price=93.9 support=88.51 resistance=104.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=37.63 liquidity=660429.5 spike=0.11
- IRON.CA: score=12.65 buy_ready=False sector_rank=21 price=32.24 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=50.75 liquidity=2891082.75 spike=0.37
- ISMA.CA: score=10.04 buy_ready=False sector_rank=9 price=28.19 support=26.83 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=14.58 liquidity=3550960.0 spike=0.11
- ISMQ.CA: score=23.76 buy_ready=False sector_rank=21 price=9.58 support=7.56 resistance=9.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=71.48 liquidity=55669348.0 spike=0.45
- ISPH.CA: score=18.46 buy_ready=False sector_rank=10 price=11.67 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=52.6 liquidity=12906154.0 spike=0.12
- JUFO.CA: score=13.64 buy_ready=False sector_rank=15 price=29.96 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=55.68 liquidity=2347510.0 spike=0.07
- KABO.CA: score=22.79 buy_ready=True sector_rank=6 price=6.38 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=7100151.5 spike=0.45
- KWIN.CA: score=9.37 buy_ready=False sector_rank=9 price=67.64 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=41.34 liquidity=1879943.88 spike=0.16
- KZPC.CA: score=3.5 buy_ready=False sector_rank=9 price=8.54 support=8.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=11.85 liquidity=1007002.06 spike=0.16
- LCSW.CA: score=25.29 buy_ready=True sector_rank=14 price=28.6 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=13674715.0 spike=0.39
- LUTS.CA: score=19.24 buy_ready=True sector_rank=9 price=0.75 support=0.57 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=62.46 liquidity=5745568.0 spike=0.12
- MAAL.CA: score=18.74 buy_ready=False sector_rank=9 price=7.48 support=5.46 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=99.39 liquidity=6248955.5 spike=0.37
- MASR.CA: score=23.49 buy_ready=True sector_rank=9 price=7.59 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=68.87 liquidity=37993632.0 spike=0.58
- MBSC.CA: score=10.69 buy_ready=False sector_rank=14 price=242.46 support=222.66 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:04 AM market time freshness=DELAYED_CURRENT RSI=38.68 liquidity=2403250.5 spike=0.08
- MCQE.CA: score=13.98 buy_ready=False sector_rank=14 price=173.14 support=166.66 resistance=196.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=45.82 liquidity=5694471.5 spike=0.42
- MCRO.CA: score=16.17 buy_ready=False sector_rank=9 price=1.23 support=1.17 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8680512.0 spike=0.27
- MENA.CA: score=12.37 buy_ready=False sector_rank=11 price=6.92 support=6.41 resistance=7.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=65.82 liquidity=932508.75 spike=0.07
- MEPA.CA: score=11.01 buy_ready=False sector_rank=9 price=1.63 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=7516388.0 spike=0.68
- MFPC.CA: score=11.76 buy_ready=False sector_rank=21 price=36.23 support=34.22 resistance=43.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=26.48 liquidity=16035537.0 spike=0.2
- MFSC.CA: score=12.37 buy_ready=False sector_rank=9 price=50.34 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=66.65 liquidity=876669.06 spike=0.11
- MHOT.CA: score=17.36 buy_ready=False sector_rank=4 price=34.84 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=74.69 liquidity=2960242.5 spike=0.17
- MICH.CA: score=15.13 buy_ready=True sector_rank=9 price=38.05 support=34.0 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=56.4 liquidity=1639099.5 spike=0.11
- MILS.CA: score=9.5 buy_ready=False sector_rank=9 price=131.8 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=34.87 liquidity=3007393.5 spike=0.33
- MIPH.CA: score=8.81 buy_ready=False sector_rank=10 price=658.51 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=51.94 liquidity=358874.66 spike=0.21
- MOED.CA: score=9.98 buy_ready=False sector_rank=9 price=0.68 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=55.97 liquidity=486168.41 spike=0.05
- MOIL.CA: score=19.04 buy_ready=True sector_rank=17 price=0.5 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=1012750.31 spike=5.11
- MOIN.CA: score=3.04 buy_ready=False sector_rank=9 price=23.73 support=22.6 resistance=25.66 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=33.42 liquidity=544864.52 spike=0.78
- MOSC.CA: score=15.54 buy_ready=True sector_rank=9 price=274.43 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=56.02 liquidity=2046946.25 spike=0.22
- MPCI.CA: score=23.49 buy_ready=True sector_rank=9 price=249.74 support=207.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=68.36 liquidity=25976398.0 spike=0.26
- MPCO.CA: score=16.84 buy_ready=False sector_rank=12 price=1.84 support=1.66 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=5427666.0 spike=0.05
- MPRC.CA: score=20.8 buy_ready=False sector_rank=9 price=38.41 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=91.85 liquidity=8307404.5 spike=0.19
- MTIE.CA: score=27.4 buy_ready=False sector_rank=1 price=9.41 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=72.03 liquidity=10808488.0 spike=0.61
- NAHO.CA: score=9.5 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=6760.0 spike=0.22
- NCCW.CA: score=14.36 buy_ready=False sector_rank=9 price=6.24 support=5.3 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=2871642.75 spike=0.08
- NEDA.CA: score=10.07 buy_ready=False sector_rank=9 price=2.75 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=500725.5 spike=1.54
- NHPS.CA: score=26.65 buy_ready=True sector_rank=9 price=68.09 support=61.55 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=63.93 liquidity=9162629.0 spike=0.97
- NINH.CA: score=9.34 buy_ready=False sector_rank=9 price=18.17 support=16.8 resistance=18.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=77.48 liquidity=1850393.0 spike=0.3
- NIPH.CA: score=25.46 buy_ready=False sector_rank=10 price=178.0 support=157.01 resistance=181.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=73.39 liquidity=78461424.0 spike=0.98
- OBRI.CA: score=13.45 buy_ready=False sector_rank=9 price=37.63 support=36.39 resistance=38.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63114992.0 spike=3.48
- OCDI.CA: score=19.29 buy_ready=False sector_rank=11 price=25.25 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=85.48 liquidity=8854591.0 spike=0.11
- OCPH.CA: score=16.76 buy_ready=True sector_rank=9 price=358.02 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=61.88 liquidity=1271359.0 spike=0.19
- ODIN.CA: score=15.86 buy_ready=True sector_rank=9 price=2.23 support=2.01 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=67.44 liquidity=4367855.0 spike=0.4
- OFH.CA: score=20.49 buy_ready=True sector_rank=9 price=0.62 support=0.57 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=15564526.0 spike=0.82
- OIH.CA: score=13.86 buy_ready=False sector_rank=5 price=1.41 support=1.33 resistance=1.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=2884499.75 spike=0.04
- OLFI.CA: score=17.11 buy_ready=True sector_rank=15 price=22.14 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=52.82 liquidity=1821342.38 spike=0.08
- ORAS.CA: score=7.6 buy_ready=False sector_rank=19 price=725.72 support=722.0 resistance=730.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16500137.0 spike=1.0
- ORHD.CA: score=23.44 buy_ready=True sector_rank=11 price=38.09 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=61.78 liquidity=18318420.0 spike=0.11
- ORWE.CA: score=15.35 buy_ready=False sector_rank=6 price=22.5 support=21.95 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=35.56 liquidity=3657228.5 spike=0.11
- PHAR.CA: score=19.54 buy_ready=True sector_rank=10 price=88.51 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=61.58 liquidity=4085312.5 spike=0.11
- PHDC.CA: score=21.44 buy_ready=False sector_rank=11 price=14.62 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=52916464.0 spike=0.15
- PHTV.CA: score=15.01 buy_ready=False sector_rank=9 price=272.72 support=201.55 resistance=277.98 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=97.6 liquidity=2518841.93 spike=0.22
- POUL.CA: score=17.52 buy_ready=True sector_rank=15 price=38.04 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=62.65 liquidity=2236207.75 spike=0.07
- PRCL.CA: score=22.29 buy_ready=False sector_rank=14 price=32.95 support=23.25 resistance=33.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=81.79 liquidity=20410014.0 spike=0.46
- PRDC.CA: score=19.4 buy_ready=True sector_rank=11 price=7.78 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=69.83 liquidity=7962654.0 spike=0.06
- PRMH.CA: score=15.34 buy_ready=False sector_rank=9 price=2.6 support=2.34 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=3852049.0 spike=0.12
- RACC.CA: score=15.35 buy_ready=True sector_rank=9 price=9.91 support=9.36 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=59.22 liquidity=1857498.13 spike=0.23
- RAKT.CA: score=2.65 buy_ready=False sector_rank=9 price=21.67 support=21.4 resistance=24.07 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=29.78 liquidity=157757.6 spike=0.62
- RAYA.CA: score=26.4 buy_ready=True sector_rank=2 price=7.84 support=6.7 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=33155812.0 spike=0.39
- RMDA.CA: score=15.2 buy_ready=False sector_rank=10 price=5.0 support=4.81 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=52.56 liquidity=3742122.0 spike=0.05
- ROTO.CA: score=16.42 buy_ready=False sector_rank=9 price=41.72 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=74.55 liquidity=2928533.75 spike=0.09
- RREI.CA: score=12.8 buy_ready=False sector_rank=9 price=3.53 support=3.34 resistance=3.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=4304142.0 spike=0.26
- RTVC.CA: score=12.08 buy_ready=False sector_rank=9 price=3.84 support=3.55 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=1590642.88 spike=0.3
- RUBX.CA: score=13.49 buy_ready=False sector_rank=9 price=13.42 support=12.7 resistance=14.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106712864.0 spike=3.73
- SAUD.CA: score=9.79 buy_ready=False sector_rank=8 price=21.23 support=19.99 resistance=22.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=45.84 liquidity=1219669.38 spike=0.15
- SCEM.CA: score=9.07 buy_ready=False sector_rank=14 price=66.89 support=63.61 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24038130.0 spike=1.39
- SCFM.CA: score=11.18 buy_ready=False sector_rank=9 price=241.07 support=226.5 resistance=269.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=2684217.75 spike=0.65
- SCTS.CA: score=20.6 buy_ready=True sector_rank=3 price=622.97 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=61.59 liquidity=1198086.88 spike=0.27
- SDTI.CA: score=15.03 buy_ready=False sector_rank=9 price=46.44 support=45.0 resistance=49.5 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=47.68 liquidity=3533480.18 spike=0.42
- SEIG.CA: score=12.8 buy_ready=False sector_rank=9 price=192.45 support=180.0 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:08 AM market time freshness=DELAYED_CURRENT RSI=84.07 liquidity=305808.44 spike=0.07
- SIPC.CA: score=9.54 buy_ready=False sector_rank=9 price=3.4 support=3.25 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=1050010.0 spike=0.09
- SKPC.CA: score=12.23 buy_ready=False sector_rank=21 price=16.0 support=15.58 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=6475184.0 spike=0.2
- SMFR.CA: score=9.18 buy_ready=False sector_rank=9 price=196.99 support=187.01 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=48.76 liquidity=688629.0 spike=0.35
- SNFC.CA: score=9.9 buy_ready=False sector_rank=9 price=11.92 support=11.68 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=43.36 liquidity=1411929.13 spike=0.09
- SPIN.CA: score=19.47 buy_ready=True sector_rank=6 price=14.46 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=56.99 liquidity=3780012.25 spike=0.61
- SPMD.CA: score=16.97 buy_ready=True sector_rank=9 price=0.43 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=3482250.0 spike=0.17
- SUGR.CA: score=8.57 buy_ready=False sector_rank=15 price=47.17 support=45.31 resistance=51.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=35.62 liquidity=1278022.13 spike=0.18
- SVCE.CA: score=25.49 buy_ready=False sector_rank=9 price=9.64 support=8.11 resistance=9.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=70.74 liquidity=42909824.0 spike=0.64
- SWDY.CA: score=15.67 buy_ready=True sector_rank=16 price=88.03 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=65.37 liquidity=4549649.5 spike=0.27
- TALM.CA: score=15.91 buy_ready=False sector_rank=3 price=15.99 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=42.99 liquidity=505266.16 spike=0.07
- TMGH.CA: score=23.44 buy_ready=True sector_rank=11 price=96.47 support=92.1 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=94591024.0 spike=0.27
- TRTO.CA: score=9.49 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.03 spike=0.0
- UEFM.CA: score=11.98 buy_ready=False sector_rank=9 price=477.14 support=460.0 resistance=505.0 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=56.06 liquidity=489545.66 spike=0.55
- UEGC.CA: score=23.49 buy_ready=True sector_rank=9 price=1.5 support=1.33 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=18078710.0 spike=0.74
- UNIP.CA: score=14.45 buy_ready=False sector_rank=9 price=0.33 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=55.06 liquidity=953489.62 spike=0.04
- UNIT.CA: score=12.28 buy_ready=False sector_rank=11 price=13.26 support=12.0 resistance=14.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=35.34 liquidity=847526.5 spike=0.13
- WCDF.CA: score=9.91 buy_ready=False sector_rank=9 price=506.06 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=33.08 liquidity=1416461.93 spike=4.15
- WKOL.CA: score=4.31 buy_ready=False sector_rank=9 price=281.12 support=273.1 resistance=312.0 source=Yahoo Finance as_of=2026-06-30T21:00:00+00:00 freshness=FRESH RSI=29.23 liquidity=817215.83 spike=0.38
- ZEOT.CA: score=21.49 buy_ready=True sector_rank=9 price=10.98 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=69.29 liquidity=11216417.0 spike=0.33
- ZMID.CA: score=23.44 buy_ready=True sector_rank=11 price=6.57 support=5.96 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=66.19 liquidity=35886944.0 spike=0.16

## Backtesting Lite
- EBSC.CA: 180d return=69.35%, max drawdown=-23.41%, MA20>MA50 days last20=20, as_of=2026-06-30T21:00:00+00:00
- MTIE.CA: 180d return=29.68%, max drawdown=-20.49%, MA20>MA50 days last20=20, as_of=2026-06-30T21:00:00+00:00
- NHPS.CA: 180d return=5.36%, max drawdown=-40.18%, MA20>MA50 days last20=11, as_of=2026-06-30T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EBSC.CA: status=RECENT_ACCEPTED latest=2026-06-17 age_days=18 sources=3 expected=Osool ESB Securities Brokerage summary=Osool ESB Securities Brokerage (EBSC.CA) has reported its financial results for the period ending December 31, 2025, with a net profit of EGP 16,774,936. The company's revenue in 2025 was EGP 26.75 million, and earnings increased by 21.88%. Recent corporate actions include Board of Directors' meetings and disclosures regarding shareholder structure.
  - Osool ESB Securities Brokerage (EBSC.CA) Reports Its Financial Results for The Period ending 31/12/2025 (Reported 26/02/2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmg7hJOfP4tV3Dw7ufqj7xDG0F-PNXvciZ2fUMbVx5PQghm_ab8TnC46A557bYutpjs97ReOhSbq11e0Ypu5H7r1k_kWZUxwaMxYdh_BJVIEhDIFswlJXOAfkfG0bvtAqv7mWrSzaJAXgGRLvgWaP1nQ==
  - Osool ESB Securities Brokerage (EGX:EBSC) Financial Performance in 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGg01yRKy30-3Jq_wo3iKqpXW_KDor6knJsaBMFhOmdrgEjTF83eJei8zZHRSIW4Vmn6clmMvnXABinzm1ZE5GLhTi1VHPc_7Ahgk_ttxjCzgH9oxPNj_oZcDseF8maLb6tEQ==
  - Release from Osool Brokerage Securities Co. (EBSC.CA) Regarding a News Published on a Website (17 June 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbHSLr-Fn_mhfOmMy2DoLZ8RgTF4auQSv5A-H9eMY69KlV7YURaCEbHFk4Y9j_73oiNU6wif6yPNQTXbA3rAUSXpLB_29KXmLyw9ev2RUKB1lKFlJVFhMqn9AyAxER1mY8nQwAE4cyBdkOItvJTeI=
- MTIE.CA: status=RECENT_ACCEPTED latest=2026-09-02 age_days=0 sources=3 expected=MM Group For Industry and International Trade summary=MM Group For Industry and International Trade (MTIE.CA) is scheduled to release its next earnings report on September 2, 2026. The company's net income for the last quarter was EGP 440.81 million, and its stock price reached an all-time high of EGP 10.38 on May 3, 2026. Recent financial performance shows an increase in net income and revenue in the latest quarter.
  - MM Group for Industry & International Trade Actuals & Estimates (EGX:MTIE) - Next Earnings Report (Sep 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNCz4S-GIchOs8kbxTYpGL-Hgs-9GHjU9SyZ1XAdVLCxKelxOmXJ3saxqLtolYa0gOh2kCIoOJtncFUajuKJ0fvcKEk1CmrP61OaHVcdm5dvavpkqSPzuPpUWNCKHKo87fUKjgB3GU-5fphsBpYW-SLNjuL0d25DXP2GQAQpVL5FZmSZps
  - MM Group for Industry & International Trade Actuals & Estimates (EGX:MTIE) - Net Income and All-Time High (May 3, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNCz4S-GIchOs8kbxTYpGL-Hgs-9GHjU9SyZ1XAdVLCxKelxOmXJ3saxqLtolYa0gOh2kCIoOJtncFUajuKJ0fvcKEk1CmrP61OaHVcdm5dvavpkqSPzuPpUWNCKHKo87fUKjgB3GU-5fphsBpYW-SLNjuL0d25DXP2GQAQpVL5FZmSZps
  - EGX:MTIE Financials | MM Group for Industry - Latest Quarter Performance: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOTcSCHagW0YlheDeqyX8KYBtbUv7wWgoLlKhjxxO8RK_3udApGGVjVCSkIEOMts0L01_mp4LoOhbwTGR5FeH2xy6wIRwhp_o60mHspfY4ZmaPe96wQ0qXlnCwq_esV9mynqd82jyGFHY6JQUc4Yxkv78PYoBBpSsm5ML5v_s4s2LfwQ==
- NHPS.CA: status=RECENT_ACCEPTED latest=2026-12-29 age_days=0 sources=3 expected=National Company for Housing Professional Syndicates SAE summary=National Company for Housing Professional Syndicates SAE (NHPS.CA) announced an annual dividend of EGP 7.50 per share, payable on December 29, 2025, with an ex-date of December 25, 2025. Eligible shareholders for an upcoming dividend of EGP 7.50 must have bought the stock before June 25, 2026, with a payment date of December 29, 2026. The company's equityholders approved EGP 3.5/share dividends for 2025.
  - National Company for Housing Professional Syndicates SAE announces Annual dividend, payable on December 29, 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmLIB32LZAz7xVXAiPYCNnYFEV70an4qtlFtB5h9GD-zHJE499yHCHi0VBoupLIO0SFrHxeoFvY6XrCjaB-qUr97CzEb1fBR08s5Bw5nrmQXsXPtLGEiDMDEBH3_c6LhCwuRkfNJWjyXs6q0ycpXwcW0Zm66O_hvfY-8dOqPO2z4wp7rJ-bK32H-B_NkzakbBiGG_RltTOKXSoUwphd9nSSyQ_qy1GbtvxjMXLqdsLcebPjzYRcBP-h8v64r6UHbtVz4tD4FlLYQ0R
  - National Company for Housing Professional Syndicates SAE (CASE:NHPS) - Upcoming Dividend (June 27 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmLIB32LZAz7xVXAiPYCNnYFEV70an4qtlFtB5h9GD-zHJE499yHCHi0VBoupLIO0SFrHxeoFvY6XrCjaB-qUr97CzEb1fBR08s5Bw5nrmQXsXPtLGEiDMDEBH3_c6LhCwuRkfNJWjyXs6q0ycpXwcW0Zm66O_hvfY-8dOqPO2z4wp7rJ-bK32H-B_NkzakbBiGG_RltTOKXSoUwphd9nSSyQ_qy1GbtvxjMXLqdsLcebPjzYRcBP-h8v64r6UHbtVz4tD4FlLYQ0R
  - NCH El-Watania's equityholders approve EGP 3.5/shr dividends for 2025 (General Assembly): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6ucT7nO5Wcagx-6JXUXAv0nRwWWaA5Om9eADo_JVJJUmzlEAu7y_I6hpvmkEWbfwydZTO54NN0YVP1JVgQIvKVagSh8s71XAdPTEbLqm1wZjxYE0_WcONB79YV5NJtPmZHNaS0fRaeUH43eXyuw==
- RAYA.CA: status=RECENT_ACCEPTED latest=2026-06-09 age_days=26 sources=3 expected=Raya Holding summary=Raya Holding (RAYA.CA) reported consolidated profits surging in 2025, with revenues reaching EGP 63.8 billion. The company's revenue in 2025 increased by 41.47% to EGP 63.83 billion, and earnings rose by 53.29% to EGP 2.59 billion. Recent announcements include the signing of an MOU and financial results for Q1 2026.
  - Raya Holding's consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBOhk-UNxKnpN_uevOT77nqL7qEEmAsBy5DunxPDTJw1mc1mhjem9MS_AC3_44XT5QaFod60-k2OhGVRA_zrTveuidKapha9FRR9Bh1YIx5Q7_4BM5uKivF1Se0UHVc3CM_e0t0bTCSYZuo_YHslA==
  - Raya Holding Company for Financial Investments (S.A.E) (EGX:RAYA) Financial Performance in 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG24HmIHsbdYSLGHJYDpz3_zivlJhqo1QvsFlVpIAErzKg52Xq25aw6dr1a2PNJrhgl31fD6I6zlbBVUdBlmBpU422UF_uptMj2m_rZ-7EmkrDqcqQdbQr11W8deGfXHWC-6A==
  - Release from Raya Holding For Financial Investments (RAYA.CA) Concerning the Signing of MOU (9 June 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBOhk-UNxKnpN_uevOT77nqL7qEEmAsBy5DunxPDTJw1mc1mhjem9MS_AC3_44XT5QaFod60-k2OhGVRA_zrTveuidKapha9FRR9Bh1YIx5Q7_4BM5uKivF1Se0UHVc3CM_e0t0bTCSYZuo_YHslA==
- EEII.CA: status=RECENT_ACCEPTED latest=2026-06-27 age_days=8 sources=3 expected=Arab Engineering Industries summary=Arab Engineering Industries (EEII.CA) reported a decrease in revenue by -16.19% to EGP 200.18 million in 2025, with earnings decreasing by -84.02% to EGP 5.76 million. The company's Q1 profit for 2026 was EGP 1.6 million. Shareholders approved a capital increase in January 2026. Recent corporate events include an Annual General Meeting on June 27, 2026.
  - Arab Engineering Industries (EGX:EEII) Financial Performance in 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6MoNlHZOXLpsdr6Wv-BTu5U-AKRDyF4SVCruxTsgrHMvODpfaHhaHrdJhR4CsRWdMzZbaokw2Zrh_olyqv0firet695fEFoY9pWVj5y5MqMfTBFoUQA6Vs0WJwuoZrO_lLg==
  - Arab Engineering Industries Q1 profit EGP 1.6 mln (May 25): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSO_66KQINayWykWPR_2UCtr2b1GZKBdEBYK5zfMK2clGgKixK0sE8pHY1DQbSyq3pxiENPJFY-RLcKwrIY6LDycArvHharj-n-qIZQpA8qXzKb-GPkpeJGd-TR50L8lhTxP5ag8ygX3Fw_g3P_-8xy4mNnx9PfC6kc9ijS9g-ZAEeXbGexk0==
  - Arab Engineering Industries Reports Earnings Results for the Full Year Ended December 31, 2025 (May 10): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSO_66KQINayWykWPR_2UCtr2b1GZKBdEBYK5zfMK2clGgKixK0sE8pHY1DQbSyq3pxiENPJFY-RLcKwrIY6LDycArvHharj-n-qIZQpA8qXzKb-GPkpeJGd-TR50L8lhTxP5ag8ygX3Fw_g3P_-8xy4mNnx9PfC6kc9ijS9g-ZAEeXbGexk0==
- SVCE.CA: status=RECENT_ACCEPTED latest=2026-05-06 age_days=60 sources=2 expected=South Valley Cement Company summary=South Valley Cement Company (SVCE.CA) faced a EGP 5000 penalty from the EGX Listing Committee on May 6, 2026, for failing to provide financial statements for the fiscal year ending December 31, 2025. The company's revenue for the trailing twelve months ending September 30, 2025, was EGP 2,758 million.
  - South Valley Cement (SVCE.CA) - Listing Committee Decision (May 06 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESK-t1F72M2d_xv2LJd1RgF49UsIAEqO_8PD2OqhnCcT9-xsdQNcGP8I55mlMETEXKkPTgbMqEPBpbd-tdDKniFtgPlwnrFQXzAcppSTq5iHQBeEDUqiOuPRoXnMdQoVxBQ6Jy96m5pGxx9-HvcKr5LVg==
  - South Valley Cement Company (EGX:SVCE) Financials & Income Statement (as of Sep 30, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE4G558ephfl5mf0-PGozU1ZMk49AEoMeLkkXVgRIBqzrpNIDwtW25Za7tdcZx5sOFtcZOKlacsxo8r64j3yRtCu2amcFmGiHsERXEcullJbyUu-68bidrQhXlmQN-cx9QJcthYGaBXse_iEj8
- NIPH.CA: status=RECENT_ACCEPTED latest=2026-07-03 age_days=2 sources=3 expected=El Nile Pharmaceuticals summary=El Nile Pharmaceuticals (NIPH.CA) released its third-quarter 2026 earnings, showing a 71% increase in revenue to EGP 638.1 million and a 19% increase in net income to EGP 69.0 million compared to Q3 2025. For fiscal year 2025, revenue increased by 12.86% to EGP 1.29 billion, and earnings rose by 39.35% to EGP 125.73 million. The company also reported its financial results for the period from July 1, 2025, to March 31, 2026.
  - Third quarter 2026 earnings released (July 03 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3qT2Z5ZKk95CjmOhN36ldkloN06dfFhYe7LFSUchUqqZCAAbq03fuQ4U_eh4qrX4LKbyKae0-l1z_FiH4duxA6_GmAHdkTdOw1Q0X49eoNT1ErcldUr-QNhiJ2jjcJ8c8rfRR4r2ixynCTrEuvYiVucB6hAxU7j1Y20YXvs-hYyXFqHqyJk80Mbc3Br4P1ol_6T2-L0kFnhJvHYnrXoxk-vf26Mx_-n7y9DsfB2jYbLAaZMzh
  - EI- Nile Co. for Pharmaceuticals and Chemical Industries (EGX:NIPH) Financial Performance in fiscal year 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHusIUmK3RwUVtddoZV7C77xAlBznG6mHmxoYskknplzfgoecDiM30GRWcMzD9_p5lbUS2rfnx76_nW_yFdr5vjKWpGN8DYDR_aomhswCS9VMoQ2Kfw2N9WoF4_yCk-L0w-VA==
  - El-Nile Co. For Pharmaceuticals And Chemical Industries (NIPH.CA) - Central Auditing Organization Report (16 June 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9hfUDG77J4wfqy4IGhs4y9vSnZbuZiHVWWS2RhfkdeAw1xGG7BobyAbYWIqVCdxugdryEZ8rQyJhaZ71LmW-bI8KuXZiBmAovXW0U5XlnZ-9S1QVfQUhRvRX0r4ehvsMsP24f_Xw3KFvRiPWytNg==
- LCSW.CA: status=RECENT_ACCEPTED latest=2026-06-30 age_days=5 sources=3 expected=Lecico Egypt summary=Lecico Egypt (LCSW.CA) reported revenue of EGP 8.07 billion and profits of EGP 290.89 million in the last 12 months ending June 30, 2026, with earnings per share at 7.27. The stock price increased by 10.32% in the last 52 weeks. For 2025, revenue was EGP 7.80 billion, an increase of 17.44%. The company has released its Q1 2026 and FY 2025 results.
  - Lecico Egypt (S.A.E.) (EGX:LCSW) Statistics & Valuation Metrics - Income Statement (June 30 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNM5Nil5HvJZn4saotaf2FCZGAcX0ylX1zWdzbZsWmohX6CzW2QCFpoLoHOss21hHwm0YEA9AOcc-RzqQvg7DZr60oHJyWyYVNCbqfKrlVTYuKDUvXL_x-WFd_nFaCX0FnnQlNVz7LmCYm3aqN
  - Lecico Egypt (S.A.E.) (EGX:LCSW) Stock Price & Overview - Financial Performance in 2025: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFl7w2aOR6lNLZ6OieipR7LG4eyoyikeBCAegpYHJBAf3ctM6aEN5JY6owDg_Rgx8yzgIXLXl21v7_OLWKbQ425uh0INZjfs8X_69KQ3_erVVuhZ1r5ve40GPE_rsOilo7VAw==
  - Lecico Egypt (LCSW.CA) - AGM Minutes (Notarized) (29 April 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQGolkJAowL92rprbAW35pPRJUydorz3Q8CZDfkTSU9D9taV0iMOjrZFbMPzk6Cx8Ru3nN-KHfi8mSVqRKluxwWdHhBt8tpru5dcnGFCGj03gikZvsH1XM3M3MvJ3UKA_LaNaxKT-cb5qDXlgI4Cc=

## Warnings
- No blocking warnings.
