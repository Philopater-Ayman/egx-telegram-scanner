# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-10T09:10:08.339240+00:00
Generated Cairo: 2026-06-10 12:10
Run timing: target 08:45 Cairo | generated Cairo 2026-06-10 12:10 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-10 12:06

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 187/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, June 10
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.0% / above MA50 65.0%
- EGX70 regime: MIXED / above MA20 58.97% / above MA50 84.62%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=429893376.0 spike=0.51 score=22.34
- FWRY.CA: liquidity=262437024.0 spike=0.88 score=13.16
- ELSH.CA: liquidity=262317680.0 spike=1.99 score=8.16
- ACAMD.CA: liquidity=161450816.0 spike=1.38 score=23.94
- ORHD.CA: liquidity=150611824.0 spike=0.73 score=21.15

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because the EGX30 is in a bearish regime and sector breadth is weak (23.81%). EGX70 shows mixed signals but still negative 5‑day returns, so risk mode is set to DEFENSIVE_NO_NEW_BUY. Liquidity is modest and most top‑ranked tickets lack clear buy readiness, reinforcing a cautious outlook for the next 1‑3 days.
- EGX30 bearish, below MA20, median 5‑day return – ‑1.6%; EGX70 mixed, median 5‑day return – 0.54%
- Sector breadth only 23.81%; leading sectors (Automotive, Tourism, Investment Holding) show mixed performance
- Top tickets (ANFI, ZMID, GBCO, KZPC, ACAMD) have high RSI or cooling liquidity, no buy‑ready signal
- Risk mode DEFENSIVE_NO_NEW_BUY – no new entries; monitor for any shift in breadth or liquidity spikes
- Uncertainty remains high; watch for changes in EGX30 breadth or sudden liquidity spikes before reconsidering

