# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-11-11T14:13:09.348848+00:00
Generated Cairo: 2026-11-11 16:13
Run timing: target 09:15 Cairo | generated Cairo 2026-11-11 16:13 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-11-11 16:09

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 175/187
- Top sector: Technology & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Wednesday, November 11
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 94.44% / above MA50 38.89%
- EGX70 regime: BEARISH / above MA20 95.0% / above MA50 27.5%
- Sector breadth: 42.86%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- GTWL.CA: liquidity=692219200.0 spike=3.09 score=10.58
- AMES.CA: liquidity=595745280.0 spike=4.81 score=11.4
- BIOC.CA: liquidity=413586368.0 spike=3.19 score=10.78
- ABUK.CA: liquidity=365650112.0 spike=3.01 score=10.42
- CCAP.CA: liquidity=362501920.0 spike=0.87 score=20.4

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- CCRS.CA: spike=9.65 liquidity=104836776.0 outlook=CONSTRUCTIVE score=67.71 buy_ready=False
- MOIL.CA: spike=9.47 liquidity=1400513.75 outlook=BULLISH_WATCH score=91 buy_ready=False
- SUGR.CA: spike=9.46 liquidity=106956592.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- KWIN.CA: spike=6.27 liquidity=54959076.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMES.CA: spike=4.81 liquidity=595745280.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Technology & Distribution: score=14.22 5d=18.85% 20d=4.92% aboveMA50=0.0%
- #2 Industrial Goods & Cables: score=12.54 5d=13.61% 20d=7.29% aboveMA50=50.0%
- #3 Agriculture & Food Production: score=12.37 5d=18.75% 20d=0.65% aboveMA50=0.0%
- #4 Tourism & Leisure: score=12.28 5d=8.08% 20d=3.92% aboveMA50=100.0%
- #5 Energy & Petrochemicals: score=12.0 5d=7.36% 20d=-3.63% aboveMA50=33.33%
- #6 Building Materials: score=11.24 5d=11.34% 20d=5.0% aboveMA50=50.0%
- #7 Healthcare: score=10.8 5d=11.26% 20d=4.56% aboveMA50=50.0%
- #8 Food, Beverages & Tobacco: score=10.22 5d=7.9% 20d=7.06% aboveMA50=28.57%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- PHAR.CA: BULLISH_WATCH score=95 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support
- ETRS.CA: BULLISH_WATCH score=93.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- UEFM.CA: BULLISH_WATCH score=93.71 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- MOIL.CA: BULLISH_WATCH score=91 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MHOT.CA: BULLISH_WATCH score=90 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support
- MOSC.CA: BULLISH_WATCH score=89.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- ZEOT.CA: BULLISH_WATCH score=89.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; sector is not leading
- ACAMD.CA: BULLISH_WATCH score=85.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- SNFC.CA: BULLISH_WATCH score=85.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=close to resistance; sector is not leading
- MOIN.CA: BULLISH_WATCH score=83.71 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support; close to resistance; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=23.36 buy_ready=False sector_rank=10 price=255.37 support=171.02 resistance=258.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=56.9 liquidity=45159956.0 spike=2.48
- ABUK.CA: score=10.42 buy_ready=False sector_rank=19 price=78.0 support=74.6 resistance=78.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=365650112.0 spike=3.01
- ACAMD.CA: score=26.64 buy_ready=False sector_rank=10 price=2.09 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=144027120.0 spike=2.62
- ACGC.CA: score=25.96 buy_ready=False sector_rank=11 price=13.86 support=11.6 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=10088128.0 spike=1.28
- ADCI.CA: score=19.36 buy_ready=False sector_rank=10 price=273.31 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=3256066.0 spike=1.35
- ADIB.CA: score=25.4 buy_ready=False sector_rank=14 price=49.89 support=43.16 resistance=50.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.34 liquidity=47686084.0 spike=0.58
- ADPC.CA: score=20.94 buy_ready=False sector_rank=10 price=3.16 support=2.53 resistance=3.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=55.07 liquidity=13302218.0 spike=1.77
- AFDI.CA: score=12.32 buy_ready=False sector_rank=10 price=46.01 support=34.8 resistance=50.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=48.93 liquidity=1918491.88 spike=0.68
- AFMC.CA: score=23.46 buy_ready=False sector_rank=10 price=149.07 support=94.6 resistance=156.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=65.98 liquidity=20798698.0 spike=1.03
- AJWA.CA: score=23.4 buy_ready=False sector_rank=10 price=266.98 support=190.2 resistance=273.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=70.46 liquidity=29891216.0 spike=0.9
- ALCN.CA: score=22.81 buy_ready=False sector_rank=17 price=32.82 support=27.11 resistance=33.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=47.82 liquidity=9405137.0 spike=0.81
- ALUM.CA: score=16.7 buy_ready=False sector_rank=10 price=21.0 support=16.02 resistance=21.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=53.63 liquidity=4338984.5 spike=1.48
- AMER.CA: score=21.76 buy_ready=False sector_rank=15 price=4.5 support=3.21 resistance=4.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.83 liquidity=103765728.0 spike=1.68
- AMES.CA: score=11.4 buy_ready=False sector_rank=10 price=51.55 support=48.01 resistance=52.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=595745280.0 spike=4.81
- AMIA.CA: score=22.34 buy_ready=False sector_rank=10 price=17.39 support=14.0 resistance=19.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.52 liquidity=34433744.0 spike=2.97
- AMOC.CA: score=16.4 buy_ready=False sector_rank=5 price=13.15 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.62 liquidity=107355016.0 spike=0.76
- APSW.CA: score=9.72 buy_ready=False sector_rank=10 price=7.92 support=7.1 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:00 PM market time freshness=DELAYED_CURRENT RSI=52.07 liquidity=315368.53 spike=0.66
- ARAB.CA: score=23.4 buy_ready=False sector_rank=15 price=0.26 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.41 liquidity=83613624.0 spike=0.94
- ARCC.CA: score=25.4 buy_ready=False sector_rank=6 price=70.13 support=58.01 resistance=70.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.81 liquidity=29315600.0 spike=0.82
- AREH.CA: score=19.62 buy_ready=False sector_rank=10 price=1.13 support=0.91 resistance=1.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=9677624.0 spike=1.27
- ASCM.CA: score=16.87 buy_ready=False sector_rank=10 price=49.07 support=38.2 resistance=50.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=53.65 liquidity=7474863.0 spike=1.0
- ASPI.CA: score=21.84 buy_ready=False sector_rank=10 price=0.34 support=0.27 resistance=0.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=59.04 liquidity=28282344.0 spike=1.22
- ATLC.CA: score=22.3 buy_ready=False sector_rank=16 price=5.18 support=3.93 resistance=5.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.88 liquidity=16371677.0 spike=1.95
- ATQA.CA: score=20.4 buy_ready=False sector_rank=19 price=10.08 support=8.25 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=43.07 liquidity=36850864.0 spike=0.81
- AXPH.CA: score=19.9 buy_ready=False sector_rank=10 price=1460.83 support=1135.0 resistance=1450.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=61.47 liquidity=6683514.0 spike=1.41
- BINV.CA: score=21.58 buy_ready=False sector_rank=18 price=55.52 support=50.62 resistance=62.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=41.73 liquidity=15120332.0 spike=1.59
- BIOC.CA: score=10.78 buy_ready=False sector_rank=10 price=440.03 support=377.01 resistance=446.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=413586368.0 spike=3.19
- BTFH.CA: score=20.54 buy_ready=False sector_rank=16 price=2.49 support=2.05 resistance=2.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.95 liquidity=186467104.0 spike=1.57
- CAED.CA: score=23.36 buy_ready=False sector_rank=10 price=108.35 support=64.0 resistance=116.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=59.47 liquidity=32835682.0 spike=1.48
- CANA.CA: score=30.4 buy_ready=False sector_rank=14 price=51.02 support=38.1 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=62.88 liquidity=75384656.0 spike=4.01
- CCAP.CA: score=20.4 buy_ready=False sector_rank=18 price=6.1 support=5.55 resistance=6.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.69 liquidity=362501920.0 spike=0.87
- CCRS.CA: score=27.4 buy_ready=False sector_rank=10 price=2.19 support=1.3 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.78 liquidity=104836776.0 spike=9.65
- CEFM.CA: score=14.56 buy_ready=False sector_rank=10 price=125.23 support=97.79 resistance=132.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.5 liquidity=2157369.25 spike=0.89
- CERA.CA: score=19.4 buy_ready=False sector_rank=10 price=1.15 support=0.93 resistance=1.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.28 liquidity=58125212.0 spike=0.7
- CFGH.CA: score=8.95 buy_ready=False sector_rank=10 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-11-09T22:00:00+00:00 freshness=FRESH RSI=45.45 liquidity=7407.64 spike=1.77
- CICH.CA: score=10.21 buy_ready=False sector_rank=16 price=10.7 support=9.63 resistance=11.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.01 liquidity=805706.75 spike=0.35
- CIEB.CA: score=23.3 buy_ready=False sector_rank=14 price=23.27 support=21.35 resistance=23.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.34 liquidity=11864185.0 spike=1.45
- CIRA.CA: score=26.06 buy_ready=False sector_rank=13 price=39.39 support=32.01 resistance=39.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=17124986.0 spike=1.33
- CLHO.CA: score=21.4 buy_ready=False sector_rank=7 price=14.63 support=12.51 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=60.99 liquidity=25048232.0 spike=0.54
- CNFN.CA: score=19.82 buy_ready=False sector_rank=16 price=4.22 support=3.25 resistance=4.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=55.44 liquidity=8417402.0 spike=0.99
- COMI.CA: score=24.4 buy_ready=False sector_rank=14 price=129.94 support=117.41 resistance=131.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.13 liquidity=342394912.0 spike=0.65
- COPR.CA: score=23.36 buy_ready=False sector_rank=10 price=0.43 support=0.33 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=42814020.0 spike=2.48
- COSG.CA: score=20.2 buy_ready=False sector_rank=10 price=1.41 support=1.11 resistance=1.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=53.03 liquidity=13049270.0 spike=1.4
- CPCI.CA: score=14.4 buy_ready=False sector_rank=10 price=598.31 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=52.58 liquidity=2997858.0 spike=0.61
- CSAG.CA: score=16.35 buy_ready=False sector_rank=17 price=35.23 support=30.1 resistance=37.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=5946399.5 spike=0.86
- DAPH.CA: score=20.86 buy_ready=False sector_rank=10 price=91.01 support=65.2 resistance=101.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.98 liquidity=27931572.0 spike=1.23
- DEIN.CA: score=9.4 buy_ready=False sector_rank=10 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=21.66 buy_ready=False sector_rank=8 price=25.2 support=20.27 resistance=25.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=5676658.0 spike=2.79
- DSCW.CA: score=20.5 buy_ready=False sector_rank=10 price=1.56 support=1.23 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.62 liquidity=21636580.0 spike=1.55
- DTPP.CA: score=23.8 buy_ready=False sector_rank=10 price=60.15 support=36.0 resistance=68.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.34 liquidity=124106072.0 spike=3.2
- EALR.CA: score=24.4 buy_ready=False sector_rank=10 price=319.05 support=236.01 resistance=325.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.34 liquidity=24222148.0 spike=3.66
- EASB.CA: score=17.02 buy_ready=False sector_rank=10 price=6.81 support=5.03 resistance=7.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.06 liquidity=6618577.0 spike=0.95
- EAST.CA: score=24.08 buy_ready=False sector_rank=8 price=34.9 support=27.02 resistance=33.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=66.82 liquidity=65869900.0 spike=1.84
- EBSC.CA: score=12.85 buy_ready=False sector_rank=10 price=1.62 support=1.2 resistance=1.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=3446412.5 spike=0.87
- ECAP.CA: score=13.04 buy_ready=False sector_rank=10 price=29.02 support=24.8 resistance=30.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.29 liquidity=1636719.25 spike=0.62
- EDFM.CA: score=12.99 buy_ready=False sector_rank=10 price=368.03 support=326.73 resistance=375.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=56.65 liquidity=588433.94 spike=0.51
- EEII.CA: score=19.7 buy_ready=False sector_rank=10 price=2.04 support=1.42 resistance=2.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=11994131.0 spike=1.15
- EFIC.CA: score=24.4 buy_ready=False sector_rank=19 price=170.26 support=121.0 resistance=174.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=56.82 liquidity=18000662.0 spike=0.65
- EFID.CA: score=21.4 buy_ready=False sector_rank=8 price=19.81 support=16.01 resistance=20.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.82 liquidity=17484676.0 spike=0.49
- EFIH.CA: score=25.4 buy_ready=False sector_rank=9 price=24.8 support=20.3 resistance=25.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=55.18 liquidity=37649304.0 spike=0.65
- EGAL.CA: score=20.4 buy_ready=False sector_rank=19 price=321.05 support=275.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=62.51 liquidity=85133520.0 spike=0.79
- EGAS.CA: score=25.4 buy_ready=False sector_rank=5 price=51.4 support=43.0 resistance=53.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.65 liquidity=15832889.0 spike=4.52
- EGBE.CA: score=6.42 buy_ready=False sector_rank=14 price=0.49 support=0.47 resistance=0.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=42.35 liquidity=23762.97 spike=0.36
- EGCH.CA: score=19.4 buy_ready=False sector_rank=19 price=11.0 support=9.66 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.33 liquidity=42239204.0 spike=0.82
- EGSA.CA: score=13.4 buy_ready=False sector_rank=12 price=9.0 support=8.7 resistance=9.09 source=Yahoo Finance as_of=2026-11-09T22:00:00+00:00 freshness=FRESH RSI=47.54 liquidity=3321.0 spike=0.45
- EGTS.CA: score=20.4 buy_ready=False sector_rank=15 price=14.12 support=10.19 resistance=14.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=56.37 liquidity=18295696.0 spike=0.9
- EHDR.CA: score=18.52 buy_ready=False sector_rank=10 price=2.23 support=1.8 resistance=2.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9123331.0 spike=0.91
- ELEC.CA: score=21.4 buy_ready=False sector_rank=2 price=1.74 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=33833104.0 spike=0.65
- ELKA.CA: score=22.4 buy_ready=False sector_rank=10 price=1.59 support=1.21 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.44 liquidity=10552407.0 spike=0.8
- ELNA.CA: score=11.12 buy_ready=False sector_rank=10 price=43.4 support=33.46 resistance=44.2 source=Yahoo Finance as_of=2026-11-09T22:00:00+00:00 freshness=FRESH RSI=79.34 liquidity=721698.63 spike=0.96
- ELSH.CA: score=24.74 buy_ready=False sector_rank=10 price=11.4 support=8.57 resistance=11.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=56.87 liquidity=33173114.0 spike=2.17
- ELWA.CA: score=2.61 buy_ready=False sector_rank=10 price=1.33 support=1.27 resistance=1.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=8.7 liquidity=1489369.75 spike=1.36
- EMFD.CA: score=22.4 buy_ready=False sector_rank=15 price=12.57 support=10.6 resistance=12.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=42980780.0 spike=0.75
- ENGC.CA: score=27.3 buy_ready=False sector_rank=10 price=39.96 support=26.91 resistance=41.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=67.12 liquidity=36256044.0 spike=2.95
- EOSB.CA: score=9.55 buy_ready=False sector_rank=10 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-11-09T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=94354.05 spike=1.03
- EPCO.CA: score=15.44 buy_ready=False sector_rank=10 price=9.18 support=7.0 resistance=9.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=57.25 liquidity=4040989.0 spike=0.75
- EPPK.CA: score=-3.18 buy_ready=False sector_rank=10 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=23.4 buy_ready=False sector_rank=12 price=135.13 support=115.0 resistance=148.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.97 liquidity=174829488.0 spike=0.74
- ETRS.CA: score=27.12 buy_ready=False sector_rank=10 price=11.0 support=9.51 resistance=11.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.67 liquidity=24121322.0 spike=1.86
- EXPA.CA: score=21.4 buy_ready=False sector_rank=14 price=14.97 support=12.0 resistance=14.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.06 liquidity=20936688.0 spike=0.89
- FAIT.CA: score=17.41 buy_ready=False sector_rank=14 price=45.19 support=40.0 resistance=46.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=53.52 liquidity=2010513.25 spike=0.78
- FAITA.CA: score=13.43 buy_ready=False sector_rank=14 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=56.19 liquidity=29680.79 spike=0.81
- FERC.CA: score=15.03 buy_ready=False sector_rank=19 price=68.8 support=52.63 resistance=72.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=56.15 liquidity=5626624.5 spike=0.74
- FWRY.CA: score=20.24 buy_ready=False sector_rank=9 price=17.88 support=15.27 resistance=18.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=48.37 liquidity=148491024.0 spike=1.42
- GBCO.CA: score=12.28 buy_ready=False sector_rank=20 price=23.15 support=20.9 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.29 liquidity=133479920.0 spike=1.11
- GDWA.CA: score=19.52 buy_ready=False sector_rank=10 price=0.57 support=0.46 resistance=0.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=50.46 liquidity=12894195.0 spike=1.06
- GGCC.CA: score=20.78 buy_ready=False sector_rank=10 price=0.59 support=0.49 resistance=0.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=45.39 liquidity=37191612.0 spike=1.69
- GIHD.CA: score=20.64 buy_ready=False sector_rank=10 price=53.23 support=32.1 resistance=57.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=60.2 liquidity=17653590.0 spike=1.12
- GMCI.CA: score=10.41 buy_ready=False sector_rank=10 price=1.62 support=1.34 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT RSI=51.11 liquidity=407358.53 spike=1.3
- GRCA.CA: score=11.4 buy_ready=False sector_rank=10 price=34.65 support=32.56 resistance=37.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39647464.0 spike=4.23
- GSSC.CA: score=11.44 buy_ready=False sector_rank=10 price=263.48 support=211.52 resistance=273.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=1035226.31 spike=0.69
- GTWL.CA: score=10.58 buy_ready=False sector_rank=10 price=148.55 support=135.12 resistance=158.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=692219200.0 spike=3.09
- HDBK.CA: score=19.5 buy_ready=False sector_rank=14 price=103.06 support=83.01 resistance=105.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=54.46 liquidity=26034292.0 spike=1.05
- HELI.CA: score=20.82 buy_ready=False sector_rank=15 price=7.09 support=5.72 resistance=7.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=93235824.0 spike=1.21
- HRHO.CA: score=22.4 buy_ready=False sector_rank=16 price=25.28 support=21.87 resistance=26.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.18 liquidity=28520512.0 spike=0.51
- ICID.CA: score=11.79 buy_ready=False sector_rank=10 price=17.29 support=14.26 resistance=18.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=49.45 liquidity=1394632.25 spike=0.27
- IDRE.CA: score=21.73 buy_ready=False sector_rank=10 price=44.0 support=29.11 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=55.75 liquidity=8570147.0 spike=1.38
- IFAP.CA: score=13.62 buy_ready=False sector_rank=3 price=17.84 support=15.12 resistance=19.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.44 liquidity=3216574.25 spike=0.49
- INFI.CA: score=20.4 buy_ready=False sector_rank=10 price=125.32 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=51.42 liquidity=14258395.0 spike=0.65
- IRON.CA: score=15.28 buy_ready=False sector_rank=19 price=25.93 support=23.13 resistance=27.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.27 liquidity=12263783.0 spike=1.44
- ISMA.CA: score=19.58 buy_ready=False sector_rank=10 price=21.63 support=14.11 resistance=23.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=11124817.0 spike=1.09
- ISMQ.CA: score=20.52 buy_ready=False sector_rank=19 price=7.59 support=5.96 resistance=7.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.34 liquidity=20469474.0 spike=1.56
- ISPH.CA: score=19.44 buy_ready=False sector_rank=7 price=10.35 support=9.02 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=50.42 liquidity=61708308.0 spike=1.02
- JUFO.CA: score=22.0 buy_ready=False sector_rank=8 price=24.7 support=21.01 resistance=24.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=54.27 liquidity=29214554.0 spike=1.3
- KABO.CA: score=20.48 buy_ready=False sector_rank=11 price=7.45 support=5.58 resistance=8.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.39 liquidity=20139044.0 spike=1.04
- KWIN.CA: score=11.4 buy_ready=False sector_rank=10 price=79.0 support=72.81 resistance=85.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54959076.0 spike=6.27
- KZPC.CA: score=23.68 buy_ready=False sector_rank=10 price=14.05 support=11.56 resistance=14.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=58.16 liquidity=11030707.0 spike=1.14
- LCSW.CA: score=21.5 buy_ready=False sector_rank=6 price=40.0 support=28.0 resistance=39.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=70.07 liquidity=23241344.0 spike=1.05
- LUTS.CA: score=22.4 buy_ready=False sector_rank=10 price=0.78 support=0.47 resistance=0.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.85 liquidity=50711924.0 spike=0.82
- MAAL.CA: score=22.6 buy_ready=False sector_rank=10 price=6.95 support=4.88 resistance=10.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=55116764.0 spike=3.1
- MASR.CA: score=20.64 buy_ready=False sector_rank=10 price=7.0 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.87 liquidity=44449856.0 spike=1.12
- MBSC.CA: score=20.4 buy_ready=False sector_rank=6 price=342.95 support=262.0 resistance=400.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.15 liquidity=43832640.0 spike=0.71
- MCQE.CA: score=22.4 buy_ready=False sector_rank=6 price=186.68 support=144.0 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.37 liquidity=40853540.0 spike=0.79
- MCRO.CA: score=25.8 buy_ready=False sector_rank=10 price=1.42 support=1.07 resistance=1.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=54.43 liquidity=128136440.0 spike=2.7
- MENA.CA: score=12.78 buy_ready=False sector_rank=15 price=6.12 support=5.45 resistance=6.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=379123.5 spike=0.1
- MEPA.CA: score=19.92 buy_ready=False sector_rank=10 price=1.45 support=1.14 resistance=1.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=45.07 liquidity=21519946.0 spike=1.26
- MFPC.CA: score=12.74 buy_ready=False sector_rank=19 price=39.17 support=37.23 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=25.86 liquidity=168812224.0 spike=2.17
- MFSC.CA: score=10.44 buy_ready=False sector_rank=10 price=37.11 support=28.55 resistance=42.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=51.58 liquidity=1036381.44 spike=0.47
- MHOT.CA: score=23.63 buy_ready=False sector_rank=4 price=16.92 support=13.0 resistance=16.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=53.89 liquidity=8208366.0 spike=1.51
- MICH.CA: score=25.08 buy_ready=False sector_rank=10 price=45.52 support=35.5 resistance=45.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=57.18 liquidity=9015457.0 spike=1.33
- MILS.CA: score=18.97 buy_ready=False sector_rank=10 price=148.56 support=94.24 resistance=158.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=53.93 liquidity=8569877.0 spike=0.94
- MIPH.CA: score=15.92 buy_ready=False sector_rank=7 price=811.75 support=610.0 resistance=810.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=61.26 liquidity=518515.66 spike=0.16
- MOED.CA: score=21.24 buy_ready=False sector_rank=10 price=0.53 support=0.39 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.37 liquidity=26480288.0 spike=1.92
- MOIL.CA: score=19.8 buy_ready=False sector_rank=5 price=0.69 support=0.6 resistance=0.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=52.81 liquidity=1400513.75 spike=9.47
- MOIN.CA: score=28.26 buy_ready=False sector_rank=10 price=33.47 support=25.7 resistance=33.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=59.82 liquidity=19433186.0 spike=2.43
- MOSC.CA: score=30.4 buy_ready=False sector_rank=10 price=289.74 support=198.01 resistance=286.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=18527132.0 spike=3.54
- MPCI.CA: score=7.6 buy_ready=False sector_rank=10 price=359.79 support=343.0 resistance=366.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=170624640.0 spike=1.6
- MPCO.CA: score=25.06 buy_ready=False sector_rank=3 price=2.16 support=1.55 resistance=2.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.04 liquidity=164868816.0 spike=1.83
- MPRC.CA: score=23.48 buy_ready=False sector_rank=10 price=40.0 support=27.0 resistance=39.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.87 liquidity=20697438.0 spike=1.04
- MTIE.CA: score=19.06 buy_ready=False sector_rank=20 price=7.32 support=6.05 resistance=8.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=17699150.0 spike=0.77
- NAHO.CA: score=6.41 buy_ready=False sector_rank=10 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:01 PM market time freshness=DELAYED_CURRENT RSI=42.11 liquidity=5691.34 spike=0.34
- NCCW.CA: score=23.4 buy_ready=False sector_rank=10 price=5.88 support=4.05 resistance=6.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=24830206.0 spike=1.5
- NEDA.CA: score=2.93 buy_ready=False sector_rank=10 price=2.46 support=2.26 resistance=2.6 source=Yahoo Finance as_of=2026-11-09T22:00:00+00:00 freshness=FRESH RSI=29.41 liquidity=367378.87 spike=2.08
- NHPS.CA: score=22.58 buy_ready=False sector_rank=10 price=65.67 support=50.0 resistance=68.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=54.93 liquidity=19900956.0 spike=2.59
- NINH.CA: score=24.34 buy_ready=False sector_rank=10 price=17.28 support=12.36 resistance=18.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=62.34 liquidity=21748630.0 spike=1.97
- NIPH.CA: score=7.34 buy_ready=False sector_rank=7 price=324.36 support=306.0 resistance=325.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=215120704.0 spike=1.47
- OBRI.CA: score=18.13 buy_ready=False sector_rank=10 price=25.54 support=18.11 resistance=27.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=51.19 liquidity=8731102.0 spike=0.95
- OCDI.CA: score=20.4 buy_ready=False sector_rank=15 price=26.2 support=21.0 resistance=26.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=32593018.0 spike=0.93
- OCPH.CA: score=20.87 buy_ready=False sector_rank=10 price=212.08 support=147.96 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=56.87 liquidity=8049986.0 spike=1.71
- ODIN.CA: score=21.42 buy_ready=False sector_rank=10 price=2.2 support=1.7 resistance=2.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=15442898.0 spike=2.01
- OFH.CA: score=21.02 buy_ready=False sector_rank=10 price=0.79 support=0.61 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=28065394.0 spike=1.31
- OIH.CA: score=20.66 buy_ready=False sector_rank=18 price=1.76 support=1.5 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.65 liquidity=49748744.0 spike=1.13
- OLFI.CA: score=18.24 buy_ready=False sector_rank=8 price=20.55 support=17.86 resistance=21.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=61.32 liquidity=6840489.5 spike=0.86
- ORAS.CA: score=4.6 buy_ready=False sector_rank=21 price=808.56 support=801.02 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=179328832.0 spike=1.0
- ORHD.CA: score=19.4 buy_ready=False sector_rank=15 price=10.45 support=8.5 resistance=11.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.29 liquidity=102816192.0 spike=0.91
- ORWE.CA: score=20.4 buy_ready=False sector_rank=11 price=25.96 support=22.2 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=53.05 liquidity=16966596.0 spike=0.49
- PHAR.CA: score=27.44 buy_ready=False sector_rank=7 price=112.49 support=90.2 resistance=112.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.4 liquidity=124195704.0 spike=2.02
- PHDC.CA: score=23.36 buy_ready=False sector_rank=15 price=12.43 support=10.33 resistance=13.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.29 liquidity=297825248.0 spike=2.48
- PHTV.CA: score=10.94 buy_ready=False sector_rank=10 price=331.14 support=300.0 resistance=343.0 source=Yahoo Finance as_of=2026-11-09T22:00:00+00:00 freshness=FRESH RSI=45.19 liquidity=542076.2 spike=0.39
- POUL.CA: score=20.36 buy_ready=False sector_rank=8 price=10.21 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=59.52 liquidity=148282000.0 spike=1.48
- PRCL.CA: score=23.82 buy_ready=False sector_rank=6 price=22.31 support=16.65 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.61 liquidity=57196768.0 spike=3.21
- PRDC.CA: score=24.86 buy_ready=False sector_rank=15 price=6.85 support=5.08 resistance=7.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=60.71 liquidity=44481144.0 spike=2.23
- PRMH.CA: score=29.68 buy_ready=False sector_rank=10 price=2.31 support=1.7 resistance=2.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=16718808.0 spike=3.14
- RACC.CA: score=20.42 buy_ready=False sector_rank=10 price=8.33 support=6.1 resistance=9.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=48.24 liquidity=10007151.0 spike=1.51
- RAKT.CA: score=12.15 buy_ready=False sector_rank=10 price=22.47 support=20.4 resistance=23.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=36.23 liquidity=425482.72 spike=1.66
- RAYA.CA: score=26.0 buy_ready=False sector_rank=1 price=6.3 support=5.02 resistance=6.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.11 liquidity=43490824.0 spike=1.8
- RMDA.CA: score=25.4 buy_ready=False sector_rank=7 price=5.6 support=4.5 resistance=5.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=25729220.0 spike=0.83
- ROTO.CA: score=20.34 buy_ready=False sector_rank=10 price=35.36 support=25.0 resistance=38.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=50.35 liquidity=13797330.0 spike=1.47
- RREI.CA: score=19.42 buy_ready=False sector_rank=10 price=2.94 support=1.96 resistance=3.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=43.96 liquidity=11404851.0 spike=1.01
- RTVC.CA: score=15.76 buy_ready=False sector_rank=10 price=3.11 support=2.66 resistance=3.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=38.94 liquidity=4717888.5 spike=1.82
- RUBX.CA: score=11.4 buy_ready=False sector_rank=10 price=14.11 support=10.51 resistance=18.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.5 liquidity=56961060.0 spike=0.9
- SAUD.CA: score=24.54 buy_ready=False sector_rank=14 price=22.18 support=19.3 resistance=23.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=57.01 liquidity=33215754.0 spike=2.07
- SCEM.CA: score=23.4 buy_ready=False sector_rank=6 price=98.07 support=73.9 resistance=99.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=27021560.0 spike=0.58
- SCFM.CA: score=11.48 buy_ready=False sector_rank=10 price=221.12 support=153.02 resistance=238.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=50.84 liquidity=2082515.88 spike=0.76
- SCTS.CA: score=13.23 buy_ready=False sector_rank=13 price=505.51 support=410.0 resistance=555.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=60.54 liquidity=2832228.75 spike=0.47
- SDTI.CA: score=23.4 buy_ready=False sector_rank=10 price=87.33 support=75.01 resistance=90.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=59.06 liquidity=12968249.0 spike=0.67
- SEIG.CA: score=17.06 buy_ready=False sector_rank=10 price=234.08 support=142.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=60.92 liquidity=3658701.0 spike=0.38
- SIPC.CA: score=23.4 buy_ready=False sector_rank=10 price=5.5 support=3.73 resistance=6.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=38272224.0 spike=0.78
- SKPC.CA: score=19.76 buy_ready=False sector_rank=19 price=15.04 support=14.01 resistance=15.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.42 liquidity=46958664.0 spike=1.18
- SMFR.CA: score=24.26 buy_ready=False sector_rank=10 price=227.74 support=165.0 resistance=264.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=62.7 liquidity=10501531.0 spike=1.43
- SNFC.CA: score=25.72 buy_ready=False sector_rank=10 price=11.21 support=10.08 resistance=11.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=53.59 liquidity=19551766.0 spike=2.16
- SPIN.CA: score=15.12 buy_ready=False sector_rank=11 price=15.51 support=12.0 resistance=16.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=67.39 liquidity=4720969.0 spike=0.78
- SPMD.CA: score=19.4 buy_ready=False sector_rank=10 price=0.36 support=0.3 resistance=0.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=48.03 liquidity=13499170.0 spike=0.76
- SUGR.CA: score=11.4 buy_ready=False sector_rank=8 price=50.55 support=47.9 resistance=51.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=106956592.0 spike=9.46
- SVCE.CA: score=20.48 buy_ready=False sector_rank=10 price=9.28 support=7.01 resistance=9.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.54 liquidity=53777216.0 spike=1.04
- SWDY.CA: score=25.4 buy_ready=False sector_rank=2 price=121.46 support=97.0 resistance=121.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=47820040.0 spike=0.86
- TALM.CA: score=21.94 buy_ready=False sector_rank=13 price=20.66 support=17.0 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=58.87 liquidity=8535681.0 spike=0.44
- TMGH.CA: score=19.4 buy_ready=False sector_rank=15 price=84.56 support=76.5 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.52 liquidity=192549568.0 spike=0.72
- TRTO.CA: score=1.42 buy_ready=False sector_rank=10 price=0.07 support=0.06 resistance=0.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:53 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=17227.06 spike=3.58
- UEFM.CA: score=20.32 buy_ready=False sector_rank=10 price=503.79 support=422.0 resistance=520.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=58.21 liquidity=3079277.75 spike=1.92
- UEGC.CA: score=19.4 buy_ready=False sector_rank=10 price=1.54 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=53.16 liquidity=23989430.0 spike=0.49
- UNIP.CA: score=16.32 buy_ready=False sector_rank=10 price=0.32 support=0.25 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=6915274.0 spike=0.94
- UNIT.CA: score=14.95 buy_ready=False sector_rank=15 price=18.01 support=15.06 resistance=19.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.7 liquidity=1546078.63 spike=0.77
- WCDF.CA: score=10.75 buy_ready=False sector_rank=10 price=548.58 support=432.5 resistance=566.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=66.21 liquidity=1753472.75 spike=1.3
- WKOL.CA: score=13.38 buy_ready=False sector_rank=10 price=183.75 support=145.33 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=24.13 liquidity=17462644.0 spike=1.49
- ZEOT.CA: score=29.62 buy_ready=False sector_rank=10 price=12.21 support=7.9 resistance=12.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=55.51 liquidity=27848698.0 spike=3.11
- ZMID.CA: score=20.4 buy_ready=False sector_rank=15 price=7.05 support=5.91 resistance=7.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=52.87 liquidity=72236296.0 spike=0.86

