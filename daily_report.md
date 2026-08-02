# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-08-02T08:40:42.635384+00:00
Generated Cairo: 2026-08-02 11:40
Run timing: target 09:15 Cairo | generated Cairo 2026-08-02 11:40 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-08-02 11:35

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 1
- Tradeable price/liquidity tickers: 173/189
- Top sector: Building Materials

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, August 02
- Freshness: DELAYED
- EGX30 regime: MIXED / above MA20 55.0% / above MA50 50.0%
- EGX70 regime: MIXED / above MA20 59.46% / above MA50 78.38%
- Sector breadth: 14.29%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- PHAR.CA: liquidity=333910848.0 spike=3.98 score=10.64
- BIOC.CA: liquidity=203312000.0 spike=2.57 score=9.45
- AMOC.CA: liquidity=149498912.0 spike=1.91 score=7.96
- RMDA.CA: liquidity=118095648.0 spike=3.89 score=25.64
- AFMC.CA: liquidity=113312320.0 spike=1.46 score=7.23

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: Scanner issued HOLD for all tickets because EGX30 and EGX70 show mixed trends, sector breadth is weak at 14.29%, and risk mode is defensive (no new buys); prioritized tickets display accumulation spikes and bullish‑watch outlooks but also cooling liquidity and extended momentum, creating uncertainty for the next 1‑3 days.
- CICH.CA, AJWA.CA, RMDA.CA: accumulation spikes (liquidity_spike 2.4‑3.9) with bullish‑watch outlooks, yet RSI 62‑71 signals extended momentum.
- MPCO.CA, LCSW.CA, EFIH.CA: tradeable liquidity regimes, cooling spikes (0.11‑0.27) and support/resistance gaps limiting near‑term upside.
- Leading sectors are Building Materials, Textiles, Agriculture & Food Production, but overall breadth remains low (14.29%) and EGX30/EGX70 stay mixed, keeping risk defensive.
- Mixed index trends and weak breadth imply near‑term moves are uncertain; await liquidity shifts or breadth improvement before considering new buys.

