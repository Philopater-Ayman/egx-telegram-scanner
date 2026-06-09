# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-09T11:01:22.076059+00:00
Generated Cairo: 2026-06-09 14:01
Run timing: target 11:00 Cairo | generated Cairo 2026-06-09 14:01 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-09 13:56

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 181/190
- Top sector: Investment Holding

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Tuesday, June 09
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 65.0%
- EGX70 regime: MIXED / above MA20 57.89% / above MA50 84.21%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=444501504.0 spike=0.51 score=26.4
- COMI.CA: liquidity=416142368.0 spike=0.61 score=18.41
- ZMID.CA: liquidity=402742944.0 spike=1.93 score=25.26
- PHDC.CA: liquidity=322643840.0 spike=0.77 score=19.4
- ELSH.CA: liquidity=307997504.0 spike=2.64 score=23.44

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The scanner stays on HOLD because the EGX30 is in a bearish regime and sector breadth is weak (19%). EGX70 is mixed but still showing negative 5‑day returns. Risk mode is DEFENSIVE_NO_NEW_BUY, so no new entries are permitted despite several tickets showing bullish watch outlooks.
- Liquidity is adequate (most stocks trade in the tradeable or accumulation‑spike regime) but cooling on the top Investment Holding pick (CCAP.CA).
- Support levels are 6‑40% below current prices; resistance is close (1‑4% above) on most tickets, limiting short‑term upside.
- Sector breadth is thin; only Investment Holding, Tourism & Leisure and Technology lead, keeping overall market risk high.
- EGX30 bearish trend and low MA20 coverage (15%) suggest continued downside pressure for the next 1‑3 days.
- Uncertainty remains high as EGX70 mixed signals could shift if breadth improves or liquidity spikes intensify.

