# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-07-22T08:01:21.303603+00:00
Generated Cairo: 2026-07-22 11:01
Run timing: target 08:45 Cairo | generated Cairo 2026-07-22 11:01 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-07-22 10:57

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 43
- Data quality issues: 1
- Tradeable price/liquidity tickers: 166/189
- Top sector: Building Materials

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, July 22
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 89.47% / above MA50 57.89%
- EGX70 regime: CONSTRUCTIVE / above MA20 81.58% / above MA50 84.21%
- Sector breadth: 52.38%
- Risk mode: SELECTIVE_SWING_TRADES_ONLY

## Top Liquidity
- CCAP.CA: liquidity=179919952.0 spike=0.29 score=21.4
- PHDC.CA: liquidity=109941576.0 spike=0.45 score=24.4
- NIPH.CA: liquidity=80697216.0 spike=0.61 score=25.4
- MCRO.CA: liquidity=72478552.0 spike=1.13 score=22.52
- LCSW.CA: liquidity=70618224.0 spike=0.96 score=26.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 is BULLISH and EGX70 CONSTRUCTIVE with sector breadth at 52.3%; leading sectors are Building Materials, Healthcare, and Industrial Goods. The scanner’s risk mode is SELECTIVE_SWING_TRADES_ONLY, so it only flags tickets that satisfy liquidity, freshness and technical gates, resulting in a HOLD stance for all candidates.

