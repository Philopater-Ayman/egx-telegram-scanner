# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-08-30T13:32:07.520726+00:00
Generated Cairo: 2026-08-30 16:32
Run timing: target 11:00 Cairo | generated Cairo 2026-08-30 16:32 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-08-30 16:28

## Control Center
- Action tickets: 3 prioritized signal(s)
- BUY-ready candidates: 48
- Data quality issues: 1
- Tradeable price/liquidity tickers: 171/189
- Top sector: Textiles

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, August 30
- Freshness: DELAYED
- EGX30 regime: CONSTRUCTIVE / above MA20 50.0% / above MA50 75.0%
- EGX70 regime: MIXED / above MA20 47.37% / above MA50 73.68%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- GTWL.CA: liquidity=541152640.0 spike=1.0 score=9.06
- EMFD.CA: liquidity=493415456.0 spike=6.05 score=33.4
- ZMID.CA: liquidity=355572288.0 spike=1.42 score=24.24
- CCAP.CA: liquidity=332587616.0 spike=0.56 score=23.88
- TMGH.CA: liquidity=323135808.0 spike=1.35 score=20.1

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: We need to output JSON with keys summary and bullets (3-5 short strings). Must not make trade decision, not invent live data, not mention quantities or position sizing. Explain why scanner selected prioritized tickets, what liquidity/sector/support/resistance/outlook means for next 1-3 days, and how EGX30/EGX70 market regime changes risk mode, and include uncertainty.

We have data: primary ticket MCQE.CA, tickets list includes MCQE.CA, SPIN.CA, ORWE.CA. Market regime: EGX30 CONSTRUCTIVE, EGX70 MIXED, risk mode SELECTIVE_SWING_TRADES_ONLY. Sector breadth 42.86%, leading sectors: Textiles, Building Materials, Agriculture & Food Production.

We need to summarize why scanner selected these tick
- Bullets: maybe 4 bullets.

Bullet 1:
- SPIN.CA (Textiles) shows RSI 67.6, price above moving averages, liquidity spike modest; extended momentum and far‑above‑support imply possible pullback; outlook BULLISH_WATCH (83).
- ORWE.CA (Textiles) has RSI 44.6, price above MA20/MA50, liquidity cooling; weaker momentum but still above support; outlook BULLISH_WATCH (84) with caution.
- Make sure no quantities or position sizing. No mention of entry, TP, SL? The instruction:
- price above moving averages

## Top Liquidity Spikes
- BINV.CA: spike=12.65 liquidity=74521208.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EPPK.CA: spike=7.42 liquidity=5590103.0 outlook=CONSTRUCTIVE score=53.15 buy_ready=False
- EMFD.CA: spike=6.05 liquidity=493415456.0 outlook=BULLISH_WATCH score=82.23 buy_ready=True
- DAPH.CA: spike=4.68 liquidity=210891408.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MPRC.CA: spike=3.57 liquidity=106317432.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=11.09 5d=1.1% 20d=17.57% aboveMA50=100.0%
- #2 Building Materials: score=10.97 5d=2.4% 20d=21.92% aboveMA50=83.33%
- #3 Agriculture & Food Production: score=8.51 5d=1.23% 20d=9.54% aboveMA50=100.0%
- #4 Industrial Goods & Cables: score=8.19 5d=3.47% 20d=15.32% aboveMA50=50.0%
- #5 Healthcare: score=8.09 5d=1.45% 20d=14.98% aboveMA50=100.0%
- #6 Transportation & Logistics: score=7.71 5d=0.0% 20d=12.91% aboveMA50=100.0%
- #7 Banking & Financials: score=7.35 5d=1.54% 20d=4.5% aboveMA50=100.0%
- #8 Basic Resources & Chemicals: score=6.65 5d=-0.11% 20d=5.64% aboveMA50=80.0%

## Today's Prioritized Action Tickets
- Priority #1: BUY MCQE.CA
  - Entry: 233.54 | Take profit: 290.86 | Stop loss: 224.2
  - Confidence: LOW | score=28.4 | outlook=BULLISH_WATCH 78
  - Reason: WATCH/BUY SETUP: MCQE.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 64.88, support 178.0, resistance 292.32, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #2: BUY SPIN.CA
  - Entry: 19.75 | Take profit: 21.77 | Stop loss: 18.96
  - Confidence: LOW | score=27.5 | outlook=BULLISH_WATCH 83
  - Reason: WATCH/BUY SETUP: SPIN.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 67.57, support 15.3, resistance 21.88, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.
- Priority #3: BUY ORWE.CA
  - Entry: 26.35 | Take profit: 28.45 | Stop loss: 25.3
  - Confidence: LOW | score=27.4 | outlook=BULLISH_WATCH 84
  - Reason: WATCH/BUY SETUP: ORWE.CA has aligned current price data, liquidity above threshold, price above MA20/MA50, RSI 44.57, support 22.55, resistance 27.41, and evidence sources. Macro trend is Bearish; market regime is SELECTIVE_SWING_TRADES_ONLY; verify price action in Thndr before treating it as a swing entry.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- LCSW.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MIPH.CA: BULLISH_WATCH score=95.09 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- IFAP.CA: BULLISH_WATCH score=93.51 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20