## Top Liquidity Spikes
- EDFM.CA: spike=4.9 liquidity=2972828.22 outlook=CONSTRUCTIVE score=58.45 buy_ready=False
- ANFI.CA: spike=4.65 liquidity=134592218.23 outlook=CONSTRUCTIVE score=68.45 buy_ready=False
- CFGH.CA: spike=3.04 liquidity=15735.25 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KZPC.CA: spike=2.54 liquidity=29339978.0 outlook=BULLISH_WATCH score=92.45 buy_ready=False
- KWIN.CA: spike=2.27 liquidity=8795770.0 outlook=BULLISH_WATCH score=98.45 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=6.9 5d=2.17% 20d=-2.47% aboveMA50=100.0%
- #2 Tourism & Leisure: score=6.81 5d=-5.99% 20d=14.85% aboveMA50=100.0%
- #3 Investment Holding: score=5.86 5d=-3.11% 20d=14.08% aboveMA50=66.67%
- #4 Textiles: score=5.77 5d=-0.81% 20d=5.88% aboveMA50=75.0%
- #5 General / Verified EGX Expansion: score=5.45 5d=1.21% 20d=0.83% aboveMA50=85.58%
- #6 Agriculture & Food Production: score=5.44 5d=4.84% 20d=1.04% aboveMA50=50.0%
- #7 Real Estate: score=5.37 5d=-1.68% 20d=5.02% aboveMA50=84.62%
- #8 Food, Beverages & Tobacco: score=5.11 5d=-0.66% 20d=1.51% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- KWIN.CA: BULLISH_WATCH score=98.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- MTIE.CA: BULLISH_WATCH score=92.9 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KZPC.CA: BULLISH_WATCH score=92.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ADCI.CA: BULLISH_WATCH score=86.45 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; close to resistance
- AXPH.CA: BULLISH_WATCH score=86.45 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ALUM.CA: BULLISH_WATCH score=83.45 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- RTVC.CA: BULLISH_WATCH score=81.45 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EPCO.CA: BULLISH_WATCH score=81.45 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MEPA.CA: BULLISH_WATCH score=81.45 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- WKOL.CA: BULLISH_WATCH score=81.45 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=12.79 buy_ready=False sector_rank=5 price=218.12 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=77.66 liquidity=4609230.0 spike=0.42
- ABUK.CA: score=9.81 buy_ready=False sector_rank=18 price=80.54 support=81.2 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=19.35 liquidity=34098552.0 spike=0.28
- ACAMD.CA: score=23.94 buy_ready=False sector_rank=5 price=2.39 support=2.1 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=59.65 liquidity=161450816.0 spike=1.38
- ACGC.CA: score=21.31 buy_ready=False sector_rank=4 price=9.87 support=8.51 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=52.21 liquidity=15920081.0 spike=0.28
- ADCI.CA: score=22.58 buy_ready=False sector_rank=5 price=221.97 support=202.22 resistance=225.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=66.05 liquidity=10258062.0 spike=1.7
- ADIB.CA: score=18.1 buy_ready=False sector_rank=16 price=46.11 support=45.3 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=44.08 liquidity=25350940.0 spike=0.16
- ADPC.CA: score=5.2 buy_ready=False sector_rank=5 price=3.65 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=24.74 liquidity=4022830.75 spike=0.16
- AFDI.CA: score=16.75 buy_ready=False sector_rank=5 price=44.48 support=40.0 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=61.36 liquidity=5574356.5 spike=0.3
- AFMC.CA: score=10.19 buy_ready=False sector_rank=5 price=72.05 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=41.89 liquidity=1013605.63 spike=0.11
- AJWA.CA: score=18.39 buy_ready=False sector_rank=5 price=147.32 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=84.58 liquidity=8205052.5 spike=0.48
- ALCN.CA: score=10.69 buy_ready=False sector_rank=17 price=28.64 support=28.4 resistance=30.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=40.99 liquidity=5847556.0 spike=0.27
- ALUM.CA: score=18.9 buy_ready=False sector_rank=5 price=25.37 support=22.66 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=57.44 liquidity=3716747.25 spike=0.17
- AMER.CA: score=21.15 buy_ready=False sector_rank=7 price=2.78 support=2.4 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=59.34 liquidity=24170922.0 spike=0.21
- AMES.CA: score=7.08 buy_ready=False sector_rank=5 price=50.41 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=18.46 liquidity=2901259.0 spike=0.49
- AMIA.CA: score=14.91 buy_ready=False sector_rank=5 price=9.06 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=3726188.5 spike=0.13
- AMOC.CA: score=13.74 buy_ready=False sector_rank=11 price=8.27 support=8.1 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=11902911.0 spike=0.15
- ANFI.CA: score=25.18 buy_ready=False sector_rank=5 price=18.62 support=13.5 resistance=18.62 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=79.32 liquidity=134592218.23 spike=4.65
- APSW.CA: score=3.57 buy_ready=False sector_rank=5 price=8.9 support=8.62 resistance=9.38 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=34.21 liquidity=391929.28 spike=0.46
- ARAB.CA: score=15.15 buy_ready=False sector_rank=7 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=51.72 liquidity=24060844.0 spike=0.31
- ARCC.CA: score=18.46 buy_ready=False sector_rank=13 price=56.57 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=14082638.0 spike=0.33
- AREH.CA: score=16.51 buy_ready=False sector_rank=5 price=1.51 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=80.65 liquidity=6328128.5 spike=0.23
- ARVA.CA: score=17.78 buy_ready=False sector_rank=5 price=11.2 support=7.71 resistance=11.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=74.61 liquidity=6604008.5 spike=0.26
- ASCM.CA: score=18.18 buy_ready=False sector_rank=5 price=57.18 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=75.73 liquidity=46186696.0 spike=0.68
- ASPI.CA: score=23.18 buy_ready=False sector_rank=5 price=0.34 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=60.57 liquidity=28401652.0 spike=0.45
- ATLC.CA: score=10.29 buy_ready=False sector_rank=19 price=5.02 support=4.71 resistance=5.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=66.04 liquidity=652472.5 spike=0.1
- ATQA.CA: score=21.69 buy_ready=False sector_rank=18 price=9.94 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=9886878.0 spike=0.24
- AXPH.CA: score=15.89 buy_ready=False sector_rank=5 price=1143.25 support=1100.12 resistance=1239.0 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=51.16 liquidity=4025383.25 spike=1.34
- BINV.CA: score=13.26 buy_ready=False sector_rank=3 price=46.53 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=71.75 liquidity=918081.0 spike=0.08
- BIOC.CA: score=11.45 buy_ready=False sector_rank=5 price=71.19 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=2271305.0 spike=0.35
- BTFH.CA: score=17.64 buy_ready=False sector_rank=19 price=3.11 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=43606824.0 spike=0.18
- CAED.CA: score=5.28 buy_ready=False sector_rank=5 price=71.5 support=70.41 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=1096542.25 spike=0.07
- CANA.CA: score=13.09 buy_ready=False sector_rank=16 price=37.49 support=34.01 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=65.43 liquidity=2992881.5 spike=0.21
- CCAP.CA: score=22.34 buy_ready=False sector_rank=3 price=5.51 support=4.68 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=56.52 liquidity=429893376.0 spike=0.51
- CCRS.CA: score=14.15 buy_ready=False sector_rank=5 price=2.46 support=2.1 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=2966580.0 spike=0.11
- CEFM.CA: score=4.59 buy_ready=False sector_rank=5 price=105.02 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=30.19 liquidity=413367.16 spike=0.09
- CERA.CA: score=17.63 buy_ready=False sector_rank=5 price=1.19 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=3450924.5 spike=0.23
- CFGH.CA: score=4.28 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=15735.25 spike=3.04
- CICH.CA: score=3.24 buy_ready=False sector_rank=19 price=11.83 support=11.71 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=24.14 liquidity=604599.56 spike=0.13
- CIEB.CA: score=6.56 buy_ready=False sector_rank=16 price=23.5 support=23.31 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=37.39 liquidity=1468305.63 spike=0.15
- CIRA.CA: score=12.61 buy_ready=False sector_rank=14 price=26.27 support=23.23 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=37.54 liquidity=4196858.0 spike=0.14
- CLHO.CA: score=8.25 buy_ready=False sector_rank=9 price=14.86 support=14.83 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=30.36 liquidity=4469366.5 spike=0.13
- CNFN.CA: score=8.58 buy_ready=False sector_rank=19 price=4.59 support=4.47 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=1943933.0 spike=0.11
- COMI.CA: score=18.1 buy_ready=False sector_rank=16 price=133.07 support=129.8 resistance=144.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=48.51 liquidity=120034592.0 spike=0.18
- COPR.CA: score=18.32 buy_ready=False sector_rank=5 price=0.37 support=0.32 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=67.35 liquidity=41276684.0 spike=1.07
- COSG.CA: score=23.18 buy_ready=False sector_rank=5 price=1.7 support=1.46 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=56297780.0 spike=0.92
- CPCI.CA: score=6.53 buy_ready=False sector_rank=5 price=362.84 support=340.01 resistance=370.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=82.12 liquidity=349137.81 spike=0.08
- CSAG.CA: score=15.84 buy_ready=False sector_rank=17 price=31.67 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=54.85 liquidity=5997408.0 spike=0.33
- DAPH.CA: score=6.15 buy_ready=False sector_rank=5 price=81.26 support=79.25 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=27.1 liquidity=1968620.0 spike=0.06
- DEIN.CA: score=7.18 buy_ready=False sector_rank=5 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=5.59 buy_ready=False sector_rank=8 price=24.9 support=24.24 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:41 AM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=1545193.38 spike=0.65
- DSCW.CA: score=13.12 buy_ready=False sector_rank=5 price=1.81 support=1.71 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=5940306.0 spike=0.1
- DTPP.CA: score=4.63 buy_ready=False sector_rank=5 price=122.89 support=123.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=450533.88 spike=0.12
- EALR.CA: score=10.95 buy_ready=False sector_rank=5 price=361.07 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=48.06 liquidity=1765179.13 spike=0.18
- EASB.CA: score=9.64 buy_ready=False sector_rank=5 price=5.02 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=72.58 liquidity=459663.94 spike=0.36
- EAST.CA: score=13.92 buy_ready=False sector_rank=8 price=39.41 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=60.28 liquidity=879819.75 spike=0.01
- EBSC.CA: score=14.04 buy_ready=False sector_rank=5 price=1.82 support=1.64 resistance=2.09 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=62.79 liquidity=862683.66 spike=0.35
- ECAP.CA: score=10.91 buy_ready=False sector_rank=5 price=31.01 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=88.3 liquidity=732969.88 spike=0.14
- EDFM.CA: score=17.15 buy_ready=False sector_rank=5 price=333.09 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=38.06 liquidity=2972828.22 spike=4.9
- EEII.CA: score=22.53 buy_ready=False sector_rank=5 price=2.5 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=56.1 liquidity=9348289.0 spike=0.47
- EFIC.CA: score=0.26 buy_ready=False sector_rank=18 price=205.0 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:42 AM market time freshness=DELAYED_CURRENT RSI=7.01 liquidity=447602.66 spike=0.11
- EFID.CA: score=19.04 buy_ready=False sector_rank=8 price=27.8 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=13057520.0 spike=0.17
- EFIH.CA: score=10.04 buy_ready=False sector_rank=21 price=21.15 support=21.0 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=3880684.75 spike=0.06
- EGAL.CA: score=17.81 buy_ready=False sector_rank=18 price=315.85 support=304.0 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=38.47 liquidity=27808322.0 spike=0.25
- EGAS.CA: score=12.88 buy_ready=False sector_rank=11 price=49.99 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=42.63 liquidity=2147599.75 spike=0.16
- EGBE.CA: score=8.16 buy_ready=False sector_rank=16 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=42.52 liquidity=65524.01 spike=0.47
- EGCH.CA: score=19.01 buy_ready=False sector_rank=18 price=14.6 support=12.95 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=57.7 liquidity=7205899.5 spike=0.06
- EGSA.CA: score=7.37 buy_ready=False sector_rank=15 price=8.81 support=8.3 resistance=9.19 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=67.78 liquidity=20641.83 spike=1.57
- EGTS.CA: score=21.15 buy_ready=False sector_rank=7 price=19.06 support=12.9 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=40431996.0 spike=0.35
- EHDR.CA: score=20.18 buy_ready=False sector_rank=5 price=2.79 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=85.33 liquidity=28323408.0 spike=0.56
- EKHO.CA: score=10.74 buy_ready=False sector_rank=11 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=17.0 buy_ready=False sector_rank=10 price=2.16 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=5236518.5 spike=0.19
- ELKA.CA: score=20.18 buy_ready=False sector_rank=5 price=1.3 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=32639140.0 spike=0.78
- ELNA.CA: score=9.56 buy_ready=False sector_rank=5 price=39.54 support=37.11 resistance=42.79 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=38.94 liquidity=303153.19 spike=1.04
- ELSH.CA: score=8.16 buy_ready=False sector_rank=5 price=14.2 support=13.03 resistance=14.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=262317680.0 spike=1.99
- ELWA.CA: score=11.72 buy_ready=False sector_rank=5 price=2.12 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=91.67 liquidity=1544700.63 spike=0.51
- EMFD.CA: score=18.15 buy_ready=False sector_rank=7 price=11.95 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=75.07 liquidity=104551064.0 spike=0.44
- ENGC.CA: score=18.66 buy_ready=False sector_rank=5 price=35.24 support=32.31 resistance=35.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=70.72 liquidity=7481411.0 spike=0.57
- EOSB.CA: score=11.57 buy_ready=False sector_rank=5 price=1.42 support=1.34 resistance=1.54 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=253701.45 spike=2.07
- EPCO.CA: score=14.79 buy_ready=False sector_rank=5 price=9.39 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=55.31 liquidity=1605857.25 spike=0.13
- EPPK.CA: score=6.6 buy_ready=False sector_rank=5 price=12.25 support=11.67 resistance=13.6 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=47.1 liquidity=416512.25 spike=0.39
- ETEL.CA: score=18.21 buy_ready=False sector_rank=15 price=93.44 support=92.17 resistance=99.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=13344511.0 spike=0.12
- ETRS.CA: score=21.18 buy_ready=False sector_rank=5 price=9.3 support=7.37 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=35520340.0 spike=0.64
- EXPA.CA: score=20.1 buy_ready=False sector_rank=16 price=18.9 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=13722899.0 spike=0.34
- FAIT.CA: score=3.52 buy_ready=False sector_rank=16 price=36.76 support=34.11 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=423163.63 spike=0.07
- FAITA.CA: score=8.11 buy_ready=False sector_rank=16 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=58.82 liquidity=9290.67 spike=0.23
- FERC.CA: score=5.67 buy_ready=False sector_rank=18 price=77.31 support=76.5 resistance=83.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=36.33 liquidity=857783.5 spike=0.14
- FWRY.CA: score=13.16 buy_ready=False sector_rank=21 price=18.59 support=18.32 resistance=21.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=262437024.0 spike=0.88
- GBCO.CA: score=24.4 buy_ready=False sector_rank=1 price=28.35 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=65.27 liquidity=64448976.0 spike=0.52
- GDWA.CA: score=18.21 buy_ready=False sector_rank=5 price=0.81 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=6031618.0 spike=0.64
- GGCC.CA: score=15.95 buy_ready=False sector_rank=5 price=0.43 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=5771784.0 spike=0.82
- GIHD.CA: score=14.12 buy_ready=False sector_rank=5 price=41.73 support=39.1 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=50.23 liquidity=940295.81 spike=0.17
- GMCI.CA: score=9.23 buy_ready=False sector_rank=5 price=1.74 support=1.67 resistance=1.84 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=56.67 liquidity=428001.72 spike=1.31
- GRCA.CA: score=1.9 buy_ready=False sector_rank=5 price=55.08 support=53.16 resistance=60.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:39 AM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=722093.56 spike=0.08
- GSSC.CA: score=3.14 buy_ready=False sector_rank=5 price=251.55 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=9.47 liquidity=1955747.63 spike=0.27
- GTWL.CA: score=15.42 buy_ready=False sector_rank=5 price=49.98 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=28.28 liquidity=11228298.0 spike=1.62
- HDBK.CA: score=8.5 buy_ready=False sector_rank=16 price=140.68 support=138.75 resistance=149.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=44.01 liquidity=3403061.5 spike=0.22
- HELI.CA: score=21.15 buy_ready=False sector_rank=7 price=6.62 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=56.55 liquidity=46309036.0 spike=0.28
- HRHO.CA: score=13.64 buy_ready=False sector_rank=19 price=26.8 support=26.05 resistance=29.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=47.48 liquidity=30519998.0 spike=0.16
- ICID.CA: score=20.18 buy_ready=False sector_rank=5 price=6.8 support=4.5 resistance=6.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=90.23 liquidity=12740587.0 spike=0.89
- IDRE.CA: score=12.69 buy_ready=False sector_rank=5 price=44.0 support=39.8 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=53.64 liquidity=3513283.25 spike=0.1
- IFAP.CA: score=6.98 buy_ready=False sector_rank=6 price=19.41 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=37.74 liquidity=1803941.0 spike=0.14
- INFI.CA: score=10.92 buy_ready=False sector_rank=5 price=100.69 support=99.51 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=2744645.25 spike=0.17
- IRON.CA: score=8.77 buy_ready=False sector_rank=18 price=32.33 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=36.2 liquidity=2965190.5 spike=0.38
- ISMA.CA: score=17.52 buy_ready=False sector_rank=5 price=29.55 support=20.66 resistance=30.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=92.96 liquidity=7337040.5 spike=0.15
- ISMQ.CA: score=22.29 buy_ready=False sector_rank=18 price=8.15 support=7.27 resistance=8.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=67.86 liquidity=63174660.0 spike=1.24
- ISPH.CA: score=22.78 buy_ready=False sector_rank=9 price=12.27 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=63.98 liquidity=25276198.0 spike=0.16
- JUFO.CA: score=20.04 buy_ready=False sector_rank=8 price=30.1 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=75.46 liquidity=11603208.0 spike=0.24
- KABO.CA: score=21.31 buy_ready=False sector_rank=4 price=6.36 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=72.34 liquidity=10987781.0 spike=0.55
- KWIN.CA: score=22.52 buy_ready=False sector_rank=5 price=73.62 support=69.0 resistance=80.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=58.39 liquidity=8795770.0 spike=2.27
- KZPC.CA: score=24.26 buy_ready=False sector_rank=5 price=11.05 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=29339978.0 spike=2.54
- LCSW.CA: score=10.32 buy_ready=False sector_rank=13 price=27.12 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=53.42 liquidity=1867173.88 spike=0.12
- LUTS.CA: score=17.18 buy_ready=False sector_rank=5 price=0.63 support=0.54 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=68.55 liquidity=5998159.0 spike=0.37
- MAAL.CA: score=21.97 buy_ready=False sector_rank=5 price=6.1 support=4.44 resistance=6.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=6792531.5 spike=0.53
- MASR.CA: score=21.8 buy_ready=False sector_rank=5 price=7.15 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=76298320.0 spike=1.31
- MBSC.CA: score=20.46 buy_ready=False sector_rank=13 price=275.0 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=37.97 liquidity=12285781.0 spike=0.25
- MCQE.CA: score=15.46 buy_ready=False sector_rank=13 price=181.87 support=185.59 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=44.13 liquidity=10078591.0 spike=0.53
- MCRO.CA: score=20.18 buy_ready=False sector_rank=5 price=1.26 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=57.89 liquidity=13895641.0 spike=0.16
- MENA.CA: score=14.59 buy_ready=False sector_rank=7 price=6.74 support=5.8 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:46 AM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=1443458.25 spike=0.09
- MEPA.CA: score=14.77 buy_ready=False sector_rank=5 price=1.72 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=1593663.12 spike=0.08
- MFPC.CA: score=9.81 buy_ready=False sector_rank=18 price=41.77 support=42.01 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=28.62 liquidity=20579540.0 spike=0.24
- MFSC.CA: score=6.71 buy_ready=False sector_rank=5 price=46.11 support=40.62 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=12.81 liquidity=2534654.0 spike=0.17
- MHOT.CA: score=16.76 buy_ready=False sector_rank=2 price=30.92 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=62.18 liquidity=3363622.5 spike=0.16
- MICH.CA: score=22.56 buy_ready=False sector_rank=5 price=38.27 support=35.01 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=72.61 liquidity=15053984.0 spike=1.69
- MILS.CA: score=12.94 buy_ready=False sector_rank=5 price=143.17 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=70.06 liquidity=1756181.63 spike=0.08
- MIPH.CA: score=10.81 buy_ready=False sector_rank=9 price=663.27 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:34 AM market time freshness=DELAYED_CURRENT RSI=39.51 liquidity=2029303.5 spike=0.64
- MOED.CA: score=3.1 buy_ready=False sector_rank=5 price=0.69 support=0.68 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=26.04 liquidity=2921550.75 spike=0.22
- MOIL.CA: score=14.74 buy_ready=False sector_rank=11 price=0.48 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:35 AM market time freshness=DELAYED_CURRENT RSI=64.71 liquidity=8821.78 spike=0.05
- MOIN.CA: score=8.66 buy_ready=False sector_rank=5 price=25.01 support=24.02 resistance=26.4 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=67.2 liquidity=477966.11 spike=0.28
- MOSC.CA: score=4.72 buy_ready=False sector_rank=5 price=262.99 support=264.0 resistance=320.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=19.23 liquidity=544725.63 spike=0.04
- MPCI.CA: score=23.18 buy_ready=False sector_rank=5 price=228.91 support=193.8 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=68.96 liquidity=26346710.0 spike=0.29
- MPCO.CA: score=21.18 buy_ready=False sector_rank=6 price=1.8 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=70.83 liquidity=18352954.0 spike=0.25
- MPRC.CA: score=22.49 buy_ready=False sector_rank=5 price=32.94 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.93 liquidity=9311569.0 spike=0.43
- MTIE.CA: score=18.23 buy_ready=False sector_rank=1 price=9.1 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=48.87 liquidity=3829949.5 spike=0.18
- NAHO.CA: score=5.19 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=14441.6 spike=0.39
- NCCW.CA: score=20.18 buy_ready=False sector_rank=5 price=6.6 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=82.23 liquidity=17663202.0 spike=0.72
- NEDA.CA: score=11.31 buy_ready=False sector_rank=5 price=2.8 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=132372.8 spike=0.27
- NHPS.CA: score=8.92 buy_ready=False sector_rank=5 price=69.38 support=67.53 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=46.68 liquidity=743946.31 spike=0.07
- NINH.CA: score=5.28 buy_ready=False sector_rank=5 price=17.68 support=17.53 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=26.42 liquidity=1101468.63 spike=0.11
- NIPH.CA: score=18.78 buy_ready=False sector_rank=9 price=164.0 support=155.1 resistance=186.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=57.17 liquidity=30821908.0 spike=0.27
- OBRI.CA: score=21.64 buy_ready=False sector_rank=5 price=36.73 support=33.63 resistance=39.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=48.8 liquidity=19648400.0 spike=1.73
- OCDI.CA: score=19.15 buy_ready=False sector_rank=7 price=21.51 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.38 liquidity=11932977.0 spike=0.28
- OCPH.CA: score=10.84 buy_ready=False sector_rank=5 price=359.35 support=350.0 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=1656919.0 spike=0.17
- ODIN.CA: score=15.29 buy_ready=False sector_rank=5 price=2.14 support=1.89 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:53 AM market time freshness=DELAYED_CURRENT RSI=79.07 liquidity=5110936.0 spike=0.48
- OFH.CA: score=18.34 buy_ready=False sector_rank=5 price=0.62 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=7162950.5 spike=0.32
- OIH.CA: score=12.34 buy_ready=False sector_rank=3 price=1.39 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=27.59 liquidity=21670998.0 spike=0.19
- OLFI.CA: score=21.04 buy_ready=False sector_rank=8 price=21.9 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=61.66 liquidity=15678597.0 spike=0.75
- ORAS.CA: score=4.6 buy_ready=False sector_rank=20 price=733.12 support=722.0 resistance=734.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=149097024.0 spike=1.0
- ORHD.CA: score=21.15 buy_ready=False sector_rank=7 price=37.87 support=32.9 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.47 liquidity=150611824.0 spike=0.73
- ORWE.CA: score=21.31 buy_ready=False sector_rank=4 price=23.71 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=72.17 liquidity=11997236.0 spike=0.26
- PHAR.CA: score=12.43 buy_ready=False sector_rank=9 price=86.27 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=3649818.25 spike=0.11
- PHDC.CA: score=19.15 buy_ready=False sector_rank=7 price=15.05 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=66.12 liquidity=59511444.0 spike=0.14
- PHTV.CA: score=10.42 buy_ready=False sector_rank=5 price=207.28 support=203.25 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=56.33 liquidity=1242353.13 spike=0.08
- POUL.CA: score=13.4 buy_ready=False sector_rank=8 price=36.98 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=4356441.5 spike=0.09
- PRCL.CA: score=17.46 buy_ready=False sector_rank=13 price=25.26 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=62.27 liquidity=4999336.5 spike=0.14
- PRDC.CA: score=13.52 buy_ready=False sector_rank=7 price=6.07 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=76.3 liquidity=5375224.0 spike=0.27
- PRMH.CA: score=13.59 buy_ready=False sector_rank=5 price=2.71 support=2.17 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=77.53 liquidity=5411518.0 spike=0.36
- RACC.CA: score=10.31 buy_ready=False sector_rank=5 price=9.84 support=9.56 resistance=12.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=1127318.13 spike=0.06
- RAKT.CA: score=9.29 buy_ready=False sector_rank=5 price=23.79 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=54.9 liquidity=113858.94 spike=0.43
- RAYA.CA: score=18.48 buy_ready=False sector_rank=12 price=7.38 support=6.94 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=22400936.0 spike=0.2
- RMDA.CA: score=22.78 buy_ready=False sector_rank=9 price=5.17 support=4.95 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=13300208.0 spike=0.12
- ROTO.CA: score=17.02 buy_ready=False sector_rank=5 price=34.87 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=71.72 liquidity=3842407.5 spike=0.3
- RREI.CA: score=15.39 buy_ready=False sector_rank=5 price=3.53 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=6208320.0 spike=0.26
- RTVC.CA: score=15.63 buy_ready=False sector_rank=5 price=3.96 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=57.81 liquidity=2447329.25 spike=0.36
- RUBX.CA: score=8.34 buy_ready=False sector_rank=5 price=10.37 support=9.8 resistance=11.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:50 AM market time freshness=DELAYED_CURRENT RSI=32.96 liquidity=4162439.75 spike=0.28
- SAUD.CA: score=10.98 buy_ready=False sector_rank=16 price=21.74 support=21.8 resistance=24.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=41.58 liquidity=5883817.5 spike=0.43
- SCEM.CA: score=13.21 buy_ready=False sector_rank=13 price=63.11 support=62.5 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=4752858.0 spike=0.12
- SCFM.CA: score=5.46 buy_ready=False sector_rank=5 price=260.0 support=255.7 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=30.8 liquidity=1282041.75 spike=0.06
- SCTS.CA: score=4.62 buy_ready=False sector_rank=14 price=620.62 support=590.01 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=33.16 liquidity=1200375.63 spike=0.11
- SDTI.CA: score=14.43 buy_ready=False sector_rank=5 price=47.24 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=68.43 liquidity=1254344.5 spike=0.06
- SEIG.CA: score=13.64 buy_ready=False sector_rank=5 price=188.73 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=57.11 liquidity=456727.22 spike=0.08
- SIPC.CA: score=14.31 buy_ready=False sector_rank=5 price=3.63 support=3.4 resistance=3.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:45 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=1128401.63 spike=0.07
- SKPC.CA: score=13.75 buy_ready=False sector_rank=18 price=17.24 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=40.27 liquidity=9946165.0 spike=0.15
- SMFR.CA: score=11.19 buy_ready=False sector_rank=5 price=205.18 support=203.51 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=2012366.88 spike=0.34
- SNFC.CA: score=14.05 buy_ready=False sector_rank=5 price=12.1 support=11.66 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=4871204.5 spike=0.18
- SPIN.CA: score=2.67 buy_ready=False sector_rank=4 price=14.07 support=13.69 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=23.93 liquidity=1366813.5 spike=0.28
- SPMD.CA: score=14.97 buy_ready=False sector_rank=5 price=0.42 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:49 AM market time freshness=DELAYED_CURRENT RSI=58.42 liquidity=3787338.5 spike=0.15
- SUGR.CA: score=16.18 buy_ready=False sector_rank=8 price=49.97 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:37 AM market time freshness=DELAYED_CURRENT RSI=42.71 liquidity=5131848.5 spike=0.32
- SVCE.CA: score=14.18 buy_ready=False sector_rank=5 price=8.68 support=8.33 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=28.71 liquidity=10376233.0 spike=0.09
- SWDY.CA: score=14.08 buy_ready=False sector_rank=10 price=87.16 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=54.88 liquidity=5317766.0 spike=0.15
- TALM.CA: score=15.24 buy_ready=False sector_rank=14 price=15.92 support=15.12 resistance=17.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=48.64 liquidity=2819241.5 spike=0.21
- TMGH.CA: score=14.15 buy_ready=False sector_rank=7 price=95.96 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=34.65 liquidity=76012880.0 spike=0.15
- TRTO.CA: score=7.18 buy_ready=False sector_rank=5 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=189.24 spike=0.4
- UEFM.CA: score=0.78 buy_ready=False sector_rank=5 price=473.74 support=455.6 resistance=504.97 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=33.63 liquidity=604018.49 spike=0.72
- UEGC.CA: score=21.56 buy_ready=False sector_rank=5 price=1.48 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:51 AM market time freshness=DELAYED_CURRENT RSI=72.0 liquidity=30367502.0 spike=1.19
- UNIP.CA: score=22.82 buy_ready=False sector_rank=5 price=0.33 support=0.28 resistance=0.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:54 AM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=29778260.0 spike=1.82
- UNIT.CA: score=2.72 buy_ready=False sector_rank=7 price=14.75 support=13.82 resistance=14.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:47 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6575991.0 spike=0.62
- WCDF.CA: score=4.3 buy_ready=False sector_rank=5 price=539.17 support=535.0 resistance=558.89 source=Yahoo Finance as_of=2026-06-08T21:00:00+00:00 freshness=FRESH RSI=25.38 liquidity=124548.27 spike=0.42
- WKOL.CA: score=13.11 buy_ready=False sector_rank=5 price=299.94 support=290.0 resistance=324.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:48 AM market time freshness=DELAYED_CURRENT RSI=48.9 liquidity=1929699.13 spike=0.31
- ZEOT.CA: score=14.08 buy_ready=False sector_rank=5 price=9.18 support=8.43 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:44 AM market time freshness=DELAYED_CURRENT RSI=59.86 liquidity=904403.81 spike=0.13
- ZMID.CA: score=25.15 buy_ready=False sector_rank=7 price=6.4 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:52 AM market time freshness=DELAYED_CURRENT RSI=63.11 liquidity=94810416.0 spike=0.42

