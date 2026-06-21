# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-21T10:09:10.610524+00:00
Generated Cairo: 2026-06-21 13:09
Run timing: target 09:15 Cairo | generated Cairo 2026-06-21 13:09 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-21 13:03

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 62
- Data quality issues: 0
- Tradeable price/liquidity tickers: 165/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 21
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 44.44% / above MA50 55.56%
- EGX70 regime: BULLISH / above MA20 60.0% / above MA50 80.0%
- Sector breadth: 71.43%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- TMGH.CA: liquidity=506016416.0 spike=1.11 score=24.62
- ANFI.CA: liquidity=340087598.93 spike=4.21 score=27.9
- PHDC.CA: liquidity=254219232.0 spike=0.61 score=24.4
- BTFH.CA: liquidity=232102128.0 spike=1.12 score=24.64
- CCAP.CA: liquidity=226473984.0 spike=0.26 score=21.42

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner highlighted a handful of EGX tickers that cleared evidence, liquidity and technical gates. Most show bullish watch outlooks, are in accumulation‑spike or tradeable liquidity regimes, and sit near short‑term resistance with modest support buffers. EGX30 remains bearish, limiting broad market upside, while EGX70 is bullish, allowing selective small‑mid swing opportunities. Sector breadth is healthy (71 %); automotive, agriculture and healthcare lead, but non‑bank financials also show strong liquidity spikes. Uncertainty remains high due to mixed index trends and proximity of many stocks to resistance levels.
- KWIN, ATLC, MASR, HRHO and MTIE rank highest – buy‑ready, bullish outlook, liquidity spikes and support 6‑14 % away, resistance within 1 %‑4 %
- EGX30 bearish (44 % above MA20) curtails risk; EGX70 bullish (60 % above MA20) supports selective swing bias
- Sector breadth 71 % with automotive & distribution leading; non‑bank financials show the strongest liquidity spikes
- Most tickets sit close to resistance; momentum is extended, so watch for pull‑backs or breakout confirmation
- Overall risk mode is SELECTIVE_SMALL_MID_SWINGS – stay cautious, monitor resistance breaches and index regime shifts

