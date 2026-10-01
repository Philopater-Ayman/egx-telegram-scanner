# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-10-01T13:08:34.506716+00:00
Generated Cairo: 2026-10-01 16:08
Run timing: target 09:15 Cairo | generated Cairo 2026-10-01 16:08 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-10-01 16:05

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 4
- Tradeable price/liquidity tickers: 131/186
- Top sector: Textiles

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, October 01
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 7.14% / above MA50 28.57%
- EGX70 regime: BEARISH / above MA20 22.58% / above MA50 22.58%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=765236672.0 spike=0.95 score=22.14
- COMI.CA: liquidity=433336992.0 spike=0.77 score=8.48
- GTWL.CA: liquidity=428487424.0 spike=2.9 score=8.05
- BIOC.CA: liquidity=390132896.0 spike=5.51 score=9.25
- GBCO.CA: liquidity=316754912.0 spike=4.33 score=28.4

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: 

## Top Liquidity Spikes
- BIOC.CA: spike=5.51 liquidity=390132896.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GBCO.CA: spike=4.33 liquidity=316754912.0 outlook=BULLISH_WATCH score=97.49 buy_ready=False
- MOSC.CA: spike=3.79 liquidity=13381944.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=2.9 liquidity=428487424.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MBSC.CA: spike=2.64 liquidity=95469816.0 outlook=NEUTRAL score=35.62 buy_ready=False

