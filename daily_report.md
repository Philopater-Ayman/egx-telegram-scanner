# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-23T10:03:35.969378+00:00
Generated Cairo: 2026-06-23 13:03
Run timing: target 09:15 Cairo | generated Cairo 2026-06-23 13:03 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-23 13:00

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 40
- Data quality issues: 0
- Tradeable price/liquidity tickers: 169/190
- Top sector: Healthcare

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 23
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 40.0% / above MA50 50.0%
- EGX70 regime: MIXED / above MA20 45.71% / above MA50 71.43%
- Sector breadth: 42.86%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=372363008.0 spike=0.47 score=21.36
- CNFN.CA: liquidity=309492672.0 spike=18.88 score=35.4
- ASCM.CA: liquidity=301460672.0 spike=4.52 score=13.6
- COMI.CA: liquidity=278977152.0 spike=0.48 score=24.46
- ORAS.CA: liquidity=221035056.0 spike=1.0 score=7.6

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner found no ticket meeting all evidence, liquidity, freshness and technical gates, so it defaults to a HOLD stance. EGX30 remains bearish with weak breadth below MA20, while EGX70 shows mixed signals but also limited breadth. Risk mode is set to SELECTIVE_SWING_TRADES_ONLY, meaning only high‑conviction swing ideas would be considered, but none qualified today. Leading sectors are Healthcare, Non‑bank Financial Services and Real Estate, yet overall market uncertainty remains high for the next 1‑3 days.
- EGX30 bearish, only 40% of stocks above MA20; EGX70 mixed, 46% above MA20 – market bias stays defensive.
- Sector breadth at 42.9% indicates limited participation; Healthcare leads with strongest liquidity spikes.
- Top scanner rows (CNFN, CLHO, OCDI, etc.) show bullish outlooks but failed evidence or liquidity checks, so no trade signal.
- Risk mode SELECTIVE_SWING_TRADES_ONLY limits exposure; stay on the sidelines until clearer technical or fundamental triggers appear.
- Uncertainty high – watch for any shift in EGX30 breadth or sector momentum before taking new positions.

## Top Liquidity Spikes
- CNFN.CA: spike=18.88 liquidity=309492672.0 outlook=BULLISH_WATCH score=100 buy_ready=True
- GIHD.CA: spike=16.48 liquidity=52164672.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- DOMT.CA: spike=9.34 liquidity=19755582.0 outlook=BULLISH_WATCH score=88.36 buy_ready=True
- MPRC.CA: spike=4.84 liquidity=103710872.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NINH.CA: spike=4.69 liquidity=21072842.0 outlook=BULLISH_WATCH score=71.99 buy_ready=False

