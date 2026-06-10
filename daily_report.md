# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-06-10T16:16:06.649108+00:00
Generated Cairo: 2026-06-10 19:16
Run timing: target 15:30 Cairo | generated Cairo 2026-06-10 19:16 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-06-10 19:13

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 177/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, June 10
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.0% / above MA50 40.0%
- EGX70 regime: BEARISH / above MA20 35.14% / above MA50 78.38%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=1197311232.0 spike=1.42 score=5.39
- COMI.CA: liquidity=555350080.0 spike=0.82 score=15.14
- ELSH.CA: liquidity=514690304.0 spike=3.91 score=11.93
- ORAS.CA: liquidity=455092576.0 spike=1.0 score=4.6
- FWRY.CA: liquidity=369707168.0 spike=1.24 score=13.29

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The EGX30 and EGX70 indices are both in a bearish regime, with weak breadth (≈19%) and negative short‑term returns. Consequently the scanner is in DEFENSIVE_NO_NEW_BUY mode, so no BUY signals are issued despite several tickets showing bullish watch outlooks.
- Liquidity is adequate (spikes up to 11×) but momentum is extended, keeping risk flags high.
- Key support levels sit 4‑9% below current prices; resistance is within 1‑7%, limiting upside in the next 1‑3 days.
- Sector breadth is low; Real Estate and General/Verified EGX Expansion lead but remain under pressure.
- Market regime shift to defensive mode raises uncertainty; any new entry should wait for broader index recovery.