## Sector Leaderboard
- #1 Textiles: score=6.61 5d=0.94% 20d=2.26% aboveMA50=75.0%
- #2 Automotive & Distribution: score=6.49 5d=-1.78% 20d=1.76% aboveMA50=50.0%
- #3 Investment Holding: score=5.35 5d=-6.36% 20d=12.37% aboveMA50=66.67%
- #4 Telecommunications: score=4.0 5d=-2.3% 20d=7.64% aboveMA50=50.0%
- #5 Energy & Petrochemicals: score=3.06 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #6 Building Materials: score=2.62 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Technology & Distribution: score=1.62 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- GBCO.CA: BULLISH_WATCH score=97.49 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- ACGC.CA: BULLISH_WATCH score=92.61 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KABO.CA: BULLISH_WATCH score=91.61 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- CCAP.CA: BULLISH_WATCH score=90.35 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- NIPH.CA: BULLISH_WATCH score=82 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=78.35 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- CANA.CA: BULLISH_WATCH score=72.21 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ORWE.CA: BULLISH_WATCH score=70.61 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- CIRA.CA: CONSTRUCTIVE score=65.82 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- ICID.CA: CONSTRUCTIVE score=64.62 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- MFSC.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=4.25 buy_ready=False sector_rank=13 price=256.21 support=244.0 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10411195.0 spike=0.44
- ABUK.CA: score=10.62 buy_ready=False sector_rank=19 price=87.02 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.97 liquidity=41764384.0 spike=0.29
- ACAMD.CA: score=14.25 buy_ready=False sector_rank=13 price=2.03 support=1.87 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=30133666.0 spike=0.59
- ACGC.CA: score=24.4 buy_ready=False sector_rank=1 price=14.52 support=13.11 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.21 liquidity=20228772.0 spike=0.78
- ADCI.CA: score=1.99 buy_ready=False sector_rank=13 price=272.0 support=256.0 resistance=303.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.14 liquidity=2737622.5 spike=1.0
- ADIB.CA: score=14.48 buy_ready=False sector_rank=9 price=49.81 support=48.2 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.0 liquidity=59822364.0 spike=0.78
- ADPC.CA: score=3.81 buy_ready=False sector_rank=13 price=3.61 support=3.4 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=23.81 liquidity=5559813.0 spike=0.31
- AFDI.CA: score=8.0 buy_ready=False sector_rank=13 price=52.0 support=47.7 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=3755756.0 spike=0.45
- AFMC.CA: score=6.45 buy_ready=False sector_rank=13 price=161.7 support=148.11 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=104528752.0 spike=2.1
- AJWA.CA: score=16.17 buy_ready=False sector_rank=13 price=182.07 support=175.15 resistance=188.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.26 liquidity=7925367.5 spike=0.53
- ALCN.CA: score=19.3 buy_ready=False sector_rank=11 price=34.09 support=30.4 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.05 liquidity=24524578.0 spike=0.72
- ALUM.CA: score=3.02 buy_ready=False sector_rank=13 price=23.74 support=21.65 resistance=29.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.96 liquidity=3771939.25 spike=0.63
- AMER.CA: score=3.64 buy_ready=False sector_rank=18 price=4.51 support=4.36 resistance=4.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=51191684.0 spike=1.32
- AMES.CA: score=10.25 buy_ready=False sector_rank=13 price=46.76 support=40.15 resistance=94.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.28 liquidity=106278168.0 spike=0.43
- AMIA.CA: score=17.25 buy_ready=False sector_rank=13 price=18.43 support=17.12 resistance=20.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.32 liquidity=10158685.0 spike=0.48
- AMOC.CA: score=6.0 buy_ready=False sector_rank=5 price=14.04 support=13.2 resistance=14.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=186981728.0 spike=1.39
- APSW.CA: score=-1.24 buy_ready=False sector_rank=13 price=8.23 support=7.81 resistance=8.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=25.9 liquidity=508066.53 spike=0.75
- ARAB.CA: score=8.0 buy_ready=False sector_rank=18 price=0.24 support=0.2 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.89 liquidity=54122496.0 spike=0.77
- ARCC.CA: score=5.31 buy_ready=False sector_rank=6 price=67.18 support=63.5 resistance=67.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24494290.0 spike=1.13
- AREH.CA: score=4.89 buy_ready=False sector_rank=13 price=1.29 support=1.23 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17385762.0 spike=1.32
- ASCM.CA: score=7.75 buy_ready=False sector_rank=13 price=58.52 support=53.8 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=17.57 liquidity=8499498.0 spike=0.53
- ASPI.CA: score=4.25 buy_ready=False sector_rank=13 price=0.36 support=0.34 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22286978.0 spike=0.43
- ATLC.CA: score=3.34 buy_ready=False sector_rank=17 price=6.13 support=5.62 resistance=6.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12849838.0 spike=0.72
- ATQA.CA: score=7.62 buy_ready=False sector_rank=19 price=11.33 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.35 liquidity=64106272.0 spike=0.74
- AXPH.CA: score=8.77 buy_ready=False sector_rank=13 price=1507.07 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.39 liquidity=6518098.0 spike=0.96
- BINV.CA: score=22.94 buy_ready=False sector_rank=3 price=59.74 support=49.51 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.08 liquidity=33516240.0 spike=1.4
- BIOC.CA: score=9.25 buy_ready=False sector_rank=13 price=348.22 support=334.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=390132896.0 spike=5.51
- BTFH.CA: score=12.34 buy_ready=False sector_rank=17 price=2.81 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=90586704.0 spike=1.0
- CAED.CA: score=4.39 buy_ready=False sector_rank=13 price=122.16 support=113.5 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20664902.0 spike=1.07
- CANA.CA: score=19.48 buy_ready=False sector_rank=9 price=45.77 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=60.94 liquidity=10106805.0 spike=0.41
- CCAP.CA: score=22.14 buy_ready=False sector_rank=3 price=6.85 support=5.85 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.21 liquidity=765236672.0 spike=0.95
- CCRS.CA: score=14.25 buy_ready=False sector_rank=13 price=2.4 support=2.21 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.27 liquidity=11642742.0 spike=0.69
- CEFM.CA: score=1.47 buy_ready=False sector_rank=13 price=139.56 support=134.95 resistance=144.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7218589.0 spike=0.94
- CERA.CA: score=4.37 buy_ready=False sector_rank=13 price=1.38 support=1.26 resistance=1.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=145627264.0 spike=1.06
- CFGH.CA: score=-1.74 buy_ready=False sector_rank=13 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=30 September 12:44 PM market time freshness=DELAYED_CURRENT RSI=10.0 liquidity=8576.05 spike=0.76
- CICH.CA: score=-1.34 buy_ready=False sector_rank=17 price=11.67 support=10.75 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=33.85 liquidity=319463.19 spike=0.05
- CIEB.CA: score=9.32 buy_ready=False sector_rank=9 price=23.95 support=23.0 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.7 liquidity=9835894.0 spike=0.81
- CIRA.CA: score=19.33 buy_ready=False sector_rank=10 price=39.29 support=34.02 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.91 liquidity=15913002.0 spike=0.44
- CLHO.CA: score=8.77 buy_ready=False sector_rank=15 price=15.55 support=13.9 resistance=18.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.94 liquidity=21609062.0 spike=0.41
- CNFN.CA: score=3.64 buy_ready=False sector_rank=17 price=4.15 support=3.84 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.95 liquidity=6301971.5 spike=0.6
- COMI.CA: score=8.48 buy_ready=False sector_rank=9 price=127.23 support=124.5 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.15 liquidity=433336992.0 spike=0.77
- COPR.CA: score=4.25 buy_ready=False sector_rank=13 price=0.49 support=0.47 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19917622.0 spike=0.67
- COSG.CA: score=4.33 buy_ready=False sector_rank=13 price=1.6 support=1.53 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24554004.0 spike=1.04
- CPCI.CA: score=19.84 buy_ready=False sector_rank=13 price=595.69 support=530.0 resistance=594.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=82.7 liquidity=8553842.0 spike=2.52
- CSAG.CA: score=3.28 buy_ready=False sector_rank=11 price=36.5 support=34.52 resistance=42.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=3983121.25 spike=0.38
- DAPH.CA: score=9.35 buy_ready=False sector_rank=13 price=95.0 support=89.1 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.07 liquidity=28458900.0 spike=1.05
- DEIN.CA: score=7.25 buy_ready=False sector_rank=13 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=1.25 buy_ready=False sector_rank=21 price=25.24 support=23.81 resistance=29.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.36 liquidity=4785153.5 spike=1.03
- DSCW.CA: score=9.47 buy_ready=False sector_rank=13 price=1.7 support=1.58 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=34569304.0 spike=1.61
- DTPP.CA: score=4.25 buy_ready=False sector_rank=13 price=292.19 support=276.0 resistance=294.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28608014.0 spike=0.33
- EALR.CA: score=2.59 buy_ready=False sector_rank=13 price=334.74 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.0 liquidity=4341860.0 spike=0.36
- EASB.CA: score=2.7 buy_ready=False sector_rank=13 price=7.19 support=6.04 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.22 liquidity=3447170.25 spike=0.24
- EAST.CA: score=6.4 buy_ready=False sector_rank=21 price=29.28 support=27.91 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=2.28 liquidity=39741072.0 spike=0.83
- EBSC.CA: score=-0.23 buy_ready=False sector_rank=13 price=1.75 support=1.61 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=15.71 liquidity=1521948.38 spike=0.3
- ECAP.CA: score=3.09 buy_ready=False sector_rank=13 price=30.91 support=29.13 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=22.95 liquidity=3843826.0 spike=0.78
- EDFM.CA: score=6.82 buy_ready=False sector_rank=13 price=401.0 support=354.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.64 liquidity=2091765.88 spike=1.24
- EEII.CA: score=8.75 buy_ready=False sector_rank=13 price=2.12 support=2.02 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.12 liquidity=13392573.0 spike=1.25
- EFIC.CA: score=6.62 buy_ready=False sector_rank=19 price=168.28 support=147.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.31 liquidity=61868308.0 spike=0.17
- EFID.CA: score=7.54 buy_ready=False sector_rank=21 price=19.29 support=18.1 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=8.01 liquidity=100592112.0 spike=1.57
- EFIH.CA: score=4.29 buy_ready=False sector_rank=12 price=23.35 support=22.23 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=47452852.0 spike=0.92
- EGAL.CA: score=11.46 buy_ready=False sector_rank=19 price=341.74 support=331.5 resistance=383.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.72 liquidity=67241072.0 spike=1.42
- EGAS.CA: score=10.25 buy_ready=False sector_rank=5 price=56.43 support=53.62 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.19 liquidity=5028063.5 spike=0.39
- EGBE.CA: score=9.65 buy_ready=False sector_rank=9 price=0.52 support=0.49 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=224180.33 spike=2.47
- EGCH.CA: score=12.62 buy_ready=False sector_rank=19 price=13.58 support=12.88 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.37 liquidity=48579888.0 spike=0.39
- EGSA.CA: score=0.6 buy_ready=False sector_rank=4 price=8.85 support=8.82 resistance=9.1 source=Yahoo Finance as_of=2026-09-29T21:00:00+00:00 freshness=FRESH RSI=7.69 liquidity=601.8 spike=0.09
- EGTS.CA: score=13.0 buy_ready=False sector_rank=18 price=16.44 support=15.65 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.69 liquidity=15384810.0 spike=0.44
- EHDR.CA: score=7.07 buy_ready=False sector_rank=13 price=2.51 support=2.35 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.45 liquidity=7824288.5 spike=0.49
- ELEC.CA: score=7.52 buy_ready=False sector_rank=16 price=1.88 support=1.72 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.28 liquidity=41312212.0 spike=0.6
- ELKA.CA: score=4.07 buy_ready=False sector_rank=13 price=1.57 support=1.51 resistance=1.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9823194.0 spike=0.6
- ELNA.CA: score=0.3 buy_ready=False sector_rank=13 price=35.22 support=33.46 resistance=38.99 source=Yahoo Finance as_of=2026-09-29T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=52231.26 spike=0.16
- ELSH.CA: score=4.25 buy_ready=False sector_rank=13 price=11.91 support=11.22 resistance=11.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10295905.0 spike=0.38
- ELWA.CA: score=0.04 buy_ready=False sector_rank=13 price=1.46 support=1.44 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:07 PM market time freshness=DELAYED_CURRENT RSI=5.56 liquidity=1248847.25 spike=1.27
- EMFD.CA: score=3.08 buy_ready=False sector_rank=18 price=12.86 support=12.56 resistance=12.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106884104.0 spike=1.04
- ENGC.CA: score=4.25 buy_ready=False sector_rank=13 price=36.41 support=34.7 resistance=36.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17064624.0 spike=1.0
- EOSB.CA: score=9.25 buy_ready=False sector_rank=13 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-29T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6958.24 spike=0.13
- EPCO.CA: score=-2.68 buy_ready=False sector_rank=13 price=10.0 support=9.61 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3072172.25 spike=0.21
- EPPK.CA: score=-5.33 buy_ready=False sector_rank=13 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=18.6 buy_ready=False sector_rank=4 price=138.71 support=113.99 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.7 liquidity=132174968.0 spike=0.44
- ETRS.CA: score=3.06 buy_ready=False sector_rank=13 price=10.5 support=9.82 resistance=11.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.77 liquidity=3812142.0 spike=0.4
- EXPA.CA: score=17.68 buy_ready=False sector_rank=9 price=21.03 support=20.4 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.47 liquidity=38960196.0 spike=1.1
- FAIT.CA: score=6.17 buy_ready=False sector_rank=9 price=45.31 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.79 liquidity=3686858.75 spike=0.73
- FAITA.CA: score=3.49 buy_ready=False sector_rank=9 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-09-29T21:00:00+00:00 freshness=FRESH RSI=43.75 liquidity=2983.32 spike=0.09
- FERC.CA: score=3.88 buy_ready=False sector_rank=19 price=76.66 support=70.42 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.95 liquidity=2257315.0 spike=0.21
- FWRY.CA: score=10.21 buy_ready=False sector_rank=12 price=18.86 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=136309360.0 spike=1.46
- GBCO.CA: score=28.4 buy_ready=False sector_rank=2 price=31.17 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=316754912.0 spike=4.33
- GDWA.CA: score=8.25 buy_ready=False sector_rank=13 price=0.68 support=0.61 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=6.59 liquidity=18957950.0 spike=0.57
- GGCC.CA: score=9.25 buy_ready=False sector_rank=13 price=0.69 support=0.65 resistance=0.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.95 liquidity=11852867.0 spike=0.72
- GIHD.CA: score=9.25 buy_ready=False sector_rank=13 price=63.51 support=60.9 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.68 liquidity=11754000.0 spike=0.42
- GMCI.CA: score=0.7 buy_ready=False sector_rank=13 price=1.57 support=1.49 resistance=1.94 source=Yahoo Finance as_of=2026-09-29T21:00:00+00:00 freshness=FRESH RSI=19.61 liquidity=893507.44 spike=1.78
- GRCA.CA: score=1.34 buy_ready=False sector_rank=13 price=37.0 support=33.04 resistance=37.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7089914.0 spike=0.23
- GSSC.CA: score=-4.46 buy_ready=False sector_rank=13 price=272.0 support=262.0 resistance=273.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1296632.13 spike=0.17
- GTWL.CA: score=8.05 buy_ready=False sector_rank=13 price=171.47 support=150.0 resistance=175.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=428487424.0 spike=2.9
- HDBK.CA: score=4.48 buy_ready=False sector_rank=9 price=110.94 support=105.25 resistance=111.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17198646.0 spike=0.39
- HELI.CA: score=8.0 buy_ready=False sector_rank=18 price=7.45 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.57 liquidity=64429796.0 spike=0.44
- HRHO.CA: score=7.76 buy_ready=False sector_rank=17 price=24.2 support=22.81 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=13.62 liquidity=90606032.0 spike=1.21
- ICID.CA: score=19.63 buy_ready=False sector_rank=13 price=18.8 support=16.52 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.77 liquidity=10103487.0 spike=1.19
- IDRE.CA: score=10.57 buy_ready=False sector_rank=13 price=49.64 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.24 liquidity=6320319.5 spike=0.41
- IFAP.CA: score=0.49 buy_ready=False sector_rank=14 price=19.33 support=17.17 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=33.56 liquidity=2396055.75 spike=0.15
- INFI.CA: score=9.25 buy_ready=False sector_rank=13 price=123.74 support=104.0 resistance=160.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.05 liquidity=11757490.0 spike=0.73
- IRON.CA: score=6.62 buy_ready=False sector_rank=19 price=26.55 support=25.01 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.88 liquidity=10061731.0 spike=0.78
- ISMA.CA: score=4.35 buy_ready=False sector_rank=13 price=25.4 support=23.2 resistance=26.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15465776.0 spike=1.05
- ISMQ.CA: score=8.28 buy_ready=False sector_rank=19 price=8.08 support=7.6 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.31 liquidity=28160830.0 spike=1.33
- ISPH.CA: score=10.25 buy_ready=False sector_rank=15 price=11.69 support=11.22 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.64 liquidity=120807616.0 spike=1.74
- JUFO.CA: score=6.4 buy_ready=False sector_rank=21 price=25.06 support=24.4 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.65 liquidity=13796450.0 spike=0.7
- KABO.CA: score=25.06 buy_ready=False sector_rank=1 price=9.24 support=7.97 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=45241528.0 spike=1.33
- KWIN.CA: score=8.45 buy_ready=False sector_rank=13 price=79.78 support=72.21 resistance=115.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.47 liquidity=9205462.0 spike=0.56
- KZPC.CA: score=5.57 buy_ready=False sector_rank=13 price=13.0 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.13 liquidity=3326101.5 spike=0.12
- LCSW.CA: score=18.01 buy_ready=False sector_rank=6 price=33.36 support=28.86 resistance=36.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.48 liquidity=25742910.0 spike=1.48
- LUTS.CA: score=4.25 buy_ready=False sector_rank=13 price=0.93 support=0.87 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=99667696.0 spike=0.98
- MAAL.CA: score=4.25 buy_ready=False sector_rank=13 price=10.82 support=9.96 resistance=11.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20857176.0 spike=0.95
- MASR.CA: score=9.25 buy_ready=False sector_rank=13 price=7.67 support=6.82 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.81 liquidity=59795504.0 spike=0.62
- MBSC.CA: score=13.33 buy_ready=False sector_rank=6 price=297.0 support=288.0 resistance=438.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=0.87 liquidity=95469816.0 spike=2.64
- MCQE.CA: score=7.29 buy_ready=False sector_rank=6 price=189.77 support=182.0 resistance=190.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41911252.0 spike=2.12
- MCRO.CA: score=9.25 buy_ready=False sector_rank=13 price=1.55 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.62 liquidity=66884412.0 spike=0.54
- MENA.CA: score=-1.47 buy_ready=False sector_rank=18 price=6.26 support=5.8 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.45 liquidity=534180.19 spike=0.44
- MEPA.CA: score=2.7 buy_ready=False sector_rank=13 price=1.72 support=1.64 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8452793.0 spike=0.23
- MFPC.CA: score=15.62 buy_ready=False sector_rank=19 price=45.61 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.29 liquidity=32510658.0 spike=0.24
- MHOT.CA: score=11.4 buy_ready=False sector_rank=20 price=17.39 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.77 liquidity=16469191.0 spike=0.92
- MICH.CA: score=4.88 buy_ready=False sector_rank=13 price=45.93 support=42.01 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.92 liquidity=5636002.5 spike=0.46
- MILS.CA: score=9.89 buy_ready=False sector_rank=13 price=183.61 support=165.5 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.34 liquidity=23853800.0 spike=1.32
- MIPH.CA: score=8.17 buy_ready=False sector_rank=15 price=812.49 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.91 liquidity=1395794.5 spike=0.15
- MOED.CA: score=4.25 buy_ready=False sector_rank=13 price=0.68 support=0.65 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18328246.0 spike=0.41
- MOIL.CA: score=10.4 buy_ready=False sector_rank=5 price=0.71 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=71.19 liquidity=176434.23 spike=0.71
- MOIN.CA: score=9.9 buy_ready=False sector_rank=13 price=35.02 support=32.0 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.96 liquidity=7655754.0 spike=0.26
- MOSC.CA: score=9.25 buy_ready=False sector_rank=13 price=282.63 support=267.0 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13381944.0 spike=3.79
- MPCI.CA: score=4.25 buy_ready=False sector_rank=13 price=346.51 support=330.06 resistance=349.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=101394648.0 spike=0.89
- MPCO.CA: score=17.09 buy_ready=False sector_rank=14 price=2.47 support=2.09 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.05 liquidity=103985920.0 spike=0.54
- MPRC.CA: score=14.25 buy_ready=False sector_rank=13 price=39.02 support=37.65 resistance=44.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.52 liquidity=24766270.0 spike=0.91
- MTIE.CA: score=8.4 buy_ready=False sector_rank=2 price=8.26 support=7.9 resistance=8.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16264616.0 spike=0.8
- NAHO.CA: score=4.26 buy_ready=False sector_rank=13 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=7341.39 spike=0.16
- NCCW.CA: score=17.25 buy_ready=False sector_rank=13 price=7.19 support=5.96 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.88 liquidity=24183374.0 spike=0.31
- NEDA.CA: score=0.16 buy_ready=False sector_rank=13 price=2.61 support=2.48 resistance=2.89 source=Yahoo Finance as_of=2026-09-29T21:00:00+00:00 freshness=FRESH RSI=31.91 liquidity=910728.14 spike=0.95
- NHPS.CA: score=5.69 buy_ready=False sector_rank=13 price=72.01 support=68.5 resistance=74.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24346756.0 spike=1.72
- NINH.CA: score=8.66 buy_ready=False sector_rank=13 price=19.25 support=18.53 resistance=24.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=22.62 liquidity=9415884.0 spike=0.63
- NIPH.CA: score=19.91 buy_ready=False sector_rank=15 price=330.97 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=42.0 liquidity=197784624.0 spike=1.57
- OBRI.CA: score=1.1 buy_ready=False sector_rank=13 price=25.74 support=24.5 resistance=25.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6852532.5 spike=0.68
- OCDI.CA: score=3.0 buy_ready=False sector_rank=18 price=26.92 support=25.6 resistance=27.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33023876.0 spike=0.57
- OCPH.CA: score=3.11 buy_ready=False sector_rank=13 price=223.92 support=190.0 resistance=263.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=4857543.0 spike=0.98
- ODIN.CA: score=3.43 buy_ready=False sector_rank=13 price=2.53 support=2.35 resistance=3.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.69 liquidity=4184796.25 spike=0.34
- OFH.CA: score=4.25 buy_ready=False sector_rank=13 price=0.92 support=0.92 resistance=0.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=93914824.0 spike=0.7
- OIH.CA: score=12.14 buy_ready=False sector_rank=3 price=1.85 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.23 liquidity=65403260.0 spike=0.59
- OLFI.CA: score=12.12 buy_ready=False sector_rank=21 price=21.64 support=21.2 resistance=23.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.57 liquidity=21442946.0 spike=1.36
- ORAS.CA: score=4.6 buy_ready=False sector_rank=8 price=819.88 support=785.0 resistance=821.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=115648824.0 spike=1.0
- ORHD.CA: score=8.0 buy_ready=False sector_rank=18 price=38.9 support=37.41 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.73 liquidity=88255360.0 spike=0.54
- ORWE.CA: score=24.4 buy_ready=False sector_rank=1 price=27.78 support=26.01 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.13 liquidity=38446832.0 spike=0.72
- PHAR.CA: score=9.97 buy_ready=False sector_rank=15 price=116.17 support=102.0 resistance=133.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=33.45 liquidity=135676176.0 spike=1.6
- PHDC.CA: score=8.0 buy_ready=False sector_rank=18 price=13.25 support=12.36 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.57 liquidity=66525856.0 spike=0.53
- PHTV.CA: score=5.0 buy_ready=False sector_rank=13 price=335.92 support=315.1 resistance=378.89 source=Yahoo Finance as_of=2026-09-29T21:00:00+00:00 freshness=FRESH RSI=40.38 liquidity=750781.23 spike=0.47
- POUL.CA: score=7.18 buy_ready=False sector_rank=21 price=10.27 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=3.65 liquidity=42851788.0 spike=1.39
- PRCL.CA: score=5.73 buy_ready=False sector_rank=6 price=26.54 support=23.56 resistance=27.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=20311010.0 spike=1.34
- PRDC.CA: score=8.0 buy_ready=False sector_rank=18 price=7.38 support=6.81 resistance=9.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.47 liquidity=13147161.0 spike=0.39
- PRMH.CA: score=1.81 buy_ready=False sector_rank=13 price=2.24 support=2.03 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=23.23 liquidity=2566537.75 spike=0.51
- RACC.CA: score=-0.45 buy_ready=False sector_rank=13 price=9.32 support=9.01 resistance=9.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5300552.0 spike=0.44
- RAKT.CA: score=-1.58 buy_ready=False sector_rank=13 price=21.32 support=20.26 resistance=23.0 source=Yahoo Finance as_of=2026-09-29T21:00:00+00:00 freshness=FRESH RSI=21.01 liquidity=171370.16 spike=0.94
- RAYA.CA: score=4.81 buy_ready=False sector_rank=7 price=6.59 support=6.22 resistance=6.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57578844.0 spike=1.08
- RMDA.CA: score=8.77 buy_ready=False sector_rank=15 price=5.46 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.48 liquidity=39145468.0 spike=0.73
- ROTO.CA: score=5.73 buy_ready=False sector_rank=13 price=40.1 support=37.07 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13450983.0 spike=1.74
- RREI.CA: score=9.09 buy_ready=False sector_rank=13 price=3.92 support=3.53 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.3 liquidity=4843850.0 spike=0.38
- RTVC.CA: score=-0.13 buy_ready=False sector_rank=13 price=3.52 support=3.37 resistance=4.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=1624713.0 spike=0.64
- RUBX.CA: score=4.25 buy_ready=False sector_rank=13 price=15.3 support=14.4 resistance=15.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=60061108.0 spike=0.87
- SAUD.CA: score=14.48 buy_ready=False sector_rank=9 price=23.11 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.45 liquidity=10103302.0 spike=0.52
- SCEM.CA: score=5.05 buy_ready=False sector_rank=6 price=80.18 support=76.9 resistance=81.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31342530.0 spike=0.48
- SCFM.CA: score=3.47 buy_ready=False sector_rank=13 price=247.9 support=223.11 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.64 liquidity=5220748.0 spike=0.88
- SCTS.CA: score=-0.01 buy_ready=False sector_rank=10 price=545.15 support=520.3 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.75 liquidity=661747.69 spike=0.31
- SDTI.CA: score=16.25 buy_ready=False sector_rank=13 price=84.33 support=69.3 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.63 liquidity=11524878.0 spike=0.34
- SEIG.CA: score=-5.03 buy_ready=False sector_rank=13 price=226.76 support=213.11 resistance=231.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=720149.5 spike=0.4
- SIPC.CA: score=12.25 buy_ready=False sector_rank=13 price=5.11 support=4.22 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=31285242.0 spike=0.44
- SKPC.CA: score=6.62 buy_ready=False sector_rank=19 price=16.19 support=15.4 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.5 liquidity=78114488.0 spike=0.72
- SMFR.CA: score=0.27 buy_ready=False sector_rank=13 price=221.72 support=210.6 resistance=234.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6025507.0 spike=0.94
- SNFC.CA: score=21.25 buy_ready=False sector_rank=13 price=11.53 support=10.27 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=64.02 liquidity=11038805.0 spike=0.8
- SPIN.CA: score=11.19 buy_ready=False sector_rank=1 price=16.46 support=15.11 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.0 liquidity=6789676.5 spike=0.93
- SPMD.CA: score=11.87 buy_ready=False sector_rank=13 price=0.38 support=0.36 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.3 liquidity=8626134.0 spike=0.11
- SUGR.CA: score=7.4 buy_ready=False sector_rank=21 price=52.89 support=50.5 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=21.36 liquidity=11619718.0 spike=0.45
- SVCE.CA: score=4.25 buy_ready=False sector_rank=13 price=10.15 support=9.72 resistance=10.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=63723600.0 spike=0.48
- SWDY.CA: score=5.28 buy_ready=False sector_rank=16 price=119.93 support=106.05 resistance=121.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=130815056.0 spike=1.88
- TALM.CA: score=4.33 buy_ready=False sector_rank=10 price=20.99 support=19.01 resistance=22.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=36861572.0 spike=0.55
- TMGH.CA: score=7.0 buy_ready=False sector_rank=18 price=88.0 support=84.4 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=8.12 liquidity=229163616.0 spike=0.85
- TRTO.CA: score=-0.75 buy_ready=False sector_rank=13 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-29T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=703.62 spike=0.04
- UEFM.CA: score=12.2 buy_ready=False sector_rank=13 price=509.97 support=407.57 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=42.66 liquidity=5272308.0 spike=1.34
- UEGC.CA: score=4.25 buy_ready=False sector_rank=13 price=1.56 support=1.49 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33204514.0 spike=0.93
- UNIP.CA: score=6.29 buy_ready=False sector_rank=13 price=0.35 support=0.32 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.09 liquidity=7038377.5 spike=0.35
- UNIT.CA: score=-4.96 buy_ready=False sector_rank=18 price=17.53 support=16.6 resistance=17.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2044588.25 spike=0.14
- WCDF.CA: score=7.39 buy_ready=False sector_rank=13 price=654.28 support=575.5 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=34.64 liquidity=5140941.0 spike=0.97
- WKOL.CA: score=0.45 buy_ready=False sector_rank=13 price=292.14 support=281.01 resistance=294.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6204073.5 spike=0.46
- ZEOT.CA: score=6.35 buy_ready=False sector_rank=13 price=12.55 support=11.56 resistance=12.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10889159.0 spike=2.05
- ZMID.CA: score=8.0 buy_ready=False sector_rank=18 price=7.68 support=7.07 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=9.79 liquidity=81778848.0 spike=0.56

