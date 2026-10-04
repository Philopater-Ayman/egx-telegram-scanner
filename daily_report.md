# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-10-04T12:19:18.418983+00:00
Generated Cairo: 2026-10-04 15:19
Run timing: target 09:15 Cairo | generated Cairo 2026-10-04 15:19 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-10-04 15:15

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 170/187
- Top sector: Fintech & Payments

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, October 04
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 17.65% / above MA50 47.06%
- EGX70 regime: BEARISH / above MA20 32.43% / above MA50 29.73%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=632024448.0 spike=0.77 score=21.4
- HRHO.CA: liquidity=481086048.0 spike=6.31 score=9.44
- ETEL.CA: liquidity=440575968.0 spike=1.46 score=5.14
- BIOC.CA: liquidity=330133920.0 spike=4.42 score=27.94
- TMGH.CA: liquidity=270229696.0 spike=0.99 score=7.16

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (sector breadth 23.8%), risk mode is DEFENSIVE_NO_NEW_BUY, so the scanner flags accumulation spikes in a few tickers but keeps all positions at HOLD due to uncertain short‑term outlook.
- Liquidity spikes (ACCUMULATION_SPIKE) in ALCN.CA, BIOC.CA, EFIH.CA, FWRY.CA indicate short‑term buying interest, yet prices are near or above resistance, limiting upside in the next 1‑3 days.
- Sector leadership is narrow—only Fintech & Payments, Energy & Petrochemicals, and Education show strength; most tickers lie in non‑leading sectors, reducing conviction for sustained moves.
- Support/resistance distances show many stocks trading close to resistance (e.g., EFIH.CA +0.13%, FWRY.CA +3.56%) or with modest support gaps, suggesting limited room for upside before a pull‑back.
- The bearish EGX30/EGX70 regime forces a DEFENSIVE_NO_NEW_BUY risk mode, adding uncertainty that any bullish watch could reverse quickly.

## Top Liquidity Spikes
- MCQE.CA: spike=6.93 liquidity=146597552.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- HRHO.CA: spike=6.31 liquidity=481086048.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- OBRI.CA: spike=6.06 liquidity=58986888.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ARCC.CA: spike=6.04 liquidity=129072488.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BIOC.CA: spike=4.42 liquidity=330133920.0 outlook=BULLISH_WATCH score=78 buy_ready=False