## Backtesting Lite
- ANFI.CA: 180d return=186.9%, max drawdown=-19.31%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- ZMID.CA: 180d return=62.61%, max drawdown=-19.84%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- GBCO.CA: 180d return=29.48%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-06-08T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=525 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- KZPC.CA: status=OLD_ACCEPTED latest=2024-01-01 age_days=891 sources=3 expected=Kafr El Zayat For Pesticides & Chemicals Co.(S.A.E) summary=Kafr El Zayat to set up fund with EGP 5m capital; Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024; Kafr El Zayat Pesticides’ EGM approves stock split, capital hike
  - Kafr El Zayat to set up fund with EGP 5m capital: https://english.mubasher.info/news/4201137/Kafr-El-Zayat-to-set-up-fund-with-EGP-5m-capital/
  - Kafr El Zayat Pesticides targets EGP 1.73bn sales in 2024: https://english.mubasher.info/news/4200526/Kafr-El-Zayat-Pesticides-targets-EGP-1-73bn-sales-in-2024/
  - Kafr El Zayat Pesticides’ EGM approves stock split, capital hike: https://english.mubasher.info/news/4052937/Kafr-El-Zayat-Pesticides-EGM-approves-stock-split-capital-hike/
- ACAMD.CA: status=OLD_ACCEPTED latest=2020-01-01 age_days=2352 sources=3 expected=Arab Co.,for asset management and development summary=Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25; Arab Co. for Asset Management approves offer to sell land in El-Minya; Arab Co. Asset Management swings to loss in 2020
  - Arab Company for Asset Management shifts to EGP 7m net profits in 9M-25: https://english.mubasher.info/news/4543171/Arab-Company-for-Asset-Management-shifts-to-EGP-7m-net-profits-in-9M-25/
  - Arab Co. for Asset Management approves offer to sell land in El-Minya: https://english.mubasher.info/news/3777445/Arab-Co-for-Asset-Management-approves-offer-to-sell-land-in-El-Minya/
  - Arab Co. Asset Management swings to loss in 2020: https://english.mubasher.info/news/3767136/Arab-Co-Asset-Management-swings-to-loss-in-2020/
