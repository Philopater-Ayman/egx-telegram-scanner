# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-09T10:09:55.700398+00:00
Generated Cairo: 2026-09-09 13:09
Run timing: target 08:45 Cairo | generated Cairo 2026-09-09 13:09 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-09 13:05

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 68
- Data quality issues: 1
- Tradeable price/liquidity tickers: 180/189
- Top sector: Building Materials

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, September 09
- Freshness: DELAYED
- EGX30 regime: BULLISH / above MA20 65.0% / above MA50 80.0%
- EGX70 regime: CONSTRUCTIVE / above MA20 55.0% / above MA50 72.5%
- Sector breadth: 66.67%
- Risk mode: BROAD_RISK_ON

## Top Liquidity
- CCAP.CA: liquidity=439281984.0 spike=0.65 score=28.9
- AMES.CA: liquidity=303886208.0 spike=1.6 score=15.43
- ETEL.CA: liquidity=287633632.0 spike=1.81 score=29.52
- TMGH.CA: liquidity=227704032.0 spike=0.83 score=27.16
- COMI.CA: liquidity=193720480.0 spike=0.36 score=25.9

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 shows a bullish bias while EGX70 is constructive, sector breadth is 66.7% and risk mode is broad risk on; the scanner ranked several tickets with bullish watch outlooks but flagged cooling liquidity, near‑resistance levels and mixed evidence, resulting in a fallback HOLD recommendation.
- The EGX30 bullish (65% above MA20, 80% above MA50) and EGX70 constructive backdrop lifts risk mode to broad risk on, increasing buy tolerance but also heightening uncertainty when fundamental evidence is weak or missing.

## Top Liquidity Spikes
- EASB.CA: spike=8.04 liquidity=60912188.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- NCCW.CA: spike=6.02 liquidity=175709328.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELNA.CA: spike=3.62 liquidity=1546769.66 outlook=NEUTRAL score=47.32 buy_ready=False
- UEFM.CA: spike=2.82 liquidity=11694230.17 outlook=CONSTRUCTIVE score=64.32 buy_ready=False
- ASPI.CA: spike=2.75 liquidity=120222648.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=11.37 5d=1.93% 20d=27.22% aboveMA50=83.33%
- #2 Textiles: score=11.26 5d=3.2% 20d=18.61% aboveMA50=100.0%
- #3 Investment Holding: score=11.14 5d=1.98% 20d=16.86% aboveMA50=100.0%
- #4 Telecommunications: score=11.07 5d=3.79% 20d=6.46% aboveMA50=100.0%
- #5 Agriculture & Food Production: score=10.09 5d=4.84% 20d=7.08% aboveMA50=100.0%
- #6 Basic Resources & Chemicals: score=9.66 5d=5.2% 20d=10.97% aboveMA50=80.0%
- #7 Transportation & Logistics: score=9.18 5d=3.19% 20d=8.25% aboveMA50=100.0%
- #8 Industrial Goods & Cables: score=7.26 5d=3.17% 20d=10.57% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local fallback HOLD: no candidate passed evidence, liquidity, freshness, and technical gates.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EFIC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- LCSW.CA: BULLISH_WATCH score=96 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ETEL.CA: BULLISH_WATCH score=93 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance
- KABO.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ARCC.CA: BULLISH_WATCH score=90 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- RUBX.CA: BULLISH_WATCH score=86.32 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- MEPA.CA: BULLISH_WATCH score=86.32 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SCEM.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- IFAP.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SPIN.CA: BULLISH_WATCH score=86 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support

## BUY-Ready Candidates
- ORWE.CA: rank=29.9 outlook=BULLISH_WATCH outlook_score=76 sector_rank=2 price=28.11 support=24.5 resistance=29.41 liquidity=18922502.0
- RUBX.CA: rank=29.61 outlook=BULLISH_WATCH outlook_score=86.32 sector_rank=13 price=13.6 support=12.2 resistance=13.94 liquidity=41413588.0
- ETEL.CA: rank=29.52 outlook=BULLISH_WATCH outlook_score=93 sector_rank=4 price=123.99 support=107.0 resistance=126.4 liquidity=287633632.0
- SCEM.CA: rank=28.9 outlook=BULLISH_WATCH outlook_score=86 sector_rank=1 price=100.49 support=82.34 resistance=113.0 liquidity=23664400.0
- MEPA.CA: rank=28.49 outlook=BULLISH_WATCH outlook_score=86.32 sector_rank=13 price=2.09 support=1.8 resistance=2.25 liquidity=55204624.0
- GBCO.CA: rank=28.4 outlook=BULLISH_WATCH outlook_score=80.5 sector_rank=12 price=31.27 support=27.51 resistance=32.45 liquidity=73235912.0
- EFIC.CA: rank=28.32 outlook=BULLISH_WATCH outlook_score=100 sector_rank=6 price=215.08 support=192.75 resistance=260.0 liquidity=163017808.0
- LCSW.CA: rank=27.92 outlook=BULLISH_WATCH outlook_score=96 sector_rank=1 price=35.05 support=32.12 resistance=37.5 liquidity=9021325.0
- FWRY.CA: rank=27.9 outlook=BULLISH_WATCH outlook_score=71.3 sector_rank=10 price=19.21 support=18.66 resistance=19.69 liquidity=24847840.0
- SWDY.CA: rank=27.9 outlook=CONSTRUCTIVE outlook_score=68.26 sector_rank=8 price=130.12 support=106.51 resistance=139.7 liquidity=69636432.0

