# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-08-18T07:04:27.106527+00:00
Generated Cairo: 2026-08-18 10:04
Run timing: target 09:15 Cairo | generated Cairo 2026-08-18 10:04 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-08-18 10:00

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 50
- Data quality issues: 1
- Tradeable price/liquidity tickers: 156/189
- Top sector: Building Materials

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, August 17
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 70.59% / above MA50 70.59%
- EGX70 regime: BULLISH / above MA20 64.71% / above MA50 82.35%
- Sector breadth: 47.62%
- Risk mode: SELECTIVE_SMALL_MID_SWINGS

## Top Liquidity
- PHAR.CA: liquidity=658931392.0 spike=1.73 score=25.86
- GTWL.CA: liquidity=600489664.0 spike=6.47 score=14.27
- CCAP.CA: liquidity=542911488.0 spike=0.93 score=24.4
- BIOC.CA: liquidity=392344928.0 spike=1.81 score=24.89
- NIPH.CA: liquidity=379648512.0 spike=1.27 score=9.94

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 shows mixed trend while EGX70 is bullish; sector breadth near 48% with leading sectors in Building Materials, Transportation & Logistics, Agriculture & Food Production; risk mode set to selective small‑mid swings with buy support limited to selective only; scanner’s top rows highlight accumulation spikes and bullish watch outlooks but none cleared evidence/liquidity/freshness gates, resulting in a fallback HOLD.
- Prioritized tickets (COPR.CA, AJWA.CA, ETEL.CA, etc.) scored high on rank_score and liquidity_spike, indicating accumulation interest and bullish watch outlook for the next 1‑3 days.
- Each ticket failed evidence, freshness, or technical gates (weak source match, extended momentum, overheated RSI, or proximity to resistance), keeping confidence at LOW.
- EGX30’s mixed trend (median 5‑day return –0.16%) and EGX70’s bullish bias (median 5‑day return +2.86%) shift risk mode to SELECTIVE_SMALL_MID_SWINGS, allowing only selective entries with tight stop‑loss considerations.
- Sector breadth at 47.62% and leading sectors show strength, but the lack of confirming evidence adds uncertainty, so the scanner defaults to HOLD until clearer signals appear.

