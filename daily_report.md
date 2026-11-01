# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-11-01T18:03:51.863100+00:00
Generated Cairo: 2026-11-01 20:03
Run timing: target 15:30 Cairo | generated Cairo 2026-11-01 20:03 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-11-01 20:00

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 5
- Tradeable price/liquidity tickers: 173/185
- Top sector: Building Materials

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, November 01
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.53% / above MA50 0.0%
- EGX70 regime: BEARISH / above MA20 8.11% / above MA50 5.41%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- AMOC.CA: liquidity=565547584.0 spike=4.25 score=24.34
- COMI.CA: liquidity=428923648.0 spike=0.84 score=13.88
- CCAP.CA: liquidity=378095296.0 spike=0.78 score=12.49
- TMGH.CA: liquidity=247620848.0 spike=0.96 score=12.45
- ORAS.CA: liquidity=173631232.0 spike=1.0 score=4.6

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- MENA.CA: spike=12.39 liquidity=33222170.0 outlook=WEAK_OR_RISKY score=23 buy_ready=False
- SEIG.CA: spike=10.14 liquidity=24300130.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- AMOC.CA: spike=4.25 liquidity=565547584.0 outlook=BULLISH_WATCH score=81.86 buy_ready=False
- ELNA.CA: spike=3.36 liquidity=1754081.0 outlook=NEUTRAL score=48 buy_ready=False
- ISPH.CA: spike=3.02 liquidity=135866752.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=2.78 5d=-0.62% 20d=3.54% aboveMA50=16.67%
- #2 Tourism & Leisure: score=2.73 5d=4.37% 20d=-2.5% aboveMA50=0.0%
- #3 Fintech & Payments: score=2.54 5d=2.18% 20d=-1.99% aboveMA50=0.0%
- #4 Banking & Financials: score=2.19 5d=0.09% 20d=-4.33% aboveMA50=20.0%
- #5 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #6 Energy & Petrochemicals: score=0.86 5d=-1.81% 20d=-7.8% aboveMA50=33.33%
- #7 Healthcare: score=0.43 5d=0.85% 20d=-6.88% aboveMA50=0.0%
- #8 Food, Beverages & Tobacco: score=0.07 5d=-1.14% 20d=-3.54% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CANA.CA: BULLISH_WATCH score=87.19 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=far above support
- AMOC.CA: BULLISH_WATCH score=81.86 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- LCSW.CA: BULLISH_WATCH score=80.78 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- CPCI.CA: BULLISH_WATCH score=72 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- AJWA.CA: BULLISH_WATCH score=70 liquidity=TRADEABLE sector=LAGGING risk=sector is not leading
- SCEM.CA: CONSTRUCTIVE score=65.78 liquidity=TRADEABLE sector=LEADING risk=below MA50
- ADIB.CA: CONSTRUCTIVE score=61.19 liquidity=TRADEABLE sector=IMPROVING risk=below MA50
- EFIH.CA: CONSTRUCTIVE score=59.54 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; below MA50
- SDTI.CA: CONSTRUCTIVE score=58 liquidity=TRADEABLE sector=LAGGING risk=below MA20; sector is not leading
- MPCI.CA: CONSTRUCTIVE score=56 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=below MA50; far above support; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- EDFM.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- GTWL.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=0.62 buy_ready=False sector_rank=16 price=215.84 support=171.02 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=34.68 liquidity=3328194.0 spike=0.36
- ABUK.CA: score=13.25 buy_ready=False sector_rank=17 price=85.0 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.35 liquidity=79937768.0 spike=0.95
- ACAMD.CA: score=12.29 buy_ready=False sector_rank=16 price=1.91 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=40858408.0 spike=0.93
- ACGC.CA: score=9.06 buy_ready=False sector_rank=11 price=12.88 support=11.6 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=5376798.0 spike=0.65
- ADCI.CA: score=14.4 buy_ready=False sector_rank=16 price=258.12 support=221.0 resistance=278.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=51.17 liquidity=5169637.0 spike=2.97
- ADIB.CA: score=19.06 buy_ready=False sector_rank=4 price=47.36 support=43.16 resistance=50.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.15 liquidity=82980032.0 spike=1.09
- ADPC.CA: score=4.08 buy_ready=False sector_rank=16 price=2.94 support=2.53 resistance=3.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=35.22 liquidity=1792047.0 spike=0.19
- AFDI.CA: score=1.62 buy_ready=False sector_rank=16 price=43.7 support=34.8 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=27.79 liquidity=3326120.75 spike=0.87
- AFMC.CA: score=13.99 buy_ready=False sector_rank=16 price=127.01 support=94.6 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.49 liquidity=25297572.0 spike=1.35
- AJWA.CA: score=18.35 buy_ready=False sector_rank=16 price=211.06 support=179.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=53.33 liquidity=35699552.0 spike=1.03
- ALCN.CA: score=8.69 buy_ready=False sector_rank=15 price=31.3 support=27.11 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=43.01 liquidity=5290946.5 spike=0.28
- ALUM.CA: score=0.98 buy_ready=False sector_rank=16 price=18.4 support=16.02 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=30.4 liquidity=3486478.25 spike=1.1
- AMER.CA: score=15.45 buy_ready=False sector_rank=14 price=4.24 support=3.21 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.6 liquidity=21368794.0 spike=0.38
- AMES.CA: score=9.29 buy_ready=False sector_rank=16 price=32.27 support=28.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=25.87 liquidity=19626354.0 spike=0.36
- AMIA.CA: score=8.09 buy_ready=False sector_rank=16 price=17.32 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.11 liquidity=4802305.0 spike=0.31
- AMOC.CA: score=24.34 buy_ready=False sector_rank=6 price=14.31 support=12.55 resistance=14.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=53.51 liquidity=565547584.0 spike=4.25
- APSW.CA: score=-2.38 buy_ready=False sector_rank=16 price=7.27 support=7.1 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:06 PM market time freshness=DELAYED_CURRENT RSI=27.17 liquidity=327169.47 spike=0.53
- ARAB.CA: score=8.45 buy_ready=False sector_rank=14 price=0.23 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.84 liquidity=105346928.0 spike=0.87
- ARCC.CA: score=18.11 buy_ready=False sector_rank=1 price=63.61 support=58.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=35.86 liquidity=19917510.0 spike=0.45
- AREH.CA: score=1.31 buy_ready=False sector_rank=16 price=1.04 support=0.91 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=34.55 liquidity=4013241.0 spike=0.51
- ASCM.CA: score=0.12 buy_ready=False sector_rank=16 price=43.31 support=38.2 resistance=59.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=27.14 liquidity=2825396.5 spike=0.34
- ASPI.CA: score=14.29 buy_ready=False sector_rank=16 price=0.3 support=0.27 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=37.43 liquidity=11856474.0 spike=0.62
- ATLC.CA: score=4.44 buy_ready=False sector_rank=18 price=4.93 support=3.93 resistance=6.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=2445632.25 spike=0.34
- ATQA.CA: score=7.25 buy_ready=False sector_rank=17 price=9.04 support=8.25 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=26.77 liquidity=27564780.0 spike=0.53
- AXPH.CA: score=10.85 buy_ready=False sector_rank=16 price=1340.07 support=1135.0 resistance=1550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=42.61 liquidity=5314248.0 spike=1.12
- BINV.CA: score=0.08 buy_ready=False sector_rank=20 price=51.62 support=51.0 resistance=63.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=31.17 liquidity=2595929.75 spike=0.21
- BIOC.CA: score=13.29 buy_ready=False sector_rank=16 price=278.83 support=212.05 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=46.24 liquidity=55092764.0 spike=0.52
- BTFH.CA: score=11.99 buy_ready=False sector_rank=18 price=2.31 support=2.05 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=83348336.0 spike=0.72
- CAED.CA: score=5.02 buy_ready=False sector_rank=16 price=87.04 support=64.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=34.07 liquidity=6729001.0 spike=0.71
- CANA.CA: score=26.2 buy_ready=False sector_rank=4 price=47.63 support=38.1 resistance=46.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=58.17 liquidity=39156004.0 spike=2.16
- CCAP.CA: score=12.49 buy_ready=False sector_rank=20 price=5.94 support=5.8 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.4 liquidity=378095296.0 spike=0.78
- CCRS.CA: score=3.44 buy_ready=False sector_rank=16 price=1.69 support=1.3 resistance=2.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=28.23 liquidity=6143930.5 spike=0.92
- CEFM.CA: score=7.71 buy_ready=False sector_rank=16 price=113.4 support=97.79 resistance=140.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.4 liquidity=3518245.5 spike=1.45
- CERA.CA: score=7.29 buy_ready=False sector_rank=16 price=1.03 support=0.93 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=29.41 liquidity=45111472.0 spike=0.37
- CFGH.CA: score=-2.71 buy_ready=False sector_rank=16 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=10.0 liquidity=0.0 spike=0.0
- CICH.CA: score=-0.95 buy_ready=False sector_rank=18 price=10.71 support=9.63 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=32.64 liquidity=1893773.88 spike=1.08
- CIEB.CA: score=17.06 buy_ready=False sector_rank=4 price=22.64 support=21.35 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.3 liquidity=12515343.0 spike=1.59
- CIRA.CA: score=14.02 buy_ready=False sector_rank=9 price=36.01 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=43.83 liquidity=12120667.0 spike=0.76
- CLHO.CA: score=10.17 buy_ready=False sector_rank=7 price=13.38 support=12.51 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=29.36 liquidity=30869708.0 spike=0.83
- CNFN.CA: score=4.74 buy_ready=False sector_rank=18 price=3.69 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=38.5 liquidity=2750484.75 spike=0.3
- COMI.CA: score=13.88 buy_ready=False sector_rank=4 price=117.77 support=118.06 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.51 liquidity=428923648.0 spike=0.84
- COPR.CA: score=7.7 buy_ready=False sector_rank=16 price=0.4 support=0.33 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=31.47 liquidity=9411760.0 spike=0.59
- COSG.CA: score=3.74 buy_ready=False sector_rank=16 price=1.27 support=1.11 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=6445813.5 spike=0.61
- CPCI.CA: score=14.55 buy_ready=False sector_rank=16 price=600.05 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.06 liquidity=4255325.5 spike=0.82
- CSAG.CA: score=8.42 buy_ready=False sector_rank=15 price=33.49 support=30.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=5024902.0 spike=0.77
- DAPH.CA: score=7.29 buy_ready=False sector_rank=16 price=80.01 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=30.37 liquidity=16882908.0 spike=0.42
- DEIN.CA: score=6.29 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=6.73 buy_ready=False sector_rank=8 price=22.81 support=20.27 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=1703975.75 spike=0.58
- DSCW.CA: score=13.04 buy_ready=False sector_rank=16 price=1.47 support=1.23 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=8747472.0 spike=0.61
- DTPP.CA: score=5.17 buy_ready=False sector_rank=16 price=47.3 support=43.15 resistance=50.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=71377432.0 spike=1.94
- EALR.CA: score=-0.44 buy_ready=False sector_rank=16 price=258.55 support=236.01 resistance=355.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=25.33 liquidity=2271869.5 spike=0.72
- EASB.CA: score=3.45 buy_ready=False sector_rank=16 price=6.09 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.01 liquidity=5141207.5 spike=1.01
- EAST.CA: score=11.4 buy_ready=False sector_rank=8 price=31.52 support=27.01 resistance=32.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=74.08 liquidity=4369594.0 spike=0.1
- EBSC.CA: score=6.11 buy_ready=False sector_rank=16 price=1.43 support=1.2 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=1815960.88 spike=0.72
- ECAP.CA: score=-0.88 buy_ready=False sector_rank=16 price=26.17 support=24.8 resistance=31.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=31.17 liquidity=1825717.5 spike=0.55
- EEII.CA: score=6.19 buy_ready=False sector_rank=16 price=1.69 support=1.42 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=8373722.5 spike=1.26
- EFIC.CA: score=10.05 buy_ready=False sector_rank=17 price=137.74 support=121.0 resistance=178.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.17 liquidity=7804353.0 spike=0.35
- EFID.CA: score=15.03 buy_ready=False sector_rank=8 price=17.91 support=16.01 resistance=19.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=42.76 liquidity=24512266.0 spike=0.62
- EFIH.CA: score=18.04 buy_ready=False sector_rank=3 price=23.0 support=20.3 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=131427064.0 spike=2.01
- EGAL.CA: score=15.25 buy_ready=False sector_rank=17 price=303.43 support=275.0 resistance=359.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=35.16 liquidity=38998440.0 spike=0.4
- EGAS.CA: score=0.83 buy_ready=False sector_rank=6 price=46.89 support=43.0 resistance=58.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=31.66 liquidity=2484839.5 spike=0.57
- EGBE.CA: score=7.21 buy_ready=False sector_rank=4 price=0.51 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:24 PM market time freshness=DELAYED_CURRENT RSI=37.38 liquidity=214553.1 spike=2.06
- EGCH.CA: score=7.25 buy_ready=False sector_rank=17 price=10.2 support=10.0 resistance=13.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=25.61 liquidity=53443276.0 spike=0.98
- EGSA.CA: score=2.95 buy_ready=False sector_rank=19 price=8.81 support=8.75 resistance=9.09 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=46.05 liquidity=4405.0 spike=0.89
- EGTS.CA: score=8.41 buy_ready=False sector_rank=14 price=12.28 support=10.19 resistance=17.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=28.44 liquidity=29664406.0 spike=1.48
- EHDR.CA: score=0.8 buy_ready=False sector_rank=16 price=2.02 support=1.8 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=3509287.75 spike=0.39
- ELEC.CA: score=12.92 buy_ready=False sector_rank=10 price=1.5 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.54 liquidity=27935592.0 spike=0.56
- ELKA.CA: score=12.31 buy_ready=False sector_rank=16 price=1.41 support=1.21 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.71 liquidity=13588539.0 spike=1.01
- ELNA.CA: score=14.77 buy_ready=False sector_rank=16 price=39.66 support=33.46 resistance=39.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=1754081.0 spike=3.36
- ELSH.CA: score=10.01 buy_ready=False sector_rank=16 price=9.98 support=8.57 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=35.8 liquidity=7720617.5 spike=0.42
- ELWA.CA: score=1.59 buy_ready=False sector_rank=16 price=1.5 support=1.43 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:03 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=496513.5 spike=1.9
- EMFD.CA: score=13.45 buy_ready=False sector_rank=14 price=11.94 support=10.6 resistance=13.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=39.58 liquidity=28723720.0 spike=0.57
- ENGC.CA: score=12.42 buy_ready=False sector_rank=16 price=34.96 support=26.91 resistance=38.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=6132727.0 spike=0.59
- EOSB.CA: score=10.82 buy_ready=False sector_rank=16 price=1.61 support=1.56 resistance=1.72 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=170141.58 spike=2.18
- EPCO.CA: score=-0.31 buy_ready=False sector_rank=16 price=7.98 support=7.0 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=33.4 liquidity=2399670.0 spike=0.56
- EPPK.CA: score=-6.29 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=7.95 buy_ready=False sector_rank=19 price=118.0 support=115.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=28.61 liquidity=118281192.0 spike=0.45
- ETRS.CA: score=13.52 buy_ready=False sector_rank=16 price=10.42 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=46.99 liquidity=8232101.5 spike=0.62
- EXPA.CA: score=15.88 buy_ready=False sector_rank=4 price=14.0 support=12.0 resistance=16.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.33 liquidity=31838766.0 spike=0.94
- FAIT.CA: score=6.75 buy_ready=False sector_rank=4 price=43.51 support=40.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=45.78 liquidity=1877316.88 spike=0.68
- FAITA.CA: score=11.88 buy_ready=False sector_rank=4 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=54.46 liquidity=6663.33 spike=0.2
- FERC.CA: score=-1.3 buy_ready=False sector_rank=17 price=61.21 support=53.57 resistance=77.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=33.29 liquidity=1448019.5 spike=0.41
- FWRY.CA: score=10.02 buy_ready=False sector_rank=3 price=16.46 support=16.45 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=30.48 liquidity=94519992.0 spike=0.75
- GBCO.CA: score=4.1 buy_ready=False sector_rank=12 price=21.71 support=21.51 resistance=23.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=141925392.0 spike=1.21
- GDWA.CA: score=8.67 buy_ready=False sector_rank=16 price=0.55 support=0.48 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=35.05 liquidity=6380526.5 spike=0.48
- GGCC.CA: score=4.67 buy_ready=False sector_rank=16 price=0.52 support=0.52 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=28714970.0 spike=1.69
- GIHD.CA: score=6.31 buy_ready=False sector_rank=16 price=43.26 support=41.0 resistance=44.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33593120.0 spike=2.51
- GMCI.CA: score=-0.81 buy_ready=False sector_rank=16 price=1.39 support=1.41 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=438108.5 spike=1.73
- GRCA.CA: score=2.12 buy_ready=False sector_rank=16 price=26.16 support=22.57 resistance=39.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=25.12 liquidity=2826054.75 spike=0.57
- GSSC.CA: score=3.1 buy_ready=False sector_rank=16 price=255.37 support=211.52 resistance=290.0 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=38.74 liquidity=808501.4 spike=0.78
- HDBK.CA: score=14.12 buy_ready=False sector_rank=4 price=97.9 support=83.01 resistance=112.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=25140696.0 spike=1.12
- HELI.CA: score=13.45 buy_ready=False sector_rank=14 price=6.37 support=5.72 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.7 liquidity=43428120.0 spike=0.65
- HRHO.CA: score=6.99 buy_ready=False sector_rank=18 price=23.15 support=22.8 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=30.44 liquidity=26319474.0 spike=0.22
- ICID.CA: score=7.02 buy_ready=False sector_rank=16 price=17.41 support=14.26 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=48.79 liquidity=3729602.25 spike=0.53
- IDRE.CA: score=6.94 buy_ready=False sector_rank=16 price=37.65 support=29.11 resistance=52.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=32.11 liquidity=8567007.0 spike=1.54
- IFAP.CA: score=-0.49 buy_ready=False sector_rank=21 price=16.46 support=15.51 resistance=19.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=27.02 liquidity=3114777.5 spike=0.66
- INFI.CA: score=13.05 buy_ready=False sector_rank=16 price=113.17 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.84 liquidity=9762298.0 spike=0.47
- IRON.CA: score=4.15 buy_ready=False sector_rank=17 price=24.56 support=23.53 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=31.07 liquidity=6897638.0 spike=0.65
- ISMA.CA: score=2.38 buy_ready=False sector_rank=16 price=18.8 support=14.11 resistance=27.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.35 liquidity=5092128.0 spike=0.71
- ISMQ.CA: score=4.65 buy_ready=False sector_rank=17 price=7.22 support=6.55 resistance=7.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=25865206.0 spike=1.7
- ISPH.CA: score=8.21 buy_ready=False sector_rank=7 price=9.49 support=9.17 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=135866752.0 spike=3.02
- JUFO.CA: score=15.03 buy_ready=False sector_rank=8 price=22.52 support=21.01 resistance=26.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=10693299.0 spike=0.6
- KABO.CA: score=7.69 buy_ready=False sector_rank=11 price=6.8 support=5.58 resistance=9.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=30.21 liquidity=17711074.0 spike=0.79
- KWIN.CA: score=4.16 buy_ready=False sector_rank=16 price=54.48 support=44.02 resistance=82.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=28.75 liquidity=6168367.5 spike=1.35
- KZPC.CA: score=6.11 buy_ready=False sector_rank=16 price=12.65 support=11.56 resistance=13.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=2815877.25 spike=0.41
- LCSW.CA: score=27.11 buy_ready=False sector_rank=1 price=35.69 support=28.0 resistance=36.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.98 liquidity=16183157.0 spike=0.63
- LUTS.CA: score=5.99 buy_ready=False sector_rank=16 price=0.72 support=0.64 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=127488896.0 spike=2.35
- MAAL.CA: score=8.81 buy_ready=False sector_rank=16 price=6.92 support=4.88 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.26 liquidity=16291694.0 spike=1.26
- MASR.CA: score=13.29 buy_ready=False sector_rank=16 price=6.7 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.29 liquidity=30678482.0 spike=0.61
- MBSC.CA: score=13.11 buy_ready=False sector_rank=1 price=299.0 support=262.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=29.94 liquidity=33433098.0 spike=0.31
- MCQE.CA: score=19.11 buy_ready=False sector_rank=1 price=166.98 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=35.34 liquidity=34445664.0 spike=0.47
- MCRO.CA: score=12.29 buy_ready=False sector_rank=16 price=1.29 support=1.07 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=42658588.0 spike=0.92
- MENA.CA: score=12.45 buy_ready=False sector_rank=14 price=5.62 support=5.45 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.69 liquidity=33222170.0 spike=12.39
- MEPA.CA: score=8.09 buy_ready=False sector_rank=16 price=1.25 support=1.14 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=27.38 liquidity=18526478.0 spike=1.4
- MFPC.CA: score=13.25 buy_ready=False sector_rank=17 price=44.03 support=40.66 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.56 liquidity=34505612.0 spike=0.68
- MFSC.CA: score=-1.39 buy_ready=False sector_rank=16 price=32.63 support=28.55 resistance=47.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:02 PM market time freshness=DELAYED_CURRENT RSI=27.44 liquidity=1315564.75 spike=0.66
- MHOT.CA: score=13.48 buy_ready=False sector_rank=2 price=14.99 support=13.0 resistance=16.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=42.96 liquidity=7390488.5 spike=0.99
- MICH.CA: score=7.35 buy_ready=False sector_rank=16 price=40.59 support=35.5 resistance=44.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=43.58 liquidity=2060143.0 spike=0.33
- MILS.CA: score=3.76 buy_ready=False sector_rank=16 price=126.98 support=96.02 resistance=195.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=26.16 liquidity=6466747.5 spike=0.77
- MIPH.CA: score=4.7 buy_ready=False sector_rank=7 price=747.84 support=610.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=40.02 liquidity=526496.19 spike=0.15
- MOED.CA: score=7.29 buy_ready=False sector_rank=16 price=0.47 support=0.39 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=24.4 liquidity=11508841.0 spike=0.86
- MOIL.CA: score=4.5 buy_ready=False sector_rank=6 price=0.64 support=0.6 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=153399.0 spike=0.76
- MOIN.CA: score=3.08 buy_ready=False sector_rank=16 price=28.5 support=25.7 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=27.06 liquidity=4788159.0 spike=0.59
- MOSC.CA: score=3.32 buy_ready=False sector_rank=16 price=239.2 support=198.01 resistance=310.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=1030650.94 spike=0.27
- MPCI.CA: score=18.43 buy_ready=False sector_rank=16 price=319.04 support=238.6 resistance=369.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.35 liquidity=152603696.0 spike=1.57
- MPCO.CA: score=6.4 buy_ready=False sector_rank=21 price=1.76 support=1.55 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=33436516.0 spike=0.41
- MPRC.CA: score=8.51 buy_ready=False sector_rank=16 price=32.95 support=27.0 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=24149588.0 spike=1.61
- MTIE.CA: score=8.14 buy_ready=False sector_rank=12 price=6.94 support=6.05 resistance=8.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=38.9 liquidity=5457973.0 spike=0.27
- NAHO.CA: score=3.31 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=38.1 liquidity=16785.58 spike=0.97
- NCCW.CA: score=7.43 buy_ready=False sector_rank=16 price=5.23 support=4.05 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=30.68 liquidity=20212246.0 spike=1.07
- NEDA.CA: score=-0.65 buy_ready=False sector_rank=16 price=2.36 support=2.47 resistance=2.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:55 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=302282.84 spike=1.88
- NHPS.CA: score=1.54 buy_ready=False sector_rank=16 price=55.75 support=50.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=24.29 liquidity=4247478.5 spike=0.54
- NINH.CA: score=1.84 buy_ready=False sector_rank=16 price=14.88 support=12.36 resistance=20.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=28.97 liquidity=2548679.5 spike=0.25
- NIPH.CA: score=14.57 buy_ready=False sector_rank=7 price=282.05 support=205.0 resistance=341.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.43 liquidity=153238976.0 spike=1.2
- OBRI.CA: score=5.19 buy_ready=False sector_rank=16 price=23.1 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.07 liquidity=7895260.5 spike=0.54
- OCDI.CA: score=12.45 buy_ready=False sector_rank=14 price=22.82 support=21.0 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.61 liquidity=21993930.0 spike=0.62
- OCPH.CA: score=-0.82 buy_ready=False sector_rank=16 price=183.79 support=147.96 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=34.18 liquidity=1887035.0 spike=0.58
- ODIN.CA: score=9.69 buy_ready=False sector_rank=16 price=2.05 support=1.7 resistance=2.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=7060601.5 spike=1.17
- OFH.CA: score=8.29 buy_ready=False sector_rank=16 price=0.7 support=0.61 resistance=0.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=29.74 liquidity=18507222.0 spike=0.66
- OIH.CA: score=12.49 buy_ready=False sector_rank=20 price=1.65 support=1.5 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=10523827.0 spike=0.22
- OLFI.CA: score=2.1 buy_ready=False sector_rank=8 price=19.0 support=17.86 resistance=22.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=27.19 liquidity=4071576.75 spike=0.3
- ORAS.CA: score=4.6 buy_ready=False sector_rank=5 price=813.85 support=807.14 resistance=837.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=173631232.0 spike=1.0
- ORHD.CA: score=9.45 buy_ready=False sector_rank=14 price=9.69 support=8.5 resistance=12.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=31.29 liquidity=41001972.0 spike=0.35
- ORWE.CA: score=3.91 buy_ready=False sector_rank=11 price=24.78 support=23.34 resistance=25.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=41478116.0 spike=1.11
- PHAR.CA: score=14.41 buy_ready=False sector_rank=7 price=99.33 support=90.2 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=37.25 liquidity=61765132.0 spike=1.12
- PHDC.CA: score=4.41 buy_ready=False sector_rank=14 price=10.64 support=10.51 resistance=11.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=128784472.0 spike=1.48
- PHTV.CA: score=3.82 buy_ready=False sector_rank=16 price=316.85 support=300.0 resistance=360.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=35.46 liquidity=526352.0 spike=0.56
- POUL.CA: score=15.03 buy_ready=False sector_rank=8 price=9.44 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=30655622.0 spike=0.54
- PRCL.CA: score=21.89 buy_ready=False sector_rank=1 price=20.11 support=16.65 resistance=27.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.86 liquidity=24564896.0 spike=2.39
- PRDC.CA: score=13.74 buy_ready=False sector_rank=14 price=6.07 support=5.08 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.58 liquidity=9294245.0 spike=0.27
- PRMH.CA: score=8.27 buy_ready=False sector_rank=16 price=1.86 support=1.7 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.1 liquidity=3415302.25 spike=1.28
- RACC.CA: score=1.72 buy_ready=False sector_rank=16 price=7.24 support=6.1 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=4432276.5 spike=0.62
- RAKT.CA: score=0.6 buy_ready=False sector_rank=16 price=22.35 support=20.4 resistance=25.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=26.11 liquidity=307127.06 spike=0.71
- RAYA.CA: score=7.66 buy_ready=False sector_rank=13 price=5.33 support=5.02 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.86 liquidity=16685151.0 spike=0.83
- RMDA.CA: score=16.17 buy_ready=False sector_rank=7 price=5.05 support=4.5 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=49.05 liquidity=18901474.0 spike=0.79
- ROTO.CA: score=0.38 buy_ready=False sector_rank=16 price=29.93 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=24.78 liquidity=3086647.5 spike=0.38
- RREI.CA: score=8.73 buy_ready=False sector_rank=16 price=2.7 support=1.96 resistance=4.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=26.64 liquidity=17513064.0 spike=1.72
- RTVC.CA: score=-0.61 buy_ready=False sector_rank=16 price=2.8 support=2.77 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=16.81 liquidity=2102300.0 spike=0.75
- RUBX.CA: score=8.29 buy_ready=False sector_rank=16 price=12.84 support=10.51 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.72 liquidity=55777556.0 spike=0.66
- SAUD.CA: score=7.31 buy_ready=False sector_rank=4 price=20.5 support=19.3 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=32.72 liquidity=8434138.0 spike=0.74
- SCEM.CA: score=21.07 buy_ready=False sector_rank=1 price=85.97 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=87204632.0 spike=1.48
- SCFM.CA: score=8.69 buy_ready=False sector_rank=16 price=215.74 support=153.02 resistance=259.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=37.82 liquidity=4101812.5 spike=2.15
- SCTS.CA: score=10.21 buy_ready=False sector_rank=9 price=499.55 support=410.0 resistance=588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=43.61 liquidity=4115570.0 spike=1.04
- SDTI.CA: score=16.29 buy_ready=False sector_rank=16 price=83.0 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=40.42 liquidity=16188421.0 spike=0.94
- SEIG.CA: score=8.29 buy_ready=False sector_rank=16 price=223.68 support=192.0 resistance=223.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=24300130.0 spike=10.14
- SIPC.CA: score=13.29 buy_ready=False sector_rank=16 price=4.56 support=3.73 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.49 liquidity=22645248.0 spike=0.38
- SKPC.CA: score=14.25 buy_ready=False sector_rank=17 price=15.01 support=14.01 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.16 liquidity=28436002.0 spike=0.49
- SMFR.CA: score=-0.74 buy_ready=False sector_rank=16 price=183.23 support=165.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=27.55 liquidity=1969175.63 spike=0.66
- SNFC.CA: score=7.7 buy_ready=False sector_rank=16 price=10.74 support=10.08 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=37.45 liquidity=5404779.0 spike=0.69
- SPIN.CA: score=8.49 buy_ready=False sector_rank=11 price=13.83 support=12.0 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=36.83 liquidity=3803321.25 spike=0.74
- SPMD.CA: score=9.04 buy_ready=False sector_rank=16 price=0.34 support=0.3 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.45 liquidity=4752439.0 spike=0.32
- SUGR.CA: score=7.62 buy_ready=False sector_rank=8 price=48.58 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=44.41 liquidity=3593279.0 spike=0.4
- SVCE.CA: score=12.29 buy_ready=False sector_rank=16 price=8.5 support=7.01 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=35.17 liquidity=42704008.0 spike=0.65
- SWDY.CA: score=15.92 buy_ready=False sector_rank=10 price=110.41 support=97.0 resistance=124.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=49.55 liquidity=24267764.0 spike=0.43
- TALM.CA: score=9.02 buy_ready=False sector_rank=9 price=18.58 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=29.43 liquidity=12609477.0 spike=0.46
- TMGH.CA: score=12.45 buy_ready=False sector_rank=14 price=78.62 support=79.4 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.08 liquidity=247620848.0 spike=0.96
- TRTO.CA: score=-1.71 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-28T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=187.0 spike=0.03
- UEFM.CA: score=-0.98 buy_ready=False sector_rank=16 price=435.28 support=422.0 resistance=550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=23.52 liquidity=1731075.25 spike=0.81
- UEGC.CA: score=14.29 buy_ready=False sector_rank=16 price=1.4 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.22 liquidity=26883878.0 spike=0.58
- UNIP.CA: score=2.87 buy_ready=False sector_rank=16 price=0.29 support=0.25 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=31.79 liquidity=5580916.0 spike=0.7
- UNIT.CA: score=8.93 buy_ready=False sector_rank=14 price=17.76 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=51.89 liquidity=1483574.25 spike=0.47
- WCDF.CA: score=-2.02 buy_ready=False sector_rank=16 price=493.63 support=432.5 resistance=639.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=23.34 liquidity=683223.5 spike=0.34
- WKOL.CA: score=-0.11 buy_ready=False sector_rank=16 price=241.03 support=218.0 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=34.27 liquidity=2596778.0 spike=0.36
- ZEOT.CA: score=5.61 buy_ready=False sector_rank=16 price=10.55 support=8.0 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.08 liquidity=2313143.75 spike=0.29
- ZMID.CA: score=13.45 buy_ready=False sector_rank=14 price=6.52 support=5.91 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.51 liquidity=32865398.0 spike=0.48

