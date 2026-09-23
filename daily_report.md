# Telegram-First EGX Scanner Report

Scan phase: Post-close tomorrow tickets
Generated UTC: 2026-09-23T17:22:29.452709+00:00
Generated Cairo: 2026-09-23 20:22
Run timing: target 15:30 Cairo | generated Cairo 2026-09-23 20:22 | cron 30 12 * * 0-4
Trigger: scheduled cron=30 12 * * 0-4 mapped to post_close; Cairo now 2026-09-23 20:18

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 3
- Tradeable price/liquidity tickers: 180/187
- Top sector: Investment Holding

## Market Context
- Market trend: Unavailable
- Source: Market context unavailable
- As of: None
- Freshness: MISSING
- EGX30 regime: BEARISH / above MA20 21.05% / above MA50 47.37%
- EGX70 regime: BEARISH / above MA20 27.5% / above MA50 40.0%
- Sector breadth: 33.33%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=707877184.0 spike=1.1 score=11.6
- CCAP.CA: liquidity=536362560.0 spike=0.64 score=21.4
- ORHD.CA: liquidity=391716992.0 spike=2.68 score=17.34
- ETEL.CA: liquidity=320776800.0 spike=1.18 score=21.76
- OIH.CA: liquidity=222129696.0 spike=1.86 score=21.12

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: 

## Top Liquidity Spikes
- NEDA.CA: spike=7.81 liquidity=7374408.25 outlook=NEUTRAL score=42.65 buy_ready=False
- NHPS.CA: spike=5.75 liquidity=90538464.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- MAAL.CA: spike=5.57 liquidity=70373696.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGTS.CA: spike=3.59 liquidity=96761704.0 outlook=CONSTRUCTIVE score=56 buy_ready=False
- MHOT.CA: spike=3.29 liquidity=32383944.0 outlook=BULLISH_WATCH score=74 buy_ready=False

## Sector Leaderboard
- #1 Investment Holding: score=13.1 5d=7.13% 20d=16.43% aboveMA50=100.0%
- #2 Tourism & Leisure: score=10.91 5d=-0.11% 20d=0.11% aboveMA50=100.0%
- #3 Telecommunications: score=10.45 5d=2.08% 20d=11.0% aboveMA50=100.0%
- #4 Transportation & Logistics: score=7.12 5d=6.82% 20d=3.25% aboveMA50=50.0%
- #5 Energy & Petrochemicals: score=7.06 5d=3.21% 20d=3.71% aboveMA50=66.67%
- #6 Banking & Financials: score=6.73 5d=2.08% 20d=4.62% aboveMA50=70.0%
- #7 Education: score=5.64 5d=-3.97% 20d=13.37% aboveMA50=66.67%
- #8 Agriculture & Food Production: score=5.62 5d=-0.72% 20d=10.07% aboveMA50=50.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- SAUD.CA: BULLISH_WATCH score=99.73 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=momentum is extended
- OFH.CA: BULLISH_WATCH score=88.65 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- BINV.CA: BULLISH_WATCH score=82 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- EXPA.CA: BULLISH_WATCH score=81.73 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- DTPP.CA: BULLISH_WATCH score=76.65 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- MHOT.CA: BULLISH_WATCH score=74 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI
- ALCN.CA: BULLISH_WATCH score=73.12 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; close to resistance
- AMOC.CA: BULLISH_WATCH score=73.06 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support
- OIH.CA: BULLISH_WATCH score=73 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=overheated RSI; close to resistance
- HDBK.CA: BULLISH_WATCH score=72.73 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; far above support

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- EKHO.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ANFI.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.
- ARVA.CA: No usable market data returned. Check Yahoo symbol or add a manual fallback row.

