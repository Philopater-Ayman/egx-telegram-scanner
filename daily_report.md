# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-11-02T15:43:05.527080+00:00
Generated Cairo: 2026-11-02 17:43
Run timing: target 09:15 Cairo | generated Cairo 2026-11-02 17:43 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-11-02 17:39

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 166/187
- Top sector: Building Materials

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, November 02
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 0.0% / above MA50 0.0%
- EGX70 regime: BEARISH / above MA20 10.53% / above MA50 5.26%
- Sector breadth: 0.0%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=740411136.0 spike=1.45 score=14.82
- GTWL.CA: liquidity=709989504.0 spike=4.6 score=21.57
- CCAP.CA: liquidity=334176864.0 spike=0.72 score=12.58
- AMOC.CA: liquidity=254796544.0 spike=1.68 score=25.82
- ORAS.CA: liquidity=228640080.0 spike=1.0 score=4.6

## AI Narrative
- Provider: OpenRouter ERROR
- Model: openai/gpt-oss-120b:free
- Summary: OpenRouter narrative failed; local scanner summary used.

## Top Liquidity Spikes
- SEIG.CA: spike=11.96 liquidity=43693852.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ELWA.CA: spike=10.61 liquidity=2381658.5 outlook=WEAK_OR_RISKY score=23.43 buy_ready=False
- PRCL.CA: spike=7.02 liquidity=73547048.0 outlook=CONSTRUCTIVE score=55.25 buy_ready=False
- EPCO.CA: spike=6.09 liquidity=25922200.0 outlook=WEAK_OR_RISKY score=21.43 buy_ready=False
- GTWL.CA: spike=4.6 liquidity=709989504.0 outlook=NEUTRAL score=38.43 buy_ready=False

