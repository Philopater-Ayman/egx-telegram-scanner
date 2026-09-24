# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-09-24T11:43:14.631365+00:00
Generated Cairo: 2026-09-24 14:43
Run timing: target 09:15 Cairo | generated Cairo 2026-09-24 14:43 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-09-24 14:39

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 176/187
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, September 24
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.79% / above MA50 36.84%
- EGX70 regime: BEARISH / above MA20 23.68% / above MA50 26.32%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=949659584.0 spike=1.14 score=20.68
- COMI.CA: liquidity=502607488.0 spike=0.8 score=10.39
- OFH.CA: liquidity=420152768.0 spike=3.06 score=8.12
- RUBX.CA: liquidity=298542816.0 spike=6.51 score=26.0
- OIH.CA: liquidity=246648480.0 spike=2.03 score=22.46

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak breadth (23.8% sector breadth); risk mode is defensive, so the scanner flags accumulation‑spike stocks in leading sectors but keeps them on hold.
- MHOT.CA (Tourism & Leisure) shows a liquidity spike (2.3×) and price near resistance (3.2% away) with a bullish‑watch outlook, but the bearish market regime prevents a new buy.
- MAAL.CA and RUBX.CA exhibit high liquidity spikes yet sit far above support and belong to non‑leading sectors, leaving their outlook neutral/bullish watch with notable uncertainty.
- ALCN.CA and EGTS.CA have tradeable liquidity and modest support distances, but sector breadth is weak and some RSIs approach overbought, suggesting caution despite bullish‑watch scores.
- Overall EGX30/EGX70 stay below their MA20 and MA50, keeping risk mode defensive; therefore no new buys are advised even though individual tickets show accumulation signals.