## Backtesting Lite
- LCSW.CA: 180d return=53.36%, max drawdown=-17.84%, MA20>MA50 days last20=0, as_of=2026-10-28T21:00:00+00:00
- CANA.CA: 180d return=13.94%, max drawdown=-36.46%, MA20>MA50 days last20=19, as_of=2026-10-28T21:00:00+00:00
- AMOC.CA: 180d return=109.06%, max drawdown=-16.73%, MA20>MA50 days last20=20, as_of=2026-10-28T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=669 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- PRCL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ceramic and Porcelain summary=Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=669 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- MCQE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=669 sources=3 expected=Misr Cement Qena summary=Misr Cement to distribute EGP 10/shr dividends for 2025; Misr Cement stock is testing technical level ahead of historical peak – Analysis; Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits
  - Misr Cement to distribute EGP 10/shr dividends for 2025: https://english.mubasher.info/news/4586191/Misr-Cement-to-distribute-EGP-10-shr-dividends-for-2025/
  - Misr Cement stock is testing technical level ahead of historical peak – Analysis: https://english.mubasher.info/news/4560306/Misr-Cement-stock-is-testing-technical-level-ahead-of-historical-peak-Analysis/
  - Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits: https://english.mubasher.info/news/4524754/Misr-Cement-witnesses-3-254-remarkable-jump-in-9M-25-consolidated-net-profits/
- ADIB.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Abu Dhabi Islamic Bank Egypt summary=ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26; ADIB Egypt stock approaches breakout above EGP 41; ADIB Egypt’s stock holds uptrend despite corrections
  - ADIB Egypt’s consolidated profits leap to EGP 3.6bn in Q1-26: https://english.mubasher.info/news/4607278/ADIB-Egypt-s-consolidated-profits-leap-to-EGP-3-6bn-in-Q1-26/
  - ADIB Egypt stock approaches breakout above EGP 41: https://english.mubasher.info/news/4591391/ADIB-Egypt-stock-approaches-breakout-above-EGP-41/
  - ADIB Egypt’s stock holds uptrend despite corrections: https://english.mubasher.info/news/4562331/ADIB-Egypt-s-stock-holds-uptrend-despite-corrections/
- MPCI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Memphis Pharmaceuticals & Chemical Industries summary=Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.

## Warnings
- OpenRouter API error: 404
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for ADIB.CA matches the company but no source/report date was detected.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