## Sector Leaderboard
- #1 Building Materials: score=7.25 5d=12.68% 20d=-2.57% aboveMA50=16.67%
- #2 Energy & Petrochemicals: score=3.65 5d=0.0% 20d=0.0% aboveMA50=33.33%
- #3 Tourism & Leisure: score=3.49 5d=11.28% 20d=-7.5% aboveMA50=0.0%
- #4 Education: score=2.73 5d=8.27% 20d=-8.36% aboveMA50=0.0%
- #5 Banking & Financials: score=2.3 5d=3.83% 20d=-5.06% aboveMA50=10.0%
- #6 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 General / Verified EGX Expansion: score=1.43 5d=8.04% 20d=-15.46% aboveMA50=4.9%
- #8 Fintech & Payments: score=1.42 5d=2.23% 20d=-7.62% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- AMOC.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- LCSW.CA: BULLISH_WATCH score=74.25 liquidity=TRADEABLE sector=LEADING risk=momentum is extended; far above support
- AJWA.CA: CONSTRUCTIVE score=67.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- SCEM.CA: CONSTRUCTIVE score=65.25 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA50
- POUL.CA: CONSTRUCTIVE score=61.82 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA50; sector is not leading
- SDTI.CA: CONSTRUCTIVE score=59.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20
- PRCL.CA: CONSTRUCTIVE score=55.25 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=below MA20; below MA50; far above support
- ARCC.CA: CONSTRUCTIVE score=53.25 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20; below MA50
- PRMH.CA: NEUTRAL score=49.43 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=below MA20; below MA50
- CPCI.CA: NEUTRAL score=47.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; below MA20

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=12.59 buy_ready=False sector_rank=7 price=209.98 support=171.02 resistance=275.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=37.23 liquidity=7019313.5 spike=0.79
- ABUK.CA: score=15.54 buy_ready=False sector_rank=16 price=80.52 support=80.5 resistance=95.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.14 liquidity=145017568.0 spike=1.68
- ACAMD.CA: score=13.57 buy_ready=False sector_rank=7 price=1.9 support=1.86 resistance=2.16 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=30130922.0 spike=0.68
- ACGC.CA: score=10.98 buy_ready=False sector_rank=11 price=12.7 support=11.6 resistance=14.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=47.23 liquidity=6563519.0 spike=0.87
- ADCI.CA: score=8.67 buy_ready=False sector_rank=7 price=251.56 support=221.0 resistance=280.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.19 liquidity=1975338.63 spike=1.06
- ADIB.CA: score=16.94 buy_ready=False sector_rank=5 price=46.4 support=43.16 resistance=50.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=77738616.0 spike=1.01
- ADPC.CA: score=11.38 buy_ready=False sector_rank=7 price=2.87 support=2.53 resistance=3.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=5805298.0 spike=0.63
- AFDI.CA: score=2.72 buy_ready=False sector_rank=7 price=42.96 support=34.8 resistance=54.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT RSI=31.97 liquidity=3144800.25 spike=0.83
- AFMC.CA: score=16.89 buy_ready=False sector_rank=7 price=121.41 support=94.6 resistance=179.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.04 liquidity=17155392.0 spike=1.16
- AJWA.CA: score=19.57 buy_ready=False sector_rank=7 price=214.92 support=179.0 resistance=229.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=20468410.0 spike=0.57
- ALCN.CA: score=5.35 buy_ready=False sector_rank=13 price=30.58 support=27.11 resistance=36.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.45 liquidity=5991377.5 spike=0.33
- ALUM.CA: score=0.72 buy_ready=False sector_rank=7 price=17.97 support=16.02 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=33.85 liquidity=2148931.0 spike=0.68
- AMER.CA: score=16.29 buy_ready=False sector_rank=15 price=4.12 support=3.21 resistance=5.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.07 liquidity=38972740.0 spike=0.72
- AMES.CA: score=12.11 buy_ready=False sector_rank=7 price=32.39 support=28.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=26.71 liquidity=90189544.0 spike=1.77
- AMIA.CA: score=12.71 buy_ready=False sector_rank=7 price=17.8 support=14.0 resistance=19.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=40.77 liquidity=8141774.5 spike=0.53
- AMOC.CA: score=25.82 buy_ready=False sector_rank=2 price=13.61 support=12.55 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=254796544.0 spike=1.68
- APSW.CA: score=-0.95 buy_ready=False sector_rank=7 price=7.35 support=7.1 resistance=8.92 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=25.41 liquidity=478869.09 spike=0.79
- ARAB.CA: score=9.29 buy_ready=False sector_rank=15 price=0.23 support=0.2 resistance=0.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.11 liquidity=66839652.0 spike=0.54
- ARCC.CA: score=19.4 buy_ready=False sector_rank=1 price=62.6 support=58.01 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=40.16 liquidity=25046522.0 spike=0.57
- AREH.CA: score=12.6 buy_ready=False sector_rank=7 price=1.04 support=0.91 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.25 liquidity=8652821.0 spike=1.19
- ASCM.CA: score=3.62 buy_ready=False sector_rank=7 price=41.6 support=38.2 resistance=59.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=5048858.5 spike=0.63
- ASPI.CA: score=15.57 buy_ready=False sector_rank=7 price=0.29 support=0.27 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=39.64 liquidity=11743216.0 spike=0.63
- ATLC.CA: score=1.19 buy_ready=False sector_rank=12 price=4.68 support=4.55 resistance=4.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6751113.5 spike=1.01
- ATQA.CA: score=8.18 buy_ready=False sector_rank=16 price=9.0 support=8.25 resistance=12.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=28.5 liquidity=43887160.0 spike=0.87
- AXPH.CA: score=11.32 buy_ready=False sector_rank=7 price=1315.09 support=1135.0 resistance=1550.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=42.41 liquidity=4725349.0 spike=1.01
- BINV.CA: score=2.58 buy_ready=False sector_rank=20 price=51.03 support=51.0 resistance=62.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=29.26 liquidity=4995229.5 spike=0.46
- BIOC.CA: score=16.57 buy_ready=False sector_rank=7 price=265.05 support=212.05 resistance=379.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=44.32 liquidity=38197704.0 spike=0.42
- BTFH.CA: score=13.42 buy_ready=False sector_rank=12 price=2.28 support=2.05 resistance=2.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.1 liquidity=64627520.0 spike=0.56
- CAED.CA: score=6.81 buy_ready=False sector_rank=7 price=82.7 support=64.0 resistance=130.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=34.48 liquidity=8234323.0 spike=0.93
- CANA.CA: score=4.92 buy_ready=False sector_rank=5 price=45.0 support=44.81 resistance=48.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14208617.0 spike=0.73
- CCAP.CA: score=12.58 buy_ready=False sector_rank=20 price=5.68 support=5.8 resistance=6.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.03 liquidity=334176864.0 spike=0.72
- CCRS.CA: score=3.46 buy_ready=False sector_rank=7 price=1.61 support=1.3 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=33.04 liquidity=4887472.0 spike=0.77
- CEFM.CA: score=5.63 buy_ready=False sector_rank=7 price=108.58 support=97.79 resistance=140.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=41.89 liquidity=1055026.88 spike=0.47
- CERA.CA: score=8.57 buy_ready=False sector_rank=7 price=1.02 support=0.93 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=47007584.0 spike=0.4
- CFGH.CA: score=-1.42 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.12 source=Yahoo Finance as_of=2026-10-31T22:00:00+00:00 freshness=FRESH RSI=12.5 liquidity=3286.44 spike=0.66
- CICH.CA: score=4.96 buy_ready=False sector_rank=12 price=10.54 support=9.63 resistance=12.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=40.13 liquidity=1543689.25 spike=0.84
- CIEB.CA: score=16.7 buy_ready=False sector_rank=5 price=21.97 support=21.35 resistance=24.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=47.07 liquidity=11071023.0 spike=1.39
- CIRA.CA: score=11.91 buy_ready=False sector_rank=4 price=35.21 support=32.01 resistance=41.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=47.54 liquidity=6821927.5 spike=0.44
- CLHO.CA: score=10.48 buy_ready=False sector_rank=10 price=13.03 support=12.51 resistance=16.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.37 liquidity=36561472.0 spike=0.97
- CNFN.CA: score=6.69 buy_ready=False sector_rank=12 price=3.59 support=3.25 resistance=4.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=43.5 liquidity=3276781.75 spike=0.36
- COMI.CA: score=14.82 buy_ready=False sector_rank=5 price=121.53 support=117.41 resistance=129.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.71 liquidity=740411136.0 spike=1.45
- COPR.CA: score=4.57 buy_ready=False sector_rank=7 price=0.38 support=0.37 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10367760.0 spike=0.67
- COSG.CA: score=10.48 buy_ready=False sector_rank=7 price=1.22 support=1.11 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=36.99 liquidity=6906011.5 spike=0.71
- CPCI.CA: score=11.08 buy_ready=False sector_rank=7 price=590.92 support=502.25 resistance=620.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=52.91 liquidity=3506971.25 spike=0.71
- CSAG.CA: score=11.38 buy_ready=False sector_rank=13 price=33.22 support=30.1 resistance=38.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=44.57 liquidity=6925179.5 spike=1.05
- DAPH.CA: score=13.57 buy_ready=False sector_rank=7 price=78.74 support=65.2 resistance=114.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=36.14 liquidity=12078226.0 spike=0.3
- DEIN.CA: score=7.57 buy_ready=False sector_rank=7 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=29 October 12:10 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=62.1 spike=0.02
- DOMT.CA: score=5.91 buy_ready=False sector_rank=14 price=22.8 support=20.27 resistance=25.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=44.76 liquidity=585001.75 spike=0.21
- DSCW.CA: score=14.79 buy_ready=False sector_rank=7 price=1.42 support=1.23 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=9219137.0 spike=0.71
- DTPP.CA: score=8.57 buy_ready=False sector_rank=7 price=45.32 support=36.0 resistance=334.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=6.51 liquidity=33404756.0 spike=0.86
- EALR.CA: score=8.57 buy_ready=False sector_rank=7 price=251.58 support=236.01 resistance=355.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=26.61 liquidity=7254287.0 spike=2.37
- EASB.CA: score=7.06 buy_ready=False sector_rank=7 price=5.88 support=5.03 resistance=8.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.68 liquidity=2484064.0 spike=0.48
- EAST.CA: score=4.33 buy_ready=False sector_rank=14 price=30.35 support=29.7 resistance=31.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16809262.0 spike=0.4
- EBSC.CA: score=7.56 buy_ready=False sector_rank=7 price=1.4 support=1.2 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=1986290.0 spike=0.78
- ECAP.CA: score=0.02 buy_ready=False sector_rank=7 price=25.88 support=24.8 resistance=31.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=29.79 liquidity=1450604.0 spike=0.45
- EDFM.CA: score=5.73 buy_ready=False sector_rank=7 price=350.03 support=312.92 resistance=396.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.93 liquidity=1156818.0 spike=0.92
- EEII.CA: score=11.15 buy_ready=False sector_rank=7 price=1.67 support=1.42 resistance=2.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=31.76 liquidity=14605882.0 spike=2.29
- EFIC.CA: score=15.18 buy_ready=False sector_rank=16 price=134.57 support=121.0 resistance=173.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=39.53 liquidity=13902962.0 spike=0.7
- EFID.CA: score=16.07 buy_ready=False sector_rank=14 price=17.89 support=16.01 resistance=19.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=46.22 liquidity=49161068.0 spike=1.37
- EFIH.CA: score=15.63 buy_ready=False sector_rank=8 price=22.93 support=20.3 resistance=25.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=44.23 liquidity=105881360.0 spike=1.53
- EGAL.CA: score=15.18 buy_ready=False sector_rank=16 price=297.22 support=275.0 resistance=359.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.29 liquidity=53710540.0 spike=0.56
- EGAS.CA: score=2.32 buy_ready=False sector_rank=2 price=44.43 support=43.81 resistance=47.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4664785.5 spike=1.1
- EGBE.CA: score=4.98 buy_ready=False sector_rank=5 price=0.49 support=0.47 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=56945.03 spike=0.55
- EGCH.CA: score=8.18 buy_ready=False sector_rank=16 price=9.89 support=10.0 resistance=13.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=25.75 liquidity=45968544.0 spike=0.84
- EGSA.CA: score=4.01 buy_ready=False sector_rank=19 price=8.71 support=8.7 resistance=9.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:47 PM market time freshness=DELAYED_CURRENT RSI=46.05 liquidity=8712.07 spike=1.3
- EGTS.CA: score=-1.4 buy_ready=False sector_rank=15 price=11.54 support=11.31 resistance=12.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4312882.5 spike=0.21
- EHDR.CA: score=13.11 buy_ready=False sector_rank=7 price=1.92 support=1.8 resistance=2.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=37.61 liquidity=9413309.0 spike=1.06
- ELEC.CA: score=13.5 buy_ready=False sector_rank=9 price=1.49 support=1.34 resistance=1.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=42134508.0 spike=0.85
- ELKA.CA: score=15.57 buy_ready=False sector_rank=7 price=1.4 support=1.21 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=9999025.0 spike=0.73
- ELNA.CA: score=9.42 buy_ready=False sector_rank=7 price=40.39 support=33.46 resistance=39.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:11 PM market time freshness=DELAYED_CURRENT RSI=76.94 liquidity=664540.63 spike=1.09
- ELSH.CA: score=9.64 buy_ready=False sector_rank=7 price=9.59 support=8.57 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=38.37 liquidity=4069695.25 spike=0.22
- ELWA.CA: score=5.95 buy_ready=False sector_rank=7 price=1.43 support=1.45 resistance=1.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=2381658.5 spike=10.61
- EMFD.CA: score=16.29 buy_ready=False sector_rank=15 price=11.9 support=10.6 resistance=13.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=44.68 liquidity=38462076.0 spike=0.83
- ENGC.CA: score=-1.49 buy_ready=False sector_rank=7 price=33.17 support=32.5 resistance=35.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3942054.25 spike=0.4
- EOSB.CA: score=9.62 buy_ready=False sector_rank=7 price=1.61 support=1.55 resistance=1.72 source=Yahoo Finance as_of=2026-10-31T22:00:00+00:00 freshness=FRESH RSI=70.0 liquidity=45947.79 spike=0.57
- EPCO.CA: score=18.57 buy_ready=False sector_rank=7 price=8.11 support=7.0 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=37.2 liquidity=25922200.0 spike=6.09
- EPPK.CA: score=-5.01 buy_ready=False sector_rank=7 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=8.4 buy_ready=False sector_rank=19 price=119.81 support=115.0 resistance=156.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=28.72 liquidity=201285392.0 spike=0.76
- ETRS.CA: score=15.56 buy_ready=False sector_rank=7 price=10.37 support=9.51 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=55.03 liquidity=8986856.0 spike=0.67
- EXPA.CA: score=12.04 buy_ready=False sector_rank=5 price=13.52 support=12.0 resistance=16.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=41.1 liquidity=6124044.0 spike=0.18
- FAIT.CA: score=8.59 buy_ready=False sector_rank=5 price=42.78 support=40.0 resistance=45.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:09 PM market time freshness=DELAYED_CURRENT RSI=46.47 liquidity=1668116.63 spike=0.62
- FAITA.CA: score=11.92 buy_ready=False sector_rank=5 price=1.0 support=0.98 resistance=1.01 source=Yahoo Finance as_of=2026-10-31T22:00:00+00:00 freshness=FRESH RSI=60.44 liquidity=214.79 spike=0.01
- FERC.CA: score=5.29 buy_ready=False sector_rank=16 price=58.35 support=53.57 resistance=77.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=35.05 liquidity=2107639.5 spike=0.6
- FWRY.CA: score=8.97 buy_ready=False sector_rank=8 price=15.75 support=16.24 resistance=19.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=24.03 liquidity=149223312.0 spike=1.2
- GBCO.CA: score=6.54 buy_ready=False sector_rank=21 price=21.43 support=21.51 resistance=32.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=18.35 liquidity=73104280.0 spike=0.67
- GDWA.CA: score=13.77 buy_ready=False sector_rank=7 price=0.53 support=0.48 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.07 liquidity=13865704.0 spike=1.1
- GGCC.CA: score=8.57 buy_ready=False sector_rank=7 price=0.51 support=0.49 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=30.96 liquidity=16531444.0 spike=0.93
- GIHD.CA: score=4.89 buy_ready=False sector_rank=7 price=40.89 support=39.21 resistance=43.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16729318.0 spike=1.16
- GMCI.CA: score=3.65 buy_ready=False sector_rank=7 price=1.43 support=1.34 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=833153.31 spike=3.12
- GRCA.CA: score=-2.96 buy_ready=False sector_rank=7 price=24.43 support=24.18 resistance=27.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2469325.75 spike=0.52
- GSSC.CA: score=3.9 buy_ready=False sector_rank=7 price=250.3 support=211.52 resistance=290.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=44.12 liquidity=328150.91 spike=0.34
- GTWL.CA: score=21.57 buy_ready=False sector_rank=7 price=124.07 support=73.02 resistance=184.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.07 liquidity=709989504.0 spike=4.6
- HDBK.CA: score=14.14 buy_ready=False sector_rank=5 price=95.78 support=83.01 resistance=112.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=41.4 liquidity=25340538.0 spike=1.11
- HELI.CA: score=8.61 buy_ready=False sector_rank=15 price=6.09 support=5.72 resistance=7.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=76455056.0 spike=1.16
- HRHO.CA: score=8.42 buy_ready=False sector_rank=12 price=22.47 support=22.8 resistance=27.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=31.05 liquidity=67340568.0 spike=0.58
- ICID.CA: score=5.7 buy_ready=False sector_rank=7 price=16.84 support=14.26 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:10 PM market time freshness=DELAYED_CURRENT RSI=46.73 liquidity=1125306.38 spike=0.17
- IDRE.CA: score=10.13 buy_ready=False sector_rank=7 price=36.34 support=29.11 resistance=52.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=39.89 liquidity=6319939.0 spike=1.12
- IFAP.CA: score=-2.07 buy_ready=False sector_rank=17 price=15.44 support=15.12 resistance=16.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4190104.75 spike=0.88
- INFI.CA: score=14.57 buy_ready=False sector_rank=7 price=111.17 support=93.44 resistance=138.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=45.92 liquidity=14809513.0 spike=0.72
- IRON.CA: score=8.38 buy_ready=False sector_rank=16 price=23.75 support=23.53 resistance=32.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.32 liquidity=11429971.0 spike=1.1
- ISMA.CA: score=19.91 buy_ready=False sector_rank=7 price=18.53 support=14.11 resistance=27.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=35.32 liquidity=21153642.0 spike=3.17
- ISMQ.CA: score=13.66 buy_ready=False sector_rank=16 price=7.09 support=5.96 resistance=8.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.58 liquidity=18845180.0 spike=1.24
- ISPH.CA: score=9.68 buy_ready=False sector_rank=10 price=9.11 support=9.14 resistance=12.03 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=29.82 liquidity=73091504.0 spike=1.6
- JUFO.CA: score=15.33 buy_ready=False sector_rank=14 price=22.77 support=21.01 resistance=26.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=39.75 liquidity=16313024.0 spike=0.93
- KABO.CA: score=14.08 buy_ready=False sector_rank=11 price=6.62 support=5.58 resistance=9.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=37.3 liquidity=28126480.0 spike=1.33
- KWIN.CA: score=2.53 buy_ready=False sector_rank=7 price=52.96 support=44.02 resistance=82.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=31.42 liquidity=3961821.25 spike=0.9
- KZPC.CA: score=10.85 buy_ready=False sector_rank=7 price=12.41 support=11.56 resistance=13.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=49.61 liquidity=6274405.0 spike=0.91
- LCSW.CA: score=26.4 buy_ready=False sector_rank=1 price=35.3 support=28.0 resistance=36.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=63.56 liquidity=20841548.0 spike=0.83
- LUTS.CA: score=18.15 buy_ready=False sector_rank=7 price=0.7 support=0.47 resistance=0.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=43.02 liquidity=100066656.0 spike=1.79
- MAAL.CA: score=1.66 buy_ready=False sector_rank=7 price=6.47 support=6.21 resistance=7.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7091855.0 spike=0.56
- MASR.CA: score=13.57 buy_ready=False sector_rank=7 price=6.48 support=5.6 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.29 liquidity=26241580.0 spike=0.53
- MBSC.CA: score=14.64 buy_ready=False sector_rank=1 price=305.61 support=262.0 resistance=414.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=33.47 liquidity=116099704.0 spike=1.12
- MCQE.CA: score=20.4 buy_ready=False sector_rank=1 price=162.04 support=144.0 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=40.4 liquidity=56030240.0 spike=0.76
- MCRO.CA: score=15.57 buy_ready=False sector_rank=7 price=1.25 support=1.07 resistance=1.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=27383076.0 spike=0.61
- MENA.CA: score=3.81 buy_ready=False sector_rank=15 price=5.62 support=5.45 resistance=7.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=36.76 liquidity=513639.81 spike=0.12
- MEPA.CA: score=8.57 buy_ready=False sector_rank=7 price=1.23 support=1.14 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=28.75 liquidity=13372535.0 spike=0.98
- MFPC.CA: score=14.76 buy_ready=False sector_rank=16 price=42.6 support=40.66 resistance=47.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=65200292.0 spike=1.29
- MFSC.CA: score=-0.04 buy_ready=False sector_rank=7 price=31.82 support=28.55 resistance=47.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=30.44 liquidity=1383103.0 spike=0.73
- MHOT.CA: score=7.68 buy_ready=False sector_rank=3 price=14.84 support=13.0 resistance=16.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=39.5 liquidity=2288284.0 spike=0.32
- MICH.CA: score=10.66 buy_ready=False sector_rank=7 price=39.54 support=35.5 resistance=44.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=48.02 liquidity=4089280.5 spike=0.66
- MILS.CA: score=3.94 buy_ready=False sector_rank=7 price=121.36 support=96.02 resistance=190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=31.21 liquidity=5365561.0 spike=0.71
- MIPH.CA: score=4.92 buy_ready=False sector_rank=10 price=741.06 support=610.0 resistance=840.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=41.28 liquidity=438478.41 spike=0.12
- MOED.CA: score=8.57 buy_ready=False sector_rank=7 price=0.45 support=0.39 resistance=0.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=25.85 liquidity=10695157.0 spike=0.82
- MOIL.CA: score=7.61 buy_ready=False sector_rank=2 price=0.61 support=0.6 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=38.41 liquidity=149977.52 spike=0.75
- MOIN.CA: score=2.28 buy_ready=False sector_rank=7 price=27.24 support=25.7 resistance=37.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=30.84 liquidity=2705850.25 spike=0.34
- MOSC.CA: score=4.07 buy_ready=False sector_rank=7 price=232.16 support=198.01 resistance=299.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:06 PM market time freshness=DELAYED_CURRENT RSI=39.62 liquidity=500409.28 spike=0.16
- MPCI.CA: score=5.09 buy_ready=False sector_rank=7 price=299.99 support=292.0 resistance=323.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=125533680.0 spike=1.26
- MPCO.CA: score=9.28 buy_ready=False sector_rank=17 price=1.73 support=1.55 resistance=2.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=32.23 liquidity=137827744.0 spike=1.77
- MPRC.CA: score=10.94 buy_ready=False sector_rank=7 price=31.99 support=27.0 resistance=41.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=7365442.0 spike=0.49
- MTIE.CA: score=2.54 buy_ready=False sector_rank=21 price=6.52 support=6.32 resistance=6.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13341950.0 spike=0.68
- NAHO.CA: score=-5.42 buy_ready=False sector_rank=7 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:47 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=6870.99 spike=0.39
- NCCW.CA: score=8.57 buy_ready=False sector_rank=7 price=5.08 support=4.05 resistance=7.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=34.79 liquidity=13676640.0 spike=0.73
- NEDA.CA: score=0.49 buy_ready=False sector_rank=7 price=2.36 support=2.35 resistance=2.68 source=Yahoo Finance as_of=2026-10-31T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=301622.15 spike=1.81
- NHPS.CA: score=2.34 buy_ready=False sector_rank=7 price=54.57 support=50.0 resistance=77.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=28.12 liquidity=3764289.0 spike=0.55
- NINH.CA: score=-0.73 buy_ready=False sector_rank=7 price=14.01 support=13.99 resistance=14.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4699975.5 spike=0.48
- NIPH.CA: score=4.92 buy_ready=False sector_rank=10 price=262.76 support=255.0 resistance=282.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=152481744.0 spike=1.22
- OBRI.CA: score=12.09 buy_ready=False sector_rank=7 price=22.17 support=18.11 resistance=33.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=39.68 liquidity=8515144.0 spike=0.58
- OCDI.CA: score=13.29 buy_ready=False sector_rank=15 price=22.5 support=21.0 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=39.58 liquidity=19385346.0 spike=0.56
- OCPH.CA: score=8.19 buy_ready=False sector_rank=7 price=175.78 support=147.96 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=38.32 liquidity=2617102.5 spike=0.85
- ODIN.CA: score=16.85 buy_ready=False sector_rank=7 price=1.95 support=1.7 resistance=2.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=40.31 liquidity=10126628.0 spike=1.64
- OFH.CA: score=8.71 buy_ready=False sector_rank=7 price=0.7 support=0.61 resistance=0.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=32.81 liquidity=9134481.0 spike=0.37
- OIH.CA: score=12.58 buy_ready=False sector_rank=20 price=1.62 support=1.5 resistance=1.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.19 liquidity=29174624.0 spike=0.66
- OLFI.CA: score=3.82 buy_ready=False sector_rank=14 price=18.62 support=17.86 resistance=22.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:13 PM market time freshness=DELAYED_CURRENT RSI=28.3 liquidity=5488372.0 spike=0.43
- ORAS.CA: score=4.6 buy_ready=False sector_rank=6 price=786.73 support=781.0 resistance=820.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=228640080.0 spike=1.0
- ORHD.CA: score=10.29 buy_ready=False sector_rank=15 price=9.5 support=8.5 resistance=12.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=34.59 liquidity=41206732.0 spike=0.36
- ORWE.CA: score=14.42 buy_ready=False sector_rank=11 price=24.2 support=22.62 resistance=28.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.57 liquidity=33053450.0 spike=0.88
- PHAR.CA: score=16.48 buy_ready=False sector_rank=10 price=95.05 support=90.2 resistance=119.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=39.01 liquidity=51313916.0 spike=0.99
- PHDC.CA: score=8.73 buy_ready=False sector_rank=15 price=10.73 support=10.51 resistance=13.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=25.45 liquidity=109774896.0 spike=1.22
- PHTV.CA: score=13.21 buy_ready=False sector_rank=7 price=316.26 support=300.0 resistance=360.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=37.72 liquidity=3641008.5 spike=3.78
- POUL.CA: score=22.25 buy_ready=False sector_rank=14 price=9.84 support=8.81 resistance=10.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=47.52 liquidity=195205280.0 spike=3.46
- PRCL.CA: score=25.4 buy_ready=False sector_rank=1 price=21.11 support=16.65 resistance=27.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=73547048.0 spike=7.02
- PRDC.CA: score=15.25 buy_ready=False sector_rank=15 price=5.99 support=5.08 resistance=8.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=41.27 liquidity=9955289.0 spike=0.29
- PRMH.CA: score=20.57 buy_ready=False sector_rank=7 price=1.81 support=1.7 resistance=2.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=10332243.0 spike=3.82
- RACC.CA: score=5.24 buy_ready=False sector_rank=7 price=7.22 support=6.1 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=28.26 liquidity=6670083.5 spike=0.94
- RAKT.CA: score=3.88 buy_ready=False sector_rank=7 price=22.35 support=20.4 resistance=25.08 source=Yahoo Finance as_of=2026-10-31T22:00:00+00:00 freshness=FRESH RSI=40.92 liquidity=307178.41 spike=0.69
- RAYA.CA: score=8.62 buy_ready=False sector_rank=18 price=5.21 support=5.02 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=28295426.0 spike=1.57
- RMDA.CA: score=17.12 buy_ready=False sector_rank=10 price=5.0 support=4.5 resistance=5.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=48.36 liquidity=30344638.0 spike=1.32
- ROTO.CA: score=1.41 buy_ready=False sector_rank=7 price=29.07 support=25.0 resistance=42.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=28.01 liquidity=2838571.0 spike=0.38
- RREI.CA: score=4.57 buy_ready=False sector_rank=7 price=2.56 support=2.45 resistance=2.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10356077.0 spike=0.96
- RTVC.CA: score=1.59 buy_ready=False sector_rank=7 price=2.7 support=2.77 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:12 PM market time freshness=DELAYED_CURRENT RSI=18.52 liquidity=2939583.75 spike=1.04
- RUBX.CA: score=9.57 buy_ready=False sector_rank=7 price=12.23 support=10.51 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=34.54 liquidity=46286604.0 spike=0.55
- SAUD.CA: score=13.42 buy_ready=False sector_rank=5 price=19.8 support=19.3 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=38.31 liquidity=9501033.0 spike=0.84
- SCEM.CA: score=23.4 buy_ready=False sector_rank=1 price=87.03 support=73.9 resistance=95.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:28 PM market time freshness=DELAYED_CURRENT RSI=48.54 liquidity=34424504.0 spike=0.56
- SCFM.CA: score=-3.23 buy_ready=False sector_rank=7 price=204.67 support=193.4 resistance=219.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2021082.13 spike=1.09
- SCTS.CA: score=10.1 buy_ready=False sector_rank=4 price=482.16 support=410.0 resistance=588.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=47.33 liquidity=4005088.25 spike=0.97
- SDTI.CA: score=12.68 buy_ready=False sector_rank=7 price=81.55 support=75.01 resistance=90.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=42.47 liquidity=5103990.5 spike=0.29
- SEIG.CA: score=9.57 buy_ready=False sector_rank=7 price=247.5 support=225.11 resistance=268.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=43693852.0 spike=11.96
- SIPC.CA: score=14.57 buy_ready=False sector_rank=7 price=4.38 support=3.73 resistance=6.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=41.06 liquidity=15627218.0 spike=0.26
- SKPC.CA: score=15.18 buy_ready=False sector_rank=16 price=14.73 support=14.01 resistance=16.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=23734618.0 spike=0.43
- SMFR.CA: score=-0.29 buy_ready=False sector_rank=7 price=182.83 support=165.0 resistance=245.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:07 PM market time freshness=DELAYED_CURRENT RSI=30.11 liquidity=1139545.75 spike=0.41
- SNFC.CA: score=10.99 buy_ready=False sector_rank=7 price=10.6 support=10.08 resistance=11.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=38.24 liquidity=7419303.0 spike=0.99
- SPIN.CA: score=17.78 buy_ready=False sector_rank=11 price=13.98 support=12.0 resistance=17.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=35.99 liquidity=10926479.0 spike=2.18
- SPMD.CA: score=10.41 buy_ready=False sector_rank=7 price=0.33 support=0.3 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=4839391.0 spike=0.33
- SUGR.CA: score=10.2 buy_ready=False sector_rank=14 price=48.0 support=44.62 resistance=54.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=47.7 liquidity=5876035.0 spike=0.68
- SVCE.CA: score=13.57 buy_ready=False sector_rank=7 price=8.26 support=7.01 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.43 liquidity=24700436.0 spike=0.38
- SWDY.CA: score=16.68 buy_ready=False sector_rank=9 price=108.4 support=97.0 resistance=124.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.03 liquidity=55131508.0 spike=1.09
- TALM.CA: score=10.09 buy_ready=False sector_rank=4 price=18.47 support=17.0 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=23.42 liquidity=18884688.0 spike=0.73
- TMGH.CA: score=13.29 buy_ready=False sector_rank=15 price=78.02 support=78.37 resistance=93.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=38.97 liquidity=195098672.0 spike=0.75
- TRTO.CA: score=-0.43 buy_ready=False sector_rank=7 price=0.05 support=0.05 resistance=0.07 source=Yahoo Finance as_of=2026-10-31T22:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=1341.89 spike=0.19
- UEFM.CA: score=0.39 buy_ready=False sector_rank=7 price=429.03 support=422.0 resistance=528.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:25 PM market time freshness=DELAYED_CURRENT RSI=22.97 liquidity=1818508.25 spike=0.93
- UEGC.CA: score=15.57 buy_ready=False sector_rank=7 price=1.36 support=1.21 resistance=1.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=48.11 liquidity=23762214.0 spike=0.51
- UNIP.CA: score=8.11 buy_ready=False sector_rank=7 price=0.28 support=0.25 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=36.42 liquidity=4537680.5 spike=0.57
- UNIT.CA: score=10.44 buy_ready=False sector_rank=15 price=17.52 support=15.06 resistance=19.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:05 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=2143614.25 spike=0.69
- WCDF.CA: score=-0.91 buy_ready=False sector_rank=7 price=493.33 support=432.5 resistance=635.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:14 PM market time freshness=DELAYED_CURRENT RSI=24.83 liquidity=516359.22 spike=0.28
- WKOL.CA: score=9.16 buy_ready=False sector_rank=7 price=237.59 support=218.0 resistance=309.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:27 PM market time freshness=DELAYED_CURRENT RSI=35.04 liquidity=5587003.5 spike=0.8
- ZEOT.CA: score=8.56 buy_ready=False sector_rank=7 price=10.15 support=8.0 resistance=13.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:26 PM market time freshness=DELAYED_CURRENT RSI=46.92 liquidity=2987671.5 spike=0.4
- ZMID.CA: score=14.65 buy_ready=False sector_rank=15 price=6.5 support=5.91 resistance=7.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=02:29 PM market time freshness=DELAYED_CURRENT RSI=37.13 liquidity=77660184.0 spike=1.18

