# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-09-24T10:32:22.715126+00:00
Generated Cairo: 2026-09-24 13:32
Run timing: target 08:45 Cairo | generated Cairo 2026-09-24 13:32 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-09-24 13:29

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 171/187
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, September 24
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 16.67% / above MA50 33.33%
- EGX70 regime: BEARISH / above MA20 15.38% / above MA50 28.21%
- Sector breadth: 19.05%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=725924032.0 spike=0.87 score=19.4
- OFH.CA: liquidity=350218624.0 spike=2.55 score=7.04
- COMI.CA: liquidity=334469344.0 spike=0.53 score=9.08
- RUBX.CA: liquidity=211302336.0 spike=4.61 score=25.94
- OIH.CA: liquidity=209649632.0 spike=1.72 score=18.84

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: 

## Top Liquidity Spikes
- EGBE.CA: spike=8.62 liquidity=638162.69 outlook=WEAK_OR_RISKY score=31.7 buy_ready=False
- MAAL.CA: spike=5.25 liquidity=76528504.0 outlook=BULLISH_WATCH score=86 buy_ready=False
- RUBX.CA: spike=4.61 liquidity=211302336.0 outlook=CONSTRUCTIVE score=58 buy_ready=False
- GIHD.CA: spike=2.91 liquidity=76893120.0 outlook=BULLISH_WATCH score=72 buy_ready=False
- OFH.CA: spike=2.55 liquidity=350218624.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=11.7 5d=6.04% 20d=2.68% aboveMA50=100.0%
- #2 Telecommunications: score=9.66 5d=2.58% 20d=11.29% aboveMA50=100.0%
- #3 Investment Holding: score=9.54 5d=0.46% 20d=15.28% aboveMA50=100.0%
- #4 Transportation & Logistics: score=6.99 5d=6.74% 20d=3.81% aboveMA50=50.0%
- #5 Education: score=6.37 5d=-3.49% 20d=16.36% aboveMA50=66.67%
- #6 Energy & Petrochemicals: score=4.73 5d=-0.37% 20d=5.88% aboveMA50=66.67%
- #7 Agriculture & Food Production: score=4.12 5d=-2.22% 20d=7.08% aboveMA50=50.0%
- #8 Automotive & Distribution: score=2.87 5d=-0.33% 20d=2.53% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MHOT.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MAAL.CA: BULLISH_WATCH score=86 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=far above support; sector is not leading
- ALCN.CA: BULLISH_WATCH score=84.99 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- BINV.CA: BULLISH_WATCH score=81.54 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- EGTS.CA: BULLISH_WATCH score=80 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=momentum is extended; sector is not leading
- ETEL.CA: BULLISH_WATCH score=75.66 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; overheated RSI
- OIH.CA: BULLISH_WATCH score=74.54 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; overheated RSI
- EXPA.CA: BULLISH_WATCH score=73.7 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading
- GIHD.CA: BULLISH_WATCH score=72 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=far above support; sector is not leading
- DTPP.CA: BULLISH_WATCH score=71 liquidity=TRADEABLE sector=LAGGING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=13.94 buy_ready=False sector_rank=17 price=280.02 support=288.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=42.77 liquidity=10404110.0 spike=0.43
- ABUK.CA: score=20.04 buy_ready=False sector_rank=10 price=90.01 support=75.76 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=50.99 liquidity=58528936.0 spike=0.31
- ACAMD.CA: score=13.1 buy_ready=False sector_rank=17 price=1.94 support=1.98 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=53388860.0 spike=1.08
- ACGC.CA: score=17.67 buy_ready=False sector_rank=11 price=13.94 support=13.65 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=47.73 liquidity=14426656.0 spike=0.54
- ADCI.CA: score=5.07 buy_ready=False sector_rank=17 price=280.89 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=39.13 liquidity=1133886.75 spike=0.24
- ADIB.CA: score=15.08 buy_ready=False sector_rank=9 price=50.42 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=44.69 liquidity=54395340.0 spike=0.67
- ADPC.CA: score=15.94 buy_ready=False sector_rank=17 price=3.82 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=12521859.0 spike=0.69
- AFDI.CA: score=8.87 buy_ready=False sector_rank=17 price=52.1 support=51.6 resistance=61.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=35.11 liquidity=4933414.5 spike=0.26
- AFMC.CA: score=11.54 buy_ready=False sector_rank=17 price=152.28 support=153.0 resistance=221.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=42.5 liquidity=7608445.0 spike=0.13
- AJWA.CA: score=13.94 buy_ready=False sector_rank=17 price=179.12 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=32193018.0 spike=0.74
- ALCN.CA: score=25.4 buy_ready=False sector_rank=4 price=33.05 support=30.05 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=20702964.0 spike=0.56
- ALUM.CA: score=2.25 buy_ready=False sector_rank=17 price=24.0 support=24.44 resistance=30.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=27.76 liquidity=3318472.5 spike=0.39
- AMER.CA: score=13.28 buy_ready=False sector_rank=20 price=4.93 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=38.18 liquidity=25467126.0 spike=0.46
- AMES.CA: score=7.94 buy_ready=False sector_rank=17 price=47.9 support=48.45 resistance=150.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=12.0 liquidity=31572002.0 spike=0.12
- AMIA.CA: score=8.35 buy_ready=False sector_rank=17 price=18.25 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=33.61 liquidity=6415407.5 spike=0.18
- AMOC.CA: score=18.89 buy_ready=False sector_rank=6 price=13.13 support=10.91 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=72279256.0 spike=0.42
- APSW.CA: score=3.37 buy_ready=False sector_rank=17 price=8.32 support=8.2 resistance=8.79 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=42.86 liquidity=430376.94 spike=0.54
- ARAB.CA: score=7.28 buy_ready=False sector_rank=20 price=0.22 support=0.23 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=42257636.0 spike=0.44
- ARCC.CA: score=7.4 buy_ready=False sector_rank=21 price=66.64 support=68.05 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=19.44 liquidity=13606433.0 spike=0.44
- AREH.CA: score=7.26 buy_ready=False sector_rank=17 price=1.38 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=37.04 liquidity=3324925.75 spike=0.24
- ASCM.CA: score=8.94 buy_ready=False sector_rank=17 price=57.68 support=57.36 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=26.89 liquidity=14675792.0 spike=0.8
- ASPI.CA: score=3.94 buy_ready=False sector_rank=17 price=0.38 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=31241816.0 spike=0.49
- ATLC.CA: score=11.24 buy_ready=False sector_rank=15 price=6.62 support=5.41 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=48.28 liquidity=3963582.25 spike=0.14
- ATQA.CA: score=18.04 buy_ready=False sector_rank=10 price=12.25 support=11.56 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=59.89 liquidity=32441878.0 spike=0.3
- AXPH.CA: score=13.76 buy_ready=False sector_rank=17 price=1636.21 support=1620.0 resistance=1750.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=45.73 liquidity=6823430.0 spike=0.74
- BINV.CA: score=22.4 buy_ready=False sector_rank=3 price=55.23 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=67.33 liquidity=11088035.0 spike=0.44
- BIOC.CA: score=8.94 buy_ready=False sector_rank=17 price=252.82 support=247.03 resistance=453.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=18.56 liquidity=11239556.0 spike=0.12
- BTFH.CA: score=8.68 buy_ready=False sector_rank=15 price=2.81 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=34.04 liquidity=98575920.0 spike=1.2
- CAED.CA: score=-1.78 buy_ready=False sector_rank=17 price=113.1 support=112.01 resistance=123.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4287146.5 spike=0.21
- CANA.CA: score=16.05 buy_ready=False sector_rank=9 price=45.36 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=64.41 liquidity=3966350.75 spike=0.17
- CCAP.CA: score=19.4 buy_ready=False sector_rank=3 price=7.07 support=5.74 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=75.96 liquidity=725924032.0 spike=0.87
- CCRS.CA: score=9.25 buy_ready=False sector_rank=17 price=2.49 support=2.4 resistance=2.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=47.75 liquidity=5315889.0 spike=0.17
- CEFM.CA: score=8.52 buy_ready=False sector_rank=17 price=140.94 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=44.9 liquidity=1582363.63 spike=0.18
- CERA.CA: score=13.94 buy_ready=False sector_rank=17 price=1.29 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=42.72 liquidity=54276476.0 spike=0.42
- CFGH.CA: score=1.94 buy_ready=False sector_rank=17 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=21.43 liquidity=5336.81 spike=0.32
- CICH.CA: score=10.3 buy_ready=False sector_rank=15 price=12.06 support=11.51 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=63.43 liquidity=1017468.19 spike=0.17
- CIEB.CA: score=11.14 buy_ready=False sector_rank=9 price=24.2 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=6061012.0 spike=0.44
- CIRA.CA: score=21.4 buy_ready=False sector_rank=5 price=38.97 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=68.01 liquidity=12503377.0 spike=0.32
- CLHO.CA: score=8.61 buy_ready=False sector_rank=19 price=15.44 support=15.4 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=15.07 liquidity=19091638.0 spike=0.28
- CNFN.CA: score=4.11 buy_ready=False sector_rank=15 price=4.31 support=4.32 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=29.89 liquidity=5831444.0 spike=0.52
- COMI.CA: score=9.08 buy_ready=False sector_rank=9 price=126.98 support=128.1 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=17.88 liquidity=334469344.0 spike=0.53
- COPR.CA: score=16.94 buy_ready=False sector_rank=17 price=0.47 support=0.46 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=14945163.0 spike=0.38
- COSG.CA: score=8.94 buy_ready=False sector_rank=17 price=1.64 support=1.71 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=21.95 liquidity=14992790.0 spike=0.5
- CPCI.CA: score=11.43 buy_ready=False sector_rank=17 price=558.71 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=69.3 liquidity=2495199.5 spike=0.78
- CSAG.CA: score=3.63 buy_ready=False sector_rank=4 price=37.52 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=30.39 liquidity=2229224.75 spike=0.15
- DAPH.CA: score=3.94 buy_ready=False sector_rank=17 price=102.85 support=102.0 resistance=110.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=21041062.0 spike=0.36
- DEIN.CA: score=6.94 buy_ready=False sector_rank=17 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=0.73 buy_ready=False sector_rank=16 price=25.61 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=29.15 liquidity=2721792.25 spike=0.51
- DSCW.CA: score=7.94 buy_ready=False sector_rank=17 price=1.72 support=1.77 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=18.52 liquidity=13638600.0 spike=0.59
- DTPP.CA: score=18.94 buy_ready=False sector_rank=17 price=323.06 support=296.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=56.97 liquidity=54526968.0 spike=0.66
- EALR.CA: score=6.29 buy_ready=False sector_rank=17 price=350.22 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=40.95 liquidity=3352974.5 spike=0.25
- EASB.CA: score=7.13 buy_ready=False sector_rank=17 price=7.51 support=7.13 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=3193588.5 spike=0.2
- EAST.CA: score=8.0 buy_ready=False sector_rank=16 price=30.62 support=31.31 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=6.67 liquidity=34144904.0 spike=0.57
- EBSC.CA: score=5.49 buy_ready=False sector_rank=17 price=1.92 support=1.95 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=38.03 liquidity=1556769.63 spike=0.13
- ECAP.CA: score=4.17 buy_ready=False sector_rank=17 price=31.14 support=31.16 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=29.46 liquidity=5234878.5 spike=0.56
- EDFM.CA: score=-0.55 buy_ready=False sector_rank=17 price=387.64 support=389.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=30.27 liquidity=511210.09 spike=0.29
- EEII.CA: score=14.94 buy_ready=False sector_rank=17 price=2.22 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=12411871.0 spike=0.85
- EFIC.CA: score=14.04 buy_ready=False sector_rank=10 price=177.59 support=183.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=44.01 liquidity=29882524.0 spike=0.09
- EFID.CA: score=14.0 buy_ready=False sector_rank=16 price=28.83 support=29.71 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=37791856.0 spike=0.56
- EFIH.CA: score=14.28 buy_ready=False sector_rank=13 price=22.81 support=22.16 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=48.16 liquidity=34384092.0 spike=0.59
- EGAL.CA: score=18.04 buy_ready=False sector_rank=10 price=343.1 support=351.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=39.03 liquidity=36020052.0 spike=0.42
- EGAS.CA: score=6.53 buy_ready=False sector_rank=6 price=54.2 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=34.13 liquidity=5635012.0 spike=0.47
- EGBE.CA: score=13.72 buy_ready=False sector_rank=9 price=0.52 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=638162.69 spike=8.62
- EGCH.CA: score=13.2 buy_ready=False sector_rank=10 price=13.9 support=13.51 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=132463632.0 spike=1.08
- EGSA.CA: score=13.4 buy_ready=False sector_rank=2 price=9.0 support=8.69 resistance=9.1 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=36.84 liquidity=1044.0 spike=0.16
- EGTS.CA: score=21.82 buy_ready=False sector_rank=20 price=17.84 support=16.51 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=62.9 liquidity=54362252.0 spike=1.77
- EHDR.CA: score=8.94 buy_ready=False sector_rank=17 price=2.51 support=2.6 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=29.41 liquidity=13308445.0 spike=0.79
- ELEC.CA: score=8.28 buy_ready=False sector_rank=14 price=1.92 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=42850592.0 spike=0.55
- ELKA.CA: score=8.94 buy_ready=False sector_rank=17 price=1.57 support=1.64 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=15.62 liquidity=15571662.0 spike=0.44
- ELNA.CA: score=-2.02 buy_ready=False sector_rank=17 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=25.47 liquidity=42052.68 spike=0.11
- ELSH.CA: score=7.61 buy_ready=False sector_rank=17 price=12.09 support=12.06 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=31.18 liquidity=8674187.0 spike=0.24
- ELWA.CA: score=-1.03 buy_ready=False sector_rank=17 price=1.69 support=1.64 resistance=1.99 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=32.14 liquidity=32676.15 spike=0.02
- EMFD.CA: score=16.28 buy_ready=False sector_rank=20 price=13.11 support=12.17 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=35.57 liquidity=48727588.0 spike=0.31
- ENGC.CA: score=13.94 buy_ready=False sector_rank=17 price=39.92 support=41.0 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=12680323.0 spike=0.72
- EOSB.CA: score=8.94 buy_ready=False sector_rank=17 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=83.21 spike=0.0
- EPCO.CA: score=6.44 buy_ready=False sector_rank=17 price=10.44 support=10.6 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=43.35 liquidity=2503045.75 spike=0.17
- EPPK.CA: score=-5.64 buy_ready=False sector_rank=17 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=22.4 buy_ready=False sector_rank=2 price=131.99 support=112.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=86.89 liquidity=93641176.0 spike=0.33
- ETRS.CA: score=3.77 buy_ready=False sector_rank=17 price=10.51 support=10.6 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=31.78 liquidity=4829004.0 spike=0.38
- EXPA.CA: score=22.08 buy_ready=False sector_rank=9 price=21.3 support=19.96 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=53.15 liquidity=20180634.0 spike=0.57
- FAIT.CA: score=9.86 buy_ready=False sector_rank=9 price=45.86 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=1776504.63 spike=0.22
- FAITA.CA: score=4.09 buy_ready=False sector_rank=9 price=0.98 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=36.84 liquidity=9943.41 spike=0.21
- FERC.CA: score=6.27 buy_ready=False sector_rank=10 price=77.37 support=77.3 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=37.89 liquidity=2227397.75 spike=0.16
- FWRY.CA: score=14.28 buy_ready=False sector_rank=13 price=18.57 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=47.09 liquidity=77136728.0 spike=0.6
- GBCO.CA: score=19.15 buy_ready=False sector_rank=8 price=30.2 support=28.04 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=62.85 liquidity=61216324.0 spike=0.85
- GDWA.CA: score=7.94 buy_ready=False sector_rank=17 price=0.71 support=0.74 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=12.8 liquidity=26512812.0 spike=0.61
- GGCC.CA: score=2.21 buy_ready=False sector_rank=17 price=0.74 support=0.7 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8278247.0 spike=0.25
- GIHD.CA: score=22.76 buy_ready=False sector_rank=17 price=76.57 support=63.1 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=54.91 liquidity=76893120.0 spike=2.91
- GMCI.CA: score=0.17 buy_ready=False sector_rank=17 price=1.71 support=1.69 resistance=1.94 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=22.22 liquidity=813700.1 spike=1.71
- GRCA.CA: score=3.68 buy_ready=False sector_rank=17 price=38.83 support=38.7 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=17.32 liquidity=5741269.5 spike=0.12
- GSSC.CA: score=7.92 buy_ready=False sector_rank=17 price=289.83 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=48.13 liquidity=985868.5 spike=0.12
- GTWL.CA: score=3.94 buy_ready=False sector_rank=17 price=217.98 support=216.4 resistance=228.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=86895712.0 spike=0.53
- HDBK.CA: score=17.08 buy_ready=False sector_rank=9 price=107.86 support=95.51 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=41.13 liquidity=20954964.0 spike=0.35
- HELI.CA: score=13.28 buy_ready=False sector_rank=20 price=7.73 support=7.64 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=43.56 liquidity=52165632.0 spike=0.3
- HRHO.CA: score=8.28 buy_ready=False sector_rank=15 price=23.99 support=24.4 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=23.05 liquidity=51002076.0 spike=0.52
- ICID.CA: score=9.51 buy_ready=False sector_rank=17 price=16.55 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=35.83 liquidity=2575627.0 spike=0.24
- IDRE.CA: score=9.62 buy_ready=False sector_rank=17 price=51.99 support=51.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=5686409.0 spike=0.34
- IFAP.CA: score=11.45 buy_ready=False sector_rank=7 price=20.0 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=36.61 liquidity=5798909.0 spike=0.28
- INFI.CA: score=9.96 buy_ready=False sector_rank=17 price=124.2 support=122.0 resistance=161.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=17.97 liquidity=26980960.0 spike=1.51
- IRON.CA: score=4.76 buy_ready=False sector_rank=10 price=27.17 support=26.3 resistance=31.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=32.89 liquidity=5712239.0 spike=0.41
- ISMA.CA: score=-0.83 buy_ready=False sector_rank=17 price=28.28 support=27.7 resistance=29.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5236232.0 spike=0.25
- ISMQ.CA: score=10.04 buy_ready=False sector_rank=10 price=8.39 support=8.53 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=22.88 liquidity=10391720.0 spike=0.42
- ISPH.CA: score=8.61 buy_ready=False sector_rank=19 price=11.66 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=27.13 liquidity=53266784.0 spike=0.79
- JUFO.CA: score=13.48 buy_ready=False sector_rank=16 price=25.59 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=39.93 liquidity=25911854.0 spike=1.24
- KABO.CA: score=17.67 buy_ready=False sector_rank=11 price=8.95 support=9.0 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=46.34 liquidity=16555746.0 spike=0.41
- KWIN.CA: score=5.95 buy_ready=False sector_rank=17 price=86.98 support=82.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=25.27 liquidity=7017847.0 spike=0.17
- KZPC.CA: score=15.6 buy_ready=False sector_rank=17 price=13.4 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=60.53 liquidity=8665145.0 spike=0.27
- LCSW.CA: score=3.24 buy_ready=False sector_rank=21 price=31.4 support=31.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=28.77 liquidity=5837322.0 spike=0.24
- LUTS.CA: score=13.94 buy_ready=False sector_rank=17 price=0.84 support=0.83 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=49.46 liquidity=24292474.0 spike=0.17
- MAAL.CA: score=27.94 buy_ready=False sector_rank=17 price=10.33 support=8.18 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=54.22 liquidity=76528504.0 spike=5.25
- MASR.CA: score=13.94 buy_ready=False sector_rank=17 price=7.41 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=42.04 liquidity=35047484.0 spike=0.36
- MBSC.CA: score=7.4 buy_ready=False sector_rank=21 price=325.1 support=333.33 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=24.82 liquidity=26939130.0 spike=0.6
- MCQE.CA: score=4.96 buy_ready=False sector_rank=21 price=199.08 support=200.0 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=16.4 liquidity=7560269.0 spike=0.3
- MCRO.CA: score=16.94 buy_ready=False sector_rank=17 price=1.56 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=59.26 liquidity=22088580.0 spike=0.18
- MENA.CA: score=0.44 buy_ready=False sector_rank=20 price=6.55 support=6.56 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=32.69 liquidity=1848420.63 spike=1.16
- MEPA.CA: score=13.94 buy_ready=False sector_rank=17 price=1.78 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=48.15 liquidity=12667810.0 spike=0.32
- MFPC.CA: score=20.04 buy_ready=False sector_rank=10 price=46.8 support=39.34 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=55.57 liquidity=33017888.0 spike=0.19
- MFSC.CA: score=10.22 buy_ready=False sector_rank=17 price=50.3 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=44.18 liquidity=1288921.75 spike=0.27
- MHOT.CA: score=29.06 buy_ready=False sector_rank=1 price=19.0 support=16.61 resistance=19.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=56.6 liquidity=20521502.0 spike=1.83
- MICH.CA: score=7.7 buy_ready=False sector_rank=17 price=46.58 support=46.03 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=27.96 liquidity=8765137.0 spike=0.65
- MILS.CA: score=7.07 buy_ready=False sector_rank=17 price=183.08 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=3133478.75 spike=0.15
- MIPH.CA: score=12.5 buy_ready=False sector_rank=19 price=800.0 support=700.2 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=57.77 liquidity=3884815.25 spike=0.42
- MOED.CA: score=7.94 buy_ready=False sector_rank=17 price=0.7 support=0.7 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=20.67 liquidity=13613098.0 spike=0.2
- MOIL.CA: score=14.71 buy_ready=False sector_rank=6 price=0.71 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=72.13 liquidity=413482.31 spike=1.7
- MOIN.CA: score=10.67 buy_ready=False sector_rank=17 price=34.45 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=45.45 liquidity=3735479.5 spike=0.12
- MOSC.CA: score=0.77 buy_ready=False sector_rank=17 price=288.04 support=290.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=20.29 liquidity=1833375.75 spike=0.32
- MPCI.CA: score=11.94 buy_ready=False sector_rank=17 price=373.42 support=371.11 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=28.09 liquidity=31807336.0 spike=0.23
- MPCO.CA: score=22.65 buy_ready=False sector_rank=7 price=2.54 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=88248136.0 spike=0.51
- MPRC.CA: score=6.02 buy_ready=False sector_rank=17 price=38.5 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=28.88 liquidity=7081553.5 spike=0.18
- MTIE.CA: score=9.15 buy_ready=False sector_rank=8 price=8.16 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=24.77 liquidity=12197175.0 spike=0.48
- NAHO.CA: score=-6.03 buy_ready=False sector_rank=17 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:37 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=38708.33 spike=0.66
- NCCW.CA: score=20.94 buy_ready=False sector_rank=17 price=7.3 support=5.77 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=64.66 liquidity=38003232.0 spike=0.52
- NEDA.CA: score=3.99 buy_ready=False sector_rank=17 price=2.75 support=2.7 resistance=2.89 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=51.52 liquidity=53377.5 spike=0.06
- NHPS.CA: score=15.28 buy_ready=False sector_rank=17 price=77.98 support=72.52 resistance=92.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=25984864.0 spike=1.67
- NINH.CA: score=8.94 buy_ready=False sector_rank=17 price=19.71 support=20.13 resistance=24.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=25.07 liquidity=10973111.0 spike=0.55
- NIPH.CA: score=3.61 buy_ready=False sector_rank=19 price=315.38 support=315.01 resistance=334.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=75855456.0 spike=0.5
- OBRI.CA: score=6.38 buy_ready=False sector_rank=17 price=28.7 support=29.51 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=16.72 liquidity=8446255.0 spike=0.56
- OCDI.CA: score=8.28 buy_ready=False sector_rank=20 price=27.7 support=28.0 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=16.71 liquidity=50652596.0 spike=0.68
- OCPH.CA: score=6.7 buy_ready=False sector_rank=17 price=228.21 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=36.19 liquidity=1762886.25 spike=0.28
- ODIN.CA: score=2.06 buy_ready=False sector_rank=17 price=2.58 support=2.54 resistance=2.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8120401.0 spike=0.41
- OFH.CA: score=7.04 buy_ready=False sector_rank=17 price=0.99 support=0.98 resistance=1.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=350218624.0 spike=2.55
- OIH.CA: score=18.84 buy_ready=False sector_rank=3 price=2.09 support=1.98 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=76.0 liquidity=209649632.0 spike=1.72
- OLFI.CA: score=14.31 buy_ready=False sector_rank=16 price=22.3 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=54.4 liquidity=8306666.5 spike=0.47
- ORAS.CA: score=4.6 buy_ready=False sector_rank=12 price=814.69 support=811.1 resistance=835.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=107712448.0 spike=1.0
- ORHD.CA: score=13.28 buy_ready=False sector_rank=20 price=39.38 support=40.5 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=36.34 liquidity=121995664.0 spike=0.75
- ORWE.CA: score=17.71 buy_ready=False sector_rank=11 price=27.01 support=25.6 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=54.21 liquidity=55722092.0 spike=1.02
- PHAR.CA: score=8.61 buy_ready=False sector_rank=19 price=109.06 support=111.55 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=19.91 liquidity=38954824.0 spike=0.41
- PHDC.CA: score=8.28 buy_ready=False sector_rank=20 price=12.9 support=12.91 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=18.92 liquidity=44463092.0 spike=0.29
- PHTV.CA: score=4.66 buy_ready=False sector_rank=17 price=336.95 support=311.27 resistance=378.89 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=36.3 liquidity=719051.33 spike=0.46
- POUL.CA: score=11.56 buy_ready=False sector_rank=16 price=38.55 support=37.15 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=21 September 01:28 PM market time freshness=DELAYED_CURRENT RSI=32.25 liquidity=58845364.0 spike=2.28
- PRCL.CA: score=11.34 buy_ready=False sector_rank=21 price=30.5 support=30.52 resistance=34.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=47.47 liquidity=8937180.0 spike=0.52
- PRDC.CA: score=8.28 buy_ready=False sector_rank=20 price=7.23 support=7.3 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=12.38 liquidity=36061976.0 spike=0.65
- PRMH.CA: score=6.91 buy_ready=False sector_rank=17 price=2.5 support=2.43 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:12 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=2976788.75 spike=0.39
- RACC.CA: score=7.45 buy_ready=False sector_rank=17 price=9.28 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=44.64 liquidity=3518951.75 spike=0.21
- RAKT.CA: score=3.02 buy_ready=False sector_rank=17 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-22T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=80724.48 spike=0.38
- RAYA.CA: score=8.77 buy_ready=False sector_rank=18 price=6.92 support=6.8 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=27.27 liquidity=20456722.0 spike=0.38
- RMDA.CA: score=13.61 buy_ready=False sector_rank=19 price=5.73 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=44.85 liquidity=27713628.0 spike=0.48
- ROTO.CA: score=1.55 buy_ready=False sector_rank=17 price=38.62 support=35.02 resistance=45.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=33.66 liquidity=2613484.25 spike=0.36
- RREI.CA: score=10.09 buy_ready=False sector_rank=17 price=3.93 support=4.05 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=36.63 liquidity=6155297.5 spike=0.38
- RTVC.CA: score=-0.68 buy_ready=False sector_rank=17 price=3.78 support=3.79 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=29.82 liquidity=1379619.5 spike=0.38
- RUBX.CA: score=25.94 buy_ready=False sector_rank=17 price=16.39 support=12.42 resistance=17.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=70.14 liquidity=211302336.0 spike=4.61
- SAUD.CA: score=5.08 buy_ready=False sector_rank=9 price=23.03 support=22.85 resistance=24.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19151650.0 spike=0.99
- SCEM.CA: score=7.4 buy_ready=False sector_rank=21 price=83.96 support=83.9 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=19.63 liquidity=21497036.0 spike=0.23
- SCFM.CA: score=5.27 buy_ready=False sector_rank=17 price=258.88 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=40.47 liquidity=1337243.0 spike=0.19
- SCTS.CA: score=2.34 buy_ready=False sector_rank=5 price=570.97 support=566.66 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=29.48 liquidity=938221.88 spike=0.38
- SDTI.CA: score=16.76 buy_ready=False sector_rank=17 price=77.44 support=68.57 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=71.04 liquidity=7822430.0 spike=0.32
- SEIG.CA: score=-0.38 buy_ready=False sector_rank=17 price=226.51 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=31.27 liquidity=686173.19 spike=0.36
- SIPC.CA: score=16.94 buy_ready=False sector_rank=17 price=5.17 support=4.77 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=51.5 liquidity=11787385.0 spike=0.17
- SKPC.CA: score=9.04 buy_ready=False sector_rank=10 price=16.99 support=17.16 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=31.19 liquidity=91387936.0 spike=0.69
- SMFR.CA: score=1.7 buy_ready=False sector_rank=17 price=220.32 support=226.1 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=27.35 liquidity=2766731.5 spike=0.36
- SNFC.CA: score=17.41 buy_ready=False sector_rank=17 price=11.48 support=10.26 resistance=11.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=79.49 liquidity=9478468.0 spike=0.66
- SPIN.CA: score=2.18 buy_ready=False sector_rank=11 price=16.75 support=16.1 resistance=20.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=27.94 liquidity=2504246.0 spike=0.18
- SPMD.CA: score=12.28 buy_ready=False sector_rank=17 price=0.4 support=0.4 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=8345986.5 spike=0.11
- SUGR.CA: score=14.03 buy_ready=False sector_rank=16 price=57.08 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=7027692.0 spike=0.19
- SVCE.CA: score=11.94 buy_ready=False sector_rank=17 price=10.81 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=29.25 liquidity=22517666.0 spike=0.12
- SWDY.CA: score=4.28 buy_ready=False sector_rank=14 price=116.81 support=116.5 resistance=124.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50422680.0 spike=0.88
- TALM.CA: score=23.4 buy_ready=False sector_rank=5 price=20.05 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=64.22 liquidity=22031840.0 spike=0.33
- TMGH.CA: score=8.28 buy_ready=False sector_rank=20 price=91.26 support=92.56 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=31.88 liquidity=164522608.0 spike=0.58
- TRTO.CA: score=-6.06 buy_ready=False sector_rank=17 price=0.05 support=0.05 resistance=0.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8494.17 spike=0.29
- UEFM.CA: score=-0.59 buy_ready=False sector_rank=17 price=469.55 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=30.06 liquidity=1474998.38 spike=0.48
- UEGC.CA: score=3.94 buy_ready=False sector_rank=17 price=1.52 support=1.51 resistance=1.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26132894.0 spike=0.5
- UNIP.CA: score=8.97 buy_ready=False sector_rank=17 price=0.36 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=5032673.0 spike=0.23
- UNIT.CA: score=4.8 buy_ready=False sector_rank=20 price=17.14 support=17.12 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=47.33 liquidity=1524361.5 spike=0.11
- WCDF.CA: score=8.71 buy_ready=False sector_rank=17 price=680.68 support=640.0 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=1778350.0 spike=0.34
- WKOL.CA: score=8.0 buy_ready=False sector_rank=17 price=321.62 support=325.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:15 PM market time freshness=DELAYED_CURRENT RSI=42.95 liquidity=4068838.5 spike=0.3
- ZEOT.CA: score=2.97 buy_ready=False sector_rank=17 price=12.26 support=12.6 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=28.18 liquidity=4033204.25 spike=0.66
- ZMID.CA: score=8.28 buy_ready=False sector_rank=20 price=8.0 support=8.07 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:13 PM market time freshness=DELAYED_CURRENT RSI=28.98 liquidity=56004524.0 spike=0.26

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
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- GIHD.CA: status=OLD_ACCEPTED latest=2016-01-01 age_days=3919 sources=3 expected=Gharbia Islamic Housing Development Company summary=Gharbia Islamic Housing to discuss raising capital mid-December; Gharbia Islamic Housing to distribute EGP 0.2/shr; Gharbia Islamic Housing profits fall 46% in 2016
  - Gharbia Islamic Housing to discuss raising capital mid-December: https://english.mubasher.info/news/3147599/Gharbia-Islamic-Housing-to-discuss-raising-capital-mid-December/
  - Gharbia Islamic Housing to distribute EGP 0.2/shr: https://english.mubasher.info/news/3082262/Gharbia-Islamic-Housing-to-distribute-EGP-0-2-shr/
  - Gharbia Islamic Housing profits fall 46% in 2016: https://english.mubasher.info/news/3068305/Gharbia-Islamic-Housing-profits-fall-46-in-2016/
- MPCO.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=631 sources=3 expected=Mansoura Poultry summary=Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m; Mansoura Poultry’s stock rebounds from key support level; Mansoura Poultry stock witnesses clear emergence of buying power
  - Mansoura Poultry’s consolidated net profits drop in 2025; revenues near EGP 857m: https://english.mubasher.info/news/4596342/Mansoura-Poultry-s-consolidated-net-profits-drop-in-2025-revenues-near-EGP-857m/
  - Mansoura Poultry’s stock rebounds from key support level: https://english.mubasher.info/news/4554482/Mansoura-Poultry-s-stock-rebounds-from-key-support-level/
  - Mansoura Poultry stock witnesses clear emergence of buying power: https://english.mubasher.info/news/4539119/Mansoura-Poultry-stock-witnesses-clear-emergence-of-buying-power/
- BINV.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=B Investments Holding summary=Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.

## Warnings
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for MAAL.CA: source text did not clearly match MAAL.CA / Marseille Almasreia Alkhalegeya For Holding Investment SAE.
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence for GIHD.CA matches the company but appears old; latest detected date is 2016-01-01.
- Evidence for MPCO.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for BINV.CA: source text did not clearly match BINV.CA / B Investments Holding.