## Top Liquidity Spikes
- CFGH.CA: spike=111.4 liquidity=1921395.08 outlook=CONSTRUCTIVE score=69.77 buy_ready=False
- TRTO.CA: spike=108.8 liquidity=146794.26 outlook=NEUTRAL score=36.77 buy_ready=False
- EOSB.CA: spike=7.81 liquidity=446389.14 outlook=CONSTRUCTIVE score=65.77 buy_ready=False
- ADCI.CA: spike=5.09 liquidity=51920748.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- PHAR.CA: spike=3.98 liquidity=333910848.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=7.06 5d=-1.38% 20d=9.43% aboveMA50=83.33%
- #2 Textiles: score=6.98 5d=-2.65% 20d=12.23% aboveMA50=75.0%
- #3 Agriculture & Food Production: score=6.81 5d=3.28% 20d=3.81% aboveMA50=50.0%
- #4 Fintech & Payments: score=6.49 5d=-2.96% 20d=6.82% aboveMA50=100.0%
- #5 General / Verified EGX Expansion: score=5.77 5d=-0.49% 20d=8.76% aboveMA50=69.9%
- #6 Energy & Petrochemicals: score=5.34 5d=0.52% 20d=3.21% aboveMA50=50.0%
- #7 Industrial Goods & Cables: score=5.11 5d=-2.34% 20d=5.51% aboveMA50=100.0%
- #8 Telecommunications: score=4.96 5d=-0.45% 20d=6.8% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MPCO.CA: BULLISH_WATCH score=92.81 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MCQE.CA: BULLISH_WATCH score=87.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARCC.CA: BULLISH_WATCH score=87.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- PRCL.CA: BULLISH_WATCH score=87.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- IFAP.CA: BULLISH_WATCH score=86.81 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ATLC.CA: BULLISH_WATCH score=86.16 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- AJWA.CA: BULLISH_WATCH score=84.77 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- LCSW.CA: BULLISH_WATCH score=83.06 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- EFIH.CA: BULLISH_WATCH score=82.49 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EHDR.CA: BULLISH_WATCH score=81.77 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=8.45 buy_ready=False sector_rank=5 price=310.6 support=279.0 resistance=314.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60915884.0 spike=2.07
- ABUK.CA: score=19.36 buy_ready=False sector_rank=16 price=74.41 support=67.73 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=59.64 liquidity=54341164.0 spike=0.35
- ACAMD.CA: score=19.31 buy_ready=False sector_rank=5 price=2.35 support=2.21 resistance=2.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=45.95 liquidity=11552740.0 spike=0.16
- ACGC.CA: score=17.87 buy_ready=False sector_rank=2 price=10.67 support=9.15 resistance=11.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=68.12 liquidity=4465349.5 spike=0.15
- ADCI.CA: score=11.31 buy_ready=False sector_rank=5 price=288.71 support=256.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51920748.0 spike=5.09
- ADIB.CA: score=19.73 buy_ready=False sector_rank=10 price=53.11 support=46.0 resistance=52.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=79.01 liquidity=25704284.0 spike=0.18
- ADPC.CA: score=16.53 buy_ready=False sector_rank=5 price=3.88 support=3.45 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=3223878.75 spike=0.09
- AFDI.CA: score=18.6 buy_ready=False sector_rank=5 price=53.03 support=43.77 resistance=52.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=71.27 liquidity=7289596.5 spike=0.41
- AFMC.CA: score=7.23 buy_ready=False sector_rank=5 price=202.0 support=184.78 resistance=221.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=113312320.0 spike=1.46
- AJWA.CA: score=26.11 buy_ready=False sector_rank=5 price=191.12 support=161.0 resistance=210.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 July 01:28 PM market time freshness=DELAYED_CURRENT RSI=63.35 liquidity=75489496.0 spike=2.4
- ALCN.CA: score=15.32 buy_ready=False sector_rank=15 price=29.65 support=28.2 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=4945156.5 spike=0.22
- ALUM.CA: score=10.65 buy_ready=False sector_rank=5 price=23.04 support=21.1 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=49.17 liquidity=342038.81 spike=0.06
- AMER.CA: score=17.04 buy_ready=False sector_rank=9 price=4.53 support=2.4 resistance=4.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=82.38 liquidity=9150028.0 spike=0.08
- AMES.CA: score=21.31 buy_ready=False sector_rank=5 price=123.05 support=57.5 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=65.57 liquidity=11840321.0 spike=0.12
- AMIA.CA: score=9.62 buy_ready=False sector_rank=5 price=11.28 support=8.62 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=75.38 liquidity=1315687.25 spike=0.09
- AMOC.CA: score=7.96 buy_ready=False sector_rank=6 price=9.57 support=9.16 resistance=9.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=149498912.0 spike=1.91
- APSW.CA: score=9.85 buy_ready=False sector_rank=5 price=8.72 support=8.1 resistance=9.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=56.12 liquidity=544972.38 spike=0.35
- ARAB.CA: score=18.89 buy_ready=False sector_rank=9 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=20475220.0 spike=0.15
- ARCC.CA: score=20.74 buy_ready=False sector_rank=1 price=56.25 support=54.2 resistance=58.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=50.72 liquidity=4337265.5 spike=0.15
- AREH.CA: score=3.51 buy_ready=False sector_rank=5 price=1.42 support=1.38 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=28.0 liquidity=2203994.25 spike=0.08
- ARVA.CA: score=8.31 buy_ready=False sector_rank=5 price=12.35 support=10.5 resistance=12.6 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=81.59 liquidity=0.0 spike=0.0
- ASCM.CA: score=14.14 buy_ready=False sector_rank=5 price=62.87 support=57.25 resistance=66.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=66.08 liquidity=4830434.5 spike=0.09
- ASPI.CA: score=18.31 buy_ready=False sector_rank=5 price=0.43 support=0.31 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=75.86 liquidity=11472272.0 spike=0.29
- ATLC.CA: score=22.0 buy_ready=False sector_rank=11 price=5.3 support=5.0 resistance=5.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=11291140.0 spike=1.67
- ATQA.CA: score=18.0 buy_ready=False sector_rank=16 price=9.88 support=9.43 resistance=10.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=59.2 liquidity=5636060.5 spike=0.14
- AXPH.CA: score=16.34 buy_ready=False sector_rank=5 price=1249.87 support=1090.02 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=4716038.0 spike=1.16
- BINV.CA: score=8.82 buy_ready=False sector_rank=13 price=47.59 support=45.97 resistance=51.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:03 AM market time freshness=DELAYED_CURRENT RSI=46.06 liquidity=394188.75 spike=0.05
- BIOC.CA: score=9.45 buy_ready=False sector_rank=5 price=285.15 support=241.15 resistance=286.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=203312000.0 spike=2.57
- BTFH.CA: score=21.66 buy_ready=False sector_rank=11 price=3.08 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=30535194.0 spike=0.14
- CAED.CA: score=18.31 buy_ready=False sector_rank=5 price=129.21 support=71.0 resistance=143.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=75.25 liquidity=14985765.0 spike=0.22
- CANA.CA: score=15.25 buy_ready=False sector_rank=10 price=38.22 support=35.2 resistance=39.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=55.24 liquidity=2526264.5 spike=0.15
- CCAP.CA: score=15.43 buy_ready=False sector_rank=13 price=5.21 support=4.76 resistance=5.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=48.04 liquidity=66325048.0 spike=0.09
- CCRS.CA: score=12.63 buy_ready=False sector_rank=5 price=2.53 support=2.26 resistance=2.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=64.38 liquidity=1317101.38 spike=0.07
- CEFM.CA: score=21.31 buy_ready=False sector_rank=5 price=139.06 support=98.3 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=70.8 liquidity=17373260.0 spike=0.67
- CERA.CA: score=11.47 buy_ready=False sector_rank=5 price=1.28 support=1.21 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=2157447.75 spike=0.09
- CFGH.CA: score=14.23 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 July 12:18 PM market time freshness=DELAYED_CURRENT RSI=52.63 liquidity=1921395.08 spike=111.4
- CICH.CA: score=27.66 buy_ready=False sector_rank=11 price=12.5 support=11.6 resistance=12.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=21080638.0 spike=3.86
- CIEB.CA: score=10.75 buy_ready=False sector_rank=10 price=24.16 support=23.55 resistance=24.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=38.99 liquidity=2019006.25 spike=0.21
- CIRA.CA: score=20.41 buy_ready=False sector_rank=14 price=36.0 support=28.04 resistance=36.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=74.85 liquidity=18582482.0 spike=0.33
- CLHO.CA: score=18.24 buy_ready=False sector_rank=12 price=16.85 support=15.98 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=54.66 liquidity=7600292.5 spike=0.18
- CNFN.CA: score=11.28 buy_ready=False sector_rank=11 price=4.77 support=4.68 resistance=5.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=2612261.25 spike=0.13
- COMI.CA: score=20.73 buy_ready=False sector_rank=10 price=141.66 support=127.25 resistance=142.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=67.31 liquidity=36596276.0 spike=0.09
- COPR.CA: score=15.82 buy_ready=False sector_rank=5 price=0.41 support=0.35 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=70.19 liquidity=5512802.0 spike=0.18
- COSG.CA: score=14.53 buy_ready=False sector_rank=5 price=1.64 support=1.5 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=5219027.5 spike=0.12
- CPCI.CA: score=19.95 buy_ready=False sector_rank=5 price=483.18 support=393.0 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=70.5 liquidity=14705939.0 spike=1.32
- CSAG.CA: score=10.72 buy_ready=False sector_rank=15 price=32.0 support=31.35 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=41.21 liquidity=2341905.25 spike=0.17
- DAPH.CA: score=14.47 buy_ready=False sector_rank=5 price=97.28 support=81.0 resistance=99.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=72.04 liquidity=3165129.25 spike=0.17
- DEIN.CA: score=-3.69 buy_ready=False sector_rank=5 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=7.69 buy_ready=False sector_rank=19 price=26.26 support=26.35 resistance=27.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=383018.13 spike=0.12
- DSCW.CA: score=18.31 buy_ready=False sector_rank=5 price=1.95 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=77.42 liquidity=10998826.0 spike=0.2
- DTPP.CA: score=21.31 buy_ready=False sector_rank=5 price=249.46 support=183.0 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=66.53 liquidity=15212965.0 spike=0.19
- EALR.CA: score=7.79 buy_ready=False sector_rank=5 price=419.23 support=395.01 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47238568.0 spike=1.74
- EASB.CA: score=10.18 buy_ready=False sector_rank=5 price=7.34 support=6.88 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=53.1 liquidity=872548.31 spike=0.07
- EAST.CA: score=13.3 buy_ready=False sector_rank=19 price=36.6 support=36.01 resistance=37.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=44.1 liquidity=14324999.0 spike=0.18
- EBSC.CA: score=10.06 buy_ready=False sector_rank=5 price=1.89 support=1.74 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=755758.13 spike=0.09
- ECAP.CA: score=12.52 buy_ready=False sector_rank=5 price=33.14 support=32.12 resistance=34.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=54.95 liquidity=1212247.63 spike=0.21
- EDFM.CA: score=13.36 buy_ready=False sector_rank=5 price=389.85 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=72.34 liquidity=2051299.75 spike=0.39
- EEII.CA: score=5.61 buy_ready=False sector_rank=5 price=2.65 support=2.47 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=30.61 liquidity=1297706.5 spike=0.06
- EFIC.CA: score=11.26 buy_ready=False sector_rank=16 price=200.0 support=180.07 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=66.48 liquidity=1898932.0 spike=0.11
- EFID.CA: score=4.28 buy_ready=False sector_rank=19 price=27.15 support=26.64 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=34.41 liquidity=4977646.5 spike=0.11
- EFIH.CA: score=23.4 buy_ready=False sector_rank=4 price=22.73 support=20.3 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=55.13 liquidity=17294472.0 spike=0.27
- EGAL.CA: score=14.73 buy_ready=False sector_rank=16 price=296.93 support=283.03 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=54.07 liquidity=7370322.0 spike=0.18
- EGAS.CA: score=23.02 buy_ready=False sector_rank=6 price=55.17 support=48.5 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=68.21 liquidity=26448980.0 spike=1.94
- EGBE.CA: score=9.47 buy_ready=False sector_rank=10 price=0.48 support=-0.34 resistance=0.49 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=96.7 liquidity=124468.86 spike=1.81
- EGCH.CA: score=17.36 buy_ready=False sector_rank=16 price=13.31 support=12.24 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=60528728.0 spike=0.97
- EGSA.CA: score=1.0 buy_ready=False sector_rank=8 price=8.81 support=8.67 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:11 AM market time freshness=DELAYED_CURRENT RSI=27.66 liquidity=16058.42 spike=0.86
- EGTS.CA: score=7.36 buy_ready=False sector_rank=9 price=17.41 support=17.15 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=34.58 liquidity=6473463.0 spike=0.14
- EHDR.CA: score=16.08 buy_ready=False sector_rank=5 price=2.78 support=2.49 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=4774164.0 spike=0.11
- EKHO.CA: score=5.14 buy_ready=False sector_rank=6 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=16.21 buy_ready=False sector_rank=7 price=2.17 support=2.08 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=8169206.5 spike=0.11
- ELKA.CA: score=19.31 buy_ready=False sector_rank=5 price=1.72 support=1.35 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=24244564.0 spike=0.31
- ELNA.CA: score=9.13 buy_ready=False sector_rank=5 price=37.54 support=37.0 resistance=40.5 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.76 liquidity=1457190.22 spike=2.18
- ELSH.CA: score=19.31 buy_ready=False sector_rank=5 price=13.55 support=11.53 resistance=15.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=42.8 liquidity=17127466.0 spike=0.12
- ELWA.CA: score=1.73 buy_ready=False sector_rank=5 price=1.75 support=1.74 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:06 AM market time freshness=DELAYED_CURRENT RSI=26.19 liquidity=423694.38 spike=0.28
- EMFD.CA: score=10.89 buy_ready=False sector_rank=9 price=11.3 support=11.08 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=26.62 liquidity=15224408.0 spike=0.26
- ENGC.CA: score=16.49 buy_ready=False sector_rank=5 price=41.41 support=36.31 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=59.04 liquidity=5186391.0 spike=0.2
- EOSB.CA: score=20.75 buy_ready=False sector_rank=5 price=1.55 support=1.5 resistance=1.55 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=446389.14 spike=7.81
- EPCO.CA: score=14.64 buy_ready=False sector_rank=5 price=10.8 support=8.57 resistance=11.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=70.67 liquidity=3333411.25 spike=0.11
- EPPK.CA: score=11.49 buy_ready=False sector_rank=5 price=15.07 support=13.52 resistance=15.93 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=61.16 liquidity=181246.89 spike=0.17
- ETEL.CA: score=20.98 buy_ready=False sector_rank=8 price=106.62 support=92.02 resistance=108.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=67.21 liquidity=16266059.0 spike=0.18
- ETRS.CA: score=19.2 buy_ready=False sector_rank=5 price=10.6 support=10.1 resistance=10.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=49.99 liquidity=7892378.0 spike=0.19
- EXPA.CA: score=19.73 buy_ready=False sector_rank=10 price=20.1 support=18.18 resistance=20.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=83.57 liquidity=13129981.0 spike=0.39
- FAIT.CA: score=6.25 buy_ready=False sector_rank=10 price=36.66 support=36.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=520133.84 spike=0.21
- FAITA.CA: score=0.74 buy_ready=False sector_rank=10 price=0.97 support=0.96 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=10837.81 spike=0.26
- FERC.CA: score=10.96 buy_ready=False sector_rank=16 price=76.87 support=73.45 resistance=85.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=49.92 liquidity=1601971.25 spike=0.14
- FWRY.CA: score=21.4 buy_ready=False sector_rank=4 price=19.14 support=18.28 resistance=19.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=38.43 liquidity=17357610.0 spike=0.14
- GBCO.CA: score=14.64 buy_ready=False sector_rank=17 price=30.52 support=29.53 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=42.99 liquidity=6452045.0 spike=0.1
- GDWA.CA: score=17.12 buy_ready=False sector_rank=5 price=0.81 support=0.76 resistance=0.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=56.77 liquidity=8810042.0 spike=0.08
- GGCC.CA: score=9.66 buy_ready=False sector_rank=5 price=0.84 support=0.48 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=76.99 liquidity=1355824.12 spike=0.04
- GIHD.CA: score=22.58 buy_ready=False sector_rank=5 price=58.09 support=41.71 resistance=65.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=59.67 liquidity=9273684.0 spike=0.17
- GMCI.CA: score=9.64 buy_ready=False sector_rank=5 price=1.97 support=1.75 resistance=2.26 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=40.68 liquidity=336481.91 spike=0.27
- GRCA.CA: score=15.25 buy_ready=False sector_rank=5 price=60.28 support=48.0 resistance=68.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=70.56 liquidity=3944044.75 spike=0.23
- GSSC.CA: score=14.06 buy_ready=False sector_rank=5 price=282.22 support=241.32 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=71.0 liquidity=2756016.5 spike=0.19
- GTWL.CA: score=16.31 buy_ready=False sector_rank=5 price=102.13 support=82.2 resistance=118.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=33.45 liquidity=16030772.0 spike=0.12
- HDBK.CA: score=18.73 buy_ready=False sector_rank=10 price=84.7 support=76.9 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=63.36 liquidity=21777976.0 spike=0.5
- HELI.CA: score=20.89 buy_ready=False sector_rank=9 price=8.4 support=6.41 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=73.26 liquidity=32099906.0 spike=0.15
- HRHO.CA: score=14.66 buy_ready=False sector_rank=11 price=26.5 support=25.95 resistance=27.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=38.46 liquidity=11804688.0 spike=0.14
- ICID.CA: score=20.17 buy_ready=False sector_rank=5 price=7.96 support=6.55 resistance=8.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=54.31 liquidity=10468888.0 spike=1.43
- IDRE.CA: score=15.72 buy_ready=False sector_rank=5 price=48.08 support=42.22 resistance=52.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=53.68 liquidity=2415499.0 spike=0.09
- IFAP.CA: score=12.56 buy_ready=False sector_rank=3 price=19.54 support=18.96 resistance=20.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=47.59 liquidity=1159984.5 spike=0.12
- INFI.CA: score=7.65 buy_ready=False sector_rank=5 price=112.58 support=108.1 resistance=114.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29904618.0 spike=1.67
- IRON.CA: score=1.26 buy_ready=False sector_rank=16 price=30.51 support=30.14 resistance=32.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=2.83 liquidity=1902882.5 spike=0.3
- ISMA.CA: score=13.41 buy_ready=False sector_rank=5 price=30.5 support=26.54 resistance=32.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=69.1 liquidity=2102370.75 spike=0.08
- ISMQ.CA: score=18.36 buy_ready=False sector_rank=16 price=9.13 support=8.96 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=35.35 liquidity=14132007.0 spike=0.15
- ISPH.CA: score=17.64 buy_ready=False sector_rank=12 price=11.63 support=11.2 resistance=11.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=38.78 liquidity=19557470.0 spike=0.4
- JUFO.CA: score=5.35 buy_ready=False sector_rank=19 price=29.05 support=28.48 resistance=31.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=19.95 liquidity=6050160.5 spike=0.23
- KABO.CA: score=19.96 buy_ready=False sector_rank=2 price=8.12 support=6.26 resistance=8.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=64.41 liquidity=6555894.5 spike=0.13
- KWIN.CA: score=18.31 buy_ready=False sector_rank=5 price=97.33 support=66.1 resistance=111.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=83.46 liquidity=11502178.0 spike=0.22
- KZPC.CA: score=10.2 buy_ready=False sector_rank=5 price=8.56 support=8.26 resistance=8.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=888273.69 spike=0.17
- LCSW.CA: score=23.83 buy_ready=False sector_rank=1 price=34.08 support=28.38 resistance=37.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=61.64 liquidity=7433612.5 spike=0.11
- LUTS.CA: score=5.06 buy_ready=False sector_rank=5 price=0.56 support=0.54 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=13.29 liquidity=4750915.5 spike=0.15
- MAAL.CA: score=10.4 buy_ready=False sector_rank=5 price=8.79 support=7.13 resistance=8.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=74.47 liquidity=1096581.5 spike=0.07
- MASR.CA: score=19.31 buy_ready=False sector_rank=5 price=7.94 support=7.24 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=13841462.0 spike=0.17
- MBSC.CA: score=16.13 buy_ready=False sector_rank=1 price=243.18 support=231.51 resistance=249.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=44.96 liquidity=2729955.75 spike=0.15
- MCQE.CA: score=21.11 buy_ready=False sector_rank=1 price=186.87 support=170.0 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=55.32 liquidity=4713758.0 spike=0.26
- MCRO.CA: score=18.31 buy_ready=False sector_rank=5 price=1.52 support=1.2 resistance=1.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=77.27 liquidity=58011376.0 spike=0.42
- MENA.CA: score=9.67 buy_ready=False sector_rank=9 price=6.92 support=6.74 resistance=7.59 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=38.67 liquidity=781281.85 spike=0.1
- MEPA.CA: score=23.31 buy_ready=False sector_rank=5 price=1.87 support=1.56 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=63.16 liquidity=14373775.0 spike=0.29
- MFPC.CA: score=19.36 buy_ready=False sector_rank=16 price=37.63 support=35.19 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=47.34 liquidity=41984936.0 spike=0.46
- MFSC.CA: score=7.66 buy_ready=False sector_rank=5 price=46.81 support=45.05 resistance=53.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=44.04 liquidity=1352804.75 spike=0.24
- MHOT.CA: score=7.43 buy_ready=False sector_rank=20 price=16.51 support=16.2 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=43.09 liquidity=2854769.75 spike=0.25
- MICH.CA: score=23.31 buy_ready=False sector_rank=5 price=41.91 support=37.46 resistance=43.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=64.56 liquidity=11287609.0 spike=0.68
- MILS.CA: score=21.31 buy_ready=False sector_rank=5 price=196.5 support=128.91 resistance=211.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=70.81 liquidity=23750948.0 spike=0.47
- MIPH.CA: score=-1.61 buy_ready=False sector_rank=12 price=779.44 support=740.45 resistance=784.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2757116.5 spike=0.8
- MOED.CA: score=15.31 buy_ready=False sector_rank=5 price=0.68 support=0.68 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=11444468.0 spike=0.45
- MOIL.CA: score=10.2 buy_ready=False sector_rank=6 price=0.67 support=0.47 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:10 AM market time freshness=DELAYED_CURRENT RSI=92.15 liquidity=61975.14 spike=0.08
- MOIN.CA: score=5.47 buy_ready=False sector_rank=5 price=23.6 support=23.03 resistance=24.76 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=51.08 liquidity=158686.4 spike=0.3
- MOSC.CA: score=15.36 buy_ready=False sector_rank=5 price=291.15 support=260.01 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:12 AM market time freshness=DELAYED_CURRENT RSI=62.23 liquidity=2049164.5 spike=0.17
- MPCI.CA: score=18.31 buy_ready=False sector_rank=5 price=293.97 support=237.12 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=84.45 liquidity=18971268.0 spike=0.19
- MPCO.CA: score=24.4 buy_ready=False sector_rank=3 price=1.96 support=1.77 resistance=2.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=53.66 liquidity=15816312.0 spike=0.19
- MPRC.CA: score=15.33 buy_ready=False sector_rank=5 price=45.1 support=37.51 resistance=47.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=62.11 liquidity=4026017.5 spike=0.13
- MTIE.CA: score=16.97 buy_ready=False sector_rank=17 price=9.59 support=9.09 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=6783346.5 spike=0.28
- NAHO.CA: score=5.32 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:31 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9132.01 spike=0.36
- NCCW.CA: score=16.75 buy_ready=False sector_rank=5 price=6.98 support=6.01 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=70.49 liquidity=5443447.5 spike=0.19
- NEDA.CA: score=6.63 buy_ready=False sector_rank=5 price=2.74 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=319884.04 spike=0.41
- NHPS.CA: score=17.77 buy_ready=False sector_rank=5 price=84.34 support=67.0 resistance=95.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=6457179.0 spike=0.07
- NINH.CA: score=6.31 buy_ready=False sector_rank=5 price=22.83 support=21.65 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22338588.0 spike=0.52
- NIPH.CA: score=17.64 buy_ready=False sector_rank=12 price=232.68 support=165.0 resistance=242.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=77.86 liquidity=75684328.0 spike=0.46
- OBRI.CA: score=9.19 buy_ready=False sector_rank=5 price=32.93 support=32.2 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=24.17 liquidity=7885390.0 spike=0.18
- OCDI.CA: score=20.89 buy_ready=False sector_rank=9 price=28.57 support=24.46 resistance=29.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=60.81 liquidity=79039168.0 spike=0.8
- OCPH.CA: score=18.31 buy_ready=False sector_rank=5 price=477.86 support=350.6 resistance=496.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=82.68 liquidity=14031704.0 spike=0.56
- ODIN.CA: score=7.71 buy_ready=False sector_rank=5 price=2.93 support=2.84 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=34005016.0 spike=1.7
- OFH.CA: score=18.83 buy_ready=False sector_rank=5 price=0.7 support=0.59 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=66.49 liquidity=7522830.0 spike=0.11
- OIH.CA: score=22.43 buy_ready=False sector_rank=13 price=1.48 support=1.4 resistance=1.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=19757912.0 spike=0.26
- OLFI.CA: score=9.36 buy_ready=False sector_rank=19 price=22.83 support=21.91 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=47.3 liquidity=2051895.13 spike=0.06
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=712.52 support=708.0 resistance=714.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22223324.0 spike=1.0
- ORHD.CA: score=20.89 buy_ready=False sector_rank=9 price=39.5 support=37.76 resistance=40.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=13003159.0 spike=0.09
- ORWE.CA: score=20.4 buy_ready=False sector_rank=2 price=22.89 support=22.2 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=10763923.0 spike=0.43
- PHAR.CA: score=10.64 buy_ready=False sector_rank=12 price=124.8 support=104.2 resistance=124.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=333910848.0 spike=3.98
- PHDC.CA: score=15.89 buy_ready=False sector_rank=9 price=14.51 support=14.32 resistance=15.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=15553861.0 spike=0.07
- PHTV.CA: score=11.39 buy_ready=False sector_rank=5 price=321.35 support=260.0 resistance=329.0 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=73.12 liquidity=2080098.59 spike=0.43
- POUL.CA: score=5.56 buy_ready=False sector_rank=19 price=37.86 support=36.5 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=32.88 liquidity=3251423.5 spike=0.1
- PRCL.CA: score=20.69 buy_ready=False sector_rank=1 price=36.1 support=30.83 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=6286029.0 spike=0.13
- PRDC.CA: score=20.89 buy_ready=False sector_rank=9 price=9.4 support=7.4 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=55.01 liquidity=19506476.0 spike=0.16
- PRMH.CA: score=7.09 buy_ready=False sector_rank=5 price=2.6 support=2.48 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=779520.69 spike=0.05
- RACC.CA: score=16.44 buy_ready=False sector_rank=5 price=10.0 support=9.65 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=7127575.0 spike=0.31
- RAKT.CA: score=12.54 buy_ready=False sector_rank=5 price=22.53 support=21.25 resistance=23.7 source=Yahoo Finance as_of=2026-07-29T21:00:00+00:00 freshness=FRESH RSI=53.46 liquidity=693563.54 spike=2.27
- RAYA.CA: score=9.7 buy_ready=False sector_rank=21 price=7.51 support=7.3 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=6389915.0 spike=0.05
- RMDA.CA: score=25.64 buy_ready=False sector_rank=12 price=5.46 support=4.91 resistance=5.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=71.64 liquidity=118095648.0 spike=3.89
- ROTO.CA: score=15.49 buy_ready=False sector_rank=5 price=44.48 support=40.5 resistance=45.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=51.49 liquidity=4184241.5 spike=0.21
- RREI.CA: score=19.58 buy_ready=False sector_rank=5 price=4.65 support=3.45 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=71.0 liquidity=8270721.0 spike=0.13
- RTVC.CA: score=7.92 buy_ready=False sector_rank=5 price=3.79 support=3.7 resistance=4.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=1616390.38 spike=0.34
- RUBX.CA: score=12.61 buy_ready=False sector_rank=5 price=12.57 support=11.22 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=42.57 liquidity=3302066.0 spike=0.05
- SAUD.CA: score=17.87 buy_ready=False sector_rank=10 price=21.7 support=21.01 resistance=22.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=54.51 liquidity=10699865.0 spike=1.07
- SCEM.CA: score=21.4 buy_ready=False sector_rank=1 price=81.51 support=61.28 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=75.59 liquidity=57187004.0 spike=0.74
- SCFM.CA: score=23.31 buy_ready=False sector_rank=5 price=288.11 support=237.08 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=60.42 liquidity=13345781.0 spike=0.5
- SCTS.CA: score=9.2 buy_ready=False sector_rank=14 price=610.87 support=599.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT RSI=47.65 liquidity=787085.88 spike=0.13
- SDTI.CA: score=13.92 buy_ready=False sector_rank=5 price=58.6 support=46.0 resistance=60.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=83.8 liquidity=5612234.5 spike=0.31
- SEIG.CA: score=19.6 buy_ready=False sector_rank=5 price=258.73 support=186.05 resistance=285.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=57.13 liquidity=8293106.5 spike=0.3
- SIPC.CA: score=11.31 buy_ready=False sector_rank=5 price=4.55 support=3.99 resistance=4.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100703104.0 spike=3.96
- SKPC.CA: score=16.36 buy_ready=False sector_rank=16 price=15.93 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=43.31 liquidity=11026416.0 spike=0.29
- SMFR.CA: score=13.34 buy_ready=False sector_rank=5 price=235.43 support=193.0 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:18 AM market time freshness=DELAYED_CURRENT RSI=66.77 liquidity=2027375.38 spike=0.09
- SNFC.CA: score=6.54 buy_ready=False sector_rank=5 price=10.92 support=11.01 resistance=12.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=12.03 liquidity=5234689.0 spike=0.46
- SPIN.CA: score=21.46 buy_ready=False sector_rank=2 price=15.99 support=14.0 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=68.35 liquidity=8059723.5 spike=0.31
- SPMD.CA: score=21.31 buy_ready=False sector_rank=5 price=0.47 support=0.43 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=18286870.0 spike=0.66
- SUGR.CA: score=7.08 buy_ready=False sector_rank=19 price=46.63 support=46.47 resistance=47.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:17 AM market time freshness=DELAYED_CURRENT RSI=42.02 liquidity=1778218.38 spike=0.33
- SVCE.CA: score=5.68 buy_ready=False sector_rank=5 price=9.2 support=8.96 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=28.05 liquidity=4372445.0 spike=0.08
- SWDY.CA: score=21.04 buy_ready=False sector_rank=7 price=93.47 support=86.1 resistance=97.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=65.15 liquidity=10434071.0 spike=0.48
- TALM.CA: score=5.79 buy_ready=False sector_rank=14 price=18.5 support=18.3 resistance=18.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:15 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38481232.0 spike=1.19
- TMGH.CA: score=18.89 buy_ready=False sector_rank=9 price=97.44 support=94.1 resistance=103.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:14 AM market time freshness=DELAYED_CURRENT RSI=50.6 liquidity=30610510.0 spike=0.08
- TRTO.CA: score=12.45 buy_ready=False sector_rank=5 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 July 11:46 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=146794.26 spike=108.8
- UEFM.CA: score=13.79 buy_ready=False sector_rank=5 price=543.39 support=473.0 resistance=625.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=486384.84 spike=0.09
- UEGC.CA: score=15.64 buy_ready=False sector_rank=5 price=2.36 support=1.41 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=70.87 liquidity=4332433.0 spike=0.08
- UNIP.CA: score=15.26 buy_ready=False sector_rank=5 price=0.38 support=0.32 resistance=0.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:19 AM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=1949616.5 spike=0.07
- UNIT.CA: score=4.8 buy_ready=False sector_rank=9 price=17.87 support=12.8 resistance=21.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:13 AM market time freshness=DELAYED_CURRENT RSI=21.87 liquidity=916730.56 spike=0.03
- WCDF.CA: score=13.81 buy_ready=False sector_rank=5 price=583.4 support=504.0 resistance=634.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=2502870.5 spike=0.77
- WKOL.CA: score=9.29 buy_ready=False sector_rank=5 price=358.54 support=332.5 resistance=363.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43235712.0 spike=2.49
- ZEOT.CA: score=17.66 buy_ready=False sector_rank=5 price=12.54 support=10.81 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:20 AM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=6352961.0 spike=0.21
- ZMID.CA: score=20.89 buy_ready=False sector_rank=9 price=7.25 support=6.47 resistance=7.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:16 AM market time freshness=DELAYED_CURRENT RSI=57.92 liquidity=33091352.0 spike=0.12

