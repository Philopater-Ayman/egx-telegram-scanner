# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-10-07T15:03:07.121141+00:00
Generated Cairo: 2026-10-07 18:03
Run timing: target 11:00 Cairo | generated Cairo 2026-10-07 18:03 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-10-07 17:59

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 7
- Tradeable price/liquidity tickers: 180/183
- Top sector: Fintech & Payments

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, October 07
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 21.05% / above MA50 36.84%
- EGX70 regime: BEARISH / above MA20 33.33% / above MA50 35.9%
- Sector breadth: 52.38%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ORAS.CA: liquidity=637229824.0 spike=1.0 score=4.6
- COMI.CA: liquidity=418422272.0 spike=0.77 score=9.21
- CCAP.CA: liquidity=339093696.0 spike=0.42 score=18.93
- FWRY.CA: liquidity=336845728.0 spike=3.59 score=31.4
- AMOC.CA: liquidity=250964784.0 spike=1.84 score=22.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: 

## Top Liquidity Spikes
- RAKT.CA: spike=4.35 liquidity=1328021.18 outlook=BULLISH_WATCH score=71.99 buy_ready=False
- SIPC.CA: spike=3.71 liquidity=183080896.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- FWRY.CA: spike=3.59 liquidity=336845728.0 outlook=BULLISH_WATCH score=100 buy_ready=False
- DAPH.CA: spike=3.39 liquidity=110708520.0 outlook=WEAK_OR_RISKY score=19.99 buy_ready=False
- AJWA.CA: spike=2.62 liquidity=45247820.0 outlook=CONSTRUCTIVE score=63.99 buy_ready=False

