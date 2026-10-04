# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-10-04T11:19:08.521454+00:00
Generated Cairo: 2026-10-04 14:19
Run timing: target 08:45 Cairo | generated Cairo 2026-10-04 14:19 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-10-04 14:16

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 172/187
- Top sector: Fintech & Payments

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, October 04
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 17.65% / above MA50 47.06%
- EGX70 regime: BEARISH / above MA20 31.58% / above MA50 28.95%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=497326112.0 spike=0.6 score=21.4
- ETEL.CA: liquidity=414641088.0 spike=1.37 score=4.93
- HRHO.CA: liquidity=385814176.0 spike=5.06 score=9.36
- BIOC.CA: liquidity=317506848.0 spike=4.25 score=27.83
- TMGH.CA: liquidity=242770560.0 spike=0.89 score=7.08

## AI Narrative
- Provider: OpenRouter OK
- Model: nvidia/nemotron-3-super-120b-a12b:free
- Summary: EGX30/EGX70 bearish, sector breadth low, defensive risk mode; scanner flags accumulation spikes and bullish‑watch outlook on select stocks but maintains HOLD due to market weakness.
- Liquidity accumulation spikes on ALCN.CA, BIOC.CA, EFIH.CA, FWRY.CA indicate short‑term buying interest, yet prices sit near resistance or above support with limited upside space.
- Sector leadership in Fintech & Payments, Energy & Petrochemicals, Education shows relative strength, but overall EGX breadth (<24%) keeps the market defensive.
- Support/resistance distances (e.g., EFIH.CA ~0.5% below resistance, FWRY.CA ~3.8% above support) reveal tight ranges; any breakout would need confirmation amid the bearish EGX30/EGX70 trend.
- Outlook scores are bullish watch (70‑100) but confidence is LOW; uncertainty remains high until the regime shifts from defensive to neutral/ bullish.

## Top Liquidity Spikes
- MCQE.CA: spike=6.19 liquidity=131054504.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- OBRI.CA: spike=5.74 liquidity=55893872.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ARCC.CA: spike=5.64 liquidity=120507400.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- HRHO.CA: spike=5.06 liquidity=385814176.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- BIOC.CA: spike=4.25 liquidity=317506848.0 outlook=BULLISH_WATCH score=78 buy_ready=False