## Backtesting Lite
- LCSW.CA: 180d return=38.96%, max drawdown=-17.84%, MA20>MA50 days last20=0, as_of=2026-10-31T22:00:00+00:00
- AMOC.CA: 180d return=113.69%, max drawdown=-16.73%, MA20>MA50 days last20=20, as_of=2026-10-31T22:00:00+00:00
- PRCL.CA: 180d return=23.18%, max drawdown=-53.75%, MA20>MA50 days last20=0, as_of=2026-10-31T22:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- AMOC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Alexandria Mineral Oils summary=AMOC achieves EGP 10.5bn consolidated sales in Q1-26; AMOC studies potential project with Germany’s SULZER; AMOC to pay out EGP 0.4/shr dividends for H2-25
  - AMOC achieves EGP 10.5bn consolidated sales in Q1-26: https://english.mubasher.info/news/4604903/AMOC-achieves-EGP-10-5bn-consolidated-sales-in-Q1-26/
  - AMOC studies potential project with Germany’s SULZER: https://english.mubasher.info/news/4586853/AMOC-studies-potential-project-with-Germany-s-SULZER/
  - AMOC to pay out EGP 0.4/shr dividends for H2-25: https://english.mubasher.info/news/4586775/AMOC-to-pay-out-EGP-0-4-shr-dividends-for-H2-25/