## Top Liquidity Spikes
- EGBE.CA: spike=9.03 liquidity=668112.44 outlook=WEAK_OR_RISKY score=32.48 buy_ready=False
- RUBX.CA: spike=6.51 liquidity=298542816.0 outlook=NEUTRAL score=46 buy_ready=False
- MAAL.CA: spike=5.88 liquidity=85565800.0 outlook=BULLISH_WATCH score=80 buy_ready=False
- GIHD.CA: spike=3.55 liquidity=93892424.0 outlook=BULLISH_WATCH score=72 buy_ready=False
- OFH.CA: spike=3.06 liquidity=420152768.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=12.4 5d=6.04% 20d=2.68% aboveMA50=100.0%
- #2 Investment Holding: score=10.95 5d=0.46% 20d=15.28% aboveMA50=100.0%
- #3 Telecommunications: score=9.78 5d=2.58% 20d=11.29% aboveMA50=100.0%
- #4 Transportation & Logistics: score=7.37 5d=6.74% 20d=3.81% aboveMA50=50.0%
- #5 Education: score=6.6 5d=-3.49% 20d=16.36% aboveMA50=66.67%
- #6 Energy & Petrochemicals: score=6.11 5d=-0.37% 20d=5.88% aboveMA50=66.67%
- #7 Agriculture & Food Production: score=4.35 5d=-2.22% 20d=7.08% aboveMA50=50.0%
- #8 Banking & Financials: score=3.48 5d=-0.1% 20d=-0.42% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MHOT.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- OIH.CA: BULLISH_WATCH score=93 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- ALCN.CA: BULLISH_WATCH score=90.37 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- BINV.CA: BULLISH_WATCH score=87 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- MAAL.CA: BULLISH_WATCH score=80 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=far above support; sector is not leading
- EGTS.CA: BULLISH_WATCH score=80 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=momentum is extended; sector is not leading
- DTPP.CA: BULLISH_WATCH score=76 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- AMOC.CA: BULLISH_WATCH score=72.11 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- GIHD.CA: BULLISH_WATCH score=72 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=far above support; sector is not leading
- KZPC.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=14.0 buy_ready=False sector_rank=16 price=285.07 support=288.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=42.77 liquidity=14387184.0 spike=0.59
- ABUK.CA: score=20.26 buy_ready=False sector_rank=9 price=90.7 support=75.76 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=50.99 liquidity=84928528.0 spike=0.45
- ACAMD.CA: score=13.98 buy_ready=False sector_rank=16 price=1.94 support=1.98 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=73795912.0 spike=1.49
- ACGC.CA: score=17.82 buy_ready=False sector_rank=12 price=14.28 support=13.65 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=21982324.0 spike=0.82
- ADCI.CA: score=5.71 buy_ready=False sector_rank=16 price=280.66 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=1717491.75 spike=0.37
- ADIB.CA: score=15.91 buy_ready=False sector_rank=8 price=51.46 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.69 liquidity=101770352.0 spike=1.26
- ADPC.CA: score=16.96 buy_ready=False sector_rank=16 price=3.79 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=26821106.0 spike=1.48
- AFDI.CA: score=10.21 buy_ready=False sector_rank=16 price=52.03 support=51.6 resistance=61.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.11 liquidity=6213233.0 spike=0.32
- AFMC.CA: score=14.0 buy_ready=False sector_rank=16 price=153.12 support=153.0 resistance=221.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.5 liquidity=10727174.0 spike=0.19
- AJWA.CA: score=16.0 buy_ready=False sector_rank=16 price=181.2 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=34700880.0 spike=0.8
- ALCN.CA: score=25.4 buy_ready=False sector_rank=4 price=33.5 support=30.05 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=33103032.0 spike=0.9
- ALUM.CA: score=6.17 buy_ready=False sector_rank=16 price=24.01 support=24.44 resistance=30.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=27.76 liquidity=7177980.0 spike=0.84
- AMER.CA: score=13.45 buy_ready=False sector_rank=20 price=5.02 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.18 liquidity=33657472.0 spike=0.61
- AMES.CA: score=8.0 buy_ready=False sector_rank=16 price=48.98 support=48.45 resistance=150.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=12.0 liquidity=44336072.0 spike=0.16
- AMIA.CA: score=14.0 buy_ready=False sector_rank=16 price=18.83 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.61 liquidity=10706276.0 spike=0.29
- AMOC.CA: score=21.4 buy_ready=False sector_rank=6 price=13.31 support=10.91 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=97293304.0 spike=0.57
- APSW.CA: score=3.51 buy_ready=False sector_rank=16 price=8.19 support=8.2 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.86 liquidity=513617.75 spike=0.59
- ARAB.CA: score=8.45 buy_ready=False sector_rank=20 price=0.23 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=72428448.0 spike=0.75
- ARCC.CA: score=7.4 buy_ready=False sector_rank=21 price=66.57 support=68.05 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.44 liquidity=23800448.0 spike=0.77
- AREH.CA: score=9.37 buy_ready=False sector_rank=16 price=1.37 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=37.04 liquidity=5377051.5 spike=0.39
- ASCM.CA: score=9.18 buy_ready=False sector_rank=16 price=57.79 support=57.36 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.89 liquidity=19983478.0 spike=1.09
- ASPI.CA: score=14.0 buy_ready=False sector_rank=16 price=0.39 support=0.41 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.51 liquidity=41557492.0 spike=0.65
- ATLC.CA: score=3.91 buy_ready=False sector_rank=18 price=6.46 support=6.18 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10972340.0 spike=0.38
- ATQA.CA: score=18.26 buy_ready=False sector_rank=9 price=12.54 support=11.56 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=59.89 liquidity=50140028.0 spike=0.46
- AXPH.CA: score=17.78 buy_ready=False sector_rank=16 price=1656.46 support=1620.0 resistance=1750.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=45.73 liquidity=12820388.0 spike=1.39
- BINV.CA: score=23.68 buy_ready=False sector_rank=2 price=56.95 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=67.33 liquidity=28675438.0 spike=1.14
- BIOC.CA: score=9.0 buy_ready=False sector_rank=16 price=255.66 support=247.03 resistance=453.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=18.56 liquidity=15960487.0 spike=0.17
- BTFH.CA: score=9.03 buy_ready=False sector_rank=18 price=2.84 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.04 liquidity=128441312.0 spike=1.56
- CAED.CA: score=5.96 buy_ready=False sector_rank=16 price=116.76 support=117.0 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.16 liquidity=6961098.0 spike=0.33
- CANA.CA: score=22.39 buy_ready=False sector_rank=8 price=47.49 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.41 liquidity=10907033.0 spike=0.47
- CCAP.CA: score=20.68 buy_ready=False sector_rank=2 price=7.09 support=5.74 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=75.96 liquidity=949659584.0 spike=1.14
- CCRS.CA: score=12.65 buy_ready=False sector_rank=16 price=2.53 support=2.4 resistance=2.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.75 liquidity=8653178.0 spike=0.28
- CEFM.CA: score=9.09 buy_ready=False sector_rank=16 price=139.21 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.9 liquidity=2092578.63 spike=0.23
- CERA.CA: score=14.28 buy_ready=False sector_rank=16 price=1.3 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=149104048.0 spike=1.14
- CFGH.CA: score=2.0 buy_ready=False sector_rank=16 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=21.43 liquidity=5336.81 spike=0.32
- CICH.CA: score=7.39 buy_ready=False sector_rank=18 price=11.9 support=11.51 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=63.43 liquidity=1482579.63 spike=0.24
- CIEB.CA: score=15.83 buy_ready=False sector_rank=8 price=24.07 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=16881902.0 spike=1.22
- CIRA.CA: score=21.4 buy_ready=False sector_rank=5 price=39.07 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=68.01 liquidity=20349314.0 spike=0.51
- CLHO.CA: score=8.73 buy_ready=False sector_rank=19 price=15.5 support=15.4 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=15.07 liquidity=30764372.0 spike=0.45
- CNFN.CA: score=6.4 buy_ready=False sector_rank=18 price=4.31 support=4.32 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.89 liquidity=8495693.0 spike=0.76
- COMI.CA: score=10.39 buy_ready=False sector_rank=8 price=128.58 support=128.1 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.88 liquidity=502607488.0 spike=0.8
- COPR.CA: score=17.0 buy_ready=False sector_rank=16 price=0.48 support=0.46 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=20945662.0 spike=0.53
- COSG.CA: score=9.0 buy_ready=False sector_rank=16 price=1.66 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.95 liquidity=21054666.0 spike=0.71
- CPCI.CA: score=12.43 buy_ready=False sector_rank=16 price=561.41 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=69.3 liquidity=3337286.75 spike=1.05
- CSAG.CA: score=6.25 buy_ready=False sector_rank=4 price=37.53 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.39 liquidity=4854401.5 spike=0.32
- DAPH.CA: score=4.0 buy_ready=False sector_rank=16 price=103.35 support=101.55 resistance=110.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33241150.0 spike=0.57
- DEIN.CA: score=7.0 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=1.24 buy_ready=False sector_rank=15 price=25.64 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=29.15 liquidity=3165989.0 spike=0.59
- DSCW.CA: score=8.0 buy_ready=False sector_rank=16 price=1.74 support=1.77 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=18.52 liquidity=21734136.0 spike=0.94
- DTPP.CA: score=19.0 buy_ready=False sector_rank=16 price=325.43 support=296.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=56.97 liquidity=66309332.0 spike=0.8
- EALR.CA: score=-1.1 buy_ready=False sector_rank=16 price=342.17 support=340.0 resistance=367.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4900353.5 spike=0.36
- EASB.CA: score=8.22 buy_ready=False sector_rank=16 price=7.49 support=7.13 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=4228039.5 spike=0.26
- EAST.CA: score=8.08 buy_ready=False sector_rank=15 price=31.13 support=31.31 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=6.67 liquidity=41342896.0 spike=0.68
- EBSC.CA: score=6.13 buy_ready=False sector_rank=16 price=1.94 support=1.95 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.03 liquidity=2133631.0 spike=0.18
- ECAP.CA: score=4.84 buy_ready=False sector_rank=16 price=31.25 support=31.16 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=29.46 liquidity=5844375.5 spike=0.63
- EDFM.CA: score=-0.47 buy_ready=False sector_rank=16 price=387.66 support=389.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.27 liquidity=534348.13 spike=0.3
- EEII.CA: score=16.16 buy_ready=False sector_rank=16 price=2.33 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=15770821.0 spike=1.08
- EFIC.CA: score=14.26 buy_ready=False sector_rank=9 price=175.01 support=183.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.01 liquidity=39684884.0 spike=0.11
- EFID.CA: score=14.08 buy_ready=False sector_rank=15 price=29.43 support=29.71 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=57716936.0 spike=0.86
- EFIH.CA: score=14.52 buy_ready=False sector_rank=14 price=22.87 support=22.16 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.16 liquidity=55270480.0 spike=0.94
- EGAL.CA: score=18.26 buy_ready=False sector_rank=9 price=355.82 support=351.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=51083136.0 spike=0.6
- EGAS.CA: score=10.03 buy_ready=False sector_rank=6 price=55.01 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.13 liquidity=8633255.0 spike=0.72
- EGBE.CA: score=14.06 buy_ready=False sector_rank=8 price=0.52 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:50 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=668112.44 spike=9.03
- EGCH.CA: score=16.0 buy_ready=False sector_rank=9 price=14.13 support=13.51 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=169004304.0 spike=1.37
- EGSA.CA: score=12.4 buy_ready=False sector_rank=3 price=9.0 support=8.69 resistance=9.1 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=36.84 liquidity=1044.0 spike=0.16
- EGTS.CA: score=24.21 buy_ready=False sector_rank=20 price=18.1 support=16.51 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.9 liquidity=88244032.0 spike=2.88
- EHDR.CA: score=9.2 buy_ready=False sector_rank=16 price=2.56 support=2.6 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.41 liquidity=18508200.0 spike=1.1
- ELEC.CA: score=9.23 buy_ready=False sector_rank=11 price=1.93 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=55888884.0 spike=0.72
- ELKA.CA: score=9.0 buy_ready=False sector_rank=16 price=1.58 support=1.64 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=15.62 liquidity=20481830.0 spike=0.58
- ELNA.CA: score=-1.96 buy_ready=False sector_rank=16 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=25.47 liquidity=42052.68 spike=0.11
- ELSH.CA: score=9.0 buy_ready=False sector_rank=16 price=12.26 support=12.06 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.18 liquidity=16071730.0 spike=0.44
- ELWA.CA: score=-1.3 buy_ready=False sector_rank=16 price=1.62 support=1.64 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.14 liquidity=707691.62 spike=0.4
- EMFD.CA: score=16.45 buy_ready=False sector_rank=20 price=13.2 support=12.17 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=35.57 liquidity=64424240.0 spike=0.41
- ENGC.CA: score=14.0 buy_ready=False sector_rank=16 price=40.37 support=41.0 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=16221312.0 spike=0.92
- EOSB.CA: score=9.0 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=83.21 spike=0.0
- EPCO.CA: score=8.22 buy_ready=False sector_rank=16 price=10.46 support=10.6 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.35 liquidity=4223953.0 spike=0.28
- EPPK.CA: score=-5.58 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=21.4 buy_ready=False sector_rank=3 price=134.5 support=112.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=86.89 liquidity=139725632.0 spike=0.49
- ETRS.CA: score=7.55 buy_ready=False sector_rank=16 price=10.48 support=10.6 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.78 liquidity=8550980.0 spike=0.67
- EXPA.CA: score=22.39 buy_ready=False sector_rank=8 price=21.62 support=19.96 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=53.15 liquidity=25310728.0 spike=0.71
- FAIT.CA: score=14.92 buy_ready=False sector_rank=8 price=46.31 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=4525781.0 spike=0.56
- FAITA.CA: score=5.43 buy_ready=False sector_rank=8 price=0.99 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.84 liquidity=37724.81 spike=0.8
- FERC.CA: score=8.76 buy_ready=False sector_rank=9 price=76.88 support=77.3 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.89 liquidity=4499134.5 spike=0.32
- FWRY.CA: score=14.6 buy_ready=False sector_rank=14 price=18.8 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.09 liquidity=134370480.0 spike=1.04
- GBCO.CA: score=19.26 buy_ready=False sector_rank=10 price=30.41 support=28.04 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=62.85 liquidity=72089632.0 spike=1.0
- GDWA.CA: score=8.0 buy_ready=False sector_rank=16 price=0.71 support=0.74 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=12.8 liquidity=37205352.0 spike=0.86
- GGCC.CA: score=9.0 buy_ready=False sector_rank=16 price=0.76 support=0.78 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.49 liquidity=11978958.0 spike=0.36
- GIHD.CA: score=24.0 buy_ready=False sector_rank=16 price=76.49 support=63.1 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=93892424.0 spike=3.55
- GMCI.CA: score=-1.69 buy_ready=False sector_rank=16 price=1.7 support=1.69 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=310501.81 spike=0.63
- GRCA.CA: score=5.7 buy_ready=False sector_rank=16 price=39.22 support=38.7 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=17.32 liquidity=7699609.5 spike=0.17
- GSSC.CA: score=9.54 buy_ready=False sector_rank=16 price=290.91 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=48.13 liquidity=2539749.5 spike=0.3
- GTWL.CA: score=17.0 buy_ready=False sector_rank=16 price=224.99 support=210.0 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.33 liquidity=113959336.0 spike=0.7
- HDBK.CA: score=17.39 buy_ready=False sector_rank=8 price=107.22 support=95.51 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=41.13 liquidity=32648966.0 spike=0.54
- HELI.CA: score=13.45 buy_ready=False sector_rank=20 price=7.85 support=7.64 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=43.56 liquidity=74260200.0 spike=0.43
- HRHO.CA: score=7.91 buy_ready=False sector_rank=18 price=24.23 support=24.4 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=23.05 liquidity=68765648.0 spike=0.7
- ICID.CA: score=0.26 buy_ready=False sector_rank=16 price=17.92 support=16.52 resistance=17.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6268770.0 spike=0.57
- IDRE.CA: score=12.45 buy_ready=False sector_rank=16 price=52.01 support=51.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=8452135.0 spike=0.51
- IFAP.CA: score=13.46 buy_ready=False sector_rank=7 price=20.06 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=7722506.5 spike=0.37
- INFI.CA: score=10.32 buy_ready=False sector_rank=16 price=124.8 support=122.0 resistance=161.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=17.97 liquidity=29739404.0 spike=1.66
- IRON.CA: score=8.95 buy_ready=False sector_rank=9 price=28.14 support=26.3 resistance=31.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.89 liquidity=9689955.0 spike=0.7
- ISMA.CA: score=6.92 buy_ready=False sector_rank=16 price=28.41 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=34.75 liquidity=7924090.5 spike=0.38
- ISMQ.CA: score=10.26 buy_ready=False sector_rank=9 price=8.58 support=8.53 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.88 liquidity=15955469.0 spike=0.64
- ISPH.CA: score=9.11 buy_ready=False sector_rank=19 price=11.65 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.13 liquidity=80124952.0 spike=1.19
- JUFO.CA: score=14.44 buy_ready=False sector_rank=15 price=25.82 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=39.93 liquidity=34941136.0 spike=1.68
- KABO.CA: score=17.82 buy_ready=False sector_rank=12 price=9.0 support=9.0 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=25867604.0 spike=0.63
- KWIN.CA: score=9.0 buy_ready=False sector_rank=16 price=88.62 support=82.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.27 liquidity=10060281.0 spike=0.25
- KZPC.CA: score=19.0 buy_ready=False sector_rank=16 price=13.9 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=60.53 liquidity=18918458.0 spike=0.59
- LCSW.CA: score=7.4 buy_ready=False sector_rank=21 price=31.81 support=31.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.77 liquidity=13684502.0 spike=0.57
- LUTS.CA: score=14.0 buy_ready=False sector_rank=16 price=0.85 support=0.83 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=49.46 liquidity=32709554.0 spike=0.23
- MAAL.CA: score=28.0 buy_ready=False sector_rank=16 price=10.7 support=8.18 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=85565800.0 spike=5.88
- MASR.CA: score=14.0 buy_ready=False sector_rank=16 price=7.44 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.04 liquidity=52203508.0 spike=0.54
- MBSC.CA: score=7.4 buy_ready=False sector_rank=21 price=329.67 support=333.33 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.82 liquidity=33581092.0 spike=0.75
- MCQE.CA: score=7.4 buy_ready=False sector_rank=21 price=200.84 support=200.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=16.4 liquidity=10717680.0 spike=0.43
- MCRO.CA: score=17.0 buy_ready=False sector_rank=16 price=1.59 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=59598808.0 spike=0.47
- MENA.CA: score=2.64 buy_ready=False sector_rank=20 price=6.45 support=6.56 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=2748822.25 spike=1.72
- MEPA.CA: score=14.0 buy_ready=False sector_rank=16 price=1.79 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=17661486.0 spike=0.45
- MFPC.CA: score=20.26 buy_ready=False sector_rank=9 price=47.01 support=39.34 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=55.57 liquidity=48444960.0 spike=0.27
- MFSC.CA: score=8.86 buy_ready=False sector_rank=16 price=49.99 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.18 liquidity=1861490.75 spike=0.39
- MHOT.CA: score=30.0 buy_ready=False sector_rank=1 price=18.89 support=16.61 resistance=19.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=25767810.0 spike=2.3
- MICH.CA: score=12.64 buy_ready=False sector_rank=16 price=48.38 support=46.03 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=27.96 liquidity=17844074.0 spike=1.32
- MILS.CA: score=7.99 buy_ready=False sector_rank=16 price=184.7 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=3995824.5 spike=0.19
- MIPH.CA: score=14.43 buy_ready=False sector_rank=19 price=809.92 support=700.2 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=57.77 liquidity=5700463.0 spike=0.61
- MOED.CA: score=8.0 buy_ready=False sector_rank=16 price=0.7 support=0.7 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=20.67 liquidity=21345912.0 spike=0.32
- MOIL.CA: score=17.84 buy_ready=False sector_rank=6 price=0.7 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=698445.25 spike=2.87
- MOIN.CA: score=12.83 buy_ready=False sector_rank=16 price=34.73 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=5832196.5 spike=0.19
- MOSC.CA: score=1.41 buy_ready=False sector_rank=16 price=290.02 support=290.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=20.29 liquidity=2414516.0 spike=0.42
- MPCI.CA: score=12.0 buy_ready=False sector_rank=16 price=379.98 support=371.11 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.09 liquidity=76007032.0 spike=0.55
- MPCO.CA: score=22.74 buy_ready=False sector_rank=7 price=2.58 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=127799184.0 spike=0.73
- MPRC.CA: score=9.0 buy_ready=False sector_rank=16 price=38.99 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.88 liquidity=15256951.0 spike=0.4
- MTIE.CA: score=9.26 buy_ready=False sector_rank=10 price=8.15 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=24.77 liquidity=17706208.0 spike=0.69
- NAHO.CA: score=-5.97 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38835.46 spike=0.67
- NCCW.CA: score=21.0 buy_ready=False sector_rank=16 price=7.39 support=5.77 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=64.66 liquidity=50186416.0 spike=0.69
- NEDA.CA: score=4.47 buy_ready=False sector_rank=16 price=2.7 support=2.7 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=475913.84 spike=0.5
- NHPS.CA: score=6.0 buy_ready=False sector_rank=16 price=77.61 support=77.5 resistance=82.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31039170.0 spike=2.0
- NINH.CA: score=9.0 buy_ready=False sector_rank=16 price=20.05 support=20.13 resistance=24.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=25.07 liquidity=19199882.0 spike=0.96
- NIPH.CA: score=16.73 buy_ready=False sector_rank=19 price=325.41 support=290.0 resistance=401.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.47 liquidity=106909880.0 spike=0.71
- OBRI.CA: score=8.0 buy_ready=False sector_rank=16 price=28.35 support=29.51 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=16.72 liquidity=11457137.0 spike=0.77
- OCDI.CA: score=8.45 buy_ready=False sector_rank=20 price=28.0 support=28.0 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=16.71 liquidity=69247504.0 spike=0.92
- OCPH.CA: score=7.71 buy_ready=False sector_rank=16 price=225.64 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=36.19 liquidity=2714203.0 spike=0.43
- ODIN.CA: score=13.65 buy_ready=False sector_rank=16 price=2.65 support=2.55 resistance=3.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.25 liquidity=9658736.0 spike=0.49
- OFH.CA: score=8.12 buy_ready=False sector_rank=16 price=1.02 support=0.98 resistance=1.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=420152768.0 spike=3.06
- OIH.CA: score=22.46 buy_ready=False sector_rank=2 price=2.11 support=1.98 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=76.0 liquidity=246648480.0 spike=2.03
- OLFI.CA: score=16.08 buy_ready=False sector_rank=15 price=22.42 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=54.4 liquidity=11108510.0 spike=0.63
- ORAS.CA: score=4.6 buy_ready=False sector_rank=13 price=818.44 support=802.0 resistance=835.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=156633088.0 spike=1.0
- ORHD.CA: score=13.61 buy_ready=False sector_rank=20 price=40.72 support=40.5 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.34 liquidity=173978080.0 spike=1.08
- ORWE.CA: score=18.4 buy_ready=False sector_rank=12 price=26.97 support=25.6 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.21 liquidity=70407920.0 spike=1.29
- PHAR.CA: score=8.73 buy_ready=False sector_rank=19 price=110.95 support=111.55 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.91 liquidity=53277704.0 spike=0.56
- PHDC.CA: score=8.45 buy_ready=False sector_rank=20 price=13.18 support=12.91 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=18.92 liquidity=81312128.0 spike=0.53
- PHTV.CA: score=8.8 buy_ready=False sector_rank=16 price=347.34 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.3 liquidity=1683019.25 spike=1.06
- POUL.CA: score=11.64 buy_ready=False sector_rank=15 price=38.55 support=37.15 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=21 September 01:28 PM market time freshness=DELAYED_CURRENT RSI=32.25 liquidity=58845364.0 spike=2.28
- PRCL.CA: score=12.4 buy_ready=False sector_rank=21 price=30.8 support=30.52 resistance=34.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.47 liquidity=14078143.0 spike=0.83
- PRDC.CA: score=8.45 buy_ready=False sector_rank=20 price=7.3 support=7.3 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=12.38 liquidity=42215568.0 spike=0.76
- PRMH.CA: score=7.93 buy_ready=False sector_rank=16 price=2.48 support=2.43 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=3936512.5 spike=0.52
- RACC.CA: score=9.03 buy_ready=False sector_rank=16 price=9.43 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=44.64 liquidity=5033778.5 spike=0.31
- RAKT.CA: score=3.08 buy_ready=False sector_rank=16 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=80724.48 spike=0.38
- RAYA.CA: score=8.92 buy_ready=False sector_rank=17 price=6.92 support=6.8 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=33457928.0 spike=0.62
- RMDA.CA: score=13.73 buy_ready=False sector_rank=19 price=5.79 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=51538776.0 spike=0.9
- ROTO.CA: score=2.62 buy_ready=False sector_rank=16 price=39.57 support=35.02 resistance=45.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=33.66 liquidity=3622049.5 spike=0.5
- RREI.CA: score=12.23 buy_ready=False sector_rank=16 price=4.02 support=4.05 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=36.63 liquidity=8233738.0 spike=0.5
- RTVC.CA: score=-0.21 buy_ready=False sector_rank=16 price=3.73 support=3.79 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=29.82 liquidity=1791106.63 spike=0.49
- RUBX.CA: score=26.0 buy_ready=False sector_rank=16 price=17.7 support=12.42 resistance=17.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=298542816.0 spike=6.51
- SAUD.CA: score=6.05 buy_ready=False sector_rank=8 price=23.29 support=22.75 resistance=24.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25793450.0 spike=1.33
- SCEM.CA: score=7.4 buy_ready=False sector_rank=21 price=84.57 support=83.9 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=19.63 liquidity=29670232.0 spike=0.32
- SCFM.CA: score=5.56 buy_ready=False sector_rank=16 price=257.94 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:10 PM market time freshness=DELAYED_CURRENT RSI=40.47 liquidity=1564252.5 spike=0.22
- SCTS.CA: score=2.58 buy_ready=False sector_rank=5 price=572.97 support=566.66 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=29.48 liquidity=1182030.38 spike=0.48
- SDTI.CA: score=19.0 buy_ready=False sector_rank=16 price=79.99 support=68.57 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=71.04 liquidity=23455470.0 spike=0.97
- SEIG.CA: score=-0.15 buy_ready=False sector_rank=16 price=226.15 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=31.27 liquidity=854699.44 spike=0.45
- SIPC.CA: score=17.0 buy_ready=False sector_rank=16 price=5.17 support=4.77 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=51.5 liquidity=17442464.0 spike=0.25
- SKPC.CA: score=9.26 buy_ready=False sector_rank=9 price=17.06 support=17.16 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.19 liquidity=122265856.0 spike=0.93
- SMFR.CA: score=3.12 buy_ready=False sector_rank=16 price=221.88 support=226.1 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.35 liquidity=4125935.0 spike=0.54
- SNFC.CA: score=18.0 buy_ready=False sector_rank=16 price=11.54 support=10.26 resistance=11.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=79.49 liquidity=12788700.0 spike=0.9
- SPIN.CA: score=4.76 buy_ready=False sector_rank=12 price=16.81 support=16.1 resistance=20.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.94 liquidity=4935768.5 spike=0.36
- SPMD.CA: score=14.0 buy_ready=False sector_rank=16 price=0.4 support=0.4 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=15797946.0 spike=0.21
- SUGR.CA: score=17.08 buy_ready=False sector_rank=15 price=57.05 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=11559520.0 spike=0.32
- SVCE.CA: score=12.0 buy_ready=False sector_rank=16 price=10.9 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=29.25 liquidity=49259248.0 spike=0.25
- SWDY.CA: score=21.01 buy_ready=False sector_rank=11 price=118.74 support=122.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=38.63 liquidity=137794128.0 spike=2.39
- TALM.CA: score=23.4 buy_ready=False sector_rank=5 price=20.39 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=64.22 liquidity=29864376.0 spike=0.45
- TMGH.CA: score=8.45 buy_ready=False sector_rank=20 price=91.85 support=92.56 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=31.88 liquidity=218448256.0 spike=0.76
- TRTO.CA: score=-5.99 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10604.6 spike=0.37
- UEFM.CA: score=0.53 buy_ready=False sector_rank=16 price=458.83 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=30.06 liquidity=2538174.5 spike=0.83
- UEGC.CA: score=15.0 buy_ready=False sector_rank=16 price=1.57 support=1.61 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=43.64 liquidity=39122888.0 spike=0.75
- UNIP.CA: score=13.06 buy_ready=False sector_rank=16 price=0.36 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=9066216.0 spike=0.42
- UNIT.CA: score=7.09 buy_ready=False sector_rank=20 price=17.79 support=17.12 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=47.33 liquidity=3633110.0 spike=0.25
- WCDF.CA: score=9.13 buy_ready=False sector_rank=16 price=688.82 support=640.0 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=2132114.25 spike=0.41
- WKOL.CA: score=8.98 buy_ready=False sector_rank=16 price=325.34 support=325.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=4985270.0 spike=0.37
- ZEOT.CA: score=4.63 buy_ready=False sector_rank=16 price=12.31 support=12.6 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=28.18 liquidity=5629741.0 spike=0.92
- ZMID.CA: score=8.45 buy_ready=False sector_rank=20 price=8.02 support=8.07 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=28.98 liquidity=84170072.0 spike=0.39

