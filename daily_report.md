# Telegram-First EGX Scanner Report

Scan phase: Evening tomorrow plan
Generated UTC: 2026-09-27T19:51:47.989810+00:00
Generated Cairo: 2026-09-27 22:51
Run timing: target 19:30 Cairo | generated Cairo 2026-09-27 22:51 | cron 30 16 * * 0-4
Trigger: scheduled cron=30 16 * * 0-4 mapped to evening_plan; Cairo now 2026-09-27 22:48

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 137/187
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, September 27
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.88% / above MA50 23.53%
- EGX70 regime: BEARISH / above MA20 11.76% / above MA50 26.47%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=602190720.0 spike=0.69 score=19.4
- TMGH.CA: liquidity=313304960.0 spike=1.08 score=8.11
- ZMID.CA: liquidity=188722576.0 spike=0.98 score=7.95
- POUL.CA: liquidity=169051872.0 spike=6.55 score=8.63
- SDTI.CA: liquidity=163713744.0 spike=6.63 score=9.01

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30 and EGX70 are bearish with weak sector breadth, putting the market in a defensive mode that overrides the scanner’s bullish‑watch tickets, resulting in a HOLD recommendation.

## Top Liquidity Spikes
- EGSA.CA: spike=15.36 liquidity=100936.9 outlook=CONSTRUCTIVE score=66 buy_ready=False
- MHOT.CA: spike=12.16 liquidity=133366208.0 outlook=BULLISH_WATCH score=100 buy_ready=False
- SDTI.CA: spike=6.63 liquidity=163713744.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- POUL.CA: spike=6.55 liquidity=169051872.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MAAL.CA: spike=4.46 liquidity=81656192.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=26.84 5d=4.89% 20d=3.22% aboveMA50=100.0%
- #2 Telecommunications: score=20.35 5d=1.12% 20d=10.4% aboveMA50=100.0%
- #3 Investment Holding: score=7.65 5d=-2.76% 20d=16.46% aboveMA50=100.0%
- #4 Education: score=5.29 5d=-5.09% 20d=13.91% aboveMA50=66.67%
- #5 Energy & Petrochemicals: score=3.62 5d=-2.9% 20d=6.33% aboveMA50=66.67%
- #6 Technology & Distribution: score=3.21 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #7 Agriculture & Food Production: score=2.95 5d=-5.24% 20d=5.69% aboveMA50=50.0%
- #8 Banking & Financials: score=2.05 5d=-2.26% 20d=-1.1% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MHOT.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- CANA.CA: BULLISH_WATCH score=84.05 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended; sector is not leading
- BINV.CA: BULLISH_WATCH score=79.65 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- TALM.CA: BULLISH_WATCH score=75.29 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MPCO.CA: BULLISH_WATCH score=73.95 liquidity=TRADEABLE sector=IMPROVING risk=far above support
- EXPA.CA: BULLISH_WATCH score=72.05 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- CIRA.CA: BULLISH_WATCH score=71.29 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- EGTS.CA: CONSTRUCTIVE score=68 liquidity=TRADEABLE sector=LAGGING risk=momentum is extended; sector is not leading
- OIH.CA: CONSTRUCTIVE score=67.65 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20; momentum is extended
- EGSA.CA: CONSTRUCTIVE score=66 liquidity=THIN sector=LEADING risk=liquidity below minimum; close to resistance

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=1.14 buy_ready=False sector_rank=14 price=266.15 support=263.02 resistance=293.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7128180.5 spike=0.29
- ABUK.CA: score=17.47 buy_ready=False sector_rank=12 price=87.63 support=76.01 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=55.49 liquidity=47267720.0 spike=0.25
- ACAMD.CA: score=9.27 buy_ready=False sector_rank=14 price=1.87 support=1.94 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.82 liquidity=79428688.0 spike=1.63
- ACGC.CA: score=16.64 buy_ready=False sector_rank=10 price=13.81 support=13.65 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.67 liquidity=9034950.0 spike=0.35
- ADCI.CA: score=5.97 buy_ready=False sector_rank=14 price=275.04 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.46 liquidity=1957342.38 spike=0.43
- ADIB.CA: score=14.82 buy_ready=False sector_rank=8 price=51.81 support=49.0 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=41.07 liquidity=59696864.0 spike=0.7
- ADPC.CA: score=4.41 buy_ready=False sector_rank=14 price=3.52 support=3.51 resistance=3.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22521920.0 spike=1.2
- AFDI.CA: score=9.03 buy_ready=False sector_rank=14 price=51.5 support=51.5 resistance=61.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=39.42 liquidity=5017316.0 spike=0.28
- AFMC.CA: score=3.02 buy_ready=False sector_rank=14 price=140.64 support=140.02 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9009488.0 spike=0.16
- AJWA.CA: score=18.01 buy_ready=False sector_rank=14 price=179.96 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.11 liquidity=16760887.0 spike=0.38
- ALCN.CA: score=19.8 buy_ready=False sector_rank=9 price=32.05 support=30.05 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=53.19 liquidity=16385635.0 spike=0.43
- ALUM.CA: score=4.16 buy_ready=False sector_rank=14 price=22.84 support=23.6 resistance=30.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.0 liquidity=5150985.0 spike=0.69
- AMER.CA: score=12.95 buy_ready=False sector_rank=19 price=4.85 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.09 liquidity=20786264.0 spike=0.4
- AMES.CA: score=4.01 buy_ready=False sector_rank=14 price=45.03 support=45.01 resistance=49.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=57438364.0 spike=0.21
- AMIA.CA: score=17.01 buy_ready=False sector_rank=14 price=18.65 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=25051932.0 spike=0.71
- AMOC.CA: score=18.45 buy_ready=False sector_rank=5 price=12.81 support=11.0 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.22 liquidity=58780720.0 spike=0.34
- APSW.CA: score=3.52 buy_ready=False sector_rank=14 price=8.19 support=8.16 resistance=8.79 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=35.61 liquidity=512538.36 spike=0.62
- ARAB.CA: score=6.95 buy_ready=False sector_rank=19 price=0.21 support=0.22 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=20.34 liquidity=46107848.0 spike=0.53
- ARCC.CA: score=8.41 buy_ready=False sector_rank=21 price=63.81 support=66.12 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=18.63 liquidity=45398408.0 spike=1.46
- AREH.CA: score=1.49 buy_ready=False sector_rank=14 price=1.26 support=1.25 resistance=1.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7478473.5 spike=0.55
- ASCM.CA: score=7.69 buy_ready=False sector_rank=14 price=58.61 support=57.36 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.49 liquidity=8677123.0 spike=0.47
- ASPI.CA: score=4.01 buy_ready=False sector_rank=14 price=0.36 support=0.36 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=23300884.0 spike=0.36
- ATLC.CA: score=3.24 buy_ready=False sector_rank=18 price=5.82 support=5.68 resistance=6.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10064368.0 spike=0.35
- ATQA.CA: score=17.47 buy_ready=False sector_rank=12 price=12.37 support=11.56 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.85 liquidity=66957156.0 spike=0.64
- AXPH.CA: score=15.45 buy_ready=False sector_rank=14 price=1600.79 support=1580.0 resistance=1750.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.43 liquidity=8218119.0 spike=1.11
- BINV.CA: score=16.7 buy_ready=False sector_rank=3 price=56.07 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.76 liquidity=4300351.0 spike=0.16
- BIOC.CA: score=4.01 buy_ready=False sector_rank=14 price=238.37 support=237.0 resistance=263.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15495003.0 spike=0.18
- BTFH.CA: score=7.24 buy_ready=False sector_rank=18 price=2.72 support=2.79 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=76992352.0 spike=0.89
- CAED.CA: score=2.1 buy_ready=False sector_rank=14 price=113.58 support=112.01 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.95 liquidity=3094658.25 spike=0.15
- CANA.CA: score=23.04 buy_ready=False sector_rank=8 price=46.46 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=65.91 liquidity=37909084.0 spike=1.61
- CCAP.CA: score=19.4 buy_ready=False sector_rank=3 price=6.8 support=5.74 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.61 liquidity=602190720.0 spike=0.69
- CCRS.CA: score=9.93 buy_ready=False sector_rank=14 price=2.42 support=2.4 resistance=2.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=46.9 liquidity=5922219.5 spike=0.25
- CEFM.CA: score=6.16 buy_ready=False sector_rank=14 price=132.9 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.31 liquidity=2156547.75 spike=0.24
- CERA.CA: score=4.01 buy_ready=False sector_rank=14 price=1.22 support=1.2 resistance=1.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=116159384.0 spike=0.84
- CFGH.CA: score=2.01 buy_ready=False sector_rank=14 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=23.08 liquidity=1710.51 spike=0.1
- CICH.CA: score=5.59 buy_ready=False sector_rank=18 price=11.85 support=11.51 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.08 liquidity=2344148.0 spike=0.4
- CIEB.CA: score=9.82 buy_ready=False sector_rank=8 price=24.01 support=23.9 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=28.51 liquidity=10203533.0 spike=0.73
- CIRA.CA: score=23.12 buy_ready=False sector_rank=4 price=39.07 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.94 liquidity=19209412.0 spike=0.48
- CLHO.CA: score=8.72 buy_ready=False sector_rank=15 price=15.18 support=15.35 resistance=18.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.8 liquidity=16714120.0 spike=0.24
- CNFN.CA: score=4.35 buy_ready=False sector_rank=18 price=4.1 support=4.24 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.26 liquidity=7101077.0 spike=0.64
- COMI.CA: score=9.82 buy_ready=False sector_rank=8 price=128.55 support=126.81 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=14.02 liquidity=144358816.0 spike=0.23
- COPR.CA: score=14.01 buy_ready=False sector_rank=14 price=0.46 support=0.46 resistance=0.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=17044414.0 spike=0.49
- COSG.CA: score=9.01 buy_ready=False sector_rank=14 price=1.6 support=1.63 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.57 liquidity=13585088.0 spike=0.47
- CPCI.CA: score=13.12 buy_ready=False sector_rank=14 price=560.05 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=71.71 liquidity=3687964.75 spike=1.21
- CSAG.CA: score=4.29 buy_ready=False sector_rank=9 price=36.29 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.89 liquidity=4485019.5 spike=0.3
- DAPH.CA: score=9.01 buy_ready=False sector_rank=14 price=99.0 support=101.55 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.93 liquidity=31513640.0 spike=0.59
- DEIN.CA: score=7.01 buy_ready=False sector_rank=14 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=4.04 buy_ready=False sector_rank=16 price=24.92 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.45 liquidity=6086206.5 spike=1.16
- DSCW.CA: score=8.01 buy_ready=False sector_rank=14 price=1.72 support=1.71 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.63 liquidity=17933980.0 spike=0.78
- DTPP.CA: score=17.01 buy_ready=False sector_rank=14 price=313.3 support=296.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=57.15 liquidity=41069500.0 spike=0.48
- EALR.CA: score=1.85 buy_ready=False sector_rank=14 price=343.82 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=32.72 liquidity=3842664.5 spike=0.29
- EASB.CA: score=7.43 buy_ready=False sector_rank=14 price=7.24 support=7.13 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.44 liquidity=3420771.0 spike=0.21
- EAST.CA: score=7.24 buy_ready=False sector_rank=16 price=30.69 support=30.59 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=4.1 liquidity=9603629.0 spike=0.16
- EBSC.CA: score=6.53 buy_ready=False sector_rank=14 price=1.88 support=1.9 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.49 liquidity=2522707.0 spike=0.23
- ECAP.CA: score=1.38 buy_ready=False sector_rank=14 price=30.02 support=31.0 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=18.79 liquidity=3374456.0 spike=0.38
- EDFM.CA: score=-0.63 buy_ready=False sector_rank=14 price=384.29 support=382.35 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=30.78 liquidity=362954.31 spike=0.2
- EEII.CA: score=4.01 buy_ready=False sector_rank=14 price=2.16 support=2.15 resistance=2.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=11213172.0 spike=0.76
- EFIC.CA: score=4.47 buy_ready=False sector_rank=12 price=159.45 support=157.42 resistance=179.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=69716992.0 spike=0.2
- EFID.CA: score=13.63 buy_ready=False sector_rank=16 price=29.15 support=28.56 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.21 liquidity=50554936.0 spike=0.73
- EFIH.CA: score=13.61 buy_ready=False sector_rank=17 price=22.92 support=22.16 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=43.39 liquidity=27423822.0 spike=0.46
- EGAL.CA: score=17.47 buy_ready=False sector_rank=12 price=350.78 support=340.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.49 liquidity=16134413.0 spike=0.22
- EGAS.CA: score=14.93 buy_ready=False sector_rank=5 price=57.0 support=53.62 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.18 liquidity=39311876.0 spike=3.24
- EGBE.CA: score=7.98 buy_ready=False sector_rank=8 price=0.52 support=0.49 resistance=0.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=45.65 liquidity=103320.87 spike=1.03
- EGCH.CA: score=17.59 buy_ready=False sector_rank=12 price=13.93 support=13.53 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.25 liquidity=137475792.0 spike=1.06
- EGSA.CA: score=18.5 buy_ready=False sector_rank=2 price=9.0 support=8.8 resistance=9.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=24 September 12:29 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=100936.9 spike=15.36
- EGTS.CA: score=20.47 buy_ready=False sector_rank=19 price=17.99 support=16.51 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.03 liquidity=43424484.0 spike=1.26
- EHDR.CA: score=10.03 buy_ready=False sector_rank=14 price=2.56 support=2.44 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.75 liquidity=25749144.0 spike=1.51
- ELEC.CA: score=6.9 buy_ready=False sector_rank=20 price=1.88 support=1.91 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.64 liquidity=53602576.0 spike=0.69
- ELKA.CA: score=7.28 buy_ready=False sector_rank=14 price=1.51 support=1.54 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=10.53 liquidity=9273403.0 spike=0.27
- ELNA.CA: score=-1.87 buy_ready=False sector_rank=14 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=27.7 liquidity=126897.66 spike=0.33
- ELSH.CA: score=9.11 buy_ready=False sector_rank=14 price=11.68 support=12.06 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.62 liquidity=37659568.0 spike=1.05
- ELWA.CA: score=-0.5 buy_ready=False sector_rank=14 price=1.63 support=1.61 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=28.13 liquidity=490571.16 spike=0.29
- EMFD.CA: score=2.95 buy_ready=False sector_rank=19 price=12.67 support=12.63 resistance=13.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=85924328.0 spike=0.55
- ENGC.CA: score=13.45 buy_ready=False sector_rank=14 price=39.73 support=39.11 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=9446421.0 spike=0.53
- EOSB.CA: score=13.49 buy_ready=False sector_rank=14 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=218437.25 spike=3.13
- EPCO.CA: score=4.01 buy_ready=False sector_rank=14 price=9.84 support=9.71 resistance=11.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12559152.0 spike=0.84
- EPPK.CA: score=-5.57 buy_ready=False sector_rank=14 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=20.4 buy_ready=False sector_rank=2 price=133.61 support=112.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=79.88 liquidity=114661760.0 spike=0.4
- ETRS.CA: score=5.34 buy_ready=False sector_rank=14 price=10.35 support=10.42 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.19 liquidity=6333385.0 spike=0.5
- EXPA.CA: score=21.88 buy_ready=False sector_rank=8 price=21.94 support=19.96 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.42 liquidity=36994172.0 spike=1.03
- FAIT.CA: score=10.99 buy_ready=False sector_rank=8 price=44.23 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=51.75 liquidity=3174653.75 spike=0.5
- FAITA.CA: score=3.84 buy_ready=False sector_rank=8 price=0.98 support=0.98 resistance=1.01 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=20924.57 spike=0.49
- FERC.CA: score=9.51 buy_ready=False sector_rank=12 price=74.01 support=76.1 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=37.24 liquidity=6045867.5 spike=0.43
- FWRY.CA: score=8.61 buy_ready=False sector_rank=17 price=18.72 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=25.35 liquidity=36660376.0 spike=0.28
- GBCO.CA: score=16.09 buy_ready=False sector_rank=13 price=30.0 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=54.78 liquidity=49779696.0 spike=0.69
- GDWA.CA: score=4.01 buy_ready=False sector_rank=14 price=0.67 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26148506.0 spike=0.6
- GGCC.CA: score=-1.35 buy_ready=False sector_rank=14 price=0.7 support=0.7 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=4642600.0 spike=0.16
- GIHD.CA: score=4.01 buy_ready=False sector_rank=14 price=71.46 support=70.3 resistance=78.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=27035228.0 spike=0.88
- GMCI.CA: score=-1.58 buy_ready=False sector_rank=14 price=1.64 support=1.65 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=21.43 liquidity=413562.62 spike=0.84
- GRCA.CA: score=3.42 buy_ready=False sector_rank=14 price=36.41 support=35.1 resistance=40.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9415800.0 spike=0.21
- GSSC.CA: score=5.04 buy_ready=False sector_rank=14 price=286.32 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=44.16 liquidity=1032157.94 spike=0.12
- GTWL.CA: score=4.01 buy_ready=False sector_rank=14 price=210.54 support=208.0 resistance=227.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=85806384.0 spike=0.56
- HDBK.CA: score=16.82 buy_ready=False sector_rank=8 price=107.79 support=95.51 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=40.67 liquidity=14698816.0 spike=0.25
- HELI.CA: score=12.95 buy_ready=False sector_rank=19 price=7.63 support=7.59 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.78 liquidity=75190624.0 spike=0.45
- HRHO.CA: score=7.24 buy_ready=False sector_rank=18 price=23.65 support=23.91 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=10.53 liquidity=67642504.0 spike=0.68
- ICID.CA: score=15.31 buy_ready=False sector_rank=14 price=17.41 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.55 liquidity=8301993.5 spike=0.84
- IDRE.CA: score=2.7 buy_ready=False sector_rank=14 price=47.15 support=46.0 resistance=53.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8696997.0 spike=0.52
- IFAP.CA: score=11.81 buy_ready=False sector_rank=7 price=19.9 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=36.87 liquidity=6627448.5 spike=0.32
- INFI.CA: score=9.01 buy_ready=False sector_rank=14 price=121.97 support=122.0 resistance=161.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.79 liquidity=12536835.0 spike=0.68
- IRON.CA: score=14.84 buy_ready=False sector_rank=12 price=27.17 support=26.3 resistance=31.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.47 liquidity=9374566.0 spike=0.68
- ISMA.CA: score=8.67 buy_ready=False sector_rank=14 price=26.71 support=27.7 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=9666517.0 spike=0.53
- ISMQ.CA: score=9.47 buy_ready=False sector_rank=12 price=8.26 support=8.35 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=14008849.0 spike=0.57
- ISPH.CA: score=7.72 buy_ready=False sector_rank=15 price=11.55 support=11.5 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.94 liquidity=43403036.0 spike=0.63
- JUFO.CA: score=7.63 buy_ready=False sector_rank=16 price=25.52 support=25.5 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.1 liquidity=16242618.0 spike=0.76
- KABO.CA: score=14.6 buy_ready=False sector_rank=10 price=8.6 support=8.78 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.72 liquidity=10917641.0 spike=0.27
- KWIN.CA: score=1.07 buy_ready=False sector_rank=14 price=84.14 support=84.05 resistance=90.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7065205.0 spike=0.18
- KZPC.CA: score=17.01 buy_ready=False sector_rank=14 price=13.53 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.15 liquidity=12825989.0 spike=0.4
- LCSW.CA: score=7.49 buy_ready=False sector_rank=21 price=31.0 support=31.0 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=19.46 liquidity=12291301.0 spike=0.52
- LUTS.CA: score=4.01 buy_ready=False sector_rank=14 price=0.77 support=0.76 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26850186.0 spike=0.22
- MAAL.CA: score=9.01 buy_ready=False sector_rank=14 price=11.31 support=10.63 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81656192.0 spike=4.46
- MASR.CA: score=9.01 buy_ready=False sector_rank=14 price=7.11 support=7.26 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=16.58 liquidity=49847824.0 spike=0.52
- MBSC.CA: score=7.49 buy_ready=False sector_rank=21 price=323.39 support=325.0 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.55 liquidity=30347580.0 spike=0.69
- MCQE.CA: score=2.49 buy_ready=False sector_rank=21 price=195.35 support=195.06 resistance=208.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=18497370.0 spike=0.74
- MCRO.CA: score=4.01 buy_ready=False sector_rank=14 price=1.49 support=1.48 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39138200.0 spike=0.31
- MENA.CA: score=-1.43 buy_ready=False sector_rank=19 price=6.44 support=6.45 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=29.57 liquidity=620477.0 spike=0.37
- MEPA.CA: score=2.97 buy_ready=False sector_rank=14 price=1.7 support=1.7 resistance=1.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8963544.0 spike=0.23
- MFPC.CA: score=4.47 buy_ready=False sector_rank=12 price=44.63 support=43.17 resistance=47.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=42640844.0 spike=0.24
- MFSC.CA: score=8.94 buy_ready=False sector_rank=14 price=47.85 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.93 liquidity=4875886.5 spike=1.03
- MHOT.CA: score=32.4 buy_ready=False sector_rank=1 price=18.86 support=16.61 resistance=19.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=56.49 liquidity=133366208.0 spike=12.16
- MICH.CA: score=4.01 buy_ready=False sector_rank=14 price=45.11 support=45.0 resistance=49.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12534805.0 spike=0.93
- MILS.CA: score=12.46 buy_ready=False sector_rank=14 price=181.41 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.42 liquidity=8449756.0 spike=0.41
- MIPH.CA: score=1.21 buy_ready=False sector_rank=15 price=766.0 support=760.01 resistance=839.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7489438.0 spike=0.79
- MOED.CA: score=4.01 buy_ready=False sector_rank=14 price=0.66 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=15399644.0 spike=0.24
- MOIL.CA: score=12.48 buy_ready=False sector_rank=5 price=0.71 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=73.02 liquidity=30338.85 spike=0.11
- MOIN.CA: score=12.01 buy_ready=False sector_rank=14 price=34.37 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=26.15 liquidity=28791358.0 spike=1.0
- MOSC.CA: score=0.19 buy_ready=False sector_rank=14 price=283.92 support=281.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=17.29 liquidity=1177897.63 spike=0.21
- MPCI.CA: score=9.01 buy_ready=False sector_rank=14 price=364.77 support=363.63 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=26.37 liquidity=135225488.0 spike=0.98
- MPCO.CA: score=20.18 buy_ready=False sector_rank=7 price=2.49 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=158070352.0 spike=0.89
- MPRC.CA: score=14.01 buy_ready=False sector_rank=14 price=38.3 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=14052014.0 spike=0.38
- MTIE.CA: score=8.09 buy_ready=False sector_rank=13 price=8.1 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.23 liquidity=17670424.0 spike=0.7
- NAHO.CA: score=7.02 buy_ready=False sector_rank=14 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=10646.93 spike=0.18
- NCCW.CA: score=4.01 buy_ready=False sector_rank=14 price=6.65 support=6.44 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26135690.0 spike=0.35
- NEDA.CA: score=3.66 buy_ready=False sector_rank=14 price=2.57 support=2.68 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=652427.56 spike=0.69
- NHPS.CA: score=3.45 buy_ready=False sector_rank=14 price=73.16 support=73.03 resistance=79.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9441952.0 spike=0.59
- NINH.CA: score=9.01 buy_ready=False sector_rank=14 price=19.42 support=19.55 resistance=24.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=23.3 liquidity=11994077.0 spike=0.64
- NIPH.CA: score=3.72 buy_ready=False sector_rank=15 price=308.53 support=303.0 resistance=340.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=56452568.0 spike=0.38
- OBRI.CA: score=2.18 buy_ready=False sector_rank=14 price=26.61 support=25.89 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8170767.5 spike=0.55
- OCDI.CA: score=7.95 buy_ready=False sector_rank=19 price=27.72 support=27.4 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=16.97 liquidity=20877528.0 spike=0.29
- OCPH.CA: score=-3.21 buy_ready=False sector_rank=14 price=211.5 support=207.0 resistance=233.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2782713.5 spike=0.45
- ODIN.CA: score=2.58 buy_ready=False sector_rank=14 price=2.48 support=2.45 resistance=2.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=8569654.0 spike=0.5
- OFH.CA: score=4.11 buy_ready=False sector_rank=14 price=0.91 support=0.91 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=146236224.0 spike=1.05
- OIH.CA: score=20.4 buy_ready=False sector_rank=3 price=2.08 support=1.98 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=38795976.0 spike=0.31
- OLFI.CA: score=3.82 buy_ready=False sector_rank=16 price=22.17 support=22.07 resistance=23.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=34.04 liquidity=3192230.5 spike=0.18
- ORAS.CA: score=4.6 buy_ready=False sector_rank=11 price=810.53 support=809.0 resistance=835.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=39616416.0 spike=1.0
- ORHD.CA: score=12.95 buy_ready=False sector_rank=19 price=39.91 support=39.1 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=121445376.0 spike=0.73
- ORWE.CA: score=12.6 buy_ready=False sector_rank=10 price=27.0 support=25.6 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.78 liquidity=44346596.0 spike=0.79
- PHAR.CA: score=8.72 buy_ready=False sector_rank=15 price=107.54 support=108.1 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.99 liquidity=92577408.0 spike=1.0
- PHDC.CA: score=8.09 buy_ready=False sector_rank=19 price=13.01 support=12.71 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.29 liquidity=157906880.0 spike=1.07
- PHTV.CA: score=5.66 buy_ready=False sector_rank=14 price=346.0 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=44.14 liquidity=1650950.63 spike=1.0
- POUL.CA: score=8.63 buy_ready=False sector_rank=16 price=9.53 support=9.4 resistance=12.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=169051872.0 spike=6.55
- PRCL.CA: score=2.49 buy_ready=False sector_rank=21 price=28.38 support=28.26 resistance=31.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14640434.0 spike=0.84
- PRDC.CA: score=7.95 buy_ready=False sector_rank=19 price=7.12 support=7.14 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.44 liquidity=15533398.0 spike=0.28
- PRMH.CA: score=0.69 buy_ready=False sector_rank=14 price=2.37 support=2.43 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=32.94 liquidity=1686348.0 spike=0.23
- RACC.CA: score=2.7 buy_ready=False sector_rank=14 price=9.09 support=9.2 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=24.04 liquidity=4688590.0 spike=0.29
- RAKT.CA: score=3.06 buy_ready=False sector_rank=14 price=22.08 support=21.2 resistance=23.02 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=48377.28 spike=0.22
- RAYA.CA: score=7.56 buy_ready=False sector_rank=6 price=6.41 support=6.32 resistance=7.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=109501576.0 spike=2.14
- RMDA.CA: score=3.72 buy_ready=False sector_rank=15 price=5.41 support=4.83 resistance=5.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=33733728.0 spike=0.57
- ROTO.CA: score=14.01 buy_ready=False sector_rank=14 price=39.81 support=35.02 resistance=45.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=22.95 liquidity=26015558.0 spike=3.79
- RREI.CA: score=2.56 buy_ready=False sector_rank=14 price=3.93 support=3.86 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.08 liquidity=3551346.25 spike=0.23
- RTVC.CA: score=2.41 buy_ready=False sector_rank=14 price=3.61 support=3.67 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=4077856.5 spike=1.16
- RUBX.CA: score=4.25 buy_ready=False sector_rank=14 price=16.28 support=16.26 resistance=17.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=68090200.0 spike=1.12
- SAUD.CA: score=16.82 buy_ready=False sector_rank=8 price=22.34 support=22.7 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=44.31 liquidity=16969286.0 spike=0.85
- SCEM.CA: score=7.65 buy_ready=False sector_rank=21 price=81.08 support=83.05 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.7 liquidity=95350888.0 spike=1.08
- SCFM.CA: score=4.54 buy_ready=False sector_rank=14 price=249.88 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:12 PM market time freshness=DELAYED_CURRENT RSI=35.83 liquidity=1529113.38 spike=0.23
- SCTS.CA: score=1.98 buy_ready=False sector_rank=4 price=570.68 support=566.66 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=24.5 liquidity=866418.31 spike=0.36
- SDTI.CA: score=9.01 buy_ready=False sector_rank=14 price=86.38 support=79.0 resistance=91.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=163713744.0 spike=6.63
- SEIG.CA: score=0.38 buy_ready=False sector_rank=14 price=226.19 support=222.1 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:11 PM market time freshness=DELAYED_CURRENT RSI=30.53 liquidity=1369050.75 spike=0.73
- SIPC.CA: score=4.01 buy_ready=False sector_rank=14 price=4.82 support=4.81 resistance=5.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=13805037.0 spike=0.19
- SKPC.CA: score=8.47 buy_ready=False sector_rank=12 price=16.34 support=16.8 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.33 liquidity=95567424.0 spike=0.7
- SMFR.CA: score=1.35 buy_ready=False sector_rank=14 price=212.55 support=217.0 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=26.08 liquidity=2340393.5 spike=0.31
- SNFC.CA: score=18.01 buy_ready=False sector_rank=14 price=11.33 support=10.26 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=77.78 liquidity=11453473.0 spike=0.81
- SPIN.CA: score=4.86 buy_ready=False sector_rank=10 price=15.8 support=15.7 resistance=17.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=10905846.0 spike=1.13
- SPMD.CA: score=13.01 buy_ready=False sector_rank=14 price=0.39 support=0.4 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=13810704.0 spike=0.18
- SUGR.CA: score=10.06 buy_ready=False sector_rank=16 price=55.24 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.74 liquidity=3424761.25 spike=0.1
- SVCE.CA: score=4.01 buy_ready=False sector_rank=14 price=10.2 support=10.17 resistance=11.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=44524484.0 spike=0.23
- SWDY.CA: score=7.9 buy_ready=False sector_rank=20 price=113.45 support=116.5 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.54 liquidity=52591352.0 spike=0.83
- TALM.CA: score=21.12 buy_ready=False sector_rank=4 price=19.99 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=58.26 liquidity=23653604.0 spike=0.36
- TMGH.CA: score=8.11 buy_ready=False sector_rank=19 price=90.03 support=90.0 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=17.46 liquidity=313304960.0 spike=1.08
- TRTO.CA: score=-0.98 buy_ready=False sector_rank=14 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-23T21:00:00+00:00 freshness=FRESH RSI=26.47 liquidity=10509.86 spike=0.36
- UEFM.CA: score=-0.88 buy_ready=False sector_rank=14 price=450.64 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:09 PM market time freshness=DELAYED_CURRENT RSI=32.27 liquidity=1107765.5 spike=0.36
- UEGC.CA: score=4.01 buy_ready=False sector_rank=14 price=1.48 support=1.47 resistance=1.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=30319882.0 spike=0.63
- UNIP.CA: score=3.63 buy_ready=False sector_rank=14 price=0.34 support=0.33 resistance=0.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=9626563.0 spike=0.45
- UNIT.CA: score=4.68 buy_ready=False sector_rank=19 price=17.04 support=16.66 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.51 liquidity=1724141.5 spike=0.12
- WCDF.CA: score=10.43 buy_ready=False sector_rank=14 price=658.79 support=640.0 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=52.17 liquidity=3419338.5 spike=0.66
- WKOL.CA: score=-0.29 buy_ready=False sector_rank=14 price=308.99 support=307.5 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=5699210.0 spike=0.42
- ZEOT.CA: score=1.88 buy_ready=False sector_rank=14 price=11.77 support=12.25 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=26.7 liquidity=2876024.25 spike=0.47
- ZMID.CA: score=7.95 buy_ready=False sector_rank=19 price=7.82 support=7.92 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.57 liquidity=188722576.0 spike=0.98