## Top Liquidity Spikes
- EGBE.CA: spike=90.79 liquidity=328888.31 outlook=WEAK_OR_RISKY score=20.01 buy_ready=False
- WCDF.CA: spike=5.98 liquidity=9867449.05 outlook=BULLISH_WATCH score=79.66 buy_ready=True
- EGSA.CA: spike=3.71 liquidity=49422.1 outlook=NEUTRAL score=39.28 buy_ready=False
- UEFM.CA: spike=3.39 liquidity=14273295.45 outlook=CONSTRUCTIVE score=65.66 buy_ready=False
- MOED.CA: spike=3.35 liquidity=41878704.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=11.37 5d=5.83% 20d=15.9% aboveMA50=83.33%
- #2 Healthcare: score=9.55 5d=5.96% 20d=4.61% aboveMA50=83.33%
- #3 Industrial Goods & Cables: score=8.79 5d=3.38% 20d=4.58% aboveMA50=100.0%
- #4 Investment Holding: score=8.19 5d=0.93% 20d=6.92% aboveMA50=100.0%
- #5 Transportation & Logistics: score=8.05 5d=1.95% 20d=5.76% aboveMA50=100.0%
- #6 Telecommunications: score=7.28 5d=0.72% 20d=1.82% aboveMA50=50.0%
- #7 Automotive & Distribution: score=6.68 5d=-1.58% 20d=5.92% aboveMA50=100.0%
- #8 Textiles: score=6.63 5d=1.97% 20d=3.73% aboveMA50=75.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- ISPH.CA: BULLISH_WATCH score=95.55 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CLHO.CA: BULLISH_WATCH score=95.55 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- ARCC.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- GBCO.CA: BULLISH_WATCH score=82.68 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- WCDF.CA: BULLISH_WATCH score=79.66 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- MENA.CA: BULLISH_WATCH score=77.32 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- LCSW.CA: BULLISH_WATCH score=77 liquidity=TRADEABLE sector=LEADING risk=overheated RSI; far above support
- ROTO.CA: BULLISH_WATCH score=76.66 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ASCM.CA: BULLISH_WATCH score=76.66 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- LUTS.CA: BULLISH_WATCH score=76.66 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- WCDF.CA: rank=29.13 outlook=BULLISH_WATCH outlook_score=79.66 sector_rank=13 price=586.58 support=504.0 resistance=634.15 liquidity=9867449.05
- ISPH.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=95.55 sector_rank=2 price=11.86 support=11.2 resistance=12.6 liquidity=40699784.0
- TALM.CA: rank=26.4 outlook=BULLISH_WATCH outlook_score=70.2 sector_rank=11 price=16.15 support=15.27 resistance=16.34 liquidity=10950262.0
- OBRI.CA: rank=26.26 outlook=CONSTRUCTIVE outlook_score=62.66 sector_rank=13 price=36.18 support=31.5 resistance=39.27 liquidity=21310770.0
- ARCC.CA: rank=25.15 outlook=BULLISH_WATCH outlook_score=90 sector_rank=1 price=56.55 support=53.0 resistance=57.88 liquidity=5750420.5
- CLHO.CA: rank=24.93 outlook=BULLISH_WATCH outlook_score=95.55 sector_rank=2 price=16.86 support=15.7 resistance=17.9 liquidity=6527229.5
- BTFH.CA: rank=24.72 outlook=CONSTRUCTIVE outlook_score=69.21 sector_rank=15 price=3.1 support=2.91 resistance=3.2 liquidity=9040233.0
- FWRY.CA: rank=24.4 outlook=CONSTRUCTIVE outlook_score=57.46 sector_rank=9 price=19.49 support=18.13 resistance=19.55 liquidity=11728561.0
- EMFD.CA: rank=24.4 outlook=BULLISH_WATCH outlook_score=71.32 sector_rank=10 price=11.88 support=11.24 resistance=12.22 liquidity=11897586.0
- ORHD.CA: rank=24.4 outlook=CONSTRUCTIVE outlook_score=65.32 sector_rank=10 price=39.68 support=37.0 resistance=40.2 liquidity=37339996.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=16.88 buy_ready=False sector_rank=13 price=235.96 support=196.0 resistance=253.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=73.91 liquidity=617541.63 spike=0.04
- ABUK.CA: score=20.48 buy_ready=False sector_rank=16 price=72.86 support=66.66 resistance=75.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=68.1 liquidity=15997691.0 spike=0.1
- ACAMD.CA: score=24.26 buy_ready=False sector_rank=13 price=2.47 support=2.14 resistance=2.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=74.29 liquidity=45365592.0 spike=0.59
- ACGC.CA: score=9.76 buy_ready=False sector_rank=8 price=10.39 support=10.2 resistance=10.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24250990.0 spike=1.18
- ADCI.CA: score=18.28 buy_ready=True sector_rank=13 price=256.71 support=230.0 resistance=258.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=60.7 liquidity=2017845.75 spike=0.17
- ADIB.CA: score=24.0 buy_ready=True sector_rank=14 price=49.3 support=44.1 resistance=48.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=57.06 liquidity=24440068.0 spike=0.26
- ADPC.CA: score=11.9 buy_ready=False sector_rank=13 price=4.2 support=4.16 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56909140.0 spike=2.32
- AFDI.CA: score=26.26 buy_ready=False sector_rank=13 price=49.18 support=41.84 resistance=48.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=74.69 liquidity=12915088.0 spike=0.91
- AFMC.CA: score=9.62 buy_ready=False sector_rank=13 price=102.39 support=101.0 resistance=106.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12457390.0 spike=1.18
- AJWA.CA: score=12.84 buy_ready=False sector_rank=13 price=169.51 support=169.0 resistance=192.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=41.52 liquidity=574530.5 spike=0.05
- ALCN.CA: score=15.82 buy_ready=False sector_rank=5 price=29.84 support=27.7 resistance=30.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=74.12 liquidity=1421820.38 spike=0.07
- ALUM.CA: score=13.8 buy_ready=False sector_rank=13 price=23.8 support=20.55 resistance=23.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=81.32 liquidity=536819.94 spike=0.08
- AMER.CA: score=9.4 buy_ready=False sector_rank=10 price=4.29 support=4.19 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22648742.0 spike=0.23
- AMES.CA: score=24.26 buy_ready=False sector_rank=13 price=121.1 support=45.15 resistance=144.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=73.04 liquidity=37132388.0 spike=0.41
- AMIA.CA: score=13.77 buy_ready=False sector_rank=13 price=10.33 support=8.4 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=82.96 liquidity=507287.94 spike=0.05
- AMOC.CA: score=22.2 buy_ready=False sector_rank=12 price=8.33 support=7.42 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=70.88 liquidity=7795250.5 spike=0.13
- APSW.CA: score=13.79 buy_ready=False sector_rank=13 price=9.21 support=8.0 resistance=9.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=87.8 liquidity=528110.25 spike=0.43
- ARAB.CA: score=24.4 buy_ready=True sector_rank=10 price=0.24 support=0.2 resistance=0.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=16899680.0 spike=0.15
- ARCC.CA: score=25.15 buy_ready=True sector_rank=1 price=56.55 support=53.0 resistance=57.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=67.63 liquidity=5750420.5 spike=0.25
- AREH.CA: score=13.04 buy_ready=False sector_rank=13 price=1.46 support=1.48 resistance=1.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=47.92 liquidity=3776274.5 spike=0.1
- ARVA.CA: score=16.96 buy_ready=True sector_rank=13 price=11.11 support=10.5 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=55.87 liquidity=2699816.5 spike=0.16
- ASCM.CA: score=18.98 buy_ready=True sector_rank=13 price=61.79 support=56.29 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=60.16 liquidity=4718631.5 spike=0.07
- ASPI.CA: score=16.17 buy_ready=False sector_rank=13 price=0.36 support=0.3 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=79.61 liquidity=2901633.5 spike=0.12
- ATLC.CA: score=22.66 buy_ready=False sector_rank=15 price=5.17 support=4.92 resistance=5.43 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=59.57 liquidity=10563737.08 spike=1.49
- ATQA.CA: score=20.71 buy_ready=True sector_rank=16 price=9.66 support=9.21 resistance=9.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=62.14 liquidity=5229746.0 spike=0.19
- AXPH.CA: score=16.67 buy_ready=False sector_rank=13 price=1230.75 support=1075.0 resistance=1342.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:37 AM market time freshness=DELAYED_CURRENT RSI=74.16 liquidity=404878.28 spike=0.11
- BINV.CA: score=14.86 buy_ready=False sector_rank=4 price=47.6 support=47.57 resistance=47.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=456315.72 spike=1.0
- BIOC.CA: score=11.74 buy_ready=False sector_rank=13 price=124.09 support=113.25 resistance=128.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47448108.0 spike=2.24
- BTFH.CA: score=24.72 buy_ready=True sector_rank=15 price=3.1 support=2.91 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=62.0 liquidity=9040233.0 spike=0.04
- CAED.CA: score=15.93 buy_ready=False sector_rank=13 price=116.0 support=68.0 resistance=134.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=81.23 liquidity=4668152.5 spike=0.1
- CANA.CA: score=14.14 buy_ready=True sector_rank=14 price=36.66 support=34.7 resistance=37.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=60.04 liquidity=1139611.0 spike=0.08
- CCAP.CA: score=21.4 buy_ready=False sector_rank=4 price=5.51 support=4.65 resistance=5.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=78.63 liquidity=179919952.0 spike=0.29
- CCRS.CA: score=14.37 buy_ready=False sector_rank=13 price=2.63 support=2.18 resistance=2.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=81.08 liquidity=1107683.0 spike=0.07
- CEFM.CA: score=1.99 buy_ready=False sector_rank=13 price=124.85 support=123.4 resistance=128.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2723181.75 spike=0.24
- CERA.CA: score=16.48 buy_ready=False sector_rank=13 price=1.34 support=1.19 resistance=1.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=2218850.25 spike=0.09
- CFGH.CA: score=-0.04 buy_ready=False sector_rank=13 price=0.11 support=0.11 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:19 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12485.12 spike=1.34
- CICH.CA: score=16.35 buy_ready=False sector_rank=15 price=12.05 support=11.52 resistance=12.46 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=55.56 liquidity=3662489.11 spike=0.8
- CIEB.CA: score=16.42 buy_ready=True sector_rank=14 price=24.47 support=23.3 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:36 AM market time freshness=DELAYED_CURRENT RSI=63.83 liquidity=2412532.0 spike=0.33
- CIRA.CA: score=20.01 buy_ready=False sector_rank=11 price=31.77 support=27.45 resistance=33.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=70.55 liquidity=5613152.0 spike=0.15
- CLHO.CA: score=24.93 buy_ready=True sector_rank=2 price=16.86 support=15.7 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=65.11 liquidity=6527229.5 spike=0.13
- CNFN.CA: score=12.18 buy_ready=False sector_rank=15 price=4.85 support=4.61 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=68.52 liquidity=492549.97 spike=0.01
- COMI.CA: score=24.0 buy_ready=True sector_rank=14 price=139.01 support=126.21 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=68.5 liquidity=64530964.0 spike=0.17
- COPR.CA: score=17.5 buy_ready=False sector_rank=13 price=0.39 support=0.35 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=74.55 liquidity=4240073.0 spike=0.2
- COSG.CA: score=9.78 buy_ready=False sector_rank=13 price=1.77 support=1.72 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=46031836.0 spike=1.26
- CPCI.CA: score=14.68 buy_ready=False sector_rank=13 price=472.47 support=367.7 resistance=512.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=74.9 liquidity=412561.41 spike=0.04
- CSAG.CA: score=16.21 buy_ready=True sector_rank=5 price=33.51 support=30.87 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=65.6 liquidity=1805811.38 spike=0.09
- DAPH.CA: score=20.79 buy_ready=True sector_rank=13 price=90.87 support=78.52 resistance=87.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=67.5 liquidity=6526297.5 spike=0.64
- DEIN.CA: score=-0.74 buy_ready=False sector_rank=13 price=11.38 support=13.65 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=12.23 buy_ready=False sector_rank=17 price=26.68 support=26.06 resistance=27.83 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=46.79 liquidity=1168690.73 spike=0.24
- DSCW.CA: score=23.26 buy_ready=False sector_rank=13 price=1.98 support=1.71 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=96.3 liquidity=13090456.0 spike=0.3
- DTPP.CA: score=16.97 buy_ready=False sector_rank=13 price=223.21 support=114.67 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=78.19 liquidity=5710845.0 spike=0.1
- EALR.CA: score=14.88 buy_ready=False sector_rank=13 price=367.41 support=332.0 resistance=425.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=68.74 liquidity=618868.88 spike=0.04
- EASB.CA: score=6.89 buy_ready=False sector_rank=13 price=8.3 support=8.1 resistance=8.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7622859.0 spike=0.45
- EAST.CA: score=10.67 buy_ready=False sector_rank=17 price=37.37 support=36.11 resistance=39.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=48.91 liquidity=1609078.38 spike=0.03
- EBSC.CA: score=12.88 buy_ready=False sector_rank=13 price=1.89 support=1.71 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:36 AM market time freshness=DELAYED_CURRENT RSI=59.72 liquidity=615542.88 spike=0.09
- ECAP.CA: score=12.71 buy_ready=False sector_rank=13 price=33.75 support=31.52 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=68.1 liquidity=445221.06 spike=0.05
- EDFM.CA: score=12.09 buy_ready=False sector_rank=13 price=395.53 support=310.2 resistance=430.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:37 AM market time freshness=DELAYED_CURRENT RSI=79.75 liquidity=821071.88 spike=0.22
- EEII.CA: score=17.22 buy_ready=False sector_rank=13 price=2.75 support=2.35 resistance=2.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=73.03 liquidity=2957123.5 spike=0.14
- EFIC.CA: score=10.48 buy_ready=False sector_rank=16 price=185.14 support=180.02 resistance=213.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=997986.5 spike=0.1
- EFID.CA: score=14.75 buy_ready=False sector_rank=17 price=28.1 support=25.5 resistance=28.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=4687821.5 spike=0.12
- EFIH.CA: score=21.34 buy_ready=True sector_rank=9 price=23.09 support=20.0 resistance=23.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=66.39 liquidity=6939697.0 spike=0.17
- EGAL.CA: score=15.43 buy_ready=False sector_rank=16 price=303.5 support=272.28 resistance=312.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=73.35 liquidity=4954445.5 spike=0.1
- EGAS.CA: score=17.13 buy_ready=False sector_rank=12 price=52.5 support=46.51 resistance=54.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=72.73 liquidity=2727471.25 spike=0.24
- EGBE.CA: score=18.33 buy_ready=False sector_rank=14 price=0.48 support=-0.34 resistance=0.48 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=96.84 liquidity=328888.31 spike=90.79
- EGCH.CA: score=13.22 buy_ready=False sector_rank=16 price=13.15 support=12.13 resistance=13.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=72.04 liquidity=2742674.0 spike=0.05
- EGSA.CA: score=18.45 buy_ready=False sector_rank=6 price=9.1 support=8.67 resistance=9.21 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=80.7 liquidity=49422.1 spike=3.71
- EGTS.CA: score=10.75 buy_ready=False sector_rank=10 price=17.77 support=15.1 resistance=19.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=56.83 liquidity=1346846.13 spike=0.03
- EHDR.CA: score=17.24 buy_ready=False sector_rank=13 price=2.92 support=2.37 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=76.14 liquidity=5977139.5 spike=0.17
- EKHO.CA: score=8.4 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=22.32 buy_ready=True sector_rank=3 price=2.24 support=2.04 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=69.05 liquidity=7915015.5 spike=0.13
- ELKA.CA: score=17.94 buy_ready=False sector_rank=13 price=2.08 support=1.19 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=86.55 liquidity=6679950.5 spike=0.1
- ELNA.CA: score=14.67 buy_ready=False sector_rank=13 price=38.64 support=35.55 resistance=40.5 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=64.05 liquidity=1050389.74 spike=1.68
- ELSH.CA: score=17.94 buy_ready=False sector_rank=13 price=14.1 support=11.1 resistance=15.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=72.31 liquidity=5680482.5 spike=0.05
- ELWA.CA: score=9.96 buy_ready=False sector_rank=13 price=1.96 support=1.87 resistance=2.14 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=48.57 liquidity=691611.49 spike=0.58
- EMFD.CA: score=24.4 buy_ready=True sector_rank=10 price=11.88 support=11.24 resistance=12.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=56.05 liquidity=11897586.0 spike=0.16
- ENGC.CA: score=13.98 buy_ready=False sector_rank=13 price=42.42 support=33.91 resistance=44.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:37 AM market time freshness=DELAYED_CURRENT RSI=78.52 liquidity=719307.19 spike=0.03
- EOSB.CA: score=14.43 buy_ready=False sector_rank=13 price=1.48 support=1.48 resistance=1.55 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=49079.76 spike=1.06
- EPCO.CA: score=10.16 buy_ready=False sector_rank=13 price=11.58 support=11.05 resistance=11.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31863096.0 spike=1.45
- EPPK.CA: score=17.0 buy_ready=False sector_rank=13 price=15.13 support=12.31 resistance=15.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=63.09 liquidity=736060.94 spike=0.65
- ETEL.CA: score=9.66 buy_ready=False sector_rank=6 price=105.75 support=103.8 resistance=106.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70413160.0 spike=1.13
- ETRS.CA: score=15.48 buy_ready=True sector_rank=13 price=10.82 support=10.12 resistance=11.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=60.34 liquidity=1219088.88 spike=0.02
- EXPA.CA: score=18.06 buy_ready=False sector_rank=14 price=20.0 support=18.03 resistance=19.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=83.13 liquidity=5054849.0 spike=0.19
- FAIT.CA: score=14.42 buy_ready=False sector_rank=14 price=37.92 support=35.06 resistance=37.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:36 AM market time freshness=DELAYED_CURRENT RSI=67.98 liquidity=412633.56 spike=0.15
- FAITA.CA: score=9.02 buy_ready=False sector_rank=14 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:32 AM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=15391.03 spike=0.43
- FERC.CA: score=14.41 buy_ready=False sector_rank=16 price=78.75 support=72.75 resistance=83.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=84.94 liquidity=2931810.0 spike=0.35
- FWRY.CA: score=24.4 buy_ready=True sector_rank=9 price=19.49 support=18.13 resistance=19.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=65.95 liquidity=11728561.0 spike=0.09
- GBCO.CA: score=19.88 buy_ready=True sector_rank=7 price=31.79 support=29.01 resistance=34.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=51.95 liquidity=5481379.0 spike=0.07
- GDWA.CA: score=22.26 buy_ready=False sector_rank=13 price=0.87 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=82.28 liquidity=43753712.0 spike=0.93
- GGCC.CA: score=8.96 buy_ready=False sector_rank=13 price=0.83 support=0.81 resistance=0.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9699811.0 spike=0.33
- GIHD.CA: score=9.26 buy_ready=False sector_rank=13 price=56.09 support=56.0 resistance=57.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14343089.0 spike=0.41
- GMCI.CA: score=15.27 buy_ready=True sector_rank=13 price=2.05 support=1.66 resistance=2.26 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=66.28 liquidity=1005727.93 spike=0.79
- GRCA.CA: score=24.08 buy_ready=False sector_rank=13 price=63.97 support=48.0 resistance=68.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=79.62 liquidity=13321749.0 spike=1.41
- GSSC.CA: score=12.81 buy_ready=False sector_rank=13 price=271.09 support=240.0 resistance=288.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=85.8 liquidity=1541553.0 spike=0.16
- GTWL.CA: score=22.26 buy_ready=True sector_rank=13 price=103.84 support=47.85 resistance=117.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=68.62 liquidity=30802764.0 spike=0.24
- HDBK.CA: score=14.06 buy_ready=False sector_rank=14 price=83.0 support=75.3 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=51.26 liquidity=4059277.75 spike=0.1
- HELI.CA: score=20.75 buy_ready=False sector_rank=10 price=8.29 support=6.36 resistance=8.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=91.87 liquidity=7353996.5 spike=0.04
- HRHO.CA: score=23.78 buy_ready=True sector_rank=15 price=27.12 support=26.09 resistance=27.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=55.64 liquidity=8099350.0 spike=0.07
- ICID.CA: score=17.24 buy_ready=True sector_rank=13 price=8.2 support=6.55 resistance=8.98 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=59.1 liquidity=2979174.73 spike=0.39
- IDRE.CA: score=4.78 buy_ready=False sector_rank=13 price=47.7 support=47.25 resistance=48.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5515445.0 spike=0.41
- IFAP.CA: score=10.67 buy_ready=False sector_rank=19 price=19.09 support=18.47 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=3896757.75 spike=0.7
- INFI.CA: score=15.39 buy_ready=False sector_rank=13 price=106.25 support=88.51 resistance=109.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=80.31 liquidity=2121807.75 spike=0.17
- IRON.CA: score=7.86 buy_ready=False sector_rank=16 price=31.37 support=30.45 resistance=33.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=35.03 liquidity=382473.06 spike=0.05
- ISMA.CA: score=16.46 buy_ready=False sector_rank=13 price=28.06 support=26.54 resistance=30.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=45.61 liquidity=4191566.25 spike=0.25
- ISMQ.CA: score=17.42 buy_ready=True sector_rank=16 price=9.3 support=8.1 resistance=10.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=50.61 liquidity=3943307.75 spike=0.03
- ISPH.CA: score=26.4 buy_ready=True sector_rank=2 price=11.86 support=11.2 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=40699784.0 spike=0.76
- JUFO.CA: score=14.89 buy_ready=False sector_rank=17 price=29.07 support=28.5 resistance=31.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=46.26 liquidity=6822607.0 spike=0.32
- KABO.CA: score=16.87 buy_ready=False sector_rank=8 price=8.53 support=6.04 resistance=8.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=95.35 liquidity=3471699.75 spike=0.09
- KWIN.CA: score=23.26 buy_ready=False sector_rank=13 price=95.92 support=65.0 resistance=95.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=91.8 liquidity=18215132.0 spike=0.54
- KZPC.CA: score=12.68 buy_ready=False sector_rank=13 price=8.63 support=8.26 resistance=9.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=57.84 liquidity=413117.25 spike=0.07
- LCSW.CA: score=26.4 buy_ready=False sector_rank=1 price=33.55 support=27.01 resistance=35.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=21 July 01:29 PM market time freshness=DELAYED_CURRENT RSI=89.62 liquidity=70618224.0 spike=0.96
- LUTS.CA: score=16.25 buy_ready=True sector_rank=13 price=0.74 support=0.69 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=1988309.12 spike=0.05
- MAAL.CA: score=14.2 buy_ready=False sector_rank=13 price=8.7 support=6.57 resistance=8.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=91.79 liquidity=933952.44 spike=0.05
- MASR.CA: score=20.16 buy_ready=False sector_rank=13 price=8.28 support=6.71 resistance=8.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=84.43 liquidity=8900656.0 spike=0.1
- MBSC.CA: score=18.36 buy_ready=False sector_rank=1 price=245.78 support=222.66 resistance=251.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:36 AM market time freshness=DELAYED_CURRENT RSI=68.55 liquidity=3958851.75 spike=0.22
- MCQE.CA: score=19.27 buy_ready=False sector_rank=1 price=190.1 support=166.66 resistance=191.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=80.37 liquidity=2865325.5 spike=0.17
- MCRO.CA: score=22.52 buy_ready=False sector_rank=13 price=1.42 support=1.17 resistance=1.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=78.79 liquidity=72478552.0 spike=1.13
- MENA.CA: score=18.75 buy_ready=True sector_rank=10 price=7.07 support=6.59 resistance=7.59 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=57.67 liquidity=4351698.23 spike=0.61
- MEPA.CA: score=12.08 buy_ready=False sector_rank=13 price=1.93 support=1.92 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43191772.0 spike=2.41
- MFPC.CA: score=18.22 buy_ready=False sector_rank=16 price=37.68 support=34.22 resistance=38.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=69.54 liquidity=7737691.0 spike=0.08
- MFSC.CA: score=9.8 buy_ready=False sector_rank=13 price=46.67 support=45.05 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=43.36 liquidity=532710.75 spike=0.07
- MHOT.CA: score=9.97 buy_ready=False sector_rank=21 price=16.86 support=16.12 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=37.28 liquidity=3574532.0 spike=0.24
- MICH.CA: score=11.62 buy_ready=False sector_rank=13 price=41.0 support=40.02 resistance=41.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28639534.0 spike=2.18
- MILS.CA: score=4.38 buy_ready=False sector_rank=13 price=170.68 support=168.23 resistance=173.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5113068.5 spike=0.18
- MIPH.CA: score=14.87 buy_ready=False sector_rank=2 price=760.29 support=630.13 resistance=780.0 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=85.68 liquidity=1471161.11 spike=0.43
- MOED.CA: score=13.96 buy_ready=False sector_rank=13 price=0.76 support=0.72 resistance=0.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41878704.0 spike=3.35
- MOIL.CA: score=13.43 buy_ready=False sector_rank=12 price=0.59 support=0.46 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=85.92 liquidity=33986.59 spike=0.08
- MOIN.CA: score=10.5 buy_ready=False sector_rank=13 price=24.04 support=22.6 resistance=24.76 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=65.07 liquidity=232466.81 spike=0.31
- MOSC.CA: score=17.78 buy_ready=True sector_rank=13 price=288.36 support=250.0 resistance=329.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=50.92 liquidity=1520059.13 spike=0.13
- MPCI.CA: score=23.26 buy_ready=False sector_rank=13 price=277.87 support=222.55 resistance=284.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=80.94 liquidity=28852750.0 spike=0.27
- MPCO.CA: score=15.5 buy_ready=True sector_rank=19 price=1.86 support=1.7 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=64.29 liquidity=2724139.25 spike=0.05
- MPRC.CA: score=15.55 buy_ready=False sector_rank=13 price=44.32 support=33.7 resistance=44.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=81.85 liquidity=2283000.25 spike=0.04
- MTIE.CA: score=18.77 buy_ready=True sector_rank=7 price=9.37 support=8.75 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=63.5 liquidity=2372399.0 spike=0.11
- NAHO.CA: score=3.27 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=10534.56 spike=0.4
- NCCW.CA: score=21.15 buy_ready=False sector_rank=13 price=6.6 support=5.82 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=74.42 liquidity=4884804.0 spike=0.2
- NEDA.CA: score=15.4 buy_ready=False sector_rank=13 price=2.86 support=2.7 resistance=3.02 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=66.67 liquidity=738923.87 spike=1.2
- NHPS.CA: score=9.26 buy_ready=False sector_rank=13 price=92.82 support=91.5 resistance=94.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=40329196.0 spike=0.6
- NINH.CA: score=21.26 buy_ready=False sector_rank=13 price=22.03 support=17.12 resistance=23.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=80.89 liquidity=16908754.0 spike=0.46
- NIPH.CA: score=25.4 buy_ready=False sector_rank=2 price=236.29 support=157.01 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=89.1 liquidity=80697216.0 spike=0.61
- OBRI.CA: score=26.26 buy_ready=True sector_rank=13 price=36.18 support=31.5 resistance=39.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=64.54 liquidity=21310770.0 spike=0.63
- OCDI.CA: score=15.38 buy_ready=False sector_rank=10 price=27.35 support=22.3 resistance=28.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=72.02 liquidity=982320.5 spike=0.01
- OCPH.CA: score=2.4 buy_ready=False sector_rank=13 price=457.95 support=454.5 resistance=473.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3138949.0 spike=0.15
- ODIN.CA: score=14.71 buy_ready=False sector_rank=13 price=2.54 support=2.05 resistance=2.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:34 AM market time freshness=DELAYED_CURRENT RSI=77.46 liquidity=3449330.5 spike=0.24
- OFH.CA: score=17.42 buy_ready=False sector_rank=13 price=0.71 support=0.57 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=91.02 liquidity=4157175.0 spike=0.08
- OIH.CA: score=17.58 buy_ready=False sector_rank=4 price=1.48 support=1.36 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=4184898.75 spike=0.06
- OLFI.CA: score=21.18 buy_ready=True sector_rank=17 price=23.4 support=21.0 resistance=23.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=66.0 liquidity=33708100.0 spike=1.06
- ORAS.CA: score=7.6 buy_ready=False sector_rank=20 price=714.97 support=712.01 resistance=715.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41174836.0 spike=1.0
- ORHD.CA: score=24.4 buy_ready=True sector_rank=10 price=39.68 support=37.0 resistance=40.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=56.22 liquidity=37339996.0 spike=0.25
- ORWE.CA: score=24.4 buy_ready=True sector_rank=8 price=23.14 support=21.95 resistance=23.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=67.92 liquidity=10033157.0 spike=0.48
- PHAR.CA: score=25.4 buy_ready=False sector_rank=2 price=91.5 support=83.6 resistance=92.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=75.44 liquidity=18038880.0 spike=0.56
- PHDC.CA: score=24.4 buy_ready=True sector_rank=10 price=15.3 support=14.26 resistance=15.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=109941576.0 spike=0.45
- PHTV.CA: score=13.15 buy_ready=False sector_rank=13 price=310.47 support=232.0 resistance=317.0 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=78.73 liquidity=1883000.56 spike=0.22
- POUL.CA: score=11.7 buy_ready=False sector_rank=17 price=38.8 support=35.94 resistance=41.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=57.53 liquidity=631541.31 spike=0.02
- PRCL.CA: score=19.14 buy_ready=True sector_rank=1 price=36.57 support=27.4 resistance=38.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=67.74 liquidity=3743751.75 spike=0.07
- PRDC.CA: score=24.4 buy_ready=True sector_rank=10 price=9.6 support=6.67 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=69.79 liquidity=13580750.0 spike=0.11
- PRMH.CA: score=15.21 buy_ready=False sector_rank=13 price=2.74 support=2.34 resistance=2.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=73.58 liquidity=941000.13 spike=0.04
- RACC.CA: score=13.73 buy_ready=False sector_rank=13 price=9.95 support=9.36 resistance=10.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=64.35 liquidity=2463518.25 spike=0.12
- RAKT.CA: score=12.92 buy_ready=False sector_rank=13 price=22.64 support=21.25 resistance=23.79 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=52.22 liquidity=340573.51 spike=1.16
- RAYA.CA: score=20.84 buy_ready=False sector_rank=18 price=7.6 support=6.99 resistance=8.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=15269947.0 spike=0.12
- RMDA.CA: score=16.8 buy_ready=False sector_rank=2 price=5.02 support=4.81 resistance=5.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=57.78 liquidity=3395936.25 spike=0.19
- ROTO.CA: score=19.63 buy_ready=True sector_rank=13 price=42.54 support=38.0 resistance=46.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=52.79 liquidity=5369558.5 spike=0.2
- RREI.CA: score=13.46 buy_ready=False sector_rank=13 price=3.78 support=3.34 resistance=4.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=76.39 liquidity=2195078.25 spike=0.08
- RTVC.CA: score=14.48 buy_ready=False sector_rank=13 price=4.09 support=3.55 resistance=4.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=79.75 liquidity=1212749.25 spike=0.27
- RUBX.CA: score=19.23 buy_ready=False sector_rank=13 price=13.87 support=9.97 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=70.96 liquidity=4967778.0 spike=0.07
- SAUD.CA: score=13.09 buy_ready=False sector_rank=14 price=22.04 support=19.99 resistance=21.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=68.13 liquidity=2083111.5 spike=0.39
- SCEM.CA: score=26.4 buy_ready=False sector_rank=1 price=77.76 support=60.14 resistance=81.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=84.16 liquidity=11247045.0 spike=0.25
- SCFM.CA: score=1.69 buy_ready=False sector_rank=13 price=273.73 support=271.0 resistance=276.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2430208.5 spike=0.15
- SCTS.CA: score=9.66 buy_ready=False sector_rank=11 price=609.33 support=540.0 resistance=649.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=75.94 liquidity=1255070.38 spike=0.21
- SDTI.CA: score=17.8 buy_ready=True sector_rank=13 price=49.17 support=45.55 resistance=48.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=66.95 liquidity=1531828.25 spike=0.28
- SEIG.CA: score=20.85 buy_ready=False sector_rank=13 price=237.55 support=182.01 resistance=285.0 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=71.05 liquidity=6584886.08 spike=0.29
- SIPC.CA: score=20.94 buy_ready=False sector_rank=13 price=3.9 support=3.25 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=84.52 liquidity=7680735.0 spike=0.58
- SKPC.CA: score=19.25 buy_ready=False sector_rank=16 price=16.1 support=14.8 resistance=16.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=51.23 liquidity=7767500.0 spike=0.22
- SMFR.CA: score=12.98 buy_ready=False sector_rank=13 price=228.94 support=187.01 resistance=277.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=76.07 liquidity=1711238.25 spike=0.09
- SNFC.CA: score=18.23 buy_ready=False sector_rank=13 price=11.29 support=11.21 resistance=12.39 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=37.11 liquidity=8970650.11 spike=0.84
- SPIN.CA: score=17.78 buy_ready=False sector_rank=8 price=14.95 support=13.8 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=82.18 liquidity=4381227.0 spike=0.32
- SPMD.CA: score=14.12 buy_ready=False sector_rank=13 price=0.45 support=0.41 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=81.67 liquidity=2855356.0 spike=0.13
- SUGR.CA: score=15.03 buy_ready=False sector_rank=17 price=47.67 support=45.31 resistance=48.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=62.91 liquidity=3969941.5 spike=0.75
- SVCE.CA: score=21.16 buy_ready=True sector_rank=13 price=9.39 support=8.76 resistance=10.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:40 AM market time freshness=DELAYED_CURRENT RSI=63.0 liquidity=6899672.5 spike=0.11
- SWDY.CA: score=22.27 buy_ready=False sector_rank=3 price=93.46 support=84.3 resistance=93.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=76.3 liquidity=9872456.0 spike=0.57
- TALM.CA: score=26.4 buy_ready=True sector_rank=11 price=16.15 support=15.27 resistance=16.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=53.09 liquidity=10950262.0 spike=0.84
- TMGH.CA: score=23.4 buy_ready=False sector_rank=10 price=101.71 support=92.1 resistance=103.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:38 AM market time freshness=DELAYED_CURRENT RSI=77.41 liquidity=36882140.0 spike=0.1
- TRTO.CA: score=12.52 buy_ready=False sector_rank=13 price=0.03 support=0.03 resistance=0.03 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=953.53 spike=2.13
- UEFM.CA: score=29.04 buy_ready=False sector_rank=13 price=550.37 support=460.0 resistance=625.0 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=73.56 liquidity=14273295.45 spike=3.39
- UEGC.CA: score=18.31 buy_ready=False sector_rank=13 price=2.38 support=1.33 resistance=2.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=96.67 liquidity=5049192.5 spike=0.12
- UNIP.CA: score=20.36 buy_ready=False sector_rank=13 price=0.42 support=0.29 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=90.48 liquidity=7100266.0 spike=0.38
- UNIT.CA: score=21.4 buy_ready=False sector_rank=10 price=18.92 support=12.0 resistance=21.39 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=76.36 liquidity=10558987.16 spike=0.38
- WCDF.CA: score=29.13 buy_ready=True sector_rank=13 price=586.58 support=504.0 resistance=634.15 source=Yahoo Finance as_of=2026-07-19T21:00:00+00:00 freshness=FRESH RSI=65.93 liquidity=9867449.05 spike=5.98
- WKOL.CA: score=14.73 buy_ready=False sector_rank=13 price=312.74 support=273.1 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:42 AM market time freshness=DELAYED_CURRENT RSI=71.52 liquidity=461749.47 spike=0.05
- ZEOT.CA: score=15.23 buy_ready=False sector_rank=13 price=11.72 support=10.4 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:41 AM market time freshness=DELAYED_CURRENT RSI=64.22 liquidity=966476.38 spike=0.02
- ZMID.CA: score=23.4 buy_ready=False sector_rank=10 price=7.48 support=6.19 resistance=7.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=09:39 AM market time freshness=DELAYED_CURRENT RSI=82.57 liquidity=38754328.0 spike=0.16

