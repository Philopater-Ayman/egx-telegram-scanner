# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-07-30T08:48:45.523088+00:00
Generated Cairo: 2026-07-30 11:48
Run timing: target 09:15 Cairo | generated Cairo 2026-07-30 11:48 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-07-30 11:45

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 179/189
- Top sector: Education

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, July 30
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 40.0% / above MA50 35.0%
- EGX70 regime: MIXED / above MA20 46.15% / above MA50 69.23%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- AMOC.CA: liquidity=265328080.0 spike=4.4 score=10.84
- CCAP.CA: liquidity=226923408.0 spike=0.32 score=19.12
- BIOC.CA: liquidity=200903024.0 spike=3.08 score=10.56
- AFMC.CA: liquidity=176427376.0 spike=2.89 score=10.18
- PHAR.CA: liquidity=154925552.0 spike=2.48 score=23.36

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 bearish, EGX70 mixed, sector breadth 33%; defensive risk mode blocks new buys; scanner highlights top tickets with constructive/bullish watch but stretched momentum.
- Selection based on high rank_score, constructive outlook, accumulation‑spike liquidity and strong sector showing (Education, Textiles, Agriculture).
- Liquidity spikes and support far below current price suggest limited near‑term upside; resistance is tight or above, implying possible pull‑back in 1‑3 days.
- EGX30 bearish and EGX70 mixed keep risk in DEFENSIVE_NO_NEW_BUY mode, so no new buy is allowed despite individual ticket optimism.
- Uncertainty remains from overheated RSI (>70), cooling liquidity in some names and mixed sector breadth, which could reverse the short‑term bias.

## Top Liquidity Spikes
- EOSB.CA: spike=12.18 liquidity=442157.66 outlook=CONSTRUCTIVE score=67.33 buy_ready=False
- AMOC.CA: spike=4.4 liquidity=265328080.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BIOC.CA: spike=3.08 liquidity=200903024.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- WKOL.CA: spike=3.04 liquidity=31546908.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELWA.CA: spike=2.91 liquidity=4460411.4 outlook=NEUTRAL score=40.33 buy_ready=False