## Top Liquidity Spikes
- MICH.CA: spike=11.09 liquidity=99037672.0 outlook=BULLISH_WATCH score=73.82 buy_ready=False
- CFGH.CA: spike=5.7 liquidity=29522.0 outlook=WEAK_OR_RISKY score=1.82 buy_ready=False
- ADCI.CA: spike=4.88 liquidity=29442062.0 outlook=BULLISH_WATCH score=95.82 buy_ready=False
- ANFI.CA: spike=4.65 liquidity=134592218.23 outlook=BULLISH_WATCH score=77.82 buy_ready=False
- LUTS.CA: spike=4.03 liquidity=66183484.0 outlook=BULLISH_WATCH score=93.82 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=6.45 5d=2.17% 20d=-2.47% aboveMA50=100.0%
- #2 Real Estate: score=5.32 5d=-1.18% 20d=4.07% aboveMA50=69.23%
- #3 General / Verified EGX Expansion: score=4.82 5d=0.88% 20d=0.0% aboveMA50=71.15%
- #4 Textiles: score=4.73 5d=-0.81% 20d=5.88% aboveMA50=75.0%
- #5 Healthcare: score=4.42 5d=1.46% 20d=-1.7% aboveMA50=100.0%
- #6 Food, Beverages & Tobacco: score=4.28 5d=-0.66% 20d=1.51% aboveMA50=85.71%
- #7 Tourism & Leisure: score=4.11 5d=-5.99% 20d=14.85% aboveMA50=100.0%
- #8 Building Materials: score=3.96 5d=-1.06% 20d=1.38% aboveMA50=83.33%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KZPC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ORHD.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- ALUM.CA: BULLISH_WATCH score=98.82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=96.32 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- ADCI.CA: BULLISH_WATCH score=95.82 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended; close to resistance
- EEII.CA: BULLISH_WATCH score=95.82 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- RTVC.CA: BULLISH_WATCH score=95.82 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- GGCC.CA: BULLISH_WATCH score=94.82 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- ELKA.CA: BULLISH_WATCH score=94.82 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended
- LUTS.CA: BULLISH_WATCH score=93.82 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=7.05 buy_ready=False sector_rank=3 price=200.18 support=200.0 resistance=224.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11703323.0 spike=1.06
- ABUK.CA: score=9.56 buy_ready=False sector_rank=16 price=79.51 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.35 liquidity=77630872.0 spike=0.64
- ACAMD.CA: score=24.41 buy_ready=False sector_rank=3 price=2.24 support=2.1 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.65 liquidity=261797392.0 spike=2.24
- ACGC.CA: score=18.89 buy_ready=False sector_rank=4 price=9.56 support=8.51 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.21 liquidity=35244128.0 spike=0.61
- ADCI.CA: score=26.93 buy_ready=False sector_rank=3 price=221.23 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=29442062.0 spike=4.88
- ADIB.CA: score=15.14 buy_ready=False sector_rank=11 price=44.88 support=45.3 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.08 liquidity=101852792.0 spike=0.64
- ADPC.CA: score=11.93 buy_ready=False sector_rank=3 price=3.6 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.74 liquidity=10827032.0 spike=0.43
- AFDI.CA: score=21.93 buy_ready=False sector_rank=3 price=42.56 support=40.0 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.36 liquidity=13356949.0 spike=0.73
- AFMC.CA: score=12.99 buy_ready=False sector_rank=3 price=70.53 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.89 liquidity=3060623.5 spike=0.34
- AJWA.CA: score=22.33 buy_ready=False sector_rank=3 price=148.09 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=84.58 liquidity=29204024.0 spike=1.7
- ALCN.CA: score=14.54 buy_ready=False sector_rank=18 price=28.24 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.99 liquidity=16555199.0 spike=0.77
- ALUM.CA: score=25.93 buy_ready=False sector_rank=3 price=24.47 support=22.66 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.44 liquidity=11557955.0 spike=0.54
- AMER.CA: score=8.13 buy_ready=False sector_rank=2 price=2.6 support=2.58 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98437568.0 spike=0.86
- AMES.CA: score=9.68 buy_ready=False sector_rank=3 price=49.85 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.46 liquidity=4747571.0 spike=0.81
- AMIA.CA: score=21.68 buy_ready=False sector_rank=3 price=8.93 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=9753709.0 spike=0.35
- AMOC.CA: score=10.38 buy_ready=False sector_rank=10 price=8.11 support=8.1 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=46626756.0 spike=0.57
- ANFI.CA: score=25.93 buy_ready=False sector_rank=3 price=18.62 support=13.5 resistance=18.62 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=79.32 liquidity=134592218.23 spike=4.65
- APSW.CA: score=5.97 buy_ready=False sector_rank=3 price=8.63 support=8.62 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.21 liquidity=1341995.63 spike=1.35
- ARAB.CA: score=19.73 buy_ready=False sector_rank=2 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=177068816.0 spike=2.3
- ARCC.CA: score=18.58 buy_ready=False sector_rank=8 price=55.91 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=40520988.0 spike=0.95
- AREH.CA: score=20.93 buy_ready=False sector_rank=3 price=1.47 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=80.65 liquidity=20795318.0 spike=0.74
- ARVA.CA: score=21.93 buy_ready=False sector_rank=3 price=10.99 support=7.71 resistance=11.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.61 liquidity=18283248.0 spike=0.73
- ASCM.CA: score=19.31 buy_ready=False sector_rank=3 price=55.13 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.73 liquidity=81080736.0 spike=1.19
- ASPI.CA: score=6.93 buy_ready=False sector_rank=3 price=0.33 support=0.33 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=53174796.0 spike=0.85
- ATLC.CA: score=10.62 buy_ready=False sector_rank=19 price=4.84 support=4.71 resistance=5.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.04 liquidity=3232372.0 spike=0.5
- ATQA.CA: score=15.56 buy_ready=False sector_rank=16 price=9.56 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=32114496.0 spike=0.79
- AXPH.CA: score=11.04 buy_ready=False sector_rank=3 price=1131.19 support=1100.12 resistance=1239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=1113349.63 spike=0.2
- BINV.CA: score=12.65 buy_ready=False sector_rank=17 price=45.98 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.75 liquidity=3101701.75 spike=0.26
- BIOC.CA: score=14.03 buy_ready=False sector_rank=3 price=70.39 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=4098421.0 spike=0.64
- BTFH.CA: score=16.38 buy_ready=False sector_rank=19 price=3.04 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=109895944.0 spike=0.46
- CAED.CA: score=7.71 buy_ready=False sector_rank=3 price=70.7 support=70.41 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=2780320.5 spike=0.18
- CANA.CA: score=17.52 buy_ready=False sector_rank=11 price=36.22 support=34.01 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.43 liquidity=17062832.0 spike=1.19
- CCAP.CA: score=5.39 buy_ready=False sector_rank=17 price=5.14 support=5.13 resistance=5.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1197311232.0 spike=1.42
- CCRS.CA: score=21.93 buy_ready=False sector_rank=3 price=2.4 support=2.1 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=10295662.0 spike=0.37
- CEFM.CA: score=5.92 buy_ready=False sector_rank=3 price=105.16 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=996177.63 spike=0.21
- CERA.CA: score=24.93 buy_ready=False sector_rank=3 price=1.18 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=10191966.0 spike=0.68
- CFGH.CA: score=5.96 buy_ready=False sector_rank=3 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=29522.0 spike=5.7
- CICH.CA: score=1.6 buy_ready=False sector_rank=19 price=11.6 support=11.71 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=2211237.75 spike=0.48
- CIEB.CA: score=21.64 buy_ready=False sector_rank=11 price=23.63 support=23.31 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.39 liquidity=17670642.0 spike=1.75
- CIRA.CA: score=16.28 buy_ready=False sector_rank=9 price=25.91 support=23.23 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.54 liquidity=7695824.5 spike=0.26
- CLHO.CA: score=13.77 buy_ready=False sector_rank=5 price=14.91 support=14.83 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=10543679.0 spike=0.3
- CNFN.CA: score=16.38 buy_ready=False sector_rank=19 price=4.43 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=12848022.0 spike=0.75
- COMI.CA: score=15.14 buy_ready=False sector_rank=11 price=131.09 support=129.8 resistance=144.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.51 liquidity=555350080.0 spike=0.82
- COPR.CA: score=20.37 buy_ready=False sector_rank=3 price=0.36 support=0.32 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.35 liquidity=66514192.0 spike=1.72
- COSG.CA: score=25.25 buy_ready=False sector_rank=3 price=1.64 support=1.46 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=101312776.0 spike=1.66
- CPCI.CA: score=10.45 buy_ready=False sector_rank=3 price=361.55 support=340.01 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=82.12 liquidity=3524489.75 spike=0.79
- CSAG.CA: score=17.54 buy_ready=False sector_rank=18 price=30.97 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.85 liquidity=14958947.0 spike=0.81
- DAPH.CA: score=9.6 buy_ready=False sector_rank=3 price=78.83 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.1 liquidity=7668214.0 spike=0.25
- DEIN.CA: score=7.93 buy_ready=False sector_rank=3 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=8.12 buy_ready=False sector_rank=6 price=24.05 support=24.24 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=5112336.0 spike=2.15
- DSCW.CA: score=17.93 buy_ready=False sector_rank=3 price=1.77 support=1.71 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=33342460.0 spike=0.55
- DTPP.CA: score=4.74 buy_ready=False sector_rank=3 price=120.3 support=123.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=2816978.0 spike=0.73
- EALR.CA: score=12.79 buy_ready=False sector_rank=3 price=356.73 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.06 liquidity=2863851.25 spike=0.3
- EASB.CA: score=11.39 buy_ready=False sector_rank=3 price=4.96 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.58 liquidity=1344525.38 spike=1.06
- EAST.CA: score=18.43 buy_ready=False sector_rank=6 price=38.39 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=7720732.0 spike=0.11
- EBSC.CA: score=14.79 buy_ready=False sector_rank=3 price=1.82 support=1.64 resistance=2.09 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=62.79 liquidity=862683.66 spike=0.35
- ECAP.CA: score=22.44 buy_ready=False sector_rank=3 price=31.09 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=88.3 liquidity=9810857.0 spike=1.85
- EDFM.CA: score=10.42 buy_ready=False sector_rank=3 price=334.11 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=38.06 liquidity=494012.97 spike=0.54
- EEII.CA: score=24.03 buy_ready=False sector_rank=3 price=2.39 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=20676724.0 spike=1.05
- EFIC.CA: score=0.23 buy_ready=False sector_rank=16 price=204.33 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=7.01 liquidity=1666096.25 spike=0.41
- EFID.CA: score=18.71 buy_ready=False sector_rank=6 price=27.8 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=41834092.0 spike=0.54
- EFIH.CA: score=12.81 buy_ready=False sector_rank=21 price=20.8 support=21.0 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=34684520.0 spike=0.54
- EGAL.CA: score=14.56 buy_ready=False sector_rank=16 price=310.93 support=304.0 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.47 liquidity=81983248.0 spike=0.74
- EGAS.CA: score=16.03 buy_ready=False sector_rank=10 price=49.96 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.63 liquidity=5652386.0 spike=0.42
- EGBE.CA: score=8.24 buy_ready=False sector_rank=11 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.52 liquidity=100033.25 spike=0.72
- EGCH.CA: score=19.56 buy_ready=False sector_rank=16 price=14.1 support=12.95 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.7 liquidity=42146824.0 spike=0.36
- EGSA.CA: score=8.87 buy_ready=False sector_rank=12 price=8.6 support=8.3 resistance=9.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=67.78 liquidity=36452.69 spike=2.43
- EGTS.CA: score=8.13 buy_ready=False sector_rank=2 price=18.38 support=18.21 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=96035496.0 spike=0.83
- EHDR.CA: score=8.21 buy_ready=False sector_rank=3 price=2.65 support=2.61 resistance=2.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=82759656.0 spike=1.64
- EKHO.CA: score=10.38 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=15.78 buy_ready=False sector_rank=13 price=2.13 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=15013953.0 spike=0.54
- ELKA.CA: score=21.95 buy_ready=False sector_rank=3 price=1.25 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=63051900.0 spike=1.51
- ELNA.CA: score=18.26 buy_ready=False sector_rank=3 price=41.26 support=37.11 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=1332774.25 spike=3.71
- ELSH.CA: score=11.93 buy_ready=False sector_rank=3 price=14.04 support=13.03 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=514690304.0 spike=3.91
- ELWA.CA: score=13.06 buy_ready=False sector_rank=3 price=2.13 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=91.67 liquidity=2133145.5 spike=0.7
- EMFD.CA: score=20.13 buy_ready=False sector_rank=2 price=11.55 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.07 liquidity=233770832.0 spike=0.97
- ENGC.CA: score=23.71 buy_ready=False sector_rank=3 price=34.31 support=32.31 resistance=35.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.72 liquidity=24820438.0 spike=1.89
- EOSB.CA: score=12.32 buy_ready=False sector_rank=3 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=253701.45 spike=2.07
- EPCO.CA: score=16.1 buy_ready=False sector_rank=3 price=9.0 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.31 liquidity=7171315.0 spike=0.57
- EPPK.CA: score=7.3 buy_ready=False sector_rank=3 price=12.17 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.1 liquidity=367715.03 spike=0.31
- ETEL.CA: score=14.98 buy_ready=False sector_rank=12 price=92.59 support=92.17 resistance=99.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=53913464.0 spike=0.49
- ETRS.CA: score=22.51 buy_ready=False sector_rank=3 price=9.27 support=7.37 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=71891328.0 spike=1.29
- EXPA.CA: score=18.14 buy_ready=False sector_rank=11 price=18.63 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=23951294.0 spike=0.6
- FAIT.CA: score=4.86 buy_ready=False sector_rank=11 price=35.95 support=34.11 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=1718651.0 spike=0.26
- FAITA.CA: score=8.16 buy_ready=False sector_rank=11 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=58.82 liquidity=17939.61 spike=0.4
- FERC.CA: score=8.42 buy_ready=False sector_rank=16 price=76.88 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.33 liquidity=3859907.25 spike=0.62
- FWRY.CA: score=13.29 buy_ready=False sector_rank=21 price=18.09 support=18.32 resistance=21.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=369707168.0 spike=1.24
- GBCO.CA: score=25.32 buy_ready=False sector_rank=1 price=27.62 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=182063392.0 spike=1.46
- GDWA.CA: score=22.53 buy_ready=False sector_rank=3 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=16971416.0 spike=1.8
- GGCC.CA: score=23.17 buy_ready=False sector_rank=3 price=0.42 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=14963678.0 spike=2.12
- GIHD.CA: score=14.14 buy_ready=False sector_rank=3 price=40.01 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=50.23 liquidity=3215067.0 spike=0.59
- GMCI.CA: score=9.23 buy_ready=False sector_rank=3 price=1.73 support=1.67 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=305239.03 spike=0.76
- GRCA.CA: score=4.35 buy_ready=False sector_rank=3 price=52.2 support=53.16 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=2426271.5 spike=0.27
- GSSC.CA: score=6.89 buy_ready=False sector_rank=3 price=249.27 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=9.47 liquidity=4961173.5 spike=0.67
- GTWL.CA: score=14.89 buy_ready=False sector_rank=3 price=47.61 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.28 liquidity=17192628.0 spike=2.48
- HDBK.CA: score=15.14 buy_ready=False sector_rank=11 price=139.07 support=138.75 resistance=149.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.01 liquidity=10147102.0 spike=0.66
- HELI.CA: score=21.39 buy_ready=False sector_rank=2 price=6.47 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.55 liquidity=188451744.0 spike=1.13
- HRHO.CA: score=13.38 buy_ready=False sector_rank=19 price=26.16 support=26.05 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.48 liquidity=114254424.0 spike=0.61
- ICID.CA: score=7.41 buy_ready=False sector_rank=3 price=6.53 support=6.45 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17859578.0 spike=1.24
- IDRE.CA: score=19.42 buy_ready=False sector_rank=3 price=43.54 support=39.8 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=9494413.0 spike=0.28
- IFAP.CA: score=6.84 buy_ready=False sector_rank=20 price=19.31 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=4089892.25 spike=0.32
- INFI.CA: score=18.07 buy_ready=False sector_rank=3 price=98.24 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=9139855.0 spike=0.57
- IRON.CA: score=15.68 buy_ready=False sector_rank=16 price=32.1 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=9655915.0 spike=1.23
- ISMA.CA: score=20.93 buy_ready=False sector_rank=3 price=29.56 support=20.66 resistance=30.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=92.96 liquidity=16829460.0 spike=0.34
- ISMQ.CA: score=25.66 buy_ready=False sector_rank=16 price=7.89 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=155400736.0 spike=3.05
- ISPH.CA: score=22.77 buy_ready=False sector_rank=5 price=11.96 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=63.98 liquidity=87458904.0 spike=0.57
- JUFO.CA: score=19.71 buy_ready=False sector_rank=6 price=29.49 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.46 liquidity=24364468.0 spike=0.5
- KABO.CA: score=18.97 buy_ready=False sector_rank=4 price=6.2 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=72.34 liquidity=20811734.0 spike=1.04
- KWIN.CA: score=24.41 buy_ready=False sector_rank=3 price=71.92 support=69.0 resistance=80.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=12580388.0 spike=3.24
- KZPC.CA: score=26.93 buy_ready=False sector_rank=3 price=10.71 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=40557248.0 spike=3.51
- LCSW.CA: score=15.86 buy_ready=False sector_rank=8 price=26.42 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=7272708.0 spike=0.46
- LUTS.CA: score=26.93 buy_ready=False sector_rank=3 price=0.64 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=68.55 liquidity=66183484.0 spike=4.03
- MAAL.CA: score=26.49 buy_ready=False sector_rank=3 price=5.89 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16405325.0 spike=1.28
- MASR.CA: score=24.93 buy_ready=False sector_rank=3 price=6.88 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=205489872.0 spike=3.54
- MBSC.CA: score=18.58 buy_ready=False sector_rank=8 price=270.98 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.97 liquidity=30834908.0 spike=0.63
- MCQE.CA: score=16.44 buy_ready=False sector_rank=8 price=180.0 support=185.59 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.13 liquidity=27399060.0 spike=1.43
- MCRO.CA: score=17.93 buy_ready=False sector_rank=3 price=1.23 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=45497428.0 spike=0.53
- MENA.CA: score=25.13 buy_ready=False sector_rank=2 price=6.81 support=5.8 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=13765879.0 spike=0.86
- MEPA.CA: score=21.93 buy_ready=False sector_rank=3 price=1.68 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=12212350.0 spike=0.64
- MFPC.CA: score=9.56 buy_ready=False sector_rank=16 price=41.22 support=42.01 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.62 liquidity=52308976.0 spike=0.61
- MFSC.CA: score=2.09 buy_ready=False sector_rank=3 price=44.0 support=43.0 resistance=47.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5165510.0 spike=0.34
- MHOT.CA: score=16.1 buy_ready=False sector_rank=7 price=30.01 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.18 liquidity=7459457.5 spike=0.36
- MICH.CA: score=26.93 buy_ready=False sector_rank=3 price=37.79 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.61 liquidity=99037672.0 spike=11.09
- MILS.CA: score=17.34 buy_ready=False sector_rank=3 price=138.55 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=70.06 liquidity=5407043.5 spike=0.24
- MIPH.CA: score=11.27 buy_ready=False sector_rank=5 price=658.09 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.51 liquidity=2501991.0 spike=0.79
- MOED.CA: score=10.93 buy_ready=False sector_rank=3 price=0.68 support=0.68 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=11460174.0 spike=0.87
- MOIL.CA: score=12.52 buy_ready=False sector_rank=10 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=145459.53 spike=0.77
- MOIN.CA: score=9.58 buy_ready=False sector_rank=3 price=25.01 support=24.02 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.2 liquidity=656316.88 spike=0.33
- MOSC.CA: score=6.88 buy_ready=False sector_rank=3 price=258.99 support=264.0 resistance=320.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.23 liquidity=1949557.5 spike=0.15
- MPCI.CA: score=23.93 buy_ready=False sector_rank=3 price=221.16 support=193.8 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=68.96 liquidity=60067636.0 spike=0.67
- MPCO.CA: score=3.75 buy_ready=False sector_rank=20 price=1.7 support=1.7 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54744244.0 spike=0.76
- MPRC.CA: score=24.07 buy_ready=False sector_rank=3 price=32.42 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.93 liquidity=23386690.0 spike=1.07
- MTIE.CA: score=22.4 buy_ready=False sector_rank=1 price=8.89 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.87 liquidity=13356049.0 spike=0.64
- NAHO.CA: score=6.17 buy_ready=False sector_rank=3 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=40542.42 spike=1.1
- NCCW.CA: score=22.29 buy_ready=False sector_rank=3 price=6.41 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=82.23 liquidity=41340936.0 spike=1.68
- NEDA.CA: score=12.29 buy_ready=False sector_rank=3 price=2.79 support=2.65 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:49 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=358087.06 spike=0.53
- NHPS.CA: score=9.19 buy_ready=False sector_rank=3 price=67.72 support=67.53 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.68 liquidity=3261029.0 spike=0.3
- NINH.CA: score=7.3 buy_ready=False sector_rank=3 price=17.13 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.42 liquidity=2369226.75 spike=0.24
- NIPH.CA: score=18.77 buy_ready=False sector_rank=5 price=162.9 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.17 liquidity=56255376.0 spike=0.49
- OBRI.CA: score=22.69 buy_ready=False sector_rank=3 price=34.9 support=33.63 resistance=39.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.8 liquidity=32639102.0 spike=2.88
- OCDI.CA: score=18.13 buy_ready=False sector_rank=2 price=20.67 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.38 liquidity=31277994.0 spike=0.73
- OCPH.CA: score=14.68 buy_ready=False sector_rank=3 price=350.66 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=4756036.5 spike=0.5
- ODIN.CA: score=21.57 buy_ready=False sector_rank=3 price=2.08 support=1.89 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=79.07 liquidity=14010464.0 spike=1.32
- OFH.CA: score=19.01 buy_ready=False sector_rank=3 price=0.61 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=23040336.0 spike=1.04
- OIH.CA: score=9.55 buy_ready=False sector_rank=17 price=1.36 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=47712448.0 spike=0.41
- OLFI.CA: score=22.09 buy_ready=False sector_rank=6 price=21.8 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.66 liquidity=35270760.0 spike=1.69
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=733.91 support=722.0 resistance=763.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=455092576.0 spike=1.0
- ORHD.CA: score=24.21 buy_ready=False sector_rank=2 price=36.65 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.47 liquidity=316715392.0 spike=1.54
- ORWE.CA: score=20.89 buy_ready=False sector_rank=4 price=23.16 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.17 liquidity=25757586.0 spike=0.56
- PHAR.CA: score=18.77 buy_ready=False sector_rank=5 price=86.0 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=14274838.0 spike=0.42
- PHDC.CA: score=21.13 buy_ready=False sector_rank=2 price=14.8 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.12 liquidity=213735552.0 spike=0.51
- PHTV.CA: score=16.38 buy_ready=False sector_rank=3 price=204.82 support=203.25 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.33 liquidity=6447084.0 spike=0.43
- POUL.CA: score=18.71 buy_ready=False sector_rank=6 price=36.0 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=18617806.0 spike=0.39
- PRCL.CA: score=22.58 buy_ready=False sector_rank=8 price=24.51 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=14357124.0 spike=0.41
- PRDC.CA: score=20.47 buy_ready=False sector_rank=2 price=6.09 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=76.3 liquidity=22892974.0 spike=1.17
- PRMH.CA: score=18.93 buy_ready=False sector_rank=3 price=2.64 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.53 liquidity=12986269.0 spike=0.86
- RACC.CA: score=17.79 buy_ready=False sector_rank=3 price=9.63 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=7862365.0 spike=0.42
- RAKT.CA: score=10.25 buy_ready=False sector_rank=3 price=23.11 support=22.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=563394.69 spike=1.88
- RAYA.CA: score=4.76 buy_ready=False sector_rank=14 price=6.96 support=6.9 resistance=7.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120374128.0 spike=1.06
- RMDA.CA: score=20.77 buy_ready=False sector_rank=5 price=5.08 support=4.95 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=33020534.0 spike=0.3
- ROTO.CA: score=22.81 buy_ready=False sector_rank=3 price=33.6 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.72 liquidity=8881097.0 spike=0.69
- RREI.CA: score=16.93 buy_ready=False sector_rank=3 price=3.42 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=14634048.0 spike=0.62
- RTVC.CA: score=20.1 buy_ready=False sector_rank=3 price=3.91 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=6176283.5 spike=0.92
- RUBX.CA: score=9.11 buy_ready=False sector_rank=3 price=10.12 support=9.8 resistance=11.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.96 liquidity=8178065.0 spike=0.55
- SAUD.CA: score=15.28 buy_ready=False sector_rank=11 price=21.43 support=21.8 resistance=24.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.58 liquidity=14725116.0 spike=1.07
- SCEM.CA: score=18.58 buy_ready=False sector_rank=8 price=62.18 support=62.5 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=33323044.0 spike=0.85
- SCFM.CA: score=8.78 buy_ready=False sector_rank=3 price=255.5 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.8 liquidity=3851465.75 spike=0.18
- SCTS.CA: score=8.18 buy_ready=False sector_rank=9 price=610.21 support=590.01 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.16 liquidity=4593378.0 spike=0.42
- SDTI.CA: score=23.93 buy_ready=False sector_rank=3 price=46.52 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.43 liquidity=12310732.0 spike=0.63
- SEIG.CA: score=14.64 buy_ready=False sector_rank=3 price=182.99 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.11 liquidity=2712866.25 spike=0.5
- SIPC.CA: score=22.47 buy_ready=False sector_rank=3 price=3.56 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=19753266.0 spike=1.27
- SKPC.CA: score=13.56 buy_ready=False sector_rank=16 price=16.97 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.27 liquidity=37474988.0 spike=0.55
- SMFR.CA: score=14.45 buy_ready=False sector_rank=3 price=201.06 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=4520972.5 spike=0.75
- SNFC.CA: score=19.93 buy_ready=False sector_rank=3 price=12.12 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=17728638.0 spike=0.66
- SPIN.CA: score=3.55 buy_ready=False sector_rank=4 price=13.8 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.93 liquidity=2654617.75 spike=0.53
- SPMD.CA: score=21.93 buy_ready=False sector_rank=3 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.42 liquidity=10624708.0 spike=0.42
- SUGR.CA: score=17.69 buy_ready=False sector_rank=6 price=49.25 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.71 liquidity=8981112.0 spike=0.56
- SVCE.CA: score=14.93 buy_ready=False sector_rank=3 price=8.45 support=8.33 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.71 liquidity=28047462.0 spike=0.24
- SWDY.CA: score=17.78 buy_ready=False sector_rank=13 price=86.21 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=17923540.0 spike=0.52
- TALM.CA: score=22.51 buy_ready=False sector_rank=9 price=15.95 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.64 liquidity=9922275.0 spike=0.74
- TMGH.CA: score=16.13 buy_ready=False sector_rank=2 price=94.21 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.65 liquidity=255510592.0 spike=0.51
- TRTO.CA: score=7.93 buy_ready=False sector_rank=3 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=189.24 spike=0.4
- UEFM.CA: score=1.5 buy_ready=False sector_rank=3 price=473.85 support=455.6 resistance=504.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=33.63 liquidity=567872.25 spike=0.41
- UEGC.CA: score=23.67 buy_ready=False sector_rank=3 price=1.4 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=47792292.0 spike=1.87
- UNIP.CA: score=25.93 buy_ready=False sector_rank=3 price=0.32 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=59380480.0 spike=3.64
- UNIT.CA: score=22.3 buy_ready=False sector_rank=2 price=13.85 support=11.28 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.32 liquidity=9167237.0 spike=0.86
- WCDF.CA: score=5.75 buy_ready=False sector_rank=3 price=539.84 support=535.0 resistance=558.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=25.38 liquidity=577913.94 spike=1.12
- WKOL.CA: score=14.32 buy_ready=False sector_rank=3 price=297.99 support=290.0 resistance=324.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.9 liquidity=4390590.0 spike=0.7
- ZEOT.CA: score=1.9 buy_ready=False sector_rank=3 price=8.69 support=8.41 resistance=9.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4968252.0 spike=0.71
- ZMID.CA: score=27.13 buy_ready=False sector_rank=2 price=6.15 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.11 liquidity=213343776.0 spike=0.94