## Backtesting Lite
- WCDF.CA: 180d return=20.91%, max drawdown=-8.96%, MA20>MA50 days last20=0, as_of=2026-07-19T21:00:00+00:00
- UEFM.CA: 180d return=10.03%, max drawdown=-15.21%, MA20>MA50 days last20=5, as_of=2026-07-19T21:00:00+00:00
- ISPH.CA: 180d return=4.0%, max drawdown=-23.92%, MA20>MA50 days last20=17, as_of=2026-07-19T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- WCDF.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Middle & West Delta Flour Mills summary=Middle and West Delta Mills&#39; board approves EGP 25m capital raise through bonus shares; Middle and West Delta Mills approves EGP 13/shr dividend for FY20/21; Middle and West Delta Mills posts EGP 191m profit in FY20/21
  - Middle and West Delta Mills&#39; board approves EGP 25m capital raise through bonus shares: https://english.mubasher.info/news/4543138/Middle-and-West-Delta-Mills-board-approves-EGP-25m-capital-raise-through-bonus-shares/
  - Middle and West Delta Mills approves EGP 13/shr dividend for FY20/21: https://english.mubasher.info/news/3864614/Middle-and-West-Delta-Mills-approves-EGP-13-shr-dividend-for-FY20-21/
  - Middle and West Delta Mills posts EGP 191m profit in FY20/21: https://english.mubasher.info/news/3846031/Middle-and-West-Delta-Mills-posts-EGP-191m-profit-in-FY20-21/