## Backtesting Lite
- CANA.CA: 180d return=18.7%, max drawdown=-36.46%, MA20>MA50 days last20=11, as_of=2026-11-09T22:00:00+00:00
- MOSC.CA: 180d return=67.7%, max drawdown=-37.28%, MA20>MA50 days last20=0, as_of=2026-11-09T22:00:00+00:00
- PRMH.CA: 180d return=12.2%, max drawdown=-40.0%, MA20>MA50 days last20=0, as_of=2026-11-09T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=679 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- MOSC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Oils & Soap summary=Misr Oils and Soap not to pay dividends for FY20/21; Misr Oils and Soap&#39;s profit plunges 78% in FY20/21; Misr Oils and Soap swings to loss in 10 months
  - Misr Oils and Soap not to pay dividends for FY20/21: https://english.mubasher.info/news/3856493/Misr-Oils-and-Soap-not-to-pay-dividends-for-FY20-21/
  - Misr Oils and Soap&#39;s profit plunges 78% in FY20/21: https://english.mubasher.info/news/3851183/Misr-Oils-and-Soap-s-profit-plunges-78-in-FY20-21/
  - Misr Oils and Soap swings to loss in 10 months: https://english.mubasher.info/news/3811105/Misr-Oils-and-Soap-swings-to-loss-in-10-months/
