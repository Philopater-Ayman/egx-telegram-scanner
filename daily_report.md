# Telegram-First EGX Scanner Report

Scan phase: Open liquidity confirmation
Generated UTC: 2026-06-11T11:02:43.457988+00:00
Generated Cairo: 2026-06-11 14:02
Run timing: target 09:15 Cairo | generated Cairo 2026-06-11 14:02 | cron 15 6 * * 0-4
Trigger: scheduled cron=15 6 * * 0-4 mapped to open_confirm; Cairo now 2026-06-11 13:57

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 188/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Thursday, June 11
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 10.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 27.5% / above MA50 67.5%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- CCAP.CA: liquidity=488916288.0 spike=0.58 score=18.34
- COMI.CA: liquidity=378372608.0 spike=0.58 score=14.33
- FWRY.CA: liquidity=248917344.0 spike=0.88 score=12.43
- ORAS.CA: liquidity=225385104.0 spike=1.0 score=4.6
- TMGH.CA: liquidity=204475936.0 spike=0.44 score=14.44

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD as the EGX30 and EGX70 are both in a bearish regime with weak breadth (≈9.5%). Market risk mode is DEFENSIVE_NO_NEW_BUY, meaning new long entries are discouraged until broader conditions improve. Liquidity spikes and bullish outlooks appear on a few stocks, but sector support is limited and many show overbought RSI or cooling liquidity, adding uncertainty for the next 1‑3 days.
- EGX30/EGX70 trends bearish, median 5‑day returns –3.4% / –2.4%, breadth below MA20/MA50.
- Risk mode DEFENSIVE_NO_NEW_BUY – market does not support fresh buys despite isolated bullish watches.
- Top sectors (Automotive, Energy, Real Estate) show mixed signals; only Automotive has modest upside, Energy still near‑flat.
- Key stocks (EGAS, MPCI, ZMID) show bullish outlooks but face resistance levels and, in some cases, high RSI or cooling liquidity.
- Uncertainty remains high; monitor sector breadth and liquidity spikes before considering any entry.

