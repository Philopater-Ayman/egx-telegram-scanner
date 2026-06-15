# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-15T12:42:35.272089+00:00
Generated Cairo: 2026-06-15 15:42
Run timing: target 09:15 Cairo | generated Cairo 2026-06-15 15:42 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-15 15:39

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 180/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, June 15
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 35.0% / above MA50 55.0%
- EGX70 regime: BEARISH / above MA20 52.63% / above MA50 73.68%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=1014171776.0 spike=1.2 score=20.79
- COMI.CA: liquidity=838770048.0 spike=1.27 score=21.39
- PHDC.CA: liquidity=831878080.0 spike=2.16 score=25.72
- FWRY.CA: liquidity=559666880.0 spike=2.04 score=11.81
- EMFD.CA: liquidity=422189024.0 spike=1.71 score=24.82

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (23.81%). Liquidity is modest and sector support is limited, so the market is in DEFENSIVE_NO_NEW_BUY mode. While a few real‑estate and automotive stocks show bullish watch signals and short‑term accumulation spikes, the overall outlook for the next 1‑3 days remains cautious.
- EGX30/EGX70 trends bearish, median 5‑day returns negative, liquidity spikes modest
- Sector breadth low; only automotive & distribution and real‑estate lead, but still defensive
- Top watch‑list stocks (ARAB.CA, PHDC.CA, MTIE.CA, etc.) have bullish outlooks but are near resistance or far above support
- Risk mode DEFENSIVE_NO_NEW_BUY limits new entries until market regime improves
- Uncertainty remains high as broader market weakness may persist over the next 1‑3 days