- ASPI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Aspire Capital Holding for Financial Investments summary=Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25; PREDCO, Aspire Holding consider establishing mortgage company; Pioneers Holding gets EGX&#39;s approval for capital cut, name change
  - Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25: https://english.mubasher.info/news/4541324/Aspire-Capital-records-higher-consolidated-net-profits-at-over-EGP-42m-in-9M-25/
  - PREDCO, Aspire Holding consider establishing mortgage company: https://english.mubasher.info/news/4185438/PREDCO-Aspire-Holding-consider-establishing-mortgage-company/
  - Pioneers Holding gets EGX&#39;s approval for capital cut, name change: https://english.mubasher.info/news/3861454/Pioneers-Holding-gets-EGX-s-approval-for-capital-cut-name-change/
- COSG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Oil & Soap Company summary=Cairo Oils stock stabilizes above EGP 1.50 resistance level; EGX approves capital increase, reduction of several listed firms; Cairo oils incurs EGP 25m losses in H1-19
  - Cairo Oils stock stabilizes above EGP 1.50 resistance level: https://english.mubasher.info/news/4546423/Cairo-Oils-stock-stabilizes-above-EGP-1-50-resistance-level/
  - EGX approves capital increase, reduction of several listed firms: https://english.mubasher.info/news/3828111/EGX-approves-capital-increase-reduction-of-several-listed-firms/
  - Cairo oils incurs EGP 25m losses in H1-19: https://english.mubasher.info/news/3521392/Cairo-oils-incurs-EGP-25m-losses-in-H1-19/
- MPCI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Memphis Pharmaceuticals & Chemical Industries summary=Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.

## Warnings
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence for KZPC.CA matches the company but appears old; latest detected date is 2024-01-01.
- Evidence for ACAMD.CA matches the company but appears old; latest detected date is 2020-01-01.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
- Evidence for COSG.CA matches the company but no source/report date was detected.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