## Sector Leaderboard
- #1 Healthcare: score=7.83 5d=3.13% 20d=5.12% aboveMA50=100.0%
- #2 Non-bank Financial Services: score=6.58 5d=3.31% 20d=2.68% aboveMA50=80.0%
- #3 Real Estate: score=6.33 5d=1.63% 20d=5.26% aboveMA50=84.62%
- #4 Industrial Goods & Cables: score=5.71 5d=1.46% 20d=1.89% aboveMA50=50.0%
- #5 Education: score=5.7 5d=-0.06% 20d=5.23% aboveMA50=66.67%
- #6 Technology & Distribution: score=5.46 5d=6.14% 20d=-2.88% aboveMA50=100.0%
- #7 Agriculture & Food Production: score=5.18 5d=-1.64% 20d=8.88% aboveMA50=50.0%
- #8 Telecommunications: score=5.08 5d=1.51% 20d=-3.06% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CNFN.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- OCDI.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ATLC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- CLHO.CA: BULLISH_WATCH score=98.83 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- PHAR.CA: BULLISH_WATCH score=95.83 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- NIPH.CA: BULLISH_WATCH score=93.83 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PHDC.CA: BULLISH_WATCH score=92.33 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MICH.CA: BULLISH_WATCH score=91.99 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- ZMID.CA: BULLISH_WATCH score=91.33 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- DOMT.CA: BULLISH_WATCH score=88.36 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- CNFN.CA: rank=35.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=4.84 support=4.36 resistance=4.88 liquidity=309492672.0
- DOMT.CA: rank=32.74 outlook=BULLISH_WATCH outlook_score=88.36 sector_rank=10 price=27.27 support=23.7 resistance=26.3 liquidity=19755582.0
- CLHO.CA: rank=32.4 outlook=BULLISH_WATCH outlook_score=98.83 sector_rank=1 price=16.27 support=14.25 resistance=16.85 liquidity=90503688.0
- OCDI.CA: rank=32.4 outlook=BULLISH_WATCH outlook_score=100 sector_rank=3 price=22.7 support=20.0 resistance=22.49 liquidity=92838976.0
- ATLC.CA: rank=30.36 outlook=BULLISH_WATCH outlook_score=100 sector_rank=2 price=5.26 support=4.7 resistance=5.38 liquidity=10611019.0
- ISPH.CA: rank=29.4 outlook=BULLISH_WATCH outlook_score=87.83 sector_rank=1 price=12.29 support=11.3 resistance=12.74 liquidity=26397324.0
- PHAR.CA: rank=28.61 outlook=BULLISH_WATCH outlook_score=95.83 sector_rank=1 price=87.64 support=83.02 resistance=89.47 liquidity=7205130.5
- MASR.CA: rank=27.6 outlook=BULLISH_WATCH outlook_score=82.99 sector_rank=11 price=7.16 support=6.54 resistance=7.69 liquidity=37836452.0
- ORHD.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=82.33 sector_rank=3 price=39.25 support=35.01 resistance=39.68 liquidity=96062312.0
- NIPH.CA: rank=27.4 outlook=BULLISH_WATCH outlook_score=93.83 sector_rank=1 price=167.02 support=157.1 resistance=176.9 liquidity=40738528.0

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=14.87 buy_ready=True sector_rank=11 price=207.04 support=199.25 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=1272949.63 spike=0.2
- ABUK.CA: score=12.28 buy_ready=False sector_rank=20 price=68.65 support=70.5 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=8.05 liquidity=62534160.0 spike=0.42
- ACAMD.CA: score=21.6 buy_ready=False sector_rank=11 price=2.29 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=55.74 liquidity=89471488.0 spike=0.71
- ACGC.CA: score=19.03 buy_ready=False sector_rank=15 price=9.4 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=8116543.5 spike=0.14
- ADCI.CA: score=23.26 buy_ready=False sector_rank=11 price=238.77 support=211.0 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=79.84 liquidity=10390725.0 spike=1.33
- ADIB.CA: score=18.46 buy_ready=False sector_rank=12 price=45.94 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=46.17 liquidity=30909198.0 spike=0.29
- ADPC.CA: score=8.6 buy_ready=False sector_rank=11 price=3.72 support=3.7 resistance=3.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14204439.0 spike=0.53
- AFDI.CA: score=11.42 buy_ready=False sector_rank=11 price=46.88 support=46.0 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=32813394.0 spike=2.41
- AFMC.CA: score=13.09 buy_ready=False sector_rank=11 price=70.62 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=1498313.0 spike=0.31
- AJWA.CA: score=20.44 buy_ready=False sector_rank=11 price=180.0 support=130.01 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=84.42 liquidity=9842733.0 spike=0.37
- ALCN.CA: score=6.28 buy_ready=False sector_rank=17 price=28.07 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=34.02 liquidity=3480657.25 spike=0.24
- ALUM.CA: score=14.61 buy_ready=False sector_rank=11 price=22.89 support=23.02 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=3014770.25 spike=0.27
- AMER.CA: score=15.4 buy_ready=False sector_rank=3 price=2.38 support=2.47 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=43937060.0 spike=0.5
- AMES.CA: score=12.74 buy_ready=False sector_rank=11 price=49.05 support=48.0 resistance=53.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=35.12 liquidity=2148920.75 spike=0.61
- AMIA.CA: score=14.31 buy_ready=False sector_rank=11 price=8.7 support=8.54 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=54.63 liquidity=2717267.75 spike=0.19
- AMOC.CA: score=13.91 buy_ready=False sector_rank=9 price=7.64 support=7.71 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=17.2 liquidity=41836580.0 spike=0.6
- ANFI.CA: score=13.87 buy_ready=False sector_rank=11 price=33.12 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=76.32 liquidity=3274408.69 spike=0.04
- APSW.CA: score=3.02 buy_ready=False sector_rank=11 price=8.57 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=21.33 liquidity=420400.13 spike=0.45
- ARAB.CA: score=25.4 buy_ready=False sector_rank=3 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=52.78 liquidity=45110952.0 spike=0.53
- ARCC.CA: score=17.45 buy_ready=False sector_rank=19 price=54.99 support=54.31 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=38.83 liquidity=10407825.0 spike=0.29
- AREH.CA: score=22.6 buy_ready=False sector_rank=11 price=1.58 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=80.85 liquidity=20001040.0 spike=0.65
- ARVA.CA: score=23.6 buy_ready=True sector_rank=11 price=11.19 support=7.81 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=14052105.0 spike=0.43
- ASCM.CA: score=13.6 buy_ready=False sector_rank=11 price=65.29 support=64.6 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=301460672.0 spike=4.52
- ASPI.CA: score=23.6 buy_ready=True sector_rank=11 price=0.32 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=60.96 liquidity=14533806.0 spike=0.21
- ATLC.CA: score=30.36 buy_ready=True sector_rank=2 price=5.26 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=10611019.0 spike=1.98
- ATQA.CA: score=14.51 buy_ready=False sector_rank=20 price=9.4 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=45.49 liquidity=8221144.0 spike=0.24
- AXPH.CA: score=14.27 buy_ready=False sector_rank=11 price=1122.42 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=47.39 liquidity=670419.06 spike=0.37
- BINV.CA: score=14.4 buy_ready=True sector_rank=13 price=47.67 support=42.9 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=43.93 liquidity=1032536.13 spike=0.1
- BIOC.CA: score=12.81 buy_ready=False sector_rank=11 price=71.25 support=68.34 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=46.54 liquidity=1217365.25 spike=0.46
- BTFH.CA: score=25.4 buy_ready=False sector_rank=2 price=3.07 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=93372056.0 spike=0.45
- CAED.CA: score=24.09 buy_ready=True sector_rank=11 price=72.21 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=56.39 liquidity=6232338.0 spike=1.13
- CANA.CA: score=19.83 buy_ready=True sector_rank=12 price=36.58 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=62.15 liquidity=4366566.0 spike=0.45
- CCAP.CA: score=21.36 buy_ready=False sector_rank=13 price=5.14 support=4.92 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=372363008.0 spike=0.47
- CCRS.CA: score=19.73 buy_ready=False sector_rank=11 price=2.38 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=47.89 liquidity=8134361.0 spike=0.35
- CEFM.CA: score=4.72 buy_ready=False sector_rank=11 price=101.13 support=100.53 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=27.36 liquidity=1128010.88 spike=0.34
- CERA.CA: score=19.1 buy_ready=True sector_rank=11 price=1.23 support=1.14 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=68.0 liquidity=6504288.5 spike=0.41
- CFGH.CA: score=2.6 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=0.0 spike=0.0
- CICH.CA: score=17.09 buy_ready=False sector_rank=2 price=11.93 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=2690620.5 spike=0.75
- CIEB.CA: score=25.2 buy_ready=True sector_rank=12 price=24.05 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=55.74 liquidity=7517267.5 spike=1.11
- CIRA.CA: score=25.14 buy_ready=True sector_rank=5 price=28.7 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=66.92 liquidity=26372876.0 spike=1.43
- CLHO.CA: score=32.4 buy_ready=True sector_rank=1 price=16.27 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=45.29 liquidity=90503688.0 spike=3.53
- CNFN.CA: score=35.4 buy_ready=True sector_rank=2 price=4.84 support=4.36 resistance=4.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=309492672.0 spike=18.88
- COMI.CA: score=24.46 buy_ready=False sector_rank=12 price=134.39 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=278977152.0 spike=0.48
- COPR.CA: score=8.6 buy_ready=False sector_rank=11 price=0.36 support=0.36 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14625154.0 spike=0.33
- COSG.CA: score=21.6 buy_ready=False sector_rank=11 price=1.57 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=15257624.0 spike=0.24
- CPCI.CA: score=14.38 buy_ready=False sector_rank=11 price=371.52 support=346.0 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=73.6 liquidity=785417.63 spike=0.38
- CSAG.CA: score=18.38 buy_ready=False sector_rank=17 price=31.17 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=47.26 liquidity=7579362.5 spike=0.65
- DAPH.CA: score=16.31 buy_ready=False sector_rank=11 price=80.85 support=76.6 resistance=82.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=52.65 liquidity=1711041.63 spike=0.17
- DEIN.CA: score=9.6 buy_ready=False sector_rank=11 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=32.74 buy_ready=True sector_rank=10 price=27.27 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=61.63 liquidity=19755582.0 spike=9.34
- DSCW.CA: score=19.6 buy_ready=False sector_rank=11 price=1.8 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=19612152.0 spike=0.39
- DTPP.CA: score=3.91 buy_ready=False sector_rank=11 price=116.34 support=114.0 resistance=131.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=10.98 liquidity=318034.31 spike=0.17
- EALR.CA: score=14.6 buy_ready=False sector_rank=11 price=356.63 support=350.15 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=49.3 liquidity=999593.0 spike=0.29
- EASB.CA: score=22.26 buy_ready=False sector_rank=11 price=7.62 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=96.82 liquidity=9165323.0 spike=1.25
- EAST.CA: score=23.74 buy_ready=False sector_rank=10 price=38.5 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=61.93 liquidity=20342616.0 spike=0.45
- EBSC.CA: score=17.04 buy_ready=True sector_rank=11 price=1.83 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=61.9 liquidity=1447509.63 spike=0.54
- ECAP.CA: score=18.25 buy_ready=False sector_rank=11 price=32.97 support=29.36 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=94.89 liquidity=5658089.5 spike=0.92
- EDFM.CA: score=11.6 buy_ready=False sector_rank=11 price=332.0 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=35.25 liquidity=0.0 spike=0.0
- EEII.CA: score=22.92 buy_ready=True sector_rank=11 price=2.39 support=2.29 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=5322163.0 spike=0.32
- EFIC.CA: score=1.69 buy_ready=False sector_rank=20 price=199.41 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=23.61 liquidity=406703.06 spike=0.18
- EFID.CA: score=13.74 buy_ready=False sector_rank=10 price=27.69 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=33.77 liquidity=17201266.0 spike=0.23
- EFIH.CA: score=16.75 buy_ready=False sector_rank=21 price=21.01 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=37.27 liquidity=11919635.0 spike=0.23
- EGAL.CA: score=12.28 buy_ready=False sector_rank=20 price=286.68 support=294.99 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=13.55 liquidity=74064536.0 spike=0.98
- EGAS.CA: score=14.25 buy_ready=True sector_rank=9 price=51.13 support=47.5 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=68.92 liquidity=2343559.25 spike=0.19
- EGBE.CA: score=11.55 buy_ready=False sector_rank=12 price=0.44 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=88203.16 spike=0.83
- EGCH.CA: score=7.28 buy_ready=False sector_rank=20 price=12.83 support=12.8 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15948467.0 spike=0.21
- EGSA.CA: score=7.03 buy_ready=False sector_rank=8 price=8.78 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=30.0 liquidity=0.0 spike=0.0
- EGTS.CA: score=18.4 buy_ready=False sector_rank=3 price=18.01 support=17.25 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=34.17 liquidity=19189974.0 spike=0.15
- EHDR.CA: score=21.6 buy_ready=True sector_rank=11 price=2.6 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=22293690.0 spike=0.4
- EKHO.CA: score=13.91 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=17.52 buy_ready=False sector_rank=4 price=2.1 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=7233289.5 spike=0.31
- ELKA.CA: score=8.6 buy_ready=False sector_rank=11 price=1.25 support=1.24 resistance=1.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22398250.0 spike=0.56
- ELNA.CA: score=8.76 buy_ready=False sector_rank=11 price=38.01 support=37.11 resistance=41.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=51.56 liquidity=519064.75 spike=1.32
- ELSH.CA: score=8.6 buy_ready=False sector_rank=11 price=12.13 support=12.0 resistance=12.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33293090.0 spike=0.18
- ELWA.CA: score=14.33 buy_ready=False sector_rank=11 price=2.08 support=1.87 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=732903.19 spike=0.23
- EMFD.CA: score=25.4 buy_ready=True sector_rank=3 price=11.9 support=10.4 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=54.13 liquidity=53854860.0 spike=0.19
- ENGC.CA: score=19.67 buy_ready=False sector_rank=11 price=36.67 support=32.61 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=74.34 liquidity=4073922.0 spike=0.28
- EOSB.CA: score=15.6 buy_ready=False sector_rank=11 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=13.82 buy_ready=False sector_rank=11 price=9.09 support=8.9 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=3219376.25 spike=0.33
- EPPK.CA: score=17.6 buy_ready=False sector_rank=11 price=12.68 support=11.67 resistance=13.12 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=57.63 liquidity=0.0 spike=0.0
- ETEL.CA: score=19.03 buy_ready=False sector_rank=8 price=95.85 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=61831864.0 spike=0.78
- ETRS.CA: score=22.6 buy_ready=False sector_rank=11 price=10.37 support=7.65 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=76.67 liquidity=22148962.0 spike=0.36
- EXPA.CA: score=21.46 buy_ready=False sector_rank=12 price=18.46 support=18.21 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=46.63 liquidity=11032612.0 spike=0.33
- FAIT.CA: score=12.72 buy_ready=False sector_rank=12 price=36.36 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=1257614.0 spike=0.27
- FAITA.CA: score=11.97 buy_ready=False sector_rank=12 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:22 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=50244.7 spike=1.23
- FERC.CA: score=16.92 buy_ready=False sector_rank=20 price=76.85 support=75.0 resistance=79.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=10535041.0 spike=2.82
- FWRY.CA: score=11.75 buy_ready=False sector_rank=21 price=18.99 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=32.04 liquidity=118933784.0 spike=0.41
- GBCO.CA: score=7.96 buy_ready=False sector_rank=14 price=30.82 support=30.27 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34348308.0 spike=0.32
- GDWA.CA: score=16.03 buy_ready=False sector_rank=11 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=58.54 liquidity=6429058.0 spike=0.46
- GGCC.CA: score=21.02 buy_ready=True sector_rank=11 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=6424644.0 spike=0.82
- GIHD.CA: score=13.6 buy_ready=False sector_rank=11 price=44.6 support=42.79 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52164672.0 spike=16.48
- GMCI.CA: score=15.6 buy_ready=False sector_rank=11 price=1.77 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=62.5 liquidity=0.0 spike=0.0
- GRCA.CA: score=8.77 buy_ready=False sector_rank=11 price=54.01 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:32 AM market time freshness=DELAYED_CURRENT RSI=34.33 liquidity=5173479.5 spike=0.95
- GSSC.CA: score=6.5 buy_ready=False sector_rank=11 price=250.66 support=228.1 resistance=257.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=28.98 liquidity=2906278.75 spike=0.6
- GTWL.CA: score=15.05 buy_ready=False sector_rank=11 price=48.17 support=45.47 resistance=52.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=48.56 liquidity=2457125.5 spike=0.36
- HDBK.CA: score=27.46 buy_ready=False sector_rank=12 price=163.26 support=138.0 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=75.16 liquidity=76593592.0 spike=3.8
- HELI.CA: score=23.4 buy_ready=False sector_rank=3 price=6.44 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=46301248.0 spike=0.33
- HRHO.CA: score=22.4 buy_ready=False sector_rank=2 price=27.01 support=25.8 resistance=27.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=51.97 liquidity=65262856.0 spike=0.44
- ICID.CA: score=14.49 buy_ready=False sector_rank=11 price=7.37 support=4.56 resistance=7.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=86.27 liquidity=1891377.88 spike=0.12
- IDRE.CA: score=23.66 buy_ready=True sector_rank=11 price=45.09 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=50.46 liquidity=18837440.0 spike=1.03
- IFAP.CA: score=5.5 buy_ready=False sector_rank=7 price=19.02 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=33.05 liquidity=2428427.25 spike=0.36
- INFI.CA: score=10.28 buy_ready=False sector_rank=11 price=94.1 support=93.0 resistance=105.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=12.22 liquidity=7685541.5 spike=0.85
- IRON.CA: score=14.8 buy_ready=False sector_rank=20 price=31.62 support=31.3 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=46.83 liquidity=6519008.0 spike=0.79
- ISMA.CA: score=16.92 buy_ready=False sector_rank=11 price=29.51 support=25.1 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=81.53 liquidity=8325799.5 spike=0.2
- ISMQ.CA: score=24.28 buy_ready=True sector_rank=20 price=8.26 support=7.31 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=58.1 liquidity=34313072.0 spike=0.46
- ISPH.CA: score=29.4 buy_ready=True sector_rank=1 price=12.29 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=60.23 liquidity=26397324.0 spike=0.2
- JUFO.CA: score=25.74 buy_ready=True sector_rank=10 price=31.01 support=27.6 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=69.51 liquidity=12457024.0 spike=0.3
- KABO.CA: score=9.4 buy_ready=False sector_rank=15 price=6.09 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:36 AM market time freshness=DELAYED_CURRENT RSI=38.71 liquidity=2492275.25 spike=0.13
- KWIN.CA: score=7.4 buy_ready=False sector_rank=11 price=66.89 support=66.65 resistance=70.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8105338.0 spike=1.35
- KZPC.CA: score=17.98 buy_ready=True sector_rank=11 price=10.68 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=2385723.5 spike=0.31
- LCSW.CA: score=22.86 buy_ready=True sector_rank=19 price=27.82 support=26.0 resistance=28.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=53.08 liquidity=6412121.5 spike=0.64
- LUTS.CA: score=8.6 buy_ready=False sector_rank=11 price=0.74 support=0.73 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28657960.0 spike=0.72
- MAAL.CA: score=15.51 buy_ready=False sector_rank=11 price=6.6 support=4.68 resistance=6.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=80.1 liquidity=2910680.5 spike=0.2
- MASR.CA: score=27.6 buy_ready=True sector_rank=11 price=7.16 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=57.93 liquidity=37836452.0 spike=0.67
- MBSC.CA: score=17.45 buy_ready=False sector_rank=19 price=244.68 support=247.43 resistance=260.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=49.73 liquidity=15247631.0 spike=0.35
- MCQE.CA: score=10.12 buy_ready=False sector_rank=19 price=172.16 support=174.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=22.19 liquidity=7675064.0 spike=0.48
- MCRO.CA: score=12.6 buy_ready=False sector_rank=11 price=1.22 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=13544601.0 spike=0.3
- MENA.CA: score=11.51 buy_ready=False sector_rank=3 price=6.79 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=29.06 liquidity=1114374.25 spike=0.07
- MEPA.CA: score=16.09 buy_ready=False sector_rank=11 price=1.64 support=1.66 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=7491876.0 spike=0.44
- MFPC.CA: score=12.28 buy_ready=False sector_rank=20 price=35.65 support=36.76 resistance=44.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=6.41 liquidity=75463432.0 spike=0.81
- MFSC.CA: score=12.54 buy_ready=False sector_rank=11 price=52.89 support=46.99 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35834336.0 spike=2.97
- MHOT.CA: score=8.87 buy_ready=False sector_rank=16 price=35.83 support=35.55 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35627032.0 spike=1.49
- MICH.CA: score=26.64 buy_ready=True sector_rank=11 price=37.62 support=35.31 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=68.78 liquidity=24186528.0 spike=1.52
- MILS.CA: score=14.69 buy_ready=False sector_rank=11 price=137.02 support=131.58 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:42 AM market time freshness=DELAYED_CURRENT RSI=48.27 liquidity=3089556.25 spike=0.18
- MIPH.CA: score=21.21 buy_ready=False sector_rank=1 price=660.08 support=648.25 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=64.54 liquidity=1812998.0 spike=0.82
- MOED.CA: score=14.0 buy_ready=False sector_rank=11 price=0.68 support=0.65 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=4408067.5 spike=0.35
- MOIL.CA: score=16.03 buy_ready=False sector_rank=9 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=52.83 liquidity=126758.39 spike=0.79
- MOIN.CA: score=2.6 buy_ready=False sector_rank=11 price=24.09 support=24.01 resistance=25.66 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=14.86 liquidity=0.0 spike=0.0
- MOSC.CA: score=14.03 buy_ready=False sector_rank=11 price=271.94 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=2432565.0 spike=0.28
- MPCI.CA: score=26.58 buy_ready=False sector_rank=11 price=244.24 support=202.3 resistance=243.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=73.68 liquidity=120497944.0 spike=1.49
- MPCO.CA: score=24.17 buy_ready=False sector_rank=7 price=1.93 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=71.6 liquidity=103463920.0 spike=1.05
- MPRC.CA: score=13.6 buy_ready=False sector_rank=11 price=35.98 support=33.9 resistance=36.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103710872.0 spike=4.84
- MTIE.CA: score=17.52 buy_ready=False sector_rank=14 price=9.07 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=48.87 liquidity=6559773.5 spike=0.38
- NAHO.CA: score=2.6 buy_ready=False sector_rank=11 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=20.0 liquidity=0.0 spike=0.0
- NCCW.CA: score=26.56 buy_ready=False sector_rank=11 price=6.6 support=5.22 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=70.12 liquidity=69969528.0 spike=2.48
- NEDA.CA: score=11.6 buy_ready=False sector_rank=11 price=2.77 support=2.65 resistance=2.84 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=56.76 liquidity=0.0 spike=0.0
- NHPS.CA: score=13.73 buy_ready=False sector_rank=11 price=67.91 support=65.03 resistance=71.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=2138973.75 spike=0.49
- NINH.CA: score=23.6 buy_ready=False sector_rank=11 price=17.84 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=32.32 liquidity=21072842.0 spike=4.69
- NIPH.CA: score=27.4 buy_ready=True sector_rank=1 price=167.02 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=40738528.0 spike=0.53
- OBRI.CA: score=17.87 buy_ready=False sector_rank=11 price=34.55 support=33.63 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=48.1 liquidity=7275922.5 spike=0.54
- OCDI.CA: score=32.4 buy_ready=True sector_rank=3 price=22.7 support=20.0 resistance=22.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=92838976.0 spike=2.5
- OCPH.CA: score=13.6 buy_ready=False sector_rank=11 price=357.9 support=346.57 resistance=374.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22138008.0 spike=4.1
- ODIN.CA: score=20.17 buy_ready=True sector_rank=11 price=2.11 support=1.9 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=4577256.5 spike=0.41
- OFH.CA: score=15.99 buy_ready=False sector_rank=11 price=0.6 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=44.66 liquidity=8391955.0 spike=0.37
- OIH.CA: score=14.82 buy_ready=False sector_rank=13 price=1.39 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=148131120.0 spike=1.73
- OLFI.CA: score=23.74 buy_ready=True sector_rank=10 price=22.08 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=11079762.0 spike=0.55
- ORAS.CA: score=7.6 buy_ready=False sector_rank=18 price=793.96 support=791.0 resistance=812.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=221035056.0 spike=1.0
- ORHD.CA: score=27.4 buy_ready=True sector_rank=3 price=39.25 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=59.61 liquidity=96062312.0 spike=0.52
- ORWE.CA: score=20.71 buy_ready=False sector_rank=15 price=23.0 support=22.12 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=9794024.0 spike=0.24
- PHAR.CA: score=28.61 buy_ready=True sector_rank=1 price=87.64 support=83.02 resistance=89.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=60.2 liquidity=7205130.5 spike=0.2
- PHDC.CA: score=25.4 buy_ready=True sector_rank=3 price=15.56 support=14.32 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=54.6 liquidity=198752608.0 spike=0.47
- PHTV.CA: score=22.6 buy_ready=False sector_rank=11 price=235.09 support=201.55 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=13704553.0 spike=0.74
- POUL.CA: score=9.6 buy_ready=False sector_rank=10 price=38.35 support=37.6 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=48062756.0 spike=1.43
- PRCL.CA: score=8.01 buy_ready=False sector_rank=19 price=30.66 support=28.66 resistance=30.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39240788.0 spike=1.28
- PRDC.CA: score=10.4 buy_ready=False sector_rank=3 price=6.96 support=6.67 resistance=7.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72327952.0 spike=0.72
- PRMH.CA: score=25.6 buy_ready=True sector_rank=11 price=2.72 support=2.23 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=60.55 liquidity=11212001.0 spike=0.4
- RACC.CA: score=26.44 buy_ready=True sector_rank=11 price=10.0 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=43.96 liquidity=23704754.0 spike=2.42
- RAKT.CA: score=8.33 buy_ready=False sector_rank=11 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=39.79 liquidity=391641.56 spike=1.17
- RAYA.CA: score=22.18 buy_ready=False sector_rank=6 price=7.25 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=48.55 liquidity=35676020.0 spike=0.39
- RMDA.CA: score=22.33 buy_ready=False sector_rank=1 price=5.03 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=6933074.5 spike=0.08
- ROTO.CA: score=24.9 buy_ready=False sector_rank=11 price=43.09 support=32.66 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=84.24 liquidity=53343388.0 spike=2.15
- RREI.CA: score=15.87 buy_ready=False sector_rank=11 price=3.52 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=5275347.0 spike=0.25
- RTVC.CA: score=13.02 buy_ready=False sector_rank=11 price=3.83 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=2421058.5 spike=0.48
- RUBX.CA: score=16.53 buy_ready=False sector_rank=11 price=10.3 support=9.8 resistance=10.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=5934375.0 spike=0.54
- SAUD.CA: score=7.31 buy_ready=False sector_rank=12 price=21.41 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=32.06 liquidity=3841180.75 spike=0.37
- SCEM.CA: score=5.0 buy_ready=False sector_rank=19 price=61.21 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=2554486.5 spike=0.13
- SCFM.CA: score=6.12 buy_ready=False sector_rank=11 price=242.1 support=248.1 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=23.66 liquidity=2522838.75 spike=0.23
- SCTS.CA: score=6.5 buy_ready=False sector_rank=5 price=592.21 support=565.25 resistance=648.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=28.59 liquidity=2218519.25 spike=0.45
- SDTI.CA: score=17.94 buy_ready=False sector_rank=11 price=46.23 support=43.6 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=71.18 liquidity=2339973.0 spike=0.16
- SEIG.CA: score=14.15 buy_ready=False sector_rank=11 price=184.59 support=177.32 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=551541.56 spike=0.12
- SIPC.CA: score=10.83 buy_ready=False sector_rank=11 price=3.45 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=2233570.0 spike=0.18
- SKPC.CA: score=15.67 buy_ready=False sector_rank=20 price=16.12 support=16.13 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=9384629.0 spike=0.18
- SMFR.CA: score=9.22 buy_ready=False sector_rank=11 price=199.32 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:30 AM market time freshness=DELAYED_CURRENT RSI=41.88 liquidity=624696.56 spike=0.18
- SNFC.CA: score=15.29 buy_ready=False sector_rank=11 price=12.03 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:14 AM market time freshness=DELAYED_CURRENT RSI=36.32 liquidity=3690391.75 spike=0.14
- SPIN.CA: score=3.68 buy_ready=False sector_rank=15 price=13.91 support=13.3 resistance=14.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=23.33 liquidity=770525.75 spike=0.17
- SPMD.CA: score=8.62 buy_ready=False sector_rank=11 price=0.43 support=0.43 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26860300.0 spike=1.01
- SUGR.CA: score=7.33 buy_ready=False sector_rank=10 price=47.77 support=48.0 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=24.76 liquidity=4583035.0 spike=0.31
- SVCE.CA: score=23.6 buy_ready=True sector_rank=11 price=9.19 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=42.4 liquidity=33684892.0 spike=0.38
- SWDY.CA: score=26.32 buy_ready=True sector_rank=4 price=88.97 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=37.66 liquidity=36088952.0 spike=2.02
- TALM.CA: score=19.22 buy_ready=True sector_rank=5 price=16.0 support=15.32 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=2936282.75 spike=0.38
- TMGH.CA: score=23.4 buy_ready=False sector_rank=3 price=95.06 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=50.74 liquidity=154920928.0 spike=0.32
- TRTO.CA: score=9.6 buy_ready=False sector_rank=11 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=10.67 buy_ready=False sector_rank=11 price=483.15 support=455.6 resistance=489.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=30.31 liquidity=1414281.13 spike=1.83
- UEGC.CA: score=19.55 buy_ready=False sector_rank=11 price=1.4 support=1.31 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=65.79 liquidity=7949781.0 spike=0.32
- UNIP.CA: score=8.6 buy_ready=False sector_rank=11 price=0.32 support=0.29 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18468222.0 spike=0.77
- UNIT.CA: score=8.78 buy_ready=False sector_rank=3 price=13.28 support=12.5 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=30.53 liquidity=378784.25 spike=0.05
- WCDF.CA: score=8.76 buy_ready=False sector_rank=11 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-20T21:00:00+00:00 freshness=FRESH RSI=42.27 liquidity=167032.3 spike=0.63
- WKOL.CA: score=9.87 buy_ready=False sector_rank=11 price=290.0 support=287.66 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=35.88 liquidity=1275377.13 spike=0.41
- ZEOT.CA: score=22.8 buy_ready=False sector_rank=11 price=11.4 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=84.02 liquidity=23048878.0 spike=1.1
- ZMID.CA: score=25.4 buy_ready=True sector_rank=3 price=6.37 support=5.81 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=58.87 liquidity=197457616.0 spike=0.96