## Sector Leaderboard
- #1 Fintech & Payments: score=9.65 5d=1.18% 20d=-0.61% aboveMA50=100.0%
- #2 Energy & Petrochemicals: score=8.21 5d=2.58% 20d=4.07% aboveMA50=66.67%
- #3 Education: score=7.19 5d=0.56% 20d=12.26% aboveMA50=66.67%
- #4 Automotive & Distribution: score=6.51 5d=1.46% 20d=0.21% aboveMA50=50.0%
- #5 Textiles: score=6.36 5d=2.17% 20d=1.25% aboveMA50=75.0%
- #6 Investment Holding: score=6.29 5d=-2.96% 20d=14.67% aboveMA50=66.67%
- #7 Building Materials: score=6.03 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Transportation & Logistics: score=5.18 5d=-0.48% 20d=-5.2% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- FWRY.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- EFIH.CA: BULLISH_WATCH score=94.65 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- AMOC.CA: BULLISH_WATCH score=93.21 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- GBCO.CA: BULLISH_WATCH score=87.51 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ORWE.CA: BULLISH_WATCH score=87.36 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- TALM.CA: BULLISH_WATCH score=83.19 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- ACGC.CA: BULLISH_WATCH score=82.36 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CIRA.CA: BULLISH_WATCH score=81.19 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- BIOC.CA: BULLISH_WATCH score=78 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=momentum is extended; far above support; sector is not leading
- KABO.CA: BULLISH_WATCH score=76.36 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=5.73 buy_ready=False sector_rank=16 price=261.99 support=230.11 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.94 liquidity=6793753.0 spike=0.29
- ABUK.CA: score=16.65 buy_ready=False sector_rank=17 price=88.75 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=43074096.0 spike=0.34
- ACAMD.CA: score=17.94 buy_ready=False sector_rank=16 price=2.06 support=1.87 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=45068404.0 spike=0.9
- ACGC.CA: score=18.58 buy_ready=False sector_rank=5 price=14.58 support=13.11 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=7181680.5 spike=0.27
- ADCI.CA: score=6.5 buy_ready=False sector_rank=16 price=274.1 support=256.0 resistance=298.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=2543890.25 spike=1.01
- ADIB.CA: score=15.35 buy_ready=False sector_rank=9 price=49.9 support=48.2 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=77273536.0 spike=1.01
- ADPC.CA: score=5.45 buy_ready=False sector_rank=16 price=3.67 support=3.4 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.74 liquidity=7511908.5 spike=0.43
- AFDI.CA: score=8.99 buy_ready=False sector_rank=16 price=52.06 support=47.7 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=5051175.0 spike=0.64
- AFMC.CA: score=17.94 buy_ready=False sector_rank=16 price=161.86 support=131.0 resistance=188.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=27493196.0 spike=0.52
- AJWA.CA: score=17.96 buy_ready=False sector_rank=16 price=182.01 support=175.15 resistance=188.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=14126028.0 spike=1.01
- ALCN.CA: score=28.07 buy_ready=False sector_rank=8 price=35.0 support=30.4 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.15 liquidity=114291512.0 spike=3.77
- ALUM.CA: score=4.1 buy_ready=False sector_rank=16 price=24.55 support=21.65 resistance=29.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.87 liquidity=5158783.0 spike=0.88
- AMER.CA: score=13.16 buy_ready=False sector_rank=19 price=4.6 support=4.05 resistance=5.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=31122238.0 spike=0.77
- AMES.CA: score=3.94 buy_ready=False sector_rank=16 price=50.07 support=46.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=193619664.0 spike=0.8
- AMIA.CA: score=19.1 buy_ready=False sector_rank=16 price=19.1 support=17.12 resistance=20.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=22414028.0 spike=1.08
- AMOC.CA: score=23.4 buy_ready=False sector_rank=2 price=13.9 support=12.18 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.56 liquidity=123924520.0 spike=0.91
- APSW.CA: score=3.99 buy_ready=False sector_rank=16 price=8.16 support=7.81 resistance=8.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=745481.69 spike=1.15
- ARAB.CA: score=15.48 buy_ready=False sector_rank=19 price=0.25 support=0.2 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.5 liquidity=82257088.0 spike=1.16
- ARCC.CA: score=11.4 buy_ready=False sector_rank=7 price=73.43 support=67.7 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=129072488.0 spike=6.04
- AREH.CA: score=7.94 buy_ready=False sector_rank=16 price=1.34 support=1.14 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=10829171.0 spike=0.84
- ASCM.CA: score=12.89 buy_ready=False sector_rank=16 price=59.34 support=53.8 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.05 liquidity=8954082.0 spike=0.57
- ASPI.CA: score=8.94 buy_ready=False sector_rank=16 price=0.38 support=0.33 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.73 liquidity=14455074.0 spike=0.29
- ATLC.CA: score=13.18 buy_ready=False sector_rank=13 price=6.43 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.67 liquidity=5745766.5 spike=0.34
- ATQA.CA: score=11.65 buy_ready=False sector_rank=17 price=11.73 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=57825052.0 spike=0.66
- AXPH.CA: score=5.42 buy_ready=False sector_rank=16 price=1535.4 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.21 liquidity=3481106.0 spike=0.51
- BINV.CA: score=18.71 buy_ready=False sector_rank=6 price=60.03 support=49.51 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=68.72 liquidity=7308729.5 spike=0.29
- BIOC.CA: score=27.94 buy_ready=False sector_rank=16 price=354.03 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.85 liquidity=330133920.0 spike=4.42
- BTFH.CA: score=13.44 buy_ready=False sector_rank=13 price=2.85 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=85005920.0 spike=0.92
- CAED.CA: score=13.94 buy_ready=False sector_rank=16 price=123.57 support=103.1 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.12 liquidity=10203185.0 spike=0.51
- CANA.CA: score=21.03 buy_ready=False sector_rank=9 price=46.2 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=31666460.0 spike=1.35
- CCAP.CA: score=21.4 buy_ready=False sector_rank=6 price=6.81 support=5.97 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.89 liquidity=632024448.0 spike=0.77
- CCRS.CA: score=9.92 buy_ready=False sector_rank=16 price=2.44 support=2.21 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=5978924.0 spike=0.36
- CEFM.CA: score=11.02 buy_ready=False sector_rank=16 price=142.2 support=113.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=4082257.75 spike=0.53
- CERA.CA: score=18.74 buy_ready=False sector_rank=16 price=1.45 support=1.18 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=267561456.0 spike=1.9
- CFGH.CA: score=-2.06 buy_ready=False sector_rank=16 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=10.0 liquidity=0.0 spike=0.0
- CICH.CA: score=11.74 buy_ready=False sector_rank=13 price=12.18 support=10.75 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.44 liquidity=2303007.75 spike=0.39
- CIEB.CA: score=13.06 buy_ready=False sector_rank=9 price=24.39 support=23.0 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.7 liquidity=7728758.0 spike=0.63
- CIRA.CA: score=22.4 buy_ready=False sector_rank=3 price=39.85 support=35.56 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=54.97 liquidity=19526124.0 spike=0.54
- CLHO.CA: score=16.55 buy_ready=False sector_rank=11 price=16.05 support=13.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=26637260.0 spike=0.52
- CNFN.CA: score=8.2 buy_ready=False sector_rank=13 price=4.27 support=3.84 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.4 liquidity=9760020.0 spike=1.0
- COMI.CA: score=9.33 buy_ready=False sector_rank=9 price=127.04 support=124.5 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=205310016.0 spike=0.37
- COPR.CA: score=19.52 buy_ready=False sector_rank=16 price=0.51 support=0.44 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.62 liquidity=37201560.0 spike=1.29
- COSG.CA: score=8.94 buy_ready=False sector_rank=16 price=1.65 support=1.46 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.12 liquidity=13989004.0 spike=0.67
- CPCI.CA: score=14.44 buy_ready=False sector_rank=16 price=606.25 support=530.0 resistance=600.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=87.11 liquidity=5496574.5 spike=1.5
- CSAG.CA: score=13.35 buy_ready=False sector_rank=8 price=37.92 support=34.52 resistance=42.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=7281188.5 spike=0.77
- DAPH.CA: score=9.06 buy_ready=False sector_rank=16 price=96.78 support=89.1 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=27460576.0 spike=1.06
- DEIN.CA: score=6.94 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=3.94 buy_ready=False sector_rank=18 price=25.53 support=23.81 resistance=29.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=5996300.0 spike=1.27
- DSCW.CA: score=8.36 buy_ready=False sector_rank=16 price=1.72 support=1.58 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.03 liquidity=26373604.0 spike=1.21
- DTPP.CA: score=11.94 buy_ready=False sector_rank=16 price=295.36 support=250.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.93 liquidity=24847596.0 spike=0.28
- EALR.CA: score=0.14 buy_ready=False sector_rank=16 price=343.21 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=2201512.5 spike=0.19
- EASB.CA: score=2.75 buy_ready=False sector_rank=16 price=7.65 support=7.25 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8809943.0 spike=0.61
- EAST.CA: score=7.4 buy_ready=False sector_rank=18 price=29.56 support=27.91 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.77 liquidity=36906252.0 spike=0.77
- EBSC.CA: score=1.46 buy_ready=False sector_rank=16 price=1.82 support=1.61 resistance=2.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=3524645.25 spike=0.75
- ECAP.CA: score=4.8 buy_ready=False sector_rank=16 price=30.79 support=29.13 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=5535674.0 spike=1.16
- EDFM.CA: score=7.11 buy_ready=False sector_rank=16 price=401.97 support=354.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.52 liquidity=2333137.25 spike=1.42
- EEII.CA: score=13.34 buy_ready=False sector_rank=16 price=2.18 support=2.02 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=13046024.0 spike=1.2
- EFIC.CA: score=7.65 buy_ready=False sector_rank=17 price=171.85 support=147.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.31 liquidity=24413740.0 spike=0.07
- EFID.CA: score=8.02 buy_ready=False sector_rank=18 price=19.37 support=18.1 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.33 liquidity=84944640.0 spike=1.31
- EFIH.CA: score=27.14 buy_ready=False sector_rank=1 price=23.97 support=20.2 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=116380192.0 spike=2.37
- EGAL.CA: score=16.37 buy_ready=False sector_rank=17 price=345.0 support=331.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.34 liquidity=156403696.0 spike=3.36
- EGAS.CA: score=17.16 buy_ready=False sector_rank=2 price=57.11 support=53.62 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=6762905.0 spike=0.56
- EGBE.CA: score=12.83 buy_ready=False sector_rank=9 price=0.53 support=0.49 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=214000.52 spike=2.14
- EGCH.CA: score=13.65 buy_ready=False sector_rank=17 price=13.65 support=12.88 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=41.92 liquidity=47309300.0 spike=0.43
- EGSA.CA: score=-0.78 buy_ready=False sector_rank=14 price=8.85 support=8.82 resistance=9.1 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=9.52 liquidity=79.65 spike=0.01
- EGTS.CA: score=13.62 buy_ready=False sector_rank=19 price=16.52 support=15.65 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.79 liquidity=43398852.0 spike=1.23
- EHDR.CA: score=7.85 buy_ready=False sector_rank=16 price=2.58 support=2.35 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.94 liquidity=8907565.0 spike=0.57
- ELEC.CA: score=13.17 buy_ready=False sector_rank=15 price=1.92 support=1.72 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=29626994.0 spike=0.43
- ELKA.CA: score=13.94 buy_ready=False sector_rank=16 price=1.65 support=1.43 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.56 liquidity=12413033.0 spike=0.8
- ELNA.CA: score=0.08 buy_ready=False sector_rank=16 price=35.22 support=33.46 resistance=38.99 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=140774.34 spike=0.45
- ELSH.CA: score=9.74 buy_ready=False sector_rank=16 price=12.1 support=10.8 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=36689232.0 spike=1.4
- ELWA.CA: score=-1.61 buy_ready=False sector_rank=16 price=1.48 support=1.43 resistance=1.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=5.41 liquidity=451346.25 spike=0.47
- EMFD.CA: score=11.16 buy_ready=False sector_rank=19 price=12.8 support=11.7 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=45688188.0 spike=0.47
- ENGC.CA: score=8.94 buy_ready=False sector_rank=16 price=37.51 support=33.33 resistance=46.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.88 liquidity=16076022.0 spike=0.93
- EOSB.CA: score=8.94 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=301.44 spike=0.01
- EPCO.CA: score=2.23 buy_ready=False sector_rank=16 price=10.17 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.15 liquidity=3294286.75 spike=0.23
- EPPK.CA: score=-5.64 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=5.14 buy_ready=False sector_rank=14 price=149.08 support=139.1 resistance=154.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=440575968.0 spike=1.46
- ETRS.CA: score=19.01 buy_ready=False sector_rank=16 price=10.95 support=9.82 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=9894754.0 spike=1.09
- EXPA.CA: score=20.33 buy_ready=False sector_rank=9 price=21.45 support=20.4 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=27101836.0 spike=0.8
- FAIT.CA: score=11.38 buy_ready=False sector_rank=9 price=45.0 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=40.51 liquidity=3049996.5 spike=0.6
- FAITA.CA: score=6.54 buy_ready=False sector_rank=9 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=51429.94 spike=1.58
- FERC.CA: score=4.63 buy_ready=False sector_rank=17 price=77.03 support=70.42 resistance=82.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=41.65 liquidity=1979509.75 spike=0.23
- FWRY.CA: score=26.46 buy_ready=False sector_rank=1 price=19.1 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.17 liquidity=196670816.0 spike=2.03
- GBCO.CA: score=23.8 buy_ready=False sector_rank=4 price=32.37 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=54.16 liquidity=191489504.0 spike=2.2
- GDWA.CA: score=7.94 buy_ready=False sector_rank=16 price=0.68 support=0.61 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.88 liquidity=16757626.0 spike=0.5
- GGCC.CA: score=5.02 buy_ready=False sector_rank=16 price=0.73 support=0.7 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23801636.0 spike=1.54
- GIHD.CA: score=8.94 buy_ready=False sector_rank=16 price=65.54 support=60.9 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.8 liquidity=16292513.0 spike=0.59
- GMCI.CA: score=-1.74 buy_ready=False sector_rank=16 price=1.62 support=1.49 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=20.83 liquidity=319001.38 spike=0.68
- GRCA.CA: score=7.94 buy_ready=False sector_rank=16 price=38.26 support=32.11 resistance=63.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=27.89 liquidity=11461672.0 spike=0.4
- GSSC.CA: score=4.58 buy_ready=False sector_rank=16 price=279.47 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.04 liquidity=635610.63 spike=0.12
- GTWL.CA: score=8.94 buy_ready=False sector_rank=16 price=175.12 support=124.5 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=148841312.0 spike=0.94
- HDBK.CA: score=18.33 buy_ready=False sector_rank=9 price=111.95 support=102.03 resistance=123.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.26 liquidity=16102696.0 spike=0.41
- HELI.CA: score=13.16 buy_ready=False sector_rank=19 price=7.48 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.51 liquidity=40825264.0 spike=0.3
- HRHO.CA: score=9.44 buy_ready=False sector_rank=13 price=26.0 support=24.21 resistance=26.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=481086048.0 spike=6.31
- ICID.CA: score=13.29 buy_ready=False sector_rank=16 price=18.29 support=16.52 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.24 liquidity=4354793.0 spike=0.57
- IDRE.CA: score=11.0 buy_ready=False sector_rank=16 price=50.92 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.37 liquidity=7062215.5 spike=0.46
- IFAP.CA: score=3.08 buy_ready=False sector_rank=12 price=19.8 support=17.17 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.32 liquidity=3618661.25 spike=0.24
- INFI.CA: score=8.76 buy_ready=False sector_rank=16 price=125.64 support=104.0 resistance=152.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.58 liquidity=9824606.0 spike=0.7
- IRON.CA: score=13.61 buy_ready=False sector_rank=17 price=27.87 support=25.01 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=40.72 liquidity=8957550.0 spike=0.69
- ISMA.CA: score=2.41 buy_ready=False sector_rank=16 price=26.7 support=25.4 resistance=26.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8473158.0 spike=0.59
- ISMQ.CA: score=10.13 buy_ready=False sector_rank=17 price=8.43 support=7.6 resistance=9.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.08 liquidity=35868908.0 spike=1.74
- ISPH.CA: score=9.57 buy_ready=False sector_rank=11 price=12.05 support=11.22 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.35 liquidity=72954784.0 spike=1.01
- JUFO.CA: score=7.94 buy_ready=False sector_rank=18 price=25.51 support=24.4 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.91 liquidity=23767380.0 spike=1.27
- KABO.CA: score=21.4 buy_ready=False sector_rank=5 price=9.21 support=7.97 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=40.05 liquidity=12290756.0 spike=0.36
- KWIN.CA: score=9.9 buy_ready=False sector_rank=16 price=81.25 support=72.21 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=35.38 liquidity=5957455.0 spike=0.39
- KZPC.CA: score=11.59 buy_ready=False sector_rank=16 price=13.02 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.47 liquidity=4647553.5 spike=0.17
- LCSW.CA: score=18.4 buy_ready=False sector_rank=7 price=33.44 support=28.86 resistance=36.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=14114452.0 spike=0.84
- LUTS.CA: score=18.94 buy_ready=False sector_rank=16 price=0.95 support=0.72 resistance=1.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=48.2 liquidity=50983924.0 spike=0.51
- MAAL.CA: score=18.96 buy_ready=False sector_rank=16 price=10.78 support=8.18 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=22073644.0 spike=1.01
- MASR.CA: score=13.94 buy_ready=False sector_rank=16 price=7.77 support=6.82 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=39830720.0 spike=0.43
- MBSC.CA: score=11.4 buy_ready=False sector_rank=7 price=356.64 support=306.98 resistance=356.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=159536768.0 spike=4.07
- MCQE.CA: score=11.4 buy_ready=False sector_rank=7 price=219.45 support=195.02 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=146597552.0 spike=6.93
- MCRO.CA: score=16.94 buy_ready=False sector_rank=16 price=1.58 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.35 liquidity=86775752.0 spike=0.71
- MENA.CA: score=-0.39 buy_ready=False sector_rank=19 price=6.36 support=5.8 resistance=6.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=32.23 liquidity=1274281.25 spike=1.09
- MEPA.CA: score=8.72 buy_ready=False sector_rank=16 price=1.78 support=1.56 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=9781687.0 spike=0.27
- MFPC.CA: score=16.65 buy_ready=False sector_rank=17 price=47.11 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.2 liquidity=41243560.0 spike=0.33
- MFSC.CA: score=5.06 buy_ready=False sector_rank=16 price=46.58 support=42.5 resistance=51.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.58 liquidity=1123193.88 spike=0.36
- MHOT.CA: score=11.85 buy_ready=False sector_rank=20 price=17.71 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.93 liquidity=15813964.0 spike=0.87
- MICH.CA: score=9.91 buy_ready=False sector_rank=16 price=47.19 support=42.01 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=5965256.5 spike=0.54
- MILS.CA: score=8.94 buy_ready=False sector_rank=16 price=184.86 support=165.5 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.44 liquidity=13044301.0 spike=0.71
- MIPH.CA: score=9.15 buy_ready=False sector_rank=11 price=818.78 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=51.24 liquidity=1595745.13 spike=0.17
- MOED.CA: score=7.94 buy_ready=False sector_rank=16 price=0.7 support=0.59 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.19 liquidity=16187925.0 spike=0.37
- MOIL.CA: score=10.79 buy_ready=False sector_rank=2 price=0.7 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=267077.66 spike=1.06
- MOIN.CA: score=12.25 buy_ready=False sector_rank=16 price=35.0 support=32.0 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=5309592.5 spike=0.21
- MOSC.CA: score=1.95 buy_ready=False sector_rank=16 price=287.45 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.93 liquidity=3011534.75 spike=0.82
- MPCI.CA: score=4.8 buy_ready=False sector_rank=16 price=364.09 support=350.02 resistance=369.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=154870064.0 spike=1.43
- MPCO.CA: score=17.46 buy_ready=False sector_rank=12 price=2.53 support=2.17 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.1 liquidity=110322000.0 spike=0.57
- MPRC.CA: score=17.94 buy_ready=False sector_rank=16 price=40.9 support=37.65 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.54 liquidity=19240768.0 spike=0.74
- MTIE.CA: score=16.68 buy_ready=False sector_rank=4 price=8.14 support=7.5 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=43.62 liquidity=31419882.0 spike=1.64
- NAHO.CA: score=3.95 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=11353.73 spike=0.26
- NCCW.CA: score=18.94 buy_ready=False sector_rank=16 price=7.45 support=6.06 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.48 liquidity=36877512.0 spike=0.48
- NEDA.CA: score=4.13 buy_ready=False sector_rank=16 price=2.61 support=2.48 resistance=2.89 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=35.71 liquidity=187640.72 spike=0.2
- NHPS.CA: score=4.4 buy_ready=False sector_rank=16 price=75.65 support=72.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17993650.0 spike=1.23
- NINH.CA: score=10.3 buy_ready=False sector_rank=16 price=19.67 support=18.53 resistance=24.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.11 liquidity=24635606.0 spike=1.68
- NIPH.CA: score=20.17 buy_ready=False sector_rank=11 price=331.08 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.32 liquidity=160801824.0 spike=1.31
- OBRI.CA: score=8.94 buy_ready=False sector_rank=16 price=29.64 support=25.8 resistance=30.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58986888.0 spike=6.06
- OCDI.CA: score=8.16 buy_ready=False sector_rank=19 price=27.26 support=24.2 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=24.59 liquidity=34156304.0 spike=0.66
- OCPH.CA: score=2.07 buy_ready=False sector_rank=16 price=234.95 support=190.0 resistance=263.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=33.98 liquidity=4125008.75 spike=0.86
- ODIN.CA: score=12.38 buy_ready=False sector_rank=16 price=2.65 support=2.35 resistance=3.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.22 liquidity=8437072.0 spike=0.77
- OFH.CA: score=13.94 buy_ready=False sector_rank=16 price=0.92 support=0.83 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.07 liquidity=44636912.0 spike=0.33
- OIH.CA: score=11.4 buy_ready=False sector_rank=6 price=1.87 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.64 liquidity=39555728.0 spike=0.36
- OLFI.CA: score=14.08 buy_ready=False sector_rank=18 price=21.6 support=21.2 resistance=23.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.39 liquidity=28043398.0 spike=1.84
- ORAS.CA: score=4.6 buy_ready=False sector_rank=10 price=830.0 support=822.0 resistance=845.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=159873280.0 spike=1.0
- ORHD.CA: score=8.16 buy_ready=False sector_rank=19 price=39.31 support=37.41 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.89 liquidity=130294656.0 spike=0.8
- ORWE.CA: score=21.78 buy_ready=False sector_rank=5 price=27.8 support=26.01 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=64270232.0 spike=1.19
- PHAR.CA: score=14.55 buy_ready=False sector_rank=11 price=117.49 support=102.0 resistance=132.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=71269016.0 spike=0.87
- PHDC.CA: score=8.84 buy_ready=False sector_rank=19 price=13.19 support=12.36 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.17 liquidity=158488752.0 spike=1.34
- PHTV.CA: score=4.77 buy_ready=False sector_rank=16 price=336.55 support=315.1 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=829592.25 spike=0.53
- POUL.CA: score=8.04 buy_ready=False sector_rank=18 price=10.13 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.78 liquidity=43460248.0 spike=1.32
- PRCL.CA: score=11.4 buy_ready=False sector_rank=7 price=26.76 support=22.8 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.6 liquidity=10774056.0 spike=0.69
- PRDC.CA: score=3.16 buy_ready=False sector_rank=19 price=8.11 support=7.32 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27032160.0 spike=0.92
- PRMH.CA: score=3.26 buy_ready=False sector_rank=16 price=2.32 support=2.03 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=4317620.5 spike=0.94
- RACC.CA: score=14.48 buy_ready=False sector_rank=16 price=9.39 support=8.51 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=14829380.0 spike=1.27
- RAKT.CA: score=1.1 buy_ready=False sector_rank=16 price=21.69 support=20.26 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=27.32 liquidity=423521.47 spike=2.37
- RAYA.CA: score=12.84 buy_ready=False sector_rank=21 price=6.8 support=5.72 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.07 liquidity=29243736.0 spike=0.62
- RMDA.CA: score=9.55 buy_ready=False sector_rank=11 price=5.56 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.33 liquidity=22304466.0 spike=0.41
- ROTO.CA: score=11.0 buy_ready=False sector_rank=16 price=39.66 support=35.02 resistance=44.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.37 liquidity=7063563.0 spike=0.9
- RREI.CA: score=5.15 buy_ready=False sector_rank=16 price=3.98 support=3.53 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.61 liquidity=6206101.5 spike=0.51
- RTVC.CA: score=2.45 buy_ready=False sector_rank=16 price=3.62 support=3.37 resistance=4.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=3631438.25 spike=1.44
- RUBX.CA: score=18.94 buy_ready=False sector_rank=16 price=15.74 support=12.59 resistance=18.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.37 liquidity=47861672.0 spike=0.67
- SAUD.CA: score=20.33 buy_ready=False sector_rank=9 price=23.91 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.95 liquidity=14261275.0 spike=0.73
- SCEM.CA: score=11.0 buy_ready=False sector_rank=7 price=88.66 support=81.67 resistance=89.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=209007056.0 spike=3.3
- SCFM.CA: score=-0.93 buy_ready=False sector_rank=16 price=251.3 support=223.11 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.6 liquidity=1125838.5 spike=0.19
- SCTS.CA: score=3.08 buy_ready=False sector_rank=3 price=556.96 support=520.3 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=23.45 liquidity=680530.63 spike=0.34
- SDTI.CA: score=15.94 buy_ready=False sector_rank=16 price=83.49 support=70.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=79.77 liquidity=18251960.0 spike=0.54
- SEIG.CA: score=5.26 buy_ready=False sector_rank=16 price=237.21 support=200.0 resistance=267.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=39.57 liquidity=1318298.13 spike=0.77
- SIPC.CA: score=11.94 buy_ready=False sector_rank=16 price=5.24 support=4.22 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=20218224.0 spike=0.29
- SKPC.CA: score=7.65 buy_ready=False sector_rank=17 price=16.25 support=15.4 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=27.56 liquidity=62610168.0 spike=0.6
- SMFR.CA: score=1.4 buy_ready=False sector_rank=16 price=229.86 support=205.01 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.66 liquidity=2462150.0 spike=0.38
- SNFC.CA: score=16.73 buy_ready=False sector_rank=16 price=11.59 support=10.58 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.09 liquidity=5785964.5 spike=0.43
- SPIN.CA: score=6.01 buy_ready=False sector_rank=5 price=17.0 support=15.11 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.87 liquidity=4605469.0 spike=0.63
- SPMD.CA: score=12.94 buy_ready=False sector_rank=16 price=0.39 support=0.36 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.5 liquidity=10253476.0 spike=0.13
- SUGR.CA: score=11.4 buy_ready=False sector_rank=18 price=55.03 support=50.5 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=23.29 liquidity=10867890.0 spike=0.49
- SVCE.CA: score=6.14 buy_ready=False sector_rank=16 price=10.8 support=10.41 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=259934592.0 spike=2.1
- SWDY.CA: score=17.17 buy_ready=False sector_rank=15 price=120.09 support=102.31 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.84 liquidity=71839536.0 spike=0.97
- TALM.CA: score=22.4 buy_ready=False sector_rank=3 price=21.27 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=59.94 liquidity=18053124.0 spike=0.27
- TMGH.CA: score=7.16 buy_ready=False sector_rank=19 price=88.61 support=84.4 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=13.53 liquidity=270229696.0 spike=0.99
- TRTO.CA: score=-1.06 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4842.83 spike=0.28
- UEFM.CA: score=9.58 buy_ready=False sector_rank=16 price=511.46 support=407.57 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:06 PM market time freshness=DELAYED_CURRENT RSI=45.7 liquidity=1636348.0 spike=0.4
- UEGC.CA: score=14.18 buy_ready=False sector_rank=16 price=1.62 support=1.37 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=39463760.0 spike=1.12
- UNIP.CA: score=13.94 buy_ready=False sector_rank=16 price=0.36 support=0.32 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.21 liquidity=13713195.0 spike=0.68
- UNIT.CA: score=4.81 buy_ready=False sector_rank=19 price=17.72 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=46.37 liquidity=1646234.38 spike=0.11
- WCDF.CA: score=8.66 buy_ready=False sector_rank=16 price=657.29 support=575.5 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:05 PM market time freshness=DELAYED_CURRENT RSI=37.38 liquidity=1716691.75 spike=0.32
- WKOL.CA: score=3.19 buy_ready=False sector_rank=16 price=298.0 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=25.4 liquidity=5248034.0 spike=0.39
- ZEOT.CA: score=12.4 buy_ready=False sector_rank=16 price=12.99 support=10.6 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.84 liquidity=7698285.0 spike=1.38
- ZMID.CA: score=8.16 buy_ready=False sector_rank=19 price=7.7 support=7.07 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=17.08 liquidity=46711932.0 spike=0.34

## Backtesting Lite
- ALCN.CA: 180d return=61.78%, max drawdown=-15.82%, MA20>MA50 days last20=20, as_of=2026-09-30T21:00:00+00:00
- BIOC.CA: 180d return=483.91%, max drawdown=-55.36%, MA20>MA50 days last20=12, as_of=2026-09-30T21:00:00+00:00
- EFIH.CA: 180d return=18.92%, max drawdown=-22.68%, MA20>MA50 days last20=13, as_of=2026-09-30T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- BIOC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GlaxoSmithKline S.A.E summary=Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- EFIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=E-Finance For Digital and Financial Investments summary=Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- FWRY.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Fawry For Banking Technology and Electronic Payments summary=Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/

## Warnings
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for BIOC.CA: source text did not clearly match BIOC.CA / GlaxoSmithKline S.A.E.
- Evidence rejected for EFIH.CA: source text did not clearly match EFIH.CA / E-Finance For Digital and Financial Investments.
- Evidence rejected for FWRY.CA: source text did not clearly match FWRY.CA / Fawry For Banking Technology and Electronic Payments.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
