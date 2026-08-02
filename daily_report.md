# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-08-02T07:57:46.814261+00:00
Generated Cairo: 2026-08-02 10:57
Run timing: target 08:45 Cairo | generated Cairo 2026-08-02 10:57 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-08-02 10:52

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 177/189
- Top sector: Textiles

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, August 02
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 55.0% / above MA50 40.0%
- EGX70 regime: MIXED / above MA20 54.05% / above MA50 78.38%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- PHAR.CA: liquidity=288409696.0 spike=3.44 score=10.68
- AMOC.CA: liquidity=113103040.0 spike=1.44 score=6.66
- BIOC.CA: liquidity=112094936.0 spike=1.42 score=7.24
- AJWA.CA: liquidity=75489496.0 spike=2.4 score=26.2
- OCDI.CA: liquidity=54734200.0 spike=0.55 score=20.85

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 bearish, EGX70 mixed, sector breadth only 14% → defensive risk mode (no new buys). Scanner highlights AJWA.CA, MPCO.CA, EALR.CA as top watchlist due to bullish outlook scores, accumulation or tradeable liquidity, and clear support‑resistance gaps, but confidence stays low and liquidity cooling adds uncertainty for the next 1‑3 days.
- . It's okay to mention percentages as they are part of data.

Return JSON only.

Let's craft:

{
- AJWA.CA: accumulation spike, liquidity ~75M, outlook bullish watch (85), resistance ~9.9% above, RSI 63, sector General/Verified EGX Expansion.
- MPCO.CA: tradeable liquidity, cooling spike, outlook bullish watch (93), support 10.7% below, resistance 5.6% above, sector Agriculture & Food Production (rank 2).
- EALR.CA: tradeable liquidity, moderate spike, outlook bullish watch (77), support 20.8% below, resistance 5.8% above, sector General/Verified EGX Expansion.
- Market regime: EGX30 bearish (below MA50), EGX70 mixed, sector breadth weak → defensive_no_new_buy; uncertainty remains from cooling liquidity and mixed signals.

## Top Liquidity Spikes
- CFGH.CA: spike=111.4 liquidity=1921395.08 outlook=BULLISH_WATCH score=70.15 buy_ready=False
- TRTO.CA: spike=108.8 liquidity=146794.26 outlook=NEUTRAL score=37.15 buy_ready=False
- EOSB.CA: spike=7.81 liquidity=446389.14 outlook=CONSTRUCTIVE score=66.15 buy_ready=False
- PHAR.CA: spike=3.44 liquidity=288409696.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AJWA.CA: spike=2.4 liquidity=75489496.0 outlook=BULLISH_WATCH score=85.15 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=7.6 5d=-2.65% 20d=12.23% aboveMA50=100.0%
- #2 Agriculture & Food Production: score=6.7 5d=3.28% 20d=3.81% aboveMA50=50.0%
- #3 Building Materials: score=6.48 5d=-1.38% 20d=9.43% aboveMA50=83.33%
- #4 General / Verified EGX Expansion: score=6.15 5d=-0.51% 20d=10.24% aboveMA50=74.76%
- #5 Industrial Goods & Cables: score=4.88 5d=-2.34% 20d=5.51% aboveMA50=100.0%
- #6 Fintech & Payments: score=4.87 5d=-2.96% 20d=6.82% aboveMA50=50.0%
- #7 Telecommunications: score=4.64 5d=-0.45% 20d=6.8% aboveMA50=50.0%
- #8 Real Estate: score=4.63 5d=-2.7% 20d=9.63% aboveMA50=76.92%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=92.7 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=87.6 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARCC.CA: BULLISH_WATCH score=86.48 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MCQE.CA: BULLISH_WATCH score=86.48 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- AJWA.CA: BULLISH_WATCH score=85.15 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- LCSW.CA: BULLISH_WATCH score=82.48 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- ADPC.CA: BULLISH_WATCH score=82.15 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EHDR.CA: BULLISH_WATCH score=82.15 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- UEFM.CA: BULLISH_WATCH score=81.15 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=80.87 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=6.4 buy_ready=False sector_rank=4 price=291.15 support=279.0 resistance=308.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28667658.0 spike=0.97
- ABUK.CA: score=19.05 buy_ready=False sector_rank=17 price=73.9 support=67.73 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=59.64 liquidity=21159268.0 spike=0.13
- ACAMD.CA: score=18.23 buy_ready=False sector_rank=4 price=2.35 support=2.21 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=8832339.0 spike=0.12
- ACGC.CA: score=18.01 buy_ready=False sector_rank=1 price=10.71 support=9.15 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=68.12 liquidity=3609040.75 spike=0.12
- ADCI.CA: score=4.56 buy_ready=False sector_rank=4 price=265.94 support=256.0 resistance=266.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8164283.5 spike=0.8
- ADIB.CA: score=19.56 buy_ready=False sector_rank=12 price=52.93 support=46.0 resistance=52.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=79.01 liquidity=17922948.0 spike=0.13
- ADPC.CA: score=14.83 buy_ready=False sector_rank=4 price=3.86 support=3.45 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=1427111.0 spike=0.04
- AFDI.CA: score=16.65 buy_ready=False sector_rank=4 price=53.0 support=43.77 resistance=52.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=71.27 liquidity=5251449.0 spike=0.29
- AFMC.CA: score=6.4 buy_ready=False sector_rank=4 price=199.32 support=184.78 resistance=221.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=52170792.0 spike=0.67
- AJWA.CA: score=26.2 buy_ready=False sector_rank=4 price=191.12 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 July 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.35 liquidity=75489496.0 spike=2.4
- ALCN.CA: score=12.21 buy_ready=False sector_rank=15 price=29.4 support=28.2 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=1890693.75 spike=0.08
- ALUM.CA: score=10.07 buy_ready=False sector_rank=4 price=22.9 support=21.1 resistance=24.09 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=49.17 liquidity=1670967.17 spike=0.28
- AMER.CA: score=13.16 buy_ready=False sector_rank=8 price=4.51 support=2.4 resistance=4.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=82.38 liquidity=5312821.5 spike=0.05
- AMES.CA: score=17.46 buy_ready=False sector_rank=4 price=122.38 support=57.5 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=65.57 liquidity=6064662.0 spike=0.06
- AMIA.CA: score=8.75 buy_ready=False sector_rank=4 price=11.35 support=8.62 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=75.38 liquidity=350761.81 spike=0.02
- AMOC.CA: score=6.66 buy_ready=False sector_rank=10 price=9.58 support=9.16 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=113103040.0 spike=1.44
- APSW.CA: score=13.09 buy_ready=False sector_rank=4 price=8.75 support=8.1 resistance=9.34 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=56.12 liquidity=685133.75 spike=0.45
- ARAB.CA: score=18.85 buy_ready=False sector_rank=8 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=12258747.0 spike=0.09
- ARCC.CA: score=17.4 buy_ready=False sector_rank=3 price=56.3 support=54.2 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=50.72 liquidity=2999846.0 spike=0.11
- AREH.CA: score=2.66 buy_ready=False sector_rank=4 price=1.43 support=1.38 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:29 AM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=1255121.25 spike=0.05
- ARVA.CA: score=8.4 buy_ready=False sector_rank=4 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=81.59 liquidity=0.0 spike=0.0
- ASCM.CA: score=12.62 buy_ready=False sector_rank=4 price=63.0 support=57.25 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=3224928.0 spike=0.06
- ASPI.CA: score=15.74 buy_ready=False sector_rank=4 price=0.42 support=0.31 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=7338333.0 spike=0.19
- ATLC.CA: score=13.91 buy_ready=False sector_rank=11 price=5.25 support=5.0 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=3280153.0 spike=0.49
- ATQA.CA: score=14.8 buy_ready=False sector_rank=17 price=9.87 support=9.43 resistance=10.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=2748350.75 spike=0.07
- AXPH.CA: score=11.95 buy_ready=False sector_rank=4 price=1227.3 support=1090.02 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=552186.5 spike=0.14
- BINV.CA: score=13.02 buy_ready=False sector_rank=13 price=47.46 support=45.97 resistance=51.35 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=46.06 liquidity=4498733.31 spike=0.62
- BIOC.CA: score=7.24 buy_ready=False sector_rank=4 price=271.7 support=241.15 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=112094936.0 spike=1.42
- BTFH.CA: score=22.63 buy_ready=False sector_rank=11 price=3.09 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=16843756.0 spike=0.08
- CAED.CA: score=14.14 buy_ready=False sector_rank=4 price=127.73 support=71.0 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=75.25 liquidity=5737282.0 spike=0.08
- CANA.CA: score=14.13 buy_ready=False sector_rank=12 price=38.12 support=35.2 resistance=39.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=55.24 liquidity=1565173.88 spike=0.09
- CCAP.CA: score=15.52 buy_ready=False sector_rank=13 price=5.22 support=4.76 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=48.04 liquidity=44247012.0 spike=0.06
- CCRS.CA: score=11.72 buy_ready=False sector_rank=4 price=2.54 support=2.26 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:24 AM market time freshness=DELAYED_CURRENT RSI=64.38 liquidity=317815.56 spike=0.02
- CEFM.CA: score=21.4 buy_ready=False sector_rank=4 price=139.36 support=98.3 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=70.8 liquidity=13869327.0 spike=0.53
- CERA.CA: score=10.35 buy_ready=False sector_rank=4 price=1.28 support=1.21 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=952197.69 spike=0.04
- CFGH.CA: score=14.32 buy_ready=False sector_rank=4 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 July 12:18 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=1921395.08 spike=111.4
- CICH.CA: score=13.76 buy_ready=False sector_rank=11 price=12.29 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=1131179.0 spike=0.21
- CIEB.CA: score=6.2 buy_ready=False sector_rank=12 price=23.8 support=23.55 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=38.99 liquidity=639285.38 spike=0.07
- CIRA.CA: score=15.52 buy_ready=False sector_rank=14 price=35.59 support=28.04 resistance=36.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=74.85 liquidity=5090638.0 spike=0.09
- CLHO.CA: score=12.64 buy_ready=False sector_rank=9 price=16.7 support=15.98 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=1842355.0 spike=0.04
- CNFN.CA: score=9.58 buy_ready=False sector_rank=11 price=4.79 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=955747.94 spike=0.05
- COMI.CA: score=20.56 buy_ready=False sector_rank=12 price=141.65 support=127.25 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=24845996.0 spike=0.06
- COPR.CA: score=13.8 buy_ready=False sector_rank=4 price=0.41 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=3401658.75 spike=0.11
- COSG.CA: score=12.34 buy_ready=False sector_rank=4 price=1.64 support=1.5 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=2944219.75 spike=0.07
- CPCI.CA: score=9.81 buy_ready=False sector_rank=4 price=465.68 support=393.0 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=70.5 liquidity=409702.81 spike=0.04
- CSAG.CA: score=9.79 buy_ready=False sector_rank=15 price=32.0 support=31.35 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=41.21 liquidity=1470119.88 spike=0.1
- DAPH.CA: score=12.84 buy_ready=False sector_rank=4 price=97.42 support=81.0 resistance=99.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=72.04 liquidity=1439699.88 spike=0.08
- DEIN.CA: score=-3.6 buy_ready=False sector_rank=4 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=9.54 buy_ready=False sector_rank=19 price=26.55 support=26.35 resistance=27.83 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=42.28 liquidity=2266626.53 spike=0.71
- DSCW.CA: score=12.76 buy_ready=False sector_rank=4 price=1.96 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=4364662.5 spike=0.08
- DTPP.CA: score=21.15 buy_ready=False sector_rank=4 price=250.07 support=183.0 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=66.53 liquidity=9751739.0 spike=0.12
- EALR.CA: score=23.4 buy_ready=False sector_rank=4 price=408.32 support=338.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=21931798.0 spike=0.81
- EASB.CA: score=10.06 buy_ready=False sector_rank=4 price=7.29 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=53.1 liquidity=663012.75 spike=0.05
- EAST.CA: score=5.47 buy_ready=False sector_rank=19 price=36.33 support=36.01 resistance=37.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=44.1 liquidity=2200014.75 spike=0.03
- EBSC.CA: score=11.01 buy_ready=False sector_rank=4 price=1.87 support=1.74 resistance=2.25 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=36.36 liquidity=1608583.35 spike=0.19
- ECAP.CA: score=9.7 buy_ready=False sector_rank=4 price=32.82 support=32.12 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=302255.06 spike=0.05
- EDFM.CA: score=12.59 buy_ready=False sector_rank=4 price=392.36 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=72.34 liquidity=1187958.63 spike=0.23
- EEII.CA: score=5.17 buy_ready=False sector_rank=4 price=2.62 support=2.47 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=30.61 liquidity=766008.13 spike=0.03
- EFIC.CA: score=9.78 buy_ready=False sector_rank=17 price=199.94 support=180.07 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=66.48 liquidity=735508.5 spike=0.04
- EFID.CA: score=2.56 buy_ready=False sector_rank=19 price=27.12 support=26.64 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=34.41 liquidity=3290325.25 spike=0.07
- EFIH.CA: score=22.78 buy_ready=False sector_rank=6 price=22.67 support=20.3 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=55.13 liquidity=9827228.0 spike=0.15
- EGAL.CA: score=11.48 buy_ready=False sector_rank=17 price=297.09 support=283.03 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=4427538.0 spike=0.11
- EGAS.CA: score=20.78 buy_ready=False sector_rank=10 price=54.1 support=48.5 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=68.21 liquidity=10753731.0 spike=0.79
- EGBE.CA: score=9.3 buy_ready=False sector_rank=12 price=0.48 support=-0.34 resistance=0.49 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=96.7 liquidity=124468.86 spike=1.81
- EGCH.CA: score=16.19 buy_ready=False sector_rank=17 price=13.01 support=12.24 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=9144296.0 spike=0.15
- EGSA.CA: score=0.86 buy_ready=False sector_rank=7 price=8.87 support=8.67 resistance=9.21 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=27.66 liquidity=8870.0 spike=0.48
- EGTS.CA: score=4.39 buy_ready=False sector_rank=8 price=17.39 support=17.15 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=34.58 liquidity=3535437.25 spike=0.08
- EHDR.CA: score=14.76 buy_ready=False sector_rank=4 price=2.78 support=2.49 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=3363878.0 spike=0.08
- EKHO.CA: score=4.78 buy_ready=False sector_rank=10 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=12.28 buy_ready=False sector_rank=5 price=2.16 support=2.08 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=4332505.5 spike=0.06
- ELKA.CA: score=19.4 buy_ready=False sector_rank=4 price=1.72 support=1.35 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=11755148.0 spike=0.15
- ELNA.CA: score=9.22 buy_ready=False sector_rank=4 price=37.54 support=37.0 resistance=40.5 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.76 liquidity=1457190.22 spike=2.18
- ELSH.CA: score=18.89 buy_ready=False sector_rank=4 price=13.66 support=11.53 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=42.8 liquidity=9490624.0 spike=0.06
- ELWA.CA: score=2.2 buy_ready=False sector_rank=4 price=1.75 support=1.74 resistance=2.14 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=26.19 liquidity=801318.0 spike=0.53
- EMFD.CA: score=7.66 buy_ready=False sector_rank=8 price=11.3 support=11.08 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=26.62 liquidity=6803323.5 spike=0.12
- ENGC.CA: score=12.85 buy_ready=False sector_rank=4 price=41.2 support=36.31 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=59.04 liquidity=1453899.0 spike=0.06
- EOSB.CA: score=20.85 buy_ready=False sector_rank=4 price=1.55 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=446389.14 spike=7.81
- EPCO.CA: score=13.45 buy_ready=False sector_rank=4 price=10.8 support=8.57 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=70.67 liquidity=2046304.13 spike=0.07
- EPPK.CA: score=11.58 buy_ready=False sector_rank=4 price=15.07 support=13.52 resistance=15.93 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=61.16 liquidity=181246.89 spike=0.17
- ETEL.CA: score=20.86 buy_ready=False sector_rank=7 price=105.58 support=92.02 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=67.21 liquidity=11750975.0 spike=0.13
- ETRS.CA: score=17.5 buy_ready=False sector_rank=4 price=10.6 support=10.1 resistance=10.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=49.99 liquidity=6104410.5 spike=0.15
- EXPA.CA: score=11.14 buy_ready=False sector_rank=12 price=20.09 support=18.18 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=83.57 liquidity=1579105.88 spike=0.05
- FAIT.CA: score=6.74 buy_ready=False sector_rank=12 price=36.55 support=36.1 resistance=38.0 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=42.94 liquidity=1176800.33 spike=0.47
- FAITA.CA: score=0.57 buy_ready=False sector_rank=12 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:18 AM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=8412.81 spike=0.2
- FERC.CA: score=4.41 buy_ready=False sector_rank=17 price=76.15 support=73.45 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=363720.63 spike=0.03
- FWRY.CA: score=17.95 buy_ready=False sector_rank=6 price=19.1 support=18.28 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=38.43 liquidity=12546973.0 spike=0.1
- GBCO.CA: score=9.8 buy_ready=False sector_rank=16 price=30.03 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=42.99 liquidity=1696035.25 spike=0.03
- GDWA.CA: score=13.06 buy_ready=False sector_rank=4 price=0.81 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=56.77 liquidity=4661367.5 spike=0.04
- GGCC.CA: score=9.17 buy_ready=False sector_rank=4 price=0.84 support=0.48 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=76.99 liquidity=765343.69 spike=0.02
- GIHD.CA: score=20.62 buy_ready=False sector_rank=4 price=58.96 support=41.71 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=59.67 liquidity=7218460.0 spike=0.14
- GMCI.CA: score=9.74 buy_ready=False sector_rank=4 price=1.97 support=1.75 resistance=2.26 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=40.68 liquidity=336481.91 spike=0.27
- GRCA.CA: score=12.83 buy_ready=False sector_rank=4 price=59.43 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=70.56 liquidity=1429366.88 spike=0.08
- GSSC.CA: score=13.09 buy_ready=False sector_rank=4 price=282.12 support=241.32 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=71.0 liquidity=1690609.13 spike=0.12
- GTWL.CA: score=16.4 buy_ready=False sector_rank=4 price=102.39 support=82.2 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=33.45 liquidity=10982990.0 spike=0.08
- HDBK.CA: score=16.06 buy_ready=False sector_rank=12 price=83.59 support=76.9 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=63.36 liquidity=7504971.5 spike=0.17
- HELI.CA: score=16.76 buy_ready=False sector_rank=8 price=8.23 support=6.41 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=73.26 liquidity=5908370.5 spike=0.03
- HRHO.CA: score=9.33 buy_ready=False sector_rank=11 price=26.4 support=25.95 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=4698901.0 spike=0.05
- ICID.CA: score=21.99 buy_ready=False sector_rank=4 price=8.1 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:26 AM market time freshness=DELAYED_CURRENT RSI=54.31 liquidity=9886003.0 spike=1.35
- IDRE.CA: score=14.19 buy_ready=False sector_rank=4 price=47.7 support=42.22 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=53.68 liquidity=793963.13 spike=0.03
- IFAP.CA: score=12.9 buy_ready=False sector_rank=2 price=19.51 support=18.96 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=47.59 liquidity=498551.16 spike=0.05
- INFI.CA: score=17.94 buy_ready=False sector_rank=4 price=110.49 support=91.01 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=71.07 liquidity=6544858.5 spike=0.36
- IRON.CA: score=-0.02 buy_ready=False sector_rank=17 price=30.44 support=30.14 resistance=32.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=2.83 liquidity=930639.94 spike=0.15
- ISMA.CA: score=12.22 buy_ready=False sector_rank=4 price=30.85 support=26.54 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=69.1 liquidity=817779.25 spike=0.03
- ISMQ.CA: score=15.82 buy_ready=False sector_rank=17 price=9.04 support=8.96 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=7773851.0 spike=0.08
- ISPH.CA: score=12.24 buy_ready=False sector_rank=9 price=11.5 support=11.2 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=6445114.5 spike=0.13
- JUFO.CA: score=1.69 buy_ready=False sector_rank=19 price=29.0 support=28.48 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=19.95 liquidity=2421776.0 spike=0.09
- KABO.CA: score=15.41 buy_ready=False sector_rank=1 price=7.96 support=6.26 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=64.41 liquidity=1010808.88 spike=0.02
- KWIN.CA: score=16.7 buy_ready=False sector_rank=4 price=97.63 support=66.1 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=83.46 liquidity=8299445.0 spike=0.16
- KZPC.CA: score=11.32 buy_ready=False sector_rank=4 price=8.5 support=8.26 resistance=8.78 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=54.41 liquidity=3918321.5 spike=0.75
- LCSW.CA: score=19.36 buy_ready=False sector_rank=3 price=34.08 support=28.38 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=61.64 liquidity=4962638.5 spike=0.07
- LUTS.CA: score=1.99 buy_ready=False sector_rank=4 price=0.56 support=0.54 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=13.29 liquidity=1592764.38 spike=0.05
- MAAL.CA: score=10.14 buy_ready=False sector_rank=4 price=8.75 support=7.13 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=74.47 liquidity=737068.0 spike=0.04
- MASR.CA: score=16.97 buy_ready=False sector_rank=4 price=7.92 support=7.24 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=7573807.5 spike=0.09
- MBSC.CA: score=13.06 buy_ready=False sector_rank=3 price=243.54 support=231.51 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=44.96 liquidity=1655891.88 spike=0.09
- MCQE.CA: score=16.8 buy_ready=False sector_rank=3 price=186.73 support=170.0 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=55.32 liquidity=2397301.5 spike=0.13
- MCRO.CA: score=18.4 buy_ready=False sector_rank=4 price=1.54 support=1.2 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=32607854.0 spike=0.24
- MENA.CA: score=9.63 buy_ready=False sector_rank=8 price=6.92 support=6.74 resistance=7.59 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.67 liquidity=781281.85 spike=0.1
- MEPA.CA: score=19.16 buy_ready=False sector_rank=4 price=1.84 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=5755241.0 spike=0.11
- MFPC.CA: score=19.05 buy_ready=False sector_rank=17 price=37.25 support=35.19 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=47.34 liquidity=16370903.0 spike=0.18
- MFSC.CA: score=9.52 buy_ready=False sector_rank=4 price=47.11 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=1123538.63 spike=0.2
- MHOT.CA: score=6.1 buy_ready=False sector_rank=20 price=16.41 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=1592867.38 spike=0.14
- MICH.CA: score=18.7 buy_ready=False sector_rank=4 price=42.03 support=37.46 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=5302480.5 spike=0.32
- MILS.CA: score=21.4 buy_ready=False sector_rank=4 price=196.35 support=128.91 resistance=211.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=70.81 liquidity=14671764.0 spike=0.29
- MIPH.CA: score=11.82 buy_ready=False sector_rank=9 price=740.09 support=650.0 resistance=780.0 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=64.9 liquidity=1028725.14 spike=0.3
- MOED.CA: score=11.97 buy_ready=False sector_rank=4 price=0.66 support=0.68 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=6571978.5 spike=0.26
- MOIL.CA: score=9.8 buy_ready=False sector_rank=10 price=0.68 support=0.47 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=92.15 liquidity=16299.67 spike=0.02
- MOIN.CA: score=5.56 buy_ready=False sector_rank=4 price=23.6 support=23.03 resistance=24.76 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=51.08 liquidity=158686.4 spike=0.3
- MOSC.CA: score=15.08 buy_ready=False sector_rank=4 price=292.02 support=260.01 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=62.23 liquidity=1681431.5 spike=0.14
- MPCI.CA: score=18.4 buy_ready=False sector_rank=4 price=294.72 support=237.12 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=84.45 liquidity=11544358.0 spike=0.12
- MPCO.CA: score=25.4 buy_ready=False sector_rank=2 price=1.96 support=1.77 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=53.66 liquidity=10106072.0 spike=0.12
- MPRC.CA: score=13.25 buy_ready=False sector_rank=4 price=45.33 support=37.51 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=62.11 liquidity=1854535.75 spike=0.06
- MTIE.CA: score=12.15 buy_ready=False sector_rank=16 price=9.55 support=9.09 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=2042282.5 spike=0.08
- NAHO.CA: score=5.41 buy_ready=False sector_rank=4 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9132.01 spike=0.36
- NCCW.CA: score=15.2 buy_ready=False sector_rank=4 price=7.0 support=6.01 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=70.49 liquidity=3802709.75 spike=0.13
- NEDA.CA: score=6.72 buy_ready=False sector_rank=4 price=2.74 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=319884.04 spike=0.41
- NHPS.CA: score=14.63 buy_ready=False sector_rank=4 price=83.99 support=67.0 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=3234223.75 spike=0.04
- NINH.CA: score=15.55 buy_ready=False sector_rank=4 price=22.34 support=17.4 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=71.97 liquidity=4149383.5 spike=0.1
- NIPH.CA: score=17.8 buy_ready=False sector_rank=9 price=228.77 support=165.0 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=77.86 liquidity=29126664.0 spike=0.18
- OBRI.CA: score=4.44 buy_ready=False sector_rank=4 price=32.81 support=32.2 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=24.17 liquidity=3042996.5 spike=0.07
- OCDI.CA: score=20.85 buy_ready=False sector_rank=8 price=28.53 support=24.46 resistance=29.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:29 AM market time freshness=DELAYED_CURRENT RSI=60.81 liquidity=54734200.0 spike=0.55
- OCPH.CA: score=12.2 buy_ready=False sector_rank=4 price=471.08 support=350.6 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=82.68 liquidity=3797880.5 spike=0.15
- ODIN.CA: score=6.64 buy_ready=False sector_rank=4 price=2.96 support=2.84 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22329850.0 spike=1.12
- OFH.CA: score=13.26 buy_ready=False sector_rank=4 price=0.71 support=0.59 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=66.49 liquidity=1859465.62 spike=0.03
- OIH.CA: score=22.52 buy_ready=False sector_rank=13 price=1.47 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=18056172.0 spike=0.24
- OLFI.CA: score=8.48 buy_ready=False sector_rank=19 price=22.81 support=21.91 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=47.3 liquidity=1208336.13 spike=0.04
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=711.08 support=708.0 resistance=714.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13236950.0 spike=1.0
- ORHD.CA: score=16.0 buy_ready=False sector_rank=8 price=39.54 support=37.76 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=5151407.5 spike=0.04
- ORWE.CA: score=22.36 buy_ready=False sector_rank=1 price=22.99 support=22.2 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:33 AM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=7960464.5 spike=0.32
- PHAR.CA: score=10.68 buy_ready=False sector_rank=9 price=124.8 support=104.2 resistance=124.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=288409696.0 spike=3.44
- PHDC.CA: score=14.63 buy_ready=False sector_rank=8 price=14.44 support=14.32 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=8778057.0 spike=0.04
- PHTV.CA: score=11.48 buy_ready=False sector_rank=4 price=321.35 support=260.0 resistance=329.0 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=73.12 liquidity=2080098.59 spike=0.43
- POUL.CA: score=4.68 buy_ready=False sector_rank=19 price=38.0 support=36.5 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=2408922.25 spike=0.07
- PRCL.CA: score=13.84 buy_ready=False sector_rank=3 price=35.5 support=30.83 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=3437158.25 spike=0.07
- PRDC.CA: score=20.84 buy_ready=False sector_rank=8 price=9.3 support=7.4 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=55.01 liquidity=9990062.0 spike=0.08
- PRMH.CA: score=6.94 buy_ready=False sector_rank=4 price=2.6 support=2.48 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=537903.31 spike=0.03
- RACC.CA: score=12.1 buy_ready=False sector_rank=4 price=10.03 support=9.65 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=2697097.0 spike=0.12
- RAKT.CA: score=12.63 buy_ready=False sector_rank=4 price=22.53 support=21.25 resistance=23.7 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=53.46 liquidity=693563.54 spike=2.27
- RAYA.CA: score=6.97 buy_ready=False sector_rank=21 price=7.53 support=7.3 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=3669111.0 spike=0.03
- RMDA.CA: score=22.4 buy_ready=False sector_rank=9 price=5.38 support=4.91 resistance=5.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=71.64 liquidity=54491172.0 spike=1.8
- ROTO.CA: score=11.91 buy_ready=False sector_rank=4 price=43.11 support=40.5 resistance=45.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=51.49 liquidity=505971.19 spike=0.03
- RREI.CA: score=17.01 buy_ready=False sector_rank=4 price=4.65 support=3.45 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=71.0 liquidity=5613207.0 spike=0.09
- RTVC.CA: score=6.94 buy_ready=False sector_rank=4 price=3.82 support=3.7 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=538279.06 spike=0.11
- RUBX.CA: score=10.97 buy_ready=False sector_rank=4 price=12.54 support=11.22 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=42.57 liquidity=1572820.38 spike=0.02
- SAUD.CA: score=16.72 buy_ready=False sector_rank=12 price=21.66 support=21.01 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=54.51 liquidity=9157186.0 spike=0.92
- SCEM.CA: score=19.4 buy_ready=False sector_rank=3 price=81.22 support=61.28 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=75.59 liquidity=41365892.0 spike=0.53
- SCFM.CA: score=23.4 buy_ready=False sector_rank=4 price=290.04 support=237.08 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=60.42 liquidity=10567060.0 spike=0.4
- SCTS.CA: score=10.6 buy_ready=False sector_rank=14 price=608.31 support=599.0 resistance=649.0 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=47.65 liquidity=2167408.52 spike=0.36
- SDTI.CA: score=10.93 buy_ready=False sector_rank=4 price=59.05 support=46.0 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=83.8 liquidity=2532119.25 spike=0.14
- SEIG.CA: score=17.55 buy_ready=False sector_rank=4 price=264.87 support=186.05 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=6154867.0 spike=0.23
- SIPC.CA: score=6.4 buy_ready=False sector_rank=4 price=4.31 support=3.99 resistance=4.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22549890.0 spike=0.89
- SKPC.CA: score=11.57 buy_ready=False sector_rank=17 price=15.86 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=43.31 liquidity=5521055.5 spike=0.15
- SMFR.CA: score=12.24 buy_ready=False sector_rank=4 price=235.26 support=193.0 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=66.77 liquidity=839486.88 spike=0.04
- SNFC.CA: score=3.86 buy_ready=False sector_rank=4 price=11.0 support=11.01 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=12.03 liquidity=2464926.0 spike=0.22
- SPIN.CA: score=18.79 buy_ready=False sector_rank=1 price=15.99 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=68.35 liquidity=4391664.5 spike=0.17
- SPMD.CA: score=21.4 buy_ready=False sector_rank=4 price=0.47 support=0.43 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=11265436.0 spike=0.41
- SUGR.CA: score=6.14 buy_ready=False sector_rank=19 price=46.51 support=46.47 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=42.02 liquidity=863150.13 spike=0.16
- SVCE.CA: score=7.32 buy_ready=False sector_rank=4 price=9.24 support=8.96 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=28.05 liquidity=2919443.25 spike=0.05
- SWDY.CA: score=15.66 buy_ready=False sector_rank=5 price=93.76 support=86.1 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:30 AM market time freshness=DELAYED_CURRENT RSI=65.15 liquidity=4708889.0 spike=0.22
- TALM.CA: score=5.43 buy_ready=False sector_rank=14 price=18.48 support=18.3 resistance=18.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25889754.0 spike=0.8
- TMGH.CA: score=18.85 buy_ready=False sector_rank=8 price=97.54 support=94.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=50.6 liquidity=20389718.0 spike=0.06
- TRTO.CA: score=12.55 buy_ready=False sector_rank=4 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 July 11:46 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=146794.26 spike=108.8
- UEFM.CA: score=21.81 buy_ready=False sector_rank=4 price=537.5 support=473.0 resistance=625.0 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=58.21 liquidity=7533062.5 spike=1.44
- UEGC.CA: score=14.25 buy_ready=False sector_rank=4 price=2.36 support=1.41 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=70.87 liquidity=2845367.0 spike=0.05
- UNIP.CA: score=14.37 buy_ready=False sector_rank=4 price=0.38 support=0.32 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=971518.44 spike=0.03
- UNIT.CA: score=4.42 buy_ready=False sector_rank=8 price=17.76 support=12.8 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:27 AM market time freshness=DELAYED_CURRENT RSI=21.87 liquidity=568912.38 spike=0.02
- WCDF.CA: score=12.95 buy_ready=False sector_rank=4 price=588.26 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=1552630.38 spike=0.48
- WKOL.CA: score=6.94 buy_ready=False sector_rank=4 price=347.18 support=332.5 resistance=363.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22125446.0 spike=1.27
- ZEOT.CA: score=16.05 buy_ready=False sector_rank=4 price=12.41 support=10.81 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:35 AM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=4653639.0 spike=0.15
- ZMID.CA: score=20.85 buy_ready=False sector_rank=8 price=7.24 support=6.47 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=57.92 liquidity=15380288.0 spike=0.06

## Backtesting Lite
- AJWA.CA: 180d return=45.38%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-07-29T21:00:00+00:00
- MPCO.CA: 180d return=14.12%, max drawdown=-20.56%, MA20>MA50 days last20=20, as_of=2026-07-29T21:00:00+00:00
- EALR.CA: 180d return=20.65%, max drawdown=-26.75%, MA20>MA50 days last20=5, as_of=2026-07-29T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=578 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- EALR.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Company For Land Reclamation summary=El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23; El Arabia for Land Reclamation starts work on Bahariya Oasis project; El Arabia for Land Reclamation H1 losses down 16%
  - El Arabia for Land Reclamation targets EGP 2.5m profits in FY22/23: https://english.mubasher.info/news/3938373/El-Arabia-for-Land-Reclamation-targets-EGP-2-5m-profits-in-FY22-23/
  - El Arabia for Land Reclamation starts work on Bahariya Oasis project: https://english.mubasher.info/news/3493569/El-Arabia-for-Land-Reclamation-starts-work-on-Bahariya-Oasis-project/
  - El Arabia for Land Reclamation H1 losses down 16%: https://english.mubasher.info/news/3058199/El-Arabia-for-Land-Reclamation-H1-losses-down-16-/
- SCFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=South Cairo and Giza Flour Mills and Bakeries Company summary=South Cairo and Giza Mills targets over EGP 412.5m revenues in FY26/27; South Cairo and Giza Mills turns profitable in 8M-25/26; South Cairo and Giza Mills sells asset for EGP 17m
  - South Cairo and Giza Mills targets over EGP 412.5m revenues in FY26/27: https://english.mubasher.info/news/4583387/South-Cairo-and-Giza-Mills-targets-over-EGP-412-5m-revenues-in-FY26-27/
  - South Cairo and Giza Mills turns profitable in 8M-25/26: https://english.mubasher.info/news/4583237/South-Cairo-and-Giza-Mills-turns-profitable-in-8M-25-26/
  - South Cairo and Giza Mills sells asset for EGP 17m: https://english.mubasher.info/news/4547145/South-Cairo-and-Giza-Mills-sells-asset-for-EGP-17m/
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- BTFH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Beltone Holding summary=Evidence rejected for BTFH.CA: source text did not clearly match BTFH.CA / Beltone Holding.
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.

## Warnings
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for EALR.CA matches the company but no source/report date was detected.
- Evidence for SCFM.CA matches the company but no source/report date was detected.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for BTFH.CA: source text did not clearly match BTFH.CA / Beltone Holding.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
