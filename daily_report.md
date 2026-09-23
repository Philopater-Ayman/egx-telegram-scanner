# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-23T11:31:11.308343+00:00
Generated Cairo: 2026-09-23 14:31
Run timing: target 09:15 Cairo | generated Cairo 2026-09-23 14:31 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-23 14:28

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 180/187
- Top sector: Investment Holding

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, September 23
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 21.05% / above MA50 47.37%
- EGX70 regime: BEARISH / above MA20 25.0% / above MA50 42.5%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=651124160.0 spike=1.01 score=11.42
- CCAP.CA: liquidity=462257760.0 spike=0.55 score=21.4
- ORHD.CA: liquidity=355072640.0 spike=2.43 score=16.81
- ETEL.CA: liquidity=291523968.0 spike=1.07 score=21.54
- OIH.CA: liquidity=206535248.0 spike=1.73 score=20.86

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: 

## Top Liquidity Spikes
- NEDA.CA: spike=7.81 liquidity=7374408.25 outlook=NEUTRAL score=42.64 buy_ready=False
- NHPS.CA: spike=5.57 liquidity=87709992.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MAAL.CA: spike=5.45 liquidity=68856032.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGTS.CA: spike=3.41 liquidity=91901960.0 outlook=CONSTRUCTIVE score=56 buy_ready=False
- MHOT.CA: spike=3.24 liquidity=31874556.0 outlook=BULLISH_WATCH score=74 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=12.96 5d=7.13% 20d=16.43% aboveMA50=100.0%
- #2 Tourism & Leisure: score=10.84 5d=-0.11% 20d=0.11% aboveMA50=100.0%
- #3 Telecommunications: score=10.37 5d=2.08% 20d=11.0% aboveMA50=100.0%
- #4 Transportation & Logistics: score=7.08 5d=6.82% 20d=3.25% aboveMA50=50.0%
- #5 Energy & Petrochemicals: score=7.05 5d=3.21% 20d=3.71% aboveMA50=66.67%
- #6 Banking & Financials: score=6.69 5d=2.08% 20d=4.62% aboveMA50=70.0%
- #7 Education: score=5.63 5d=-3.97% 20d=13.37% aboveMA50=66.67%
- #8 Agriculture & Food Production: score=5.59 5d=-0.72% 20d=10.07% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SAUD.CA: BULLISH_WATCH score=87.69 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended
- BINV.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- EXPA.CA: BULLISH_WATCH score=81.69 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- OIH.CA: BULLISH_WATCH score=79 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; close to resistance
- OFH.CA: BULLISH_WATCH score=76.64 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- DTPP.CA: BULLISH_WATCH score=76.64 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- MHOT.CA: BULLISH_WATCH score=74 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- ALCN.CA: BULLISH_WATCH score=73.08 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; close to resistance
- AMOC.CA: BULLISH_WATCH score=73.05 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- HDBK.CA: BULLISH_WATCH score=72.69 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=14.26 buy_ready=False sector_rank=18 price=290.54 support=288.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.13 liquidity=18948436.0 spike=0.77
- ABUK.CA: score=20.7 buy_ready=False sector_rank=10 price=92.03 support=75.01 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=120823704.0 spike=0.65
- ACAMD.CA: score=14.26 buy_ready=False sector_rank=18 price=2.0 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.1 liquidity=28730818.0 spike=0.54
- ACGC.CA: score=12.68 buy_ready=False sector_rank=11 price=14.0 support=13.65 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=4180185.75 spike=0.14
- ADCI.CA: score=4.86 buy_ready=False sector_rank=18 price=285.38 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=34.59 liquidity=2602983.25 spike=0.56
- ADIB.CA: score=16.4 buy_ready=False sector_rank=6 price=51.89 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=75796360.0 spike=0.97
- ADPC.CA: score=18.26 buy_ready=False sector_rank=18 price=4.0 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=17312046.0 spike=0.93
- AFDI.CA: score=6.29 buy_ready=False sector_rank=18 price=52.07 support=51.6 resistance=61.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=2038910.13 spike=0.09
- AFMC.CA: score=12.43 buy_ready=False sector_rank=18 price=158.28 support=153.0 resistance=232.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.7 liquidity=8171297.5 spike=0.14
- AJWA.CA: score=14.34 buy_ready=False sector_rank=18 price=178.82 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8088232.5 spike=0.18
- ALCN.CA: score=25.4 buy_ready=False sector_rank=4 price=34.2 support=30.03 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=56.12 liquidity=25281656.0 spike=0.7
- ALUM.CA: score=4.01 buy_ready=False sector_rank=18 price=24.96 support=25.0 resistance=30.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=26.38 liquidity=4756343.5 spike=0.41
- AMER.CA: score=13.95 buy_ready=False sector_rank=20 price=5.03 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.02 liquidity=23882706.0 spike=0.43
- AMES.CA: score=8.26 buy_ready=False sector_rank=18 price=49.99 support=48.45 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=11.06 liquidity=52959884.0 spike=0.2
- AMIA.CA: score=12.5 buy_ready=False sector_rank=18 price=18.36 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=5240840.0 spike=0.14
- AMOC.CA: score=21.4 buy_ready=False sector_rank=5 price=13.3 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=56958048.0 spike=0.32
- APSW.CA: score=-1.31 buy_ready=False sector_rank=18 price=8.32 support=8.2 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=33.59 liquidity=430168.34 spike=0.48
- ARAB.CA: score=8.95 buy_ready=False sector_rank=20 price=0.23 support=0.24 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=60793312.0 spike=0.62
- ARCC.CA: score=11.27 buy_ready=False sector_rank=21 price=68.54 support=69.0 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=26.48 liquidity=20972004.0 spike=0.63
- AREH.CA: score=12.4 buy_ready=False sector_rank=18 price=1.4 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=8140965.5 spike=0.58
- ASCM.CA: score=5.71 buy_ready=False sector_rank=18 price=57.86 support=58.16 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=30.91 liquidity=6456832.0 spike=0.34
- ASPI.CA: score=14.26 buy_ready=False sector_rank=18 price=0.41 support=0.41 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.7 liquidity=30955338.0 spike=0.49
- ATLC.CA: score=13.52 buy_ready=False sector_rank=12 price=6.92 support=5.35 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=3608754.75 spike=0.13
- ATQA.CA: score=20.7 buy_ready=False sector_rank=10 price=12.92 support=11.36 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.24 liquidity=42573332.0 spike=0.38
- AXPH.CA: score=11.32 buy_ready=False sector_rank=18 price=1669.44 support=1560.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=4060824.25 spike=0.44
- BINV.CA: score=21.08 buy_ready=False sector_rank=1 price=56.37 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=66.21 liquidity=6681275.0 spike=0.27
- BIOC.CA: score=9.26 buy_ready=False sector_rank=18 price=263.62 support=247.03 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.58 liquidity=11949774.0 spike=0.13
- BTFH.CA: score=16.26 buy_ready=False sector_rank=12 price=2.88 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=38.64 liquidity=95093480.0 spike=1.17
- CAED.CA: score=2.57 buy_ready=False sector_rank=18 price=120.9 support=122.6 resistance=154.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.76 liquidity=3314974.25 spike=0.15
- CANA.CA: score=21.4 buy_ready=False sector_rank=6 price=45.93 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=71.01 liquidity=13692070.0 spike=0.6
- CCAP.CA: score=21.4 buy_ready=False sector_rank=1 price=7.04 support=5.74 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=81.95 liquidity=462257760.0 spike=0.55
- CCRS.CA: score=13.1 buy_ready=False sector_rank=18 price=2.55 support=2.4 resistance=3.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=8841348.0 spike=0.21
- CEFM.CA: score=7.79 buy_ready=False sector_rank=18 price=143.52 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.06 liquidity=535030.25 spike=0.06
- CERA.CA: score=14.26 buy_ready=False sector_rank=18 price=1.35 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.54 liquidity=52882304.0 spike=0.41
- CFGH.CA: score=2.26 buy_ready=False sector_rank=18 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=26.67 liquidity=7695.92 spike=0.46
- CICH.CA: score=13.83 buy_ready=False sector_rank=12 price=12.34 support=11.47 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=70.42 liquidity=1913316.25 spike=0.31
- CIEB.CA: score=19.4 buy_ready=False sector_rank=6 price=24.73 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=12196970.0 spike=0.89
- CIRA.CA: score=21.25 buy_ready=False sector_rank=7 price=39.87 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=70.3 liquidity=14719893.0 spike=0.37
- CLHO.CA: score=9.31 buy_ready=False sector_rank=17 price=15.8 support=15.4 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=25879204.0 spike=0.35
- CNFN.CA: score=3.5 buy_ready=False sector_rank=12 price=4.44 support=4.46 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=31.33 liquidity=4580041.0 spike=0.4
- COMI.CA: score=11.42 buy_ready=False sector_rank=6 price=129.0 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=651124160.0 spike=1.01
- COPR.CA: score=17.26 buy_ready=False sector_rank=18 price=0.48 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.44 liquidity=10171815.0 spike=0.23
- COSG.CA: score=14.26 buy_ready=False sector_rank=18 price=1.71 support=1.77 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=18518458.0 spike=0.57
- CPCI.CA: score=10.26 buy_ready=False sector_rank=18 price=563.28 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=1007250.56 spike=0.31
- CSAG.CA: score=5.08 buy_ready=False sector_rank=4 price=37.76 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.56 liquidity=3680180.0 spike=0.24
- DAPH.CA: score=9.26 buy_ready=False sector_rank=18 price=109.01 support=108.25 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.58 liquidity=24939104.0 spike=0.43
- DEIN.CA: score=7.26 buy_ready=False sector_rank=18 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=11.3 buy_ready=False sector_rank=16 price=26.01 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=36.1 liquidity=6440216.0 spike=1.23
- DSCW.CA: score=5.0 buy_ready=False sector_rank=18 price=1.78 support=1.77 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.38 liquidity=6748024.0 spike=0.27
- DTPP.CA: score=19.26 buy_ready=False sector_rank=18 price=327.67 support=295.13 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.9 liquidity=69209544.0 spike=0.86
- EALR.CA: score=9.65 buy_ready=False sector_rank=18 price=367.01 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.72 liquidity=5396150.0 spike=0.39
- EASB.CA: score=17.26 buy_ready=False sector_rank=18 price=7.88 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.34 liquidity=11155818.0 spike=0.66
- EAST.CA: score=8.4 buy_ready=False sector_rank=16 price=31.87 support=31.31 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=11.58 liquidity=16201507.0 spike=0.21
- EBSC.CA: score=5.92 buy_ready=False sector_rank=18 price=1.97 support=1.95 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=1661431.0 spike=0.11
- ECAP.CA: score=1.05 buy_ready=False sector_rank=18 price=31.6 support=31.16 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.26 liquidity=1796071.13 spike=0.16
- EDFM.CA: score=4.75 buy_ready=False sector_rank=18 price=393.0 support=390.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.76 liquidity=498498.97 spike=0.28
- EEII.CA: score=15.46 buy_ready=False sector_rank=18 price=2.29 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.54 liquidity=16202831.0 spike=1.1
- EFIC.CA: score=14.7 buy_ready=False sector_rank=10 price=184.74 support=183.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.76 liquidity=14844787.0 spike=0.04
- EFID.CA: score=14.4 buy_ready=False sector_rank=16 price=30.31 support=29.71 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=48.82 liquidity=42916020.0 spike=0.64
- EFIH.CA: score=14.23 buy_ready=False sector_rank=19 price=23.39 support=22.16 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49038092.0 spike=0.82
- EGAL.CA: score=18.7 buy_ready=False sector_rank=10 price=360.64 support=351.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=37.89 liquidity=34243240.0 spike=0.35
- EGAS.CA: score=14.41 buy_ready=False sector_rank=5 price=55.63 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=8008765.0 spike=0.68
- EGBE.CA: score=9.64 buy_ready=False sector_rank=6 price=0.52 support=0.49 resistance=0.55 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=43.3 liquidity=79786.39 spike=1.08
- EGCH.CA: score=18.7 buy_ready=False sector_rank=10 price=13.95 support=13.33 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=80996520.0 spike=0.66
- EGSA.CA: score=12.4 buy_ready=False sector_rank=3 price=9.0 support=8.69 resistance=9.1 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=4590.0 spike=0.71
- EGTS.CA: score=25.77 buy_ready=False sector_rank=20 price=18.71 support=16.51 resistance=18.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=91901960.0 spike=3.41
- EHDR.CA: score=4.18 buy_ready=False sector_rank=18 price=2.63 support=2.65 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.81 liquidity=4920398.0 spike=0.28
- ELEC.CA: score=8.6 buy_ready=False sector_rank=13 price=1.96 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=28940122.0 spike=0.37
- ELKA.CA: score=6.28 buy_ready=False sector_rank=18 price=1.65 support=1.64 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=15.62 liquidity=7026928.5 spike=0.19
- ELNA.CA: score=-1.46 buy_ready=False sector_rank=18 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=26.38 liquidity=285246.79 spike=0.74
- ELSH.CA: score=12.36 buy_ready=False sector_rank=18 price=12.1 support=12.55 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.6 liquidity=8106508.0 spike=0.22
- ELWA.CA: score=0.08 buy_ready=False sector_rank=18 price=1.69 support=1.64 resistance=1.99 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=25.0 liquidity=822666.68 spike=0.47
- EMFD.CA: score=16.95 buy_ready=False sector_rank=20 price=13.39 support=12.1 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.92 liquidity=43543352.0 spike=0.27
- ENGC.CA: score=14.86 buy_ready=False sector_rank=18 price=41.65 support=41.0 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.05 liquidity=22034120.0 spike=1.3
- EOSB.CA: score=9.38 buy_ready=False sector_rank=18 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=67542.97 spike=1.03
- EPCO.CA: score=8.08 buy_ready=False sector_rank=18 price=10.66 support=10.6 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=3823321.5 spike=0.24
- EPPK.CA: score=-5.32 buy_ready=False sector_rank=18 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=21.54 buy_ready=False sector_rank=3 price=138.33 support=112.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=87.08 liquidity=291523968.0 spike=1.07
- ETRS.CA: score=6.0 buy_ready=False sector_rank=18 price=10.61 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=33.01 liquidity=6748624.0 spike=0.53
- EXPA.CA: score=23.4 buy_ready=False sector_rank=6 price=21.86 support=19.96 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=31555672.0 spike=0.89
- FAIT.CA: score=11.05 buy_ready=False sector_rank=6 price=46.55 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=1653289.38 spike=0.2
- FAITA.CA: score=5.41 buy_ready=False sector_rank=6 price=0.98 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=14747.09 spike=0.3
- FERC.CA: score=11.18 buy_ready=False sector_rank=10 price=77.56 support=77.3 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.09 liquidity=6477687.5 spike=0.45
- FWRY.CA: score=14.23 buy_ready=False sector_rank=19 price=18.98 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.43 liquidity=120953880.0 spike=0.88
- GBCO.CA: score=22.91 buy_ready=False sector_rank=9 price=31.12 support=27.51 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=64.3 liquidity=58275572.0 spike=0.77
- GDWA.CA: score=8.26 buy_ready=False sector_rank=18 price=0.74 support=0.75 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=14.04 liquidity=30824514.0 spike=0.71
- GGCC.CA: score=14.26 buy_ready=False sector_rank=18 price=0.78 support=0.81 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.96 liquidity=15295678.0 spike=0.46
- GIHD.CA: score=19.26 buy_ready=False sector_rank=18 price=73.75 support=61.61 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.87 liquidity=13545958.0 spike=0.51
- GMCI.CA: score=0.42 buy_ready=False sector_rank=18 price=1.71 support=1.69 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=819411.19 spike=1.67
- GRCA.CA: score=8.26 buy_ready=False sector_rank=18 price=40.13 support=38.7 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.06 liquidity=23510890.0 spike=0.48
- GSSC.CA: score=13.25 buy_ready=False sector_rank=18 price=299.44 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.08 liquidity=1993533.25 spike=0.23
- GTWL.CA: score=17.26 buy_ready=False sector_rank=18 price=230.56 support=210.0 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=59.32 liquidity=67962624.0 spike=0.37
- HDBK.CA: score=23.4 buy_ready=False sector_rank=6 price=113.87 support=91.7 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=51.84 liquidity=17552568.0 spike=0.29
- HELI.CA: score=16.23 buy_ready=False sector_rank=20 price=7.94 support=7.36 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=52.81 liquidity=190503056.0 spike=1.14
- HRHO.CA: score=8.92 buy_ready=False sector_rank=12 price=24.42 support=24.4 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.03 liquidity=41944924.0 spike=0.4
- ICID.CA: score=18.64 buy_ready=False sector_rank=18 price=17.0 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=17966252.0 spike=1.69
- IDRE.CA: score=14.86 buy_ready=False sector_rank=18 price=53.03 support=51.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=7608811.0 spike=0.46
- IFAP.CA: score=14.32 buy_ready=False sector_rank=8 price=20.08 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.01 liquidity=8081426.0 spike=0.37
- INFI.CA: score=8.05 buy_ready=False sector_rank=18 price=123.16 support=123.0 resistance=161.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=21.62 liquidity=8796967.0 spike=0.45
- IRON.CA: score=9.7 buy_ready=False sector_rank=10 price=27.96 support=26.3 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=22.67 liquidity=10362793.0 spike=0.75
- ISMA.CA: score=8.91 buy_ready=False sector_rank=18 price=29.86 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.11 liquidity=4657077.0 spike=0.2
- ISMQ.CA: score=10.7 buy_ready=False sector_rank=10 price=8.6 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.48 liquidity=13379513.0 spike=0.53
- ISPH.CA: score=9.31 buy_ready=False sector_rank=17 price=12.02 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=34.94 liquidity=14452984.0 spike=0.21
- JUFO.CA: score=13.71 buy_ready=False sector_rank=16 price=26.83 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.16 liquidity=8314851.0 spike=0.39
- KABO.CA: score=15.51 buy_ready=False sector_rank=11 price=9.08 support=8.92 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=7001943.5 spike=0.17
- KWIN.CA: score=9.26 buy_ready=False sector_rank=18 price=90.0 support=82.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=12.61 liquidity=37338120.0 spike=0.8
- KZPC.CA: score=12.25 buy_ready=False sector_rank=18 price=13.68 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=61.56 liquidity=2991845.25 spike=0.08
- LCSW.CA: score=5.31 buy_ready=False sector_rank=21 price=31.9 support=31.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.56 liquidity=7038596.0 spike=0.29
- LUTS.CA: score=14.26 buy_ready=False sector_rank=18 price=0.87 support=0.83 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=21303210.0 spike=0.12
- MAAL.CA: score=9.26 buy_ready=False sector_rank=18 price=10.3 support=9.03 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68856032.0 spike=5.45
- MASR.CA: score=14.26 buy_ready=False sector_rank=18 price=7.6 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.43 liquidity=27629784.0 spike=0.28
- MBSC.CA: score=11.27 buy_ready=False sector_rank=21 price=339.49 support=333.33 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=22.57 liquidity=23226544.0 spike=0.52
- MCQE.CA: score=8.27 buy_ready=False sector_rank=21 price=200.09 support=203.5 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.88 liquidity=23318528.0 spike=0.88
- MCRO.CA: score=17.26 buy_ready=False sector_rank=18 price=1.63 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.92 liquidity=37275228.0 spike=0.3
- MENA.CA: score=4.67 buy_ready=False sector_rank=20 price=6.63 support=6.58 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=721837.31 spike=0.45
- MEPA.CA: score=10.12 buy_ready=False sector_rank=18 price=1.86 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.32 liquidity=5860290.5 spike=0.15
- MFPC.CA: score=22.7 buy_ready=False sector_rank=10 price=47.62 support=39.02 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=62.46 liquidity=53169804.0 spike=0.3
- MFSC.CA: score=11.46 buy_ready=False sector_rank=18 price=51.08 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.59 liquidity=2199766.0 spike=0.46
- MHOT.CA: score=26.88 buy_ready=False sector_rank=2 price=18.71 support=16.61 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.91 liquidity=31874556.0 spike=3.24
- MICH.CA: score=11.15 buy_ready=False sector_rank=18 price=47.16 support=47.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=24.75 liquidity=8898793.0 spike=0.57
- MILS.CA: score=8.98 buy_ready=False sector_rank=18 price=190.57 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=35.06 liquidity=4720230.0 spike=0.2
- MIPH.CA: score=16.37 buy_ready=False sector_rank=17 price=838.26 support=700.2 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=7061982.5 spike=0.79
- MOED.CA: score=8.26 buy_ready=False sector_rank=18 price=0.71 support=0.7 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.23 liquidity=14462791.0 spike=0.21
- MOIL.CA: score=13.14 buy_ready=False sector_rank=5 price=0.7 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=68.33 liquidity=380338.5 spike=1.68
- MOIN.CA: score=10.77 buy_ready=False sector_rank=18 price=35.61 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=3511394.25 spike=0.11
- MOSC.CA: score=-0.17 buy_ready=False sector_rank=18 price=299.78 support=290.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=21.23 liquidity=569541.63 spike=0.09
- MPCI.CA: score=12.26 buy_ready=False sector_rank=18 price=385.0 support=371.11 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.84 liquidity=76244200.0 spike=0.53
- MPCO.CA: score=21.24 buy_ready=False sector_rank=8 price=2.63 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=67.93 liquidity=135119936.0 spike=0.79
- MPRC.CA: score=9.26 buy_ready=False sector_rank=18 price=39.05 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.54 liquidity=20599364.0 spike=0.54
- MTIE.CA: score=9.91 buy_ready=False sector_rank=9 price=8.19 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=23.15 liquidity=17751444.0 spike=0.67
- NAHO.CA: score=-4.16 buy_ready=False sector_rank=18 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100493.34 spike=1.74
- NCCW.CA: score=5.2 buy_ready=False sector_rank=18 price=7.64 support=7.15 resistance=7.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99875448.0 spike=1.47
- NEDA.CA: score=16.63 buy_ready=False sector_rank=18 price=2.75 support=2.7 resistance=2.89 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=51.52 liquidity=7374408.25 spike=7.81
- NHPS.CA: score=9.26 buy_ready=False sector_rank=18 price=82.7 support=73.63 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=87709992.0 spike=5.57
- NINH.CA: score=2.64 buy_ready=False sector_rank=18 price=20.24 support=20.3 resistance=25.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.17 liquidity=3379668.0 spike=0.11
- NIPH.CA: score=17.31 buy_ready=False sector_rank=17 price=333.01 support=290.0 resistance=401.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.36 liquidity=95316688.0 spike=0.62
- OBRI.CA: score=4.09 buy_ready=False sector_rank=18 price=29.58 support=29.51 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=5833644.0 spike=0.39
- OCDI.CA: score=8.95 buy_ready=False sector_rank=20 price=28.13 support=28.52 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=26.51 liquidity=47788236.0 spike=0.61
- OCPH.CA: score=8.41 buy_ready=False sector_rank=18 price=235.07 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=3153351.0 spike=0.49
- ODIN.CA: score=13.5 buy_ready=False sector_rank=18 price=2.75 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=9242552.0 spike=0.42
- OFH.CA: score=20.1 buy_ready=False sector_rank=18 price=1.09 support=0.98 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=61.29 liquidity=191325728.0 spike=1.42
- OIH.CA: score=20.86 buy_ready=False sector_rank=1 price=2.17 support=1.94 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=76.92 liquidity=206535248.0 spike=1.73
- OLFI.CA: score=14.83 buy_ready=False sector_rank=16 price=22.59 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=57.38 liquidity=8433959.0 spike=0.48
- ORAS.CA: score=4.6 buy_ready=False sector_rank=14 price=840.55 support=837.02 resistance=847.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55489776.0 spike=1.0
- ORHD.CA: score=16.81 buy_ready=False sector_rank=20 price=40.58 support=40.85 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=355072640.0 spike=2.43
- ORWE.CA: score=20.5 buy_ready=False sector_rank=11 price=27.6 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.23 liquidity=30542590.0 spike=0.56
- PHAR.CA: score=9.31 buy_ready=False sector_rank=17 price=113.49 support=111.55 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=31.66 liquidity=25560348.0 spike=0.25
- PHDC.CA: score=8.95 buy_ready=False sector_rank=20 price=13.38 support=12.91 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=39744684.0 spike=0.25
- PHTV.CA: score=4.98 buy_ready=False sector_rank=18 price=336.95 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.4 liquidity=725215.56 spike=0.43
- POUL.CA: score=16.96 buy_ready=False sector_rank=16 price=38.55 support=37.15 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=21 September 01:28 PM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=58845364.0 spike=2.28
- PRCL.CA: score=12.72 buy_ready=False sector_rank=21 price=31.51 support=30.61 resistance=34.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=43.97 liquidity=9447533.0 spike=0.56
- PRDC.CA: score=8.95 buy_ready=False sector_rank=20 price=7.41 support=7.51 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=11.9 liquidity=24883956.0 spike=0.43
- PRMH.CA: score=5.72 buy_ready=False sector_rank=18 price=2.59 support=2.43 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=1465910.63 spike=0.14
- RACC.CA: score=6.87 buy_ready=False sector_rank=18 price=9.58 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=2612894.0 spike=0.15
- RAKT.CA: score=4.01 buy_ready=False sector_rank=18 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=278804.16 spike=1.24
- RAYA.CA: score=15.42 buy_ready=False sector_rank=15 price=7.01 support=6.8 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=80006576.0 spike=1.49
- RMDA.CA: score=17.31 buy_ready=False sector_rank=17 price=5.92 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=29645446.0 spike=0.52
- ROTO.CA: score=6.14 buy_ready=False sector_rank=18 price=40.57 support=35.02 resistance=45.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.16 liquidity=6883090.5 spike=0.89
- RREI.CA: score=14.26 buy_ready=False sector_rank=18 price=4.1 support=4.2 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.14 liquidity=10427434.0 spike=0.61
- RTVC.CA: score=-0.14 buy_ready=False sector_rank=18 price=3.81 support=3.79 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=26.56 liquidity=1602847.0 spike=0.38
- RUBX.CA: score=7.56 buy_ready=False sector_rank=18 price=16.94 support=15.44 resistance=16.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=108924768.0 spike=2.65
- SAUD.CA: score=24.24 buy_ready=False sector_rank=6 price=24.58 support=22.7 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=69.68 liquidity=26104064.0 spike=1.42
- SCEM.CA: score=8.27 buy_ready=False sector_rank=21 price=84.51 support=84.5 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=21.9 liquidity=24425582.0 spike=0.25
- SCFM.CA: score=5.39 buy_ready=False sector_rank=18 price=266.54 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=39.64 liquidity=1130100.75 spike=0.15
- SCTS.CA: score=1.93 buy_ready=False sector_rank=7 price=583.53 support=566.66 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=27.3 liquidity=673593.13 spike=0.24
- SDTI.CA: score=13.49 buy_ready=False sector_rank=18 price=77.53 support=67.3 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.38 liquidity=5234018.5 spike=0.19
- SEIG.CA: score=5.62 buy_ready=False sector_rank=18 price=230.49 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.72 liquidity=1367694.88 spike=0.73
- SIPC.CA: score=17.26 buy_ready=False sector_rank=18 price=5.37 support=4.75 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=18966672.0 spike=0.27
- SKPC.CA: score=13.7 buy_ready=False sector_rank=10 price=17.63 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=33.89 liquidity=38191748.0 spike=0.29
- SMFR.CA: score=1.64 buy_ready=False sector_rank=18 price=229.74 support=226.1 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.21 liquidity=2388149.0 spike=0.3
- SNFC.CA: score=18.26 buy_ready=False sector_rank=18 price=11.54 support=10.26 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=82.12 liquidity=13027532.0 spike=0.86
- SPIN.CA: score=8.13 buy_ready=False sector_rank=11 price=17.02 support=16.1 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=30.92 liquidity=7623660.0 spike=0.56
- SPMD.CA: score=14.26 buy_ready=False sector_rank=18 price=0.42 support=0.4 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=35038744.0 spike=0.47
- SUGR.CA: score=11.96 buy_ready=False sector_rank=16 price=58.25 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.87 liquidity=4560604.0 spike=0.11
- SVCE.CA: score=12.26 buy_ready=False sector_rank=18 price=11.11 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.3 liquidity=36717136.0 spike=0.19
- SWDY.CA: score=17.6 buy_ready=False sector_rank=13 price=124.51 support=122.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=28060360.0 spike=0.45
- TALM.CA: score=21.25 buy_ready=False sector_rank=7 price=20.8 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=65.69 liquidity=24374724.0 spike=0.36
- TMGH.CA: score=13.95 buy_ready=False sector_rank=20 price=92.75 support=93.08 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.39 liquidity=143331504.0 spike=0.5
- TRTO.CA: score=7.27 buy_ready=False sector_rank=18 price=0.06 support=0.05 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=16175.52 spike=0.58
- UEFM.CA: score=-0.51 buy_ready=False sector_rank=18 price=476.98 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=30.28 liquidity=1238285.13 spike=0.4
- UEGC.CA: score=16.26 buy_ready=False sector_rank=18 price=1.62 support=1.66 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=42197700.0 spike=0.8
- UNIP.CA: score=10.6 buy_ready=False sector_rank=18 price=0.37 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=6342651.0 spike=0.28
- UNIT.CA: score=6.03 buy_ready=False sector_rank=20 price=18.02 support=17.12 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=46.5 liquidity=2077935.0 spike=0.15
- WCDF.CA: score=10.21 buy_ready=False sector_rank=18 price=700.33 support=636.31 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=60.47 liquidity=958570.63 spike=0.19
- WKOL.CA: score=9.91 buy_ready=False sector_rank=18 price=331.12 support=325.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=5655833.5 spike=0.42
- ZEOT.CA: score=5.62 buy_ready=False sector_rank=18 price=12.7 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=34.88 liquidity=6307022.0 spike=1.03
- ZMID.CA: score=11.95 buy_ready=False sector_rank=20 price=8.31 support=7.91 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=29.97 liquidity=153092400.0 spike=0.72

## Backtesting Lite
- MHOT.CA: 180d return=-29.25%, max drawdown=-54.07%, MA20>MA50 days last20=14, as_of=2026-09-21T21:00:00+00:00
- EGTS.CA: 180d return=133.0%, max drawdown=-25.75%, MA20>MA50 days last20=0, as_of=2026-09-21T21:00:00+00:00
- ALCN.CA: 180d return=51.26%, max drawdown=-15.82%, MA20>MA50 days last20=20, as_of=2026-09-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- EGTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Resorts Company summary=Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=630 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.

## Warnings
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