- PRMH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Prime Holding S.A.E summary=Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- ZEOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Extracted Oil & Derivatives Co. summary=Extracted Oils stock nears record high on strong momentum; Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis; Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26
  - Extracted Oils stock nears record high on strong momentum: https://english.mubasher.info/news/4599376/Extracted-Oils-stock-nears-record-high-on-strong-momentum/
  - Extracted Oils stock witnesses increasing buying power amid current resistance – Analysis: https://english.mubasher.info/news/4555925/Extracted-Oils-stock-witnesses-increasing-buying-power-amid-current-resistance-Analysis/
  - Extracted Oils swings to nearly EGP 14.5m net profits in Q1-25/26: https://english.mubasher.info/news/4537956/Extracted-Oils-swings-to-nearly-EGP-14-5m-net-profits-in-Q1-25-26/
- MOIN.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Mohandes Insurance Company summary=Mohandes Insurance unveils EGP 150m capital hike; Mohandes Insurance targets EGP 1.39bn investments in FY23/24; Mohandes Insurance eyes EGP 1bn investments in FY22/23
  - Mohandes Insurance unveils EGP 150m capital hike: https://english.mubasher.info/news/4538925/Mohandes-Insurance-unveils-EGP-150m-capital-hike/
  - Mohandes Insurance targets EGP 1.39bn investments in FY23/24: https://english.mubasher.info/news/4147038/Mohandes-Insurance-targets-EGP-1-39bn-investments-in-FY23-24/
  - Mohandes Insurance eyes EGP 1bn investments in FY22/23: https://english.mubasher.info/news/3986755/Mohandes-Insurance-eyes-EGP-1bn-investments-in-FY22-23/