## Backtesting Lite
- GBCO.CA: 180d return=13.03%, max drawdown=-24.35%, MA20>MA50 days last20=1, as_of=2026-09-29T21:00:00+00:00
- KABO.CA: 180d return=46.83%, max drawdown=-23.4%, MA20>MA50 days last20=20, as_of=2026-09-29T21:00:00+00:00
- ACGC.CA: 180d return=70.73%, max drawdown=-12.62%, MA20>MA50 days last20=20, as_of=2026-09-29T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- KABO.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nasr Clothing and Textiles summary=KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits; KABO sells over 1.9m shares in Spinalex for EGP 20m; KABO unveils international agreements, expansion plan including export lines
  - KABO posts EGP 17m in Q1-25/26 unaudited consolidated net profits: https://english.mubasher.info/news/4600162/KABO-posts-EGP-17m-in-Q1-25-26-unaudited-consolidated-net-profits/
  - KABO sells over 1.9m shares in Spinalex for EGP 20m: https://english.mubasher.info/news/4543747/KABO-sells-over-1-9m-shares-in-Spinalex-for-EGP-20m/
  - KABO unveils international agreements, expansion plan including export lines: https://english.mubasher.info/news/4533185/KABO-unveils-international-agreements-expansion-plan-including-export-lines/