## Top Liquidity Spikes
- TRTO.CA: spike=45.23 liquidity=101958.3 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NAHO.CA: spike=21.45 liquidity=605044.19 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMIA.CA: spike=8.6 liquidity=152188576.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- SPIN.CA: spike=6.89 liquidity=212072208.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KZPC.CA: spike=6.5 liquidity=72365024.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=14.84 5d=12.88% 20d=18.85% aboveMA50=66.67%
- #2 Transportation & Logistics: score=13.81 5d=8.95% 20d=15.5% aboveMA50=100.0%
- #3 Agriculture & Food Production: score=12.57 5d=6.85% 20d=13.02% aboveMA50=100.0%
- #4 Education: score=12.37 5d=4.4% 20d=19.47% aboveMA50=100.0%
- #5 Tourism & Leisure: score=11.02 5d=11.05% 20d=13.96% aboveMA50=0.0%
- #6 Basic Resources & Chemicals: score=10.26 5d=4.33% 20d=6.18% aboveMA50=90.0%
- #7 Banking & Financials: score=9.26 5d=1.84% 20d=9.66% aboveMA50=90.0%
- #8 Healthcare: score=8.86 5d=-0.18% 20d=11.88% aboveMA50=83.33%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MIPH.CA: BULLISH_WATCH score=96.86 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- COPR.CA: BULLISH_WATCH score=89.68 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ISMQ.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SCTS.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CLHO.CA: BULLISH_WATCH score=84.86 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- CIEB.CA: BULLISH_WATCH score=84.26 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ATLC.CA: BULLISH_WATCH score=84.23 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- AJWA.CA: BULLISH_WATCH score=83.68 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support; sector is not leading
- ETEL.CA: BULLISH_WATCH score=82.76 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- CCAP.CA: BULLISH_WATCH score=82.08 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- COPR.CA: rank=29.97 outlook=BULLISH_WATCH outlook_score=89.68 sector_rank=13 price=0.44 support=0.37 resistance=0.45 liquidity=67859448.0
- AJWA.CA: rank=29.77 outlook=BULLISH_WATCH outlook_score=83.68 sector_rank=13 price=197.36 support=161.0 resistance=210.0 liquidity=68546176.0
- ETEL.CA: rank=29.62 outlook=BULLISH_WATCH outlook_score=82.76 sector_rank=11 price=117.03 support=97.54 resistance=116.25 liquidity=198238112.0
- SAUD.CA: rank=28.64 outlook=BULLISH_WATCH outlook_score=78.26 sector_rank=7 price=23.47 support=21.3 resistance=23.62 liquidity=18769322.0
- RACC.CA: rank=28.31 outlook=BULLISH_WATCH outlook_score=81.68 sector_rank=13 price=10.45 support=9.8 resistance=10.6 liquidity=48735376.0
- ATLC.CA: rank=26.87 outlook=BULLISH_WATCH outlook_score=84.23 sector_rank=17 price=5.59 support=5.0 resistance=5.95 liquidity=28972088.0
- EFIH.CA: rank=26.7 outlook=CONSTRUCTIVE outlook_score=58.82 sector_rank=9 price=24.97 support=21.9 resistance=25.0 liquidity=123205968.0
- CIEB.CA: rank=26.58 outlook=BULLISH_WATCH outlook_score=84.26 sector_rank=7 price=24.71 support=23.75 resistance=24.7 liquidity=12949083.0
- OLFI.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=70.08 sector_rank=10 price=24.89 support=22.25 resistance=26.52 liquidity=20908100.0
- EHDR.CA: rank=26.31 outlook=CONSTRUCTIVE outlook_score=63.68 sector_rank=13 price=3.13 support=2.69 resistance=3.19 liquidity=48488672.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=14.27 buy_ready=False sector_rank=13 price=366.0 support=307.0 resistance=366.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=171169008.0 spike=4.09
- ABUK.CA: score=23.4 buy_ready=False sector_rank=6 price=78.12 support=70.6 resistance=78.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.87 liquidity=85557472.0 spike=0.56
- ACAMD.CA: score=19.27 buy_ready=False sector_rank=13 price=2.22 support=2.2 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=25590884.0 spike=0.42
- ACGC.CA: score=11.34 buy_ready=False sector_rank=15 price=13.8 support=12.8 resistance=13.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=74675496.0 spike=2.21
- ADCI.CA: score=24.27 buy_ready=True sector_rank=13 price=299.14 support=235.45 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=65.17 liquidity=16055018.0 spike=0.74
- ADIB.CA: score=23.4 buy_ready=False sector_rank=7 price=55.04 support=46.02 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=77.1 liquidity=47387692.0 spike=0.41
- ADPC.CA: score=26.27 buy_ready=True sector_rank=13 price=4.5 support=3.76 resistance=4.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.36 liquidity=33482050.0 spike=0.66
- AFDI.CA: score=9.27 buy_ready=False sector_rank=13 price=62.5 support=57.6 resistance=66.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21128962.0 spike=0.85
- AFMC.CA: score=24.27 buy_ready=False sector_rank=13 price=243.99 support=77.25 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.06 liquidity=80947608.0 spike=0.5
- AJWA.CA: score=29.77 buy_ready=True sector_rank=13 price=197.36 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.69 liquidity=68546176.0 spike=1.75
- ALCN.CA: score=25.5 buy_ready=False sector_rank=2 price=30.97 support=28.8 resistance=32.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=79.56 liquidity=25667930.0 spike=1.05
- ALUM.CA: score=21.39 buy_ready=False sector_rank=13 price=28.42 support=22.72 resistance=30.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.47 liquidity=20003054.0 spike=1.06
- AMER.CA: score=23.77 buy_ready=False sector_rank=16 price=6.75 support=3.92 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.95 liquidity=86490224.0 spike=0.73
- AMES.CA: score=24.27 buy_ready=True sector_rank=13 price=120.37 support=106.59 resistance=136.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=43.67 liquidity=11232573.0 spike=0.15
- AMIA.CA: score=14.27 buy_ready=False sector_rank=13 price=15.24 support=12.71 resistance=15.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=152188576.0 spike=8.6
- AMOC.CA: score=11.84 buy_ready=False sector_rank=14 price=11.49 support=10.91 resistance=11.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=267818320.0 spike=2.43
- APSW.CA: score=11.08 buy_ready=False sector_rank=13 price=9.12 support=8.5 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=24.72 liquidity=1807106.13 spike=1.0
- ARAB.CA: score=21.77 buy_ready=False sector_rank=16 price=0.24 support=0.23 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=38118492.0 spike=0.35
- ARCC.CA: score=24.4 buy_ready=False sector_rank=1 price=75.8 support=55.16 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=83.71 liquidity=88219576.0 spike=0.95
- AREH.CA: score=21.27 buy_ready=False sector_rank=13 price=1.52 support=1.38 resistance=1.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=37926444.0 spike=0.98
- ARVA.CA: score=10.27 buy_ready=False sector_rank=13 price=12.35 support=10.68 resistance=12.6 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ASCM.CA: score=22.27 buy_ready=False sector_rank=13 price=63.0 support=60.1 resistance=69.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=58.16 liquidity=38810964.0 spike=0.64
- ASPI.CA: score=9.27 buy_ready=False sector_rank=13 price=0.55 support=0.53 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33552322.0 spike=0.75
- ATLC.CA: score=26.87 buy_ready=True sector_rank=17 price=5.59 support=5.0 resistance=5.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=63.85 liquidity=28972088.0 spike=1.59
- ATQA.CA: score=25.26 buy_ready=False sector_rank=6 price=11.03 support=9.56 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.75 liquidity=82978304.0 spike=1.43
- AXPH.CA: score=19.15 buy_ready=True sector_rank=13 price=1344.57 support=1121.56 resistance=1460.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:11 PM market time freshness=DELAYED_CURRENT RSI=62.99 liquidity=2882332.5 spike=0.66
- BINV.CA: score=13.27 buy_ready=False sector_rank=12 price=48.2 support=46.01 resistance=50.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=73.26 liquidity=2866929.5 spike=0.4
- BIOC.CA: score=24.89 buy_ready=False sector_rank=13 price=507.0 support=106.61 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=84.02 liquidity=392344928.0 spike=1.81
- BTFH.CA: score=21.69 buy_ready=False sector_rank=17 price=3.11 support=3.05 resistance=3.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=132454728.0 spike=0.58
- CAED.CA: score=24.27 buy_ready=True sector_rank=13 price=129.15 support=104.22 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=17153852.0 spike=0.23
- CANA.CA: score=23.4 buy_ready=False sector_rank=7 price=42.31 support=35.2 resistance=43.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=78.06 liquidity=17027802.0 spike=0.76
- CCAP.CA: score=24.4 buy_ready=True sector_rank=12 price=5.36 support=5.14 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=45.56 liquidity=542911488.0 spike=0.93
- CCRS.CA: score=18.09 buy_ready=False sector_rank=13 price=2.5 support=2.44 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=25175218.0 spike=1.41
- CEFM.CA: score=18.29 buy_ready=True sector_rank=13 price=135.08 support=108.01 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=55.92 liquidity=4022474.25 spike=0.12
- CERA.CA: score=22.27 buy_ready=False sector_rank=13 price=1.31 support=1.25 resistance=1.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=11096991.0 spike=0.54
- CFGH.CA: score=4.34 buy_ready=False sector_rank=13 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67179.98 spike=4.06
- CICH.CA: score=16.61 buy_ready=True sector_rank=17 price=12.67 support=11.8 resistance=13.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:11 PM market time freshness=DELAYED_CURRENT RSI=63.19 liquidity=2913282.25 spike=0.38
- CIEB.CA: score=26.58 buy_ready=True sector_rank=7 price=24.71 support=23.75 resistance=24.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=57.95 liquidity=12949083.0 spike=1.09
- CIRA.CA: score=24.4 buy_ready=True sector_rank=4 price=37.3 support=30.91 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=68.97 liquidity=53351848.0 spike=0.89
- CLHO.CA: score=24.4 buy_ready=True sector_rank=8 price=17.34 support=16.0 resistance=19.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=54.47 liquidity=41327288.0 spike=0.8
- CNFN.CA: score=21.69 buy_ready=False sector_rank=17 price=4.87 support=4.68 resistance=5.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=52.73 liquidity=19596830.0 spike=0.86
- COMI.CA: score=22.4 buy_ready=False sector_rank=7 price=138.81 support=132.81 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.19 liquidity=378081376.0 spike=0.9
- COPR.CA: score=29.97 buy_ready=True sector_rank=13 price=0.44 support=0.37 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=67859448.0 spike=1.85
- COSG.CA: score=26.27 buy_ready=True sector_rank=13 price=1.8 support=1.6 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=67.5 liquidity=43342816.0 spike=0.9
- CPCI.CA: score=19.78 buy_ready=False sector_rank=13 price=538.84 support=440.01 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=71.71 liquidity=5511111.5 spike=0.36
- CSAG.CA: score=23.4 buy_ready=False sector_rank=2 price=41.62 support=31.35 resistance=43.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=85.18 liquidity=11675777.0 spike=0.46
- DAPH.CA: score=21.27 buy_ready=False sector_rank=13 price=129.02 support=84.31 resistance=147.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=79.63 liquidity=23116272.0 spike=0.59
- DEIN.CA: score=-0.73 buy_ready=False sector_rank=13 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=21.63 buy_ready=True sector_rank=10 price=29.13 support=26.01 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=65.7 liquidity=7227858.0 spike=0.5
- DSCW.CA: score=24.27 buy_ready=True sector_rank=13 price=2.04 support=1.86 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=83160024.0 spike=0.87
- DTPP.CA: score=24.27 buy_ready=False sector_rank=13 price=295.06 support=222.0 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=74.68 liquidity=34361456.0 spike=0.54
- EALR.CA: score=14.27 buy_ready=False sector_rank=13 price=456.01 support=390.25 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=212252880.0 spike=6.34
- EASB.CA: score=20.13 buy_ready=False sector_rank=13 price=7.47 support=6.71 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=14301001.0 spike=1.43
- EAST.CA: score=22.4 buy_ready=False sector_rank=10 price=36.75 support=36.01 resistance=37.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=48.01 liquidity=44168800.0 spike=0.67
- EBSC.CA: score=16.77 buy_ready=True sector_rank=13 price=1.93 support=1.85 resistance=2.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=2502922.25 spike=0.45
- ECAP.CA: score=24.79 buy_ready=False sector_rank=13 price=39.3 support=32.12 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=14639619.0 spike=1.26
- EDFM.CA: score=12.52 buy_ready=False sector_rank=13 price=411.42 support=352.0 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=82.27 liquidity=1247401.38 spike=0.22
- EEII.CA: score=26.27 buy_ready=True sector_rank=13 price=3.05 support=2.54 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.68 liquidity=13747525.0 spike=0.69
- EFIC.CA: score=28.4 buy_ready=False sector_rank=6 price=234.7 support=184.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.16 liquidity=145703696.0 spike=4.01
- EFID.CA: score=23.52 buy_ready=False sector_rank=10 price=33.38 support=26.64 resistance=32.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=90.91 liquidity=92308368.0 spike=1.06
- EFIH.CA: score=26.7 buy_ready=True sector_rank=9 price=24.97 support=21.9 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=64.86 liquidity=123205968.0 spike=1.15
- EGAL.CA: score=23.68 buy_ready=False sector_rank=6 price=345.0 support=292.0 resistance=358.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.2 liquidity=204469488.0 spike=2.14
- EGAS.CA: score=23.98 buy_ready=True sector_rank=14 price=59.58 support=50.0 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=69.59 liquidity=10995311.0 spike=0.43
- EGBE.CA: score=12.52 buy_ready=False sector_rank=7 price=0.53 support=0.45 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=121987.53 spike=0.75
- EGCH.CA: score=23.98 buy_ready=False sector_rank=6 price=14.21 support=12.69 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=75.57 liquidity=150794816.0 spike=1.29
- EGSA.CA: score=4.42 buy_ready=False sector_rank=11 price=8.67 support=8.65 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:02 PM market time freshness=DELAYED_CURRENT RSI=20.45 liquidity=18708.9 spike=0.92
- EGTS.CA: score=25.77 buy_ready=True sector_rank=16 price=18.69 support=17.11 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=25752698.0 spike=0.64
- EHDR.CA: score=26.31 buy_ready=True sector_rank=13 price=3.13 support=2.69 resistance=3.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=53.75 liquidity=48488672.0 spike=1.02
- EKHO.CA: score=9.98 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=20.26 buy_ready=False sector_rank=18 price=2.19 support=2.12 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=43385748.0 spike=0.58
- ELKA.CA: score=17.27 buy_ready=False sector_rank=13 price=1.74 support=1.69 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=31980840.0 spike=0.38
- ELNA.CA: score=5.27 buy_ready=False sector_rank=13 price=37.88 support=36.5 resistance=39.49 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=24.19 liquidity=0.0 spike=0.0
- ELSH.CA: score=22.27 buy_ready=False sector_rank=13 price=13.91 support=13.31 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.9 liquidity=28155904.0 spike=0.32
- ELWA.CA: score=6.78 buy_ready=False sector_rank=13 price=1.73 support=1.65 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=28.95 liquidity=505875.59 spike=0.33
- EMFD.CA: score=20.77 buy_ready=False sector_rank=16 price=11.65 support=11.08 resistance=12.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=55.7 liquidity=35588376.0 spike=0.59
- ENGC.CA: score=27.59 buy_ready=False sector_rank=13 price=50.77 support=40.11 resistance=51.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=75.06 liquidity=84614128.0 spike=3.16
- EOSB.CA: score=18.27 buy_ready=False sector_rank=13 price=1.55 support=1.52 resistance=1.62 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- EPCO.CA: score=26.27 buy_ready=True sector_rank=13 price=11.95 support=10.32 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=57.25 liquidity=20539150.0 spike=0.6
- EPPK.CA: score=5.12 buy_ready=False sector_rank=13 price=13.37 support=12.62 resistance=15.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=13.99 liquidity=844198.0 spike=0.94
- ETEL.CA: score=29.62 buy_ready=True sector_rank=11 price=117.03 support=97.54 resistance=116.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=198238112.0 spike=1.61
- ETRS.CA: score=14.27 buy_ready=False sector_rank=13 price=11.46 support=11.11 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=102545704.0 spike=4.2
- EXPA.CA: score=23.4 buy_ready=False sector_rank=7 price=21.2 support=19.25 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=75.56 liquidity=12075542.0 spike=0.33
- FAIT.CA: score=24.38 buy_ready=False sector_rank=7 price=42.42 support=36.1 resistance=40.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=86.86 liquidity=8438071.0 spike=2.27
- FAITA.CA: score=18.47 buy_ready=False sector_rank=7 price=0.99 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=58.11 liquidity=90590.81 spike=1.99
- FERC.CA: score=23.46 buy_ready=False sector_rank=6 price=78.87 support=75.01 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.94 liquidity=18376820.0 spike=1.03
- FWRY.CA: score=24.4 buy_ready=True sector_rank=9 price=19.22 support=18.69 resistance=19.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=117284200.0 spike=0.92
- GBCO.CA: score=19.99 buy_ready=False sector_rank=19 price=30.27 support=29.53 resistance=33.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=58.52 liquidity=48929984.0 spike=0.79
- GDWA.CA: score=13.27 buy_ready=False sector_rank=13 price=0.81 support=0.8 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=18.95 liquidity=39878676.0 spike=0.37
- GGCC.CA: score=25.21 buy_ready=True sector_rank=13 price=0.99 support=0.73 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=59.24 liquidity=72576680.0 spike=1.47
- GIHD.CA: score=24.27 buy_ready=True sector_rank=13 price=67.0 support=49.32 resistance=76.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.46 liquidity=26008168.0 spike=0.56
- GMCI.CA: score=12.93 buy_ready=False sector_rank=13 price=1.92 support=1.88 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 12:57 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=655999.75 spike=0.9
- GRCA.CA: score=9.83 buy_ready=False sector_rank=13 price=58.67 support=54.7 resistance=59.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23592972.0 spike=1.28
- GSSC.CA: score=19.12 buy_ready=True sector_rank=13 price=281.17 support=263.6 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=65.14 liquidity=6852081.0 spike=0.4
- GTWL.CA: score=14.27 buy_ready=False sector_rank=13 price=168.28 support=161.03 resistance=184.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=600489664.0 spike=6.47
- HDBK.CA: score=10.96 buy_ready=False sector_rank=7 price=91.97 support=88.85 resistance=91.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=67936040.0 spike=1.78
- HELI.CA: score=21.77 buy_ready=False sector_rank=16 price=7.59 support=7.73 resistance=8.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.53 liquidity=125221432.0 spike=0.72
- HRHO.CA: score=17.69 buy_ready=False sector_rank=17 price=26.4 support=25.95 resistance=28.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.72 liquidity=82766664.0 spike=0.86
- ICID.CA: score=12.35 buy_ready=False sector_rank=13 price=14.88 support=13.4 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36672292.0 spike=2.54
- IDRE.CA: score=25.07 buy_ready=True sector_rank=13 price=54.25 support=44.52 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=64.99 liquidity=8793007.0 spike=0.3
- IFAP.CA: score=22.58 buy_ready=False sector_rank=3 price=20.79 support=19.0 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=77.55 liquidity=24486834.0 spike=1.09
- INFI.CA: score=24.09 buy_ready=False sector_rank=13 price=153.2 support=101.53 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=76.82 liquidity=126788336.0 spike=2.41
- IRON.CA: score=18.88 buy_ready=False sector_rank=6 price=31.34 support=30.14 resistance=34.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=49.51 liquidity=11366272.0 spike=1.24
- ISMA.CA: score=26.27 buy_ready=False sector_rank=13 price=35.0 support=27.1 resistance=36.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=74.68 liquidity=16318795.0 spike=0.6
- ISMQ.CA: score=24.4 buy_ready=True sector_rank=6 price=9.39 support=8.96 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=52.56 liquidity=32040584.0 spike=0.47
- ISPH.CA: score=24.4 buy_ready=True sector_rank=8 price=13.44 support=11.3 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=147794992.0 spike=0.8
- JUFO.CA: score=23.4 buy_ready=False sector_rank=10 price=27.24 support=22.78 resistance=36.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=45.77 liquidity=43169000.0 spike=0.74
- KABO.CA: score=11.28 buy_ready=False sector_rank=15 price=9.64 support=9.2 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73956296.0 spike=2.18
- KWIN.CA: score=16.71 buy_ready=False sector_rank=13 price=85.65 support=73.0 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=9438443.0 spike=0.18
- KZPC.CA: score=14.27 buy_ready=False sector_rank=13 price=12.2 support=11.5 resistance=13.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=72365024.0 spike=6.5
- LCSW.CA: score=25.4 buy_ready=False sector_rank=1 price=32.8 support=30.2 resistance=37.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=36.09 liquidity=20835006.0 spike=0.49
- LUTS.CA: score=14.27 buy_ready=False sector_rank=13 price=1.19 support=1.03 resistance=1.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=356172448.0 spike=5.67
- MAAL.CA: score=21.39 buy_ready=True sector_rank=13 price=8.9 support=8.32 resistance=9.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=47.19 liquidity=7117987.0 spike=0.47
- MASR.CA: score=22.27 buy_ready=False sector_rank=13 price=7.7 support=7.45 resistance=8.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.66 liquidity=40192620.0 spike=0.53
- MBSC.CA: score=28.04 buy_ready=False sector_rank=1 price=395.64 support=231.51 resistance=399.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=96.78 liquidity=118054480.0 spike=1.82
- MCQE.CA: score=26.42 buy_ready=False sector_rank=1 price=240.52 support=175.55 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.41 liquidity=80804512.0 spike=2.01
- MCRO.CA: score=24.27 buy_ready=True sector_rank=13 price=1.51 support=1.32 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=105855992.0 spike=0.58
- MENA.CA: score=23.58 buy_ready=True sector_rank=16 price=7.27 support=6.83 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=56.19 liquidity=7387674.0 spike=1.21
- MEPA.CA: score=22.27 buy_ready=False sector_rank=13 price=1.81 support=1.69 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=46.51 liquidity=18298978.0 spike=0.29
- MFPC.CA: score=23.58 buy_ready=False sector_rank=6 price=39.69 support=35.37 resistance=40.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=81.4 liquidity=95869832.0 spike=1.09
- MFSC.CA: score=17.34 buy_ready=True sector_rank=13 price=49.53 support=45.95 resistance=65.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=55.73 liquidity=3066362.5 spike=0.25
- MHOT.CA: score=21.57 buy_ready=False sector_rank=5 price=18.89 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=63.66 liquidity=9170239.0 spike=0.54
- MICH.CA: score=23.59 buy_ready=False sector_rank=13 price=47.78 support=37.7 resistance=53.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=70.32 liquidity=9317975.0 spike=0.27
- MILS.CA: score=24.27 buy_ready=True sector_rank=13 price=191.35 support=140.1 resistance=211.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:26 PM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=34361280.0 spike=0.51
- MIPH.CA: score=23.16 buy_ready=True sector_rank=8 price=770.0 support=722.7 resistance=828.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=57.62 liquidity=7676488.5 spike=1.54
- MOED.CA: score=15.27 buy_ready=False sector_rank=13 price=0.69 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=31098108.0 spike=0.95
- MOIL.CA: score=12.21 buy_ready=False sector_rank=14 price=0.67 support=0.55 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=66.29 liquidity=234358.28 spike=0.38
- MOIN.CA: score=10.45 buy_ready=False sector_rank=13 price=38.14 support=38.0 resistance=40.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40908544.0 spike=1.59
- MOSC.CA: score=23.27 buy_ready=False sector_rank=13 price=336.63 support=280.4 resistance=370.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=87.47 liquidity=17812556.0 spike=0.93
- MPCI.CA: score=24.27 buy_ready=False sector_rank=13 price=377.7 support=243.0 resistance=460.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=73.12 liquidity=106084864.0 spike=0.68
- MPCO.CA: score=22.4 buy_ready=False sector_rank=3 price=2.13 support=1.82 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=77.19 liquidity=55995532.0 spike=0.54
- MPRC.CA: score=22.27 buy_ready=False sector_rank=13 price=44.96 support=43.02 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=55.51 liquidity=18249524.0 spike=0.65
- MTIE.CA: score=20.29 buy_ready=False sector_rank=19 price=9.22 support=8.01 resistance=11.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=51.62 liquidity=54656792.0 spike=1.15
- NAHO.CA: score=4.88 buy_ready=False sector_rank=13 price=0.14 support=0.14 resistance=0.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=605044.19 spike=21.45
- NCCW.CA: score=14.27 buy_ready=False sector_rank=13 price=6.14 support=5.67 resistance=7.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=20336424.0 spike=0.57
- NEDA.CA: score=18.72 buy_ready=True sector_rank=13 price=2.83 support=2.7 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=1792207.88 spike=2.33
- NHPS.CA: score=24.27 buy_ready=True sector_rank=13 price=91.74 support=82.25 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=56.77 liquidity=51402376.0 spike=0.81
- NINH.CA: score=22.27 buy_ready=False sector_rank=13 price=21.78 support=19.49 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=47.9 liquidity=20448738.0 spike=0.37
- NIPH.CA: score=9.94 buy_ready=False sector_rank=8 price=376.02 support=366.01 resistance=408.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=379648512.0 spike=1.27
- OBRI.CA: score=24.13 buy_ready=False sector_rank=13 price=33.58 support=31.61 resistance=36.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=35.19 liquidity=44995192.0 spike=1.43
- OCDI.CA: score=8.77 buy_ready=False sector_rank=16 price=33.0 support=32.8 resistance=34.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=83048952.0 spike=0.61
- OCPH.CA: score=9.27 buy_ready=False sector_rank=13 price=270.0 support=269.99 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35371244.0 spike=0.98
- ODIN.CA: score=24.39 buy_ready=False sector_rank=13 price=3.32 support=2.42 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=38122344.0 spike=1.06
- OFH.CA: score=21.27 buy_ready=False sector_rank=13 price=0.88 support=0.67 resistance=0.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.0 liquidity=73784688.0 spike=0.8
- OIH.CA: score=23.4 buy_ready=False sector_rank=12 price=1.78 support=1.41 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=92.5 liquidity=107936664.0 spike=0.99
- OLFI.CA: score=26.4 buy_ready=True sector_rank=10 price=24.89 support=22.25 resistance=26.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=62.13 liquidity=20908100.0 spike=0.32
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=761.2 support=751.5 resistance=794.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=183936768.0 spike=1.0
- ORHD.CA: score=25.77 buy_ready=False sector_rank=16 price=42.46 support=38.0 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=71.98 liquidity=45519108.0 spike=0.27
- ORWE.CA: score=20.92 buy_ready=False sector_rank=15 price=25.9 support=22.55 resistance=27.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.85 liquidity=70709632.0 spike=0.94
- PHAR.CA: score=25.86 buy_ready=False sector_rank=8 price=137.26 support=89.1 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=72.45 liquidity=658931392.0 spike=1.73
- PHDC.CA: score=24.99 buy_ready=True sector_rank=16 price=15.68 support=14.32 resistance=15.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=369137408.0 spike=1.61
- PHTV.CA: score=3.17 buy_ready=False sector_rank=13 price=358.55 support=355.3 resistance=379.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:07 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3337241.25 spike=1.28
- POUL.CA: score=21.4 buy_ready=False sector_rank=10 price=38.1 support=36.5 resistance=40.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.76 liquidity=19217946.0 spike=0.71
- PRCL.CA: score=14.0 buy_ready=False sector_rank=1 price=36.14 support=34.41 resistance=36.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63035108.0 spike=1.8
- PRDC.CA: score=21.77 buy_ready=False sector_rank=16 price=9.0 support=8.7 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=78954256.0 spike=0.72
- PRMH.CA: score=18.68 buy_ready=False sector_rank=13 price=2.6 support=2.56 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=52.54 liquidity=7404497.0 spike=0.54
- RACC.CA: score=28.31 buy_ready=True sector_rank=13 price=10.45 support=9.8 resistance=10.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=65.31 liquidity=48735376.0 spike=2.02
- RAKT.CA: score=8.27 buy_ready=False sector_rank=13 price=22.63 support=21.66 resistance=24.0 source=Yahoo Finance as_of=2026-08-15T21:00:00+00:00 freshness=FRESH RSI=49.49 liquidity=0.0 spike=0.0
- RAYA.CA: score=11.01 buy_ready=False sector_rank=21 price=7.24 support=6.97 resistance=7.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=21.79 liquidity=94881112.0 spike=0.99
- RMDA.CA: score=24.4 buy_ready=False sector_rank=8 price=6.4 support=4.95 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=71.48 liquidity=73699360.0 spike=0.64
- ROTO.CA: score=24.05 buy_ready=False sector_rank=13 price=50.79 support=40.5 resistance=51.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=78.63 liquidity=32162214.0 spike=1.39
- RREI.CA: score=24.27 buy_ready=True sector_rank=13 price=4.64 support=3.72 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=44170148.0 spike=0.68
- RTVC.CA: score=7.31 buy_ready=False sector_rank=13 price=3.79 support=3.73 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=34.29 liquidity=3033284.75 spike=0.56
- RUBX.CA: score=11.79 buy_ready=False sector_rank=13 price=13.17 support=12.7 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75029280.0 spike=2.26
- SAUD.CA: score=28.64 buy_ready=True sector_rank=7 price=23.47 support=21.3 resistance=23.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:25 PM market time freshness=DELAYED_CURRENT RSI=63.56 liquidity=18769322.0 spike=1.12
- SCEM.CA: score=13.24 buy_ready=False sector_rank=1 price=107.89 support=103.0 resistance=110.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=257213472.0 spike=1.42
- SCFM.CA: score=21.7 buy_ready=True sector_rank=13 price=283.41 support=256.5 resistance=319.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:13 PM market time freshness=DELAYED_CURRENT RSI=46.95 liquidity=7423996.5 spike=0.29
- SCTS.CA: score=19.63 buy_ready=True sector_rank=4 price=616.67 support=602.01 resistance=685.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=45.94 liquidity=3227053.25 spike=0.38
- SDTI.CA: score=21.27 buy_ready=False sector_rank=13 price=70.33 support=46.6 resistance=75.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=13943320.0 spike=0.49
- SEIG.CA: score=18.85 buy_ready=False sector_rank=13 price=272.01 support=237.0 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=88.17 liquidity=5581448.0 spike=0.44
- SIPC.CA: score=12.99 buy_ready=False sector_rank=13 price=5.08 support=4.99 resistance=5.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=160577376.0 spike=2.86
- SKPC.CA: score=25.62 buy_ready=True sector_rank=6 price=16.85 support=15.61 resistance=16.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=65.5 liquidity=100288920.0 spike=2.11
- SMFR.CA: score=24.27 buy_ready=False sector_rank=13 price=261.94 support=225.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=74.09 liquidity=17063622.0 spike=0.42
- SNFC.CA: score=21.27 buy_ready=False sector_rank=13 price=11.11 support=10.6 resistance=11.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:14 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=11593340.0 spike=0.95
- SPIN.CA: score=13.92 buy_ready=False sector_rank=15 price=20.25 support=19.82 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=212072208.0 spike=6.89
- SPMD.CA: score=24.27 buy_ready=True sector_rank=13 price=0.48 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=63.73 liquidity=16052670.0 spike=0.47
- SUGR.CA: score=27.86 buy_ready=False sector_rank=10 price=51.0 support=46.47 resistance=51.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=71.77 liquidity=38203976.0 spike=2.73
- SVCE.CA: score=21.27 buy_ready=False sector_rank=13 price=10.87 support=9.06 resistance=12.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=75.08 liquidity=81332896.0 spike=0.84
- SWDY.CA: score=10.22 buy_ready=False sector_rank=18 price=122.44 support=119.01 resistance=125.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127990312.0 spike=1.98
- TALM.CA: score=21.4 buy_ready=False sector_rank=4 price=19.7 support=15.65 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=75.04 liquidity=20091190.0 spike=0.48
- TMGH.CA: score=18.77 buy_ready=False sector_rank=16 price=96.91 support=95.2 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=267179600.0 spike=0.77
- TRTO.CA: score=4.37 buy_ready=False sector_rank=13 price=0.05 support=0.04 resistance=0.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 12:59 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=101958.3 spike=45.23
- UEFM.CA: score=26.07 buy_ready=False sector_rank=13 price=543.52 support=511.3 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:12 PM market time freshness=DELAYED_CURRENT RSI=68.17 liquidity=16215125.0 spike=2.9
- UEGC.CA: score=22.27 buy_ready=False sector_rank=13 price=2.44 support=2.08 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=13273314.0 spike=0.27
- UNIP.CA: score=22.27 buy_ready=False sector_rank=13 price=0.4 support=0.36 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=45.36 liquidity=18757288.0 spike=0.68
- UNIT.CA: score=3.79 buy_ready=False sector_rank=16 price=18.94 support=18.65 resistance=20.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5024335.0 spike=0.27
- WCDF.CA: score=13.02 buy_ready=False sector_rank=13 price=634.3 support=523.3 resistance=700.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:07 PM market time freshness=DELAYED_CURRENT RSI=77.93 liquidity=1747765.13 spike=0.33
- WKOL.CA: score=14.27 buy_ready=False sector_rank=13 price=376.61 support=326.5 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=143681776.0 spike=6.02
- ZEOT.CA: score=26.27 buy_ready=False sector_rank=13 price=14.22 support=11.51 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:27 PM market time freshness=DELAYED_CURRENT RSI=73.97 liquidity=15192413.0 spike=0.44
- ZMID.CA: score=25.77 buy_ready=True sector_rank=16 price=7.5 support=7.06 resistance=7.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=17 August 01:28 PM market time freshness=DELAYED_CURRENT RSI=49.56 liquidity=63372824.0 spike=0.26