## Backtesting Lite
- CICH.CA: 180d return=50.25%, max drawdown=-14.78%, MA20>MA50 days last20=0, as_of=2026-07-29T21:00:00+00:00
- AJWA.CA: 180d return=45.38%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-07-29T21:00:00+00:00
- RMDA.CA: 180d return=27.06%, max drawdown=-27.97%, MA20>MA50 days last20=9, as_of=2026-07-29T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CICH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=CI Capital Holding summary=Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- AJWA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=AJWA For Food Industries Co. Egypt summary=Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture; AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3; Ajwa Egypt turns to losses in 9M
  - Ajwa Egypt&#39;s board approves capital increase to EGP 500m, joins new food venture: https://english.mubasher.info/news/4532004/Ajwa-Egypt-s-board-approves-capital-increase-to-EGP-500m-joins-new-food-venture/
  - AJWA Egypt’s standalone net profits retreat to EGP 14m in 9M-25 amid shift to profitability in Q3: https://english.mubasher.info/news/4527545/AJWA-Egypt-s-standalone-net-profits-retreat-to-EGP-14m-in-9M-25-amid-shift-to-profitability-in-Q3/
  - Ajwa Egypt turns to losses in 9M: https://english.mubasher.info/news/3883210/Ajwa-Egypt-turns-to-losses-in-9M/