## Sector Leaderboard
- #1 Fintech & Payments: score=12.79 5d=6.27% 20d=0.48% aboveMA50=100.0%
- #2 Telecommunications: score=9.41 5d=5.74% 20d=11.45% aboveMA50=100.0%
- #3 Building Materials: score=6.92 5d=11.67% 20d=-11.48% aboveMA50=50.0%
- #4 Education: score=6.38 5d=3.3% 20d=2.84% aboveMA50=66.67%
- #5 Automotive & Distribution: score=6.13 5d=5.41% 20d=-0.92% aboveMA50=50.0%
- #6 Investment Holding: score=4.83 5d=0.14% 20d=6.16% aboveMA50=66.67%
- #7 Transportation & Logistics: score=4.81 5d=3.22% 20d=-1.44% aboveMA50=50.0%
- #8 Energy & Petrochemicals: score=4.3 5d=0.88% 20d=0.77% aboveMA50=66.67%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- FWRY.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- EFIH.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support
- MBSC.CA: BULLISH_WATCH score=99.92 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=far above support
- LCSW.CA: BULLISH_WATCH score=89.92 liquidity=TRADEABLE sector=LEADING risk=far above support
- CIRA.CA: BULLISH_WATCH score=87.38 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARCC.CA: BULLISH_WATCH score=86.92 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- GBCO.CA: BULLISH_WATCH score=81.13 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARAB.CA: BULLISH_WATCH score=81.04 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- EDFM.CA: BULLISH_WATCH score=77.99 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- AMOC.CA: BULLISH_WATCH score=74.3 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- ORHD.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- EXPA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- CAED.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=5.95 buy_ready=False sector_rank=13 price=261.04 support=230.11 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=24.08 liquidity=6151743.0 spike=0.3
- ABUK.CA: score=17.89 buy_ready=False sector_rank=12 price=89.12 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.11 liquidity=93761504.0 spike=0.87
- ACAMD.CA: score=18.8 buy_ready=False sector_rank=13 price=2.05 support=1.87 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.81 liquidity=36076280.0 spike=0.84
- ACGC.CA: score=10.48 buy_ready=False sector_rank=14 price=14.33 support=13.11 resistance=15.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.85 liquidity=2749722.75 spike=0.14
- ADCI.CA: score=5.5 buy_ready=False sector_rank=13 price=272.01 support=256.0 resistance=295.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.93 liquidity=704704.56 spike=0.3
- ADIB.CA: score=10.23 buy_ready=False sector_rank=10 price=47.75 support=48.02 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.22 liquidity=72852176.0 spike=1.01
- ADPC.CA: score=13.8 buy_ready=False sector_rank=13 price=3.53 support=3.4 resistance=4.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=10132785.0 spike=0.64
- AFDI.CA: score=15.03 buy_ready=False sector_rank=13 price=54.07 support=47.7 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.23 liquidity=6234218.5 spike=0.89
- AFMC.CA: score=16.8 buy_ready=False sector_rank=13 price=152.8 support=131.0 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=13572170.0 spike=0.47
- AJWA.CA: score=22.04 buy_ready=False sector_rank=13 price=196.16 support=176.0 resistance=197.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=83.55 liquidity=45247820.0 spike=2.62
- ALCN.CA: score=22.92 buy_ready=False sector_rank=7 price=34.32 support=30.4 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.72 liquidity=20531096.0 spike=0.6
- ALUM.CA: score=6.95 buy_ready=False sector_rank=13 price=23.53 support=21.65 resistance=28.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.89 liquidity=2156620.0 spike=0.41
- AMER.CA: score=16.42 buy_ready=False sector_rank=17 price=5.03 support=4.05 resistance=5.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.2 liquidity=45464256.0 spike=0.98
- AMES.CA: score=15.8 buy_ready=False sector_rank=13 price=46.37 support=40.15 resistance=66.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.27 liquidity=51405512.0 spike=0.34
- AMIA.CA: score=16.9 buy_ready=False sector_rank=13 price=19.18 support=17.12 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=77.08 liquidity=17362642.0 spike=1.05
- AMOC.CA: score=22.4 buy_ready=False sector_rank=8 price=14.5 support=12.18 resistance=14.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.59 liquidity=250964784.0 spike=1.84
- APSW.CA: score=10.14 buy_ready=False sector_rank=13 price=8.44 support=7.81 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.59 liquidity=1085005.25 spike=1.63
- ARAB.CA: score=24.76 buy_ready=False sector_rank=17 price=0.27 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.11 liquidity=126584280.0 spike=1.67
- ARCC.CA: score=24.4 buy_ready=False sector_rank=3 price=71.07 support=60.01 resistance=76.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=20092410.0 spike=0.7
- AREH.CA: score=9.05 buy_ready=False sector_rank=13 price=1.29 support=1.14 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.96 liquidity=5252735.5 spike=0.49
- ASCM.CA: score=10.13 buy_ready=False sector_rank=13 price=57.53 support=53.8 resistance=65.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.34 liquidity=3330463.0 spike=0.34
- ASPI.CA: score=9.8 buy_ready=False sector_rank=13 price=0.36 support=0.33 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.84 liquidity=14594139.0 spike=0.31
- ATLC.CA: score=12.41 buy_ready=False sector_rank=9 price=6.3 support=5.2 resistance=7.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.35 liquidity=3922364.25 spike=0.3
- ATQA.CA: score=17.89 buy_ready=False sector_rank=12 price=12.0 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=55682128.0 spike=0.68
- AXPH.CA: score=3.69 buy_ready=False sector_rank=13 price=1495.64 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.29 liquidity=3891342.25 spike=0.59
- BINV.CA: score=19.8 buy_ready=False sector_rank=6 price=58.26 support=49.91 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.47 liquidity=8869432.0 spike=0.36
- BIOC.CA: score=18.8 buy_ready=False sector_rank=13 price=324.84 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.03 liquidity=65018844.0 spike=0.69
- BTFH.CA: score=14.49 buy_ready=False sector_rank=9 price=2.77 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.47 liquidity=72468120.0 spike=0.78
- CANA.CA: score=19.64 buy_ready=False sector_rank=10 price=44.93 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=62.82 liquidity=9430163.0 spike=0.42
- CCAP.CA: score=18.93 buy_ready=False sector_rank=6 price=6.59 support=6.08 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=339093696.0 spike=0.42
- CCRS.CA: score=8.92 buy_ready=False sector_rank=13 price=2.32 support=2.21 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.07 liquidity=9127857.0 spike=0.64
- CEFM.CA: score=8.0 buy_ready=False sector_rank=13 price=135.82 support=113.0 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=3202893.75 spike=0.95
- CERA.CA: score=16.94 buy_ready=False sector_rank=13 price=1.37 support=1.18 resistance=1.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.71 liquidity=151765008.0 spike=1.07
- CFGH.CA: score=0.01 buy_ready=False sector_rank=13 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=13721.9 spike=1.6
- CICH.CA: score=7.21 buy_ready=False sector_rank=9 price=11.94 support=10.75 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=1726842.13 spike=0.42
- CIEB.CA: score=11.36 buy_ready=False sector_rank=10 price=24.0 support=23.0 resistance=25.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=6148950.5 spike=0.66
- CIRA.CA: score=21.7 buy_ready=False sector_rank=4 price=39.42 support=36.8 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.94 liquidity=39692328.0 spike=1.15
- CLHO.CA: score=16.32 buy_ready=False sector_rank=18 price=15.2 support=13.9 resistance=16.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.45 liquidity=27373122.0 spike=0.6
- CNFN.CA: score=11.33 buy_ready=False sector_rank=9 price=4.33 support=3.84 resistance=4.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=14360919.0 spike=1.92
- COMI.CA: score=9.21 buy_ready=False sector_rank=10 price=124.64 support=124.5 resistance=140.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.32 liquidity=418422272.0 spike=0.77
- COPR.CA: score=19.8 buy_ready=False sector_rank=13 price=0.48 support=0.44 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.45 liquidity=14329979.0 spike=0.56
- COSG.CA: score=8.73 buy_ready=False sector_rank=13 price=1.61 support=1.46 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.9 liquidity=8937595.0 spike=0.54
- CPCI.CA: score=10.81 buy_ready=False sector_rank=13 price=602.9 support=530.0 resistance=613.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=87.51 liquidity=3911104.0 spike=1.05
- CSAG.CA: score=9.88 buy_ready=False sector_rank=7 price=36.82 support=34.52 resistance=41.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=3955159.0 spike=0.47
- DAPH.CA: score=14.58 buy_ready=False sector_rank=13 price=107.08 support=89.1 resistance=134.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.3 liquidity=110708520.0 spike=3.39
- DEIN.CA: score=7.8 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance as_of=2026-10-05T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=10.17 buy_ready=False sector_rank=21 price=24.0 support=23.81 resistance=28.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.66 liquidity=10755096.0 spike=2.27
- DSCW.CA: score=4.79 buy_ready=False sector_rank=13 price=1.7 support=1.58 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=5997761.0 spike=0.31
- DTPP.CA: score=17.8 buy_ready=False sector_rank=13 price=302.15 support=250.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.95 liquidity=52522504.0 spike=0.54
- EALR.CA: score=3.71 buy_ready=False sector_rank=13 price=342.16 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.56 liquidity=4912222.5 spike=0.5
- EASB.CA: score=9.79 buy_ready=False sector_rank=13 price=7.64 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.81 liquidity=1989678.5 spike=0.13
- EAST.CA: score=7.63 buy_ready=False sector_rank=21 price=28.75 support=27.91 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=17.9 liquidity=40159696.0 spike=0.77
- EBSC.CA: score=4.65 buy_ready=False sector_rank=13 price=1.77 support=1.61 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.33 liquidity=858771.44 spike=0.2
- ECAP.CA: score=3.56 buy_ready=False sector_rank=13 price=30.1 support=29.13 resistance=33.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.9 liquidity=2759540.0 spike=0.61
- EDFM.CA: score=14.7 buy_ready=False sector_rank=13 price=410.0 support=354.0 resistance=428.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.18 liquidity=2565514.0 spike=2.17
- EEII.CA: score=14.6 buy_ready=False sector_rank=13 price=2.13 support=2.02 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.72 liquidity=8806858.0 spike=0.93
- EFIC.CA: score=8.89 buy_ready=False sector_rank=12 price=163.04 support=147.0 resistance=229.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.91 liquidity=15564284.0 spike=0.22
- EFID.CA: score=7.63 buy_ready=False sector_rank=21 price=19.07 support=18.1 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.88 liquidity=15174604.0 spike=0.26
- EFIH.CA: score=30.38 buy_ready=False sector_rank=1 price=25.3 support=20.2 resistance=24.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.73 liquidity=119781336.0 spike=1.99
- EGAL.CA: score=11.93 buy_ready=False sector_rank=12 price=339.98 support=331.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=104605384.0 spike=2.02
- EGAS.CA: score=9.38 buy_ready=False sector_rank=8 price=56.15 support=53.62 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.51 liquidity=3657010.75 spike=0.32
- EGBE.CA: score=8.67 buy_ready=False sector_rank=10 price=0.54 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.35 liquidity=141440.25 spike=1.16
- EGCH.CA: score=14.89 buy_ready=False sector_rank=12 price=13.36 support=12.88 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.05 liquidity=29302782.0 spike=0.31
- EGSA.CA: score=6.4 buy_ready=False sector_rank=2 price=8.87 support=8.82 resistance=9.1 source=Yahoo Finance as_of=2026-10-05T21:00:00+00:00 freshness=FRESH RSI=11.76 liquidity=0.0 spike=0.0
- EGTS.CA: score=11.11 buy_ready=False sector_rank=17 price=16.42 support=15.65 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.8 liquidity=6696034.0 spike=0.19
- EHDR.CA: score=11.07 buy_ready=False sector_rank=13 price=2.53 support=2.35 resistance=2.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.71 liquidity=6277300.5 spike=0.52
- ELEC.CA: score=15.54 buy_ready=False sector_rank=16 price=1.87 support=1.72 resistance=2.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=16595071.0 spike=0.25
- ELKA.CA: score=16.8 buy_ready=False sector_rank=13 price=1.61 support=1.43 resistance=1.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.04 liquidity=13620799.0 spike=0.97
- ELNA.CA: score=0.88 buy_ready=False sector_rank=13 price=35.22 support=33.46 resistance=38.0 source=Yahoo Finance as_of=2026-10-05T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=85584.6 spike=0.44
- ELSH.CA: score=15.4 buy_ready=False sector_rank=13 price=12.13 support=10.8 resistance=13.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.56 liquidity=28611752.0 spike=1.3
- ELWA.CA: score=-0.53 buy_ready=False sector_rank=13 price=1.59 support=1.43 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=678380.06 spike=0.76
- EMFD.CA: score=14.42 buy_ready=False sector_rank=17 price=12.8 support=11.7 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.38 liquidity=38458516.0 spike=0.46
- ENGC.CA: score=14.8 buy_ready=False sector_rank=13 price=37.0 support=33.33 resistance=46.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.44 liquidity=14276444.0 spike=0.82
- EOSB.CA: score=9.84 buy_ready=False sector_rank=13 price=1.57 support=1.58 resistance=1.64 source=Yahoo Finance as_of=2026-10-05T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=47246.01 spike=0.95
- EPCO.CA: score=2.89 buy_ready=False sector_rank=13 price=9.79 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.3 liquidity=3098196.0 spike=0.22
- EPPK.CA: score=-4.78 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.4 buy_ready=False sector_rank=2 price=147.94 support=121.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=74.5 liquidity=127165696.0 spike=0.43
- ETRS.CA: score=19.36 buy_ready=False sector_rank=13 price=10.78 support=9.82 resistance=11.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.9 liquidity=12244795.0 spike=1.28
- FAIT.CA: score=10.49 buy_ready=False sector_rank=10 price=45.59 support=38.48 resistance=48.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.83 liquidity=2281312.25 spike=0.68
- FAITA.CA: score=11.35 buy_ready=False sector_rank=10 price=1.0 support=0.98 resistance=0.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=46284.48 spike=1.55
- FERC.CA: score=6.92 buy_ready=False sector_rank=12 price=75.27 support=70.42 resistance=82.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=3032689.0 spike=0.44
- FWRY.CA: score=31.4 buy_ready=False sector_rank=1 price=19.08 support=17.5 resistance=19.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=336845728.0 spike=3.59
- GBCO.CA: score=23.48 buy_ready=False sector_rank=5 price=31.24 support=27.0 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.41 liquidity=106487056.0 spike=1.04
- GDWA.CA: score=6.99 buy_ready=False sector_rank=13 price=0.67 support=0.61 resistance=0.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.61 liquidity=8193812.0 spike=0.34
- GGCC.CA: score=6.39 buy_ready=False sector_rank=13 price=0.72 support=0.65 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.96 liquidity=6591457.5 spike=0.43
- GIHD.CA: score=9.11 buy_ready=False sector_rank=13 price=62.34 support=60.9 resistance=78.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.34 liquidity=9310697.0 spike=0.39
- GMCI.CA: score=6.12 buy_ready=False sector_rank=13 price=1.64 support=1.49 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=326856.34 spike=0.69
- GRCA.CA: score=4.51 buy_ready=False sector_rank=13 price=37.7 support=32.11 resistance=61.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.92 liquidity=3709670.75 spike=0.17
- GSSC.CA: score=6.36 buy_ready=False sector_rank=13 price=282.98 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.03 liquidity=1568603.75 spike=0.4
- HDBK.CA: score=17.21 buy_ready=False sector_rank=10 price=106.09 support=102.03 resistance=121.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.97 liquidity=19899652.0 spike=0.63
- HELI.CA: score=9.42 buy_ready=False sector_rank=17 price=7.47 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.97 liquidity=28097854.0 spike=0.24
- HRHO.CA: score=24.49 buy_ready=False sector_rank=9 price=26.7 support=22.81 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.3 liquidity=112811784.0 spike=0.88
- ICID.CA: score=12.29 buy_ready=False sector_rank=13 price=18.17 support=16.52 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.36 liquidity=2497930.0 spike=0.3
- IDRE.CA: score=8.56 buy_ready=False sector_rank=13 price=50.14 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.46 liquidity=3764239.25 spike=0.25
- IFAP.CA: score=10.69 buy_ready=False sector_rank=11 price=19.4 support=17.17 resistance=21.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.31 liquidity=6589111.0 spike=0.76
- INFI.CA: score=17.6 buy_ready=False sector_rank=13 price=129.14 support=104.0 resistance=149.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.72 liquidity=19573418.0 spike=1.4
- IRON.CA: score=26.03 buy_ready=False sector_rank=12 price=29.79 support=25.01 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.59 liquidity=30631262.0 spike=2.57
- ISMA.CA: score=7.11 buy_ready=False sector_rank=13 price=25.6 support=22.7 resistance=34.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=38.36 liquidity=2318015.75 spike=0.17
- ISMQ.CA: score=14.89 buy_ready=False sector_rank=12 price=8.25 support=7.6 resistance=9.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.11 liquidity=14726316.0 spike=0.71
- ISPH.CA: score=14.32 buy_ready=False sector_rank=18 price=11.65 support=11.22 resistance=13.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.86 liquidity=21800542.0 spike=0.33
- JUFO.CA: score=7.97 buy_ready=False sector_rank=21 price=24.98 support=24.4 resistance=27.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.92 liquidity=18329734.0 spike=1.17
- KABO.CA: score=12.47 buy_ready=False sector_rank=14 price=8.81 support=7.97 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.8 liquidity=7739932.0 spike=0.24
- KWIN.CA: score=4.61 buy_ready=False sector_rank=13 price=76.75 support=72.21 resistance=98.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.86 liquidity=4817749.0 spike=0.38
- KZPC.CA: score=8.65 buy_ready=False sector_rank=13 price=13.17 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=5851179.0 spike=0.34
- LCSW.CA: score=27.12 buy_ready=False sector_rank=3 price=34.8 support=28.86 resistance=35.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.76 liquidity=25130000.0 spike=1.36
- LUTS.CA: score=16.8 buy_ready=False sector_rank=13 price=0.91 support=0.72 resistance=1.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.01 liquidity=44133560.0 spike=0.52
- MAAL.CA: score=17.18 buy_ready=False sector_rank=13 price=10.9 support=8.18 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=72.18 liquidity=7383571.0 spike=0.32
- MASR.CA: score=21.8 buy_ready=False sector_rank=13 price=7.87 support=6.82 resistance=8.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.4 liquidity=59666584.0 spike=0.82
- MBSC.CA: score=26.08 buy_ready=False sector_rank=3 price=376.31 support=288.0 resistance=426.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.65 liquidity=140725760.0 spike=1.84
- MCQE.CA: score=18.92 buy_ready=False sector_rank=3 price=196.74 support=177.02 resistance=246.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.28 liquidity=75153696.0 spike=1.76
- MCRO.CA: score=9.8 buy_ready=False sector_rank=13 price=1.51 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.15 liquidity=27537760.0 spike=0.3
- MENA.CA: score=11.06 buy_ready=False sector_rank=17 price=6.7 support=5.8 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=52.9 liquidity=1708372.0 spike=1.47
- MEPA.CA: score=9.56 buy_ready=False sector_rank=13 price=1.72 support=1.56 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=4764783.0 spike=0.3
- MFPC.CA: score=17.89 buy_ready=False sector_rank=12 price=46.59 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.01 liquidity=26493044.0 spike=0.26
- MFSC.CA: score=7.1 buy_ready=False sector_rank=13 price=44.85 support=42.5 resistance=49.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=48.01 liquidity=2308623.25 spike=0.87
- MHOT.CA: score=10.14 buy_ready=False sector_rank=19 price=17.51 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.63 liquidity=6987822.5 spike=0.38
- MICH.CA: score=10.2 buy_ready=False sector_rank=13 price=47.04 support=42.01 resistance=51.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.32 liquidity=5405720.5 spike=0.52
- MILS.CA: score=9.35 buy_ready=False sector_rank=13 price=183.87 support=165.5 resistance=213.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.0 liquidity=4553870.0 spike=0.45
- MIPH.CA: score=12.38 buy_ready=False sector_rank=18 price=829.4 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.47 liquidity=3067752.0 spike=0.35
- MOED.CA: score=8.26 buy_ready=False sector_rank=13 price=0.68 support=0.59 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.64 liquidity=9462833.0 spike=0.27
- MOIL.CA: score=8.86 buy_ready=False sector_rank=8 price=0.69 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=55.71 liquidity=136973.08 spike=0.53
- MOIN.CA: score=17.8 buy_ready=False sector_rank=13 price=35.49 support=32.0 resistance=42.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.97 liquidity=15049192.0 spike=0.97
- MOSC.CA: score=5.85 buy_ready=False sector_rank=13 price=278.65 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.95 liquidity=1053731.0 spike=0.28
- MPCI.CA: score=9.8 buy_ready=False sector_rank=13 price=346.01 support=305.45 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.3 liquidity=69052720.0 spike=0.66
- MPCO.CA: score=13.1 buy_ready=False sector_rank=11 price=2.39 support=2.18 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.91 liquidity=66783352.0 spike=0.35
- MPRC.CA: score=13.09 buy_ready=False sector_rank=13 price=40.23 support=37.65 resistance=42.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=4294061.5 spike=0.21
- MTIE.CA: score=16.05 buy_ready=False sector_rank=5 price=8.06 support=7.5 resistance=8.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=8651205.0 spike=0.49
- NAHO.CA: score=4.81 buy_ready=False sector_rank=13 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance as_of=2026-10-05T21:00:00+00:00 freshness=FRESH RSI=43.33 liquidity=9680.54 spike=0.25
- NCCW.CA: score=17.8 buy_ready=False sector_rank=13 price=7.02 support=6.3 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=12800883.0 spike=0.16
- NEDA.CA: score=5.01 buy_ready=False sector_rank=13 price=2.61 support=2.48 resistance=2.89 source=Yahoo Finance as_of=2026-10-05T21:00:00+00:00 freshness=FRESH RSI=36.59 liquidity=210462.56 spike=0.26
- NHPS.CA: score=11.45 buy_ready=False sector_rank=13 price=73.29 support=66.0 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=4656476.0 spike=0.31
- NINH.CA: score=8.2 buy_ready=False sector_rank=13 price=19.06 support=18.53 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.2 liquidity=8400085.0 spike=0.58
- NIPH.CA: score=16.32 buy_ready=False sector_rank=18 price=316.85 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.95 liquidity=37717136.0 spike=0.3
- OBRI.CA: score=13.64 buy_ready=False sector_rank=13 price=28.36 support=22.8 resistance=33.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.53 liquidity=7847824.0 spike=0.63
- OCDI.CA: score=9.42 buy_ready=False sector_rank=17 price=27.51 support=24.2 resistance=33.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.34 liquidity=14881147.0 spike=0.29
- OCPH.CA: score=7.83 buy_ready=False sector_rank=13 price=221.69 support=190.0 resistance=258.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.56 liquidity=2031291.38 spike=0.52
- ODIN.CA: score=9.3 buy_ready=False sector_rank=13 price=2.53 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=4499393.0 spike=0.48
- OFH.CA: score=14.8 buy_ready=False sector_rank=13 price=0.88 support=0.83 resistance=1.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.42 liquidity=23496336.0 spike=0.22
- OIH.CA: score=10.93 buy_ready=False sector_rank=6 price=1.88 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.64 liquidity=22657394.0 spike=0.22
- OLFI.CA: score=7.63 buy_ready=False sector_rank=21 price=21.09 support=20.82 resistance=23.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.53 liquidity=10934591.0 spike=0.62
- ORAS.CA: score=4.6 buy_ready=False sector_rank=15 price=880.1 support=839.0 resistance=894.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=637229824.0 spike=1.0
- ORWE.CA: score=17.73 buy_ready=False sector_rank=14 price=27.1 support=26.01 resistance=28.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.69 liquidity=10873100.0 spike=0.27
- PHAR.CA: score=16.32 buy_ready=False sector_rank=18 price=113.97 support=102.0 resistance=129.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=25178564.0 spike=0.33
- PHDC.CA: score=16.42 buy_ready=False sector_rank=17 price=12.81 support=12.36 resistance=14.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.05 liquidity=74709600.0 spike=0.66
- PHTV.CA: score=5.25 buy_ready=False sector_rank=13 price=351.81 support=315.1 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=33.51 liquidity=453466.38 spike=0.35
- POUL.CA: score=7.63 buy_ready=False sector_rank=21 price=9.99 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=5.02 liquidity=16065999.0 spike=0.48
- PRCL.CA: score=4.05 buy_ready=False sector_rank=3 price=25.62 support=22.8 resistance=33.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.6 liquidity=1653549.75 spike=0.13
- PRDC.CA: score=16.42 buy_ready=False sector_rank=17 price=7.1 support=6.81 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.65 liquidity=29576354.0 spike=0.85
- PRMH.CA: score=1.13 buy_ready=False sector_rank=13 price=2.24 support=2.03 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.48 liquidity=2330361.75 spike=0.55
- RACC.CA: score=10.79 buy_ready=False sector_rank=13 price=9.32 support=8.51 resistance=10.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.98 liquidity=3995696.0 spike=0.55
- RAKT.CA: score=18.12 buy_ready=False sector_rank=13 price=23.89 support=20.26 resistance=23.9 source=Yahoo Finance as_of=2026-10-05T21:00:00+00:00 freshness=FRESH RSI=65.9 liquidity=1328021.18 spike=4.35
- RAYA.CA: score=13.23 buy_ready=False sector_rank=20 price=6.6 support=5.72 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.55 liquidity=9128606.0 spike=0.24
- RMDA.CA: score=9.32 buy_ready=False sector_rank=18 price=5.41 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.28 liquidity=14428980.0 spike=0.41
- ROTO.CA: score=18.74 buy_ready=False sector_rank=13 price=40.86 support=35.02 resistance=43.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.31 liquidity=9481346.0 spike=1.23
- RREI.CA: score=10.89 buy_ready=False sector_rank=13 price=3.91 support=3.53 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.31 liquidity=6090772.5 spike=0.55
- RTVC.CA: score=5.56 buy_ready=False sector_rank=13 price=3.68 support=3.37 resistance=4.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=38.14 liquidity=1763579.75 spike=0.64
- RUBX.CA: score=24.4 buy_ready=False sector_rank=13 price=18.0 support=12.65 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=114043088.0 spike=1.3
- SAUD.CA: score=8.7 buy_ready=False sector_rank=10 price=22.97 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=3489159.75 spike=0.18
- SCEM.CA: score=17.4 buy_ready=False sector_rank=3 price=85.59 support=74.55 resistance=102.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.04 liquidity=38621156.0 spike=0.63
- SCFM.CA: score=4.44 buy_ready=False sector_rank=13 price=245.34 support=223.11 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.55 liquidity=644260.19 spike=0.26
- SCTS.CA: score=1.96 buy_ready=False sector_rank=4 price=549.77 support=520.3 resistance=635.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.09 liquidity=564919.75 spike=0.33
- SDTI.CA: score=19.8 buy_ready=False sector_rank=13 price=87.0 support=71.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=74.3 liquidity=25393230.0 spike=0.8
- SEIG.CA: score=8.04 buy_ready=False sector_rank=13 price=233.37 support=200.0 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=46.89 liquidity=1241064.75 spike=0.55
- SIPC.CA: score=9.8 buy_ready=False sector_rank=13 price=6.17 support=5.75 resistance=6.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=183080896.0 spike=3.71
- SKPC.CA: score=8.89 buy_ready=False sector_rank=12 price=16.25 support=15.4 resistance=19.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=54627872.0 spike=0.6
- SMFR.CA: score=10.71 buy_ready=False sector_rank=13 price=232.15 support=205.01 resistance=261.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=1917510.38 spike=0.46
- SNFC.CA: score=20.64 buy_ready=False sector_rank=13 price=11.64 support=10.58 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=16814538.0 spike=1.42
- SPIN.CA: score=7.62 buy_ready=False sector_rank=14 price=16.31 support=15.11 resistance=19.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.63 liquidity=2892692.25 spike=0.43
- SPMD.CA: score=6.33 buy_ready=False sector_rank=13 price=0.39 support=0.36 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=18.3 liquidity=7537964.0 spike=0.1
- SUGR.CA: score=12.4 buy_ready=False sector_rank=21 price=55.76 support=50.5 resistance=64.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.33 liquidity=5769755.0 spike=0.38
- SVCE.CA: score=14.8 buy_ready=False sector_rank=13 price=10.4 support=9.24 resistance=12.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.7 liquidity=77740736.0 spike=0.75
- SWDY.CA: score=14.54 buy_ready=False sector_rank=16 price=116.27 support=102.31 resistance=136.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.48 liquidity=50833692.0 spike=0.75
- TALM.CA: score=23.4 buy_ready=False sector_rank=4 price=21.71 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.16 liquidity=17823102.0 spike=0.25
- TMGH.CA: score=8.42 buy_ready=False sector_rank=17 price=87.99 support=84.4 resistance=99.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.16 liquidity=108044592.0 spike=0.47
- TRTO.CA: score=11.0 buy_ready=False sector_rank=13 price=0.07 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-10-05T21:00:00+00:00 freshness=FRESH RSI=48.39 liquidity=20555.38 spike=1.59
- UEFM.CA: score=18.09 buy_ready=False sector_rank=13 price=520.0 support=407.57 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.47 liquidity=6833708.0 spike=2.23
- UEGC.CA: score=10.8 buy_ready=False sector_rank=13 price=1.56 support=1.37 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=12112560.0 spike=0.37
- UNIP.CA: score=14.31 buy_ready=False sector_rank=13 price=0.36 support=0.32 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.77 liquidity=7509543.0 spike=0.59
- UNIT.CA: score=10.74 buy_ready=False sector_rank=17 price=17.71 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=29.2 liquidity=24849400.0 spike=1.66
- WCDF.CA: score=4.44 buy_ready=False sector_rank=13 price=658.17 support=575.5 resistance=765.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.85 liquidity=1645160.63 spike=0.45
- WKOL.CA: score=1.76 buy_ready=False sector_rank=13 price=293.91 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.44 liquidity=2963442.0 spike=0.25
- ZEOT.CA: score=9.94 buy_ready=False sector_rank=13 price=12.6 support=10.6 resistance=14.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.63 liquidity=3140756.0 spike=0.57
- ZMID.CA: score=9.42 buy_ready=False sector_rank=17 price=7.53 support=7.07 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.19 liquidity=38107844.0 spike=0.33