- ACGC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Arab Cotton Ginning summary=Arab Cotton Ginning’s stock nears significant resistance level; Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24; Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24
  - Arab Cotton Ginning’s stock nears significant resistance level: https://english.mubasher.info/news/4549011/Arab-Cotton-Ginning-s-stock-nears-significant-resistance-level/
  - Arab Cotton Ginning’s standalone profit grows 142% YoY in 9M-23/24: https://english.mubasher.info/news/4302757/Arab-Cotton-Ginning-s-standalone-profit-grows-142-YoY-in-9M-23-24/
  - Arab Cotton Ginning’s consolidated profit leaps 371% YoY in H1-23/24: https://english.mubasher.info/news/4279332/Arab-Cotton-Ginning-s-consolidated-profit-leaps-371-YoY-in-H1-23-24/
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=638 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- CCAP.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Qalaa Holdings summary=Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- SNFC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Sharkia National Company for Food Security summary=Sharkia National Food sells EGP 6.5m asset; Sharkia Food turns profitable in Q4; Sharkia National Food turns profitable in Q4
  - Sharkia National Food sells EGP 6.5m asset: https://english.mubasher.info/news/3344769/Sharkia-National-Food-sells-EGP-6-5m-asset/
  - Sharkia Food turns profitable in Q4: https://english.mubasher.info/news/3055832/Sharkia-Food-turns-profitable-in-Q4/
  - Sharkia National Food turns profitable in Q4: https://english.mubasher.info/news/3053492/Sharkia-National-Food-turns-profitable-in-Q4/
- NIPH.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=El Nile Pharmaceuticals summary=El-Nile for Pharmaceuticals logs 155% leap in H1-25/26 net profits; Nile Pharma announces FY21/22 dividends; Nile Pharma logs EGP 90.3m profit in FY21/22
  - El-Nile for Pharmaceuticals logs 155% leap in H1-25/26 net profits: https://english.mubasher.info/news/4554358/El-Nile-for-Pharmaceuticals-logs-155-leap-in-H1-25-26-net-profits/
  - Nile Pharma announces FY21/22 dividends: https://english.mubasher.info/news/4024745/Nile-Pharma-announces-FY21-22-dividends/
  - Nile Pharma logs EGP 90.3m profit in FY21/22: https://english.mubasher.info/news/3993739/Nile-Pharma-logs-EGP-90-3m-profit-in-FY21-22/

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for KABO.CA matches the company but no source/report date was detected.
- Evidence for ACGC.CA matches the company but no source/report date was detected.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for CCAP.CA: source text did not clearly match CCAP.CA / Qalaa Holdings.
- Evidence for SNFC.CA matches the company but no source/report date was detected.
- Evidence for NIPH.CA matches the company but no source/report date was detected.