## Backtesting Lite
- MHOT.CA: 180d return=-25.13%, max drawdown=-54.07%, MA20>MA50 days last20=16, as_of=2026-09-23T21:00:00+00:00
- CIRA.CA: 180d return=124.28%, max drawdown=-16.44%, MA20>MA50 days last20=20, as_of=2026-09-23T21:00:00+00:00
- CANA.CA: 180d return=12.54%, max drawdown=-36.46%, MA20>MA50 days last20=20, as_of=2026-09-23T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- CIRA.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Investment and Real Estate Development summary=CIRA Education take over 51% of L’École Française Hurghada; CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion; CIRA Education launches Middle East’s 1st initiative for care economy
  - CIRA Education take over 51% of L’École Française Hurghada: https://english.mubasher.info/news/4488666/CIRA-Education-take-over-51-of-L-%C3%89cole-Fran%C3%A7aise-Hurghada/
  - CIRA’s majority shareholder acquires 37.5% additional equity, backs regional expansion: https://english.mubasher.info/news/4393636/CIRA-s-majority-shareholder-acquires-37-5-additional-equity-backs-regional-expansion/
  - CIRA Education launches Middle East’s 1st initiative for care economy: https://english.mubasher.info/news/4391766/CIRA-Education-launches-Middle-East-s-1st-initiative-for-care-economy/