## Sector Leaderboard
- #1 Education: score=14.35 5d=12.93% 20d=15.32% aboveMA50=100.0%
- #2 Textiles: score=7.92 5d=1.32% 20d=11.88% aboveMA50=75.0%
- #3 Agriculture & Food Production: score=7.45 5d=4.52% 20d=8.39% aboveMA50=50.0%
- #4 General / Verified EGX Expansion: score=7.33 5d=0.12% 20d=13.3% aboveMA50=75.73%
- #5 Healthcare: score=7.12 5d=-0.06% 20d=9.7% aboveMA50=83.33%
- #6 Real Estate: score=6.63 5d=0.11% 20d=14.62% aboveMA50=69.23%
- #7 Building Materials: score=6.36 5d=-0.01% 20d=12.34% aboveMA50=50.0%
- #8 Telecommunications: score=6.22 5d=0.82% 20d=10.02% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=98.45 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- SPIN.CA: BULLISH_WATCH score=85.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- AJWA.CA: BULLISH_WATCH score=82.33 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- TALM.CA: BULLISH_WATCH score=81 liquidity=TRADEABLE sector=LEADING risk=overheated RSI
- ACGC.CA: BULLISH_WATCH score=79.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- KABO.CA: BULLISH_WATCH score=75.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended; far above support
- EFIH.CA: BULLISH_WATCH score=75.87 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- EGAS.CA: BULLISH_WATCH score=75.61 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- MICH.CA: BULLISH_WATCH score=75.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended
- MOSC.CA: BULLISH_WATCH score=75.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=8.66 buy_ready=False sector_rank=4 price=282.39 support=240.49 resistance=289.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43155564.0 spike=2.13
- ABUK.CA: score=19.14 buy_ready=False sector_rank=16 price=71.55 support=67.04 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=50.07 liquidity=51347688.0 spike=0.34
- ACAMD.CA: score=21.4 buy_ready=False sector_rank=4 price=2.34 support=2.2 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=56.25 liquidity=23405858.0 spike=0.32
- ACGC.CA: score=21.51 buy_ready=False sector_rank=2 price=10.22 support=9.03 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=67.04 liquidity=8113569.5 spike=0.27
- ADCI.CA: score=11.26 buy_ready=False sector_rank=4 price=251.42 support=230.0 resistance=269.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=77.43 liquidity=2858118.0 spike=0.28
- ADIB.CA: score=18.0 buy_ready=False sector_rank=11 price=51.82 support=44.9 resistance=52.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=79.65 liquidity=61434672.0 spike=0.46
- ADPC.CA: score=21.4 buy_ready=False sector_rank=4 price=3.89 support=3.37 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=67.2 liquidity=12136130.0 spike=0.35
- AFDI.CA: score=20.4 buy_ready=False sector_rank=4 price=50.7 support=42.6 resistance=52.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=79.14 liquidity=12358839.0 spike=0.7
- AFMC.CA: score=10.18 buy_ready=False sector_rank=4 price=172.23 support=148.0 resistance=179.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=176427376.0 spike=2.89
- AJWA.CA: score=23.64 buy_ready=False sector_rank=4 price=190.43 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=68.22 liquidity=31512910.0 spike=1.12
- ALCN.CA: score=7.73 buy_ready=False sector_rank=21 price=28.96 support=27.74 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=65.48 liquidity=5576263.5 spike=0.25
- ALUM.CA: score=9.22 buy_ready=False sector_rank=4 price=22.75 support=20.8 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=53.21 liquidity=824808.13 spike=0.13
- AMER.CA: score=20.4 buy_ready=False sector_rank=6 price=4.69 support=2.32 resistance=4.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=91.74 liquidity=30964150.0 spike=0.27
- AMES.CA: score=21.4 buy_ready=False sector_rank=4 price=121.54 support=57.23 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=68.14 liquidity=16308083.0 spike=0.15
- AMIA.CA: score=17.09 buy_ready=False sector_rank=4 price=11.04 support=8.43 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=79.14 liquidity=6690387.5 spike=0.45
- AMOC.CA: score=10.84 buy_ready=False sector_rank=14 price=8.88 support=8.55 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=265328080.0 spike=4.4
- APSW.CA: score=13.18 buy_ready=False sector_rank=4 price=8.84 support=8.1 resistance=9.34 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=57.58 liquidity=776832.69 spike=0.5
- ARAB.CA: score=19.4 buy_ready=False sector_rank=6 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=60.98 liquidity=29483742.0 spike=0.22
- ARCC.CA: score=20.4 buy_ready=False sector_rank=7 price=56.0 support=53.5 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=18737726.0 spike=0.67
- AREH.CA: score=14.61 buy_ready=False sector_rank=4 price=1.39 support=1.44 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=8208536.5 spike=0.29
- ARVA.CA: score=8.4 buy_ready=False sector_rank=4 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=81.74 liquidity=0.0 spike=0.0
- ASCM.CA: score=18.4 buy_ready=False sector_rank=4 price=61.57 support=57.25 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=26232896.0 spike=0.48
- ASPI.CA: score=18.4 buy_ready=False sector_rank=4 price=0.43 support=0.31 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=87.64 liquidity=12919138.0 spike=0.33
- ATLC.CA: score=9.81 buy_ready=False sector_rank=15 price=5.11 support=4.97 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=1332426.38 spike=0.19
- ATQA.CA: score=17.14 buy_ready=False sector_rank=16 price=9.79 support=9.35 resistance=10.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=76.47 liquidity=21479998.0 spike=0.55
- AXPH.CA: score=12.16 buy_ready=False sector_rank=4 price=1208.78 support=1090.02 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=64.19 liquidity=761830.44 spike=0.2
- BINV.CA: score=10.48 buy_ready=False sector_rank=10 price=46.61 support=45.09 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=46.93 liquidity=1360980.25 spike=0.19
- BIOC.CA: score=10.56 buy_ready=False sector_rank=4 price=230.95 support=210.5 resistance=239.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=200903024.0 spike=3.08
- BTFH.CA: score=22.48 buy_ready=False sector_rank=15 price=3.09 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=98866832.0 spike=0.45
- CAED.CA: score=18.4 buy_ready=False sector_rank=4 price=126.27 support=70.1 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=77.81 liquidity=12152927.0 spike=0.18
- CANA.CA: score=16.33 buy_ready=False sector_rank=11 price=37.71 support=35.18 resistance=39.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=5324666.0 spike=0.31
- CCAP.CA: score=19.12 buy_ready=False sector_rank=10 price=5.28 support=4.71 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=226923408.0 spike=0.32
- CCRS.CA: score=19.4 buy_ready=False sector_rank=4 price=2.54 support=2.18 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=68.0 liquidity=8000609.5 spike=0.45
- CEFM.CA: score=23.16 buy_ready=False sector_rank=4 price=137.66 support=96.1 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=71.78 liquidity=43431168.0 spike=1.88
- CERA.CA: score=15.2 buy_ready=False sector_rank=4 price=1.28 support=1.2 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=54.05 liquidity=5800714.0 spike=0.23
- CFGH.CA: score=-1.51 buy_ready=False sector_rank=4 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31725.23 spike=2.03
- CICH.CA: score=9.45 buy_ready=False sector_rank=15 price=12.02 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=55.16 liquidity=1969427.75 spike=0.38
- CIEB.CA: score=10.39 buy_ready=False sector_rank=11 price=23.86 support=23.37 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=54.86 liquidity=4388969.5 spike=0.5
- CIRA.CA: score=23.4 buy_ready=False sector_rank=1 price=35.41 support=27.74 resistance=36.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=84.29 liquidity=39410372.0 spike=0.74
- CLHO.CA: score=19.26 buy_ready=False sector_rank=5 price=16.36 support=15.98 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=62.01 liquidity=9864021.0 spike=0.23
- CNFN.CA: score=10.96 buy_ready=False sector_rank=15 price=4.76 support=4.7 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=56.82 liquidity=2478645.5 spike=0.12
- COMI.CA: score=21.0 buy_ready=False sector_rank=11 price=139.52 support=126.89 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=68.64 liquidity=84842856.0 spike=0.2
- COPR.CA: score=17.4 buy_ready=False sector_rank=4 price=0.4 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=75.76 liquidity=12269654.0 spike=0.41
- COSG.CA: score=19.4 buy_ready=False sector_rank=4 price=1.62 support=1.5 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=68.18 liquidity=18254628.0 spike=0.41
- CPCI.CA: score=12.96 buy_ready=False sector_rank=4 price=462.45 support=389.0 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=72.51 liquidity=1564630.25 spike=0.14
- CSAG.CA: score=12.59 buy_ready=False sector_rank=21 price=31.56 support=32.0 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=8439605.0 spike=0.57
- DAPH.CA: score=19.21 buy_ready=False sector_rank=4 price=95.31 support=80.06 resistance=99.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=80.96 liquidity=8809640.0 spike=0.49
- DEIN.CA: score=-3.6 buy_ready=False sector_rank=4 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=8.44 buy_ready=False sector_rank=18 price=26.4 support=26.35 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=45.59 liquidity=973408.88 spike=0.3
- DSCW.CA: score=21.4 buy_ready=False sector_rank=4 price=1.91 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=75.0 liquidity=18647014.0 spike=0.34
- DTPP.CA: score=21.4 buy_ready=False sector_rank=4 price=238.49 support=153.55 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=65.3 liquidity=18353574.0 spike=0.24
- EALR.CA: score=8.38 buy_ready=False sector_rank=4 price=420.83 support=365.0 resistance=424.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=37317000.0 spike=1.99
- EASB.CA: score=11.45 buy_ready=False sector_rank=4 price=7.33 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=60.77 liquidity=2047286.13 spike=0.15
- EAST.CA: score=15.47 buy_ready=False sector_rank=18 price=36.25 support=36.01 resistance=37.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=42123608.0 spike=0.54
- EBSC.CA: score=10.16 buy_ready=False sector_rank=4 price=1.86 support=1.74 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=759299.63 spike=0.09
- ECAP.CA: score=11.91 buy_ready=False sector_rank=4 price=32.23 support=31.95 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=66.3 liquidity=2514561.75 spike=0.43
- EDFM.CA: score=14.47 buy_ready=False sector_rank=4 price=389.8 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=73.92 liquidity=3069328.75 spike=0.63
- EEII.CA: score=17.07 buy_ready=False sector_rank=4 price=2.61 support=2.37 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=7670984.5 spike=0.34
- EFIC.CA: score=18.14 buy_ready=False sector_rank=16 price=195.33 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=71.09 liquidity=10296657.0 spike=0.62
- EFID.CA: score=9.47 buy_ready=False sector_rank=18 price=26.82 support=26.64 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=33.03 liquidity=21451558.0 spike=0.46
- EFIH.CA: score=22.95 buy_ready=False sector_rank=12 price=22.4 support=20.16 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=58.31 liquidity=28697054.0 spike=0.45
- EGAL.CA: score=17.14 buy_ready=False sector_rank=16 price=296.0 support=275.0 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=55.2 liquidity=11477789.0 spike=0.27
- EGAS.CA: score=16.29 buy_ready=False sector_rank=14 price=51.86 support=48.5 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=3441406.75 spike=0.27
- EGBE.CA: score=8.52 buy_ready=False sector_rank=11 price=0.47 support=-0.34 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=95.96 liquidity=71170.44 spike=1.22
- EGCH.CA: score=15.14 buy_ready=False sector_rank=16 price=12.82 support=12.19 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=24798974.0 spike=0.4
- EGSA.CA: score=6.41 buy_ready=False sector_rank=8 price=8.87 support=8.67 resistance=9.21 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=10954.45 spike=0.6
- EGTS.CA: score=11.26 buy_ready=False sector_rank=6 price=17.48 support=16.75 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=39.35 liquidity=4857105.5 spike=0.11
- EHDR.CA: score=21.4 buy_ready=False sector_rank=4 price=2.78 support=2.44 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=67.06 liquidity=16020137.0 spike=0.39
- EKHO.CA: score=4.84 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=17.22 buy_ready=False sector_rank=9 price=2.14 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=60.53 liquidity=28264516.0 spike=0.4
- ELKA.CA: score=19.4 buy_ready=False sector_rank=4 price=1.78 support=1.21 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=68.81 liquidity=26302420.0 spike=0.34
- ELNA.CA: score=9.85 buy_ready=False sector_rank=4 price=38.72 support=36.1 resistance=40.5 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=63.52 liquidity=449810.25 spike=0.73
- ELSH.CA: score=19.4 buy_ready=False sector_rank=4 price=13.92 support=11.53 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=60.64 liquidity=66613552.0 spike=0.46
- ELWA.CA: score=9.68 buy_ready=False sector_rank=4 price=1.79 support=1.74 resistance=2.14 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=30.77 liquidity=4460411.4 spike=2.91
- EMFD.CA: score=16.4 buy_ready=False sector_rank=6 price=11.23 support=11.4 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=45.1 liquidity=22378148.0 spike=0.37
- ENGC.CA: score=13.91 buy_ready=False sector_rank=4 price=41.93 support=36.0 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=67.59 liquidity=4505398.0 spike=0.18
- EOSB.CA: score=18.84 buy_ready=False sector_rank=4 price=1.55 support=1.5 resistance=1.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=442157.66 spike=12.18
- EPCO.CA: score=12.33 buy_ready=False sector_rank=4 price=10.61 support=8.57 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=3926806.25 spike=0.13
- EPPK.CA: score=11.73 buy_ready=False sector_rank=4 price=15.07 support=13.03 resistance=15.93 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=58.31 liquidity=334674.55 spike=0.27
- ETEL.CA: score=20.4 buy_ready=False sector_rank=8 price=103.99 support=90.05 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=84.46 liquidity=49611256.0 spike=0.59
- ETRS.CA: score=17.6 buy_ready=False sector_rank=4 price=10.45 support=10.1 resistance=11.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=8196002.0 spike=0.17
- EXPA.CA: score=20.0 buy_ready=False sector_rank=11 price=19.81 support=18.14 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=85.34 liquidity=11374956.0 spike=0.37
- FAIT.CA: score=6.64 buy_ready=False sector_rank=11 price=36.18 support=35.6 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:21 AM market time freshness=DELAYED_CURRENT RSI=53.56 liquidity=635076.5 spike=0.22
- FAITA.CA: score=1.04 buy_ready=False sector_rank=11 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=29.82 liquidity=32228.94 spike=0.76
- FERC.CA: score=8.53 buy_ready=False sector_rank=16 price=75.71 support=72.91 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=52.04 liquidity=2394713.5 spike=0.2
- FWRY.CA: score=17.95 buy_ready=False sector_rank=12 price=18.9 support=18.28 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=41.7 liquidity=33126472.0 spike=0.26
- GBCO.CA: score=18.86 buy_ready=False sector_rank=13 price=29.83 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=49.45 liquidity=14722578.0 spike=0.21
- GDWA.CA: score=18.4 buy_ready=False sector_rank=4 price=0.81 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=66.86 liquidity=43188632.0 spike=0.42
- GGCC.CA: score=17.53 buy_ready=False sector_rank=4 price=0.81 support=0.46 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=79.32 liquidity=9127346.0 spike=0.24
- GIHD.CA: score=20.29 buy_ready=False sector_rank=4 price=57.73 support=40.91 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=73.4 liquidity=8888739.0 spike=0.17
- GMCI.CA: score=9.93 buy_ready=False sector_rank=4 price=1.98 support=1.74 resistance=2.26 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=35.29 liquidity=532441.81 spike=0.39
- GRCA.CA: score=14.28 buy_ready=False sector_rank=4 price=59.95 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:23 AM market time freshness=DELAYED_CURRENT RSI=73.51 liquidity=2877050.0 spike=0.18
- GSSC.CA: score=21.16 buy_ready=False sector_rank=4 price=278.09 support=241.32 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=76.68 liquidity=16731193.0 spike=1.38
- GTWL.CA: score=21.4 buy_ready=False sector_rank=4 price=101.25 support=76.25 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=20339440.0 spike=0.15
- HDBK.CA: score=15.38 buy_ready=False sector_rank=11 price=81.68 support=76.9 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=53.14 liquidity=6379543.0 spike=0.21
- HELI.CA: score=20.4 buy_ready=False sector_rank=6 price=8.4 support=6.4 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=86.57 liquidity=136343520.0 spike=0.67
- HRHO.CA: score=14.48 buy_ready=False sector_rank=15 price=26.2 support=26.25 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=43.65 liquidity=34632092.0 spike=0.4
- ICID.CA: score=13.1 buy_ready=False sector_rank=4 price=8.0 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=61.04 liquidity=3704135.25 spike=0.49
- IDRE.CA: score=19.54 buy_ready=False sector_rank=4 price=47.1 support=41.8 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=66.69 liquidity=8140505.0 spike=0.3
- IFAP.CA: score=12.75 buy_ready=False sector_rank=3 price=19.2 support=18.96 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=61.19 liquidity=4352812.0 spike=0.46
- INFI.CA: score=15.16 buy_ready=False sector_rank=4 price=107.46 support=89.02 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=75.62 liquidity=6759522.5 spike=0.4
- IRON.CA: score=1.8 buy_ready=False sector_rank=16 price=30.29 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=25.87 liquidity=2662094.75 spike=0.42
- ISMA.CA: score=17.82 buy_ready=False sector_rank=4 price=30.4 support=26.54 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=82.93 liquidity=9420766.0 spike=0.36
- ISMQ.CA: score=18.14 buy_ready=False sector_rank=16 price=9.15 support=9.06 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=41.42 liquidity=45576264.0 spike=0.49
- ISPH.CA: score=18.4 buy_ready=False sector_rank=5 price=11.36 support=11.2 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=54.81 liquidity=19075918.0 spike=0.39
- JUFO.CA: score=9.47 buy_ready=False sector_rank=18 price=28.61 support=28.5 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=19.68 liquidity=11140409.0 spike=0.43
- KABO.CA: score=21.16 buy_ready=False sector_rank=2 price=7.89 support=6.21 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=65.11 liquidity=7762620.0 spike=0.16
- KWIN.CA: score=18.4 buy_ready=False sector_rank=4 price=98.11 support=66.1 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=89.37 liquidity=21354166.0 spike=0.41
- KZPC.CA: score=9.22 buy_ready=False sector_rank=4 price=8.46 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=60.66 liquidity=1821549.75 spike=0.35
- LCSW.CA: score=21.4 buy_ready=False sector_rank=7 price=33.04 support=27.64 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=65.69 liquidity=11848733.0 spike=0.18
- LUTS.CA: score=5.93 buy_ready=False sector_rank=4 price=0.55 support=0.56 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=18.65 liquidity=5527227.0 spike=0.17
- MAAL.CA: score=15.73 buy_ready=False sector_rank=4 price=8.84 support=7.09 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=78.62 liquidity=7325409.0 spike=0.45
- MASR.CA: score=19.4 buy_ready=False sector_rank=4 price=7.89 support=7.24 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=62.68 liquidity=37469740.0 spike=0.44
- MBSC.CA: score=13.92 buy_ready=False sector_rank=7 price=243.0 support=230.0 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=53.17 liquidity=3521411.5 spike=0.19
- MCQE.CA: score=14.48 buy_ready=False sector_rank=7 price=180.01 support=168.05 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=56.94 liquidity=6079192.5 spike=0.34
- MCRO.CA: score=19.4 buy_ready=False sector_rank=4 price=1.48 support=1.19 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=85.71 liquidity=60428348.0 spike=0.45
- MENA.CA: score=9.91 buy_ready=False sector_rank=6 price=6.96 support=6.72 resistance=7.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=506156.59 spike=0.06
- MEPA.CA: score=21.4 buy_ready=False sector_rank=4 price=1.8 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=71.7 liquidity=17188214.0 spike=0.35
- MFPC.CA: score=17.14 buy_ready=False sector_rank=16 price=36.16 support=34.95 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=42.49 liquidity=53637572.0 spike=0.61
- MFSC.CA: score=7.71 buy_ready=False sector_rank=4 price=46.49 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:25 AM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=1312546.0 spike=0.23
- MHOT.CA: score=8.41 buy_ready=False sector_rank=19 price=16.5 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=50.38 liquidity=2983378.0 spike=0.26
- MICH.CA: score=18.6 buy_ready=False sector_rank=4 price=39.61 support=36.1 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=7198279.0 spike=0.44
- MILS.CA: score=24.86 buy_ready=False sector_rank=4 price=196.61 support=126.31 resistance=205.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=72.81 liquidity=78017944.0 spike=1.73
- MIPH.CA: score=11.9 buy_ready=False sector_rank=5 price=735.59 support=632.11 resistance=780.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=64.07 liquidity=495484.09 spike=0.14
- MOED.CA: score=15.4 buy_ready=False sector_rank=4 price=0.69 support=0.65 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=53.4 liquidity=12906715.0 spike=0.54
- MOIL.CA: score=10.48 buy_ready=False sector_rank=14 price=0.69 support=0.46 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=92.31 liquidity=631387.19 spike=0.87
- MOIN.CA: score=5.69 buy_ready=False sector_rank=4 price=23.6 support=22.66 resistance=24.76 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=46.41 liquidity=293159.2 spike=0.38
- MOSC.CA: score=15.6 buy_ready=False sector_rank=4 price=284.04 support=260.01 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=65.47 liquidity=4195146.0 spike=0.35
- MPCI.CA: score=20.4 buy_ready=False sector_rank=4 price=291.0 support=236.1 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=89.58 liquidity=43732628.0 spike=0.44
- MPCO.CA: score=24.4 buy_ready=False sector_rank=3 price=1.93 support=1.76 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=67.35 liquidity=66938264.0 spike=0.83
- MPRC.CA: score=15.87 buy_ready=False sector_rank=4 price=45.93 support=37.51 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=78.44 liquidity=5466516.5 spike=0.18
- MTIE.CA: score=20.86 buy_ready=False sector_rank=13 price=9.48 support=8.92 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=57.84 liquidity=16179745.0 spike=0.69
- NAHO.CA: score=5.41 buy_ready=False sector_rank=4 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=6086.54 spike=0.21
- NCCW.CA: score=18.4 buy_ready=False sector_rank=4 price=6.95 support=5.94 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=78.41 liquidity=17079066.0 spike=0.61
- NEDA.CA: score=8.11 buy_ready=False sector_rank=4 price=2.72 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=47.37 liquidity=1028032.17 spike=1.34
- NHPS.CA: score=20.73 buy_ready=False sector_rank=4 price=84.04 support=62.1 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=69.77 liquidity=9327204.0 spike=0.11
- NINH.CA: score=15.97 buy_ready=False sector_rank=4 price=21.52 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=76.48 liquidity=7568355.5 spike=0.17
- NIPH.CA: score=18.4 buy_ready=False sector_rank=5 price=223.0 support=160.55 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=79.42 liquidity=87831216.0 spike=0.56
- OBRI.CA: score=16.4 buy_ready=False sector_rank=4 price=32.98 support=32.4 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=39.48 liquidity=11409497.0 spike=0.27
- OCDI.CA: score=21.4 buy_ready=False sector_rank=6 price=27.98 support=24.31 resistance=29.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=62.34 liquidity=39498468.0 spike=0.41
- OCPH.CA: score=13.25 buy_ready=False sector_rank=4 price=452.8 support=348.0 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=83.04 liquidity=4846052.0 spike=0.2
- ODIN.CA: score=20.4 buy_ready=False sector_rank=4 price=2.71 support=2.07 resistance=2.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=79.17 liquidity=14201108.0 spike=0.78
- OFH.CA: score=21.4 buy_ready=False sector_rank=4 price=0.7 support=0.58 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=73.74 liquidity=14440715.0 spike=0.22
- OIH.CA: score=22.98 buy_ready=False sector_rank=10 price=1.47 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=73.33 liquidity=133609584.0 spike=1.93
- OLFI.CA: score=16.34 buy_ready=False sector_rank=18 price=22.66 support=21.91 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=56.11 liquidity=6873961.0 spike=0.2
- ORAS.CA: score=4.6 buy_ready=False sector_rank=17 price=712.76 support=702.05 resistance=719.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42259812.0 spike=1.0
- ORHD.CA: score=21.4 buy_ready=False sector_rank=6 price=38.92 support=37.52 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=58.77 liquidity=59262340.0 spike=0.4
- ORWE.CA: score=20.4 buy_ready=False sector_rank=2 price=22.61 support=22.2 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=54.81 liquidity=10069870.0 spike=0.41
- PHAR.CA: score=23.36 buy_ready=False sector_rank=5 price=98.19 support=84.2 resistance=97.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=80.84 liquidity=154925552.0 spike=2.48
- PHDC.CA: score=16.4 buy_ready=False sector_rank=6 price=14.5 support=14.41 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=46.41 liquidity=69383648.0 spike=0.29
- PHTV.CA: score=11.92 buy_ready=False sector_rank=4 price=319.9 support=260.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=83.89 liquidity=1515131.38 spike=0.31
- POUL.CA: score=8.08 buy_ready=False sector_rank=18 price=37.09 support=37.02 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=33.27 liquidity=8614007.0 spike=0.26
- PRCL.CA: score=16.05 buy_ready=False sector_rank=7 price=35.0 support=30.6 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=48.73 liquidity=6651201.0 spike=0.14
- PRDC.CA: score=21.4 buy_ready=False sector_rank=6 price=9.2 support=7.26 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=18831882.0 spike=0.16
- PRMH.CA: score=11.93 buy_ready=False sector_rank=4 price=2.59 support=2.45 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=5529700.0 spike=0.33
- RACC.CA: score=19.07 buy_ready=False sector_rank=4 price=9.98 support=9.55 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=54.59 liquidity=9665086.0 spike=0.44
- RAKT.CA: score=13.13 buy_ready=False sector_rank=4 price=23.16 support=21.25 resistance=23.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=55.6 liquidity=350085.78 spike=1.19
- RAYA.CA: score=14.24 buy_ready=False sector_rank=20 price=7.5 support=7.12 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=43.52 liquidity=29267828.0 spike=0.21
- RMDA.CA: score=21.4 buy_ready=False sector_rank=5 price=5.18 support=4.9 resistance=5.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=69.35 liquidity=15712834.0 spike=0.55
- ROTO.CA: score=15.14 buy_ready=False sector_rank=4 price=42.37 support=40.5 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=58.75 liquidity=5740651.5 spike=0.29
- RREI.CA: score=8.78 buy_ready=False sector_rank=4 price=4.65 support=4.57 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=119431936.0 spike=2.19
- RTVC.CA: score=10.73 buy_ready=False sector_rank=4 price=3.81 support=3.65 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=58.65 liquidity=2333026.75 spike=0.51
- RUBX.CA: score=14.57 buy_ready=False sector_rank=4 price=12.57 support=11.07 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=48.66 liquidity=5173025.5 spike=0.08
- SAUD.CA: score=12.85 buy_ready=False sector_rank=11 price=21.71 support=20.5 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=70.11 liquidity=6841091.0 spike=0.7
- SCEM.CA: score=18.4 buy_ready=False sector_rank=7 price=82.92 support=60.14 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=85.83 liquidity=42817136.0 spike=0.58
- SCFM.CA: score=21.58 buy_ready=False sector_rank=4 price=285.04 support=235.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=67.3 liquidity=27231828.0 spike=1.09
- SCTS.CA: score=13.66 buy_ready=False sector_rank=1 price=609.06 support=543.01 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=51.64 liquidity=1257338.75 spike=0.18
- SDTI.CA: score=20.4 buy_ready=False sector_rank=4 price=58.17 support=45.85 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=92.97 liquidity=10183410.0 spike=0.61
- SEIG.CA: score=13.76 buy_ready=False sector_rank=4 price=250.0 support=185.0 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=2364848.25 spike=0.1
- SIPC.CA: score=18.4 buy_ready=False sector_rank=4 price=3.88 support=3.27 resistance=4.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=84.27 liquidity=13053855.0 spike=0.54
- SKPC.CA: score=16.18 buy_ready=False sector_rank=16 price=15.78 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=44.95 liquidity=36021932.0 spike=1.02
- SMFR.CA: score=21.4 buy_ready=False sector_rank=4 price=239.41 support=191.02 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=65.78 liquidity=10596594.0 spike=0.51
- SNFC.CA: score=9.28 buy_ready=False sector_rank=4 price=11.06 support=11.04 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=43.98 liquidity=2879193.5 spike=0.25
- SPIN.CA: score=23.4 buy_ready=False sector_rank=2 price=15.52 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=68.14 liquidity=14785354.0 spike=0.6
- SPMD.CA: score=20.41 buy_ready=False sector_rank=4 price=0.45 support=0.42 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=61.97 liquidity=9011916.0 spike=0.33
- SUGR.CA: score=8.89 buy_ready=False sector_rank=18 price=46.54 support=46.01 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=54.27 liquidity=3423706.5 spike=0.63
- SVCE.CA: score=15.06 buy_ready=False sector_rank=4 price=9.16 support=8.9 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=56.48 liquidity=8663893.0 spike=0.16
- SWDY.CA: score=18.22 buy_ready=False sector_rank=9 price=92.52 support=85.11 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:29 AM market time freshness=DELAYED_CURRENT RSI=79.22 liquidity=11693929.0 spike=0.56
- TALM.CA: score=23.44 buy_ready=False sector_rank=1 price=17.64 support=15.27 resistance=19.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=87.76 liquidity=28951994.0 spike=1.02
- TMGH.CA: score=16.4 buy_ready=False sector_rank=6 price=96.41 support=92.6 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=131418384.0 spike=0.36
- TRTO.CA: score=7.4 buy_ready=False sector_rank=4 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-28T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- UEFM.CA: score=17.57 buy_ready=False sector_rank=4 price=549.64 support=467.2 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=74.27 liquidity=5787001.5 spike=1.19
- UEGC.CA: score=21.4 buy_ready=False sector_rank=4 price=2.28 support=1.36 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=73.08 liquidity=10285198.0 spike=0.19
- UNIP.CA: score=17.52 buy_ready=False sector_rank=4 price=0.38 support=0.32 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:28 AM market time freshness=DELAYED_CURRENT RSI=70.51 liquidity=6118273.5 spike=0.23
- UNIT.CA: score=10.48 buy_ready=False sector_rank=6 price=17.58 support=12.66 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=57.56 liquidity=1081909.0 spike=0.04
- WCDF.CA: score=14.91 buy_ready=False sector_rank=4 price=576.05 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:31 AM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=1506065.5 spike=0.48
- WKOL.CA: score=10.48 buy_ready=False sector_rank=4 price=353.8 support=311.0 resistance=363.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:33 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31546908.0 spike=3.04
- ZEOT.CA: score=20.78 buy_ready=False sector_rank=4 price=12.5 support=10.8 resistance=12.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=79.82 liquidity=35749808.0 spike=1.19
- ZMID.CA: score=18.4 buy_ready=False sector_rank=6 price=7.4 support=6.23 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:30 AM market time freshness=DELAYED_CURRENT RSI=76.54 liquidity=107836960.0 spike=0.42