## Top Liquidity Spikes
- AJWA.CA: spike=13.94 liquidity=145612192.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NCCW.CA: spike=4.37 liquidity=90136576.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KWIN.CA: spike=2.72 liquidity=10149062.0 outlook=BULLISH_WATCH score=98.41 buy_ready=False
- ELSH.CA: spike=2.64 liquidity=307997504.0 outlook=CONSTRUCTIVE score=68.41 buy_ready=False
- CFGH.CA: spike=2.51 liquidity=11321.26 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=7.82 5d=2.57% 20d=12.11% aboveMA50=66.67%
- #2 Tourism & Leisure: score=6.95 5d=-8.23% 20d=13.34% aboveMA50=100.0%
- #3 Technology & Distribution: score=6.76 5d=-0.67% 20d=2.76% aboveMA50=100.0%
- #4 Real Estate: score=6.32 5d=0.0% 20d=5.37% aboveMA50=69.23%
- #5 Healthcare: score=6.02 5d=2.38% 20d=0.11% aboveMA50=100.0%
- #6 General / Verified EGX Expansion: score=5.41 5d=0.71% 20d=0.0% aboveMA50=80.77%
- #7 Building Materials: score=5.1 5d=-2.25% 20d=3.24% aboveMA50=100.0%
- #8 Textiles: score=5.0 5d=-2.86% 20d=4.04% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KWIN.CA: BULLISH_WATCH score=98.41 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- CERA.CA: BULLISH_WATCH score=95.41 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ANFI.CA: BULLISH_WATCH score=94.41 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ZMID.CA: BULLISH_WATCH score=93.32 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RAYA.CA: BULLISH_WATCH score=92.76 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EEII.CA: BULLISH_WATCH score=92.41 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MHOT.CA: BULLISH_WATCH score=91.95 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- PRCL.CA: BULLISH_WATCH score=88.1 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; far above support
- EALR.CA: BULLISH_WATCH score=86.41 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EPCO.CA: BULLISH_WATCH score=86.41 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=8.68 buy_ready=False sector_rank=6 price=222.41 support=211.65 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26399420.0 spike=2.26
- ABUK.CA: score=9.82 buy_ready=False sector_rank=18 price=81.34 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=18.89 liquidity=43264936.0 spike=0.34
- ACAMD.CA: score=23.38 buy_ready=False sector_rank=6 price=2.29 support=2.03 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 June 01:29 PM market time freshness=DELAYED_CURRENT RSI=60.34 liquidity=133482416.0 spike=1.11
- ACGC.CA: score=21.0 buy_ready=False sector_rank=8 price=9.81 support=8.51 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=60.49 liquidity=40503908.0 spike=0.73
- ADCI.CA: score=13.13 buy_ready=False sector_rank=6 price=219.0 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=3970900.0 spike=0.59
- ADIB.CA: score=18.41 buy_ready=False sector_rank=15 price=46.2 support=45.0 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=46.78 liquidity=55311212.0 spike=0.35
- ADPC.CA: score=6.43 buy_ready=False sector_rank=6 price=3.68 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=23.16 liquidity=5261653.5 spike=0.21
- AFDI.CA: score=20.37 buy_ready=False sector_rank=6 price=43.47 support=38.51 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=65.42 liquidity=9202939.0 spike=0.51
- AFMC.CA: score=11.86 buy_ready=False sector_rank=6 price=73.26 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=43.25 liquidity=698803.94 spike=0.05
- AJWA.CA: score=11.16 buy_ready=False sector_rank=6 price=150.84 support=135.0 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145612192.0 spike=13.94
- ALCN.CA: score=14.22 buy_ready=False sector_rank=20 price=28.7 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=43.44 liquidity=11404770.0 spike=0.49
- ALUM.CA: score=23.72 buy_ready=False sector_rank=6 price=25.8 support=22.52 resistance=26.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=28272510.0 spike=1.28
- AMER.CA: score=21.4 buy_ready=False sector_rank=4 price=2.8 support=2.32 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=104378032.0 spike=0.89
- AMES.CA: score=6.88 buy_ready=False sector_rank=6 price=50.89 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=30.81 liquidity=2712876.25 spike=0.35
- AMIA.CA: score=21.16 buy_ready=False sector_rank=6 price=9.07 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=60.44 liquidity=16745077.0 spike=0.55
- AMOC.CA: score=13.99 buy_ready=False sector_rank=9 price=8.26 support=8.12 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=27.42 liquidity=23239668.0 spike=0.28
- ANFI.CA: score=25.02 buy_ready=False sector_rank=6 price=15.52 support=13.5 resistance=16.04 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=59.56 liquidity=39216123.4 spike=1.93
- APSW.CA: score=3.54 buy_ready=False sector_rank=6 price=8.89 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=29.21 liquidity=372602.78 spike=0.35
- ARAB.CA: score=17.4 buy_ready=False sector_rank=4 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=27703964.0 spike=0.36
- ARCC.CA: score=21.04 buy_ready=False sector_rank=7 price=58.04 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=66.79 liquidity=11666293.0 spike=0.27
- AREH.CA: score=20.3 buy_ready=False sector_rank=6 price=1.51 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=28735086.0 spike=1.07
- ARVA.CA: score=20.16 buy_ready=False sector_rank=6 price=11.25 support=7.71 resistance=11.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=80.46 liquidity=21675410.0 spike=0.88
- ASCM.CA: score=18.16 buy_ready=False sector_rank=6 price=56.59 support=46.2 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=75.21 liquidity=63941076.0 spike=0.98
- ASPI.CA: score=25.18 buy_ready=False sector_rank=6 price=0.35 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=56.96 liquidity=114430992.0 spike=2.01
- ATLC.CA: score=10.99 buy_ready=False sector_rank=16 price=5.05 support=4.71 resistance=5.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=2903569.5 spike=0.4
- ATQA.CA: score=21.82 buy_ready=False sector_rank=18 price=9.95 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=54.35 liquidity=16518247.0 spike=0.4
- AXPH.CA: score=15.24 buy_ready=False sector_rank=6 price=1143.23 support=1023.0 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=48.22 liquidity=4071034.75 spike=0.69
- BINV.CA: score=17.21 buy_ready=False sector_rank=1 price=46.32 support=40.53 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=65.88 liquidity=2807527.5 spike=0.22
- BIOC.CA: score=12.85 buy_ready=False sector_rank=6 price=73.51 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=60.99 liquidity=1687863.63 spike=0.24
- BTFH.CA: score=13.09 buy_ready=False sector_rank=16 price=3.12 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=146376464.0 spike=0.62
- CAED.CA: score=10.55 buy_ready=False sector_rank=6 price=72.18 support=70.41 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=32.89 liquidity=6387665.0 spike=0.42
- CANA.CA: score=16.64 buy_ready=False sector_rank=15 price=37.0 support=33.15 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=75.35 liquidity=7229697.5 spike=0.51
- CCAP.CA: score=26.4 buy_ready=False sector_rank=1 price=5.57 support=4.66 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=444501504.0 spike=0.51
- CCRS.CA: score=19.81 buy_ready=False sector_rank=6 price=2.48 support=2.05 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=51.32 liquidity=8646865.0 spike=0.31
- CEFM.CA: score=4.88 buy_ready=False sector_rank=6 price=106.1 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=34.03 liquidity=713682.38 spike=0.1
- CERA.CA: score=25.46 buy_ready=False sector_rank=6 price=1.2 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=25476626.0 spike=1.65
- CFGH.CA: score=3.2 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=11321.26 spike=2.51
- CICH.CA: score=12.77 buy_ready=False sector_rank=16 price=11.73 support=11.45 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=4624819.5 spike=1.03
- CIEB.CA: score=11.89 buy_ready=False sector_rank=15 price=23.57 support=23.31 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=47.01 liquidity=3482632.25 spike=0.32
- CIRA.CA: score=14.21 buy_ready=False sector_rank=14 price=26.57 support=21.0 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=41.34 liquidity=5704112.0 spike=0.2
- CLHO.CA: score=19.4 buy_ready=False sector_rank=5 price=14.9 support=14.58 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=40.9 liquidity=18272370.0 spike=0.52
- CNFN.CA: score=11.08 buy_ready=False sector_rank=16 price=4.59 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=37.7 liquidity=3990821.5 spike=0.23
- COMI.CA: score=18.41 buy_ready=False sector_rank=15 price=132.76 support=129.8 resistance=144.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=45.93 liquidity=416142368.0 spike=0.61
- COPR.CA: score=20.16 buy_ready=False sector_rank=6 price=0.36 support=0.32 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=10245437.0 spike=0.26
- COSG.CA: score=21.16 buy_ready=False sector_rank=6 price=1.65 support=1.45 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=65.71 liquidity=30085084.0 spike=0.5
- CPCI.CA: score=8.92 buy_ready=False sector_rank=6 price=363.28 support=340.01 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=86.18 liquidity=755888.69 spike=0.1
- CSAG.CA: score=13.85 buy_ready=False sector_rank=20 price=31.25 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=52.62 liquidity=6632198.5 spike=0.36
- DAPH.CA: score=10.94 buy_ready=False sector_rank=6 price=81.59 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=21.61 liquidity=6775466.0 spike=0.22
- DEIN.CA: score=7.16 buy_ready=False sector_rank=6 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=2.68 buy_ready=False sector_rank=11 price=24.83 support=24.24 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=25.1 liquidity=1815944.63 spike=0.77
- DSCW.CA: score=17.16 buy_ready=False sector_rank=6 price=1.82 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=43.33 liquidity=12513769.0 spike=0.2
- DTPP.CA: score=5.55 buy_ready=False sector_rank=6 price=124.61 support=123.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=31.36 liquidity=1384304.38 spike=0.3
- EALR.CA: score=21.86 buy_ready=False sector_rank=6 price=366.99 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=41.47 liquidity=13795112.0 spike=1.35
- EASB.CA: score=10.16 buy_ready=False sector_rank=6 price=5.0 support=4.61 resistance=5.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=70.31 liquidity=997353.31 spike=0.66
- EAST.CA: score=21.09 buy_ready=False sector_rank=11 price=39.32 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=61.61 liquidity=6225288.0 spike=0.09
- EBSC.CA: score=11.93 buy_ready=False sector_rank=6 price=1.82 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=766257.75 spike=0.26
- ECAP.CA: score=14.55 buy_ready=False sector_rank=6 price=31.12 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=88.64 liquidity=6049822.0 spike=1.17
- EDFM.CA: score=15.43 buy_ready=False sector_rank=6 price=337.44 support=320.2 resistance=347.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=39.0 liquidity=2226359.25 spike=2.02
- EEII.CA: score=22.26 buy_ready=False sector_rank=6 price=2.48 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=47.5 liquidity=28785734.0 spike=1.55
- EFIC.CA: score=3.34 buy_ready=False sector_rank=18 price=205.25 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=6.06 liquidity=3526614.75 spike=0.88
- EFID.CA: score=18.86 buy_ready=False sector_rank=11 price=27.92 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=59.78 liquidity=36808300.0 spike=0.48
- EFIH.CA: score=15.84 buy_ready=False sector_rank=21 price=21.21 support=21.0 resistance=22.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=43.85 liquidity=30170308.0 spike=0.47
- EGAL.CA: score=17.82 buy_ready=False sector_rank=18 price=317.94 support=303.05 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=49.35 liquidity=50848220.0 spike=0.46
- EGAS.CA: score=12.79 buy_ready=False sector_rank=9 price=49.5 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=1803147.13 spike=0.13
- EGBE.CA: score=3.42 buy_ready=False sector_rank=15 price=0.45 support=0.42 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=12204.22 spike=0.09
- EGCH.CA: score=21.82 buy_ready=False sector_rank=18 price=14.67 support=12.26 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=22266270.0 spike=0.19
- EGSA.CA: score=8.79 buy_ready=False sector_rank=12 price=8.84 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=74.7 liquidity=14522.04 spike=0.96
- EGTS.CA: score=7.52 buy_ready=False sector_rank=4 price=19.9 support=18.35 resistance=20.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=173171312.0 spike=1.56
- EHDR.CA: score=18.16 buy_ready=False sector_rank=6 price=2.77 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=83.08 liquidity=53517908.0 spike=1.0
- EKHO.CA: score=10.99 buy_ready=False sector_rank=9 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=21.64 buy_ready=False sector_rank=13 price=2.17 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=12033814.0 spike=0.42
- ELKA.CA: score=22.16 buy_ready=False sector_rank=6 price=1.27 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=64.52 liquidity=26156384.0 spike=0.64
- ELNA.CA: score=4.23 buy_ready=False sector_rank=6 price=39.54 support=37.11 resistance=42.79 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=31.97 liquidity=64885.14 spike=0.21
- ELSH.CA: score=23.44 buy_ready=False sector_rank=6 price=13.17 support=7.92 resistance=13.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=86.84 liquidity=307997504.0 spike=2.64
- ELWA.CA: score=10.78 buy_ready=False sector_rank=6 price=2.14 support=1.79 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=91.43 liquidity=620332.5 spike=0.2
- EMFD.CA: score=21.4 buy_ready=False sector_rank=4 price=12.15 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=74.1 liquidity=179371376.0 spike=0.77
- ENGC.CA: score=24.02 buy_ready=False sector_rank=6 price=34.84 support=32.31 resistance=35.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=28878234.0 spike=2.43
- EOSB.CA: score=9.26 buy_ready=False sector_rank=6 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=100002.08 spike=0.84
- EPCO.CA: score=21.32 buy_ready=False sector_rank=6 price=9.3 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=49.69 liquidity=13570193.0 spike=1.08
- EPPK.CA: score=6.49 buy_ready=False sector_rank=6 price=12.24 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=51.79 liquidity=323696.69 spike=0.27
- ETEL.CA: score=18.77 buy_ready=False sector_rank=12 price=93.91 support=92.17 resistance=101.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=57151456.0 spike=0.52
- ETRS.CA: score=7.62 buy_ready=False sector_rank=6 price=9.36 support=9.0 resistance=9.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=88397688.0 spike=1.73
- EXPA.CA: score=20.41 buy_ready=False sector_rank=15 price=18.95 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=55.02 liquidity=30953136.0 spike=0.74
- FAIT.CA: score=10.54 buy_ready=False sector_rank=15 price=37.0 support=33.94 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=2130322.75 spike=0.33
- FAITA.CA: score=8.42 buy_ready=False sector_rank=15 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=9295.9 spike=0.18
- FERC.CA: score=1.01 buy_ready=False sector_rank=18 price=77.44 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=1195596.5 spike=0.19
- FWRY.CA: score=12.84 buy_ready=False sector_rank=21 price=18.7 support=18.32 resistance=21.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=38.25 liquidity=153033632.0 spike=0.52
- GBCO.CA: score=6.85 buy_ready=False sector_rank=17 price=27.95 support=27.13 resistance=28.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=220307632.0 spike=1.93
- GDWA.CA: score=18.93 buy_ready=False sector_rank=6 price=0.82 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=6769745.5 spike=0.66
- GGCC.CA: score=22.7 buy_ready=False sector_rank=6 price=0.43 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=9615603.0 spike=1.46
- GIHD.CA: score=14.24 buy_ready=False sector_rank=6 price=41.91 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=53.59 liquidity=1072865.5 spike=0.19
- GMCI.CA: score=6.54 buy_ready=False sector_rank=6 price=1.74 support=1.67 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=65.38 liquidity=380963.53 spike=0.94
- GRCA.CA: score=3.67 buy_ready=False sector_rank=6 price=55.26 support=53.16 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=27.6 liquidity=2510596.75 spike=0.27
- GSSC.CA: score=3.94 buy_ready=False sector_rank=6 price=248.61 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=7.12 liquidity=2780351.25 spike=0.32
- GTWL.CA: score=9.69 buy_ready=False sector_rank=6 price=47.37 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=13.49 liquidity=8310090.5 spike=1.11
- HDBK.CA: score=12.08 buy_ready=False sector_rank=15 price=142.1 support=138.75 resistance=150.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=58.6 liquidity=6670002.5 spike=0.41
- HELI.CA: score=6.46 buy_ready=False sector_rank=4 price=6.73 support=6.42 resistance=6.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=172727184.0 spike=1.03
- HRHO.CA: score=14.09 buy_ready=False sector_rank=16 price=26.41 support=26.05 resistance=30.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=46568876.0 spike=0.24
- ICID.CA: score=7.78 buy_ready=False sector_rank=6 price=6.66 support=6.12 resistance=6.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22954460.0 spike=1.81
- IDRE.CA: score=14.51 buy_ready=False sector_rank=6 price=43.91 support=39.72 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.96 liquidity=5345452.5 spike=0.16
- IFAP.CA: score=3.29 buy_ready=False sector_rank=10 price=19.48 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=3309485.75 spike=0.21
- INFI.CA: score=18.16 buy_ready=False sector_rank=6 price=101.63 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=13554608.0 spike=0.81
- IRON.CA: score=10.11 buy_ready=False sector_rank=18 price=32.45 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=4291267.5 spike=0.51
- ISMA.CA: score=18.56 buy_ready=False sector_rank=6 price=29.81 support=20.15 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=91.81 liquidity=58461676.0 spike=1.2
- ISMQ.CA: score=22.94 buy_ready=False sector_rank=18 price=7.98 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=76462256.0 spike=1.56
- ISPH.CA: score=23.4 buy_ready=False sector_rank=5 price=12.43 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=64.73 liquidity=53356028.0 spike=0.35
- JUFO.CA: score=23.32 buy_ready=False sector_rank=11 price=30.27 support=26.51 resistance=30.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=71.6 liquidity=56485648.0 spike=1.23
- KABO.CA: score=21.0 buy_ready=False sector_rank=8 price=6.3 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=11186977.0 spike=0.57
- KWIN.CA: score=24.6 buy_ready=False sector_rank=6 price=75.21 support=69.0 resistance=81.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=44.62 liquidity=10149062.0 spike=2.72
- KZPC.CA: score=11.95 buy_ready=False sector_rank=6 price=10.68 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=44.2 liquidity=2781090.25 spike=0.24
- LCSW.CA: score=14.4 buy_ready=False sector_rank=7 price=27.24 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=45.55 liquidity=5359331.5 spike=0.33
- LUTS.CA: score=21.16 buy_ready=False sector_rank=6 price=0.63 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=71.69 liquidity=11683539.0 spike=0.73
- MAAL.CA: score=26.04 buy_ready=False sector_rank=6 price=6.06 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16970926.0 spike=1.44
- MASR.CA: score=19.16 buy_ready=False sector_rank=6 price=6.92 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.48 liquidity=19202432.0 spike=0.33
- MBSC.CA: score=21.04 buy_ready=False sector_rank=7 price=274.93 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=51.41 liquidity=39429040.0 spike=0.8
- MCQE.CA: score=19.04 buy_ready=False sector_rank=7 price=188.93 support=188.01 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=52.24 liquidity=15179947.0 spike=0.8
- MCRO.CA: score=22.16 buy_ready=False sector_rank=6 price=1.27 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=14256324.0 spike=0.16
- MENA.CA: score=16.2 buy_ready=False sector_rank=4 price=6.81 support=5.76 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=60.26 liquidity=2800002.0 spike=0.17
- MEPA.CA: score=21.16 buy_ready=False sector_rank=6 price=1.73 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=13899011.0 spike=0.65
- MFPC.CA: score=9.82 buy_ready=False sector_rank=18 price=42.09 support=42.3 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=32921948.0 spike=0.34
- MFSC.CA: score=7.54 buy_ready=False sector_rank=6 price=46.92 support=33.01 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=25.62 liquidity=3380759.75 spike=0.22
- MHOT.CA: score=23.5 buy_ready=False sector_rank=2 price=30.98 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=20783410.0 spike=1.05
- MICH.CA: score=16.45 buy_ready=False sector_rank=6 price=36.74 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=60.8 liquidity=3288988.25 spike=0.37
- MILS.CA: score=17.25 buy_ready=False sector_rank=6 price=143.29 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=48.66 liquidity=6083559.0 spike=0.22
- MIPH.CA: score=10.57 buy_ready=False sector_rank=5 price=660.51 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=39.8 liquidity=1169811.5 spike=0.31
- MOED.CA: score=6.71 buy_ready=False sector_rank=6 price=0.69 support=0.68 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=18.28 liquidity=6547800.5 spike=0.49
- MOIL.CA: score=13.1 buy_ready=False sector_rank=9 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=61.43 liquidity=109958.83 spike=0.59
- MOIN.CA: score=11.59 buy_ready=False sector_rank=6 price=24.99 support=23.13 resistance=26.4 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=1429452.98 spike=0.8
- MOSC.CA: score=6.47 buy_ready=False sector_rank=6 price=265.7 support=268.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=20.91 liquidity=2301620.5 spike=0.17
- MPCI.CA: score=23.2 buy_ready=False sector_rank=6 price=229.62 support=192.01 resistance=233.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=68.01 liquidity=101571488.0 spike=1.02
- MPCO.CA: score=21.68 buy_ready=False sector_rank=10 price=1.81 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=91222576.0 spike=1.35
- MPRC.CA: score=18.85 buy_ready=False sector_rank=6 price=33.69 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=73.66 liquidity=7684857.5 spike=0.36
- MTIE.CA: score=16.94 buy_ready=False sector_rank=17 price=9.08 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=47.29 liquidity=8956779.0 spike=0.4
- NAHO.CA: score=5.17 buy_ready=False sector_rank=6 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=7798.24 spike=0.21
- NCCW.CA: score=11.16 buy_ready=False sector_rank=6 price=6.72 support=6.3 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90136576.0 spike=4.37
- NEDA.CA: score=11.49 buy_ready=False sector_rank=6 price=2.8 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=326233.59 spike=0.62
- NHPS.CA: score=15.98 buy_ready=False sector_rank=6 price=69.94 support=67.53 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=44.84 liquidity=4816621.0 spike=0.44
- NINH.CA: score=10.49 buy_ready=False sector_rank=6 price=17.89 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.55 liquidity=1329950.13 spike=0.11
- NIPH.CA: score=21.4 buy_ready=False sector_rank=5 price=168.0 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=86748072.0 spike=0.71
- OBRI.CA: score=11.16 buy_ready=False sector_rank=6 price=35.4 support=33.63 resistance=39.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=30.2 liquidity=10354036.0 spike=0.99
- OCDI.CA: score=16.4 buy_ready=False sector_rank=4 price=21.04 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=45.23 liquidity=22989572.0 spike=0.55
- OCPH.CA: score=9.29 buy_ready=False sector_rank=6 price=362.97 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=32.47 liquidity=5127448.5 spike=0.46
- ODIN.CA: score=17.14 buy_ready=False sector_rank=6 price=2.07 support=1.89 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=5977195.0 spike=0.59
- OFH.CA: score=23.16 buy_ready=False sector_rank=6 price=0.63 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=46.46 liquidity=17024350.0 spike=0.77
- OIH.CA: score=14.4 buy_ready=False sector_rank=1 price=1.4 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=29932610.0 spike=0.25
- OLFI.CA: score=17.35 buy_ready=False sector_rank=11 price=21.6 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=55.17 liquidity=8486792.0 spike=0.38
- ORAS.CA: score=4.6 buy_ready=False sector_rank=19 price=727.18 support=717.0 resistance=740.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125480056.0 spike=1.0
- ORHD.CA: score=19.4 buy_ready=False sector_rank=4 price=37.13 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=65.64 liquidity=145258064.0 spike=0.71
- ORWE.CA: score=21.0 buy_ready=False sector_rank=8 price=23.8 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=69.79 liquidity=24753282.0 spike=0.54
- PHAR.CA: score=17.35 buy_ready=False sector_rank=5 price=86.48 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=52.0 liquidity=7952300.5 spike=0.22
- PHDC.CA: score=19.4 buy_ready=False sector_rank=4 price=15.18 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=67.27 liquidity=322643840.0 spike=0.77
- PHTV.CA: score=13.61 buy_ready=False sector_rank=6 price=207.59 support=201.5 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:35 PM market time freshness=DELAYED_CURRENT RSI=42.92 liquidity=4441034.5 spike=0.3
- POUL.CA: score=18.29 buy_ready=False sector_rank=11 price=37.24 support=34.06 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=60.74 liquidity=7421609.5 spike=0.15
- PRCL.CA: score=25.02 buy_ready=False sector_rank=7 price=25.3 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=68.29 liquidity=71712352.0 spike=1.99
- PRDC.CA: score=15.71 buy_ready=False sector_rank=4 price=6.11 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=72.93 liquidity=4311246.0 spike=0.22
- PRMH.CA: score=18.16 buy_ready=False sector_rank=6 price=2.79 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=83.52 liquidity=12435712.0 spike=0.77
- RACC.CA: score=12.65 buy_ready=False sector_rank=6 price=9.89 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=55.19 liquidity=3488994.0 spike=0.15
- RAKT.CA: score=9.43 buy_ready=False sector_rank=6 price=23.79 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=54.9 liquidity=262070.65 spike=0.99
- RAYA.CA: score=22.4 buy_ready=False sector_rank=3 price=7.49 support=6.94 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=37125600.0 spike=0.32
- RMDA.CA: score=21.4 buy_ready=False sector_rank=5 price=5.27 support=4.91 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=41487936.0 spike=0.38
- ROTO.CA: score=24.74 buy_ready=False sector_rank=6 price=34.88 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=21740354.0 spike=1.79
- RREI.CA: score=21.16 buy_ready=False sector_rank=6 price=3.5 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=60.27 liquidity=15408530.0 spike=0.66
- RTVC.CA: score=19.51 buy_ready=False sector_rank=6 price=4.08 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.82 liquidity=6347558.5 spike=0.99
- RUBX.CA: score=15.52 buy_ready=False sector_rank=6 price=10.55 support=9.8 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=17.0 liquidity=24305582.0 spike=1.68
- SAUD.CA: score=14.62 buy_ready=False sector_rank=15 price=22.21 support=21.8 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=49.51 liquidity=6212492.5 spike=0.44
- SCEM.CA: score=14.12 buy_ready=False sector_rank=7 price=63.97 support=62.5 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=5079451.5 spike=0.12
- SCFM.CA: score=12.12 buy_ready=False sector_rank=6 price=258.75 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=25.91 liquidity=7955957.5 spike=0.28
- SCTS.CA: score=11.99 buy_ready=False sector_rank=14 price=625.38 support=590.01 resistance=709.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:34 PM market time freshness=DELAYED_CURRENT RSI=17.82 liquidity=8479142.0 spike=0.78
- SDTI.CA: score=23.16 buy_ready=False sector_rank=6 price=47.04 support=43.4 resistance=46.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=60.94 liquidity=16702355.0 spike=0.88
- SEIG.CA: score=19.87 buy_ready=False sector_rank=6 price=188.76 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=6421698.5 spike=1.14
- SIPC.CA: score=23.36 buy_ready=False sector_rank=6 price=3.66 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=59.09 liquidity=17003372.0 spike=1.1
- SKPC.CA: score=13.82 buy_ready=False sector_rank=18 price=17.26 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=35.68 liquidity=28312532.0 spike=0.4
- SMFR.CA: score=5.83 buy_ready=False sector_rank=6 price=207.17 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=30.74 liquidity=1662689.0 spike=0.22
- SNFC.CA: score=14.97 buy_ready=False sector_rank=6 price=12.05 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=5801502.0 spike=0.21
- SPIN.CA: score=7.44 buy_ready=False sector_rank=8 price=14.1 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=43.23 liquidity=1435839.5 spike=0.29
- SPMD.CA: score=23.16 buy_ready=False sector_rank=6 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=10621667.0 spike=0.42
- SUGR.CA: score=17.41 buy_ready=False sector_rank=11 price=49.74 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=37.22 liquidity=4546477.0 spike=0.28
- SVCE.CA: score=19.16 buy_ready=False sector_rank=6 price=8.73 support=8.33 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=36.44 liquidity=22770788.0 spike=0.18
- SWDY.CA: score=16.0 buy_ready=False sector_rank=13 price=87.57 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=7361444.0 spike=0.21
- TALM.CA: score=20.51 buy_ready=False sector_rank=14 price=15.97 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=51.08 liquidity=11978333.0 spike=0.92
- TMGH.CA: score=21.4 buy_ready=False sector_rank=4 price=96.49 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=60.15 liquidity=234214480.0 spike=0.45
- TRTO.CA: score=7.16 buy_ready=False sector_rank=6 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=211.38 spike=0.44
- UEFM.CA: score=5.53 buy_ready=False sector_rank=6 price=474.61 support=455.6 resistance=505.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=36.58 liquidity=367310.81 spike=0.22
- UEGC.CA: score=21.16 buy_ready=False sector_rank=6 price=1.44 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=21571834.0 spike=0.88
- UNIP.CA: score=20.16 buy_ready=False sector_rank=6 price=0.32 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=67.69 liquidity=13414290.0 spike=0.85
- UNIT.CA: score=19.09 buy_ready=False sector_rank=4 price=14.18 support=10.89 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=65.67 liquidity=7691334.0 spike=0.73
- WCDF.CA: score=4.91 buy_ready=False sector_rank=6 price=539.17 support=535.0 resistance=559.0 source=Yahoo Finance as_of=2026-06-07T21:00:00+00:00 freshness=FRESH RSI=13.84 liquidity=370948.95 spike=1.19
- WKOL.CA: score=18.22 buy_ready=False sector_rank=6 price=303.39 support=290.0 resistance=339.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=12710350.0 spike=2.03
- ZEOT.CA: score=17.78 buy_ready=False sector_rank=6 price=9.26 support=8.43 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=58.16 liquidity=4619799.0 spike=0.64
- ZMID.CA: score=25.26 buy_ready=False sector_rank=4 price=6.43 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=57.94 liquidity=402742944.0 spike=1.93