## Top Liquidity Spikes
- EASB.CA: spike=10.42 liquidity=20741704.0 outlook=CONSTRUCTIVE score=55.55 buy_ready=False
- MOSC.CA: spike=8.72 liquidity=58435752.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ATLC.CA: spike=4.73 liquidity=19910200.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MOED.CA: spike=4.04 liquidity=44960100.0 outlook=WEAK_OR_RISKY score=26.55 buy_ready=False
- MPCO.CA: spike=4.02 liquidity=309592896.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=9.61 5d=5.54% 20d=-2.23% aboveMA50=100.0%
- #2 Real Estate: score=7.37 5d=1.94% 20d=5.26% aboveMA50=92.31%
- #3 Investment Holding: score=5.98 5d=2.48% 20d=0.96% aboveMA50=66.67%
- #4 Food, Beverages & Tobacco: score=5.28 5d=-0.93% 20d=0.18% aboveMA50=71.43%
- #5 Education: score=4.77 5d=0.22% 20d=-3.69% aboveMA50=100.0%
- #6 Banking & Financials: score=4.63 5d=-0.12% 20d=-1.16% aboveMA50=70.0%
- #7 Energy & Petrochemicals: score=4.21 5d=0.21% 20d=0.53% aboveMA50=75.0%
- #8 Textiles: score=4.13 5d=-2.08% 20d=3.81% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MTIE.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- ORHD.CA: BULLISH_WATCH score=92.37 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- EFID.CA: BULLISH_WATCH score=92.28 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- HDBK.CA: BULLISH_WATCH score=91.63 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- OBRI.CA: BULLISH_WATCH score=91.55 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- ARAB.CA: BULLISH_WATCH score=90.37 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- MENA.CA: BULLISH_WATCH score=87.37 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PHDC.CA: BULLISH_WATCH score=86.37 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- EMFD.CA: BULLISH_WATCH score=86.37 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; far above support
- KWIN.CA: BULLISH_WATCH score=85.55 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=10.51 buy_ready=False sector_rank=9 price=205.05 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.87 liquidity=2089836.63 spike=0.28
- ABUK.CA: score=9.81 buy_ready=False sector_rank=20 price=72.62 support=72.7 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.03 liquidity=192272384.0 spike=1.48
- ACAMD.CA: score=20.42 buy_ready=False sector_rank=9 price=2.3 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.69 liquidity=94643680.0 spike=0.72
- ACGC.CA: score=18.65 buy_ready=False sector_rank=8 price=9.36 support=8.95 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.88 liquidity=15800499.0 spike=0.27
- ADCI.CA: score=21.24 buy_ready=False sector_rank=9 price=226.87 support=202.22 resistance=230.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.08 liquidity=10227359.0 spike=1.41
- ADIB.CA: score=21.53 buy_ready=False sector_rank=6 price=47.37 support=44.01 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.44 liquidity=171506000.0 spike=1.34
- ADPC.CA: score=11.07 buy_ready=False sector_rank=9 price=3.55 support=3.45 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.71 liquidity=5649651.0 spike=0.22
- AFDI.CA: score=18.42 buy_ready=False sector_rank=9 price=42.32 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=10787811.0 spike=0.64
- AFMC.CA: score=10.24 buy_ready=False sector_rank=9 price=71.35 support=67.0 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=56.21 liquidity=1821077.13 spike=0.3
- AJWA.CA: score=10.42 buy_ready=False sector_rank=9 price=170.69 support=160.0 resistance=179.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=73531520.0 spike=3.54
- ALCN.CA: score=15.31 buy_ready=False sector_rank=10 price=28.85 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.7 liquidity=13055933.0 spike=0.75
- ALUM.CA: score=12.78 buy_ready=False sector_rank=9 price=23.55 support=23.05 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.53 liquidity=4357083.5 spike=0.22
- AMER.CA: score=21.4 buy_ready=False sector_rank=2 price=2.63 support=2.52 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=66453496.0 spike=0.62
- AMES.CA: score=3.76 buy_ready=False sector_rank=9 price=48.88 support=48.0 resistance=55.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.71 liquidity=1342877.63 spike=0.28
- AMIA.CA: score=19.18 buy_ready=False sector_rank=9 price=9.22 support=8.54 resistance=9.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=68.38 liquidity=25134672.0 spike=1.38
- AMOC.CA: score=10.68 buy_ready=False sector_rank=7 price=7.82 support=7.84 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=76087472.0 spike=1.0
- ANFI.CA: score=23.68 buy_ready=False sector_rank=9 price=23.96 support=13.73 resistance=24.3 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=92.83 liquidity=138402035.55 spike=3.13
- APSW.CA: score=0.06 buy_ready=False sector_rank=9 price=8.6 support=8.24 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=31.58 liquidity=635381.31 spike=0.62
- ARAB.CA: score=29.96 buy_ready=False sector_rank=2 price=0.22 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=285811712.0 spike=3.28
- ARCC.CA: score=20.18 buy_ready=False sector_rank=12 price=56.65 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=25131430.0 spike=0.65
- AREH.CA: score=7.26 buy_ready=False sector_rank=9 price=1.61 support=1.53 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51553196.0 spike=1.92
- ARVA.CA: score=6.9 buy_ready=False sector_rank=9 price=11.84 support=11.7 resistance=12.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47834524.0 spike=1.74
- ASCM.CA: score=21.22 buy_ready=False sector_rank=9 price=60.77 support=47.3 resistance=61.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.32 liquidity=128938760.0 spike=1.9
- ASPI.CA: score=22.42 buy_ready=False sector_rank=9 price=0.31 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.12 liquidity=25219722.0 spike=0.37
- ATLC.CA: score=9.35 buy_ready=False sector_rank=18 price=5.2 support=4.84 resistance=5.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19910200.0 spike=4.73
- ATQA.CA: score=12.85 buy_ready=False sector_rank=20 price=9.42 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.32 liquidity=24898280.0 spike=0.68
- AXPH.CA: score=9.55 buy_ready=False sector_rank=9 price=1121.32 support=1111.0 resistance=1185.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=40.02 liquidity=1133709.5 spike=0.35
- BINV.CA: score=25.15 buy_ready=False sector_rank=3 price=47.89 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.61 liquidity=15682130.0 spike=1.38
- BIOC.CA: score=9.48 buy_ready=False sector_rank=9 price=70.84 support=68.34 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=51.09 liquidity=1061660.0 spike=0.2
- BTFH.CA: score=13.53 buy_ready=False sector_rank=18 price=3.02 support=2.96 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.23 liquidity=224325616.0 spike=1.09
- CAED.CA: score=7.62 buy_ready=False sector_rank=9 price=71.04 support=67.21 resistance=79.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.09 liquidity=4202823.5 spike=0.46
- CANA.CA: score=6.09 buy_ready=False sector_rank=6 price=38.0 support=36.04 resistance=38.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15752017.0 spike=1.12
- CCAP.CA: score=20.79 buy_ready=False sector_rank=3 price=5.04 support=4.94 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=1014171776.0 spike=1.2
- CCRS.CA: score=18.42 buy_ready=False sector_rank=9 price=2.4 support=2.22 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=14537950.0 spike=0.57
- CEFM.CA: score=10.36 buy_ready=False sector_rank=9 price=103.48 support=100.53 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.29 liquidity=1936724.5 spike=0.53
- CERA.CA: score=18.16 buy_ready=False sector_rank=9 price=1.18 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=8735738.0 spike=0.64
- CFGH.CA: score=-0.58 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1904.14 spike=0.31
- CICH.CA: score=0.9 buy_ready=False sector_rank=18 price=11.6 support=11.1 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.96 liquidity=1549278.13 spike=0.44
- CIEB.CA: score=13.89 buy_ready=False sector_rank=6 price=23.48 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.74 liquidity=7914850.5 spike=1.06
- CIRA.CA: score=17.97 buy_ready=False sector_rank=5 price=26.81 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.14 liquidity=7058725.0 spike=0.28
- CLHO.CA: score=17.96 buy_ready=False sector_rank=13 price=15.49 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.06 liquidity=11015227.0 spike=0.37
- CNFN.CA: score=8.92 buy_ready=False sector_rank=18 price=4.42 support=4.36 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.28 liquidity=5575352.5 spike=0.35
- COMI.CA: score=21.39 buy_ready=False sector_rank=6 price=134.95 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.42 liquidity=838770048.0 spike=1.27
- COPR.CA: score=17.42 buy_ready=False sector_rank=9 price=0.36 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=17356636.0 spike=0.42
- COSG.CA: score=18.42 buy_ready=False sector_rank=9 price=1.57 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=33071790.0 spike=0.48
- CPCI.CA: score=10.24 buy_ready=False sector_rank=9 price=362.32 support=345.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=71.26 liquidity=1820886.75 spike=0.67
- CSAG.CA: score=20.31 buy_ready=False sector_rank=10 price=31.39 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=53.78 liquidity=11060223.0 spike=0.8
- DAPH.CA: score=7.39 buy_ready=False sector_rank=9 price=77.72 support=76.6 resistance=89.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=2973126.25 spike=0.1
- DEIN.CA: score=6.42 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.69 buy_ready=False sector_rank=4 price=24.35 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.34 liquidity=576830.88 spike=0.23
- DSCW.CA: score=18.66 buy_ready=False sector_rank=9 price=1.8 support=1.71 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=56984248.0 spike=1.12
- DTPP.CA: score=3.79 buy_ready=False sector_rank=9 price=117.16 support=117.01 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.87 liquidity=2868894.25 spike=1.25
- EALR.CA: score=9.95 buy_ready=False sector_rank=9 price=353.48 support=346.01 resistance=383.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.61 liquidity=1528419.75 spike=0.35
- EASB.CA: score=24.42 buy_ready=False sector_rank=9 price=6.11 support=4.61 resistance=6.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=88.89 liquidity=20741704.0 spike=10.42
- EAST.CA: score=21.11 buy_ready=False sector_rank=4 price=39.79 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.08 liquidity=59913124.0 spike=0.91
- EBSC.CA: score=12.9 buy_ready=False sector_rank=9 price=1.89 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.37 liquidity=2481586.25 spike=0.92
- ECAP.CA: score=13.11 buy_ready=False sector_rank=9 price=31.77 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=91.4 liquidity=3689791.75 spike=0.71
- EDFM.CA: score=8.74 buy_ready=False sector_rank=9 price=334.03 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=56.59 liquidity=317029.5 spike=0.47
- EEII.CA: score=13.46 buy_ready=False sector_rank=9 price=2.37 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.45 liquidity=5036192.5 spike=0.26
- EFIC.CA: score=0.21 buy_ready=False sector_rank=20 price=205.05 support=192.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.09 liquidity=2355921.5 spike=0.68
- EFID.CA: score=23.37 buy_ready=False sector_rank=4 price=28.76 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.53 liquidity=155303072.0 spike=2.13
- EFIH.CA: score=18.13 buy_ready=False sector_rank=15 price=21.35 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.78 liquidity=68410616.0 spike=1.2
- EGAL.CA: score=9.61 buy_ready=False sector_rank=20 price=299.11 support=305.01 resistance=335.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.51 liquidity=140215056.0 spike=1.38
- EGAS.CA: score=22.72 buy_ready=False sector_rank=7 price=51.5 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=73.53 liquidity=12489515.0 spike=1.02
- EGBE.CA: score=8.91 buy_ready=False sector_rank=6 price=0.43 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=43.01 liquidity=55901.77 spike=0.4
- EGCH.CA: score=16.85 buy_ready=False sector_rank=20 price=13.2 support=13.2 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=51686324.0 spike=0.47
- EGSA.CA: score=2.51 buy_ready=False sector_rank=17 price=8.74 support=8.3 resistance=9.19 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=21.87 liquidity=5742.18 spike=0.39
- EGTS.CA: score=21.4 buy_ready=False sector_rank=2 price=17.8 support=14.72 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=44999680.0 spike=0.36
- EHDR.CA: score=20.64 buy_ready=False sector_rank=9 price=2.71 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=73.39 liquidity=63055932.0 spike=1.11
- EKHO.CA: score=10.68 buy_ready=False sector_rank=7 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=13.15 buy_ready=False sector_rank=19 price=2.11 support=2.06 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=11499982.0 spike=0.43
- ELKA.CA: score=19.42 buy_ready=False sector_rank=9 price=1.26 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=38989924.0 spike=0.87
- ELNA.CA: score=8.06 buy_ready=False sector_rank=9 price=37.74 support=37.11 resistance=41.99 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=35.15 liquidity=820580.86 spike=2.41
- ELSH.CA: score=17.42 buy_ready=False sector_rank=9 price=12.95 support=8.1 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.86 liquidity=111334840.0 spike=0.65
- ELWA.CA: score=16.04 buy_ready=False sector_rank=9 price=2.1 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=5222720.0 spike=1.7
- EMFD.CA: score=24.82 buy_ready=False sector_rank=2 price=12.29 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.06 liquidity=422189024.0 spike=1.71
- ENGC.CA: score=23.44 buy_ready=False sector_rank=9 price=35.94 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=65.98 liquidity=33759472.0 spike=2.51
- EOSB.CA: score=13.88 buy_ready=False sector_rank=9 price=1.48 support=1.34 resistance=1.55 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=198135.0 spike=1.63
- EPCO.CA: score=17.31 buy_ready=False sector_rank=9 price=9.25 support=8.56 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=6887745.5 spike=0.62
- EPPK.CA: score=6.76 buy_ready=False sector_rank=9 price=11.86 support=11.67 resistance=13.0 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=45.61 liquidity=1064909.37 spike=1.14
- ETEL.CA: score=10.11 buy_ready=False sector_rank=17 price=92.58 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.37 liquidity=106964128.0 spike=1.3
- ETRS.CA: score=22.06 buy_ready=False sector_rank=9 price=10.09 support=7.37 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.99 liquidity=136271712.0 spike=2.32
- EXPA.CA: score=18.85 buy_ready=False sector_rank=6 price=18.61 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.57 liquidity=16639997.0 spike=0.46
- FAIT.CA: score=14.03 buy_ready=False sector_rank=6 price=37.42 support=35.01 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=3179499.0 spike=0.53
- FAITA.CA: score=12.87 buy_ready=False sector_rank=6 price=1.0 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=22158.95 spike=0.5
- FERC.CA: score=0.17 buy_ready=False sector_rank=20 price=76.0 support=75.0 resistance=81.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.87 liquidity=1316604.88 spike=0.24
- FWRY.CA: score=11.81 buy_ready=False sector_rank=15 price=18.77 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=33.26 liquidity=559666880.0 spike=2.04
- GBCO.CA: score=24.4 buy_ready=False sector_rank=1 price=28.45 support=25.25 resistance=29.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.42 liquidity=104245280.0 spike=0.9
- GDWA.CA: score=18.69 buy_ready=False sector_rank=9 price=0.8 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.65 liquidity=9274858.0 spike=0.7
- GGCC.CA: score=12.98 buy_ready=False sector_rank=9 price=0.41 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=57.3 liquidity=5555478.5 spike=0.74
- GIHD.CA: score=13.77 buy_ready=False sector_rank=9 price=41.35 support=35.15 resistance=43.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=58.24 liquidity=3345570.0 spike=0.8
- GMCI.CA: score=13.75 buy_ready=False sector_rank=9 price=1.78 support=1.68 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=830158.0 spike=2.25
- GRCA.CA: score=6.18 buy_ready=False sector_rank=9 price=55.41 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.85 liquidity=5764076.0 spike=0.67
- GSSC.CA: score=3.33 buy_ready=False sector_rank=9 price=248.31 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.32 liquidity=2914336.25 spike=0.5
- GTWL.CA: score=3.6 buy_ready=False sector_rank=9 price=46.34 support=45.47 resistance=58.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.05 liquidity=3177269.0 spike=0.45
- HDBK.CA: score=25.17 buy_ready=False sector_rank=6 price=146.79 support=138.0 resistance=146.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.95 liquidity=40530624.0 spike=3.16
- HELI.CA: score=21.4 buy_ready=False sector_rank=2 price=6.42 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.42 liquidity=134535248.0 spike=0.88
- HRHO.CA: score=15.45 buy_ready=False sector_rank=18 price=27.03 support=25.8 resistance=28.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=148337776.0 spike=1.05
- ICID.CA: score=16.61 buy_ready=False sector_rank=9 price=7.0 support=4.5 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=87.09 liquidity=9190246.0 spike=0.57
- IDRE.CA: score=16.7 buy_ready=False sector_rank=9 price=43.08 support=41.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.87 liquidity=8281187.5 spike=0.26
- IFAP.CA: score=6.79 buy_ready=False sector_rank=14 price=19.51 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.69 liquidity=2853074.5 spike=0.33
- INFI.CA: score=9.81 buy_ready=False sector_rank=9 price=98.25 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.0 liquidity=7385995.5 spike=0.5
- IRON.CA: score=7.26 buy_ready=False sector_rank=20 price=32.04 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.27 liquidity=4410819.0 spike=0.57
- ISMA.CA: score=19.42 buy_ready=False sector_rank=9 price=30.25 support=23.1 resistance=31.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=88.93 liquidity=23259496.0 spike=0.59
- ISMQ.CA: score=21.73 buy_ready=False sector_rank=20 price=8.17 support=7.27 resistance=8.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.52 liquidity=98957048.0 spike=1.44
- ISPH.CA: score=19.96 buy_ready=False sector_rank=13 price=12.15 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=81381072.0 spike=0.61
- JUFO.CA: score=21.45 buy_ready=False sector_rank=4 price=30.83 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.29 liquidity=52074372.0 spike=1.17
- KABO.CA: score=17.78 buy_ready=False sector_rank=8 price=6.24 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.27 liquidity=7123250.0 spike=0.34
- KWIN.CA: score=25.42 buy_ready=False sector_rank=9 price=75.04 support=69.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.34 liquidity=16113040.0 spike=3.91
- KZPC.CA: score=13.99 buy_ready=False sector_rank=9 price=10.54 support=10.3 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.05 liquidity=5569690.0 spike=0.5
- LCSW.CA: score=13.75 buy_ready=False sector_rank=12 price=26.65 support=26.0 resistance=28.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=5569763.0 spike=0.49
- LUTS.CA: score=24.1 buy_ready=False sector_rank=9 price=0.75 support=0.54 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=86.92 liquidity=96429048.0 spike=3.34
- MAAL.CA: score=9.9 buy_ready=False sector_rank=9 price=5.79 support=4.44 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.65 liquidity=2484465.75 spike=0.19
- MASR.CA: score=21.84 buy_ready=False sector_rank=9 price=7.1 support=6.54 resistance=7.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=93983112.0 spike=1.71
- MBSC.CA: score=19.06 buy_ready=False sector_rank=12 price=271.99 support=262.02 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.84 liquidity=68915680.0 spike=1.44
- MCQE.CA: score=10.18 buy_ready=False sector_rank=12 price=178.81 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.73 liquidity=13185312.0 spike=0.73
- MCRO.CA: score=14.42 buy_ready=False sector_rank=9 price=1.23 support=1.2 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=18334546.0 spike=0.34
- MENA.CA: score=20.39 buy_ready=False sector_rank=2 price=6.73 support=5.91 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=6990484.5 spike=0.41
- MEPA.CA: score=18.42 buy_ready=False sector_rank=9 price=1.7 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=11141276.0 spike=0.61
- MFPC.CA: score=10.43 buy_ready=False sector_rank=20 price=37.51 support=38.15 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=5.34 liquidity=152621600.0 spike=1.79
- MFSC.CA: score=6.22 buy_ready=False sector_rank=9 price=45.52 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.01 liquidity=2799541.75 spike=0.18
- MHOT.CA: score=9.83 buy_ready=False sector_rank=11 price=29.73 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.99 liquidity=6570511.5 spike=0.31
- MICH.CA: score=20.42 buy_ready=False sector_rank=9 price=37.0 support=35.05 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.34 liquidity=10797704.0 spike=0.75
- MILS.CA: score=20.58 buy_ready=False sector_rank=9 price=146.0 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=71.63 liquidity=20754240.0 spike=1.08
- MIPH.CA: score=10.91 buy_ready=False sector_rank=13 price=662.15 support=640.0 resistance=700.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=947748.19 spike=0.33
- MOED.CA: score=14.42 buy_ready=False sector_rank=9 price=0.71 support=0.65 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.85 liquidity=44960100.0 spike=4.04
- MOIL.CA: score=8.75 buy_ready=False sector_rank=7 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.12 liquidity=66865.75 spike=0.36
- MOIN.CA: score=8.1 buy_ready=False sector_rank=9 price=24.88 support=24.1 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.38 liquidity=682794.0 spike=0.39
- MOSC.CA: score=10.42 buy_ready=False sector_rank=9 price=280.61 support=280.0 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58435752.0 spike=8.72
- MPCI.CA: score=18.42 buy_ready=False sector_rank=9 price=218.53 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.25 liquidity=21913912.0 spike=0.25
- MPCO.CA: score=9.94 buy_ready=False sector_rank=14 price=1.99 support=1.8 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=309592896.0 spike=4.02
- MPRC.CA: score=18.42 buy_ready=False sector_rank=9 price=31.88 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.94 liquidity=11362642.0 spike=0.55
- MTIE.CA: score=25.5 buy_ready=False sector_rank=1 price=9.23 support=8.65 resistance=9.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.78 liquidity=29225384.0 spike=1.55
- NAHO.CA: score=4.45 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=33623.83 spike=0.94
- NCCW.CA: score=17.42 buy_ready=False sector_rank=9 price=6.44 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.22 liquidity=25013022.0 spike=0.92
- NEDA.CA: score=8.57 buy_ready=False sector_rank=9 price=2.75 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=53.57 liquidity=151602.0 spike=0.37
- NHPS.CA: score=6.45 buy_ready=False sector_rank=9 price=67.72 support=65.03 resistance=72.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=2026813.38 spike=0.39
- NINH.CA: score=5.42 buy_ready=False sector_rank=9 price=17.36 support=16.8 resistance=19.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.72 liquidity=1999770.0 spike=0.27
- NIPH.CA: score=17.96 buy_ready=False sector_rank=13 price=162.03 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.23 liquidity=28990388.0 spike=0.29
- OBRI.CA: score=24.1 buy_ready=False sector_rank=9 price=36.8 support=33.63 resistance=38.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=24226088.0 spike=1.84
- OCDI.CA: score=18.4 buy_ready=False sector_rank=2 price=20.7 support=20.0 resistance=22.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.76 liquidity=17382820.0 spike=0.49
- OCPH.CA: score=5.56 buy_ready=False sector_rank=9 price=344.59 support=337.0 resistance=394.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=28.16 liquidity=2140859.0 spike=0.29
- ODIN.CA: score=21.96 buy_ready=False sector_rank=9 price=2.18 support=1.89 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=19240278.0 spike=1.77
- OFH.CA: score=18.42 buy_ready=False sector_rank=9 price=0.62 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=52.73 liquidity=15273863.0 spike=0.67
- OIH.CA: score=17.39 buy_ready=False sector_rank=3 price=1.37 support=1.33 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=74922656.0 spike=0.78
- OLFI.CA: score=23.19 buy_ready=False sector_rank=4 price=22.47 support=21.0 resistance=22.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.16 liquidity=48589728.0 spike=2.54
- ORAS.CA: score=4.6 buy_ready=False sector_rank=16 price=779.75 support=772.0 resistance=785.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=260625600.0 spike=1.0
- ORHD.CA: score=23.4 buy_ready=False sector_rank=2 price=37.23 support=33.09 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.12 liquidity=166265392.0 spike=0.89
- ORWE.CA: score=20.65 buy_ready=False sector_rank=8 price=23.13 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=61.86 liquidity=14635981.0 spike=0.33
- PHAR.CA: score=14.96 buy_ready=False sector_rank=13 price=84.02 support=83.02 resistance=91.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.27 liquidity=20279238.0 spike=0.65
- PHDC.CA: score=25.72 buy_ready=False sector_rank=2 price=16.09 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.33 liquidity=831878080.0 spike=2.16
- PHTV.CA: score=9.48 buy_ready=False sector_rank=9 price=219.5 support=207.0 resistance=223.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42230984.0 spike=3.03
- POUL.CA: score=19.91 buy_ready=False sector_rank=4 price=36.75 support=34.8 resistance=38.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=62261200.0 spike=1.4
- PRCL.CA: score=20.92 buy_ready=False sector_rank=12 price=24.52 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.36 liquidity=39234232.0 spike=1.37
- PRDC.CA: score=22.4 buy_ready=False sector_rank=2 price=6.67 support=5.3 resistance=6.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=81.2 liquidity=27588690.0 spike=0.31
- PRMH.CA: score=19.52 buy_ready=False sector_rank=9 price=2.77 support=2.19 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=75.61 liquidity=25045224.0 spike=1.05
- RACC.CA: score=8.89 buy_ready=False sector_rank=9 price=9.68 support=9.38 resistance=10.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.99 liquidity=5473105.5 spike=0.46
- RAKT.CA: score=7.16 buy_ready=False sector_rank=9 price=22.59 support=22.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.37 liquidity=662938.56 spike=2.04
- RAYA.CA: score=11.76 buy_ready=False sector_rank=21 price=6.98 support=6.7 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=30.28 liquidity=66866220.0 spike=0.68
- RMDA.CA: score=19.96 buy_ready=False sector_rank=13 price=5.1 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.63 liquidity=23223652.0 spike=0.25
- ROTO.CA: score=18.25 buy_ready=False sector_rank=9 price=34.47 support=32.66 resistance=35.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=7825696.5 spike=0.59
- RREI.CA: score=20.25 buy_ready=False sector_rank=9 price=3.5 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.32 liquidity=9827219.0 spike=0.46
- RTVC.CA: score=9.97 buy_ready=False sector_rank=9 price=3.85 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.28 liquidity=2553483.25 spike=0.37
- RUBX.CA: score=11.35 buy_ready=False sector_rank=9 price=9.86 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.87 liquidity=6931151.0 spike=0.59
- SAUD.CA: score=15.26 buy_ready=False sector_rank=6 price=22.0 support=20.82 resistance=23.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.86 liquidity=9407231.0 spike=0.68
- SCEM.CA: score=15.77 buy_ready=False sector_rank=12 price=62.19 support=59.3 resistance=67.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.15 liquidity=7591917.0 spike=0.2
- SCFM.CA: score=11.63 buy_ready=False sector_rank=9 price=253.42 support=248.1 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=6209036.5 spike=0.49
- SCTS.CA: score=7.47 buy_ready=False sector_rank=5 price=605.92 support=590.01 resistance=689.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=29.2 liquidity=3560835.0 spike=0.52
- SDTI.CA: score=15.81 buy_ready=False sector_rank=9 price=46.96 support=43.4 resistance=47.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.43 liquidity=3385993.75 spike=0.21
- SEIG.CA: score=9.55 buy_ready=False sector_rank=9 price=181.31 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=53.04 liquidity=1131488.0 spike=0.22
- SIPC.CA: score=11.53 buy_ready=False sector_rank=9 price=3.47 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=6114687.5 spike=0.44
- SKPC.CA: score=12.85 buy_ready=False sector_rank=20 price=16.35 support=16.29 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.29 liquidity=34248996.0 spike=0.6
- SMFR.CA: score=11.68 buy_ready=False sector_rank=9 price=204.19 support=192.0 resistance=222.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.88 liquidity=3263444.5 spike=0.56
- SNFC.CA: score=20.42 buy_ready=False sector_rank=9 price=12.39 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.53 liquidity=10476181.0 spike=0.39
- SPIN.CA: score=1.52 buy_ready=False sector_rank=8 price=14.03 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.56 liquidity=863524.19 spike=0.19
- SPMD.CA: score=10.95 buy_ready=False sector_rank=9 price=0.41 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.29 liquidity=2528292.5 spike=0.11
- SUGR.CA: score=8.3 buy_ready=False sector_rank=4 price=48.54 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=53.03 liquidity=3188448.75 spike=0.21
- SVCE.CA: score=8.0 buy_ready=False sector_rank=9 price=9.1 support=8.56 resistance=9.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=204012464.0 spike=2.29
- SWDY.CA: score=15.21 buy_ready=False sector_rank=19 price=86.19 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.16 liquidity=8054483.5 spike=0.35
- TALM.CA: score=11.13 buy_ready=False sector_rank=5 price=16.12 support=15.12 resistance=16.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.41 liquidity=3220752.0 spike=0.28
- TMGH.CA: score=21.4 buy_ready=False sector_rank=2 price=95.03 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=351156128.0 spike=0.77
- TRTO.CA: score=8.82 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=1849.87 spike=2.2
- UEFM.CA: score=2.89 buy_ready=False sector_rank=9 price=472.48 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=27.33 liquidity=1734027.88 spike=1.87
- UEGC.CA: score=22.42 buy_ready=False sector_rank=9 price=1.41 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=61.76 liquidity=10809640.0 spike=0.42
- UNIP.CA: score=13.94 buy_ready=False sector_rank=9 price=0.32 support=0.28 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=7517672.0 spike=0.37
- UNIT.CA: score=14.73 buy_ready=False sector_rank=2 price=13.48 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=1331317.13 spike=0.12
- WCDF.CA: score=1.81 buy_ready=False sector_rank=9 price=507.59 support=450.0 resistance=554.25 source=Yahoo Finance as_of=2026-06-13T21:00:00+00:00 freshness=FRESH RSI=2.97 liquidity=465460.03 spike=1.46
- WKOL.CA: score=7.89 buy_ready=False sector_rank=9 price=290.5 support=290.0 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.46 liquidity=2466558.25 spike=0.61
- ZEOT.CA: score=21.88 buy_ready=False sector_rank=9 price=9.4 support=8.41 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=65.99 liquidity=10554799.0 spike=1.73
- ZMID.CA: score=25.4 buy_ready=False sector_rank=2 price=6.16 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.32 liquidity=133059224.0 spike=0.56