## Backtesting Lite
- ZMID.CA: 180d return=62.61%, max drawdown=-19.84%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- ADCI.CA: 180d return=34.64%, max drawdown=-38.87%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- KZPC.CA: 180d return=1.16%, max drawdown=-19.97%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=525 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- ADCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=The Arab Drug Company summary=ADCO’s net profits after tax cross EGP 182.5m in 8M-25/26; Arab Drug unveils cash dividends for FY22/23; Arab Drug’s OGM approves FY21/22 dividends
  - ADCO’s net profits after tax cross EGP 182.5m in 8M-25/26: https://english.mubasher.info/news/4587961/ADCO-s-net-profits-after-tax-cross-EGP-182-5m-in-8M-25-26/
  - Arab Drug unveils cash dividends for FY22/23: https://english.mubasher.info/news/4193946/Arab-Drug-unveils-cash-dividends-for-FY22-23/
  - Arab Drug’s OGM approves FY21/22 dividends: https://english.mubasher.info/news/4022664/Arab-Drug-s-OGM-approves-FY21-22-dividends/
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=891 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- LUTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lotus Agri Capital summary=Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- MICH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Chemical Industries Co. summary=Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26; Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis; Misr Chemical Industries posts 10% decrease in H1-25/26 net profits
  - Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26: https://english.mubasher.info/news/4597505/Misr-Chemical-Industries-net-profits-decline-to-EGP-397m-in-9M-25-26/
  - Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis: https://english.mubasher.info/news/4586207/Surpassing-Misr-Chemical-stock-s-current-levels-would-lead-to-historical-levels-Analysis/
  - Misr Chemical Industries posts 10% decrease in H1-25/26 net profits: https://english.mubasher.info/news/4554378/Misr-Chemical-Industries-posts-10-decrease-in-H1-25-26-net-profits/