- UEFM.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Upper Egypt Mills Company J.S.C summary=Upper Egypt Mills’ consolidated net profits retreat to EGP 52m in Q1-25/26; Upper Egypt Mills sells previous headquarters in Sohag; Upper Egypt Mills targets EGP 896m revenues in FY22/23
  - Upper Egypt Mills’ consolidated net profits retreat to EGP 52m in Q1-25/26: https://english.mubasher.info/news/4530741/Upper-Egypt-Mills-consolidated-net-profits-retreat-to-EGP-52m-in-Q1-25-26/
  - Upper Egypt Mills sells previous headquarters in Sohag: https://english.mubasher.info/news/4007606/Upper-Egypt-Mills-sells-previous-headquarters-in-Sohag/
  - Upper Egypt Mills targets EGP 896m revenues in FY22/23: https://english.mubasher.info/news/3973984/Upper-Egypt-Mills-targets-EGP-896m-revenues-in-FY22-23/
- ISPH.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=567 sources=3 expected=Ibn Sina Pharma summary=Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025; EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse; Ibnsina Pharma pens import, distribution deal with OMRON Healthcare
  - Ibnsina Pharma’s consolidated profits jump to EGP 952m in 2025: https://english.mubasher.info/news/4563237/Ibnsina-Pharma-s-consolidated-profits-jump-to-EGP-952m-in-2025/
  - EBRD grants EGP 1.3bn loan to Ibnsina Pharma for new warehouse: https://english.mubasher.info/news/4552027/EBRD-grants-EGP-1-3bn-loan-to-Ibnsina-Pharma-for-new-warehouse/
  - Ibnsina Pharma pens import, distribution deal with OMRON Healthcare: https://english.mubasher.info/news/4028068/Ibnsina-Pharma-pens-import-distribution-deal-with-OMRON-Healthcare/
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=567 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- AFDI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Al Ahly for Development & Investment summary=Al Ahly for Development and Investment stock breaks downtrend line; Al Ahly for Development and Investment weighs exiting subsidiary; Pico Investments ups stake in AFDI to over 15%
  - Al Ahly for Development and Investment stock breaks downtrend line: https://english.mubasher.info/news/4597902/Al-Ahly-for-Development-and-Investment-stock-breaks-downtrend-line/
  - Al Ahly for Development and Investment weighs exiting subsidiary: https://english.mubasher.info/news/4309777/Al-Ahly-for-Development-and-Investment-weighs-exiting-subsidiary/
  - Pico Investments ups stake in AFDI to over 15%: https://english.mubasher.info/news/4078120/Pico-Investments-ups-stake-in-AFDI-to-over-15-/
- OBRI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El-Ebour Co. for Real Estate Investment S.A.E. summary=El Obour for Real Estate advances UAE expansion via new subsidiary; El Obour for Real Estate registers EGP 39m consolidated net profits in 9M-25; El Ebour for Real Estate expands business in UAE
  - El Obour for Real Estate advances UAE expansion via new subsidiary: https://english.mubasher.info/news/4547120/El-Obour-for-Real-Estate-advances-UAE-expansion-via-new-subsidiary/
  - El Obour for Real Estate registers EGP 39m consolidated net profits in 9M-25: https://english.mubasher.info/news/4527519/El-Obour-for-Real-Estate-registers-EGP-39m-consolidated-net-profits-in-9M-25/
  - El Ebour for Real Estate expands business in UAE: https://english.mubasher.info/news/4469178/El-Ebour-for-Real-Estate-expands-business-in-UAE/

## Warnings
- Evidence for WCDF.CA matches the company but no source/report date was detected.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence for UEFM.CA matches the company but no source/report date was detected.
- Evidence for ISPH.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AFDI.CA matches the company but no source/report date was detected.
- Evidence for OBRI.CA matches the company but no source/report date was detected.