## Top Liquidity Spikes
- ANFI.CA: spike=4.63 liquidity=168343687.25 outlook=BULLISH_WATCH score=72.09 buy_ready=False
- ISMQ.CA: spike=2.76 liquidity=156554000.0 outlook=CONSTRUCTIVE score=68.34 buy_ready=False
- OLFI.CA: spike=2.6 liquidity=49841256.0 outlook=CONSTRUCTIVE score=61.88 buy_ready=False
- CFGH.CA: spike=2.56 liquidity=16699.85 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EGSA.CA: spike=2.43 liquidity=35930.8 outlook=NEUTRAL score=36.85 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=5.16 5d=2.25% 20d=-5.56% aboveMA50=100.0%
- #2 Energy & Petrochemicals: score=3.76 5d=-0.59% 20d=-0.21% aboveMA50=75.0%
- #3 Real Estate: score=3.6 5d=-3.4% 20d=3.87% aboveMA50=84.62%
- #4 Investment Holding: score=3.34 5d=-5.16% 20d=9.48% aboveMA50=66.67%
- #5 General / Verified EGX Expansion: score=3.09 5d=-0.89% 20d=-1.43% aboveMA50=67.31%
- #6 Agriculture & Food Production: score=3.06 5d=0.3% 20d=-3.26% aboveMA50=50.0%
- #7 Tourism & Leisure: score=2.96 5d=-6.69% 20d=11.23% aboveMA50=100.0%
- #8 Healthcare: score=2.74 5d=-0.57% 20d=-2.39% aboveMA50=100.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- EGAS.CA: BULLISH_WATCH score=100 liquidity=ACCUMULATION_SPIKE sector=LEADING risk=No major short-term scanner risk flags.
- MPCI.CA: BULLISH_WATCH score=96.09 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- ACAMD.CA: BULLISH_WATCH score=84.09 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- MENA.CA: BULLISH_WATCH score=83.6 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=81.6 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended
- AMIA.CA: BULLISH_WATCH score=79.09 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MILS.CA: BULLISH_WATCH score=79.09 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EASB.CA: BULLISH_WATCH score=78.09 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- COPR.CA: BULLISH_WATCH score=76.09 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- UNIT.CA: BULLISH_WATCH score=75.6 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; momentum is extended

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=14.95 buy_ready=False sector_rank=5 price=205.46 support=195.1 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=50.99 liquidity=6713058.0 spike=0.82
- ABUK.CA: score=9.14 buy_ready=False sector_rank=18 price=76.11 support=79.0 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=20.62 liquidity=102666384.0 spike=0.88
- ACAMD.CA: score=20.24 buy_ready=False sector_rank=5 price=2.28 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=118433600.0 spike=0.94
- ACGC.CA: score=13.01 buy_ready=False sector_rank=10 price=9.17 support=8.6 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=31.86 liquidity=20128400.0 spike=0.34
- ADCI.CA: score=20.38 buy_ready=False sector_rank=5 price=222.43 support=202.22 resistance=228.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=70.52 liquidity=9465494.0 spike=1.34
- ADIB.CA: score=14.33 buy_ready=False sector_rank=15 price=44.2 support=44.6 resistance=50.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=48568148.0 spike=0.31
- ADPC.CA: score=10.24 buy_ready=False sector_rank=5 price=3.5 support=3.54 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=25.53 liquidity=11867590.0 spike=0.47
- AFDI.CA: score=16.31 buy_ready=False sector_rank=5 price=40.48 support=40.0 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=60.02 liquidity=8076588.0 spike=0.44
- AFMC.CA: score=9.68 buy_ready=False sector_rank=5 price=69.43 support=69.33 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=42.35 liquidity=1439910.75 spike=0.19
- AJWA.CA: score=17.24 buy_ready=False sector_rank=5 price=149.97 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=79.93 liquidity=14073998.0 spike=0.77
- ALCN.CA: score=14.12 buy_ready=False sector_rank=19 price=28.38 support=28.17 resistance=30.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=41.72 liquidity=19180438.0 spike=0.97
- ALUM.CA: score=15.29 buy_ready=False sector_rank=5 price=23.54 support=22.93 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=51.48 liquidity=5052442.0 spike=0.24
- AMER.CA: score=19.44 buy_ready=False sector_rank=3 price=2.59 support=2.43 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=55.67 liquidity=37554864.0 spike=0.33
- AMES.CA: score=3.03 buy_ready=False sector_rank=5 price=48.79 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=17.32 liquidity=795231.38 spike=0.14
- AMIA.CA: score=20.24 buy_ready=False sector_rank=5 price=9.0 support=8.54 resistance=10.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=10327847.0 spike=0.37
- AMOC.CA: score=17.5 buy_ready=False sector_rank=2 price=7.94 support=8.09 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=36.17 liquidity=58932056.0 spike=0.77
- ANFI.CA: score=24.24 buy_ready=False sector_rank=5 price=19.75 support=13.5 resistance=21.99 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=87.25 liquidity=168343687.25 spike=4.63
- APSW.CA: score=1.72 buy_ready=False sector_rank=5 price=8.63 support=8.6 resistance=9.38 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=29.21 liquidity=1328726.6 spike=1.58
- ARAB.CA: score=15.44 buy_ready=False sector_rank=3 price=0.2 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=42944640.0 spike=0.51
- ARCC.CA: score=17.14 buy_ready=False sector_rank=17 price=54.56 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=58.09 liquidity=23930948.0 spike=0.55
- AREH.CA: score=17.24 buy_ready=False sector_rank=5 price=1.45 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=80.65 liquidity=15237215.0 spike=0.58
- ARVA.CA: score=17.13 buy_ready=False sector_rank=5 price=10.98 support=7.71 resistance=11.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=76.32 liquidity=9894755.0 spike=0.41
- ASCM.CA: score=20.24 buy_ready=False sector_rank=5 price=54.47 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=71.93 liquidity=19151506.0 spike=0.27
- ASPI.CA: score=22.24 buy_ready=False sector_rank=5 price=0.32 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=56.87 liquidity=26225320.0 spike=0.4
- ATLC.CA: score=4.81 buy_ready=False sector_rank=20 price=4.8 support=4.71 resistance=5.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=59.32 liquidity=1783191.88 spike=0.29
- ATQA.CA: score=13.32 buy_ready=False sector_rank=18 price=9.08 support=9.41 resistance=10.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=54.04 liquidity=42475944.0 spike=1.09
- AXPH.CA: score=9.15 buy_ready=False sector_rank=5 price=1122.84 support=1111.0 resistance=1230.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=43.08 liquidity=909172.06 spike=0.16
- BINV.CA: score=14.28 buy_ready=False sector_rank=4 price=44.89 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=68.75 liquidity=3944358.5 spike=0.34
- BIOC.CA: score=10.38 buy_ready=False sector_rank=5 price=69.71 support=70.0 resistance=79.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=48.95 liquidity=2140103.75 spike=0.33
- BTFH.CA: score=12.02 buy_ready=False sector_rank=20 price=2.99 support=3.03 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=87179584.0 spike=0.37
- CAED.CA: score=11.53 buy_ready=False sector_rank=5 price=67.61 support=70.41 resistance=84.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=36.79 liquidity=3294928.5 spike=0.23
- CANA.CA: score=11.62 buy_ready=False sector_rank=15 price=35.71 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=63.4 liquidity=5288666.0 spike=0.36
- CCAP.CA: score=18.34 buy_ready=False sector_rank=4 price=5.15 support=4.7 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=48.45 liquidity=488916288.0 spike=0.58
- CCRS.CA: score=15.67 buy_ready=False sector_rank=5 price=2.39 support=2.16 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=7430603.0 spike=0.27
- CEFM.CA: score=4.23 buy_ready=False sector_rank=5 price=103.45 support=103.07 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=29.98 liquidity=998443.38 spike=0.24
- CERA.CA: score=13.81 buy_ready=False sector_rank=5 price=1.16 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=4574984.5 spike=0.31
- CFGH.CA: score=2.37 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:32 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=16699.85 spike=2.56
- CICH.CA: score=-1.0 buy_ready=False sector_rank=20 price=11.27 support=11.5 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=23.6 liquidity=975984.38 spike=0.21
- CIEB.CA: score=9.46 buy_ready=False sector_rank=15 price=23.39 support=23.31 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=61.73 liquidity=5123608.5 spike=0.55
- CIRA.CA: score=6.17 buy_ready=False sector_rank=9 price=25.85 support=25.62 resistance=28.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=31.87 liquidity=3107790.25 spike=0.11
- CLHO.CA: score=14.76 buy_ready=False sector_rank=8 price=14.6 support=14.8 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=40.07 liquidity=6665507.0 spike=0.2
- CNFN.CA: score=6.13 buy_ready=False sector_rank=20 price=4.39 support=4.41 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=36.51 liquidity=4106730.5 spike=0.25
- COMI.CA: score=14.33 buy_ready=False sector_rank=15 price=131.82 support=129.8 resistance=139.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=48.17 liquidity=378372608.0 spike=0.58
- COPR.CA: score=21.24 buy_ready=False sector_rank=5 price=0.36 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=15248718.0 spike=0.37
- COSG.CA: score=5.24 buy_ready=False sector_rank=5 price=1.55 support=1.54 resistance=1.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=54463436.0 spike=0.84
- CPCI.CA: score=6.77 buy_ready=False sector_rank=5 price=355.31 support=340.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=79.86 liquidity=1535133.75 spike=0.36
- CSAG.CA: score=13.18 buy_ready=False sector_rank=19 price=30.69 support=30.4 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=56.74 liquidity=6057820.5 spike=0.37
- DAPH.CA: score=3.91 buy_ready=False sector_rank=5 price=77.68 support=78.6 resistance=96.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=27.7 liquidity=4676282.5 spike=0.15
- DEIN.CA: score=6.24 buy_ready=False sector_rank=5 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.22 buy_ready=False sector_rank=11 price=23.93 support=24.03 resistance=26.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=25.68 liquidity=1465067.13 spike=0.57
- DSCW.CA: score=16.24 buy_ready=False sector_rank=5 price=1.75 support=1.71 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=15867702.0 spike=0.28
- DTPP.CA: score=0.93 buy_ready=False sector_rank=5 price=117.98 support=118.03 resistance=137.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=21.74 liquidity=697104.44 spike=0.2
- EALR.CA: score=10.52 buy_ready=False sector_rank=5 price=351.76 support=346.01 resistance=392.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=52.5 liquidity=2282219.0 spike=0.4
- EASB.CA: score=11.48 buy_ready=False sector_rank=5 price=5.01 support=4.61 resistance=5.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=57.14 liquidity=1168776.38 spike=1.04
- EAST.CA: score=21.75 buy_ready=False sector_rank=11 price=38.5 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=57.19 liquidity=18831946.0 spike=0.28
- EBSC.CA: score=10.8 buy_ready=False sector_rank=5 price=1.78 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=69.23 liquidity=561785.0 spike=0.21
- ECAP.CA: score=16.07 buy_ready=False sector_rank=5 price=31.74 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=89.66 liquidity=7929021.5 spike=1.45
- EDFM.CA: score=8.73 buy_ready=False sector_rank=5 price=334.11 support=320.2 resistance=355.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.28 liquidity=490807.57 spike=0.85
- EEII.CA: score=20.24 buy_ready=False sector_rank=5 price=2.33 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=63.89 liquidity=14524912.0 spike=0.75
- EFIC.CA: score=3.81 buy_ready=False sector_rank=18 price=203.57 support=203.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=9.24 liquidity=4869427.5 spike=1.4
- EFID.CA: score=14.75 buy_ready=False sector_rank=11 price=27.51 support=27.49 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=51.39 liquidity=24372348.0 spike=0.32
- EFIH.CA: score=12.43 buy_ready=False sector_rank=21 price=20.33 support=20.54 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=40.71 liquidity=23839868.0 spike=0.41
- EGAL.CA: score=9.14 buy_ready=False sector_rank=18 price=307.51 support=308.87 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=34.63 liquidity=50334068.0 spike=0.48
- EGAS.CA: score=24.56 buy_ready=False sector_rank=2 price=50.55 support=46.51 resistance=51.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=60.58 liquidity=22721614.0 spike=2.03
- EGBE.CA: score=2.37 buy_ready=False sector_rank=15 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:33 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=42471.8 spike=0.31
- EGCH.CA: score=17.14 buy_ready=False sector_rank=18 price=13.79 support=13.18 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=51.46 liquidity=26493816.0 spike=0.23
- EGSA.CA: score=10.64 buy_ready=False sector_rank=12 price=8.6 support=8.3 resistance=9.19 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=45.05 liquidity=35930.8 spike=2.43
- EGTS.CA: score=19.44 buy_ready=False sector_rank=3 price=18.1 support=13.45 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=78647168.0 spike=0.67
- EHDR.CA: score=20.24 buy_ready=False sector_rank=5 price=2.62 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=68.82 liquidity=51106048.0 spike=0.97
- EKHO.CA: score=12.5 buy_ready=False sector_rank=2 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=15.59 buy_ready=False sector_rank=14 price=2.09 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=54.17 liquidity=17827312.0 spike=0.67
- ELKA.CA: score=19.24 buy_ready=False sector_rank=5 price=1.22 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=70.97 liquidity=27464226.0 spike=0.63
- ELNA.CA: score=10.57 buy_ready=False sector_rank=5 price=39.45 support=37.11 resistance=42.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=60.24 liquidity=338564.41 spike=0.83
- ELSH.CA: score=19.46 buy_ready=False sector_rank=5 price=13.44 support=8.1 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=84.73 liquidity=172447584.0 spike=1.11
- ELWA.CA: score=7.9 buy_ready=False sector_rank=5 price=2.09 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=88.57 liquidity=661436.13 spike=0.22
- EMFD.CA: score=21.44 buy_ready=False sector_rank=3 price=11.3 support=9.83 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=70.96 liquidity=82544728.0 spike=0.33
- ENGC.CA: score=18.29 buy_ready=False sector_rank=5 price=33.73 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=66.59 liquidity=8050646.0 spike=0.58
- EOSB.CA: score=10.35 buy_ready=False sector_rank=5 price=1.42 support=1.34 resistance=1.53 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=114534.36 spike=0.95
- EPCO.CA: score=10.36 buy_ready=False sector_rank=5 price=9.02 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=60.0 liquidity=2126308.75 spike=0.18
- EPPK.CA: score=5.6 buy_ready=False sector_rank=5 price=12.17 support=11.67 resistance=13.6 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=45.77 liquidity=366913.33 spike=0.35
- ETEL.CA: score=14.74 buy_ready=False sector_rank=12 price=90.22 support=92.17 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=35.34 liquidity=70999424.0 spike=0.81
- ETRS.CA: score=17.24 buy_ready=False sector_rank=5 price=8.91 support=7.37 resistance=9.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=84.29 liquidity=23581860.0 spike=0.41
- EXPA.CA: score=17.33 buy_ready=False sector_rank=15 price=18.47 support=18.34 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=51.28 liquidity=26152708.0 spike=0.68
- FAIT.CA: score=5.97 buy_ready=False sector_rank=15 price=35.1 support=34.73 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=33.41 liquidity=3639636.75 spike=0.59
- FAITA.CA: score=7.35 buy_ready=False sector_rank=15 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=17938.8 spike=0.44
- FERC.CA: score=6.78 buy_ready=False sector_rank=18 price=76.02 support=76.5 resistance=82.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=40.99 liquidity=2643222.5 spike=0.47
- FWRY.CA: score=12.43 buy_ready=False sector_rank=21 price=17.85 support=18.01 resistance=21.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=36.41 liquidity=248917344.0 spike=0.88
- GBCO.CA: score=24.06 buy_ready=False sector_rank=1 price=27.46 support=25.25 resistance=29.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=70.7 liquidity=68856864.0 spike=0.53
- GDWA.CA: score=15.21 buy_ready=False sector_rank=5 price=0.78 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=58.51 liquidity=8974246.0 spike=0.92
- GGCC.CA: score=12.68 buy_ready=False sector_rank=5 price=0.4 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=56.76 liquidity=6442332.0 spike=0.85
- GIHD.CA: score=5.19 buy_ready=False sector_rank=5 price=39.46 support=35.15 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=44.34 liquidity=955013.69 spike=0.2
- GMCI.CA: score=7.54 buy_ready=False sector_rank=5 price=1.73 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=51.72 liquidity=305609.69 spike=0.91
- GRCA.CA: score=6.04 buy_ready=False sector_rank=5 price=53.29 support=52.18 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=26.07 liquidity=5805915.5 spike=0.65
- GSSC.CA: score=2.79 buy_ready=False sector_rank=5 price=247.68 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=10.31 liquidity=2557439.0 spike=0.39
- GTWL.CA: score=2.54 buy_ready=False sector_rank=5 price=46.9 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=32.04 liquidity=2308819.75 spike=0.32
- HDBK.CA: score=14.33 buy_ready=False sector_rank=15 price=138.5 support=138.75 resistance=147.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=43.16 liquidity=10225196.0 spike=0.7
- HELI.CA: score=19.44 buy_ready=False sector_rank=3 price=6.34 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=51.57 liquidity=55370352.0 spike=0.33
- HRHO.CA: score=12.02 buy_ready=False sector_rank=20 price=26.1 support=26.0 resistance=29.18 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=48.25 liquidity=53586740.0 spike=0.32
- ICID.CA: score=15.82 buy_ready=False sector_rank=5 price=6.7 support=4.5 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=84.81 liquidity=8579291.0 spike=0.57
- IDRE.CA: score=13.74 buy_ready=False sector_rank=5 price=42.05 support=40.0 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=59.23 liquidity=5503618.0 spike=0.17
- IFAP.CA: score=7.88 buy_ready=False sector_rank=6 price=18.93 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=44.84 liquidity=3653254.75 spike=0.36
- INFI.CA: score=10.01 buy_ready=False sector_rank=5 price=97.68 support=98.0 resistance=112.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=36.87 liquidity=2769873.25 spike=0.17
- IRON.CA: score=14.36 buy_ready=False sector_rank=18 price=32.39 support=31.83 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=41.37 liquidity=12378445.0 spike=1.61
- ISMA.CA: score=17.42 buy_ready=False sector_rank=5 price=29.89 support=22.08 resistance=30.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=90.3 liquidity=44779588.0 spike=1.09
- ISMQ.CA: score=22.66 buy_ready=False sector_rank=18 price=8.1 support=7.27 resistance=8.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=65.14 liquidity=156554000.0 spike=2.76
- ISPH.CA: score=18.1 buy_ready=False sector_rank=8 price=11.5 support=11.12 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=65.37 liquidity=92394720.0 spike=0.62
- JUFO.CA: score=19.75 buy_ready=False sector_rank=11 price=29.0 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=69.52 liquidity=29352922.0 spike=0.62
- KABO.CA: score=10.33 buy_ready=False sector_rank=10 price=6.05 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:38 PM market time freshness=DELAYED_CURRENT RSI=57.43 liquidity=6318311.0 spike=0.31
- KWIN.CA: score=10.59 buy_ready=False sector_rank=5 price=71.11 support=69.0 resistance=80.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=48.21 liquidity=2350028.5 spike=0.54
- KZPC.CA: score=14.9 buy_ready=False sector_rank=5 price=10.52 support=10.3 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=6664459.0 spike=0.5
- LCSW.CA: score=10.6 buy_ready=False sector_rank=17 price=26.18 support=26.16 resistance=29.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=51.65 liquidity=6457997.0 spike=0.41
- LUTS.CA: score=17.24 buy_ready=False sector_rank=5 price=0.64 support=0.54 resistance=0.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=75.95 liquidity=18984640.0 spike=0.98
- MAAL.CA: score=14.72 buy_ready=False sector_rank=5 price=5.67 support=4.44 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=90.42 liquidity=7483207.0 spike=0.56
- MASR.CA: score=18.24 buy_ready=False sector_rank=5 price=6.69 support=6.63 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=51.38 liquidity=59488668.0 spike=0.92
- MBSC.CA: score=12.14 buy_ready=False sector_rank=17 price=270.03 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=24.23 liquidity=29783176.0 spike=0.62
- MCQE.CA: score=14.14 buy_ready=False sector_rank=17 price=176.58 support=179.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=35.24 liquidity=15550770.0 spike=0.81
- MCRO.CA: score=14.24 buy_ready=False sector_rank=5 price=1.21 support=1.21 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=26544838.0 spike=0.34
- MENA.CA: score=14.95 buy_ready=False sector_rank=3 price=6.72 support=5.83 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:39 PM market time freshness=DELAYED_CURRENT RSI=59.57 liquidity=3512322.0 spike=0.21
- MEPA.CA: score=16.88 buy_ready=False sector_rank=5 price=1.68 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=8643931.0 spike=0.46
- MFPC.CA: score=9.48 buy_ready=False sector_rank=18 price=39.71 support=41.05 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=28.94 liquidity=95210792.0 spike=1.17
- MFSC.CA: score=13.24 buy_ready=False sector_rank=5 price=44.14 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=15.3 liquidity=11131303.0 spike=0.72
- MHOT.CA: score=13.68 buy_ready=False sector_rank=7 price=29.2 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=40.87 liquidity=5494885.5 spike=0.26
- MICH.CA: score=20.22 buy_ready=False sector_rank=5 price=36.83 support=35.01 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=83.56 liquidity=19799932.0 spike=1.49
- MILS.CA: score=20.24 buy_ready=False sector_rank=5 price=141.82 support=127.01 resistance=153.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=49.5 liquidity=10556480.0 spike=0.53
- MIPH.CA: score=8.97 buy_ready=False sector_rank=8 price=654.08 support=640.0 resistance=729.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=55.79 liquidity=869131.19 spike=0.28
- MOED.CA: score=4.48 buy_ready=False sector_rank=5 price=0.67 support=0.68 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=33.78 liquidity=5244119.5 spike=0.41
- MOIL.CA: score=10.62 buy_ready=False sector_rank=2 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=118915.29 spike=0.62
- MOIN.CA: score=9.89 buy_ready=False sector_rank=5 price=25.01 support=24.02 resistance=26.4 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=55.47 liquidity=656687.58 spike=0.4
- MOSC.CA: score=5.46 buy_ready=False sector_rank=5 price=249.5 support=252.0 resistance=320.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=21.91 liquidity=2228676.0 spike=0.2
- MPCI.CA: score=23.84 buy_ready=False sector_rank=5 price=214.79 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=60.61 liquidity=159607920.0 spike=1.8
- MPCO.CA: score=19.22 buy_ready=False sector_rank=6 price=1.7 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=65.38 liquidity=31576546.0 spike=0.43
- MPRC.CA: score=18.61 buy_ready=False sector_rank=5 price=32.2 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=62.67 liquidity=6373948.5 spike=0.29
- MTIE.CA: score=22.06 buy_ready=False sector_rank=1 price=8.84 support=8.71 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=12368141.0 spike=0.63
- NAHO.CA: score=4.24 buy_ready=False sector_rank=5 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=5976.6 spike=0.16
- NCCW.CA: score=17.24 buy_ready=False sector_rank=5 price=6.22 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=78.64 liquidity=13504510.0 spike=0.51
- NEDA.CA: score=8.57 buy_ready=False sector_rank=5 price=2.74 support=2.65 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=57.69 liquidity=329387.0 spike=0.49
- NHPS.CA: score=6.97 buy_ready=False sector_rank=5 price=67.56 support=67.0 resistance=73.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=40.75 liquidity=2730476.75 spike=0.32
- NINH.CA: score=1.31 buy_ready=False sector_rank=5 price=16.88 support=17.0 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=31.1 liquidity=1077602.5 spike=0.12
- NIPH.CA: score=18.1 buy_ready=False sector_rank=8 price=159.81 support=155.1 resistance=183.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=57.19 liquidity=42829732.0 spike=0.38
- OBRI.CA: score=14.6 buy_ready=False sector_rank=5 price=34.96 support=33.63 resistance=39.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=45.72 liquidity=7359593.5 spike=0.6
- OCDI.CA: score=16.44 buy_ready=False sector_rank=3 price=20.41 support=20.19 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=14312657.0 spike=0.35
- OCPH.CA: score=13.32 buy_ready=False sector_rank=5 price=342.03 support=346.01 resistance=409.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=40.19 liquidity=5088618.0 spike=0.59
- ODIN.CA: score=16.51 buy_ready=False sector_rank=5 price=2.02 support=1.89 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=6272140.0 spike=0.59
- OFH.CA: score=11.05 buy_ready=False sector_rank=5 price=0.6 support=0.6 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=46.94 liquidity=6813695.0 spike=0.3
- OIH.CA: score=10.34 buy_ready=False sector_rank=4 price=1.34 support=1.35 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=29.63 liquidity=22574216.0 spike=0.21
- OLFI.CA: score=22.95 buy_ready=False sector_rank=11 price=22.03 support=21.0 resistance=22.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=74.37 liquidity=49841256.0 spike=2.6
- ORAS.CA: score=4.6 buy_ready=False sector_rank=13 price=748.22 support=731.0 resistance=761.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=225385104.0 spike=1.0
- ORHD.CA: score=17.44 buy_ready=False sector_rank=3 price=36.05 support=33.0 resistance=39.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=111885056.0 spike=0.59
- ORWE.CA: score=20.01 buy_ready=False sector_rank=10 price=22.8 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=67.82 liquidity=29470148.0 spike=0.65
- PHAR.CA: score=18.1 buy_ready=False sector_rank=8 price=84.0 support=83.96 resistance=92.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=55.91 liquidity=10513851.0 spike=0.31
- PHDC.CA: score=19.44 buy_ready=False sector_rank=3 price=14.6 support=13.01 resistance=16.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=64.91 liquidity=105565792.0 spike=0.27
- PHTV.CA: score=5.99 buy_ready=False sector_rank=5 price=202.06 support=203.25 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:36 PM market time freshness=DELAYED_CURRENT RSI=23.43 liquidity=2758878.25 spike=0.19
- POUL.CA: score=17.75 buy_ready=False sector_rank=11 price=35.9 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=55.22 liquidity=15941748.0 spike=0.34
- PRCL.CA: score=21.14 buy_ready=False sector_rank=17 price=24.06 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=64.89 liquidity=19399090.0 spike=0.66
- PRDC.CA: score=16.63 buy_ready=False sector_rank=3 price=6.0 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=70.63 liquidity=5194765.0 spike=0.26
- PRMH.CA: score=20.24 buy_ready=False sector_rank=5 price=2.63 support=2.19 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=13799928.0 spike=0.92
- RACC.CA: score=17.73 buy_ready=False sector_rank=5 price=9.72 support=9.54 resistance=10.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=44.06 liquidity=9492294.0 spike=0.64
- RAKT.CA: score=9.28 buy_ready=False sector_rank=5 price=23.11 support=22.1 resistance=25.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=44.98 liquidity=562312.53 spike=2.24
- RAYA.CA: score=17.21 buy_ready=False sector_rank=16 price=6.83 support=6.9 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=45.3 liquidity=59454420.0 spike=0.54
- RMDA.CA: score=18.1 buy_ready=False sector_rank=8 price=4.97 support=4.95 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:41 PM market time freshness=DELAYED_CURRENT RSI=51.7 liquidity=21812182.0 spike=0.21
- ROTO.CA: score=16.7 buy_ready=False sector_rank=5 price=33.34 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=49.82 liquidity=6462679.0 spike=0.49
- RREI.CA: score=12.67 buy_ready=False sector_rank=5 price=3.41 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=51.43 liquidity=7434279.0 spike=0.31
- RTVC.CA: score=9.59 buy_ready=False sector_rank=5 price=3.88 support=3.75 resistance=4.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:40 PM market time freshness=DELAYED_CURRENT RSI=54.41 liquidity=2358492.75 spike=0.35
- RUBX.CA: score=8.21 buy_ready=False sector_rank=5 price=9.96 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=42.75 liquidity=3969196.5 spike=0.28
- SAUD.CA: score=14.33 buy_ready=False sector_rank=15 price=21.07 support=21.4 resistance=24.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=39.95 liquidity=12732523.0 spike=0.93
- SCEM.CA: score=8.14 buy_ready=False sector_rank=17 price=60.09 support=61.05 resistance=72.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=19273018.0 spike=0.49
- SCFM.CA: score=3.89 buy_ready=False sector_rank=5 price=249.0 support=255.03 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=24.26 liquidity=3652485.0 spike=0.22
- SCTS.CA: score=4.92 buy_ready=False sector_rank=9 price=609.76 support=590.01 resistance=690.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=26.34 liquidity=1864198.13 spike=0.17
- SDTI.CA: score=22.24 buy_ready=False sector_rank=5 price=46.2 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=62.1 liquidity=17682706.0 spike=0.91
- SEIG.CA: score=9.92 buy_ready=False sector_rank=5 price=180.73 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:37 PM market time freshness=DELAYED_CURRENT RSI=58.72 liquidity=1682867.75 spike=0.31
- SIPC.CA: score=11.31 buy_ready=False sector_rank=5 price=3.43 support=3.4 resistance=3.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=62.5 liquidity=6071837.0 spike=0.38
- SKPC.CA: score=13.14 buy_ready=False sector_rank=18 price=16.4 support=16.8 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=40.44 liquidity=56792624.0 spike=0.91
- SMFR.CA: score=7.61 buy_ready=False sector_rank=5 price=196.93 support=201.0 resistance=224.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=37.37 liquidity=2370804.0 spike=0.4
- SNFC.CA: score=14.18 buy_ready=False sector_rank=5 price=12.08 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=43.11 liquidity=5942270.0 spike=0.22
- SPIN.CA: score=7.39 buy_ready=False sector_rank=10 price=13.85 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=25.23 liquidity=6673422.0 spike=1.35
- SPMD.CA: score=17.39 buy_ready=False sector_rank=5 price=0.4 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:45 PM market time freshness=DELAYED_CURRENT RSI=62.77 liquidity=9154201.0 spike=0.37
- SUGR.CA: score=9.52 buy_ready=False sector_rank=11 price=48.32 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:44 PM market time freshness=DELAYED_CURRENT RSI=52.18 liquidity=5769088.5 spike=0.37
- SVCE.CA: score=13.24 buy_ready=False sector_rank=5 price=8.28 support=8.41 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=31.52 liquidity=14589910.0 spike=0.13
- SWDY.CA: score=17.59 buy_ready=False sector_rank=14 price=84.49 support=85.25 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=47.96 liquidity=17064788.0 spike=0.64
- TALM.CA: score=18.99 buy_ready=False sector_rank=9 price=15.95 support=15.12 resistance=16.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=62.57 liquidity=6925399.5 spike=0.55
- TMGH.CA: score=14.44 buy_ready=False sector_rank=3 price=93.71 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:42 PM market time freshness=DELAYED_CURRENT RSI=32.91 liquidity=204475936.0 spike=0.44
- TRTO.CA: score=7.22 buy_ready=False sector_rank=5 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=680.0 spike=1.49
- UEFM.CA: score=-0.04 buy_ready=False sector_rank=5 price=469.16 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=30.06 liquidity=720134.75 spike=0.65
- UEGC.CA: score=15.24 buy_ready=False sector_rank=5 price=1.36 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=12596671.0 spike=0.46
- UNIP.CA: score=16.24 buy_ready=False sector_rank=5 price=0.32 support=0.28 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:46 PM market time freshness=DELAYED_CURRENT RSI=83.02 liquidity=12806851.0 spike=0.68
- UNIT.CA: score=10.66 buy_ready=False sector_rank=3 price=13.53 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=66.58 liquidity=1218145.5 spike=0.11
- WCDF.CA: score=10.41 buy_ready=False sector_rank=5 price=539.84 support=535.0 resistance=555.0 source=Yahoo Finance as_of=2026-06-09T21:00:00+00:00 freshness=FRESH RSI=38.12 liquidity=577628.83 spike=1.8
- WKOL.CA: score=9.76 buy_ready=False sector_rank=5 price=293.85 support=290.0 resistance=324.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:47 PM market time freshness=DELAYED_CURRENT RSI=58.14 liquidity=1522586.88 spike=0.36
- ZEOT.CA: score=19.03 buy_ready=False sector_rank=5 price=8.98 support=8.41 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=51.16 liquidity=8873380.0 spike=1.46
- ZMID.CA: score=23.44 buy_ready=False sector_rank=3 price=6.08 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:43 PM market time freshness=DELAYED_CURRENT RSI=62.1 liquidity=128348424.0 spike=0.55