- KABO.CA: BULLISH_WATCH score=85 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- ORWE.CA: BULLISH_WATCH score=84 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- SPIN.CA: BULLISH_WATCH score=83 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- ABUK.CA: BULLISH_WATCH score=82.65 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- EMFD.CA: BULLISH_WATCH score=82.23 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- EBSC.CA: BULLISH_WATCH score=81.15 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- MPCO.CA: BULLISH_WATCH score=80.51 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- EMFD.CA: rank=33.4 outlook=BULLISH_WATCH outlook_score=82.23 sector_rank=9 price=12.65 support=11.08 resistance=12.36 liquidity=493415456.0
- MCQE.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=78 sector_rank=2 price=233.54 support=178.0 resistance=292.32 liquidity=13177357.0
- SPIN.CA: rank=27.5 outlook=BULLISH_WATCH outlook_score=83 sector_rank=1 price=19.75 support=15.3 resistance=21.88 liquidity=43279068.0
- MPCO.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=80.51 sector_rank=3 price=2.21 support=1.88 resistance=2.38 liquidity=64207024.0
- ORWE.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=84 sector_rank=1 price=26.35 support=22.55 resistance=27.41 liquidity=36228112.0
- RTVC.CA: rank=27.0 outlook=BULLISH_WATCH outlook_score=73.15 sector_rank=13 price=4.23 support=3.73 resistance=4.36 liquidity=19533728.0
- ELWA.CA: rank=26.91 outlook=BULLISH_WATCH outlook_score=73.15 sector_rank=13 price=1.94 support=1.62 resistance=1.99 liquidity=6605257.5
- SKPC.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=71.65 sector_rank=8 price=17.37 support=15.61 resistance=18.15 liquidity=26454602.0
- LCSW.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=96 sector_rank=2 price=34.88 support=32.12 resistance=37.79 liquidity=14366946.0
- MILS.CA: rank=26.06 outlook=CONSTRUCTIVE outlook_score=66.15 sector_rank=13 price=216.45 support=175.0 resistance=248.4 liquidity=22423770.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=24.06 buy_ready=True sector_rank=13 price=308.3 support=240.49 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=10610151.0 spike=0.17
- ABUK.CA: score=25.82 buy_ready=True sector_rank=8 price=79.33 support=70.9 resistance=80.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=166290208.0 spike=1.71
- ACAMD.CA: score=14.06 buy_ready=False sector_rank=13 price=2.02 support=1.95 resistance=2.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=34712932.0 spike=0.6
- ACGC.CA: score=26.4 buy_ready=False sector_rank=1 price=14.27 support=10.14 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=79.23 liquidity=15859556.0 spike=0.36
- ADCI.CA: score=16.4 buy_ready=False sector_rank=13 price=292.12 support=245.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=53.07 liquidity=4341614.0 spike=0.21
- ADIB.CA: score=24.4 buy_ready=True sector_rank=7 price=53.7 support=50.1 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=29998242.0 spike=0.38
- ADPC.CA: score=22.06 buy_ready=False sector_rank=13 price=3.91 support=3.81 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=15087027.0 spike=0.33
- AFDI.CA: score=23.34 buy_ready=False sector_rank=13 price=53.92 support=50.48 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=47651900.0 spike=1.64
- AFMC.CA: score=9.06 buy_ready=False sector_rank=13 price=207.68 support=207.05 resistance=221.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54576932.0 spike=0.33
- AJWA.CA: score=19.06 buy_ready=False sector_rank=13 price=180.0 support=180.01 resistance=204.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.83 liquidity=48579764.0 spike=1.0
- ALCN.CA: score=22.4 buy_ready=False sector_rank=6 price=30.51 support=28.8 resistance=32.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.91 liquidity=16472097.0 spike=0.65
- ALUM.CA: score=23.06 buy_ready=False sector_rank=13 price=28.99 support=22.72 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=75.9 liquidity=17507718.0 spike=0.66
- AMER.CA: score=24.84 buy_ready=True sector_rank=9 price=6.53 support=4.44 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=116520736.0 spike=1.22
- AMES.CA: score=9.06 buy_ready=False sector_rank=13 price=138.35 support=135.0 resistance=150.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38476072.0 spike=0.54
- AMIA.CA: score=21.06 buy_ready=False sector_rank=13 price=19.15 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=83.62 liquidity=41330504.0 spike=0.8
- AMOC.CA: score=24.72 buy_ready=False sector_rank=11 price=11.44 support=8.55 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=74.26 liquidity=176964144.0 spike=1.2
- APSW.CA: score=9.18 buy_ready=False sector_rank=13 price=8.56 support=8.41 resistance=9.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.88 liquidity=1120081.25 spike=0.71
- ARAB.CA: score=29.0 buy_ready=False sector_rank=9 price=0.26 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.21 liquidity=195903936.0 spike=2.3
- ARCC.CA: score=23.4 buy_ready=False sector_rank=2 price=76.37 support=55.4 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.66 liquidity=26694356.0 spike=0.26
- AREH.CA: score=14.06 buy_ready=False sector_rank=13 price=1.44 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.0 liquidity=11252725.0 spike=0.38
- ARVA.CA: score=9.06 buy_ready=False sector_rank=13 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=17.06 buy_ready=False sector_rank=13 price=62.52 support=61.0 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.86 liquidity=18822404.0 spike=0.36
- ASPI.CA: score=26.5 buy_ready=False sector_rank=13 price=0.47 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.9 liquidity=125835560.0 spike=3.22
- ATLC.CA: score=17.03 buy_ready=True sector_rank=19 price=5.45 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=4592436.0 spike=0.23
- ATQA.CA: score=24.24 buy_ready=False sector_rank=8 price=11.79 support=9.66 resistance=11.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=81.17 liquidity=123121536.0 spike=1.42
- AXPH.CA: score=24.06 buy_ready=False sector_rank=13 price=1703.38 support=1121.56 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=88.41 liquidity=16218364.0 spike=1.5
- BINV.CA: score=13.88 buy_ready=False sector_rank=14 price=52.59 support=48.04 resistance=53.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74521208.0 spike=12.65
- BIOC.CA: score=9.06 buy_ready=False sector_rank=13 price=414.01 support=410.42 resistance=452.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=133234688.0 spike=0.54
- BTFH.CA: score=11.44 buy_ready=False sector_rank=19 price=2.98 support=2.94 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.32 liquidity=56772044.0 spike=0.28
- CAED.CA: score=24.06 buy_ready=False sector_rank=13 price=144.05 support=118.01 resistance=185.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.52 liquidity=15130239.0 spike=0.3
- CANA.CA: score=23.66 buy_ready=False sector_rank=7 price=41.87 support=36.62 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.33 liquidity=28831758.0 spike=1.63
- CCAP.CA: score=23.88 buy_ready=False sector_rank=14 price=5.79 support=5.14 resistance=5.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.8 liquidity=332587616.0 spike=0.56
- CCRS.CA: score=24.4 buy_ready=False sector_rank=13 price=2.75 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=53839268.0 spike=1.17
- CEFM.CA: score=20.88 buy_ready=True sector_rank=13 price=143.76 support=131.03 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.19 liquidity=6819387.0 spike=0.22
- CERA.CA: score=15.2 buy_ready=False sector_rank=13 price=1.28 support=1.23 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=6138849.0 spike=0.42
- CFGH.CA: score=-0.92 buy_ready=False sector_rank=13 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15241.9 spike=0.91
- CICH.CA: score=3.72 buy_ready=False sector_rank=19 price=12.15 support=11.92 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.86 liquidity=1288789.0 spike=0.19
- CIEB.CA: score=25.45 buy_ready=True sector_rank=7 price=24.71 support=23.75 resistance=25.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=9053531.0 spike=0.69
- CIRA.CA: score=20.17 buy_ready=False sector_rank=20 price=33.74 support=34.0 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.56 liquidity=12016053.0 spike=0.24
- CLHO.CA: score=22.4 buy_ready=False sector_rank=5 price=17.25 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=32872506.0 spike=0.53
- CNFN.CA: score=5.38 buy_ready=False sector_rank=19 price=4.76 support=4.68 resistance=5.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.03 liquidity=2944928.75 spike=0.15
- COMI.CA: score=22.4 buy_ready=False sector_rank=7 price=137.99 support=135.35 resistance=142.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=214340928.0 spike=0.44
- COPR.CA: score=21.06 buy_ready=False sector_rank=13 price=0.53 support=0.39 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=76.65 liquidity=39601636.0 spike=0.45
- COSG.CA: score=24.06 buy_ready=True sector_rank=13 price=1.8 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=18754214.0 spike=0.37
- CPCI.CA: score=14.33 buy_ready=False sector_rank=13 price=546.27 support=455.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.2 liquidity=2268226.25 spike=0.26
- CSAG.CA: score=18.61 buy_ready=True sector_rank=6 price=39.77 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.18 liquidity=4205719.0 spike=0.18
- DAPH.CA: score=14.06 buy_ready=False sector_rank=13 price=141.6 support=118.0 resistance=141.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=210891408.0 spike=4.68
- DEIN.CA: score=-0.94 buy_ready=False sector_rank=13 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=16.59 buy_ready=False sector_rank=10 price=28.4 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.12 liquidity=4230563.0 spike=0.27
- DSCW.CA: score=14.06 buy_ready=False sector_rank=13 price=1.89 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=22666084.0 spike=0.25
- DTPP.CA: score=23.02 buy_ready=False sector_rank=13 price=306.55 support=235.59 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=72.49 liquidity=64587836.0 spike=1.48
- EALR.CA: score=23.59 buy_ready=True sector_rank=13 price=400.18 support=364.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.44 liquidity=9533535.0 spike=0.2
- EASB.CA: score=22.62 buy_ready=True sector_rank=13 price=7.54 support=6.71 resistance=8.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=62.09 liquidity=6558463.5 spike=0.86
- EAST.CA: score=12.46 buy_ready=False sector_rank=10 price=35.29 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.87 liquidity=9096699.0 spike=0.14
- EBSC.CA: score=25.39 buy_ready=True sector_rank=13 price=1.97 support=1.85 resistance=2.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.45 liquidity=9305811.0 spike=1.01
- ECAP.CA: score=19.24 buy_ready=False sector_rank=13 price=33.41 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=15750175.0 spike=1.09
- EDFM.CA: score=14.92 buy_ready=False sector_rank=13 price=402.77 support=384.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=863428.81 spike=0.29
- EEII.CA: score=12.1 buy_ready=False sector_rank=13 price=3.13 support=2.93 resistance=3.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=65655220.0 spike=2.52
- EFIC.CA: score=21.4 buy_ready=False sector_rank=8 price=200.41 support=188.01 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.04 liquidity=22614276.0 spike=0.46
- EFID.CA: score=22.36 buy_ready=False sector_rank=10 price=31.3 support=26.7 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.77 liquidity=34406244.0 spike=0.38
- EFIH.CA: score=21.11 buy_ready=False sector_rank=17 price=23.35 support=22.15 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=106732560.0 spike=0.97
- EGAL.CA: score=23.42 buy_ready=False sector_rank=8 price=366.97 support=292.0 resistance=373.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=84.6 liquidity=134234400.0 spike=1.01
- EGAS.CA: score=21.75 buy_ready=False sector_rank=11 price=57.79 support=51.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=9434534.0 spike=0.4
- EGBE.CA: score=14.49 buy_ready=False sector_rank=7 price=0.54 support=0.47 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.99 liquidity=94071.38 spike=0.46
- EGCH.CA: score=22.4 buy_ready=False sector_rank=8 price=13.86 support=12.69 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=69872688.0 spike=0.57
- EGSA.CA: score=3.71 buy_ready=False sector_rank=15 price=8.69 support=8.65 resistance=8.99 source=Yahoo Finance as_of=2026-08-26T21:00:00+00:00 freshness=FRESH RSI=28.0 liquidity=0.0 spike=0.0
- EGTS.CA: score=19.4 buy_ready=False sector_rank=9 price=17.44 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.69 liquidity=22933390.0 spike=0.66
- EHDR.CA: score=22.06 buy_ready=False sector_rank=13 price=2.89 support=2.71 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=16375257.0 spike=0.43
- EKHO.CA: score=10.32 buy_ready=False sector_rank=11 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-26T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.4 buy_ready=False sector_rank=4 price=2.1 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.43 liquidity=30181540.0 spike=0.55
- ELKA.CA: score=10.4 buy_ready=False sector_rank=13 price=1.87 support=1.78 resistance=1.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108502632.0 spike=1.67
- ELNA.CA: score=10.54 buy_ready=False sector_rank=13 price=37.0 support=36.1 resistance=39.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=762549.06 spike=1.86
- ELSH.CA: score=20.54 buy_ready=False sector_rank=13 price=13.9 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=94392968.0 spike=1.74
- ELWA.CA: score=26.91 buy_ready=True sector_rank=13 price=1.94 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=6605257.5 spike=3.12
- EMFD.CA: score=33.4 buy_ready=True sector_rank=9 price=12.65 support=11.08 resistance=12.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=493415456.0 spike=6.05
- ENGC.CA: score=15.71 buy_ready=False sector_rank=13 price=45.72 support=40.11 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.68 liquidity=3649958.0 spike=0.13
- EOSB.CA: score=18.52 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-08-25T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=137492.75 spike=2.16
- EPCO.CA: score=22.06 buy_ready=False sector_rank=13 price=11.46 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=12868711.0 spike=0.69
- EPPK.CA: score=19.65 buy_ready=False sector_rank=13 price=12.64 support=12.3 resistance=15.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=5590103.0 spike=7.42
- ETEL.CA: score=23.71 buy_ready=True sector_rank=15 price=116.71 support=102.75 resistance=120.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=63.91 liquidity=94867584.0 spike=0.72
- ETRS.CA: score=23.0 buy_ready=True sector_rank=13 price=11.0 support=10.36 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=59.9 liquidity=8937025.0 spike=0.3
- EXPA.CA: score=22.62 buy_ready=False sector_rank=7 price=20.41 support=19.75 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.71 liquidity=41143812.0 spike=1.11
- FAIT.CA: score=22.84 buy_ready=False sector_rank=7 price=43.72 support=36.1 resistance=45.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=71.18 liquidity=6403914.5 spike=1.02
- FAITA.CA: score=15.33 buy_ready=False sector_rank=7 price=0.99 support=0.97 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.07 liquidity=68577.07 spike=1.43
- FERC.CA: score=23.4 buy_ready=True sector_rank=8 price=78.74 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=14473345.0 spike=0.81
- FWRY.CA: score=18.11 buy_ready=False sector_rank=17 price=18.98 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.58 liquidity=81307224.0 spike=0.66
- GBCO.CA: score=11.21 buy_ready=False sector_rank=21 price=28.41 support=27.51 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.46 liquidity=17543652.0 spike=0.35
- GDWA.CA: score=15.06 buy_ready=False sector_rank=13 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.07 liquidity=44534908.0 spike=0.71
- GGCC.CA: score=25.54 buy_ready=False sector_rank=13 price=0.94 support=0.81 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.01 liquidity=124601848.0 spike=2.74
- GIHD.CA: score=21.58 buy_ready=True sector_rank=13 price=64.21 support=56.51 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.46 liquidity=7522906.5 spike=0.29
- GMCI.CA: score=6.28 buy_ready=False sector_rank=13 price=1.87 support=1.83 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=902245.88 spike=1.66
- GRCA.CA: score=12.76 buy_ready=False sector_rank=13 price=82.3 support=74.01 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145477504.0 spike=2.85
- GSSC.CA: score=17.75 buy_ready=True sector_rank=13 price=283.16 support=274.0 resistance=301.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.55 liquidity=3692719.25 spike=0.19
- GTWL.CA: score=9.06 buy_ready=False sector_rank=13 price=238.02 support=219.0 resistance=247.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=541152640.0 spike=1.0
- HDBK.CA: score=22.4 buy_ready=False sector_rank=7 price=98.84 support=80.8 resistance=96.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.15 liquidity=28128422.0 spike=0.68
- HELI.CA: score=18.08 buy_ready=False sector_rank=9 price=7.89 support=7.34 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.81 liquidity=215768208.0 spike=1.34
- HRHO.CA: score=11.44 buy_ready=False sector_rank=19 price=25.69 support=25.49 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.76 liquidity=80112960.0 spike=0.82
- ICID.CA: score=21.06 buy_ready=False sector_rank=13 price=16.64 support=7.85 resistance=18.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=93.01 liquidity=15224474.0 spike=0.56
- IDRE.CA: score=15.86 buy_ready=False sector_rank=13 price=51.67 support=46.04 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.09 liquidity=3796643.25 spike=0.21
- IFAP.CA: score=24.7 buy_ready=False sector_rank=3 price=20.8 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=48539668.0 spike=1.65
- INFI.CA: score=24.06 buy_ready=True sector_rank=13 price=156.63 support=104.0 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.24 liquidity=17766874.0 spike=0.25
- IRON.CA: score=13.7 buy_ready=False sector_rank=8 price=30.68 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.23 liquidity=13739821.0 spike=1.15
- ISMA.CA: score=23.5 buy_ready=False sector_rank=13 price=38.42 support=29.5 resistance=39.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=88.94 liquidity=33000816.0 spike=1.22
- ISMQ.CA: score=19.4 buy_ready=False sector_rank=8 price=9.15 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.2 liquidity=16415027.0 spike=0.3
- ISPH.CA: score=17.4 buy_ready=False sector_rank=5 price=12.9 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.0 liquidity=31820032.0 spike=0.17
- JUFO.CA: score=23.36 buy_ready=False sector_rank=10 price=27.39 support=22.78 resistance=28.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=67.2 liquidity=22024010.0 spike=0.41
- KABO.CA: score=27.5 buy_ready=False sector_rank=1 price=9.27 support=7.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.29 liquidity=81807872.0 spike=2.05
- KWIN.CA: score=12.18 buy_ready=False sector_rank=13 price=120.79 support=105.0 resistance=127.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=149452688.0 spike=2.56
- KZPC.CA: score=24.06 buy_ready=False sector_rank=13 price=12.73 support=8.44 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=74.34 liquidity=21878464.0 spike=0.44
- LCSW.CA: score=26.4 buy_ready=True sector_rank=2 price=34.88 support=32.12 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=14366946.0 spike=0.46
- LUTS.CA: score=9.06 buy_ready=False sector_rank=13 price=1.16 support=1.11 resistance=1.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=154051520.0 spike=0.67
- MAAL.CA: score=24.06 buy_ready=True sector_rank=13 price=9.32 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.6 liquidity=10944785.0 spike=0.9
- MASR.CA: score=14.06 buy_ready=False sector_rank=13 price=7.71 support=7.45 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.19 liquidity=46862592.0 spike=0.69
- MBSC.CA: score=23.4 buy_ready=False sector_rank=2 price=401.33 support=240.02 resistance=434.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=80.79 liquidity=31644574.0 spike=0.38
- MCQE.CA: score=28.4 buy_ready=True sector_rank=2 price=233.54 support=178.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=64.88 liquidity=13177357.0 spike=0.23
- MCRO.CA: score=22.06 buy_ready=False sector_rank=13 price=1.49 support=1.44 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=44905480.0 spike=0.33
- MENA.CA: score=12.23 buy_ready=False sector_rank=9 price=6.85 support=6.82 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.11 liquidity=2827316.25 spike=0.48
- MEPA.CA: score=22.06 buy_ready=False sector_rank=13 price=1.82 support=1.78 resistance=2.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=13602251.0 spike=0.41
- MFPC.CA: score=26.84 buy_ready=False sector_rank=8 price=40.95 support=35.37 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.59 liquidity=174226080.0 spike=2.22
- MFSC.CA: score=19.66 buy_ready=False sector_rank=13 price=50.15 support=46.02 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=37.16 liquidity=7600501.5 spike=0.68
- MHOT.CA: score=22.29 buy_ready=False sector_rank=12 price=18.5 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.58 liquidity=12679265.0 spike=0.69
- MICH.CA: score=24.06 buy_ready=True sector_rank=13 price=49.71 support=39.01 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=17199230.0 spike=0.42
- MILS.CA: score=26.06 buy_ready=True sector_rank=13 price=216.45 support=175.0 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=22423770.0 spike=0.27
- MIPH.CA: score=24.3 buy_ready=True sector_rank=5 price=802.43 support=733.07 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.19 liquidity=8040513.0 spike=1.93
- MOED.CA: score=24.2 buy_ready=False sector_rank=13 price=0.81 support=0.65 resistance=0.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.5 liquidity=97557024.0 spike=1.07
- MOIL.CA: score=15.28 buy_ready=False sector_rank=11 price=0.69 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=581571.81 spike=1.19
- MOIN.CA: score=21.18 buy_ready=True sector_rank=13 price=34.33 support=23.11 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.03 liquidity=7123389.0 spike=0.21
- MOSC.CA: score=22.43 buy_ready=False sector_rank=13 price=317.62 support=283.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=74.56 liquidity=8372955.0 spike=0.56
- MPCI.CA: score=24.06 buy_ready=False sector_rank=13 price=406.31 support=287.01 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.12 liquidity=126657336.0 spike=0.75
- MPCO.CA: score=27.4 buy_ready=True sector_rank=3 price=2.21 support=1.88 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=64207024.0 spike=0.5
- MPRC.CA: score=14.06 buy_ready=False sector_rank=13 price=44.84 support=42.64 resistance=45.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106317432.0 spike=3.57
- MTIE.CA: score=16.21 buy_ready=False sector_rank=21 price=8.41 support=8.01 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.33 liquidity=32954838.0 spike=0.5
- NAHO.CA: score=12.17 buy_ready=False sector_rank=13 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=83.93 liquidity=134555.34 spike=1.49
- NCCW.CA: score=14.06 buy_ready=False sector_rank=13 price=5.8 support=5.59 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.65 liquidity=12169746.0 spike=0.39
- NEDA.CA: score=16.62 buy_ready=False sector_rank=13 price=2.79 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=557992.19 spike=0.66
- NHPS.CA: score=24.06 buy_ready=True sector_rank=13 price=91.0 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.08 liquidity=21055524.0 spike=0.62
- NINH.CA: score=26.06 buy_ready=True sector_rank=13 price=24.0 support=21.22 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.4 liquidity=23557050.0 spike=0.55
- NIPH.CA: score=24.4 buy_ready=True sector_rank=5 price=371.85 support=209.0 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=58.98 liquidity=162268512.0 spike=0.48
- OBRI.CA: score=22.06 buy_ready=False sector_rank=13 price=32.54 support=31.61 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.32 liquidity=15864327.0 spike=0.53
- OCDI.CA: score=22.4 buy_ready=False sector_rank=9 price=31.4 support=27.7 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.32 liquidity=108179080.0 spike=0.78
- OCPH.CA: score=14.36 buy_ready=False sector_rank=13 price=253.29 support=225.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=4301337.5 spike=0.19
- ODIN.CA: score=24.06 buy_ready=True sector_rank=13 price=3.23 support=2.64 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.31 liquidity=41074080.0 spike=0.89
- OFH.CA: score=26.06 buy_ready=False sector_rank=13 price=1.05 support=0.69 resistance=1.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=92.88 liquidity=239219792.0 spike=2.5
- OIH.CA: score=10.48 buy_ready=False sector_rank=14 price=2.1 support=1.98 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=253995520.0 spike=1.8
- OLFI.CA: score=17.1 buy_ready=False sector_rank=10 price=23.52 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=4739647.0 spike=0.08
- ORAS.CA: score=7.6 buy_ready=False sector_rank=18 price=843.89 support=811.01 resistance=849.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116522200.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=9 price=42.44 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=71244088.0 spike=0.5
- ORWE.CA: score=27.4 buy_ready=True sector_rank=1 price=26.35 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=36228112.0 spike=0.46
- PHAR.CA: score=22.4 buy_ready=False sector_rank=5 price=131.06 support=95.75 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.89 liquidity=101194272.0 spike=0.21
- PHDC.CA: score=14.4 buy_ready=False sector_rank=9 price=14.94 support=14.32 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=221030480.0 spike=0.95
- PHTV.CA: score=13.96 buy_ready=False sector_rank=13 price=340.16 support=312.0 resistance=447.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT RSI=51.82 liquidity=1896156.63 spike=0.7
- POUL.CA: score=19.99 buy_ready=True sector_rank=10 price=38.43 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=5625722.0 spike=0.22
- PRCL.CA: score=21.4 buy_ready=False sector_rank=2 price=32.84 support=32.0 resistance=37.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.03 liquidity=20217056.0 spike=0.82
- PRDC.CA: score=24.4 buy_ready=True sector_rank=9 price=9.36 support=8.7 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.91 liquidity=32850584.0 spike=0.55
- PRMH.CA: score=8.52 buy_ready=False sector_rank=13 price=2.6 support=2.46 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9460927.0 spike=0.66
- RACC.CA: score=16.34 buy_ready=False sector_rank=13 price=9.48 support=9.7 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.62 liquidity=41351216.0 spike=2.14
- RAKT.CA: score=9.21 buy_ready=False sector_rank=13 price=22.62 support=21.4 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=9.2 liquidity=688718.88 spike=2.23
- RAYA.CA: score=20.11 buy_ready=False sector_rank=16 price=7.25 support=6.95 resistance=7.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.76 liquidity=51406428.0 spike=0.72
- RMDA.CA: score=22.4 buy_ready=False sector_rank=5 price=6.08 support=5.08 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.65 liquidity=12923457.0 spike=0.11
- ROTO.CA: score=20.06 buy_ready=False sector_rank=13 price=44.41 support=41.85 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.26 liquidity=8000201.5 spike=0.37
- RREI.CA: score=20.57 buy_ready=False sector_rank=13 price=4.32 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=8507435.0 spike=0.12
- RTVC.CA: score=27.0 buy_ready=True sector_rank=13 price=4.23 support=3.73 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=65.56 liquidity=19533728.0 spike=2.47
- RUBX.CA: score=24.43 buy_ready=True sector_rank=13 price=12.85 support=12.02 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.46 liquidity=8366101.5 spike=0.47
- SAUD.CA: score=22.4 buy_ready=False sector_rank=7 price=22.9 support=21.4 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=10609306.0 spike=0.51
- SCEM.CA: score=24.4 buy_ready=True sector_rank=2 price=99.95 support=76.75 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=66.83 liquidity=195851552.0 spike=0.91
- SCFM.CA: score=20.7 buy_ready=True sector_rank=13 price=289.03 support=273.1 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=57.99 liquidity=6640961.0 spike=0.31
- SCTS.CA: score=14.1 buy_ready=True sector_rank=20 price=618.56 support=603.13 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.15 liquidity=1929842.5 spike=0.21
- SDTI.CA: score=24.86 buy_ready=True sector_rank=13 price=69.74 support=57.05 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.07 liquidity=45557656.0 spike=1.4
- SEIG.CA: score=16.05 buy_ready=True sector_rank=13 price=271.05 support=242.1 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.79 liquidity=1987412.88 spike=0.22
- SIPC.CA: score=22.06 buy_ready=False sector_rank=13 price=4.78 support=3.82 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.57 liquidity=10667894.0 spike=0.17
- SKPC.CA: score=26.4 buy_ready=True sector_rank=8 price=17.37 support=15.61 resistance=18.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=26454602.0 spike=0.37
- SMFR.CA: score=16.74 buy_ready=False sector_rank=13 price=261.87 support=228.88 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=7676473.0 spike=0.29
- SNFC.CA: score=13.22 buy_ready=False sector_rank=13 price=10.59 support=10.3 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.77 liquidity=15656578.0 spike=1.08
- SPIN.CA: score=27.5 buy_ready=True sector_rank=1 price=19.75 support=15.3 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=43279068.0 spike=1.05
- SPMD.CA: score=14.43 buy_ready=False sector_rank=13 price=0.46 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=7368326.5 spike=0.26
- SUGR.CA: score=24.36 buy_ready=False sector_rank=10 price=58.28 support=46.47 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.09 liquidity=32048492.0 spike=0.6
- SVCE.CA: score=24.06 buy_ready=False sector_rank=13 price=10.72 support=9.1 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.82 liquidity=44247056.0 spike=0.44
- SWDY.CA: score=26.4 buy_ready=False sector_rank=4 price=126.13 support=91.8 resistance=133.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=71.92 liquidity=44324332.0 spike=0.43
- TALM.CA: score=20.17 buy_ready=False sector_rank=20 price=17.52 support=17.2 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=17993808.0 spike=0.39
- TMGH.CA: score=20.1 buy_ready=False sector_rank=9 price=96.42 support=95.2 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.6 liquidity=323135808.0 spike=1.35
- TRTO.CA: score=18.15 buy_ready=False sector_rank=13 price=0.05 support=0.03 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=11980.68 spike=1.04
- UEFM.CA: score=16.08 buy_ready=True sector_rank=13 price=549.59 support=531.0 resistance=589.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=41.99 liquidity=2021335.5 spike=0.44
- UEGC.CA: score=16.22 buy_ready=False sector_rank=13 price=1.98 support=1.95 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.4 liquidity=85061832.0 spike=2.08
- UNIP.CA: score=22.06 buy_ready=False sector_rank=13 price=0.38 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.68 liquidity=17500306.0 spike=0.52
- UNIT.CA: score=17.02 buy_ready=True sector_rank=9 price=18.95 support=17.32 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.98 liquidity=2624961.25 spike=0.22
- WCDF.CA: score=13.45 buy_ready=False sector_rank=13 price=652.9 support=571.0 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=78.7 liquidity=2391863.25 spike=0.54
- WKOL.CA: score=22.81 buy_ready=True sector_rank=13 price=351.81 support=311.0 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.05 liquidity=6752929.5 spike=0.19
- ZEOT.CA: score=15.66 buy_ready=False sector_rank=13 price=13.8 support=12.1 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=3604614.25 spike=0.14
- ZMID.CA: score=24.24 buy_ready=False sector_rank=9 price=8.79 support=7.06 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.47 liquidity=355572288.0 spike=1.42