- PRCL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Ceramic and Porcelain summary=Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- SCEM.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=670 sources=3 expected=Sinai Cement summary=Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn; Upward trend line ends several-day decline for Sinai Cement stock; Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25
  - Sinai Cement’s consolidated profits fall in 2025; net sales cross EGP 9bn: https://english.mubasher.info/news/4564824/Sinai-Cement-s-consolidated-profits-fall-in-2025-net-sales-cross-EGP-9bn/
  - Upward trend line ends several-day decline for Sinai Cement stock: https://english.mubasher.info/news/4529647/Upward-trend-line-ends-several-day-decline-for-Sinai-Cement-stock/
  - Sinai Cement reports lower consolidated net profits at EGP 1.5bn in 9M-25: https://english.mubasher.info/news/4526073/Sinai-Cement-reports-lower-consolidated-net-profits-at-EGP-1-5bn-in-9M-25/
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- GTWL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Golden Textiles & Clothes Wool summary=Golden Textiles profits jump 214%; Golden Textiles OGM OKs 50 piasters/shr dividends; Golden Textiles consolidated profits down 18.5% in FY16
  - Golden Textiles profits jump 214%: https://english.mubasher.info/news/3108548/Golden-Textiles-profits-jump-214-/
  - Golden Textiles OGM OKs 50 piasters/shr dividends: https://english.mubasher.info/news/3103061/Golden-Textiles-OGM-OKs-50-piasters-shr-dividends/
  - Golden Textiles consolidated profits down 18.5% in FY16: https://english.mubasher.info/news/3092552/Golden-Textiles-consolidated-profits-down-18-5-in-FY16/
- PRMH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Prime Holding S.A.E summary=Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- MCQE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=670 sources=3 expected=Misr Cement Qena summary=Misr Cement to distribute EGP 10/shr dividends for 2025; Misr Cement stock is testing technical level ahead of historical peak – Analysis; Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits
  - Misr Cement to distribute EGP 10/shr dividends for 2025: https://english.mubasher.info/news/4586191/Misr-Cement-to-distribute-EGP-10-shr-dividends-for-2025/
  - Misr Cement stock is testing technical level ahead of historical peak – Analysis: https://english.mubasher.info/news/4560306/Misr-Cement-stock-is-testing-technical-level-ahead-of-historical-peak-Analysis/
  - Misr Cement witnesses 3,254% remarkable jump in 9M-25 consolidated net profits: https://english.mubasher.info/news/4524754/Misr-Cement-witnesses-3-254-remarkable-jump-in-9M-25-consolidated-net-profits/

## Warnings
- OpenRouter API error: 404
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for AMOC.CA matches the company but no source/report date was detected.
- Evidence rejected for PRCL.CA: source text did not clearly match PRCL.CA / Ceramic and Porcelain.
- Evidence for SCEM.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for MCQE.CA matches the company but appears old; latest detected date is 2025-01-01.