## Backtesting Lite
- EGAS.CA: 180d return=19.55%, max drawdown=-15.42%, MA20>MA50 days last20=20, as_of=2026-06-09T21:00:00+00:00
- ANFI.CA: 180d return=218.24%, max drawdown=-19.31%, MA20>MA50 days last20=20, as_of=2026-06-09T21:00:00+00:00
- GBCO.CA: 180d return=30.78%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-06-09T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- EGAS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Natural Gas and Mining Project summary=Evidence rejected for EGAS.CA: source text did not clearly match EGAS.CA / Natural Gas and Mining Project.
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- MPCI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Memphis Pharmaceuticals & Chemical Industries summary=Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=526 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- OLFI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Obour Land For Food Industries summary=Obour Land stock breaks through historical resistance barrier, settles at record levels – Analysis; Obour Land records over EGP 721.5m consolidated profits in 9M-24; Obour Land’s consolidated profits leap in H1-24; sales exceed EGP 3.8bn
  - Obour Land stock breaks through historical resistance barrier, settles at record levels – Analysis: https://english.mubasher.info/news/4550021/Obour-Land-stock-breaks-through-historical-resistance-barrier-settles-at-record-levels-Analysis/
  - Obour Land records over EGP 721.5m consolidated profits in 9M-24: https://english.mubasher.info/news/4353735/Obour-Land-records-over-EGP-721-5m-consolidated-profits-in-9M-24/
  - Obour Land’s consolidated profits leap in H1-24; sales exceed EGP 3.8bn: https://english.mubasher.info/news/4317274/Obour-Land-s-consolidated-profits-leap-in-H1-24-sales-exceed-EGP-3-8bn/