- MAAL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Marseille Almasreia Alkhalegeya For Holding Investment SAE summary=Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- ALUM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Aluminum Company (S.A.E) summary=Arab Aluminum’s stock holds steady as bullish pattern breaks; Arab Aluminum profits rise 7% in H1-17; Arab Aluminum OGM approves EGP 1/shr dividends
  - Arab Aluminum’s stock holds steady as bullish pattern breaks: https://english.mubasher.info/news/4564438/Arab-Aluminum-s-stock-holds-steady-as-bullish-pattern-breaks/
  - Arab Aluminum profits rise 7% in H1-17: https://english.mubasher.info/news/3144589/Arab-Aluminum-profits-rise-7-in-H1-17/
  - Arab Aluminum OGM approves EGP 1/shr dividends: https://english.mubasher.info/news/3076498/Arab-Aluminum-OGM-approves-EGP-1-shr-dividends/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.

## Warnings
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ADCI.CA matches the company but no source/report date was detected.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Mubasher stock page returned no evidence titles for LUTS.CA.
- No Yahoo or Mubasher evidence found for LUTS.CA.
- Evidence rejected for LUTS.CA: source text did not clearly match LUTS.CA / Lotus Agri Capital.
- Evidence for MICH.CA matches the company but no source/report date was detected.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence for ALUM.CA matches the company but no source/report date was detected.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