## Sector Leaderboard
- #1 Fintech & Payments: score=9.18 5d=1.18% 20d=-0.61% aboveMA50=100.0%
- #2 Energy & Petrochemicals: score=9.11 5d=2.58% 20d=4.07% aboveMA50=100.0%
- #3 Education: score=7.13 5d=0.56% 20d=12.26% aboveMA50=66.67%
- #4 Textiles: score=6.29 5d=2.17% 20d=1.25% aboveMA50=75.0%
- #5 Automotive & Distribution: score=6.25 5d=1.46% 20d=0.21% aboveMA50=50.0%
- #6 Investment Holding: score=6.17 5d=-2.96% 20d=14.67% aboveMA50=66.67%
- #7 Building Materials: score=5.76 5d=0.0% 20d=0.0% aboveMA50=0.0%
- #8 Transportation & Logistics: score=4.81 5d=-0.48% 20d=-5.2% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- FWRY.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- EGAS.CA: BULLISH_WATCH score=95.11 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- EFIH.CA: BULLISH_WATCH score=94.18 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=close to resistance
- AMOC.CA: BULLISH_WATCH score=94.11 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- CIRA.CA: BULLISH_WATCH score=93.13 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ORWE.CA: BULLISH_WATCH score=87.29 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- GBCO.CA: BULLISH_WATCH score=87.25 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- TALM.CA: BULLISH_WATCH score=83.13 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; far above support
- ACGC.CA: BULLISH_WATCH score=82.29 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- BIOC.CA: BULLISH_WATCH score=78 liquidity=ACCUMULATION_SPIKE sector=LAGGING risk=momentum is extended; far above support; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=5.41 buy_ready=False sector_rank=16 price=260.29 support=230.11 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=25.94 liquidity=6579640.5 spike=0.28
- ABUK.CA: score=16.61 buy_ready=False sector_rank=17 price=88.72 support=83.55 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=42.28 liquidity=39785400.0 spike=0.32
- ACAMD.CA: score=15.83 buy_ready=False sector_rank=16 price=2.04 support=1.87 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=34125848.0 spike=0.68
- ACGC.CA: score=18.12 buy_ready=False sector_rank=4 price=14.64 support=13.11 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=45.35 liquidity=6719537.5 spike=0.26
- ADCI.CA: score=6.36 buy_ready=False sector_rank=16 price=274.04 support=256.0 resistance=298.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=2528770.0 spike=1.0
- ADIB.CA: score=15.14 buy_ready=False sector_rank=9 price=49.96 support=48.2 resistance=54.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=39.56 liquidity=70749224.0 spike=0.92
- ADPC.CA: score=4.39 buy_ready=False sector_rank=16 price=3.64 support=3.4 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=34.74 liquidity=6557180.0 spike=0.38
- AFDI.CA: score=8.63 buy_ready=False sector_rank=16 price=52.05 support=47.7 resistance=56.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=48.59 liquidity=4797249.5 spike=0.61
- AFMC.CA: score=17.83 buy_ready=False sector_rank=16 price=161.86 support=131.0 resistance=188.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=48.74 liquidity=24075282.0 spike=0.46
- AJWA.CA: score=17.83 buy_ready=False sector_rank=16 price=180.02 support=175.15 resistance=188.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=54.55 liquidity=13660802.0 spike=0.97
- ALCN.CA: score=27.9 buy_ready=False sector_rank=8 price=34.97 support=30.4 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=62.15 liquidity=105739688.0 spike=3.49
- ALUM.CA: score=3.63 buy_ready=False sector_rank=16 price=24.56 support=21.65 resistance=29.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=29.87 liquidity=4802847.5 spike=0.82
- AMER.CA: score=13.08 buy_ready=False sector_rank=19 price=4.61 support=4.05 resistance=5.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=27459740.0 spike=0.68
- AMES.CA: score=3.83 buy_ready=False sector_rank=16 price=50.02 support=46.0 resistance=51.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=181973296.0 spike=0.75
- AMIA.CA: score=18.83 buy_ready=False sector_rank=16 price=18.88 support=17.12 resistance=20.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=11477273.0 spike=0.55
- AMOC.CA: score=23.4 buy_ready=False sector_rank=2 price=13.91 support=12.18 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=56.56 liquidity=114702368.0 spike=0.84
- APSW.CA: score=3.41 buy_ready=False sector_rank=16 price=8.1 support=7.81 resistance=8.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=578963.94 spike=0.89
- ARAB.CA: score=15.1 buy_ready=False sector_rank=19 price=0.25 support=0.2 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=42.5 liquidity=71181200.0 spike=1.01
- ARCC.CA: score=11.3 buy_ready=False sector_rank=7 price=73.96 support=67.7 resistance=74.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=120507400.0 spike=5.64
- AREH.CA: score=7.83 buy_ready=False sector_rank=16 price=1.33 support=1.14 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=10221081.0 spike=0.79
- ASCM.CA: score=10.2 buy_ready=False sector_rank=16 price=59.26 support=53.8 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=35.05 liquidity=6374733.0 spike=0.4
- ASPI.CA: score=8.83 buy_ready=False sector_rank=16 price=0.38 support=0.33 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=31.73 liquidity=10632071.0 spike=0.21
- ATLC.CA: score=11.28 buy_ready=False sector_rank=13 price=6.27 support=5.2 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=37.67 liquidity=3920224.5 spike=0.23
- ATQA.CA: score=11.61 buy_ready=False sector_rank=17 price=11.79 support=10.91 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=31.34 liquidity=47307876.0 spike=0.54
- AXPH.CA: score=5.23 buy_ready=False sector_rank=16 price=1533.88 support=1334.35 resistance=1987.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=32.21 liquidity=3399725.75 spike=0.5
- BINV.CA: score=17.47 buy_ready=False sector_rank=6 price=59.99 support=49.51 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=68.72 liquidity=6074432.0 spike=0.24
- BIOC.CA: score=27.83 buy_ready=False sector_rank=16 price=357.06 support=225.21 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=63.85 liquidity=317506848.0 spike=4.25
- BTFH.CA: score=13.36 buy_ready=False sector_rank=13 price=2.85 support=2.65 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=43.24 liquidity=72770600.0 spike=0.79
- CAED.CA: score=13.02 buy_ready=False sector_rank=16 price=123.72 support=103.1 resistance=152.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=45.12 liquidity=9195613.0 spike=0.46
- CANA.CA: score=20.8 buy_ready=False sector_rank=9 price=46.1 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=63.37 liquidity=31263360.0 spike=1.33
- CCAP.CA: score=21.4 buy_ready=False sector_rank=6 price=6.79 support=5.97 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=61.89 liquidity=497326112.0 spike=0.6
- CCRS.CA: score=8.83 buy_ready=False sector_rank=16 price=2.42 support=2.21 resistance=2.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:52 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=5004124.5 spike=0.3
- CEFM.CA: score=12.82 buy_ready=False sector_rank=16 price=142.49 support=113.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=40.94 liquidity=3991478.0 spike=0.52
- CERA.CA: score=18.19 buy_ready=False sector_rank=16 price=1.44 support=1.18 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=41.67 liquidity=236239680.0 spike=1.68
- CFGH.CA: score=-2.17 buy_ready=False sector_rank=16 price=0.11 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=10.0 liquidity=0.0 spike=0.0
- CICH.CA: score=11.41 buy_ready=False sector_rank=13 price=12.14 support=10.75 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=39.44 liquidity=2049347.75 spike=0.35
- CIEB.CA: score=10.01 buy_ready=False sector_rank=9 price=24.37 support=23.0 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=36.7 liquidity=4867707.5 spike=0.4
- CIRA.CA: score=22.4 buy_ready=False sector_rank=3 price=39.68 support=35.56 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=54.97 liquidity=17164778.0 spike=0.48
- CLHO.CA: score=16.52 buy_ready=False sector_rank=11 price=16.06 support=13.9 resistance=17.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=24567062.0 spike=0.48
- CNFN.CA: score=6.33 buy_ready=False sector_rank=13 price=4.23 support=3.84 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=26.4 liquidity=7973219.0 spike=0.82
- COMI.CA: score=9.14 buy_ready=False sector_rank=9 price=127.51 support=124.5 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=146670016.0 spike=0.26
- COPR.CA: score=19.09 buy_ready=False sector_rank=16 price=0.51 support=0.44 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=54.62 liquidity=32662510.0 spike=1.13
- COSG.CA: score=8.83 buy_ready=False sector_rank=16 price=1.65 support=1.46 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=27.12 liquidity=12423975.0 spike=0.59
- CPCI.CA: score=14.09 buy_ready=False sector_rank=16 price=606.37 support=530.0 resistance=600.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=87.11 liquidity=5342546.5 spike=1.46
- CSAG.CA: score=11.22 buy_ready=False sector_rank=8 price=37.7 support=34.52 resistance=42.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=5293775.0 spike=0.56
- DAPH.CA: score=8.83 buy_ready=False sector_rank=16 price=95.8 support=89.1 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=22727090.0 spike=0.88
- DEIN.CA: score=6.83 buy_ready=False sector_rank=16 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=2.94 buy_ready=False sector_rank=18 price=25.71 support=23.81 resistance=29.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=32.67 liquidity=5363654.0 spike=1.13
- DSCW.CA: score=7.95 buy_ready=False sector_rank=16 price=1.72 support=1.58 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=27.03 liquidity=22997374.0 spike=1.06
- DTPP.CA: score=11.83 buy_ready=False sector_rank=16 price=295.12 support=250.01 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=28.93 liquidity=23254170.0 spike=0.27
- EALR.CA: score=0.0 buy_ready=False sector_rank=16 price=343.2 support=312.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=29.44 liquidity=2175380.25 spike=0.19
- EASB.CA: score=1.49 buy_ready=False sector_rank=16 price=7.93 support=7.25 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=7659108.5 spike=0.53
- EAST.CA: score=7.32 buy_ready=False sector_rank=18 price=29.38 support=27.91 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=15.77 liquidity=33246234.0 spike=0.7
- EBSC.CA: score=-3.14 buy_ready=False sector_rank=16 price=1.84 support=1.77 resistance=1.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=3027976.25 spike=0.64
- ECAP.CA: score=4.08 buy_ready=False sector_rank=16 price=30.66 support=29.13 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=31.59 liquidity=5109455.5 spike=1.07
- EDFM.CA: score=6.45 buy_ready=False sector_rank=16 price=402.26 support=354.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=38.52 liquidity=2086043.75 spike=1.27
- EEII.CA: score=12.99 buy_ready=False sector_rank=16 price=2.18 support=2.02 resistance=2.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=11804943.0 spike=1.08
- EFIC.CA: score=7.61 buy_ready=False sector_rank=17 price=171.79 support=147.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=21.31 liquidity=20847674.0 spike=0.06
- EFID.CA: score=7.82 buy_ready=False sector_rank=18 price=19.29 support=18.1 resistance=32.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=13.33 liquidity=81401792.0 spike=1.25
- EFIH.CA: score=26.24 buy_ready=False sector_rank=1 price=23.89 support=20.2 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=47.31 liquidity=94408192.0 spike=1.92
- EGAL.CA: score=14.89 buy_ready=False sector_rank=17 price=346.01 support=331.5 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=27.34 liquidity=122963272.0 spike=2.64
- EGAS.CA: score=19.4 buy_ready=False sector_rank=2 price=57.9 support=53.62 resistance=60.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=5997867.5 spike=0.5
- EGBE.CA: score=12.63 buy_ready=False sector_rank=9 price=0.53 support=0.49 resistance=0.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=55.77 liquidity=213472.52 spike=2.14
- EGCH.CA: score=13.61 buy_ready=False sector_rank=17 price=13.67 support=12.88 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=41.92 liquidity=40748976.0 spike=0.37
- EGSA.CA: score=-0.81 buy_ready=False sector_rank=14 price=8.85 support=8.82 resistance=9.1 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=9.52 liquidity=79.65 spike=0.01
- EGTS.CA: score=13.36 buy_ready=False sector_rank=19 price=16.41 support=15.65 resistance=19.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=44.79 liquidity=40349220.0 spike=1.14
- EHDR.CA: score=5.36 buy_ready=False sector_rank=16 price=2.56 support=2.35 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=23.94 liquidity=6532368.5 spike=0.42
- ELEC.CA: score=13.12 buy_ready=False sector_rank=15 price=1.92 support=1.72 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=22566656.0 spike=0.33
- ELKA.CA: score=13.78 buy_ready=False sector_rank=16 price=1.64 support=1.43 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=35.56 liquidity=9948037.0 spike=0.64
- ELNA.CA: score=-0.03 buy_ready=False sector_rank=16 price=35.22 support=33.46 resistance=38.99 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=140774.34 spike=0.45
- ELSH.CA: score=9.47 buy_ready=False sector_rank=16 price=12.14 support=10.8 resistance=14.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=34539740.0 spike=1.32
- ELWA.CA: score=-0.37 buy_ready=False sector_rank=16 price=1.46 support=1.43 resistance=1.9 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=5.41 liquidity=1239599.89 spike=1.28
- EMFD.CA: score=11.08 buy_ready=False sector_rank=19 price=12.81 support=11.7 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=31.41 liquidity=31927588.0 spike=0.33
- ENGC.CA: score=8.83 buy_ready=False sector_rank=16 price=37.67 support=33.33 resistance=46.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=30.88 liquidity=14014983.0 spike=0.81
- EOSB.CA: score=8.83 buy_ready=False sector_rank=16 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=301.44 spike=0.01
- EPCO.CA: score=1.89 buy_ready=False sector_rank=16 price=10.19 support=9.25 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:54 PM market time freshness=DELAYED_CURRENT RSI=33.15 liquidity=3058752.75 spike=0.21
- EPPK.CA: score=-5.75 buy_ready=False sector_rank=16 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=4.93 buy_ready=False sector_rank=14 price=149.78 support=139.1 resistance=154.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=414641088.0 spike=1.37
- ETRS.CA: score=17.19 buy_ready=False sector_rank=16 price=10.93 support=9.82 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=40.53 liquidity=8358461.0 spike=0.92
- EXPA.CA: score=18.14 buy_ready=False sector_rank=9 price=21.39 support=20.4 resistance=22.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=23127906.0 spike=0.68
- FAIT.CA: score=10.35 buy_ready=False sector_rank=9 price=45.89 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=40.51 liquidity=2208241.25 spike=0.43
- FAITA.CA: score=5.46 buy_ready=False sector_rank=9 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=37084.82 spike=1.14
- FERC.CA: score=4.49 buy_ready=False sector_rank=17 price=77.0 support=70.42 resistance=82.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=41.65 liquidity=1878668.75 spike=0.22
- FWRY.CA: score=26.12 buy_ready=False sector_rank=1 price=19.05 support=17.5 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=43.17 liquidity=180166848.0 spike=1.86
- GBCO.CA: score=23.56 buy_ready=False sector_rank=5 price=32.3 support=27.0 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=54.16 liquidity=181625600.0 spike=2.08
- GDWA.CA: score=7.83 buy_ready=False sector_rank=16 price=0.68 support=0.61 resistance=0.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=17.88 liquidity=14540819.0 spike=0.44
- GGCC.CA: score=4.79 buy_ready=False sector_rank=16 price=0.73 support=0.7 resistance=0.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=22865374.0 spike=1.48
- GIHD.CA: score=8.83 buy_ready=False sector_rank=16 price=66.0 support=60.9 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=28.8 liquidity=15541941.0 spike=0.56
- GMCI.CA: score=-1.85 buy_ready=False sector_rank=16 price=1.62 support=1.49 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:57 PM market time freshness=DELAYED_CURRENT RSI=20.83 liquidity=319001.38 spike=0.68
- GRCA.CA: score=7.83 buy_ready=False sector_rank=16 price=38.75 support=32.11 resistance=63.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=27.89 liquidity=10795207.0 spike=0.37
- GSSC.CA: score=4.45 buy_ready=False sector_rank=16 price=279.48 support=246.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=41.04 liquidity=625252.38 spike=0.11
- GTWL.CA: score=8.83 buy_ready=False sector_rank=16 price=176.2 support=124.5 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=26.96 liquidity=141636720.0 spike=0.89
- HDBK.CA: score=18.14 buy_ready=False sector_rank=9 price=111.62 support=102.03 resistance=123.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=52.26 liquidity=13569712.0 spike=0.35
- HELI.CA: score=13.08 buy_ready=False sector_rank=19 price=7.48 support=6.94 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=42.51 liquidity=32607818.0 spike=0.24
- HRHO.CA: score=9.36 buy_ready=False sector_rank=13 price=25.78 support=24.21 resistance=26.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=385814176.0 spike=5.06
- ICID.CA: score=12.78 buy_ready=False sector_rank=16 price=18.52 support=16.52 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=49.24 liquidity=3953055.25 spike=0.51
- IDRE.CA: score=9.08 buy_ready=False sector_rank=16 price=50.72 support=45.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=43.37 liquidity=5247840.0 spike=0.34
- IFAP.CA: score=2.95 buy_ready=False sector_rank=12 price=19.75 support=17.17 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=34.32 liquidity=3510623.0 spike=0.23
- INFI.CA: score=7.4 buy_ready=False sector_rank=16 price=126.6 support=104.0 resistance=152.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=30.58 liquidity=8570707.0 spike=0.61
- IRON.CA: score=13.54 buy_ready=False sector_rank=17 price=27.87 support=25.01 resistance=30.76 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=40.72 liquidity=8928287.0 spike=0.69
- ISMA.CA: score=6.04 buy_ready=False sector_rank=16 price=26.37 support=22.7 resistance=34.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=7209638.5 spike=0.5
- ISMQ.CA: score=9.77 buy_ready=False sector_rank=17 price=8.43 support=7.6 resistance=9.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=30.08 liquidity=32520758.0 spike=1.58
- ISPH.CA: score=9.52 buy_ready=False sector_rank=11 price=11.94 support=11.22 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=27.35 liquidity=59784280.0 spike=0.82
- JUFO.CA: score=7.36 buy_ready=False sector_rank=18 price=25.7 support=24.4 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=26.91 liquidity=19056208.0 spike=1.02
- KABO.CA: score=21.4 buy_ready=False sector_rank=4 price=9.21 support=7.97 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=40.05 liquidity=10088258.0 spike=0.3
- KWIN.CA: score=9.52 buy_ready=False sector_rank=16 price=81.3 support=72.21 resistance=106.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=35.38 liquidity=5693711.5 spike=0.38
- KZPC.CA: score=11.36 buy_ready=False sector_rank=16 price=13.01 support=12.15 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=36.47 liquidity=4530376.5 spike=0.16
- LCSW.CA: score=17.52 buy_ready=False sector_rank=7 price=33.47 support=28.86 resistance=36.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=44.44 liquidity=9214671.0 spike=0.55
- LUTS.CA: score=18.83 buy_ready=False sector_rank=16 price=0.95 support=0.72 resistance=1.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=48.2 liquidity=46297192.0 spike=0.46
- MAAL.CA: score=18.83 buy_ready=False sector_rank=16 price=10.83 support=8.18 resistance=12.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=68.98 liquidity=21071686.0 spike=0.97
- MASR.CA: score=13.83 buy_ready=False sector_rank=16 price=7.75 support=6.82 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=36.82 liquidity=35809060.0 spike=0.39
- MBSC.CA: score=11.3 buy_ready=False sector_rank=7 price=356.64 support=306.98 resistance=356.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=159328128.0 spike=4.07
- MCQE.CA: score=11.3 buy_ready=False sector_rank=7 price=217.65 support=195.02 resistance=224.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=131054504.0 spike=6.19
- MCRO.CA: score=16.83 buy_ready=False sector_rank=16 price=1.59 support=1.41 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=40.35 liquidity=80587800.0 spike=0.66
- MENA.CA: score=-0.5 buy_ready=False sector_rank=19 price=6.36 support=5.8 resistance=6.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=32.23 liquidity=1259438.63 spike=1.08
- MEPA.CA: score=6.69 buy_ready=False sector_rank=16 price=1.76 support=1.56 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=7862508.5 spike=0.22
- MFPC.CA: score=16.61 buy_ready=False sector_rank=17 price=46.99 support=43.0 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=46.2 liquidity=37225840.0 spike=0.3
- MFSC.CA: score=4.85 buy_ready=False sector_rank=16 price=46.51 support=42.5 resistance=51.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=47.58 liquidity=1026916.31 spike=0.33
- MHOT.CA: score=11.81 buy_ready=False sector_rank=21 price=17.7 support=16.2 resistance=21.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=42.93 liquidity=14336859.0 spike=0.79
- MICH.CA: score=12.47 buy_ready=False sector_rank=16 price=47.72 support=42.01 resistance=52.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=36.48 liquidity=5644557.5 spike=0.51
- MILS.CA: score=8.83 buy_ready=False sector_rank=16 price=185.08 support=165.5 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:59 PM market time freshness=DELAYED_CURRENT RSI=34.44 liquidity=12254753.0 spike=0.67
- MIPH.CA: score=9.09 buy_ready=False sector_rank=11 price=819.17 support=739.69 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:56 PM market time freshness=DELAYED_CURRENT RSI=51.24 liquidity=1567045.13 spike=0.17
- MOED.CA: score=7.83 buy_ready=False sector_rank=16 price=0.7 support=0.59 resistance=0.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=28.19 liquidity=13581340.0 spike=0.31
- MOIL.CA: score=10.63 buy_ready=False sector_rank=2 price=0.7 support=0.67 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=78.57 liquidity=229690.97 spike=0.91
- MOIN.CA: score=11.51 buy_ready=False sector_rank=16 price=34.98 support=32.0 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=4683045.5 spike=0.18
- MOSC.CA: score=1.82 buy_ready=False sector_rank=16 price=287.39 support=257.0 resistance=329.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=34.93 liquidity=2994523.5 spike=0.82
- MPCI.CA: score=9.59 buy_ready=False sector_rank=16 price=360.64 support=305.45 resistance=455.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=23.8 liquidity=149190800.0 spike=1.38
- MPCO.CA: score=17.44 buy_ready=False sector_rank=12 price=2.52 support=2.17 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=41.1 liquidity=102961576.0 spike=0.53
- MPRC.CA: score=17.83 buy_ready=False sector_rank=16 price=39.99 support=37.65 resistance=43.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=44.54 liquidity=10836824.0 spike=0.42
- MTIE.CA: score=16.24 buy_ready=False sector_rank=5 price=8.15 support=7.5 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=43.62 liquidity=27242898.0 spike=1.42
- NAHO.CA: score=3.84 buy_ready=False sector_rank=16 price=0.13 support=0.12 resistance=0.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:59 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=7060.03 spike=0.16
- NCCW.CA: score=18.83 buy_ready=False sector_rank=16 price=7.45 support=6.06 resistance=8.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=38.48 liquidity=31236350.0 spike=0.41
- NEDA.CA: score=4.02 buy_ready=False sector_rank=16 price=2.61 support=2.48 resistance=2.89 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=35.71 liquidity=187640.72 spike=0.2
- NHPS.CA: score=14.21 buy_ready=False sector_rank=16 price=75.01 support=66.0 resistance=88.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=37.93 liquidity=17430080.0 spike=1.19
- NINH.CA: score=9.71 buy_ready=False sector_rank=16 price=19.9 support=18.53 resistance=24.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=27.11 liquidity=21128486.0 spike=1.44
- NIPH.CA: score=20.0 buy_ready=False sector_rank=11 price=332.54 support=290.0 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=49.32 liquidity=152513360.0 spike=1.24
- OBRI.CA: score=8.83 buy_ready=False sector_rank=16 price=29.44 support=25.8 resistance=30.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=55893872.0 spike=5.74
- OCDI.CA: score=8.08 buy_ready=False sector_rank=19 price=27.38 support=24.2 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=24.59 liquidity=29654584.0 spike=0.57
- OCPH.CA: score=1.93 buy_ready=False sector_rank=16 price=234.92 support=190.0 resistance=263.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=33.98 liquidity=4105687.25 spike=0.86
- ODIN.CA: score=10.41 buy_ready=False sector_rank=16 price=2.6 support=2.35 resistance=3.06 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=39.22 liquidity=6580367.5 spike=0.6
- OFH.CA: score=13.83 buy_ready=False sector_rank=16 price=0.93 support=0.83 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=36.07 liquidity=32197014.0 spike=0.24
- OIH.CA: score=11.4 buy_ready=False sector_rank=6 price=1.87 support=1.7 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=23.64 liquidity=30557218.0 spike=0.28
- OLFI.CA: score=13.36 buy_ready=False sector_rank=18 price=21.52 support=21.2 resistance=23.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=35.39 liquidity=23236600.0 spike=1.52
- ORAS.CA: score=4.6 buy_ready=False sector_rank=10 price=825.53 support=822.0 resistance=845.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=136477536.0 spike=1.0
- ORHD.CA: score=8.08 buy_ready=False sector_rank=19 price=39.39 support=37.41 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=30.89 liquidity=117672056.0 spike=0.72
- ORWE.CA: score=21.52 buy_ready=False sector_rank=4 price=27.54 support=26.01 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=57206004.0 spike=1.06
- PHAR.CA: score=14.52 buy_ready=False sector_rank=11 price=117.35 support=102.0 resistance=132.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=66500820.0 spike=0.81
- PHDC.CA: score=8.12 buy_ready=False sector_rank=19 price=13.01 support=12.36 resistance=15.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=32.17 liquidity=121330584.0 spike=1.02
- PHTV.CA: score=4.66 buy_ready=False sector_rank=16 price=336.49 support=315.1 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:48 PM market time freshness=DELAYED_CURRENT RSI=42.2 liquidity=827508.5 spike=0.52
- POUL.CA: score=7.58 buy_ready=False sector_rank=18 price=10.1 support=9.12 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=4.78 liquidity=37112352.0 spike=1.13
- PRCL.CA: score=9.51 buy_ready=False sector_rank=7 price=26.58 support=22.8 resistance=34.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=32.6 liquidity=8209322.5 spike=0.53
- PRDC.CA: score=8.08 buy_ready=False sector_rank=19 price=7.49 support=6.81 resistance=8.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=11709767.0 spike=0.4
- PRMH.CA: score=2.93 buy_ready=False sector_rank=16 price=2.31 support=2.03 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT RSI=29.17 liquidity=4098886.5 spike=0.9
- RACC.CA: score=14.31 buy_ready=False sector_rank=16 price=9.4 support=8.51 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=14388060.0 spike=1.24
- RAKT.CA: score=0.38 buy_ready=False sector_rank=16 price=21.69 support=20.26 resistance=23.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=27.32 liquidity=373634.47 spike=2.09
- RAYA.CA: score=12.81 buy_ready=False sector_rank=20 price=6.84 support=5.72 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=38.07 liquidity=26810230.0 spike=0.57
- RMDA.CA: score=9.52 buy_ready=False sector_rank=11 price=5.54 support=4.83 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=23.33 liquidity=20868216.0 spike=0.39
- ROTO.CA: score=10.32 buy_ready=False sector_rank=16 price=39.63 support=35.02 resistance=44.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=41.37 liquidity=6495277.0 spike=0.82
- RREI.CA: score=1.95 buy_ready=False sector_rank=16 price=3.9 support=3.53 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=32.61 liquidity=3120273.5 spike=0.26
- RTVC.CA: score=2.24 buy_ready=False sector_rank=16 price=3.63 support=3.37 resistance=4.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=24.21 liquidity=3569563.75 spike=1.42
- RUBX.CA: score=18.83 buy_ready=False sector_rank=16 price=15.81 support=12.59 resistance=18.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=58.37 liquidity=43978788.0 spike=0.61
- SAUD.CA: score=20.14 buy_ready=False sector_rank=9 price=23.83 support=21.6 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=46.95 liquidity=11980185.0 spike=0.61
- SCEM.CA: score=10.18 buy_ready=False sector_rank=7 price=89.78 support=81.67 resistance=89.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:02 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=186467744.0 spike=2.94
- SCFM.CA: score=-1.11 buy_ready=False sector_rank=16 price=251.32 support=223.11 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=34.6 liquidity=1065511.5 spike=0.18
- SCTS.CA: score=2.99 buy_ready=False sector_rank=3 price=556.9 support=520.3 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=23.45 liquidity=594721.63 spike=0.3
- SDTI.CA: score=15.83 buy_ready=False sector_rank=16 price=83.98 support=70.0 resistance=94.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=79.77 liquidity=13991468.0 spike=0.41
- SEIG.CA: score=-4.95 buy_ready=False sector_rank=16 price=239.2 support=222.0 resistance=240.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:51 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=1224865.13 spike=0.72
- SIPC.CA: score=11.83 buy_ready=False sector_rank=16 price=5.22 support=4.22 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=32.26 liquidity=18313510.0 spike=0.27
- SKPC.CA: score=7.61 buy_ready=False sector_rank=17 price=16.29 support=15.4 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=27.56 liquidity=53602680.0 spike=0.52
- SMFR.CA: score=1.2 buy_ready=False sector_rank=16 price=229.99 support=205.01 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=29.66 liquidity=2367155.0 spike=0.37
- SNFC.CA: score=15.66 buy_ready=False sector_rank=16 price=11.5 support=10.58 resistance=11.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=72.09 liquidity=4831367.5 spike=0.36
- SPIN.CA: score=5.74 buy_ready=False sector_rank=4 price=17.0 support=15.11 resistance=20.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=29.87 liquidity=4339418.0 spike=0.59
- SPMD.CA: score=11.22 buy_ready=False sector_rank=16 price=0.39 support=0.36 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=44.5 liquidity=8395014.0 spike=0.11
- SUGR.CA: score=11.32 buy_ready=False sector_rank=18 price=55.06 support=50.5 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:58 PM market time freshness=DELAYED_CURRENT RSI=23.29 liquidity=10531121.0 spike=0.47
- SVCE.CA: score=5.65 buy_ready=False sector_rank=16 price=10.85 support=10.41 resistance=11.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=235580640.0 spike=1.91
- SWDY.CA: score=17.12 buy_ready=False sector_rank=15 price=120.03 support=102.31 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=41.84 liquidity=68407048.0 spike=0.92
- TALM.CA: score=22.4 buy_ready=False sector_rank=3 price=21.2 support=17.61 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=59.94 liquidity=16342846.0 spike=0.24
- TMGH.CA: score=7.08 buy_ready=False sector_rank=19 price=89.29 support=84.4 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=13.53 liquidity=242770560.0 spike=0.89
- TRTO.CA: score=-1.17 buy_ready=False sector_rank=16 price=0.05 support=0.05 resistance=0.08 source=Yahoo Finance as_of=2026-09-30T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=4842.83 spike=0.28
- UEFM.CA: score=9.46 buy_ready=False sector_rank=16 price=511.47 support=407.57 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=45.7 liquidity=1635335.0 spike=0.4
- UEGC.CA: score=13.83 buy_ready=False sector_rank=16 price=1.61 support=1.37 resistance=1.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=35.94 liquidity=34573772.0 spike=0.98
- UNIP.CA: score=13.83 buy_ready=False sector_rank=16 price=0.36 support=0.32 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=38.21 liquidity=12159083.0 spike=0.61
- UNIT.CA: score=4.61 buy_ready=False sector_rank=19 price=17.63 support=16.41 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:53 PM market time freshness=DELAYED_CURRENT RSI=46.37 liquidity=1528679.38 spike=0.1
- WCDF.CA: score=8.54 buy_ready=False sector_rank=16 price=657.29 support=575.5 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:55 PM market time freshness=DELAYED_CURRENT RSI=37.38 liquidity=1716030.75 spike=0.32
- WKOL.CA: score=2.57 buy_ready=False sector_rank=16 price=297.05 support=266.18 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=25.4 liquidity=4737767.0 spike=0.36
- ZEOT.CA: score=7.97 buy_ready=False sector_rank=16 price=12.94 support=10.6 resistance=14.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:03 PM market time freshness=DELAYED_CURRENT RSI=39.84 liquidity=4137140.75 spike=0.74
- ZMID.CA: score=8.08 buy_ready=False sector_rank=19 price=7.7 support=7.07 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:01 PM market time freshness=DELAYED_CURRENT RSI=17.08 liquidity=40629008.0 spike=0.29

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
