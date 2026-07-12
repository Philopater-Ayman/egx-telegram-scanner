# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-12T07:52:26.352033+00:00
Generated Cairo: 2026-07-12 10:52
Run timing: target 08:45 Cairo | generated Cairo 2026-07-12 10:52 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-12 10:48

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 68
- Data quality issues: 1
- Tradeable price/liquidity tickers: 183/189
- Top sector: Telecommunications

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, July 12
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 80.0% / above MA50 50.0%
- EGX70 regime: BULLISH / above MA20 84.62% / above MA50 76.92%
- Sector breadth: 57.14%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- CCAP.CA: liquidity=275010208.0 spike=0.42 score=27.9
- ZMID.CA: liquidity=223910848.0 spike=1.06 score=28.02
- ELSH.CA: liquidity=147732576.0 spike=0.81 score=29.9
- ASCM.CA: liquidity=63448752.0 spike=0.85 score=10.9
- PRMH.CA: liquidity=60435808.0 spike=2.21 score=13.32

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlights ALCN.CA as the top priority, followed by ELSH.CA and IDRE.CA. All three show price above the 20‑ and 50‑day moving averages, decent liquidity spikes, and bullish outlook scores. EGX30 is in a constructive phase while EGX70 is bullish, keeping the market in a BROAD_RISK_ON mode, but confidence remains low and short‑term uncertainty is noted.
- ALCN.CA leads with strong liquidity (3.6× spike), support at 25.51 EGP and resistance near 33.2 EGP; RSI ~53 suggests neutral momentum.
- ELSH.CA and IDRE.CA also sit above key MAs, but sector breadth is weaker and they sit farther from support, adding extra risk.
- EGX30/EGX70 breadth (≈80% above MA20) supports a bullish backdrop, yet low confidence and potential price‑action volatility keep risk mode elevated.

## Top Liquidity Spikes
- CFGH.CA: spike=26.0 liquidity=156409.78 outlook=WEAK_OR_RISKY score=4.21 buy_ready=False
- EDFM.CA: spike=5.38 liquidity=2612992.71 outlook=BULLISH_WATCH score=88.21 buy_ready=True
- EGSA.CA: spike=4.58 liquidity=24388.88 outlook=CONSTRUCTIVE score=52 buy_ready=False
- ELNA.CA: spike=4.02 liquidity=2126982.13 outlook=CONSTRUCTIVE score=67.21 buy_ready=False
- FAITA.CA: spike=3.82 liquidity=118680.92 outlook=WEAK_OR_RISKY score=22.82 buy_ready=False

## Sector Leaderboard
- #1 Telecommunications: score=12.32 5d=4.71% 20d=4.8% aboveMA50=100.0%
- #2 Technology & Distribution: score=10.78 5d=3.9% 20d=15.27% aboveMA50=100.0%
- #3 Transportation & Logistics: score=9.84 5d=0.72% 20d=3.64% aboveMA50=100.0%
- #4 Real Estate: score=8.52 5d=4.29% 20d=6.86% aboveMA50=92.31%
- #5 Fintech & Payments: score=8.44 5d=6.13% 20d=6.92% aboveMA50=50.0%
- #6 Investment Holding: score=7.38 5d=3.17% 20d=4.41% aboveMA50=66.67%
- #7 Agriculture & Food Production: score=7.13 5d=2.88% 20d=6.28% aboveMA50=50.0%
- #8 Automotive & Distribution: score=7.12 5d=-1.6% 20d=8.34% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY ALCN.CA
  - Entry: 29.91 | Take profit: 33.03 | Stop loss: 28.71
  - Confidence: LOW | score=33.9 | outlook=BULLISH_WATCH 100
  - Reason: BUY SETUP: ALCN.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 53.59, support 25.51, resistance 33.2, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY ELSH.CA
  - Entry: 14.62 | Take profit: 15.78 | Stop loss: 14.04
  - Confidence: LOW | score=29.9 | outlook=BULLISH_WATCH 74.21
  - Reason: BUY SETUP: ELSH.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 53.52, support 11.1, resistance 14.6, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY IDRE.CA
  - Entry: 47.0 | Take profit: 50.76 | Stop loss: 45.12
  - Confidence: LOW | score=29.7 | outlook=BULLISH_WATCH 90.21
  - Reason: BUY SETUP: IDRE.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 56.8, support 41.1, resistance 46.7, and evidence sources. Macro trend is Bullish; market regime is BROAD_RISK_ON; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ALCN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- CAED.CA: BULLISH_WATCH score=94.21 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- IDRE.CA: BULLISH_WATCH score=90.21 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EDFM.CA: BULLISH_WATCH score=88.21 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading
- EMFD.CA: BULLISH_WATCH score=84.52 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=84.52 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=84.44 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- BIOC.CA: BULLISH_WATCH score=84.21 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- ETEL.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- CSAG.CA: BULLISH_WATCH score=81.84 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- ALCN.CA: rank=33.9 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=29.91 support=25.51 resistance=33.2 liquidity=41620344.0
- ELSH.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=74.21 sector_rank=10 price=14.62 support=11.1 resistance=14.6 liquidity=147732576.0
- RREI.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=73.21 sector_rank=10 price=3.85 support=3.34 resistance=3.93 liquidity=10704982.0
- IDRE.CA: rank=29.7 outlook=BULLISH_WATCH outlook_score=90.21 sector_rank=10 price=47.0 support=41.1 resistance=46.7 liquidity=21329012.0
- CAED.CA: rank=28.13 outlook=BULLISH_WATCH outlook_score=94.21 sector_rank=10 price=72.19 support=67.21 resistance=78.4 liquidity=8885700.0
- PRDC.CA: rank=28.1 outlook=BULLISH_WATCH outlook_score=76.52 sector_rank=4 price=8.58 support=5.91 resistance=9.0 liquidity=8196891.5
- ZMID.CA: rank=28.02 outlook=BULLISH_WATCH outlook_score=77.52 sector_rank=4 price=7.02 support=6.03 resistance=6.96 liquidity=223910848.0
- TMGH.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=78.52 sector_rank=4 price=97.0 support=92.1 resistance=99.43 liquidity=14677391.0
- RAYA.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=72 sector_rank=2 price=8.06 support=6.7 resistance=8.28 liquidity=12180407.0
- CCAP.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=71.38 sector_rank=6 price=5.32 support=4.65 resistance=5.32 liquidity=275010208.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=21.59 buy_ready=True sector_rank=10 price=226.04 support=196.0 resistance=247.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=63.77 liquidity=3690713.0 spike=0.26
- ABUK.CA: score=23.79 buy_ready=False sector_rank=18 price=70.52 support=66.66 resistance=80.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=45.68 liquidity=18057712.0 spike=0.13
- ACAMD.CA: score=21.96 buy_ready=True sector_rank=10 price=2.35 support=2.14 resistance=2.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=4064313.0 spike=0.04
- ACGC.CA: score=18.93 buy_ready=True sector_rank=9 price=9.64 support=8.92 resistance=9.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=51.27 liquidity=3033011.0 spike=0.14
- ADCI.CA: score=17.51 buy_ready=False sector_rank=10 price=232.77 support=219.0 resistance=248.0 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=57.26 liquidity=3605141.83 spike=0.36
- ADIB.CA: score=24.72 buy_ready=True sector_rank=12 price=47.3 support=44.01 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=48.07 liquidity=6893237.5 spike=0.07
- ADPC.CA: score=21.19 buy_ready=True sector_rank=10 price=3.72 support=3.32 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=55.04 liquidity=3286894.75 spike=0.22
- AFDI.CA: score=23.51 buy_ready=True sector_rank=10 price=47.96 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=60.67 liquidity=5606327.5 spike=0.46
- AFMC.CA: score=19.44 buy_ready=True sector_rank=10 price=74.85 support=66.0 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=1540400.75 spike=0.48
- AJWA.CA: score=23.42 buy_ready=True sector_rank=10 price=179.08 support=144.0 resistance=190.0 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=45.46 liquidity=7519748.36 spike=0.46
- ALCN.CA: score=33.9 buy_ready=True sector_rank=3 price=29.91 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=53.59 liquidity=41620344.0 spike=3.63
- ALUM.CA: score=15.84 buy_ready=False sector_rank=10 price=22.98 support=20.55 resistance=24.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=49.03 liquidity=939767.94 spike=0.12
- AMER.CA: score=27.9 buy_ready=False sector_rank=4 price=3.07 support=2.28 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=74.11 liquidity=36312264.0 spike=0.47
- AMES.CA: score=24.12 buy_ready=False sector_rank=10 price=76.81 support=45.15 resistance=84.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=77.9 liquidity=9217916.0 spike=0.27
- AMIA.CA: score=21.37 buy_ready=False sector_rank=10 price=8.9 support=8.4 resistance=9.51 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=44.44 liquidity=7469315.78 spike=0.95
- AMOC.CA: score=23.59 buy_ready=False sector_rank=19 price=8.05 support=7.42 resistance=8.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=53.05 liquidity=11741505.0 spike=0.22
- APSW.CA: score=12.28 buy_ready=False sector_rank=10 price=8.46 support=8.0 resistance=8.98 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=47.29 liquidity=379041.84 spike=0.5
- ARAB.CA: score=22.61 buy_ready=True sector_rank=4 price=0.23 support=0.2 resistance=0.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=66.04 liquidity=6708713.0 spike=0.08
- ARCC.CA: score=11.31 buy_ready=False sector_rank=15 price=55.61 support=53.0 resistance=57.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=49.28 liquidity=1029114.94 spike=0.05
- AREH.CA: score=25.9 buy_ready=True sector_rank=10 price=1.63 support=1.42 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=55.1 liquidity=10544659.0 spike=0.32
- ARVA.CA: score=14.39 buy_ready=False sector_rank=10 price=10.88 support=10.3 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=40.69 liquidity=487586.34 spike=0.02
- ASCM.CA: score=10.9 buy_ready=False sector_rank=10 price=63.35 support=58.16 resistance=63.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63448752.0 spike=0.85
- ASPI.CA: score=14.3 buy_ready=False sector_rank=10 price=0.32 support=0.3 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=55.81 liquidity=401755.56 spike=0.01
- ATLC.CA: score=15.68 buy_ready=False sector_rank=16 price=5.21 support=4.7 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=50.33 liquidity=483797.59 spike=0.07
- ATQA.CA: score=16.11 buy_ready=False sector_rank=18 price=9.6 support=9.02 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=3319250.5 spike=0.1
- AXPH.CA: score=18.16 buy_ready=True sector_rank=10 price=1185.46 support=1073.0 resistance=1342.9 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=66.59 liquidity=2261857.61 spike=0.85
- BINV.CA: score=16.89 buy_ready=False sector_rank=6 price=49.0 support=44.02 resistance=51.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=53.84 liquidity=991688.44 spike=0.15
- BIOC.CA: score=24.89 buy_ready=True sector_rank=10 price=73.6 support=66.75 resistance=76.95 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=55.49 liquidity=4090172.72 spike=1.45
- BTFH.CA: score=27.2 buy_ready=True sector_rank=16 price=3.09 support=2.91 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=48181208.0 spike=0.25
- CAED.CA: score=28.13 buy_ready=True sector_rank=10 price=72.19 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 July 01:28 PM market time freshness=DELAYED_CURRENT RSI=54.69 liquidity=8885700.0 spike=1.67
- CANA.CA: score=18.22 buy_ready=False sector_rank=12 price=36.95 support=34.5 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=394479.31 spike=0.03
- CCAP.CA: score=27.9 buy_ready=True sector_rank=6 price=5.32 support=4.65 resistance=5.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=54.37 liquidity=275010208.0 spike=0.42
- CCRS.CA: score=16.76 buy_ready=False sector_rank=10 price=2.39 support=2.18 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=863705.19 spike=0.07
- CEFM.CA: score=18.38 buy_ready=False sector_rank=10 price=105.36 support=95.75 resistance=110.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=50.09 liquidity=480160.91 spike=0.22
- CERA.CA: score=27.22 buy_ready=True sector_rank=10 price=1.33 support=1.15 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=7319672.0 spike=0.33
- CFGH.CA: score=12.06 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 July 01:00 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=156409.78 spike=26.0
- CICH.CA: score=10.82 buy_ready=False sector_rank=16 price=11.66 support=11.1 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=624167.31 spike=0.17
- CIEB.CA: score=19.99 buy_ready=True sector_rank=12 price=24.31 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=2161960.5 spike=0.32
- CIRA.CA: score=23.03 buy_ready=True sector_rank=17 price=28.96 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 July 01:28 PM market time freshness=DELAYED_CURRENT RSI=69.91 liquidity=18845852.0 spike=0.95
- CLHO.CA: score=17.18 buy_ready=True sector_rank=14 price=16.38 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=59.95 liquidity=1614850.63 spike=0.04
- CNFN.CA: score=18.67 buy_ready=True sector_rank=16 price=4.84 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=64.38 liquidity=1469090.13 spike=0.03
- COMI.CA: score=27.83 buy_ready=True sector_rank=12 price=135.42 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=51.82 liquidity=27154982.0 spike=0.06
- COPR.CA: score=14.38 buy_ready=False sector_rank=10 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=39.34 liquidity=1480681.38 spike=0.07
- COSG.CA: score=27.04 buy_ready=True sector_rank=10 price=1.65 support=1.47 resistance=1.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=9144370.0 spike=0.22
- CPCI.CA: score=13.48 buy_ready=False sector_rank=10 price=399.73 support=354.0 resistance=434.99 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=76.76 liquidity=582406.63 spike=0.25
- CSAG.CA: score=21.26 buy_ready=True sector_rank=3 price=32.6 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=65.0 liquidity=2358917.75 spike=0.14
- DAPH.CA: score=18.3 buy_ready=False sector_rank=10 price=82.77 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=398452.22 spike=0.05
- DEIN.CA: score=0.9 buy_ready=False sector_rank=10 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=16.65 buy_ready=False sector_rank=11 price=26.83 support=23.7 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=73.47 liquidity=752293.75 spike=0.15
- DSCW.CA: score=12.49 buy_ready=False sector_rank=10 price=1.78 support=1.71 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=5588510.0 spike=0.2
- DTPP.CA: score=22.9 buy_ready=False sector_rank=10 price=210.57 support=114.0 resistance=234.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=88.62 liquidity=11502267.0 spike=0.34
- EALR.CA: score=22.7 buy_ready=True sector_rank=10 price=373.03 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=4802148.5 spike=0.44
- EASB.CA: score=15.63 buy_ready=False sector_rank=10 price=7.13 support=4.87 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=46.2 liquidity=1730246.38 spike=0.1
- EAST.CA: score=7.46 buy_ready=False sector_rank=11 price=37.0 support=36.63 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=30.58 liquidity=2562826.5 spike=0.05
- EBSC.CA: score=25.98 buy_ready=True sector_rank=10 price=2.02 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=7237760.0 spike=1.42
- ECAP.CA: score=14.79 buy_ready=False sector_rank=10 price=32.5 support=30.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=892190.38 spike=0.09
- EDFM.CA: score=27.51 buy_ready=True sector_rank=10 price=341.3 support=310.2 resistance=349.93 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=64.68 liquidity=2612992.71 spike=5.38
- EEII.CA: score=17.83 buy_ready=True sector_rank=10 price=2.81 support=2.3 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=69.07 liquidity=1934066.0 spike=0.08
- EFIC.CA: score=5.53 buy_ready=False sector_rank=18 price=181.65 support=180.02 resistance=207.75 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=15.3 liquidity=1741115.19 spike=0.79
- EFID.CA: score=16.79 buy_ready=False sector_rank=11 price=28.18 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=49.27 liquidity=1893921.0 spike=0.02
- EFIH.CA: score=22.67 buy_ready=True sector_rank=5 price=22.26 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=61.78 liquidity=4769609.5 spike=0.11
- EGAL.CA: score=18.59 buy_ready=False sector_rank=18 price=294.24 support=272.28 resistance=314.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=44.65 liquidity=4799935.0 spike=0.1
- EGAS.CA: score=10.27 buy_ready=False sector_rank=19 price=49.04 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=38.8 liquidity=684263.31 spike=0.08
- EGBE.CA: score=17.88 buy_ready=False sector_rank=12 price=0.46 support=0.43 resistance=0.47 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=66.15 liquidity=51418.34 spike=0.92
- EGCH.CA: score=21.49 buy_ready=False sector_rank=18 price=13.17 support=12.13 resistance=14.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=7706129.0 spike=0.18
- EGSA.CA: score=22.92 buy_ready=False sector_rank=1 price=9.08 support=8.65 resistance=9.13 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=91.67 liquidity=24388.88 spike=4.58
- EGTS.CA: score=22.16 buy_ready=True sector_rank=4 price=18.78 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=54.61 liquidity=4258356.0 spike=0.07
- EHDR.CA: score=25.9 buy_ready=True sector_rank=10 price=2.75 support=2.37 resistance=2.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=49.38 liquidity=14017120.0 spike=0.33
- EKHO.CA: score=8.59 buy_ready=False sector_rank=19 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=16.73 buy_ready=False sector_rank=13 price=2.12 support=2.04 resistance=2.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=3098463.75 spike=0.21
- ELKA.CA: score=11.2 buy_ready=False sector_rank=10 price=1.68 support=1.59 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53420872.0 spike=1.15
- ELNA.CA: score=21.03 buy_ready=False sector_rank=10 price=38.81 support=35.55 resistance=41.48 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=46.84 liquidity=2126982.13 spike=4.02
- ELSH.CA: score=29.9 buy_ready=True sector_rank=10 price=14.62 support=11.1 resistance=14.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=53.52 liquidity=147732576.0 spike=0.81
- ELWA.CA: score=11.6 buy_ready=False sector_rank=10 price=1.95 support=1.87 resistance=2.22 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=39.47 liquidity=704297.12 spike=0.47
- EMFD.CA: score=24.76 buy_ready=True sector_rank=4 price=11.91 support=11.11 resistance=12.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=8859409.0 spike=0.06
- ENGC.CA: score=25.84 buy_ready=True sector_rank=10 price=38.99 support=33.0 resistance=39.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=67.45 liquidity=7943463.5 spike=0.47
- EOSB.CA: score=15.92 buy_ready=False sector_rank=10 price=1.48 support=1.42 resistance=1.55 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=15994.36 spike=0.18
- EPCO.CA: score=16.18 buy_ready=False sector_rank=10 price=9.1 support=8.5 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=39.23 liquidity=1283882.63 spike=0.2
- EPPK.CA: score=16.4 buy_ready=False sector_rank=10 price=14.11 support=11.72 resistance=15.25 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=70.44 liquidity=498463.96 spike=0.53
- ETEL.CA: score=24.81 buy_ready=True sector_rank=1 price=97.6 support=89.01 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=62.64 liquidity=3909364.75 spike=0.05
- ETRS.CA: score=18.3 buy_ready=True sector_rank=10 price=10.91 support=8.77 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=60.08 liquidity=2399945.25 spike=0.03
- EXPA.CA: score=27.83 buy_ready=True sector_rank=12 price=18.8 support=18.03 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=12691162.0 spike=0.47
- FAIT.CA: score=16.61 buy_ready=False sector_rank=12 price=37.0 support=35.01 resistance=37.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=48.23 liquidity=784616.06 spike=0.31
- FAITA.CA: score=17.95 buy_ready=False sector_rank=12 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=9 July 11:50 AM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=118680.92 spike=3.82
- FERC.CA: score=21.41 buy_ready=False sector_rank=18 price=75.93 support=72.75 resistance=80.83 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=53.32 liquidity=6784269.6 spike=1.92
- FWRY.CA: score=20.91 buy_ready=False sector_rank=5 price=19.33 support=17.71 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=61.03 liquidity=6006248.5 spike=0.03
- GBCO.CA: score=14.82 buy_ready=False sector_rank=8 price=30.64 support=26.62 resistance=32.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=65.5 liquidity=919154.19 spike=0.01
- GDWA.CA: score=8.57 buy_ready=False sector_rank=10 price=0.79 support=0.76 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=34.31 liquidity=1668815.62 spike=0.13
- GGCC.CA: score=24.9 buy_ready=False sector_rank=10 price=0.58 support=0.4 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=92.66 liquidity=11038849.0 spike=0.68
- GIHD.CA: score=26.1 buy_ready=False sector_rank=10 price=50.21 support=39.0 resistance=52.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=75.1 liquidity=28620204.0 spike=1.6
- GMCI.CA: score=16.66 buy_ready=False sector_rank=10 price=1.98 support=1.66 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=72.31 liquidity=758494.44 spike=0.75
- GRCA.CA: score=6.4 buy_ready=False sector_rank=10 price=48.99 support=48.01 resistance=58.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=13.6 liquidity=500895.56 spike=0.16
- GSSC.CA: score=18.4 buy_ready=False sector_rank=10 price=257.15 support=240.0 resistance=263.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=66.12 liquidity=502183.59 spike=0.11
- GTWL.CA: score=24.9 buy_ready=False sector_rank=10 price=110.59 support=46.0 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=91.76 liquidity=27207836.0 spike=0.31
- HDBK.CA: score=10.95 buy_ready=False sector_rank=12 price=78.1 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=10.7 liquidity=6126380.5 spike=0.15
- HELI.CA: score=24.9 buy_ready=False sector_rank=4 price=7.3 support=6.28 resistance=7.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=76.27 liquidity=21705102.0 spike=0.14
- HRHO.CA: score=19.05 buy_ready=False sector_rank=16 price=26.7 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=35.6 liquidity=7855743.5 spike=0.06
- ICID.CA: score=17.33 buy_ready=True sector_rank=10 price=8.13 support=6.36 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=61.2 liquidity=1427660.63 spike=0.14
- IDRE.CA: score=29.7 buy_ready=True sector_rank=10 price=47.0 support=41.1 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=56.8 liquidity=21329012.0 spike=1.9
- IFAP.CA: score=17.39 buy_ready=False sector_rank=7 price=19.55 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=494697.63 spike=0.1
- INFI.CA: score=14.64 buy_ready=False sector_rank=10 price=98.03 support=88.51 resistance=101.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=735025.94 spike=0.1
- IRON.CA: score=13.63 buy_ready=False sector_rank=18 price=32.19 support=30.51 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=50.5 liquidity=838558.38 spike=0.11
- ISMA.CA: score=12.3 buy_ready=False sector_rank=10 price=27.45 support=26.54 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=19.79 liquidity=3400087.5 spike=0.11
- ISMQ.CA: score=24.79 buy_ready=False sector_rank=18 price=9.71 support=7.67 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=73.85 liquidity=12843491.0 spike=0.09
- ISPH.CA: score=14.02 buy_ready=False sector_rank=14 price=11.54 support=11.2 resistance=12.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=41.61 liquidity=3454009.75 spike=0.05
- JUFO.CA: score=17.86 buy_ready=True sector_rank=11 price=30.78 support=28.5 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=50.71 liquidity=1957410.13 spike=0.07
- KABO.CA: score=22.56 buy_ready=False sector_rank=9 price=7.5 support=5.96 resistance=7.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=87.74 liquidity=7661065.5 spike=0.29
- KWIN.CA: score=7.9 buy_ready=False sector_rank=10 price=69.34 support=65.0 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=32.09 liquidity=1997093.38 spike=0.15
- KZPC.CA: score=7.55 buy_ready=False sector_rank=10 price=8.5 support=8.26 resistance=10.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=34.97 liquidity=649128.88 spike=0.1
- LCSW.CA: score=27.28 buy_ready=True sector_rank=15 price=31.61 support=26.0 resistance=31.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=69.27 liquidity=14550522.0 spike=0.26
- LUTS.CA: score=17.43 buy_ready=False sector_rank=10 price=0.74 support=0.65 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=39.02 liquidity=3525638.5 spike=0.07
- MAAL.CA: score=17.39 buy_ready=False sector_rank=10 price=8.21 support=5.52 resistance=8.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=99.48 liquidity=2493446.25 spike=0.15
- MASR.CA: score=27.9 buy_ready=True sector_rank=10 price=7.78 support=6.54 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=60.49 liquidity=18673558.0 spike=0.23
- MBSC.CA: score=13.39 buy_ready=False sector_rank=15 price=243.09 support=222.66 resistance=256.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=42.87 liquidity=1109810.13 spike=0.04
- MCQE.CA: score=16.02 buy_ready=False sector_rank=15 price=177.3 support=166.66 resistance=182.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=52.92 liquidity=1739602.63 spike=0.12
- MCRO.CA: score=20.99 buy_ready=True sector_rank=10 price=1.25 support=1.17 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=4085352.0 spike=0.14
- MENA.CA: score=20.79 buy_ready=True sector_rank=4 price=7.09 support=6.41 resistance=7.59 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=2890458.35 spike=0.43
- MEPA.CA: score=16.22 buy_ready=False sector_rank=10 price=1.67 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=1318727.5 spike=0.12
- MFPC.CA: score=23.79 buy_ready=False sector_rank=18 price=37.33 support=34.22 resistance=41.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=48.5 liquidity=16386146.0 spike=0.16
- MFSC.CA: score=14.43 buy_ready=False sector_rank=10 price=47.16 support=44.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=58.13 liquidity=528808.56 spike=0.07
- MHOT.CA: score=2.58 buy_ready=False sector_rank=21 price=16.58 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=15.86 liquidity=1682516.88 spike=0.11
- MICH.CA: score=16.37 buy_ready=False sector_rank=10 price=37.5 support=34.0 resistance=39.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=50.07 liquidity=2468899.5 spike=0.15
- MILS.CA: score=20.55 buy_ready=True sector_rank=10 price=136.14 support=126.31 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=38.08 liquidity=4653917.5 spike=0.43
- MIPH.CA: score=23.11 buy_ready=True sector_rank=14 price=700.0 support=630.13 resistance=710.0 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=59.94 liquidity=2659300.0 spike=1.44
- MOED.CA: score=14.34 buy_ready=False sector_rank=10 price=0.7 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=46.9 liquidity=444377.91 spike=0.05
- MOIL.CA: score=16.73 buy_ready=False sector_rank=19 price=0.52 support=0.46 resistance=0.53 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=74.0 liquidity=137993.43 spike=0.51
- MOIN.CA: score=19.11 buy_ready=False sector_rank=10 price=23.57 support=22.6 resistance=25.25 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=39.62 liquidity=2505844.52 spike=3.35
- MOSC.CA: score=12.58 buy_ready=False sector_rank=10 price=271.41 support=246.6 resistance=330.0 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=42.79 liquidity=1677313.82 spike=0.2
- MPCI.CA: score=18.28 buy_ready=True sector_rank=10 price=238.87 support=213.0 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=2382390.0 spike=0.02
- MPCO.CA: score=25.9 buy_ready=True sector_rank=7 price=1.91 support=1.66 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=16555264.0 spike=0.19
- MPRC.CA: score=22.12 buy_ready=False sector_rank=10 price=42.67 support=31.15 resistance=43.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=90.71 liquidity=7220087.5 spike=0.15
- MTIE.CA: score=20.17 buy_ready=True sector_rank=8 price=9.42 support=8.65 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=2271645.75 spike=0.11
- NAHO.CA: score=13.03 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=32723.41 spike=1.55
- NCCW.CA: score=16.02 buy_ready=False sector_rank=10 price=6.16 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=2119303.75 spike=0.08
- NEDA.CA: score=6.04 buy_ready=False sector_rank=10 price=2.74 support=2.7 resistance=2.83 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=31.58 liquidity=137320.58 spike=0.43
- NHPS.CA: score=27.64 buy_ready=True sector_rank=10 price=74.07 support=61.55 resistance=75.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=66.19 liquidity=36612116.0 spike=1.87
- NINH.CA: score=21.48 buy_ready=False sector_rank=10 price=17.45 support=16.8 resistance=18.85 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=44.44 liquidity=9759139.78 spike=1.41
- NIPH.CA: score=22.01 buy_ready=True sector_rank=14 price=177.37 support=157.01 resistance=185.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.47 liquidity=6442324.5 spike=0.07
- OBRI.CA: score=27.9 buy_ready=True sector_rank=10 price=36.92 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=11100584.0 spike=0.36
- OCDI.CA: score=15.81 buy_ready=False sector_rank=4 price=26.96 support=20.0 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=81.63 liquidity=2909787.75 spike=0.03
- OCPH.CA: score=15.97 buy_ready=False sector_rank=10 price=353.29 support=337.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=61.65 liquidity=1070839.38 spike=0.17
- ODIN.CA: score=19.24 buy_ready=True sector_rank=10 price=2.38 support=2.01 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=1341169.88 spike=0.1
- OFH.CA: score=22.04 buy_ready=True sector_rank=10 price=0.64 support=0.57 resistance=0.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=62.11 liquidity=2138498.25 spike=0.1
- OIH.CA: score=18.5 buy_ready=False sector_rank=6 price=1.42 support=1.33 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=3599563.75 spike=0.05
- OLFI.CA: score=20.38 buy_ready=True sector_rank=11 price=22.76 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=63.55 liquidity=2475105.0 spike=0.08
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=686.08 support=685.0 resistance=691.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15553527.0 spike=1.0
- ORHD.CA: score=25.9 buy_ready=True sector_rank=4 price=39.26 support=35.01 resistance=39.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=59.68 liquidity=12899143.0 spike=0.08
- ORWE.CA: score=16.68 buy_ready=False sector_rank=9 price=22.71 support=21.95 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=44.13 liquidity=2778301.5 spike=0.14
- PHAR.CA: score=16.27 buy_ready=False sector_rank=14 price=87.19 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=55.64 liquidity=700014.13 spike=0.03
- PHDC.CA: score=18.9 buy_ready=False sector_rank=4 price=14.85 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=27.55 liquidity=23209548.0 spike=0.07
- PHTV.CA: score=26.82 buy_ready=False sector_rank=10 price=291.02 support=201.55 resistance=297.0 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=90.0 liquidity=25582694.17 spike=1.96
- POUL.CA: score=17.03 buy_ready=True sector_rank=11 price=39.75 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=66.73 liquidity=1125399.63 spike=0.03
- PRCL.CA: score=19.3 buy_ready=False sector_rank=15 price=36.4 support=23.75 resistance=36.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=84.67 liquidity=5020889.5 spike=0.1
- PRDC.CA: score=28.1 buy_ready=True sector_rank=4 price=8.58 support=5.91 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=61.68 liquidity=8196891.5 spike=0.06
- PRMH.CA: score=13.32 buy_ready=False sector_rank=10 price=2.81 support=2.62 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60435808.0 spike=2.21
- RACC.CA: score=19.18 buy_ready=True sector_rank=10 price=10.12 support=9.36 resistance=10.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=1280129.75 spike=0.13
- RAKT.CA: score=11.96 buy_ready=False sector_rank=10 price=22.35 support=21.4 resistance=23.79 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=41.67 liquidity=61507.2 spike=0.25
- RAYA.CA: score=27.9 buy_ready=True sector_rank=2 price=8.06 support=6.7 resistance=8.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=65.62 liquidity=12180407.0 spike=0.11
- RMDA.CA: score=14.97 buy_ready=False sector_rank=14 price=4.99 support=4.81 resistance=5.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=1398658.25 spike=0.02
- ROTO.CA: score=19.06 buy_ready=True sector_rank=10 price=43.07 support=33.06 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=48.04 liquidity=3161251.5 spike=0.1
- RREI.CA: score=29.9 buy_ready=True sector_rank=10 price=3.85 support=3.34 resistance=3.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=58.46 liquidity=10704982.0 spike=0.59
- RTVC.CA: score=13.49 buy_ready=False sector_rank=10 price=3.8 support=3.55 resistance=3.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=592541.56 spike=0.13
- RUBX.CA: score=19.35 buy_ready=False sector_rank=10 price=13.02 support=9.8 resistance=14.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=79.35 liquidity=6449839.0 spike=0.12
- SAUD.CA: score=16.12 buy_ready=False sector_rank=12 price=21.64 support=19.99 resistance=22.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=1289608.63 spike=0.18
- SCEM.CA: score=15.72 buy_ready=False sector_rank=15 price=62.96 support=59.3 resistance=67.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=51.54 liquidity=1443270.63 spike=0.09
- SCFM.CA: score=16.93 buy_ready=False sector_rank=10 price=255.69 support=226.5 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=51.38 liquidity=2034564.0 spike=0.39
- SCTS.CA: score=18.11 buy_ready=True sector_rank=17 price=619.69 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=57.87 liquidity=1076258.88 spike=0.21
- SDTI.CA: score=16.56 buy_ready=False sector_rank=10 price=46.93 support=45.55 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=47.34 liquidity=655925.5 spike=0.09
- SEIG.CA: score=17.21 buy_ready=False sector_rank=10 price=247.34 support=180.0 resistance=272.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=83.19 liquidity=4305102.0 spike=0.29
- SIPC.CA: score=15.99 buy_ready=False sector_rank=10 price=3.46 support=3.25 resistance=3.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=51.76 liquidity=1085620.75 spike=0.12
- SKPC.CA: score=16.39 buy_ready=False sector_rank=18 price=16.33 support=15.58 resistance=16.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=50.21 liquidity=3604396.5 spike=0.11
- SMFR.CA: score=18.25 buy_ready=False sector_rank=10 price=205.3 support=187.01 resistance=209.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=351369.88 spike=0.18
- SNFC.CA: score=12.36 buy_ready=False sector_rank=10 price=11.89 support=11.26 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1461583.75 spike=0.13
- SPIN.CA: score=16.31 buy_ready=False sector_rank=9 price=14.62 support=13.3 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=70.21 liquidity=405132.97 spike=0.04
- SPMD.CA: score=19.67 buy_ready=True sector_rank=10 price=0.45 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=60.9 liquidity=1771176.12 spike=0.1
- SUGR.CA: score=5.91 buy_ready=False sector_rank=11 price=46.93 support=45.31 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=32.32 liquidity=1013092.69 spike=0.21
- SVCE.CA: score=24.51 buy_ready=True sector_rank=10 price=9.48 support=8.11 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:36 AM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=6606559.0 spike=0.09
- SWDY.CA: score=20.16 buy_ready=True sector_rank=13 price=88.97 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=60.8 liquidity=2527421.5 spike=0.19
- TALM.CA: score=6.0 buy_ready=False sector_rank=17 price=15.54 support=15.27 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=24.52 liquidity=964878.5 spike=0.08
- TMGH.CA: score=27.9 buy_ready=True sector_rank=4 price=97.0 support=92.1 resistance=99.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=54.97 liquidity=14677391.0 spike=0.04
- TRTO.CA: score=11.9 buy_ready=False sector_rank=10 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-07-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=18.35 buy_ready=False sector_rank=10 price=505.32 support=460.0 resistance=529.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.13 liquidity=448829.03 spike=0.29
- UEGC.CA: score=19.14 buy_ready=False sector_rank=10 price=1.77 support=1.33 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=78.33 liquidity=4244312.5 spike=0.19
- UNIP.CA: score=16.61 buy_ready=False sector_rank=10 price=0.34 support=0.29 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=49.47 liquidity=710000.88 spike=0.04
- UNIT.CA: score=10.9 buy_ready=False sector_rank=4 price=19.04 support=18.9 resistance=20.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17144708.0 spike=0.91
- WCDF.CA: score=6.95 buy_ready=False sector_rank=10 price=518.6 support=450.0 resistance=544.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:21 AM market time freshness=DELAYED_CURRENT RSI=29.03 liquidity=485502.78 spike=1.28
- WKOL.CA: score=18.76 buy_ready=False sector_rank=10 price=317.67 support=273.1 resistance=334.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=64.07 liquidity=859602.63 spike=0.12
- ZEOT.CA: score=16.63 buy_ready=False sector_rank=10 price=11.11 support=8.69 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=47.43 liquidity=734152.06 spike=0.02
- ZMID.CA: score=28.02 buy_ready=True sector_rank=4 price=7.02 support=6.03 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=67.71 liquidity=223910848.0 spike=1.06