## Data Quality Issues
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=12.66 buy_ready=False sector_rank=13 price=304.64 support=288.03 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=22.53 liquidity=4436402.5 spike=0.11
- ABUK.CA: score=25.9 buy_ready=False sector_rank=6 price=91.99 support=73.2 resistance=94.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=72.23 liquidity=115014624.0 spike=0.72
- ACAMD.CA: score=22.23 buy_ready=False sector_rank=13 price=2.09 support=1.95 resistance=2.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=46.27 liquidity=21241202.0 spike=0.37
- ACGC.CA: score=27.22 buy_ready=False sector_rank=2 price=15.2 support=10.36 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=70.04 liquidity=7317964.5 spike=0.17
- ADCI.CA: score=13.89 buy_ready=False sector_rank=13 price=292.66 support=280.0 resistance=389.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=662360.44 spike=0.06
- ADIB.CA: score=18.9 buy_ready=False sector_rank=11 price=51.36 support=51.58 resistance=55.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=32.31 liquidity=35863108.0 spike=0.5
- ADPC.CA: score=17.48 buy_ready=False sector_rank=13 price=3.99 support=3.85 resistance=4.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=31.91 liquidity=9251694.0 spike=0.26
- AFDI.CA: score=10.88 buy_ready=False sector_rank=13 price=54.43 support=53.54 resistance=69.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=30.17 liquidity=2656554.5 spike=0.09
- AFMC.CA: score=18.23 buy_ready=False sector_rank=13 price=168.36 support=157.0 resistance=300.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=18.46 liquidity=33872148.0 spike=0.34
- AJWA.CA: score=11.48 buy_ready=False sector_rank=13 price=180.04 support=175.15 resistance=202.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=19.02 liquidity=6247260.5 spike=0.11
- ALCN.CA: score=25.62 buy_ready=True sector_rank=7 price=31.91 support=30.03 resistance=34.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=56.87 liquidity=7722491.0 spike=0.23
- ALUM.CA: score=20.41 buy_ready=True sector_rank=13 price=28.66 support=25.5 resistance=30.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=48.63 liquidity=5183980.0 spike=0.19
- AMER.CA: score=20.7 buy_ready=False sector_rank=16 price=5.56 support=5.3 resistance=8.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=36.45 liquidity=7540013.5 spike=0.09
- AMES.CA: score=15.43 buy_ready=False sector_rank=13 price=62.71 support=64.4 resistance=173.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=23.68 liquidity=303886208.0 spike=1.6
- AMIA.CA: score=18.01 buy_ready=True sector_rank=13 price=18.9 support=10.6 resistance=22.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=66.25 liquidity=4777102.0 spike=0.07
- AMOC.CA: score=24.16 buy_ready=False sector_rank=15 price=14.0 support=9.21 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=77.52 liquidity=130024464.0 spike=0.73
- APSW.CA: score=9.84 buy_ready=False sector_rank=13 price=8.67 support=8.41 resistance=9.39 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=46.07 liquidity=615283.9 spike=0.52
- ARAB.CA: score=25.16 buy_ready=True sector_rank=16 price=0.26 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=31868652.0 spike=0.32
- ARCC.CA: score=25.13 buy_ready=True sector_rank=1 price=76.43 support=63.7 resistance=91.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=58.35 liquidity=6230546.0 spike=0.06
- AREH.CA: score=27.23 buy_ready=True sector_rank=13 price=1.53 support=1.39 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=20296364.0 spike=0.83
- ARVA.CA: score=10.23 buy_ready=False sector_rank=13 price=14.99 support=14.45 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=16 August 01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30473338.0 spike=0.56
- ASCM.CA: score=24.96 buy_ready=True sector_rank=13 price=64.17 support=62.01 resistance=69.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=61.72 liquidity=9733337.0 spike=0.32
- ASPI.CA: score=13.73 buy_ready=False sector_rank=13 price=0.43 support=0.42 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120222648.0 spike=2.75
- ATLC.CA: score=24.4 buy_ready=False sector_rank=19 price=6.98 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=72.09 liquidity=9831522.0 spike=0.33
- ATQA.CA: score=27.9 buy_ready=False sector_rank=6 price=12.62 support=10.74 resistance=12.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=72.88 liquidity=41591200.0 spike=0.37
- AXPH.CA: score=14.76 buy_ready=False sector_rank=13 price=1676.49 support=1281.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=89.73 liquidity=2527201.5 spike=0.21
- BINV.CA: score=19.49 buy_ready=True sector_rank=3 price=52.1 support=46.25 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=67.7 liquidity=2589235.25 spike=0.24
- BIOC.CA: score=18.23 buy_ready=False sector_rank=13 price=312.33 support=310.03 resistance=563.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=23.99 liquidity=19560422.0 spike=0.09
- BTFH.CA: score=20.57 buy_ready=False sector_rank=19 price=2.97 support=2.94 resistance=3.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=33386852.0 spike=0.23
- CAED.CA: score=10.23 buy_ready=False sector_rank=13 price=126.56 support=123.56 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26255326.0 spike=0.74
- CANA.CA: score=19.98 buy_ready=True sector_rank=11 price=43.31 support=39.62 resistance=44.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=62.48 liquidity=2076191.38 spike=0.12
- CCAP.CA: score=28.9 buy_ready=False sector_rank=3 price=6.17 support=5.18 resistance=6.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=73.53 liquidity=439281984.0 spike=0.65
- CCRS.CA: score=20.44 buy_ready=True sector_rank=13 price=2.69 support=2.4 resistance=3.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=53.52 liquidity=5215325.5 spike=0.1
- CEFM.CA: score=16.64 buy_ready=True sector_rank=13 price=148.96 support=132.0 resistance=168.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=65.19 liquidity=3412834.25 spike=0.19
- CERA.CA: score=28.31 buy_ready=False sector_rank=13 price=1.76 support=1.22 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=74.12 liquidity=121325936.0 spike=2.54
- CFGH.CA: score=16.26 buy_ready=False sector_rank=13 price=0.12 support=0.1 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:23 AM market time freshness=DELAYED_CURRENT RSI=72.22 liquidity=34966.5 spike=1.5
- CICH.CA: score=24.22 buy_ready=True sector_rank=19 price=13.03 support=12.0 resistance=13.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:43 AM market time freshness=DELAYED_CURRENT RSI=58.9 liquidity=5175401.0 spike=1.24
- CIEB.CA: score=22.39 buy_ready=True sector_rank=11 price=25.53 support=24.0 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=56.07 liquidity=4492242.5 spike=0.29
- CIRA.CA: score=27.9 buy_ready=True sector_rank=9 price=37.5 support=32.1 resistance=40.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=54.28 liquidity=15122714.0 spike=0.45
- CLHO.CA: score=19.86 buy_ready=False sector_rank=18 price=16.44 support=16.75 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=45.07 liquidity=72137840.0 spike=0.98
- CNFN.CA: score=14.44 buy_ready=False sector_rank=19 price=4.83 support=4.73 resistance=5.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=4872414.0 spike=0.26
- COMI.CA: score=25.9 buy_ready=False sector_rank=11 price=138.6 support=135.35 resistance=142.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=50.12 liquidity=193720480.0 spike=0.36
- COPR.CA: score=23.23 buy_ready=False sector_rank=13 price=0.49 support=0.4 resistance=0.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=45.41 liquidity=11318204.0 spike=0.12
- COSG.CA: score=27.23 buy_ready=True sector_rank=13 price=1.9 support=1.7 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=60.47 liquidity=12827436.0 spike=0.22
- CPCI.CA: score=14.09 buy_ready=False sector_rank=13 price=538.93 support=520.0 resistance=644.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=53.52 liquidity=861055.94 spike=0.13
- CSAG.CA: score=18.76 buy_ready=True sector_rank=7 price=41.15 support=38.13 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=2864083.5 spike=0.11
- DAPH.CA: score=25.23 buy_ready=True sector_rank=13 price=131.25 support=108.11 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=53.01 liquidity=12229974.0 spike=0.16
- DEIN.CA: score=13.23 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=15.01 buy_ready=False sector_rank=14 price=28.33 support=27.79 resistance=30.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=43.73 liquidity=1803362.75 spike=0.18
- DSCW.CA: score=17.19 buy_ready=False sector_rank=13 price=1.91 support=1.84 resistance=2.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=6966948.0 spike=0.1
- DTPP.CA: score=18.8 buy_ready=True sector_rank=13 price=301.16 support=290.0 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=67.85 liquidity=5568484.0 spike=0.15
- EALR.CA: score=8.72 buy_ready=False sector_rank=13 price=374.88 support=340.0 resistance=471.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=24.24 liquidity=3494961.0 spike=0.1
- EASB.CA: score=15.23 buy_ready=False sector_rank=13 price=8.17 support=7.46 resistance=8.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60912188.0 spike=8.04
- EAST.CA: score=19.83 buy_ready=False sector_rank=14 price=35.3 support=35.0 resistance=37.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=8626175.0 spike=0.14
- EBSC.CA: score=27.33 buy_ready=True sector_rank=13 price=2.16 support=1.88 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=14643223.0 spike=1.05
- ECAP.CA: score=7.64 buy_ready=False sector_rank=13 price=33.26 support=31.16 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=27.99 liquidity=2408337.0 spike=0.13
- EDFM.CA: score=15.8 buy_ready=False sector_rank=13 price=420.16 support=394.0 resistance=432.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=54.33 liquidity=570918.0 spike=0.29
- EEII.CA: score=9.62 buy_ready=False sector_rank=13 price=2.34 support=2.33 resistance=3.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=15.42 liquidity=4393192.5 spike=0.14
- EFIC.CA: score=28.32 buy_ready=True sector_rank=6 price=215.08 support=192.75 resistance=260.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=48.51 liquidity=163017808.0 spike=2.21
- EFID.CA: score=25.21 buy_ready=True sector_rank=14 price=32.09 support=29.71 resistance=34.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=41.13 liquidity=60452976.0 spike=0.83
- EFIH.CA: score=23.9 buy_ready=False sector_rank=10 price=23.65 support=22.16 resistance=25.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=40.61 liquidity=25009374.0 spike=0.27
- EGAL.CA: score=25.9 buy_ready=True sector_rank=6 price=375.96 support=303.26 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=68.13 liquidity=54565156.0 spike=0.33
- EGAS.CA: score=17.95 buy_ready=False sector_rank=15 price=58.46 support=55.21 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=48.11 liquidity=4783543.0 spike=0.36
- EGBE.CA: score=13.93 buy_ready=False sector_rank=11 price=0.51 support=0.51 resistance=0.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:24 AM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=32563.4 spike=0.16
- EGCH.CA: score=27.9 buy_ready=True sector_rank=6 price=14.05 support=13.3 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=46.57 liquidity=42493816.0 spike=0.32
- EGSA.CA: score=13.31 buy_ready=False sector_rank=4 price=9.04 support=8.65 resistance=9.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 12:41 PM market time freshness=DELAYED_CURRENT RSI=85.42 liquidity=10849.0 spike=1.2
- EGTS.CA: score=18.18 buy_ready=False sector_rank=16 price=17.41 support=16.17 resistance=20.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=36.16 liquidity=8022520.0 spike=0.24
- EHDR.CA: score=11.61 buy_ready=False sector_rank=13 price=2.92 support=2.81 resistance=3.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=3382206.25 spike=0.1
- EKHO.CA: score=11.16 buy_ready=False sector_rank=15 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=21.9 buy_ready=False sector_rank=8 price=2.08 support=2.04 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=30083682.0 spike=0.47
- ELKA.CA: score=23.97 buy_ready=True sector_rank=13 price=1.8 support=1.7 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=6746445.0 spike=0.11
- ELNA.CA: score=17.77 buy_ready=False sector_rank=13 price=37.02 support=36.1 resistance=38.99 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=40.52 liquidity=1546769.66 spike=3.62
- ELSH.CA: score=24.23 buy_ready=False sector_rank=13 price=13.6 support=12.97 resistance=14.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=18360978.0 spike=0.4
- ELWA.CA: score=15.83 buy_ready=True sector_rank=13 price=1.86 support=1.62 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=55.95 liquidity=1604305.5 spike=0.68
- EMFD.CA: score=22.16 buy_ready=False sector_rank=16 price=14.48 support=11.51 resistance=15.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=97.9 liquidity=30833012.0 spike=0.19
- ENGC.CA: score=18.71 buy_ready=False sector_rank=13 price=44.98 support=41.8 resistance=54.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=35.43 liquidity=5484895.5 spike=0.25
- EOSB.CA: score=17.27 buy_ready=False sector_rank=13 price=1.57 support=1.5 resistance=1.64 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=41135.57 spike=0.73
- EPCO.CA: score=10.4 buy_ready=False sector_rank=13 price=11.02 support=10.8 resistance=13.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=23.21 liquidity=2169950.75 spike=0.14
- EPPK.CA: score=7.59 buy_ready=False sector_rank=13 price=9.78 support=10.29 resistance=13.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=27.53 liquidity=2206221.25 spike=1.58
- ETEL.CA: score=29.52 buy_ready=True sector_rank=4 price=123.99 support=107.0 resistance=126.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=287633632.0 spike=1.81
- ETRS.CA: score=22.37 buy_ready=True sector_rank=13 price=11.26 support=10.61 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=50.81 liquidity=5140446.5 spike=0.21
- EXPA.CA: score=23.08 buy_ready=True sector_rank=11 price=21.43 support=19.8 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=53.07 liquidity=5181123.0 spike=0.13
- FAIT.CA: score=20.23 buy_ready=True sector_rank=11 price=47.81 support=37.01 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=69.21 liquidity=2333423.0 spike=0.26
- FAITA.CA: score=10.92 buy_ready=False sector_rank=11 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT RSI=48.75 liquidity=24425.04 spike=0.44
- FERC.CA: score=22.46 buy_ready=True sector_rank=6 price=79.39 support=76.7 resistance=87.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=57.72 liquidity=4557907.0 spike=0.2
- FWRY.CA: score=27.9 buy_ready=True sector_rank=10 price=19.21 support=18.66 resistance=19.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=54.29 liquidity=24847840.0 spike=0.15
- GBCO.CA: score=28.4 buy_ready=True sector_rank=12 price=31.27 support=27.51 resistance=32.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=49.93 liquidity=73235912.0 spike=1.55
- GDWA.CA: score=22.52 buy_ready=True sector_rank=13 price=0.81 support=0.77 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=51.23 liquidity=9292158.0 spike=0.2
- GGCC.CA: score=17.67 buy_ready=False sector_rank=13 price=0.85 support=0.83 resistance=1.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=37.85 liquidity=4445830.0 spike=0.09
- GIHD.CA: score=27.23 buy_ready=True sector_rank=13 price=74.72 support=58.01 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=67.77 liquidity=25567904.0 spike=0.9
- GMCI.CA: score=10.41 buy_ready=False sector_rank=13 price=1.88 support=1.83 resistance=2.03 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=37.5 liquidity=185721.44 spike=0.42
- GRCA.CA: score=10.23 buy_ready=False sector_rank=13 price=76.98 support=76.6 resistance=81.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33845876.0 spike=0.49
- GSSC.CA: score=20.7 buy_ready=True sector_rank=13 price=306.18 support=274.0 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=68.15 liquidity=3472042.5 spike=0.25
- GTWL.CA: score=25.23 buy_ready=False sector_rank=13 price=243.13 support=121.55 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=72.49 liquidity=71042576.0 spike=0.22
- HDBK.CA: score=22.9 buy_ready=False sector_rank=11 price=115.51 support=84.21 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=75.28 liquidity=10879250.0 spike=0.21
- HELI.CA: score=27.16 buy_ready=True sector_rank=16 price=8.03 support=7.34 resistance=8.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=63.93 liquidity=57900312.0 spike=0.36
- HRHO.CA: score=20.57 buy_ready=False sector_rank=19 price=25.81 support=25.33 resistance=27.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=41.64 liquidity=19690890.0 spike=0.16
- ICID.CA: score=17.29 buy_ready=False sector_rank=13 price=18.35 support=9.0 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=70.44 liquidity=4060800.0 spike=0.13
- IDRE.CA: score=17.77 buy_ready=True sector_rank=13 price=55.04 support=51.02 resistance=58.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=45.24 liquidity=2542312.0 spike=0.17
- IFAP.CA: score=24.57 buy_ready=True sector_rank=5 price=21.38 support=20.2 resistance=22.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=6674547.5 spike=0.22
- INFI.CA: score=20.91 buy_ready=False sector_rank=13 price=147.82 support=140.66 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=40.95 liquidity=7684389.0 spike=0.12
- IRON.CA: score=14.9 buy_ready=False sector_rank=6 price=29.5 support=29.15 resistance=33.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=4.55 liquidity=11247256.0 spike=0.87
- ISMA.CA: score=16.01 buy_ready=False sector_rank=13 price=32.06 support=29.0 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=38.61 liquidity=2777859.75 spike=0.11
- ISMQ.CA: score=22.9 buy_ready=False sector_rank=6 price=9.2 support=9.0 resistance=9.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=48.78 liquidity=10046565.0 spike=0.24
- ISPH.CA: score=22.86 buy_ready=False sector_rank=18 price=13.1 support=12.75 resistance=16.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=20027664.0 spike=0.18
- JUFO.CA: score=26.21 buy_ready=False sector_rank=14 price=27.13 support=26.07 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=53.61 liquidity=10008227.0 spike=0.29
- KABO.CA: score=25.86 buy_ready=True sector_rank=2 price=9.3 support=8.47 resistance=9.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=51.45 liquidity=7955949.5 spike=0.17
- KWIN.CA: score=23.23 buy_ready=False sector_rank=13 price=93.14 support=84.08 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=52.26 liquidity=22387188.0 spike=0.34
- KZPC.CA: score=23.65 buy_ready=True sector_rank=13 price=14.4 support=9.0 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=65.58 liquidity=73573016.0 spike=1.21
- LCSW.CA: score=27.92 buy_ready=True sector_rank=1 price=35.05 support=32.12 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=54.33 liquidity=9021325.0 spike=0.27
- LUTS.CA: score=23.23 buy_ready=False sector_rank=13 price=0.92 support=0.79 resistance=1.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=36.66 liquidity=41732500.0 spike=0.15
- MAAL.CA: score=21.59 buy_ready=False sector_rank=13 price=9.1 support=8.32 resistance=10.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=61.17 liquidity=6364481.0 spike=0.46
- MASR.CA: score=25.23 buy_ready=False sector_rank=13 price=8.19 support=7.45 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=76111856.0 spike=0.94
- MBSC.CA: score=27.58 buy_ready=True sector_rank=1 price=416.07 support=265.51 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=62.78 liquidity=8681960.0 spike=0.09
- MCQE.CA: score=21.64 buy_ready=True sector_rank=1 price=242.0 support=201.0 resistance=292.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=69.95 liquidity=4742591.5 spike=0.07
- MCRO.CA: score=26.47 buy_ready=True sector_rank=13 price=1.74 support=1.44 resistance=1.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=69.05 liquidity=177587344.0 spike=1.62
- MENA.CA: score=5.54 buy_ready=False sector_rank=16 price=6.75 support=6.58 resistance=7.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=30.69 liquidity=385354.28 spike=0.07
- MEPA.CA: score=28.49 buy_ready=True sector_rank=13 price=2.09 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=61.45 liquidity=55204624.0 spike=1.63
- MFPC.CA: score=24.9 buy_ready=False sector_rank=6 price=47.12 support=36.98 resistance=47.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=85.17 liquidity=53514820.0 spike=0.41
- MFSC.CA: score=18.54 buy_ready=True sector_rank=13 price=50.78 support=48.0 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=58.53 liquidity=1310144.0 spike=0.18
- MHOT.CA: score=15.97 buy_ready=False sector_rank=17 price=18.07 support=17.4 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=37.19 liquidity=2030040.13 spike=0.11
- MICH.CA: score=21.48 buy_ready=True sector_rank=13 price=50.48 support=46.3 resistance=53.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=49.29 liquidity=6251120.0 spike=0.2
- MILS.CA: score=15.91 buy_ready=False sector_rank=13 price=203.92 support=179.05 resistance=248.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=29.65 liquidity=7684215.0 spike=0.11
- MIPH.CA: score=16.46 buy_ready=True sector_rank=18 price=804.33 support=700.2 resistance=827.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=60.47 liquidity=1597587.25 spike=0.37
- MOED.CA: score=27.23 buy_ready=True sector_rank=13 price=0.81 support=0.68 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=61.24 liquidity=37123436.0 spike=0.33
- MOIL.CA: score=15.27 buy_ready=False sector_rank=15 price=0.68 support=0.65 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=59.18 liquidity=106013.58 spike=0.43
- MOIN.CA: score=27.23 buy_ready=True sector_rank=13 price=41.17 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=62.33 liquidity=22652266.0 spike=0.5
- MOSC.CA: score=14.11 buy_ready=False sector_rank=13 price=319.16 support=300.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=38.03 liquidity=885310.25 spike=0.07
- MPCI.CA: score=23.23 buy_ready=True sector_rank=13 price=425.0 support=345.0 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=68.12 liquidity=48650868.0 spike=0.26
- MPCO.CA: score=25.9 buy_ready=True sector_rank=5 price=2.3 support=2.07 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=79861080.0 spike=0.76
- MPRC.CA: score=15.73 buy_ready=False sector_rank=13 price=40.15 support=39.5 resistance=52.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=5501399.5 spike=0.13
- MTIE.CA: score=20.67 buy_ready=False sector_rank=12 price=8.56 support=8.25 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=40.22 liquidity=8370118.0 spike=0.13
- NAHO.CA: score=10.25 buy_ready=False sector_rank=13 price=0.14 support=0.1 resistance=0.16 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=25.0 liquidity=21727.71 spike=0.2
- NCCW.CA: score=15.23 buy_ready=False sector_rank=13 price=7.36 support=6.3 resistance=7.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=175709328.0 spike=6.02
- NEDA.CA: score=17.86 buy_ready=False sector_rank=13 price=2.88 support=2.7 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=629954.94 spike=0.68
- NHPS.CA: score=16.37 buy_ready=False sector_rank=13 price=83.03 support=84.03 resistance=98.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=35.56 liquidity=6139145.0 spike=0.2
- NINH.CA: score=18.61 buy_ready=True sector_rank=13 price=23.29 support=21.53 resistance=26.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=61.53 liquidity=3380168.75 spike=0.11
- NIPH.CA: score=22.86 buy_ready=False sector_rank=18 price=335.1 support=326.51 resistance=450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=41.91 liquidity=32957940.0 spike=0.1
- OBRI.CA: score=19.22 buy_ready=False sector_rank=13 price=32.56 support=31.81 resistance=34.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=42.71 liquidity=7987976.0 spike=0.32
- OCDI.CA: score=19.03 buy_ready=True sector_rank=16 price=33.65 support=30.03 resistance=36.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=50.43 liquidity=3874780.0 spike=0.03
- OCPH.CA: score=13.43 buy_ready=False sector_rank=13 price=252.31 support=242.0 resistance=341.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=41.63 liquidity=2205778.25 spike=0.12
- ODIN.CA: score=12.45 buy_ready=False sector_rank=13 price=2.88 support=2.55 resistance=3.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=19.83 liquidity=4224935.5 spike=0.1
- OFH.CA: score=23.23 buy_ready=False sector_rank=13 price=1.11 support=0.86 resistance=1.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=72.15 liquidity=81850648.0 spike=0.67
- OIH.CA: score=24.9 buy_ready=False sector_rank=3 price=2.11 support=1.62 resistance=2.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=102327040.0 spike=0.66
- OLFI.CA: score=14.59 buy_ready=False sector_rank=14 price=22.97 support=22.07 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=4380453.5 spike=0.09
- ORAS.CA: score=9.1 buy_ready=False sector_rank=20 price=860.57 support=844.0 resistance=863.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103186208.0 spike=1.0
- ORHD.CA: score=23.16 buy_ready=False sector_rank=16 price=41.82 support=40.28 resistance=43.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=60.27 liquidity=43536052.0 spike=0.34
- ORWE.CA: score=29.9 buy_ready=True sector_rank=2 price=28.11 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=63.86 liquidity=18922502.0 spike=0.22
- PHAR.CA: score=22.86 buy_ready=False sector_rank=18 price=128.15 support=124.5 resistance=178.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=28014692.0 spike=0.08
- PHDC.CA: score=20.16 buy_ready=False sector_rank=16 price=14.5 support=14.4 resistance=16.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=35.07 liquidity=63646060.0 spike=0.28
- PHTV.CA: score=13.95 buy_ready=False sector_rank=13 price=349.08 support=311.27 resistance=447.99 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=37.18 liquidity=723293.73 spike=0.34
- POUL.CA: score=22.09 buy_ready=True sector_rank=14 price=39.13 support=36.97 resistance=40.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=59.64 liquidity=4884696.0 spike=0.24
- PRCL.CA: score=16.38 buy_ready=False sector_rank=1 price=32.49 support=30.9 resistance=36.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=38.84 liquidity=2484161.0 spike=0.11
- PRDC.CA: score=16.38 buy_ready=False sector_rank=16 price=8.39 support=8.33 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=44.56 liquidity=6219667.5 spike=0.09
- PRMH.CA: score=19.09 buy_ready=True sector_rank=13 price=2.8 support=2.28 resistance=2.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=62.79 liquidity=1865022.63 spike=0.13
- RACC.CA: score=21.6 buy_ready=True sector_rank=13 price=10.07 support=9.4 resistance=10.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=41.15 liquidity=4376206.0 spike=0.17
- RAKT.CA: score=14.36 buy_ready=False sector_rank=13 price=22.7 support=21.4 resistance=24.0 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=65.77 liquidity=129617.0 spike=0.46
- RAYA.CA: score=20.42 buy_ready=False sector_rank=21 price=7.2 support=6.95 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=53.29 liquidity=13612272.0 spike=0.2
- RMDA.CA: score=24.86 buy_ready=True sector_rank=18 price=6.3 support=5.77 resistance=7.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=36273956.0 spike=0.44
- ROTO.CA: score=10.93 buy_ready=False sector_rank=13 price=42.91 support=43.01 resistance=52.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=9.5 liquidity=5700544.0 spike=0.31
- RREI.CA: score=10.39 buy_ready=False sector_rank=13 price=4.34 support=4.24 resistance=5.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=23.01 liquidity=2166469.0 spike=0.06
- RTVC.CA: score=15.41 buy_ready=False sector_rank=13 price=3.98 support=3.76 resistance=4.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:38 AM market time freshness=DELAYED_CURRENT RSI=52.04 liquidity=2178164.0 spike=0.28
- RUBX.CA: score=29.61 buy_ready=True sector_rank=13 price=13.6 support=12.2 resistance=13.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=54.93 liquidity=41413588.0 spike=2.19
- SAUD.CA: score=18.08 buy_ready=False sector_rank=11 price=23.34 support=22.13 resistance=24.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=4176212.25 spike=0.21
- SCEM.CA: score=28.9 buy_ready=True sector_rank=1 price=100.49 support=82.34 resistance=113.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=50.41 liquidity=23664400.0 spike=0.11
- SCFM.CA: score=10.52 buy_ready=False sector_rank=13 price=280.8 support=270.55 resistance=305.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=34.71 liquidity=2293290.0 spike=0.17
- SCTS.CA: score=14.52 buy_ready=False sector_rank=9 price=617.2 support=610.0 resistance=660.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=624356.5 spike=0.07
- SDTI.CA: score=21.55 buy_ready=True sector_rank=13 price=73.65 support=67.0 resistance=76.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:44 AM market time freshness=DELAYED_CURRENT RSI=59.94 liquidity=4318751.0 spike=0.18
- SEIG.CA: score=14.47 buy_ready=False sector_rank=13 price=255.18 support=255.0 resistance=293.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:28 AM market time freshness=DELAYED_CURRENT RSI=35.3 liquidity=1244578.5 spike=0.45
- SIPC.CA: score=13.49 buy_ready=False sector_rank=13 price=6.16 support=5.85 resistance=6.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=130054064.0 spike=2.63
- SKPC.CA: score=22.9 buy_ready=False sector_rank=6 price=18.8 support=16.3 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=78.23 liquidity=127419648.0 spike=0.97
- SMFR.CA: score=18.43 buy_ready=False sector_rank=13 price=253.99 support=247.0 resistance=309.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=45.96 liquidity=5201546.0 spike=0.19
- SNFC.CA: score=17.36 buy_ready=False sector_rank=13 price=10.87 support=10.26 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=3130978.0 spike=0.21
- SPIN.CA: score=24.12 buy_ready=True sector_rank=2 price=19.0 support=15.32 resistance=21.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=42.59 liquidity=6219288.5 spike=0.17
- SPMD.CA: score=13.45 buy_ready=False sector_rank=13 price=0.45 support=0.44 resistance=0.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=40.95 liquidity=3225896.5 spike=0.26
- SUGR.CA: score=27.21 buy_ready=False sector_rank=14 price=61.59 support=48.45 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=72.07 liquidity=11874743.0 spike=0.17
- SVCE.CA: score=25.23 buy_ready=False sector_rank=13 price=12.53 support=9.37 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=72.7 liquidity=123345816.0 spike=0.62
- SWDY.CA: score=27.9 buy_ready=True sector_rank=8 price=130.12 support=106.51 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=59.82 liquidity=69636432.0 spike=0.7
- TALM.CA: score=23.9 buy_ready=False sector_rank=9 price=18.11 support=17.11 resistance=20.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=36.75 liquidity=10816188.0 spike=0.42
- TMGH.CA: score=27.16 buy_ready=True sector_rank=16 price=99.0 support=94.9 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=55.46 liquidity=227704032.0 spike=0.83
- TRTO.CA: score=0.25 buy_ready=False sector_rank=13 price=0.08 support=0.07 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24602.95 spike=0.84
- UEFM.CA: score=26.87 buy_ready=False sector_rank=13 price=539.85 support=440.66 resistance=589.0 source=Yahoo Finance as_of=2026-09-07T21:00:00+00:00 freshness=FRESH RSI=47.78 liquidity=11694230.17 spike=2.82
- UEGC.CA: score=13.45 buy_ready=False sector_rank=13 price=1.73 support=1.66 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=25.24 liquidity=8226995.0 spike=0.17
- UNIP.CA: score=22.28 buy_ready=True sector_rank=13 price=0.39 support=0.35 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=46.27 liquidity=5056778.0 spike=0.14
- UNIT.CA: score=13.99 buy_ready=False sector_rank=16 price=18.82 support=17.8 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=52.22 liquidity=836631.25 spike=0.09
- WCDF.CA: score=15.74 buy_ready=False sector_rank=13 price=687.22 support=591.02 resistance=729.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=75.31 liquidity=1515499.5 spike=0.37
- WKOL.CA: score=16.5 buy_ready=True sector_rank=13 price=342.76 support=321.01 resistance=390.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=54.08 liquidity=1271478.75 spike=0.05
- ZEOT.CA: score=18.15 buy_ready=True sector_rank=13 price=13.92 support=12.73 resistance=14.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=45.1 liquidity=2925203.0 spike=0.18
- ZMID.CA: score=22.16 buy_ready=False sector_rank=16 price=9.4 support=7.39 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=78.25 liquidity=74345152.0 spike=0.29