## Ranked Scanner Results
- AALR.CA: score=14.26 buy_ready=False sector_rank=17 price=290.54 support=288.0 resistance=359.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=42.13 liquidity=19132058.0 spike=0.78
- ABUK.CA: score=20.71 buy_ready=False sector_rank=10 price=92.53 support=75.01 resistance=96.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.41 liquidity=124391552.0 spike=0.67
- ACAMD.CA: score=14.26 buy_ready=False sector_rank=17 price=2.0 support=1.99 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.1 liquidity=34697236.0 spike=0.65
- ACGC.CA: score=13.43 buy_ready=False sector_rank=11 price=13.99 support=13.65 resistance=16.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.12 liquidity=4919341.0 spike=0.17
- ADCI.CA: score=4.97 buy_ready=False sector_rank=17 price=285.51 support=267.66 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.59 liquidity=2707269.75 spike=0.58
- ADIB.CA: score=16.4 buy_ready=False sector_rank=6 price=51.85 support=50.51 resistance=55.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.27 liquidity=76700640.0 spike=0.98
- ADPC.CA: score=18.26 buy_ready=False sector_rank=17 price=4.0 support=3.81 resistance=4.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=18257334.0 spike=0.99
- AFDI.CA: score=6.34 buy_ready=False sector_rank=17 price=52.07 support=51.6 resistance=61.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.4 liquidity=2081602.5 spike=0.09
- AFMC.CA: score=13.03 buy_ready=False sector_rank=17 price=158.28 support=153.0 resistance=232.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.7 liquidity=8770701.0 spike=0.15
- AJWA.CA: score=14.73 buy_ready=False sector_rank=17 price=178.63 support=175.15 resistance=199.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=8465023.0 spike=0.19
- ALCN.CA: score=25.4 buy_ready=False sector_rank=4 price=34.2 support=30.03 resistance=34.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=56.12 liquidity=26504812.0 spike=0.73
- ALUM.CA: score=4.06 buy_ready=False sector_rank=17 price=24.95 support=25.0 resistance=30.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.38 liquidity=4802247.0 spike=0.41
- AMER.CA: score=13.98 buy_ready=False sector_rank=20 price=5.04 support=4.8 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.02 liquidity=26511096.0 spike=0.48
- AMES.CA: score=8.26 buy_ready=False sector_rank=17 price=49.98 support=48.45 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=11.06 liquidity=55659980.0 spike=0.21
- AMIA.CA: score=12.99 buy_ready=False sector_rank=17 price=18.36 support=17.12 resistance=21.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=5733360.5 spike=0.15
- AMOC.CA: score=21.4 buy_ready=False sector_rank=5 price=13.31 support=10.65 resistance=14.63 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=58496372.0 spike=0.33
- APSW.CA: score=-1.31 buy_ready=False sector_rank=17 price=8.32 support=8.2 resistance=8.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:08 PM market time freshness=DELAYED_CURRENT RSI=33.59 liquidity=430168.34 spike=0.48
- ARAB.CA: score=8.98 buy_ready=False sector_rank=20 price=0.23 support=0.24 resistance=0.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=66601160.0 spike=0.68
- ARCC.CA: score=11.26 buy_ready=False sector_rank=21 price=68.54 support=69.0 resistance=81.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.48 liquidity=21150284.0 spike=0.63
- AREH.CA: score=13.07 buy_ready=False sector_rank=17 price=1.4 support=1.39 resistance=1.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.48 liquidity=8809010.0 spike=0.63
- ASCM.CA: score=6.02 buy_ready=False sector_rank=17 price=57.86 support=58.16 resistance=66.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=30.91 liquidity=6758109.0 spike=0.36
- ASPI.CA: score=14.26 buy_ready=False sector_rank=17 price=0.41 support=0.41 resistance=0.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.7 liquidity=34348468.0 spike=0.54
- ATLC.CA: score=13.78 buy_ready=False sector_rank=12 price=6.92 support=5.35 resistance=8.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=42.55 liquidity=3865230.75 spike=0.13
- ATQA.CA: score=20.71 buy_ready=False sector_rank=10 price=12.91 support=11.36 resistance=13.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.24 liquidity=46186104.0 spike=0.41
- AXPH.CA: score=11.38 buy_ready=False sector_rank=17 price=1669.41 support=1560.0 resistance=1768.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=4122612.5 spike=0.44
- BINV.CA: score=21.15 buy_ready=False sector_rank=1 price=56.37 support=48.04 resistance=72.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=66.21 liquidity=6747545.5 spike=0.27
- BIOC.CA: score=9.26 buy_ready=False sector_rank=17 price=263.61 support=247.03 resistance=470.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.58 liquidity=12505478.0 spike=0.13
- BTFH.CA: score=16.38 buy_ready=False sector_rank=12 price=2.88 support=2.87 resistance=3.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=38.64 liquidity=99441720.0 spike=1.23
- CAED.CA: score=2.59 buy_ready=False sector_rank=17 price=120.9 support=122.6 resistance=154.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.76 liquidity=3330328.5 spike=0.15
- CANA.CA: score=21.4 buy_ready=False sector_rank=6 price=45.93 support=41.35 resistance=52.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=71.01 liquidity=13765302.0 spike=0.61
- CCAP.CA: score=21.4 buy_ready=False sector_rank=1 price=7.03 support=5.74 resistance=7.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=81.95 liquidity=536362560.0 spike=0.64
- CCRS.CA: score=13.31 buy_ready=False sector_rank=17 price=2.55 support=2.4 resistance=3.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=50.88 liquidity=9053486.0 spike=0.21
- CEFM.CA: score=7.82 buy_ready=False sector_rank=17 price=143.52 support=135.0 resistance=167.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=45.06 liquidity=557281.5 spike=0.06
- CERA.CA: score=14.26 buy_ready=False sector_rank=17 price=1.35 support=1.22 resistance=2.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=49.54 liquidity=55285180.0 spike=0.43
- CFGH.CA: score=2.27 buy_ready=False sector_rank=17 price=0.12 support=0.11 resistance=0.12 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=26.67 liquidity=7695.92 spike=0.46
- CICH.CA: score=13.94 buy_ready=False sector_rank=12 price=12.34 support=11.47 resistance=13.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.42 liquidity=2024376.25 spike=0.32
- CIEB.CA: score=19.4 buy_ready=False sector_rank=6 price=24.78 support=24.01 resistance=26.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=12646059.0 spike=0.92
- CIRA.CA: score=21.26 buy_ready=False sector_rank=7 price=39.91 support=32.1 resistance=41.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.3 liquidity=16006672.0 spike=0.4
- CLHO.CA: score=9.12 buy_ready=False sector_rank=19 price=15.83 support=15.4 resistance=18.45 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=14.29 liquidity=24028974.25 spike=0.36
- CNFN.CA: score=3.52 buy_ready=False sector_rank=12 price=4.44 support=4.46 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.33 liquidity=4608679.5 spike=0.4
- COMI.CA: score=11.6 buy_ready=False sector_rank=6 price=128.98 support=131.11 resistance=142.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=30.0 liquidity=707877184.0 spike=1.1
- COPR.CA: score=17.26 buy_ready=False sector_rank=17 price=0.48 support=0.46 resistance=0.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=47.44 liquidity=11217722.0 spike=0.26
- COSG.CA: score=14.26 buy_ready=False sector_rank=17 price=1.71 support=1.77 resistance=2.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=40.91 liquidity=20075190.0 spike=0.62
- CPCI.CA: score=10.27 buy_ready=False sector_rank=17 price=563.28 support=530.0 resistance=584.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=67.29 liquidity=1007250.56 spike=0.31
- CSAG.CA: score=5.41 buy_ready=False sector_rank=4 price=37.75 support=36.5 resistance=44.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=32.56 liquidity=4013293.25 spike=0.26
- DAPH.CA: score=9.26 buy_ready=False sector_rank=17 price=109.01 support=108.25 resistance=157.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=21.58 liquidity=26492278.0 spike=0.45
- DEIN.CA: score=7.26 buy_ready=False sector_rank=17 price=10.35 support=10.35 resistance=12.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10 September 11:17 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49.68 spike=0.01
- DOMT.CA: score=11.58 buy_ready=False sector_rank=15 price=26.01 support=25.56 resistance=29.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=36.1 liquidity=6547065.0 spike=1.25
- DSCW.CA: score=6.69 buy_ready=False sector_rank=17 price=1.78 support=1.77 resistance=1.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=34.38 liquidity=8426365.0 spike=0.34
- DTPP.CA: score=19.26 buy_ready=False sector_rank=17 price=327.5 support=295.13 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=60.9 liquidity=70241296.0 spike=0.87
- EALR.CA: score=9.68 buy_ready=False sector_rank=17 price=367.01 support=340.0 resistance=411.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=37.72 liquidity=5418904.5 spike=0.39
- EASB.CA: score=17.26 buy_ready=False sector_rank=17 price=7.87 support=7.2 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=55.34 liquidity=11385500.0 spike=0.67
- EAST.CA: score=8.54 buy_ready=False sector_rank=15 price=31.86 support=31.31 resistance=36.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=11.58 liquidity=17730486.0 spike=0.23
- EBSC.CA: score=6.05 buy_ready=False sector_rank=17 price=1.97 support=1.95 resistance=2.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=1789855.38 spike=0.12
- ECAP.CA: score=1.44 buy_ready=False sector_rank=17 price=31.6 support=31.16 resistance=34.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.26 liquidity=2180213.75 spike=0.19
- EDFM.CA: score=4.77 buy_ready=False sector_rank=17 price=393.0 support=390.0 resistance=465.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.76 liquidity=510288.97 spike=0.28
- EEII.CA: score=15.52 buy_ready=False sector_rank=17 price=2.29 support=2.15 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=39.54 liquidity=16621901.0 spike=1.13
- EFIC.CA: score=14.71 buy_ready=False sector_rank=10 price=184.57 support=183.0 resistance=239.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=44.76 liquidity=16819050.0 spike=0.05
- EFID.CA: score=14.54 buy_ready=False sector_rank=15 price=30.31 support=29.71 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.82 liquidity=44449132.0 spike=0.67
- EFIH.CA: score=14.24 buy_ready=False sector_rank=18 price=23.32 support=22.16 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=49589244.0 spike=0.83
- EGAL.CA: score=18.71 buy_ready=False sector_rank=10 price=360.81 support=351.0 resistance=395.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=37.89 liquidity=34359940.0 spike=0.35
- EGAS.CA: score=14.58 buy_ready=False sector_rank=5 price=55.75 support=55.0 resistance=61.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=38.12 liquidity=8180018.5 spike=0.69
- EGBE.CA: score=9.64 buy_ready=False sector_rank=6 price=0.52 support=0.49 resistance=0.55 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=43.3 liquidity=79786.39 spike=1.08
- EGCH.CA: score=18.71 buy_ready=False sector_rank=10 price=13.95 support=13.33 resistance=14.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=39.52 liquidity=90012344.0 spike=0.74
- EGSA.CA: score=12.4 buy_ready=False sector_rank=3 price=9.0 support=8.69 resistance=9.1 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=57.14 liquidity=4590.0 spike=0.71
- EGTS.CA: score=25.98 buy_ready=False sector_rank=20 price=18.71 support=16.51 resistance=18.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=70.13 liquidity=96761704.0 spike=3.59
- EHDR.CA: score=8.11 buy_ready=False sector_rank=17 price=2.63 support=2.65 resistance=3.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.81 liquidity=8851673.0 spike=0.51
- ELEC.CA: score=8.62 buy_ready=False sector_rank=13 price=1.96 support=1.92 resistance=2.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.43 liquidity=31028150.0 spike=0.4
- ELKA.CA: score=6.56 buy_ready=False sector_rank=17 price=1.65 support=1.64 resistance=1.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=15.62 liquidity=7299505.0 spike=0.2
- ELNA.CA: score=-1.45 buy_ready=False sector_rank=17 price=35.22 support=33.96 resistance=38.99 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=26.38 liquidity=285246.79 spike=0.74
- ELSH.CA: score=13.13 buy_ready=False sector_rank=17 price=12.1 support=12.55 resistance=14.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.6 liquidity=8873283.0 spike=0.24
- ELWA.CA: score=0.08 buy_ready=False sector_rank=17 price=1.69 support=1.64 resistance=1.99 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=25.0 liquidity=822666.68 spike=0.47
- EMFD.CA: score=16.98 buy_ready=False sector_rank=20 price=13.39 support=12.1 resistance=15.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=45.92 liquidity=43595996.0 spike=0.27
- ENGC.CA: score=14.88 buy_ready=False sector_rank=17 price=41.65 support=41.0 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=36.05 liquidity=22215090.0 spike=1.31
- EOSB.CA: score=9.39 buy_ready=False sector_rank=17 price=1.57 support=1.53 resistance=1.64 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=67542.97 spike=1.03
- EPCO.CA: score=8.86 buy_ready=False sector_rank=17 price=10.63 support=10.6 resistance=12.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=45.05 liquidity=4604777.0 spike=0.29
- EPPK.CA: score=-5.32 buy_ready=False sector_rank=17 price=10.29 support=10.29 resistance=10.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=8 September 01:25 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=419183.72 spike=0.28
- ETEL.CA: score=21.76 buy_ready=False sector_rank=3 price=138.39 support=112.5 resistance=140.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=87.08 liquidity=320776800.0 spike=1.18
- ETRS.CA: score=6.45 buy_ready=False sector_rank=17 price=10.61 support=10.66 resistance=11.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=33.01 liquidity=7187387.5 spike=0.56
- EXPA.CA: score=23.4 buy_ready=False sector_rank=6 price=21.86 support=19.96 resistance=22.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=60.43 liquidity=32300228.0 spike=0.91
- FAIT.CA: score=11.13 buy_ready=False sector_rank=6 price=46.57 support=38.48 resistance=48.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=66.28 liquidity=1728125.75 spike=0.21
- FAITA.CA: score=5.41 buy_ready=False sector_rank=6 price=0.98 support=0.98 resistance=1.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=14747.09 spike=0.3
- FERC.CA: score=11.2 buy_ready=False sector_rank=10 price=77.56 support=77.3 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=41.09 liquidity=6490097.0 spike=0.45
- FWRY.CA: score=14.24 buy_ready=False sector_rank=18 price=18.88 support=18.66 resistance=19.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.43 liquidity=125188832.0 spike=0.91
- GBCO.CA: score=22.93 buy_ready=False sector_rank=9 price=31.12 support=27.51 resistance=32.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=64.3 liquidity=60822088.0 spike=0.8
- GDWA.CA: score=8.26 buy_ready=False sector_rank=17 price=0.74 support=0.75 resistance=0.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=14.04 liquidity=32975828.0 spike=0.76
- GGCC.CA: score=14.26 buy_ready=False sector_rank=17 price=0.78 support=0.81 resistance=1.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=41.96 liquidity=16445685.0 spike=0.49
- GIHD.CA: score=19.26 buy_ready=False sector_rank=17 price=73.75 support=61.61 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=51.87 liquidity=13545958.0 spike=0.51
- GMCI.CA: score=0.42 buy_ready=False sector_rank=17 price=1.71 support=1.69 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=22.22 liquidity=819411.19 spike=1.67
- GRCA.CA: score=8.26 buy_ready=False sector_rank=17 price=40.13 support=38.7 resistance=85.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=22.06 liquidity=23848022.0 spike=0.48
- GSSC.CA: score=13.25 buy_ready=False sector_rank=17 price=299.44 support=278.0 resistance=333.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=61.08 liquidity=1994132.13 spike=0.23
- GTWL.CA: score=17.26 buy_ready=False sector_rank=17 price=230.56 support=210.0 resistance=248.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=59.32 liquidity=70281600.0 spike=0.38
- HDBK.CA: score=23.4 buy_ready=False sector_rank=6 price=113.67 support=91.7 resistance=124.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=51.84 liquidity=22671334.0 spike=0.37
- HELI.CA: score=16.46 buy_ready=False sector_rank=20 price=7.95 support=7.36 resistance=8.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=52.81 liquidity=208567280.0 spike=1.24
- HRHO.CA: score=8.92 buy_ready=False sector_rank=12 price=24.43 support=24.4 resistance=26.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=32.03 liquidity=45126504.0 spike=0.43
- ICID.CA: score=18.64 buy_ready=False sector_rank=17 price=17.0 support=16.2 resistance=19.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.53 liquidity=18000252.0 spike=1.69
- IDRE.CA: score=15.68 buy_ready=False sector_rank=17 price=53.03 support=51.0 resistance=59.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=8416829.0 spike=0.51
- IFAP.CA: score=14.33 buy_ready=False sector_rank=8 price=20.08 support=19.05 resistance=23.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=45.01 liquidity=8081426.0 spike=0.37
- INFI.CA: score=8.13 buy_ready=False sector_rank=17 price=123.16 support=123.0 resistance=161.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=21.62 liquidity=8872218.0 spike=0.46
- IRON.CA: score=9.71 buy_ready=False sector_rank=10 price=27.95 support=26.3 resistance=31.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=22.67 liquidity=10764558.0 spike=0.78
- ISMA.CA: score=8.92 buy_ready=False sector_rank=17 price=29.86 support=28.05 resistance=40.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=35.11 liquidity=4658719.5 spike=0.2
- ISMQ.CA: score=10.71 buy_ready=False sector_rank=10 price=8.59 support=8.68 resistance=9.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=24.48 liquidity=14475020.0 spike=0.57
- ISPH.CA: score=9.12 buy_ready=False sector_rank=19 price=12.02 support=11.9 resistance=13.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.94 liquidity=15135674.0 spike=0.22
- JUFO.CA: score=14.53 buy_ready=False sector_rank=15 price=26.83 support=26.45 resistance=27.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.16 liquidity=8994670.0 spike=0.43
- KABO.CA: score=16.45 buy_ready=False sector_rank=11 price=9.05 support=8.92 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=7934188.5 spike=0.19
- KWIN.CA: score=9.26 buy_ready=False sector_rank=17 price=90.0 support=82.5 resistance=137.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=12.61 liquidity=37679220.0 spike=0.81
- KZPC.CA: score=13.35 buy_ready=False sector_rank=17 price=13.68 support=12.6 resistance=14.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.56 liquidity=4087845.25 spike=0.12
- LCSW.CA: score=7.17 buy_ready=False sector_rank=21 price=31.86 support=31.61 resistance=37.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=32.56 liquidity=8909543.0 spike=0.36
- LUTS.CA: score=14.26 buy_ready=False sector_rank=17 price=0.87 support=0.83 resistance=1.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.4 liquidity=23703960.0 spike=0.14
- MAAL.CA: score=9.26 buy_ready=False sector_rank=17 price=10.3 support=9.03 resistance=10.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=70373696.0 spike=5.57
- MASR.CA: score=14.26 buy_ready=False sector_rank=17 price=7.6 support=7.49 resistance=8.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.43 liquidity=31152248.0 spike=0.32
- MBSC.CA: score=11.26 buy_ready=False sector_rank=21 price=341.0 support=333.33 resistance=470.0 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=22.57 liquidity=20918986.0 spike=0.48
- MCQE.CA: score=8.26 buy_ready=False sector_rank=21 price=200.1 support=203.5 resistance=254.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=23.88 liquidity=25863108.0 spike=0.98
- MCRO.CA: score=17.26 buy_ready=False sector_rank=17 price=1.63 support=1.48 resistance=1.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.92 liquidity=38439208.0 spike=0.31
- MENA.CA: score=4.72 buy_ready=False sector_rank=20 price=6.63 support=6.58 resistance=7.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.49 liquidity=739711.81 spike=0.46
- MEPA.CA: score=10.61 buy_ready=False sector_rank=17 price=1.86 support=1.8 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=51.32 liquidity=6345384.5 spike=0.16
- MFPC.CA: score=22.71 buy_ready=False sector_rank=10 price=47.6 support=39.02 resistance=51.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=62.46 liquidity=55871352.0 spike=0.32
- MFSC.CA: score=11.46 buy_ready=False sector_rank=17 price=51.08 support=48.5 resistance=58.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=46.59 liquidity=2201043.0 spike=0.46
- MHOT.CA: score=26.98 buy_ready=False sector_rank=2 price=18.72 support=16.61 resistance=19.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.91 liquidity=32383944.0 spike=3.29
- MICH.CA: score=11.16 buy_ready=False sector_rank=17 price=47.16 support=47.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=24.75 liquidity=8898793.0 spike=0.57
- MILS.CA: score=8.99 buy_ready=False sector_rank=17 price=190.57 support=180.01 resistance=232.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=35.06 liquidity=4730520.5 spike=0.2
- MIPH.CA: score=16.32 buy_ready=False sector_rank=19 price=839.08 support=700.2 resistance=1000.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.79 liquidity=7195749.0 spike=0.8
- MOED.CA: score=8.26 buy_ready=False sector_rank=17 price=0.71 support=0.7 resistance=0.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=25.23 liquidity=15278288.0 spike=0.22
- MOIL.CA: score=13.16 buy_ready=False sector_rank=5 price=0.7 support=0.66 resistance=0.71 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=68.33 liquidity=381152.81 spike=1.69
- MOIN.CA: score=10.77 buy_ready=False sector_rank=17 price=35.61 support=32.5 resistance=45.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=56.5 liquidity=3511394.25 spike=0.11
- MOSC.CA: score=-0.16 buy_ready=False sector_rank=17 price=299.78 support=290.0 resistance=346.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=21.23 liquidity=579734.19 spike=0.09
- MPCI.CA: score=12.26 buy_ready=False sector_rank=17 price=385.0 support=371.11 resistance=490.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=25.84 liquidity=78630456.0 spike=0.55
- MPCO.CA: score=21.25 buy_ready=False sector_rank=8 price=2.66 support=2.07 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=67.93 liquidity=139775952.0 spike=0.82
- MPRC.CA: score=9.26 buy_ready=False sector_rank=17 price=39.05 support=37.65 resistance=46.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=19.54 liquidity=20932110.0 spike=0.55
- MTIE.CA: score=9.93 buy_ready=False sector_rank=9 price=8.2 support=8.02 resistance=8.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.15 liquidity=18571320.0 spike=0.7
- NAHO.CA: score=-4.16 buy_ready=False sector_rank=17 price=0.12 support=0.12 resistance=0.13 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=100493.34 spike=1.74
- NCCW.CA: score=5.28 buy_ready=False sector_rank=17 price=7.64 support=7.15 resistance=7.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=103215448.0 spike=1.51
- NEDA.CA: score=16.63 buy_ready=False sector_rank=17 price=2.75 support=2.7 resistance=2.89 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=51.52 liquidity=7374408.25 spike=7.81
- NHPS.CA: score=9.26 buy_ready=False sector_rank=17 price=82.7 support=73.63 resistance=86.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=90538464.0 spike=5.75
- NINH.CA: score=2.74 buy_ready=False sector_rank=17 price=20.24 support=20.3 resistance=25.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=23.17 liquidity=3476091.5 spike=0.11
- NIPH.CA: score=17.12 buy_ready=False sector_rank=19 price=333.01 support=290.0 resistance=401.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.36 liquidity=101645216.0 spike=0.66
- OBRI.CA: score=4.37 buy_ready=False sector_rank=17 price=29.58 support=29.51 resistance=34.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=18.18 liquidity=6107466.0 spike=0.4
- OCDI.CA: score=8.98 buy_ready=False sector_rank=20 price=29.19 support=28.52 resistance=34.5 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=26.51 liquidity=39294440.31 spike=0.54
- OCPH.CA: score=8.41 buy_ready=False sector_rank=17 price=235.07 support=210.0 resistance=277.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=42.94 liquidity=3153351.0 spike=0.49
- ODIN.CA: score=13.75 buy_ready=False sector_rank=17 price=2.75 support=2.55 resistance=3.42 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.0 liquidity=9494974.0 spike=0.43
- OFH.CA: score=20.36 buy_ready=False sector_rank=17 price=1.09 support=0.98 resistance=1.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=61.29 liquidity=208867552.0 spike=1.55
- OIH.CA: score=21.12 buy_ready=False sector_rank=1 price=2.18 support=1.94 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=76.92 liquidity=222129696.0 spike=1.86
- OLFI.CA: score=15.53 buy_ready=False sector_rank=15 price=22.92 support=22.07 resistance=23.99 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=57.38 liquidity=6989866.58 spike=0.41
- ORAS.CA: score=4.6 buy_ready=False sector_rank=14 price=840.9 support=835.72 resistance=847.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=58181140.0 spike=1.0
- ORHD.CA: score=17.34 buy_ready=False sector_rank=20 price=40.6 support=40.85 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.49 liquidity=391716992.0 spike=2.68
- ORWE.CA: score=20.51 buy_ready=False sector_rank=11 price=27.51 support=24.5 resistance=29.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.23 liquidity=33426368.0 spike=0.61
- PHAR.CA: score=9.12 buy_ready=False sector_rank=19 price=113.54 support=111.55 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.66 liquidity=26983032.0 spike=0.27
- PHDC.CA: score=8.98 buy_ready=False sector_rank=20 price=13.38 support=12.91 resistance=15.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=31.82 liquidity=43499936.0 spike=0.27
- PHTV.CA: score=4.99 buy_ready=False sector_rank=17 price=336.95 support=311.27 resistance=378.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=40.4 liquidity=726900.31 spike=0.43
- POUL.CA: score=17.1 buy_ready=False sector_rank=15 price=38.55 support=37.15 resistance=41.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=21 September 01:28 PM market time freshness=DELAYED_CURRENT RSI=43.81 liquidity=58845364.0 spike=2.28
- PRCL.CA: score=13.04 buy_ready=False sector_rank=21 price=31.44 support=30.61 resistance=34.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=43.97 liquidity=9774456.0 spike=0.58
- PRDC.CA: score=8.98 buy_ready=False sector_rank=20 price=7.41 support=7.51 resistance=10.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=11.9 liquidity=26268536.0 spike=0.46
- PRMH.CA: score=5.73 buy_ready=False sector_rank=17 price=2.59 support=2.43 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:04 PM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=1465910.63 spike=0.14
- RACC.CA: score=6.92 buy_ready=False sector_rank=17 price=9.58 support=9.4 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=2661771.0 spike=0.16
- RAKT.CA: score=4.02 buy_ready=False sector_rank=17 price=22.08 support=21.4 resistance=23.02 source=Yahoo Finance as_of=2026-09-21T21:00:00+00:00 freshness=FRESH RSI=47.17 liquidity=278804.16 spike=1.24
- RAYA.CA: score=15.6 buy_ready=False sector_rank=16 price=7.16 support=6.8 resistance=7.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.19 liquidity=83957200.0 spike=1.56
- RMDA.CA: score=14.12 buy_ready=False sector_rank=19 price=5.87 support=5.77 resistance=6.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=31628466.0 spike=0.55
- ROTO.CA: score=6.42 buy_ready=False sector_rank=17 price=40.57 support=35.02 resistance=45.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=31.16 liquidity=7162821.0 spike=0.92
- RREI.CA: score=14.26 buy_ready=False sector_rank=17 price=4.1 support=4.2 resistance=4.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=38.14 liquidity=10618084.0 spike=0.62
- RTVC.CA: score=-0.11 buy_ready=False sector_rank=17 price=3.81 support=3.79 resistance=4.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=26.56 liquidity=1630279.0 spike=0.38
- RUBX.CA: score=7.56 buy_ready=False sector_rank=17 price=16.94 support=15.44 resistance=16.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=109061768.0 spike=2.65
- SAUD.CA: score=24.46 buy_ready=False sector_rank=6 price=24.58 support=22.7 resistance=26.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=69.68 liquidity=28174500.0 spike=1.53
- SCEM.CA: score=8.26 buy_ready=False sector_rank=21 price=84.53 support=84.5 resistance=105.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=21.9 liquidity=25422364.0 spike=0.26
- SCFM.CA: score=5.43 buy_ready=False sector_rank=17 price=266.54 support=250.2 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=39.64 liquidity=1167416.25 spike=0.16
- SCTS.CA: score=1.94 buy_ready=False sector_rank=7 price=583.49 support=566.66 resistance=639.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=27.3 liquidity=681727.13 spike=0.25
- SDTI.CA: score=14.98 buy_ready=False sector_rank=17 price=77.53 support=67.3 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=75.38 liquidity=6715306.5 spike=0.25
- SEIG.CA: score=5.63 buy_ready=False sector_rank=17 price=230.49 support=228.13 resistance=274.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=37.72 liquidity=1367694.88 spike=0.73
- SIPC.CA: score=17.26 buy_ready=False sector_rank=17 price=5.37 support=4.75 resistance=7.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=55.56 liquidity=19381078.0 spike=0.28
- SKPC.CA: score=13.71 buy_ready=False sector_rank=10 price=17.63 support=17.0 resistance=19.36 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=33.89 liquidity=41644808.0 spike=0.32
- SMFR.CA: score=1.65 buy_ready=False sector_rank=17 price=229.74 support=226.1 resistance=274.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:14 PM market time freshness=DELAYED_CURRENT RSI=30.21 liquidity=2388149.0 spike=0.3
- SNFC.CA: score=18.26 buy_ready=False sector_rank=17 price=11.54 support=10.26 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=82.12 liquidity=13835332.0 spike=0.92
- SPIN.CA: score=8.22 buy_ready=False sector_rank=11 price=17.02 support=16.1 resistance=20.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=30.92 liquidity=7708930.5 spike=0.57
- SPMD.CA: score=14.26 buy_ready=False sector_rank=17 price=0.42 support=0.4 resistance=0.62 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=36135068.0 spike=0.49
- SUGR.CA: score=12.78 buy_ready=False sector_rank=15 price=58.25 support=55.06 resistance=64.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=52.87 liquidity=5244171.5 spike=0.13
- SVCE.CA: score=12.26 buy_ready=False sector_rank=17 price=11.11 support=9.6 resistance=13.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=28.3 liquidity=40322120.0 spike=0.2
- SWDY.CA: score=17.62 buy_ready=False sector_rank=13 price=124.23 support=122.0 resistance=139.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=44.78 liquidity=29071718.0 spike=0.46
- TALM.CA: score=21.26 buy_ready=False sector_rank=7 price=20.78 support=17.11 resistance=25.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:28 PM market time freshness=DELAYED_CURRENT RSI=65.69 liquidity=24913834.0 spike=0.37
- TMGH.CA: score=13.98 buy_ready=False sector_rank=20 price=92.78 support=93.08 resistance=100.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=41.39 liquidity=155042928.0 spike=0.55
- TRTO.CA: score=7.28 buy_ready=False sector_rank=17 price=0.06 support=0.05 resistance=0.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:00 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=16175.52 spike=0.58
- UEFM.CA: score=-0.5 buy_ready=False sector_rank=17 price=476.98 support=440.66 resistance=574.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=30.28 liquidity=1238285.13 spike=0.4
- UEGC.CA: score=16.26 buy_ready=False sector_rank=17 price=1.62 support=1.66 resistance=2.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=43466352.0 spike=0.82
- UNIP.CA: score=11.28 buy_ready=False sector_rank=17 price=0.37 support=0.37 resistance=0.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=7020853.0 spike=0.31
- UNIT.CA: score=6.12 buy_ready=False sector_rank=20 price=18.02 support=17.12 resistance=23.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:26 PM market time freshness=DELAYED_CURRENT RSI=46.5 liquidity=2142392.5 spike=0.15
- WCDF.CA: score=10.22 buy_ready=False sector_rank=17 price=700.33 support=636.31 resistance=796.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:13 PM market time freshness=DELAYED_CURRENT RSI=60.47 liquidity=958570.63 spike=0.19
- WKOL.CA: score=9.97 buy_ready=False sector_rank=17 price=331.12 support=325.0 resistance=379.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:25 PM market time freshness=DELAYED_CURRENT RSI=46.88 liquidity=5705501.5 spike=0.42
- ZEOT.CA: score=5.8 buy_ready=False sector_rank=17 price=12.7 support=13.03 resistance=14.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:27 PM market time freshness=DELAYED_CURRENT RSI=34.88 liquidity=6439775.0 spike=1.05
- ZMID.CA: score=11.98 buy_ready=False sector_rank=20 price=8.34 support=7.91 resistance=9.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=01:29 PM market time freshness=DELAYED_CURRENT RSI=29.97 liquidity=162173744.0 spike=0.76