## Backtesting Lite
- ALCN.CA: 180d return=33.32%, max drawdown=-16.69%, MA20>MA50 days last20=0, as_of=2026-07-08T21:00:00+00:00
- ELSH.CA: 180d return=80.32%, max drawdown=-27.17%, MA20>MA50 days last20=20, as_of=2026-07-08T21:00:00+00:00
- RREI.CA: 180d return=57.98%, max drawdown=-27.36%, MA20>MA50 days last20=2, as_of=2026-07-08T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ALCN.CA: status=RECENT_ACCEPTED latest=2026-03-20 age_days=114 sources=3 expected=Alexandria Containers and Cargo Handling summary=Alexandria Containers and Cargo Handling (ALCN.CA) has seen significant activity in the last 12 months, including financial performance reports for 2025, dividend declarations, and a mandatory tender offer by AD Ports Group. The company also announced plans to sell a stake in Egypt Marine Ports.
  - AD Ports Group Announces Intention to Launch Mandatory Tender Offer for Alexandria Container & Cargo Handling Company (December 15, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYj5qESAVWHr-Wlu-xa1sFqDBqkAmDC9z74SqwMIahP9eOT1Bh_vWMAwAdJ2oUC3xP1GlyRYz9wNC8T6Jg0Oi729Ykk2TVeYAKW1P8Q-jZZijdsXV5Ivkc-kXIelYZ1zcZ_OybkXgyUHs9la7Gs7DfUvoPeg5J6sbs9F9Rz0Qnqe17JeqspDhhFBeLo4GMs48bhNzCF7-yuzFgaks8N10ZBYj04iSI90uyb03g1corrmVRwBanV1ZA4XIwwFxSx4G5B_XNq8UOvoCPoa9ZiR0K
  - Alexandria Container&Cargo Handling Company Reports Earnings Results for the First Quarter Ended September 30, 2025 (December 04, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuSzZVPpJ_5i3avUy7B-wN6qK1UvYtiwDZDhDD3yUEVVw8YvD9MX8Crs43JeaAjjXdwV7WOW8VWphqAb5h8kMjxHf5ftqtxXXIJOirWw3k3l7BB8CHZKyr5AJiw6ArP96qBdd0u-5fxeD3dSTzmTvgnsNDgOqVQKC4nTEInsJdxePqAKCKl0ZDSwvQ
  - Alexandria Container&Cargo Handling Company Reports Earnings Results for the Half Year Ended December 31, 2025 (March 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuSzZVPpJ_5i3avUy7B-wN6qK1UvYtiwDZDhDD3yUEVVw8YvD9MX8Crs43JeaAjjXdwV7WOW8VWphqAb5h8kMjxHf5ftqtxXXIJOirWw3k3l7BB8CHZKyr5AJiw6ArP96qBdd0u-5fxeD3dSTzmTvgnsNDgOqVQKC4nTEInsJdxePqAKCKl0ZDSwvQ
- ELSH.CA: status=RECENT_ACCEPTED latest=2026-07-04 age_days=8 sources=3 expected=Al Shams Housing and Urbanization SAE summary=Al Shams Housing and Urbanization SAE (ELSH.CA) has reported its financial performance for the last 12 months as of July 2026, including revenue, profits, and cash flow. The company also declared cash dividends and held its AGM in June 2026.
  - Al Shams Housing and Urbanization SAE (EGX:ELSH) Statistics & Valuation Metrics (July 04, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHki9-15gZ6L8AhARJ6gg9cDXSqXy7pXla_ysUyis0NMuH6CCmLO-8j27097J95UqhskM4ce02aRb_rfeNjJ_SjrftXJcHunEVWhJ-WfAg5U-TTNID-R8SOaQsrcV70ryGuRlPZHC73xfuOHby-
  - El Shams Housing & Urbanization (ELSH.CA) Declares Cash Dividends (June 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrnjXE9YxJ-YNZ2NbDUcazuAF7x9ZtQvWcQGgFTj1TNSGKWB96vPwYFnyqFqy-xgcUPC8VWnKvR7HkP7_5ZB3BGTHThGn3L450JHxfBlXoHeiPJ49lic24MDlegSb-aG2gcWMw0CEWvf9959TrjHw
  - El Shams Housing & Urbanization (ELSH.CA) - AGM Minutes (after Certification) (June 10, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrnjXE9YxJ-YNZ2NbDUcazuAF7x9ZtQvWcQGgFTj1TNSGKWB96vPwYFnyqFqy-xgcUPC8VWnKvR7HkP7_5ZB3BGTHThGn3L450JHxfBlXoHeiPJ49lic24MDlegSb-aG2gcWMw0CEWvf9959TrjHw
- RREI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Arab Real Estate Investment Co. summary=Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
- IDRE.CA: status=RECENT_ACCEPTED latest=2026-08-06 age_days=0 sources=3 expected=Ismailia Development and Real Estate Co summary=Ismailia Development and Real Estate Co (IDRE.CA) has released its 2025 financial performance and has upcoming earnings in August 2026. The company's market cap has shown significant growth, and there have been recent disclosures regarding board decisions and shareholder meetings.
  - Ismailia Development and Real Estate Co (EGX:IDRE) Stock Price & Overview (2025 Financial Performance, Earnings Date Aug 6, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFH2-Xph0Gmctf7pxa9ZvLLkvmfK0m0ihVWlKWhEdMclXm-abnIgt0Jeed49BH3CClGNwwrk16gMrtdaPPExOvTTwpuBkIkAiG367Y--k9Irxm1HjCRLq0IX3xTUAfNOdpEWg
  - Ismailia Development and Real Estate Co (EGX:IDRE) Market Cap & Net Worth (July 09, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7DX9oR0rpU8YpH730Do1jxdsoBJptLa8i6DTc4yP95v-G7fa9WdkWDltv2G-FcL-KvLVBgdTa2e48GKQQXoOX8JnwknGkKaYos43Dh5UunnFMDTadmFbsN43o_k_7fz_6JnnU_WBMeUB2N4yU
  - Ismailia Development and Real Estate Co (IDRE.CA) - Release from the FRA (March 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJi784Gibd67S5JJnYM9dOC8HJZ6Wz-mufvI5otXcO2cEBFqyEbgmHPGTG8dye-A8sNWp1U-MjgIVE3wUcpKy3XMPnkMLLQfQhRJBHG0QQQfvmBkDc260FrRj4t4IZlgFQ0gy09AQ6cGjYAiNdBLjLjQ
- CAED.CA: status=RECENT_ACCEPTED latest=2026-07-21 age_days=0 sources=3 expected=Cairo Educational Services SAE summary=Cairo Educational Services SAE (CAED.CA) reported strong financial performance in fiscal year 2025 and has an upcoming earnings date in July 2026. The company also announced dividends and saw its stock price reach an all-time high in May 2026.
  - Cairo Educational Services SAE (EGX:CAED) Stock Price & Overview (Fiscal Year 2025 Financial Performance, Earnings Date Jul 21, 2026, Ex-Dividend Date Jan 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX0zBrFaLYv30fsHoxDHiFHpnWVykYoR9jSDrwTfVdIhMe5HOviN20VF8j1n7bV4am0LAUQ5Z_FmPLs3MvGDXxDPc5kIJXbvAC1gjjxCPk8udyP8bHHJCskyybjIKCoTcyAw
  - Cairo Educational Services (CAED.CA) - Release from FRA (September 23, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-hZ_7TR4wQf2bK_dZM3fhETswYOu9glyDGKFcrHiAJxvpPIRl66pMa4eeNzyghLA8XYEAZJoTAA3xeY0b76Fmpds9VnW6z1O28FVVwBBt8RySw4iN_WmFEtqElb7tb8tRYAuo_xwDUbc5kI7Z
  - CAED Stock Price and Chart — EGX:CAED - TradingView (Net income, dividends, stock performance, all-time high May 11, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU8GfQ6I9sStvXuNm3bigo7a1EEBjoplGdYTuQ4zY_eSlnV0DBBJw4IpWSFO88Fs5DXeLKVfA_mtNZf41eklTz7dt484RjAVwdsQkshfJEEnUiiUtDaP8Gsl7YNcJx8OKTwo0UN4U
- PRDC.CA: status=RECENT_ACCEPTED latest=2026-08-20 age_days=0 sources=3 expected=Pioneers Properties For Urban Development summary=Pioneers Properties For Urban Development (PRDC.CA) reported its 2025 financial performance and Q1 2025 consolidated financial results. The company has an upcoming earnings date in August 2026 and its market cap was reported in July 2026.
  - Pioneers Properties For Urban Development - PRE Group (EGX:PRDC) - Stock Analysis (2025 Financial Performance, Earnings Date Aug 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnUi2T0ODmEaqHm8cd3CAHio1BVroWFqp8i_jb27_IZEYUZwE4iKnv3KjTdvThhkn6asjTIWFQEAb2bSc2y1UVwWmKB41ki9uATmRTt5XeXBgcBDgC7iIRkJmktKndJIdzLg
  - Pioneers Properties For Urban Development (PREDCO) (PRDC.CA) Reports Its Financial Results (Consolidated) for the Period from 01/01/2025 to 31/03/2025 (June 29, 2025): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzagSSqIU2cf2MbdgZGLt8WWfqtCv3_8VqI7zLk4vBFkTmEK0BTpOWzd5fcQ3valmoKVHNqdMkikonz5QwiuAZQb5y1yr8HE_RYDu5vn_3lDzC35xIQ5rlbgFlOCnfaqrH1AIrCW-jXau-AfeZ9NUOYg
  - Pioneer Properties for Urban Development Stock Price Today | EGX: PRDC Live (Market Cap July 09, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf5wvYv9SAlapY7YvzXSrE2QKc8lcPPLRaQkDE3254e6gVk-dpCQtSZKSJ2oK4QTRZLRGoDskbuOHcJmIZ0C6VB1Ntp26-29oZzllkxWwzaY8r_LcS8UpWEbloUTbrNkb07kT_fqNrocPwQpZVIz6GlVlykTBQXTo
- ZMID.CA: status=RECENT_ACCEPTED latest=2026-07-09 age_days=3 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi Investment and Development (ZMID.CA) has recent share price information as of July 2026 and its investor relations details are available on the EGX website. Key financial metrics like net profit, EPS, PE Ratio, and market cap were also reported.
  - IR - Zahraa El Maadi (Share Price and Financials as of July 09, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnQgC6eWyHpWP03GcT5qHO7XPIoCtakmVBIOVr-i5JMxGqJ8Tv6C6QxR3uvdREfOSN0OtqjrgyC-Q7FRSc1xlWnRFJ7VjWA-GRtC166xtssZFYzqgkRfI
  - Investor Relations Contacts Register - The Egyptian Exchange (Zahraa Maadi Investment & Development): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQaLeZkQu6X-VEPQL7VWmLYrTKAstdsAy5XsEpyXpeM2vZaAqbEhaR23Bnn7kKd0cutMNVescVZdjR-YKDTjRQiw6w7bnZgzDpDbcO7qzvWoRSqzG5YDYPW_XMrP_RdjtdtrTjfh9KWK-Pg76xA
  - Zahraa Maadi Investment and Development (ZMID) - Mubasher Info (Stock Statistics as of July 09, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbHJ-5DHUIoLDthWL15y6EscXi3vPdtZMoS60yGpLtmeC_AFVb6ifLzGcW8xn9P84D7rNIrdmY3qCvPACi6HJDsiYYtnrSoFy5Y1BRAd06WIM1maq_hMpZZjRCM3UjVg5cM4iadStycIhmiqCtJXA
- TMGH.CA: status=RECENT_ACCEPTED latest=2026-09-02 age_days=0 sources=3 expected=Talaat Moustafa Group Holding summary=Talaat Moustafa Group Holding (TMGH.CA) has recent investor relations information, including disclosures to the EGX regarding project developments in Saudi Arabia in June 2026. The company also announced dividends in May 2026 and has an upcoming earnings report in September 2026.
  - Investor Relations, Financial Results & Stock Data | TMG - Talaat Moustafa Group: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjyJt2rhjcPuSigxIsklqyOMv7ABrDKC3tKL6Jd1eemDZgLwAqrxmcA67MaZJk30zgFpUKmVctKjR5Pokc0z0gXbfZZ7VsOCYN_rK2IGOyJHGMCb9rbSGfYfG0IM3D7wvpZBsRQWSD
  - Release from TMG Holding (TMGH.CA) Concerning Company's Projects (June 26, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0oEFZpu9zIQJIm4414uPg41oDT3dE23tOeQd2tk86BW2tgg6638HB_ZVzNGHp3Oy84deTvez7QE5XfvgWyMhpkQBpW5YGy-qZLOnXHuBvEJz0jFttv1GqDOcrlXB3RLNM2WEJPNSMR5Dw2qez1YtCtA
  - T M G Holding Stock Price Today | EGX: TMGH Live - Investing.com (Dividend, Ex-Dividend Date May 19, 2026, Payment Date May 21, 2026, Next Earnings Sep 02, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYj9m3FSLtyrDxt0r8QZL_vi_tjFxzXjd8DY2loeSGx_Nps-VV4DPyskgWiGp6vRxCB_D1otfZlNvE5rIAbOtHX0nidtNgU_T4ossxbWItxpvikpQ3cT32VQ-cPWnypt2iMJxPMX8tfXM

## Warnings
- Evidence rejected for RREI.CA: source text did not clearly match RREI.CA / Arab Real Estate Investment Co..