## Backtesting Lite
- MHOT.CA: 180d return=-26.31%, max drawdown=-54.07%, MA20>MA50 days last20=15, as_of=2026-09-22T21:00:00+00:00
- MAAL.CA: 180d return=145.22%, max drawdown=-18.9%, MA20>MA50 days last20=20, as_of=2026-09-22T21:00:00+00:00
- RUBX.CA: 180d return=71.63%, max drawdown=-17.75%, MA20>MA50 days last20=10, as_of=2026-09-22T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- MAAL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Marseille Almasreia Alkhalegeya For Holding Investment SAE summary=Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- EGTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Resorts Company summary=Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- GIHD.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3919 sources=3 expected=Gharbia Islamic Housing Development Company summary=Gharbia Islamic Housing to discuss raising capital mid-December; Gharbia Islamic Housing to distribute EGP 0.2/shr; Gharbia Islamic Housing profits fall 46% in 2016
  - Gharbia Islamic Housing to discuss raising capital mid-December: https://english.mubasher.info/news/3147599/Gharbia-Islamic-Housing-to-discuss-raising-capital-mid-December/
  - Gharbia Islamic Housing to distribute EGP 0.2/shr: https://english.mubasher.info/news/3082262/Gharbia-Islamic-Housing-to-distribute-EGP-0-2-shr/
  - Gharbia Islamic Housing profits fall 46% in 2016: https://english.mubasher.info/news/3068305/Gharbia-Islamic-Housing-profits-fall-46-in-2016/
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.

## Warnings
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- Evidence for GIHD.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