## Backtesting Lite
- COPR.CA: 180d return=-22.76%, max drawdown=-53.05%, MA20>MA50 days last20=20, as_of=2026-08-15T21:00:00+00:00
- AJWA.CA: 180d return=56.14%, max drawdown=-21.78%, MA20>MA50 days last20=20, as_of=2026-08-15T21:00:00+00:00
- ETEL.CA: 180d return=82.04%, max drawdown=-30.44%, MA20>MA50 days last20=19, as_of=2026-08-15T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- COPR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Copper for Commercial Investment & Real Estate Development summary=Copper for Commercial Investment swings to EGP 7m net losses in 9M-25; NRPD’s EGM approves capital cut, increase; Two shareholders sell entire stakes in NRPD
  - Copper for Commercial Investment swings to EGP 7m net losses in 9M-25: https://english.mubasher.info/news/4530417/Copper-for-Commercial-Investment-swings-to-EGP-7m-net-losses-in-9M-25/
  - NRPD’s EGM approves capital cut, increase: https://english.mubasher.info/news/4042300/NRPD-s-EGM-approves-capital-cut-increase/
  - Two shareholders sell entire stakes in NRPD: https://english.mubasher.info/news/4006432/Two-shareholders-sell-entire-stakes-in-NRPD/
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=594 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- EFIC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=594 sources=3 expected=Egyptian Financial and Industrial summary=EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed; EFIC ordered to pay over EGP 126m as penalties; EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn
  - EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed: https://english.mubasher.info/news/4579891/EFIC-s-consolidated-profits-near-EGP-820m-in-2025-dividends-proposed/
  - EFIC ordered to pay over EGP 126m as penalties: https://english.mubasher.info/news/4535935/EFIC-ordered-to-pay-over-EGP-126m-as-penalties/
  - EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn: https://english.mubasher.info/news/4528902/EFIC-generates-lower-consolidated-net-profits-at-EGP-803m-in-9M-25-net-sales-near-EGP-8bn/