## Backtesting Lite
- MILS.CA: 180d return=49.77%, max drawdown=-29.51%, MA20>MA50 days last20=15, as_of=2026-07-28T21:00:00+00:00
- MPCO.CA: 180d return=12.57%, max drawdown=-20.56%, MA20>MA50 days last20=20, as_of=2026-07-28T21:00:00+00:00
- AJWA.CA: 180d return=44.49%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-07-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MILS.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=North Cairo Flour Mills summary=North Cairo Mills stock hits historic peak amid clear emergence of buying power; North Cairo Mills approves EGP 0.5/shr dividends for FY19/20; North Cairo Mills reports 37% profit decline in FY19/20 initial results
  - North Cairo Mills stock hits historic peak amid clear emergence of buying power: https://english.mubasher.info/news/4540088/North-Cairo-Mills-stock-hits-historic-peak-amid-clear-emergence-of-buying-power/
  - North Cairo Mills approves EGP 0.5/shr dividends for FY19/20: https://english.mubasher.info/news/3726135/North-Cairo-Mills-approves-EGP-0-5-shr-dividends-for-FY19-20/
  - North Cairo Mills reports 37% profit decline in FY19/20 initial results: https://english.mubasher.info/news/3676432/North-Cairo-Mills-reports-37-profit-decline-in-FY19-20-initial-results/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=575 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- SPIN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Spinning and Weaving summary=Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- CEFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Middle Egypt Flour Mills summary=Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26; Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend; Middle Egypt Mills reports 23% profit drop in FY19/20
  - Middle Egypt Flour Mills posts lower net profits at EGP 77m in 9M-25/26: https://english.mubasher.info/news/4601809/Middle-Egypt-Flour-Mills-posts-lower-net-profits-at-EGP-77m-in-9M-25-26/
  - Middle Egypt Flour Mills shareholders approve EGP 3.25/shr dividend: https://english.mubasher.info/news/3870911/Middle-Egypt-Flour-Mills-shareholders-approve-EGP-3-25-shr-dividend/
  - Middle Egypt Mills reports 23% profit drop in FY19/20: https://english.mubasher.info/news/3703590/Middle-Egypt-Mills-reports-23-profit-drop-in-FY19-20/

## Warnings
- Evidence for MILS.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence rejected for SPIN.CA: source text did not clearly match SPIN.CA / Alexandria Spinning and Weaving.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence for CEFM.CA matches the company but no source/report date was detected.