## Backtesting Lite
- FWRY.CA: 180d return=11.76%, max drawdown=-18.89%, MA20>MA50 days last20=3, as_of=2026-10-05T21:00:00+00:00
- EFIH.CA: 180d return=12.3%, max drawdown=-22.68%, MA20>MA50 days last20=10, as_of=2026-10-05T21:00:00+00:00
- LCSW.CA: 180d return=46.67%, max drawdown=-17.84%, MA20>MA50 days last20=9, as_of=2026-10-05T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- MBSC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=644 sources=3 expected=Misr Beni Suef Cement summary=Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025; Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25; Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25
  - Misr Beni Suef’s consolidated net profits near EGP 4bn in 2025: https://english.mubasher.info/news/4599415/Misr-Beni-Suef-s-consolidated-net-profits-near-EGP-4bn-in-2025/
  - Misr Beni Suef’s consolidated net profits hit EGP 953m in H1-25: https://english.mubasher.info/news/4488249/Misr-Beni-Suef-s-consolidated-net-profits-hit-EGP-953m-in-H1-25/
  - Misr Beni Suef Cement’s consolidate profits fall to EGP 574m in Q1-25: https://english.mubasher.info/news/4455784/Misr-Beni-Suef-Cement-s-consolidate-profits-fall-to-EGP-574m-in-Q1-25/