## Backtesting Lite
- CNFN.CA: 180d return=11.14%, max drawdown=-27.78%, MA20>MA50 days last20=20, as_of=2026-06-21T21:00:00+00:00
- DOMT.CA: 180d return=22.78%, max drawdown=-13.36%, MA20>MA50 days last20=16, as_of=2026-06-21T21:00:00+00:00
- CLHO.CA: 180d return=42.86%, max drawdown=-14.16%, MA20>MA50 days last20=20, as_of=2026-06-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/
- DOMT.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Arabian Food Industries Domty summary=Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn; Selling pressure pushes Domty’s stock toward EGP 23.50–22.85; Domty unveils demerger, establishes Dairy Products Euro Arabian
  - Domty posts lower consolidated net profits at EGP 161m in 2025; net sales exceed EGP 9.3bn: https://english.mubasher.info/news/4593671/Domty-posts-lower-consolidated-net-profits-at-EGP-161m-in-2025-net-sales-exceed-EGP-9-3bn/
  - Selling pressure pushes Domty’s stock toward EGP 23.50–22.85: https://english.mubasher.info/news/4562323/Selling-pressure-pushes-Domty-s-stock-toward-EGP-23-50-22-85/
  - Domty unveils demerger, establishes Dairy Products Euro Arabian: https://english.mubasher.info/news/4543153/Domty-unveils-demerger-establishes-Dairy-Products-Euro-Arabian/