## Top Liquidity Spikes
- TRTO.CA: spike=271.16 liquidity=266831.58 outlook=NEUTRAL score=41.76 buy_ready=False
- EASB.CA: spike=11.67 liquidity=51896916.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ROTO.CA: spike=7.93 liquidity=107207440.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- CIRA.CA: spike=5.93 liquidity=92216728.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ZEOT.CA: spike=4.63 liquidity=76731888.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=9.53 5d=3.65% 20d=7.93% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=9.07 5d=8.27% 20d=12.06% aboveMA50=50.0%
- #3 Healthcare: score=8.04 5d=1.98% 20d=1.48% aboveMA50=100.0%
- #4 Non-bank Financial Services: score=7.3 5d=0.67% 20d=0.0% aboveMA50=60.0%
- #5 Real Estate: score=7.06 5d=1.98% 20d=5.47% aboveMA50=84.62%
- #6 Energy & Petrochemicals: score=5.06 5d=0.54% 20d=2.33% aboveMA50=75.0%
- #7 General / Verified EGX Expansion: score=4.76 5d=1.02% 20d=0.48% aboveMA50=62.5%
- #8 Transportation & Logistics: score=4.76 5d=2.88% 20d=1.17% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- PHAR.CA: BULLISH_WATCH score=99.04 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- MTIE.CA: BULLISH_WATCH score=97.53 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- NIPH.CA: BULLISH_WATCH score=94.04 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- RMDA.CA: BULLISH_WATCH score=94.04 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CLHO.CA: BULLISH_WATCH score=94.04 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MPRC.CA: BULLISH_WATCH score=91.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ISPH.CA: BULLISH_WATCH score=88.04 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- NHPS.CA: BULLISH_WATCH score=85.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- MENA.CA: BULLISH_WATCH score=83.06 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- BTFH.CA: BULLISH_WATCH score=82.3 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- KWIN.CA: rank=30.9 outlook=BULLISH_WATCH outlook_score=77.76 sector_rank=7 price=76.73 support=69.0 resistance=77.0 liquidity=17251866.0
- ATLC.CA: rank=29.18 outlook=BULLISH_WATCH outlook_score=80.3 sector_rank=4 price=5.18 support=4.7 resistance=5.27 liquidity=10473545.0
- MASR.CA: rank=28.48 outlook=BULLISH_WATCH outlook_score=81.76 sector_rank=7 price=7.48 support=6.54 resistance=7.4 liquidity=73525776.0
- HRHO.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=79.3 sector_rank=4 price=27.54 support=25.8 resistance=27.9 liquidity=77354128.0
- GBCO.CA: rank=27.4 outlook=CONSTRUCTIVE outlook_score=69.53 sector_rank=1 price=28.75 support=25.25 resistance=28.81 liquidity=23620678.0
- MTIE.CA: rank=27.12 outlook=BULLISH_WATCH outlook_score=97.53 sector_rank=1 price=9.19 support=8.65 resistance=9.6 liquidity=7717805.0
- PHAR.CA: rank=27.12 outlook=BULLISH_WATCH outlook_score=99.04 sector_rank=3 price=87.52 support=83.02 resistance=88.2 liquidity=52619136.0
- MPRC.CA: rank=26.82 outlook=BULLISH_WATCH outlook_score=91.76 sector_rank=7 price=33.71 support=30.61 resistance=34.55 liquidity=49384108.0
- ADCI.CA: rank=26.42 outlook=BULLISH_WATCH outlook_score=77.76 sector_rank=7 price=233.44 support=206.51 resistance=230.9 liquidity=22183388.0
- LCSW.CA: rank=26.41 outlook=BULLISH_WATCH outlook_score=78.82 sector_rank=16 price=28.2 support=26.0 resistance=28.3 liquidity=23119378.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=14.67 buy_ready=False sector_rank=7 price=207.36 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=54.01 liquidity=767108.81 spike=0.12
- ABUK.CA: score=12.69 buy_ready=False sector_rank=21 price=71.71 support=71.06 resistance=86.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=4.08 liquidity=172757280.0 spike=1.24
- ACAMD.CA: score=23.9 buy_ready=True sector_rank=7 price=2.35 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=71822008.0 spike=0.57
- ACGC.CA: score=20.43 buy_ready=False sector_rank=13 price=9.52 support=9.11 resistance=10.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=9008522.0 spike=0.16
- ADCI.CA: score=26.42 buy_ready=True sector_rank=7 price=233.44 support=206.51 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=68.7 liquidity=22183388.0 spike=3.26
- ADIB.CA: score=25.85 buy_ready=True sector_rank=9 price=47.16 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.93 liquidity=28831218.0 spike=0.26
- ADPC.CA: score=23.9 buy_ready=True sector_rank=7 price=3.75 support=3.45 resistance=4.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=12388532.0 spike=0.48
- AFDI.CA: score=21.97 buy_ready=True sector_rank=7 price=44.22 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=54.73 liquidity=8066778.0 spike=0.49
- AFMC.CA: score=12.68 buy_ready=False sector_rank=7 price=70.74 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=778214.44 spike=0.14
- AJWA.CA: score=22.9 buy_ready=False sector_rank=7 price=174.69 support=130.01 resistance=188.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=93.13 liquidity=22812868.0 spike=0.88
- ALCN.CA: score=13.75 buy_ready=False sector_rank=8 price=28.61 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=4849746.0 spike=0.33
- ALUM.CA: score=13.95 buy_ready=False sector_rank=7 price=23.46 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=49.34 liquidity=2041789.25 spike=0.13
- AMER.CA: score=22.4 buy_ready=False sector_rank=5 price=2.52 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=16989480.0 spike=0.17
- AMES.CA: score=8.54 buy_ready=False sector_rank=7 price=49.82 support=48.0 resistance=54.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=30.05 liquidity=2640781.0 spike=0.66
- AMIA.CA: score=14.27 buy_ready=True sector_rank=7 price=9.04 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=2362454.25 spike=0.15
- AMOC.CA: score=14.02 buy_ready=False sector_rank=6 price=7.85 support=7.71 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=32845928.0 spike=0.45
- ANFI.CA: score=27.9 buy_ready=False sector_rank=7 price=41.4 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-16T21:00:00+00:00 freshness=FRESH RSI=98.86 liquidity=340087598.93 spike=4.21
- APSW.CA: score=2.9 buy_ready=False sector_rank=7 price=8.53 support=8.24 resistance=9.21 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=28.92 liquidity=0.0 spike=0.0
- ARAB.CA: score=22.4 buy_ready=False sector_rank=5 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=67.57 liquidity=21315976.0 spike=0.25
- ARCC.CA: score=20.24 buy_ready=False sector_rank=16 price=56.22 support=53.6 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.97 liquidity=9109963.0 spike=0.25
- AREH.CA: score=13.56 buy_ready=False sector_rank=7 price=1.67 support=1.63 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92917256.0 spike=3.33
- ARVA.CA: score=25.2 buy_ready=False sector_rank=7 price=11.11 support=7.71 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=72.75 liquidity=49617104.0 spike=1.65
- ASCM.CA: score=23.9 buy_ready=False sector_rank=7 price=59.44 support=47.3 resistance=64.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=73.67 liquidity=12413221.0 spike=0.18
- ASPI.CA: score=23.9 buy_ready=True sector_rank=7 price=0.32 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=60.09 liquidity=31280024.0 spike=0.46
- ATLC.CA: score=29.18 buy_ready=True sector_rank=4 price=5.18 support=4.7 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=10473545.0 spike=2.39
- ATQA.CA: score=16.21 buy_ready=False sector_rank=21 price=9.57 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=10084086.0 spike=0.29
- AXPH.CA: score=7.72 buy_ready=False sector_rank=7 price=1117.88 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=28.66 liquidity=811325.69 spike=0.43
- BINV.CA: score=15.42 buy_ready=True sector_rank=14 price=47.17 support=41.0 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=63.48 liquidity=1997902.38 spike=0.18
- BIOC.CA: score=15.25 buy_ready=True sector_rank=7 price=72.75 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=48.88 liquidity=1350402.25 spike=0.49
- BTFH.CA: score=24.64 buy_ready=True sector_rank=4 price=3.13 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=43.66 liquidity=232102128.0 spike=1.12
- CAED.CA: score=11.9 buy_ready=False sector_rank=7 price=74.51 support=73.65 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14005030.0 spike=2.5
- CANA.CA: score=19.75 buy_ready=True sector_rank=9 price=38.03 support=34.11 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=3900431.25 spike=0.37
- CCAP.CA: score=21.42 buy_ready=False sector_rank=14 price=5.11 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=226473984.0 spike=0.26
- CCRS.CA: score=22.1 buy_ready=True sector_rank=7 price=2.47 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=8200991.0 spike=0.35
- CEFM.CA: score=9.62 buy_ready=False sector_rank=7 price=103.16 support=100.53 resistance=111.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=41.26 liquidity=717495.88 spike=0.2
- CERA.CA: score=21.92 buy_ready=False sector_rank=7 price=1.25 support=1.13 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=16952494.0 spike=1.01
- CFGH.CA: score=2.9 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- CICH.CA: score=9.28 buy_ready=False sector_rank=4 price=12.23 support=12.14 resistance=12.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7302459.5 spike=2.29
- CIEB.CA: score=16.29 buy_ready=False sector_rank=9 price=23.8 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=60.1 liquidity=1442824.88 spike=0.2
- CIRA.CA: score=13.8 buy_ready=False sector_rank=11 price=29.02 support=27.17 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=92216728.0 spike=5.93
- CLHO.CA: score=17.36 buy_ready=True sector_rank=3 price=15.59 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=56.73 liquidity=1955509.75 spike=0.07
- CNFN.CA: score=14.4 buy_ready=False sector_rank=4 price=4.78 support=4.54 resistance=4.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53550516.0 spike=3.56
- COMI.CA: score=25.85 buy_ready=True sector_rank=9 price=136.45 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=63563968.0 spike=0.1
- COPR.CA: score=8.9 buy_ready=False sector_rank=7 price=0.39 support=0.39 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35168816.0 spike=0.84
- COSG.CA: score=23.9 buy_ready=True sector_rank=7 price=1.61 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=21270696.0 spike=0.31
- CPCI.CA: score=13.05 buy_ready=False sector_rank=7 price=369.91 support=345.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=71.29 liquidity=1142448.75 spike=0.53
- CSAG.CA: score=16.13 buy_ready=True sector_rank=8 price=31.43 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=50.66 liquidity=2227045.75 spike=0.17
- DAPH.CA: score=18.28 buy_ready=True sector_rank=7 price=81.58 support=76.6 resistance=83.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=2377050.5 spike=0.21
- DEIN.CA: score=9.9 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=7.3 buy_ready=False sector_rank=12 price=26.01 support=25.75 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5207430.0 spike=2.7
- DSCW.CA: score=23.9 buy_ready=False sector_rank=7 price=1.84 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=19844510.0 spike=0.38
- DTPP.CA: score=4.52 buy_ready=False sector_rank=7 price=117.05 support=114.0 resistance=132.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=16.62 liquidity=614189.88 spike=0.32
- EALR.CA: score=12.63 buy_ready=False sector_rank=7 price=356.05 support=346.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=54.36 liquidity=730446.44 spike=0.2
- EASB.CA: score=13.9 buy_ready=False sector_rank=7 price=8.7 support=8.57 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51896916.0 spike=11.67
- EAST.CA: score=24.89 buy_ready=True sector_rank=12 price=38.91 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=56.27 liquidity=9200665.0 spike=0.14
- EBSC.CA: score=15.21 buy_ready=False sector_rank=7 price=1.92 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=70.91 liquidity=1310467.63 spike=0.48
- ECAP.CA: score=27.34 buy_ready=False sector_rank=7 price=34.01 support=29.02 resistance=32.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=86.18 liquidity=16716228.0 spike=3.22
- EDFM.CA: score=12.43 buy_ready=False sector_rank=7 price=332.36 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=52.43 liquidity=525200.63 spike=0.79
- EEII.CA: score=23.9 buy_ready=True sector_rank=7 price=2.5 support=2.27 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=13902531.0 spike=0.77
- EFIC.CA: score=1.21 buy_ready=False sector_rank=21 price=204.02 support=192.01 resistance=215.0 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=23.12 liquidity=0.0 spike=0.0
- EFID.CA: score=18.69 buy_ready=False sector_rank=12 price=27.97 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=19888278.0 spike=0.27
- EFIH.CA: score=21.23 buy_ready=False sector_rank=15 price=21.41 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=35.74 liquidity=12629771.0 spike=0.24
- EGAL.CA: score=12.21 buy_ready=False sector_rank=21 price=296.4 support=297.1 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=33820428.0 spike=0.43
- EGAS.CA: score=17.59 buy_ready=True sector_rank=6 price=52.55 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=69.09 liquidity=5568677.0 spike=0.45
- EGBE.CA: score=11.86 buy_ready=False sector_rank=9 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:58 AM market time freshness=DELAYED_CURRENT RSI=44.02 liquidity=8058.82 spike=0.07
- EGCH.CA: score=18.15 buy_ready=False sector_rank=21 price=13.73 support=12.9 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=7935873.0 spike=0.08
- EGSA.CA: score=5.93 buy_ready=False sector_rank=18 price=8.78 support=8.55 resistance=9.19 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=26.47 liquidity=0.0 spike=0.0
- EGTS.CA: score=9.4 buy_ready=False sector_rank=5 price=18.89 support=18.3 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=66191084.0 spike=0.53
- EHDR.CA: score=23.81 buy_ready=True sector_rank=7 price=2.72 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=9903791.0 spike=0.17
- EKHO.CA: score=14.02 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=16.81 buy_ready=False sector_rank=10 price=2.14 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=4979468.5 spike=0.19
- ELKA.CA: score=24.9 buy_ready=True sector_rank=7 price=1.33 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=24662228.0 spike=0.6
- ELNA.CA: score=14.25 buy_ready=False sector_rank=7 price=39.72 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=50.98 liquidity=345712.63 spike=0.85
- ELSH.CA: score=8.9 buy_ready=False sector_rank=7 price=12.89 support=12.71 resistance=13.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56076568.0 spike=0.3
- ELWA.CA: score=15.72 buy_ready=True sector_rank=7 price=2.09 support=1.84 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1817606.0 spike=0.58
- EMFD.CA: score=26.4 buy_ready=False sector_rank=5 price=12.43 support=10.02 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=71.01 liquidity=46679688.0 spike=0.17
- ENGC.CA: score=8.27 buy_ready=False sector_rank=7 price=37.92 support=37.0 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9361024.0 spike=0.67
- EOSB.CA: score=17.9 buy_ready=False sector_rank=7 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=21.52 buy_ready=True sector_rank=7 price=9.19 support=8.63 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=62.42 liquidity=3611534.5 spike=0.33
- EPPK.CA: score=12.9 buy_ready=False sector_rank=7 price=12.34 support=11.67 resistance=12.89 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=47.1 liquidity=0.0 spike=0.0
- ETEL.CA: score=12.93 buy_ready=False sector_rank=18 price=93.73 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=32.31 liquidity=28681376.0 spike=0.35
- ETRS.CA: score=8.9 buy_ready=False sector_rank=7 price=10.6 support=10.31 resistance=10.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30328664.0 spike=0.5
- EXPA.CA: score=21.85 buy_ready=False sector_rank=9 price=18.43 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=16877096.0 spike=0.49
- FAIT.CA: score=13.36 buy_ready=False sector_rank=9 price=37.24 support=35.01 resistance=38.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=49.14 liquidity=1507469.38 spike=0.31
- FAITA.CA: score=11.87 buy_ready=False sector_rank=9 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=13999.16 spike=0.31
- FERC.CA: score=3.31 buy_ready=False sector_rank=21 price=75.65 support=75.0 resistance=79.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=24.38 liquidity=2098547.5 spike=0.52
- FWRY.CA: score=13.23 buy_ready=False sector_rank=15 price=18.82 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=27108262.0 spike=0.09
- GBCO.CA: score=27.4 buy_ready=True sector_rank=1 price=28.75 support=25.25 resistance=28.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=66.73 liquidity=23620678.0 spike=0.22
- GDWA.CA: score=21.64 buy_ready=True sector_rank=7 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.94 liquidity=6734886.5 spike=0.48
- GGCC.CA: score=17.54 buy_ready=True sector_rank=7 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=59.38 liquidity=4635197.0 spike=0.6
- GIHD.CA: score=16.5 buy_ready=True sector_rank=7 price=42.03 support=35.15 resistance=43.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=59.11 liquidity=2593738.5 spike=0.74
- GMCI.CA: score=15.9 buy_ready=False sector_rank=7 price=1.79 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=54.05 liquidity=0.0 spike=0.0
- GRCA.CA: score=4.81 buy_ready=False sector_rank=7 price=53.55 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=30.47 liquidity=907716.88 spike=0.15
- GSSC.CA: score=7.09 buy_ready=False sector_rank=7 price=248.75 support=228.1 resistance=263.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=21.11 liquidity=3182689.5 spike=0.65
- GTWL.CA: score=17.73 buy_ready=True sector_rank=7 price=49.07 support=45.47 resistance=52.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=1822098.0 spike=0.24
- HDBK.CA: score=13.85 buy_ready=False sector_rank=9 price=155.66 support=146.25 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60063208.0 spike=3.71
- HELI.CA: score=24.4 buy_ready=True sector_rank=5 price=6.63 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=50.83 liquidity=47570176.0 spike=0.32
- HRHO.CA: score=28.4 buy_ready=True sector_rank=4 price=27.54 support=25.8 resistance=27.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.13 liquidity=77354128.0 spike=0.51
- ICID.CA: score=8.1 buy_ready=False sector_rank=7 price=7.6 support=7.4 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9194162.0 spike=0.56
- IDRE.CA: score=23.88 buy_ready=True sector_rank=7 price=45.56 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=9979247.0 spike=0.44
- IFAP.CA: score=12.67 buy_ready=False sector_rank=2 price=19.17 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=35.91 liquidity=2272605.25 spike=0.3
- INFI.CA: score=11.42 buy_ready=False sector_rank=7 price=94.52 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=24.9 liquidity=8515048.0 spike=0.86
- IRON.CA: score=18.85 buy_ready=False sector_rank=21 price=32.04 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.32 liquidity=10555689.0 spike=1.32
- ISMA.CA: score=18.9 buy_ready=False sector_rank=7 price=30.05 support=24.05 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=80.54 liquidity=15921772.0 spike=0.37
- ISMQ.CA: score=24.21 buy_ready=True sector_rank=21 price=8.25 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=30855364.0 spike=0.44
- ISPH.CA: score=25.4 buy_ready=True sector_rank=3 price=12.4 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=59.28 liquidity=73170776.0 spike=0.57
- JUFO.CA: score=24.73 buy_ready=True sector_rank=12 price=32.07 support=26.8 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=69.55 liquidity=59311980.0 spike=1.52
- KABO.CA: score=16.54 buy_ready=False sector_rank=13 price=6.25 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=5115603.5 spike=0.26
- KWIN.CA: score=30.9 buy_ready=True sector_rank=7 price=76.73 support=69.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=62.26 liquidity=17251866.0 spike=3.55
- KZPC.CA: score=18.05 buy_ready=True sector_rank=7 price=10.77 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=57.42 liquidity=4147189.25 spike=0.47
- LCSW.CA: score=26.41 buy_ready=True sector_rank=16 price=28.2 support=26.0 resistance=28.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=42.74 liquidity=23119378.0 spike=2.64
- LUTS.CA: score=23.02 buy_ready=False sector_rank=7 price=0.76 support=0.54 resistance=0.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=83.88 liquidity=71372192.0 spike=2.06
- MAAL.CA: score=5.45 buy_ready=False sector_rank=7 price=6.67 support=6.46 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6545969.0 spike=0.47
- MASR.CA: score=28.48 buy_ready=True sector_rank=7 price=7.48 support=6.54 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=73525776.0 spike=1.29
- MBSC.CA: score=21.13 buy_ready=False sector_rank=16 price=251.0 support=247.43 resistance=273.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=48.2 liquidity=11484452.0 spike=0.26
- MCQE.CA: score=8.76 buy_ready=False sector_rank=16 price=177.82 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=25.31 liquidity=5630484.5 spike=0.35
- MCRO.CA: score=20.9 buy_ready=False sector_rank=7 price=1.24 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=16818386.0 spike=0.35
- MENA.CA: score=17.42 buy_ready=True sector_rank=5 price=6.87 support=6.15 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=3016264.0 spike=0.18
- MEPA.CA: score=23.9 buy_ready=True sector_rank=7 price=1.71 support=1.63 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=12033856.0 spike=0.7
- MFPC.CA: score=12.99 buy_ready=False sector_rank=21 price=37.24 support=36.9 resistance=45.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=4.77 liquidity=121873024.0 spike=1.39
- MFSC.CA: score=8.26 buy_ready=False sector_rank=7 price=44.66 support=43.0 resistance=55.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=21.46 liquidity=1358182.88 spike=0.11
- MHOT.CA: score=9.66 buy_ready=False sector_rank=17 price=32.5 support=31.72 resistance=34.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39079412.0 spike=1.79
- MICH.CA: score=26.16 buy_ready=False sector_rank=7 price=38.37 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=16576734.0 spike=1.13
- MILS.CA: score=16.54 buy_ready=False sector_rank=7 price=138.4 support=130.4 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=4631936.0 spike=0.23
- MIPH.CA: score=16.97 buy_ready=True sector_rank=3 price=688.2 support=647.0 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=1570550.88 spike=0.7
- MOED.CA: score=16.67 buy_ready=False sector_rank=7 price=0.7 support=0.65 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=46.03 liquidity=6769126.5 spike=0.54
- MOIL.CA: score=14.09 buy_ready=False sector_rank=6 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=63990.97 spike=0.39
- MOIN.CA: score=3.38 buy_ready=False sector_rank=7 price=24.23 support=24.12 resistance=25.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=21.12 liquidity=471577.59 spike=0.28
- MOSC.CA: score=15.85 buy_ready=True sector_rank=7 price=282.54 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=53.26 liquidity=1943037.0 spike=0.21
- MPCI.CA: score=9.98 buy_ready=False sector_rank=7 price=239.96 support=221.5 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=121572096.0 spike=1.54
- MPCO.CA: score=26.4 buy_ready=False sector_rank=2 price=1.93 support=1.54 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=17122776.0 spike=0.17
- MPRC.CA: score=26.82 buy_ready=True sector_rank=7 price=33.71 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=49384108.0 spike=2.46
- MTIE.CA: score=27.12 buy_ready=True sector_rank=1 price=9.19 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=55.48 liquidity=7717805.0 spike=0.43
- NAHO.CA: score=7.9 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- NCCW.CA: score=23.23 buy_ready=True sector_rank=7 price=6.3 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=69.02 liquidity=9329918.0 spike=0.33
- NEDA.CA: score=13.9 buy_ready=False sector_rank=7 price=2.81 support=2.65 resistance=2.84 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=61.76 liquidity=0.0 spike=0.0
- NHPS.CA: score=22.08 buy_ready=True sector_rank=7 price=70.64 support=65.03 resistance=71.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=7019641.0 spike=1.58
- NINH.CA: score=9.42 buy_ready=False sector_rank=7 price=17.49 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=43.3 liquidity=516937.16 spike=0.1
- NIPH.CA: score=25.4 buy_ready=True sector_rank=3 price=167.15 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=58687532.0 spike=0.72
- OBRI.CA: score=19.44 buy_ready=False sector_rank=7 price=35.69 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=56.68 liquidity=6531799.0 spike=0.48
- OCDI.CA: score=11.8 buy_ready=False sector_rank=5 price=22.12 support=21.4 resistance=22.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74803224.0 spike=2.2
- OCPH.CA: score=9.14 buy_ready=False sector_rank=7 price=339.96 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=26.79 liquidity=5231809.5 spike=0.9
- ODIN.CA: score=26.06 buy_ready=False sector_rank=7 price=2.23 support=1.89 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=11738475.0 spike=1.08
- OFH.CA: score=18.45 buy_ready=False sector_rank=7 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=9541610.0 spike=0.41
- OIH.CA: score=13.42 buy_ready=False sector_rank=14 price=1.37 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=12544436.0 spike=0.14
- OLFI.CA: score=26.07 buy_ready=True sector_rank=12 price=22.44 support=21.0 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=23572416.0 spike=1.19
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=791.94 support=786.0 resistance=797.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46748976.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=5 price=39.12 support=33.81 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=49.64 liquidity=156994224.0 spike=0.86
- ORWE.CA: score=23.42 buy_ready=True sector_rank=13 price=23.36 support=21.65 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.81 liquidity=13760600.0 spike=0.33
- PHAR.CA: score=27.12 buy_ready=True sector_rank=3 price=87.52 support=83.02 resistance=88.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.88 liquidity=52619136.0 spike=1.86
- PHDC.CA: score=24.4 buy_ready=True sector_rank=5 price=16.07 support=13.4 resistance=16.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=254219232.0 spike=0.61
- PHTV.CA: score=10.18 buy_ready=False sector_rank=7 price=235.08 support=216.31 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27657914.0 spike=1.64
- POUL.CA: score=18.69 buy_ready=False sector_rank=12 price=35.5 support=34.99 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=14577540.0 spike=0.4
- PRCL.CA: score=8.69 buy_ready=False sector_rank=16 price=27.08 support=26.05 resistance=27.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35876260.0 spike=1.28
- PRDC.CA: score=23.4 buy_ready=False sector_rank=5 price=8.09 support=5.32 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=90.46 liquidity=77449776.0 spike=0.79
- PRMH.CA: score=24.54 buy_ready=False sector_rank=7 price=2.86 support=2.21 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=70.63 liquidity=34920644.0 spike=1.32
- RACC.CA: score=9.74 buy_ready=False sector_rank=7 price=9.83 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=26.88 liquidity=2837868.75 spike=0.28
- RAKT.CA: score=7.9 buy_ready=False sector_rank=7 price=23.03 support=22.0 resistance=24.48 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=48.94 liquidity=0.0 spike=0.0
- RAYA.CA: score=7.84 buy_ready=False sector_rank=19 price=7.55 support=7.3 resistance=7.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103386248.0 spike=1.09
- RMDA.CA: score=24.07 buy_ready=True sector_rank=3 price=5.11 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=52.66 liquidity=8668253.0 spike=0.1
- ROTO.CA: score=13.9 buy_ready=False sector_rank=7 price=45.22 support=43.22 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107207440.0 spike=7.93
- RREI.CA: score=25.25 buy_ready=True sector_rank=7 price=3.66 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=62.63 liquidity=9341541.0 spike=0.44
- RTVC.CA: score=12.78 buy_ready=False sector_rank=7 price=3.9 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=55.38 liquidity=1874276.0 spike=0.33
- RUBX.CA: score=9.87 buy_ready=False sector_rank=7 price=10.0 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=1962921.0 spike=0.17
- SAUD.CA: score=11.59 buy_ready=False sector_rank=9 price=21.83 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=36.8 liquidity=2741987.25 spike=0.25
- SCEM.CA: score=14.13 buy_ready=False sector_rank=16 price=61.59 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=6001621.5 spike=0.28
- SCFM.CA: score=5.04 buy_ready=False sector_rank=7 price=250.71 support=248.1 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=1135828.88 spike=0.09
- SCTS.CA: score=7.97 buy_ready=False sector_rank=11 price=599.88 support=565.25 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=28.2 liquidity=1162575.38 spike=0.22
- SDTI.CA: score=23.99 buy_ready=True sector_rank=7 price=48.21 support=43.4 resistance=47.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=8082177.0 spike=0.55
- SEIG.CA: score=14.69 buy_ready=False sector_rank=7 price=186.72 support=174.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=790568.69 spike=0.17
- SIPC.CA: score=18.94 buy_ready=True sector_rank=7 price=3.56 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=5033700.0 spike=0.4
- SKPC.CA: score=11.21 buy_ready=False sector_rank=21 price=16.42 support=16.16 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=33.46 liquidity=29016050.0 spike=0.56
- SMFR.CA: score=12.87 buy_ready=False sector_rank=7 price=205.01 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=42.73 liquidity=962857.38 spike=0.23
- SNFC.CA: score=15.89 buy_ready=False sector_rank=7 price=12.08 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=47.98 liquidity=3982153.0 spike=0.15
- SPIN.CA: score=5.8 buy_ready=False sector_rank=13 price=13.82 support=13.3 resistance=14.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:33 AM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=2374518.5 spike=0.52
- SPMD.CA: score=12.86 buy_ready=False sector_rank=7 price=0.46 support=0.45 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70293112.0 spike=2.98
- SUGR.CA: score=9.41 buy_ready=False sector_rank=12 price=48.66 support=48.0 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=1718148.5 spike=0.11
- SVCE.CA: score=23.9 buy_ready=True sector_rank=7 price=9.38 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=46.67 liquidity=55837872.0 spike=0.61
- SWDY.CA: score=18.61 buy_ready=False sector_rank=10 price=87.02 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=6774597.0 spike=0.34
- TALM.CA: score=20.82 buy_ready=False sector_rank=11 price=16.29 support=15.12 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=77.6 liquidity=7998650.5 spike=1.01
- TMGH.CA: score=24.62 buy_ready=True sector_rank=5 price=98.5 support=92.91 resistance=100.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=48.52 liquidity=506016416.0 spike=1.11
- TRTO.CA: score=15.17 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 June 11:57 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=266831.58 spike=271.16
- UEFM.CA: score=10.35 buy_ready=False sector_rank=7 price=472.61 support=455.6 resistance=489.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=48.69 liquidity=443671.63 spike=0.55
- UEGC.CA: score=21.36 buy_ready=True sector_rank=7 price=1.46 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=5459628.5 spike=0.22
- UNIP.CA: score=20.59 buy_ready=False sector_rank=7 price=0.34 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=85.92 liquidity=7689330.5 spike=0.32
- UNIT.CA: score=14.86 buy_ready=False sector_rank=5 price=13.73 support=12.5 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:21 AM market time freshness=DELAYED_CURRENT RSI=58.26 liquidity=459766.72 spike=0.06
- WCDF.CA: score=10.9 buy_ready=False sector_rank=7 price=537.53 support=450.0 resistance=549.95 source=Yahoo Finance as_of=2026-06-17T21:00:00+00:00 freshness=FRESH RSI=45.74 liquidity=0.0 spike=0.0
- WKOL.CA: score=9.27 buy_ready=False sector_rank=7 price=290.07 support=289.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=44.38 liquidity=370350.81 spike=0.11
- ZEOT.CA: score=13.9 buy_ready=False sector_rank=7 price=11.86 support=11.5 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=76731888.0 spike=4.63
- ZMID.CA: score=24.4 buy_ready=True sector_rank=5 price=6.38 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=78745736.0 spike=0.37