- CANA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=634 sources=3 expected=Suez Canal Bank summary=Suez Canal Bank delivers EGP 1.6bn profits in Q1-26; Suez Canal Bank unveils details for previous dividends payout; Suez Canal Bank to distribute EGP 5bn bonus shares for 2025
  - Suez Canal Bank delivers EGP 1.6bn profits in Q1-26: https://english.mubasher.info/news/4611255/Suez-Canal-Bank-delivers-EGP-1-6bn-profits-in-Q1-26/
  - Suez Canal Bank unveils details for previous dividends payout: https://english.mubasher.info/news/4586807/Suez-Canal-Bank-unveils-details-for-previous-dividends-payout/
  - Suez Canal Bank to distribute EGP 5bn bonus shares for 2025: https://english.mubasher.info/news/4581661/Suez-Canal-Bank-to-distribute-EGP-5bn-bonus-shares-for-2025/
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- TALM.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Talim Management Services summary=Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- EGTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Resorts Company summary=Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- ETEL.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Telecom Egypt summary=Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- OIH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Orascom Investment Holding summary=Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.

## Warnings
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CIRA.CA matches the company but no source/report date was detected.
- Evidence for CANA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for TALM.CA: source text did not clearly match TALM.CA / Talim Management Services.
- Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- Evidence rejected for ETEL.CA: source text did not clearly match ETEL.CA / Telecom Egypt.
- Evidence rejected for OIH.CA: source text did not clearly match OIH.CA / Orascom Investment Holding.