## Backtesting Lite
- ORWE.CA: 180d return=30.07%, max drawdown=-9.36%, MA20>MA50 days last20=20, as_of=2026-09-07T21:00:00+00:00
- RUBX.CA: 180d return=24.88%, max drawdown=-17.75%, MA20>MA50 days last20=17, as_of=2026-09-07T21:00:00+00:00
- ETEL.CA: 180d return=93.7%, max drawdown=-30.44%, MA20>MA50 days last20=20, as_of=2026-09-07T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=616 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=616 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- MEPA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Medical Packaging Company summary=Medical Packaging stock close to break above EGP 1.7; Medical Packaging announces EGP 62m capital hike; Medical Packaging&#39;s profit jumps 54% in Q1-21
  - Medical Packaging stock close to break above EGP 1.7: https://english.mubasher.info/news/4598700/Medical-Packaging-stock-close-to-break-above-EGP-1-7/
  - Medical Packaging announces EGP 62m capital hike: https://english.mubasher.info/news/3936298/Medical-Packaging-announces-EGP-62m-capital-hike/
  - Medical Packaging&#39;s profit jumps 54% in Q1-21: https://english.mubasher.info/news/3815448/Medical-Packaging-s-profit-jumps-54-in-Q1-21/
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- EFIC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=616 sources=3 expected=Egyptian Financial and Industrial summary=EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed; EFIC ordered to pay over EGP 126m as penalties; EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn
  - EFIC’s consolidated profits near EGP 820m in 2025; dividends proposed: https://english.mubasher.info/news/4579891/EFIC-s-consolidated-profits-near-EGP-820m-in-2025-dividends-proposed/
  - EFIC ordered to pay over EGP 126m as penalties: https://english.mubasher.info/news/4535935/EFIC-ordered-to-pay-over-EGP-126m-as-penalties/
  - EFIC generates lower consolidated net profits at EGP 803m in 9M-25; net sales near EGP 8bn: https://english.mubasher.info/news/4528902/EFIC-generates-lower-consolidated-net-profits-at-EGP-803m-in-9M-25-net-sales-near-EGP-8bn/

## Warnings
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini batch evidence failed: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MEPA.CA matches the company but no source/report date was detected.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence for EFIC.CA matches the company but appears old; latest detected date is 2025-01-01.