- ISMQ.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Iron and Steel for Mines and Quarries summary=Iron and Steel for Mines and Quarries stock stabilizes above key support after correction; Will Iron and Steel for Mines and Quarries stock hit new historical peaks?; Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25
  - Iron and Steel for Mines and Quarries stock stabilizes above key support after correction: https://english.mubasher.info/news/4578786/Iron-and-Steel-for-Mines-and-Quarries-stock-stabilizes-above-key-support-after-correction/
  - Will Iron and Steel for Mines and Quarries stock hit new historical peaks?: https://english.mubasher.info/news/4556956/Will-Iron-and-Steel-for-Mines-and-Quarries-stock-hit-new-historical-peaks-/
  - Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25: https://english.mubasher.info/news/4249734/Iron-and-Steel-for-Mines-and-Quarries-expects-EGP-448m-net-profit-in-FY24-25/
- ASPI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Aspire Capital Holding for Financial Investments summary=Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25; PREDCO, Aspire Holding consider establishing mortgage company; Pioneers Holding gets EGX&#39;s approval for capital cut, name change
  - Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25: https://english.mubasher.info/news/4541324/Aspire-Capital-records-higher-consolidated-net-profits-at-over-EGP-42m-in-9M-25/
  - PREDCO, Aspire Holding consider establishing mortgage company: https://english.mubasher.info/news/4185438/PREDCO-Aspire-Holding-consider-establishing-mortgage-company/
  - Pioneers Holding gets EGX&#39;s approval for capital cut, name change: https://english.mubasher.info/news/3861454/Pioneers-Holding-gets-EGX-s-approval-for-capital-cut-name-change/

## Warnings
- Evidence rejected for EGAS.CA: source text did not clearly match EGAS.CA / Natural Gas and Mining Project.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Evidence rejected for MPCI.CA: source text did not clearly match MPCI.CA / Memphis Pharmaceuticals & Chemical Industries.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence for OLFI.CA matches the company but no source/report date was detected.
- Evidence for ISMQ.CA matches the company but no source/report date was detected.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