- IRON.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Iron and Steel summary=Evidence rejected for IRON.CA: source text did not clearly match IRON.CA / Egyptian Iron and Steel.
- ARAB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Developers Holding summary=Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency; FRA gives initial approval for Arab Developers’ rights issue; Arab Developers stock stabilizes after correction
  - Arab Developers Holding unveils EGP 1bn expansion plans to improve financial efficiency: https://english.mubasher.info/news/4601724/Arab-Developers-Holding-unveils-EGP-1bn-expansion-plans-to-improve-financial-efficiency/
  - FRA gives initial approval for Arab Developers’ rights issue: https://english.mubasher.info/news/4582627/FRA-gives-initial-approval-for-Arab-Developers-rights-issue/
  - Arab Developers stock stabilizes after correction: https://english.mubasher.info/news/4564643/Arab-Developers-stock-stabilizes-after-correction/
- HRHO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=EFG Holding summary=Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- ARCC.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=644 sources=3 expected=Arabian Cement Company summary=Arabian Cement to pay out EGP 2bn dividends for 2025; Arabian Cement’s EGM approves nearly EGP 8m capital cut; Arabian Cement’s consolidated profits near EGP 3.6bn in 2025
  - Arabian Cement to pay out EGP 2bn dividends for 2025: https://english.mubasher.info/news/4587912/Arabian-Cement-to-pay-out-EGP-2bn-dividends-for-2025/
  - Arabian Cement’s EGM approves nearly EGP 8m capital cut: https://english.mubasher.info/news/4583762/Arabian-Cement-s-EGM-approves-nearly-EGP-8m-capital-cut/
  - Arabian Cement’s consolidated profits near EGP 3.6bn in 2025: https://english.mubasher.info/news/4562679/Arabian-Cement-s-consolidated-profits-near-EGP-3-6bn-in-2025/

## Warnings
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for MBSC.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for IRON.CA: source text did not clearly match IRON.CA / Egyptian Iron and Steel.
- Evidence for ARAB.CA matches the company but no source/report date was detected.
- Evidence rejected for HRHO.CA: source text did not clearly match HRHO.CA / EFG Holding.
- Evidence for ARCC.CA matches the company but appears old; latest detected date is 2025-01-01.