- PHAR.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian International Pharmaceutical Industries summary=Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- CCRS.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3967 sources=3 expected=Gulf Canadian Company for Arab Real Estate Investment summary=10 EGX-listed firms deny ties to UAE-based Abraaj; Gulf Canadian OGM to discuss 2016 financials Thursday; Gulf Canadian OGM to discuss 2016 results 22 March
  - 10 EGX-listed firms deny ties to UAE-based Abraaj: https://english.mubasher.info/news/3308086/10-EGX-listed-firms-deny-ties-to-UAE-based-Abraaj/
  - Gulf Canadian OGM to discuss 2016 financials Thursday: https://english.mubasher.info/news/3076282/Gulf-Canadian-OGM-to-discuss-2016-financials-Thursday/
  - Gulf Canadian OGM to discuss 2016 results 22 March: https://english.mubasher.info/news/3067564/Gulf-Canadian-OGM-to-discuss-2016-results-22-March/
- ENGC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Industrial Engineering Company for Construction and Development (ICON) (S.A.E) summary=Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).

## Warnings
- OpenRouter API error: 404
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for MOSC.CA matches the company but no source/report date was detected.
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for ZEOT.CA matches the company but no source/report date was detected.
- Evidence for MOIN.CA matches the company but no source/report date was detected.
- Evidence rejected for PHAR.CA: source text did not clearly match PHAR.CA / Egyptian International Pharmaceutical Industries.
- Evidence for CCRS.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