## Backtesting Lite
- EMFD.CA: 180d return=23.55%, max drawdown=-12.76%, MA20>MA50 days last20=3, as_of=2026-08-25T21:00:00+00:00
- ARAB.CA: 180d return=1.55%, max drawdown=-38.02%, MA20>MA50 days last20=20, as_of=2026-08-25T21:00:00+00:00
- MCQE.CA: 180d return=86.11%, max drawdown=-17.56%, MA20>MA50 days last20=17, as_of=2026-08-25T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=606 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/
- ARAB.CA: status=RECENT_ACCEPTED latest=2026-08-23 age_days=7 sources=3 expected=Arab Developers Holding summary=Recent evidence for Arab Developers Holding (ARAB.CA) includes financial results, capital increases, and disclosures to the EGX, with reports spanning from August 2025 to August 2026.
  - ARAB Developers Holding (ARAB.CA) - EGM Minutes (before Certification) (August 23, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEIdGITmBhETy4apZwq2Ghe61xl6HelAkqZa5ZZH2eVC10Pj8BRwcNPGaq_pgpGRMVZeUILApvcXpeGTVifwOdJlqnbfjLRp5DdwUFdJGaCmeQE6Aj2zlkhY4ejTLWjLmACzDUks33iz9gAiikQ9ri
  - Release from ARAB Developers Holding (ARAB.CA) Regarding the EGM (July 29, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEIdGITmBhETy4apZwq2Ghe61xl6HelAkqZa5ZZH2eVC10Pj8BRwcNPGaq_pgpGRMVZeUILApvcXpeGTVifwOdJlqnbfjLRp5DdwUFdJGaCmeQE6Aj2zlkhY4ejTLWjLmACzDUks33iz9gAiikQ9ri
  - ARAB Developers Holding (ARAB.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 20, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEIdGITmBhETy4apZwq2Ghe61xl6HelAkqZa5ZZH2eVC10Pj8BRwcNPGaq_pgpGRMVZeUILApvcXpeGTVifwOdJlqnbfjLRp5DdwUFdJGaCmeQE6Aj2zlkhY4ejTLWjLmACzDUks33iz9gAiikQ9ri
- MCQE.CA: status=RECENT_ACCEPTED latest=2026-08-06 age_days=24 sources=3 expected=Misr Cement Qena summary=Misr Cement Qena (MCQE.CA) has reported strong financial performance in H1 2026 and FY 2025, with plans for alternative fuel investments. The company also made several disclosures to the EGX.
  - Misr Cement Qena logs 94.4% YoY higher consolidated profits in H1 2026 (August 6, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnMVoR4SC8fjyfforV4ciw_sfNeFBHENxIs770Zr0UA5wTThdvSL3nyq0sMdH6MfvHdwQxKIbvlHODxanxealS4b8XSI3_2-2yzzgksfwLBBCp0nsLfutmEBns5tKqZbBpdowPsCltf98-qzWQ-l_EWg==
  - Misr Cement Qena plans alternative fuel investments at Qena, Minya plants (June 25, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnMVoR4SC8fjyfforV4ciw_sfNeFBHENxIs770Zr0UA5wTThdvSL3nyq0sMdH6MfvHdwQxKIbvlHODxanxealS4b8XSI3_2-2yzzgksfwLBBCp0nsLfutmEBns5tKqZbBpdowPsCltf98-qzWQ-l_EWg==
  - Misr Cement (Qena) (MCQE.CA) Reports Its Financial Results (Consolidated) for The Period ending 31/12/2025 (March 5, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERU1p6NoR7H0KyNWF_eAJH33iIqhuRL3NZwOALNNYWcG0jABjNuqFF3bThhD3sBagZsWg7dUG0FnKkH0c9uwbGa064rdIc--YiX5Xs7OXaA428DDu4DcflQitGiG6F6vn_c1n2_XshI1n6JU7JipgU52jXqTsjAFZJ9QSH1q3OEQ==
- SPIN.CA: status=RECENT_ACCEPTED latest=2026-08-02 age_days=28 sources=3 expected=Alexandria Spinning and Weaving summary=Alexandria Spinning and Weaving (SPIN.CA) has reported Q2 2026 earnings and is subject to a proposed acquisition of a 20% stake. Financial statements and key metrics for the last 12 months are also available.
  - Alexandria Spinning & Weaving Co. Reports Earnings Results for the Second Quarter and Six Months Ended December 31, 2025 (August 2, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNTwQijDdCdC8fPnwE8OpYtSBu99d6NTukFXr3H96HqwkD84zdMUNSttXc17GL4hrzpnd4Lf5auJUb1WO_zrl60RFjHI_Ua5WF8YK301K8jIxmmpknb5LCrE4Lu80VqDkyXemd7OdOqf4D5aGHE-q8hmvpPjXB9GZlmnZwoBZl4TkNmSDKk_I=
  - New Construction Chemical and ESCOM Company proposed to acquire 20% stake in Alexandria Spinning & Weaving Co. (April 4, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNTwQijDdCdC8fPnwE8OpYtSBu99d6NTukFXr3H96HqwkD84zdMUNSttXc17GL4hrzpnd4Lf5auJUb1WO_zrl60RFjHI_Ua5WF8YK301K8jIxmmpknb5LCrE4Lu80VqDkyXemd7OdOqf4D5aGHE-q8hmvpPjXB9GZlmnZwoBZl4TkNmSDKk_I=
  - Alexandria Spinning & Weaving Income Statement Q2 2026 (Released in 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIRW0HZINUZKMlfIGW01tU2m6CU9XbWj4dwl9qD_HIuwbSc4jCKYM17UDgejf96TJnV-RGJU4S8ari3Bl8Y-g75coDXbZR91wcpE06IXfBq-2UBNtg3onkx_XX-RzFchw4iLR2Em0JIng1YQQsAx_RrTD1tqBsh_6_nr8gdFOXP6JkYg==
- KABO.CA: status=RECENT_ACCEPTED latest=2026-08-19 age_days=11 sources=3 expected=El Nasr Clothing and Textiles summary=El Nasr Clothing and Textiles (KABO.CA) has released Q1 2026 and FY 2025 earnings, proposed a capital increase, and made several disclosures to the EGX. The company's financial performance for fiscal year 2024 and Q3 2025 is also available.
  - El Nasr Clothes & Textiles (Kabo) (KABO.CA) - Release Regarding a Disclosure Form (August 19, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHindZK8OIUoT-tJrAKS5hEXCXaBu4_a-326s0axtgQz5ilP2kOv0Je5FIcvp-yuvzhaCilouhbW02g87Yl4VkAadYzhs2uCJqgXIV8GT0AmpUfIGczZzBOlSuJE5kk5m4J8mNt1Uzr8rDKOFK3aZe5
  - El Nasr Clothes & Textiles (Kabo) (KABO.CA) - Release Concerning the Periodic Disclosure to Shareholders (July 15, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHindZK8OIUoT-tJrAKS5hEXCXaBu4_a-326s0axtgQz5ilP2kOv0Je5FIcvp-yuvzhaCilouhbW02g87Yl4VkAadYzhs2uCJqgXIV8GT0AmpUfIGczZzBOlSuJE5kk5m4J8mNt1Uzr8rDKOFK3aZe5
  - El Nasr Clothes & Textiles (Kabo) (KABO.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHindZK8OIUoT-tJrAKS5hEXCXaBu4_a-326s0axtgQz5ilP2kOv0Je5FIcvp-yuvzhaCilouhbW02g87Yl4VkAadYzhs2uCJqgXIV8GT0AmpUfIGczZzBOlSuJE5kk5m4J8mNt1Uzr8rDKOFK3aZe5
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=606 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- ORWE.CA: status=RECENT_ACCEPTED latest=2026-07-28 age_days=33 sources=3 expected=Oriental Weavers summary=Oriental Weavers (ORWE.CA) has been active with several EGX disclosures, board meetings, and AGM minutes. The company reported strong financial results for 2025 and H1 2025, along with dividend disbursements and strategic agreements.
  - Oriental Weavers (ORWE.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 28, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJMfzeBag3ml2rTZZm0hzjeOPkva1sQda35qiKZHUiapo00icGF5Tgsfn57KyAg7s8hxQnTV36PY39AFUN40FVHRAlQhsGFCz0X5lT9QVl1NNfVC1fDSlalCJyHWDvEDuPzbBmuPDNIMFVNG5RulV_
  - Release from Oriental Weavers (ORWE.CA) Concerning the Board of Directors' Minutes (May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJMfzeBag3ml2rTZZm0hzjeOPkva1sQda35qiKZHUiapo00icGF5Tgsfn57KyAg7s8hxQnTV36PY39AFUN40FVHRAlQhsGFCz0X5lT9QVX1NNfVC1fDSlalCJyHWDvEDuPzbBmuPDNIMFVNG5RulV_
  - Oriental Weavers (ORWE.CA) - Minutes of the Board of Directors' Meeting (May 21, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJMfzeBag3ml2rTZZm0hzjeOPkva1sQda35qiKZHUiapo00icGF5Tgsfn57KyAg7s8hxQnTV36PY39AFUN40FVHRAlQhsGFCz0X5lT9QVX1NNfVC1fDSlalCJyHWDvEDuPzbBmuPDNIMFVNG5RulV_
- RTVC.CA: status=RECENT_ACCEPTED latest=2026-07-13 age_days=48 sources=3 expected=Remco Tourism Villages Construction summary=Remco Tourism Villages Construction (RTVC.CA) has made recent disclosures to the EGX, including AGM minutes and shareholder structure updates. The company was also involved in acquisition activities and reported its 2024 annual and Q4 2024 revenue.
  - Remco for Touristic Villages Construction (RTVC.CA) - Disclosure Form for the BoD & the Shareholders' Structure (July 13, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfFRhqTv_0X72nblsSezS3B8oujwICZ70l3JUsdgTVdH5S-I7ff4cs8NOMmsT5Ed7hhdNnmgbxqbu5Od2Dscks16t9Q2VYnDCPyMn5aQoIq7jjtHdSQgEv7N5_zz-UHaUKgkp1JCylWWTIBqnDBO0ZDAXaA8Ntxj_LIYbGHM6iTl8=
  - Remco for Touristic Villages Construction (RTVC.CA) - AGM Minutes (Notarized) (June 28, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfFRhqTv_0X72nblsSezS3B8oujwICZ70l3JUsdgTVdH5S-I7ff4cs8NOMmsT5Ed7hhdNnmgbxqbu5Od2Dscks16t9Q2VYnDCPyMn5aQoIq7jjtHdSQgEv7N5_zz-UHaUKgkp1JCylWWTIBqnDBO0ZDAXaA8Ntxj_LIYbGHM6iTl8=
  - Remco for Touristic Villages Construction (RTVC.CA) - AGM Resolutions (June 7, 2026): https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfFRhqTv_0X72nblsSezS3B8oujwICZ70l3JUsdgTVdH5S-I7ff4cs8NOMmsT5Ed7hhdNnmgbxqbu5Od2Dscks16t9Q2VYnDCPyMn5aQoIq7jjtHdSQgEv7N5_zz-UHaUKgkp1JCylWWTIBqnDBO0ZDAXaA8Ntxj_LIYbGHM6iTl8=

## Warnings
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