## Backtesting Lite
- ARAB.CA: 180d return=14.13%, max drawdown=-38.02%, MA20>MA50 days last20=20, as_of=2026-06-13T21:00:00+00:00
- PHDC.CA: 180d return=115.21%, max drawdown=-15.81%, MA20>MA50 days last20=20, as_of=2026-06-13T21:00:00+00:00
- MTIE.CA: 180d return=40.09%, max drawdown=-20.49%, MA20>MA50 days last20=20, as_of=2026-06-13T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- PHDC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=530 sources=3 expected=Palm Hills Development summary=Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma; Palm Hills records 30% higher profits in 2025, unveils new project in UAE; Strong momentum pushes Palm Hills toward EGP 10.15
  - Palm Hills, UAE’s Miran to launch new development project in Ras Al Hikma: https://english.mubasher.info/news/4598123/Palm-Hills-UAE-s-Miran-to-launch-new-development-project-in-Ras-Al-Hikma/
  - Palm Hills records 30% higher profits in 2025, unveils new project in UAE: https://english.mubasher.info/news/4580548/Palm-Hills-records-30-higher-profits-in-2025-unveils-new-project-in-UAE/
  - Strong momentum pushes Palm Hills toward EGP 10.15: https://english.mubasher.info/news/4560871/Strong-momentum-pushes-Palm-Hills-toward-EGP-10-15/
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- KWIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Kahera El Watania Investment summary=ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m; El Kahera El Watania to buy stake in Assiut for Agricultural Development; Tycoon Holding acquires 85% of Alexandria National Investment
  - ADIB Egypt&#39;s Cairo National unveils equity reduction transaction worth over EGP 3m: https://english.mubasher.info/news/4546852/ADIB-Egypt-s-Cairo-National-unveils-equity-reduction-transaction-worth-over-EGP-3m/
  - El Kahera El Watania to buy stake in Assiut for Agricultural Development: https://english.mubasher.info/news/4009433/El-Kahera-El-Watania-to-buy-stake-in-Assiut-for-Agricultural-Development/
  - Tycoon Holding acquires 85% of Alexandria National Investment: https://english.mubasher.info/news/3844623/Tycoon-Holding-acquires-85-of-Alexandria-National-Investment/
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=530 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- EMFD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=530 sources=3 expected=Emaar Misr for Development summary=Emaar Misr posts higher revenues at EGP 19.8bn in 2025; Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25; Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea
  - Emaar Misr posts higher revenues at EGP 19.8bn in 2025: https://english.mubasher.info/news/4561643/Emaar-Misr-posts-higher-revenues-at-EGP-19-8bn-in-2025/
  - Emaar Misr’s consolidated net profits drop to EGP 4.2bn in 9M-25: https://english.mubasher.info/news/4525192/Emaar-Misr-s-consolidated-net-profits-drop-to-EGP-4-2bn-in-9M-25/
  - Emaar Misr, Golden Coast to establish EGP 900bn project in Red Sea: https://english.mubasher.info/news/4495287/Emaar-Misr-Golden-Coast-to-establish-EGP-900bn-project-in-Red-Sea/

## Warnings
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for PHDC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence for KWIN.CA matches the company but no source/report date was detected.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence for EMFD.CA matches the company but appears old; latest detected date is 2025-01-01.