## Backtesting Lite
- CCAP.CA: 180d return=118.82%, max drawdown=-25.0%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- MAAL.CA: 180d return=38.05%, max drawdown=-27.25%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- CERA.CA: 180d return=-36.84%, max drawdown=-46.32%, MA20>MA50 days last20=20, as_of=2026-06-07T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- MAAL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Marseille Almasreia Alkhalegeya For Holding Investment SAE summary=Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- CERA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=The Arab Ceramic Co. summary=Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=524 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- ASPI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Aspire Capital Holding for Financial Investments summary=Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25; PREDCO, Aspire Holding consider establishing mortgage company; Pioneers Holding gets EGX&#39;s approval for capital cut, name change
  - Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25: https://english.mubasher.info/news/4541324/Aspire-Capital-records-higher-consolidated-net-profits-at-over-EGP-42m-in-9M-25/
  - PREDCO, Aspire Holding consider establishing mortgage company: https://english.mubasher.info/news/4185438/PREDCO-Aspire-Holding-consider-establishing-mortgage-company/
  - Pioneers Holding gets EGX&#39;s approval for capital cut, name change: https://english.mubasher.info/news/3861454/Pioneers-Holding-gets-EGX-s-approval-for-capital-cut-name-change/
- PRCL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ceramic and Porcelain summary=Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- ROTO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Rowad Tourism Company summary=Shareholder raises stake in Rowad Tourism; Target raises stake in Rowad Tourism to 10.68%; Rowad Tourism sees EGP 22.4m block trading deal
  - Shareholder raises stake in Rowad Tourism: https://english.mubasher.info/news/4043645/Shareholder-raises-stake-in-Rowad-Tourism/
  - Target raises stake in Rowad Tourism to 10.68%: https://english.mubasher.info/news/4031744/Target-raises-stake-in-Rowad-Tourism-to-10-68-/
  - Rowad Tourism sees EGP 22.4m block trading deal: https://english.mubasher.info/news/4031133/Rowad-Tourism-sees-EGP-22-4m-block-trading-deal/

## Warnings
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence rejected for CERA.CA: source text did not clearly match CERA.CA / The Arab Ceramic Co..
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence for ROTO.CA matches the company but no source/report date was detected.