## Backtesting Lite
- KWIN.CA: 180d return=2.96%, max drawdown=-34.04%, MA20>MA50 days last20=20, as_of=2026-06-17T21:00:00+00:00
- ATLC.CA: 180d return=46.12%, max drawdown=-16.0%, MA20>MA50 days last20=20, as_of=2026-06-17T21:00:00+00:00
- MASR.CA: 180d return=81.04%, max drawdown=-11.03%, MA20>MA50 days last20=20, as_of=2026-06-17T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- KWIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Kahera El Watania Investment summary=ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m; El Kahera El Watania to buy stake in Assiut for Agricultural Development; Tycoon Holding acquires 85% of Alexandria National Investment Gemini also reviewed web evidence but did not return ticker-specific citations.
  - ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m: https://english.mubasher.info/news/4546852/ADIB-Egypt-s-Cairo-National-unveils-equity-reduction-transaction-worth-over-EGP-3m/
  - El Kahera El Watania to buy stake in Assiut for Agricultural Development: https://english.mubasher.info/news/4009433/El-Kahera-El-Watania-to-buy-stake-in-Assiut-for-Agricultural-Development/
  - Tycoon Holding acquires 85% of Alexandria National Investment: https://english.mubasher.info/news/3844623/Tycoon-Holding-acquires-85-of-Alexandria-National-Investment/
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=536 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move Gemini also reviewed web evidence but did not return ticker-specific citations.
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- ECAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Ezz Ceramics & Porcelain Co. summary=Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.

## Warnings
- Evidence for KWIN.CA matches the company but no source/report date was detected.
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for ECAP.CA: source text did not clearly match ECAP.CA / Al Ezz Ceramics & Porcelain Co..
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