- RMDA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tenth of Ramadan Pharmaceutical Industries summary=Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=578 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- MEPA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Medical Packaging Company summary=Medical Packaging stock close to break above EGP 1.7; Medical Packaging announces EGP 62m capital hike; Medical Packaging&#39;s profit jumps 54% in Q1-21
  - Medical Packaging stock close to break above EGP 1.7: https://english.mubasher.info/news/4598700/Medical-Packaging-stock-close-to-break-above-EGP-1-7/
  - Medical Packaging announces EGP 62m capital hike: https://english.mubasher.info/news/3936298/Medical-Packaging-announces-EGP-62m-capital-hike/
  - Medical Packaging&#39;s profit jumps 54% in Q1-21: https://english.mubasher.info/news/3815448/Medical-Packaging-s-profit-jumps-54-in-Q1-21/
- MICH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Chemical Industries Co. summary=Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26; Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis; Misr Chemical Industries posts 10% decrease in H1-25/26 net profits
  - Misr Chemical Industries’ net profits decline to EGP 397m in 9M-25/26: https://english.mubasher.info/news/4597505/Misr-Chemical-Industries-net-profits-decline-to-EGP-397m-in-9M-25-26/
  - Surpassing Misr Chemical stock’s current levels would lead to historical levels – Analysis: https://english.mubasher.info/news/4586207/Surpassing-Misr-Chemical-stock-s-current-levels-would-lead-to-historical-levels-Analysis/
  - Misr Chemical Industries posts 10% decrease in H1-25/26 net profits: https://english.mubasher.info/news/4554378/Misr-Chemical-Industries-posts-10-decrease-in-H1-25-26-net-profits/

## Warnings
- Evidence rejected for CICH.CA: source text did not clearly match CICH.CA / CI Capital Holding.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for AJWA.CA matches the company but no source/report date was detected.
- Evidence rejected for RMDA.CA: source text did not clearly match RMDA.CA / Tenth of Ramadan Pharmaceutical Industries.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence for MEPA.CA matches the company but no source/report date was detected.
- Evidence for MICH.CA matches the company but no source/report date was detected.