## Backtesting Lite
- MHOT.CA: 180d return=-29.25%, max drawdown=-54.07%, MA20>MA50 days last20=14, as_of=2026-09-21T21:00:00+00:00
- EGTS.CA: 180d return=133.0%, max drawdown=-25.75%, MA20>MA50 days last20=0, as_of=2026-09-21T21:00:00+00:00
- ALCN.CA: 180d return=51.26%, max drawdown=-15.82%, MA20>MA50 days last20=20, as_of=2026-09-21T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- EGTS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Resorts Company summary=Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- ALCN.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Alexandria Containers and Cargo Handling summary=Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- SAUD.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=630 sources=3 expected=Al Baraka Bank Egypt summary=Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26; Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE; Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025
  - Al Baraka Bank Egypt records EGP 2.2bn operating income in Q1-26: https://english.mubasher.info/news/4611927/Al-Baraka-Bank-Egypt-records-EGP-2-2bn-operating-income-in-Q1-26/
  - Al Baraka Bank Egypt files MTO to acquire majority stake in A.T. LEASE: https://english.mubasher.info/news/4583822/Al-Baraka-Bank-Egypt-files-MTO-to-acquire-majority-stake-in-A-T-LEASE/
  - Al Baraka Bank Egypt to pay EGP 1.1/share dividends for 2025: https://english.mubasher.info/news/4583458/Al-Baraka-Bank-Egypt-to-pay-EGP-1-1-share-dividends-for-2025/
- HDBK.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Housing and Development Bank Egypt summary=Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- EXPA.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Export Development Bank of Egypt summary=Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- MFPC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Misr Fertilizers Production summary=Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.

## Warnings
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for EGTS.CA: source text did not clearly match EGTS.CA / Egyptian Resorts Company.
- Evidence rejected for ALCN.CA: source text did not clearly match ALCN.CA / Alexandria Containers and Cargo Handling.
- Evidence for SAUD.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for HDBK.CA: source text did not clearly match HDBK.CA / Housing and Development Bank Egypt.
- Evidence rejected for EXPA.CA: source text did not clearly match EXPA.CA / Export Development Bank of Egypt.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for MFPC.CA: source text did not clearly match MFPC.CA / Misr Fertilizers Production.