- CLHO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Cleopatra Hospital Group summary=Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025; Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn; Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo
  - Cleopatra Hospitals unveils EGP 84m dividends to employee for 2025: https://english.mubasher.info/news/4594702/Cleopatra-Hospitals-unveils-EGP-84m-dividends-to-employee-for-2025/
  - Cleopatra Hospitals posts higher consolidated profits in 2025; revenues cross EGP 7.2bn: https://english.mubasher.info/news/4579844/Cleopatra-Hospitals-posts-higher-consolidated-profits-in-2025-revenues-cross-EGP-7-2bn/
  - Cleopatra Hospitals launches EGP 3.5bn Sky hospital in East Cairo: https://english.mubasher.info/news/4553462/Cleopatra-Hospitals-launches-EGP-3-5bn-Sky-hospital-in-East-Cairo/
- OCDI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Sixth of October Development and Investment summary=Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- ATLC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Al Tawfeek Leasing summary=Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- ISPH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Ibn Sina Pharma summary=Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025; EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse; Ibnsina Pharma pens import, distribution deal with OMRON Healthcare
  - Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025: https://english.mubasher.info/news/4563237/Ibnsina-Pharma-s-consolidated-profits-jump-to-EGP-952m-in-2025/
  - EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse: https://english.mubasher.info/news/4552027/EBRD-grants-EGP-1-3bn-loan-to-Ibnsina-Pharma-for-new-warehouse/
  - Ibnsina Pharma pens import, distribution deal with OMRON Healthcare: https://english.mubasher.info/news/4028068/Ibnsina-Pharma-pens-import-distribution-deal-with-OMRON-Healthcare/
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- MASR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=538 sources=3 expected=Madinet Masr For Housing and Development summary=Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval; Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended; Madinet Masr to distribute treasury stocks in first-ever move
  - Madinet Masr to pay out EGP 0.15/shr for 2025 upon equityholders&#39; approval: https://english.mubasher.info/news/4601386/Madinet-Masr-to-pay-out-EGP-0-15-shr-for-2025-upon-equityholders-approval/
  - Madinet Masr logs 24% higher consolidated profits in 2025; dividends recommended: https://english.mubasher.info/news/4578449/Madinet-Masr-logs-24-higher-consolidated-profits-in-2025-dividends-recommended/
  - Madinet Masr to distribute treasury stocks in first-ever move: https://english.mubasher.info/news/4577724/Madinet-Masr-to-distribute-treasury-stocks-in-first-ever-move/

## Warnings
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for DOMT.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for CLHO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for OCDI.CA: source text did not clearly match OCDI.CA / Sixth of October Development and Investment.
- Evidence rejected for ATLC.CA: source text did not clearly match ATLC.CA / Al Tawfeek Leasing.
- Evidence for ISPH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence for MASR.CA matches the company but appears old; latest detected date is 2025-01-01.