- RACC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Raya Customer Experience summary=Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.
- MBSC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=594 sources=3 expected=Misr Beni Suef Cement summary=Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025; Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25; Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25
  - Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025: https://english.mubasher.info/news/4599415/Misr-Beni-Suef-s-consolidated-net-profits-near-EGP-4bn-in-2025/
  - Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25: https://english.mubasher.info/news/4488249/Misr-Beni-Suef-s-consolidated-net-profits-hit-EGP-953m-in-H1-25/
  - Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25: https://english.mubasher.info/news/4455784/Misr-Beni-Suef-Cement-s-consolidate-profits-fall-to-EGP-574m-in-Q1-25/
- SUGR.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=594 sources=3 expected=Delta Sugar summary=Delta Sugar’s net profits fall 74% in Q1-26; Delta Sugar stock tests key resistance near EGP 50 amid downtrend; Delta Sugar turns to EGP 346m net losses in 2025
  - Delta Sugar’s net profits fall 74% in Q1-26: https://english.mubasher.info/news/4604921/Delta-Sugar-s-net-profits-fall-74-in-Q1-26/
  - Delta Sugar stock tests key resistance near EGP 50 amid downtrend: https://english.mubasher.info/news/4584932/Delta-Sugar-stock-tests-key-resistance-near-EGP-50-amid-downtrend/
  - Delta Sugar turns to EGP 346m net losses in 2025: https://english.mubasher.info/news/4557875/Delta-Sugar-turns-to-EGP-346m-net-losses-in-2025/

## Warnings
- Evidence for COPR.CA matches the company but no source/report date was detected.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EFIC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for RACC.CA: source text did not clearly match RACC.CA / Raya Customer Experience.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for SUGR.CA matches the company but appears old; latest detected date is 2025-01-01.
