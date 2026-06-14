# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-14T10:50:04.058692+00:00
Generated Cairo: 2026-06-14 13:50
Run timing: target 11:00 Cairo | generated Cairo 2026-06-14 13:50 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-14 13:46

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 178/190
- Top sector: Automotive & Distribution

## Market Context
- Market trend: Bullish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 14
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 5.26% / above MA50 47.37%
- EGX70 regime: BEARISH / above MA20 43.24% / above MA50 78.38%
- Sector breadth: 4.76%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- PHDC.CA: liquidity=654200896.0 spike=1.79 score=8.06
- COMI.CA: liquidity=482557568.0 spike=0.72 score=19.67
- CCAP.CA: liquidity=419109600.0 spike=0.5 score=18.36
- TMGH.CA: liquidity=272265216.0 spike=0.61 score=14.48
- EMFD.CA: liquidity=247588368.0 spike=1.04 score=6.56

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD as EGX30 and EGX70 are both in a bearish regime with weak breadth (4.76%). Market risk mode is DEFENSIVE_NO_NEW_BUY, meaning new long entries are discouraged until broader conditions improve. Liquidity is cooling on several top‑ranked stocks and RSI levels are elevated, adding uncertainty to short‑term moves.
- EGX30/EGX70 trends bearish, median 5‑day returns –5% to –4%; only ~5% of stocks above MA20.
- Sector breadth low; leading sectors (Automotive, Textiles, Real Estate) show mixed returns and limited upside.
- Top‑ranked tickets (GBCO, ISMQ, ANFI, etc.) have high RSI, cooling liquidity or are far from support, limiting bullish case for the next 1‑3 days.
- Risk mode DEFENSIVE_NO_NEW_BUY reflects market regime; any new buys carry higher uncertainty.
- Outlook remains uncertain – watch for any shift in sector breadth or liquidity spikes before considering entries.

## Top Liquidity Spikes
- EASB.CA: spike=16.04 liquidity=16925168.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- TRTO.CA: spike=8.0 liquidity=5988.11 outlook=NEUTRAL score=39.43 buy_ready=False
- LUTS.CA: spike=6.9 liquidity=140801552.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- ANFI.CA: spike=3.32 liquidity=143236051.08 outlook=BULLISH_WATCH score=71.43 buy_ready=False
- CFGH.CA: spike=3.0 liquidity=18482.3 outlook=WEAK_OR_RISKY score=0 buy_ready=False

## Sector Leaderboard
- #1 Automotive & Distribution: score=4.83 5d=1.06% 20d=-4.12% aboveMA50=100.0%
- #2 Textiles: score=4.18 5d=-1.86% 20d=4.28% aboveMA50=75.0%
- #3 Real Estate: score=3.71 5d=-1.44% 20d=0.0% aboveMA50=69.23%
- #4 Investment Holding: score=3.41 5d=-4.1% 20d=7.16% aboveMA50=66.67%
- #5 Energy & Petrochemicals: score=3.19 5d=-1.29% 20d=0.1% aboveMA50=75.0%
- #6 Education: score=2.65 5d=-2.15% 20d=-3.64% aboveMA50=100.0%
- #7 General / Verified EGX Expansion: score=2.43 5d=-2.49% 20d=-2.17% aboveMA50=69.23%
- #8 Food, Beverages & Tobacco: score=2.22 5d=-3.69% 20d=-1.35% aboveMA50=85.71%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- HELI.CA: BULLISH_WATCH score=89.71 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- ZMID.CA: BULLISH_WATCH score=89.71 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KABO.CA: BULLISH_WATCH score=84.18 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=83.71 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- KWIN.CA: BULLISH_WATCH score=83.43 liquidity=TRADEABLE sector=IMPROVING risk=No major short-term scanner risk flags.
- ARAB.CA: BULLISH_WATCH score=80.71 liquidity=TRADEABLE sector=LEADING risk=momentum is extended
- COSG.CA: BULLISH_WATCH score=78.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- UEGC.CA: BULLISH_WATCH score=78.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MEPA.CA: BULLISH_WATCH score=78.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- SNFC.CA: BULLISH_WATCH score=78.43 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=11.71 buy_ready=False sector_rank=7 price=207.71 support=195.1 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=56.02 liquidity=1741366.5 spike=0.22
- ABUK.CA: score=10.72 buy_ready=False sector_rank=19 price=72.92 support=75.8 resistance=90.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=246850128.0 spike=2.07
- ACAMD.CA: score=19.97 buy_ready=False sector_rank=7 price=2.32 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=64.18 liquidity=102915736.0 spike=0.8
- ACGC.CA: score=10.66 buy_ready=False sector_rank=2 price=9.36 support=8.89 resistance=10.86 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=33.8 liquidity=4988515.5 spike=0.09
- ADCI.CA: score=23.53 buy_ready=False sector_rank=7 price=227.65 support=202.22 resistance=228.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=71.49 liquidity=18015010.0 spike=2.78
- ADIB.CA: score=17.67 buy_ready=False sector_rank=10 price=45.5 support=44.01 resistance=49.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=36.64 liquidity=53962952.0 spike=0.36
- ADPC.CA: score=4.7 buy_ready=False sector_rank=7 price=3.57 support=3.45 resistance=4.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=27.91 liquidity=4723187.0 spike=0.19
- AFDI.CA: score=15.34 buy_ready=False sector_rank=7 price=41.92 support=40.15 resistance=46.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=43.03 liquidity=7371301.0 spike=0.42
- AFMC.CA: score=9.18 buy_ready=False sector_rank=7 price=71.12 support=67.0 resistance=80.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=43.18 liquidity=1211925.88 spike=0.18
- AJWA.CA: score=21.19 buy_ready=False sector_rank=7 price=158.67 support=130.01 resistance=154.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=86.04 liquidity=39494288.0 spike=2.11
- ALCN.CA: score=13.7 buy_ready=False sector_rank=17 price=28.67 support=25.51 resistance=30.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=42.22 liquidity=14552424.0 spike=0.77
- ALUM.CA: score=11.67 buy_ready=False sector_rank=7 price=23.63 support=23.05 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=46.41 liquidity=3699245.5 spike=0.18
- AMER.CA: score=19.48 buy_ready=False sector_rank=3 price=2.69 support=2.52 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=47.37 liquidity=44663692.0 spike=0.41
- AMES.CA: score=4.56 buy_ready=False sector_rank=7 price=49.71 support=48.0 resistance=57.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=14.17 liquidity=1591186.38 spike=0.3
- AMIA.CA: score=19.71 buy_ready=False sector_rank=7 price=9.1 support=8.54 resistance=9.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=64.1 liquidity=9737307.0 spike=0.44
- AMOC.CA: score=10.28 buy_ready=False sector_rank=5 price=7.89 support=7.92 resistance=9.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=29.46 liquidity=45047808.0 spike=0.58
- ANFI.CA: score=23.61 buy_ready=False sector_rank=7 price=21.65 support=13.52 resistance=22.8 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=91.11 liquidity=143236051.08 spike=3.32
- APSW.CA: score=1.47 buy_ready=False sector_rank=7 price=8.64 support=8.24 resistance=9.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=34.67 liquidity=1476378.75 spike=1.51
- ARAB.CA: score=21.48 buy_ready=False sector_rank=3 price=0.21 support=0.19 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=63.33 liquidity=72074704.0 spike=0.84
- ARCC.CA: score=16.94 buy_ready=False sector_rank=16 price=56.42 support=53.35 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=50.58 liquidity=21902140.0 spike=0.51
- AREH.CA: score=16.97 buy_ready=False sector_rank=7 price=1.52 support=1.27 resistance=1.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=81.82 liquidity=19485000.0 spike=0.74
- ARVA.CA: score=20.17 buy_ready=False sector_rank=7 price=12.55 support=7.71 resistance=11.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=87.58 liquidity=39495824.0 spike=1.6
- ASCM.CA: score=17.43 buy_ready=False sector_rank=7 price=58.84 support=47.3 resistance=59.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=75.66 liquidity=87762488.0 spike=1.23
- ASPI.CA: score=21.97 buy_ready=False sector_rank=7 price=0.32 support=0.25 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=62.87 liquidity=45478524.0 spike=0.68
- ATLC.CA: score=7.41 buy_ready=False sector_rank=20 price=4.81 support=4.7 resistance=5.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=47.14 liquidity=1201607.25 spike=0.23
- ATQA.CA: score=12.58 buy_ready=False sector_rank=19 price=9.41 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=42.56 liquidity=18123684.0 spike=0.49
- AXPH.CA: score=8.88 buy_ready=False sector_rank=7 price=1122.32 support=1111.0 resistance=1190.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:21 PM market time freshness=DELAYED_CURRENT RSI=38.06 liquidity=910315.06 spike=0.23
- BINV.CA: score=14.28 buy_ready=False sector_rank=4 price=46.07 support=40.8 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=63.13 liquidity=1916207.13 spike=0.17
- BIOC.CA: score=9.3 buy_ready=False sector_rank=7 price=70.15 support=68.34 resistance=79.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=41.63 liquidity=1328083.25 spike=0.24
- BTFH.CA: score=12.2 buy_ready=False sector_rank=20 price=3.03 support=2.96 resistance=3.32 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=71717176.0 spike=0.31
- CAED.CA: score=6.02 buy_ready=False sector_rank=7 price=69.66 support=67.21 resistance=82.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=16.38 liquidity=3049546.25 spike=0.24
- CANA.CA: score=13.98 buy_ready=False sector_rank=10 price=36.47 support=34.07 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=59.43 liquidity=2314409.0 spike=0.16
- CCAP.CA: score=18.36 buy_ready=False sector_rank=4 price=5.22 support=4.82 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=49.06 liquidity=419109600.0 spike=0.5
- CCRS.CA: score=13.63 buy_ready=False sector_rank=7 price=2.44 support=2.21 resistance=2.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=49.21 liquidity=3662459.5 spike=0.14
- CEFM.CA: score=4.04 buy_ready=False sector_rank=7 price=105.49 support=100.53 resistance=119.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=31.67 liquidity=1063204.88 spike=0.28
- CERA.CA: score=12.76 buy_ready=False sector_rank=7 price=1.18 support=1.13 resistance=1.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=58.33 liquidity=3787601.5 spike=0.28
- CFGH.CA: score=2.99 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=18482.3 spike=3.0
- CICH.CA: score=-0.57 buy_ready=False sector_rank=20 price=11.53 support=11.1 resistance=13.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=15.82 liquidity=1222433.13 spike=0.27
- CIEB.CA: score=7.86 buy_ready=False sector_rank=10 price=23.5 support=23.27 resistance=24.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=44.55 liquidity=3194694.0 spike=0.38
- CIRA.CA: score=13.06 buy_ready=False sector_rank=6 price=26.61 support=25.23 resistance=28.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=32.41 liquidity=10285263.0 spike=0.37
- CLHO.CA: score=11.91 buy_ready=False sector_rank=9 price=15.11 support=14.25 resistance=16.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=36.15 liquidity=4083306.5 spike=0.12
- CNFN.CA: score=2.43 buy_ready=False sector_rank=20 price=4.43 support=4.36 resistance=4.95 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=34.85 liquidity=2224040.0 spike=0.14
- COMI.CA: score=19.67 buy_ready=False sector_rank=10 price=135.27 support=129.8 resistance=136.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=50.51 liquidity=482557568.0 spike=0.72
- COPR.CA: score=17.01 buy_ready=False sector_rank=7 price=0.36 support=0.32 resistance=0.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=48.65 liquidity=40436256.0 spike=1.02
- COSG.CA: score=19.97 buy_ready=False sector_rank=7 price=1.58 support=1.49 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=55.0 liquidity=35105356.0 spike=0.52
- CPCI.CA: score=11.55 buy_ready=False sector_rank=7 price=362.08 support=340.01 resistance=368.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:18 PM market time freshness=DELAYED_CURRENT RSI=64.68 liquidity=1578184.88 spike=0.54
- CSAG.CA: score=16.35 buy_ready=False sector_rank=17 price=31.0 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=45.14 liquidity=9650419.0 spike=0.67
- DAPH.CA: score=0.56 buy_ready=False sector_rank=7 price=77.43 support=76.6 resistance=92.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=25.25 liquidity=1588534.75 spike=0.05
- DEIN.CA: score=5.97 buy_ready=False sector_rank=7 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- DOMT.CA: score=1.38 buy_ready=False sector_rank=8 price=24.3 support=23.7 resistance=26.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=29.8 liquidity=1492985.88 spike=0.57
- DSCW.CA: score=15.97 buy_ready=False sector_rank=7 price=1.76 support=1.71 resistance=1.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=21146916.0 spike=0.41
- DTPP.CA: score=0.7 buy_ready=False sector_rank=7 price=120.26 support=117.01 resistance=137.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=21.72 liquidity=730471.31 spike=0.24
- EALR.CA: score=9.29 buy_ready=False sector_rank=7 price=356.42 support=346.01 resistance=386.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=48.98 liquidity=1321576.88 spike=0.28
- EASB.CA: score=9.97 buy_ready=False sector_rank=7 price=6.12 support=5.06 resistance=6.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=16925168.0 spike=16.04
- EAST.CA: score=19.89 buy_ready=False sector_rank=8 price=38.14 support=37.01 resistance=39.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=50.78 liquidity=31789944.0 spike=0.47
- EBSC.CA: score=13.59 buy_ready=False sector_rank=7 price=1.84 support=1.64 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=62.79 liquidity=1613059.75 spike=0.61
- ECAP.CA: score=10.36 buy_ready=False sector_rank=7 price=31.4 support=28.7 resistance=32.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=89.69 liquidity=1391489.88 spike=0.26
- EDFM.CA: score=8.44 buy_ready=False sector_rank=7 price=334.61 support=320.2 resistance=355.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=50.76 liquidity=470753.09 spike=0.69
- EEII.CA: score=13.73 buy_ready=False sector_rank=7 price=2.39 support=2.27 resistance=2.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=53.49 liquidity=3755434.5 spike=0.19
- EFIC.CA: score=-0.8 buy_ready=False sector_rank=19 price=204.85 support=192.01 resistance=219.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=15.17 liquidity=1613161.38 spike=0.45
- EFID.CA: score=17.89 buy_ready=False sector_rank=8 price=27.92 support=27.06 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=38.41 liquidity=12786266.0 spike=0.17
- EFIH.CA: score=7.4 buy_ready=False sector_rank=21 price=21.0 support=20.2 resistance=22.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=30.35 liquidity=27233548.0 spike=0.48
- EGAL.CA: score=11.58 buy_ready=False sector_rank=19 price=312.82 support=305.01 resistance=344.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=15.38 liquidity=29276818.0 spike=0.28
- EGAS.CA: score=20.07 buy_ready=False sector_rank=5 price=52.72 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=62.8 liquidity=9797621.0 spike=0.82
- EGBE.CA: score=2.68 buy_ready=False sector_rank=10 price=0.44 support=0.44 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=30.82 liquidity=16398.86 spike=0.12
- EGCH.CA: score=16.58 buy_ready=False sector_rank=19 price=13.4 support=13.2 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=47.28 liquidity=49673288.0 spike=0.43
- EGSA.CA: score=2.23 buy_ready=False sector_rank=13 price=8.74 support=8.3 resistance=9.19 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=25.37 liquidity=6598.7 spike=0.45
- EGTS.CA: score=19.48 buy_ready=False sector_rank=3 price=18.47 support=13.61 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=47.27 liquidity=51793476.0 spike=0.43
- EHDR.CA: score=20.09 buy_ready=False sector_rank=7 price=2.77 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=70.71 liquidity=56191988.0 spike=1.06
- EKHO.CA: score=10.28 buy_ready=False sector_rank=5 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=11.2 buy_ready=False sector_rank=18 price=2.11 support=2.06 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=46.43 liquidity=8526366.0 spike=0.31
- ELKA.CA: score=20.97 buy_ready=False sector_rank=7 price=1.26 support=1.12 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=62.86 liquidity=22507242.0 spike=0.51
- ELNA.CA: score=6.49 buy_ready=False sector_rank=7 price=37.65 support=37.11 resistance=41.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:41 AM market time freshness=DELAYED_CURRENT RSI=43.61 liquidity=762509.25 spike=1.88
- ELSH.CA: score=16.97 buy_ready=False sector_rank=7 price=13.56 support=8.1 resistance=14.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=78.34 liquidity=115535816.0 spike=0.7
- ELWA.CA: score=16.29 buy_ready=False sector_rank=7 price=2.15 support=1.79 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:23 PM market time freshness=DELAYED_CURRENT RSI=78.95 liquidity=6479693.0 spike=2.42
- EMFD.CA: score=6.56 buy_ready=False sector_rank=3 price=11.8 support=11.46 resistance=12.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=247588368.0 spike=1.04
- ENGC.CA: score=19.8 buy_ready=False sector_rank=7 price=34.54 support=32.31 resistance=35.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=58.88 liquidity=7824547.0 spike=0.57
- EOSB.CA: score=15.45 buy_ready=False sector_rank=7 price=1.48 support=1.34 resistance=1.49 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=299753.28 spike=2.59
- EPCO.CA: score=11.41 buy_ready=False sector_rank=7 price=9.12 support=8.56 resistance=9.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=47.45 liquidity=1434675.63 spike=0.13
- EPPK.CA: score=5.55 buy_ready=False sector_rank=7 price=12.0 support=11.67 resistance=13.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=51.18 liquidity=580030.38 spike=0.52
- ETEL.CA: score=10.08 buy_ready=False sector_rank=13 price=90.49 support=89.8 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=28.49 liquidity=120605120.0 spike=1.43
- ETRS.CA: score=4.97 buy_ready=False sector_rank=7 price=9.5 support=9.15 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=35348172.0 spike=0.62
- EXPA.CA: score=17.67 buy_ready=False sector_rank=10 price=18.61 support=18.31 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=47.4 liquidity=26287386.0 spike=0.71
- FAIT.CA: score=4.36 buy_ready=False sector_rank=10 price=35.6 support=35.0 resistance=38.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=22.01 liquidity=1687850.88 spike=0.27
- FAITA.CA: score=7.67 buy_ready=False sector_rank=10 price=0.99 support=0.98 resistance=1.0 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=4132.26 spike=0.1
- FERC.CA: score=5.39 buy_ready=False sector_rank=19 price=76.09 support=75.0 resistance=81.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=37.14 liquidity=1805204.38 spike=0.32
- FWRY.CA: score=7.4 buy_ready=False sector_rank=21 price=18.44 support=17.71 resistance=20.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=29.48 liquidity=147134256.0 spike=0.54
- GBCO.CA: score=23.93 buy_ready=False sector_rank=1 price=28.29 support=25.25 resistance=29.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=72.17 liquidity=82103728.0 spike=0.7
- GDWA.CA: score=10.03 buy_ready=False sector_rank=7 price=0.79 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=51.89 liquidity=6061435.5 spike=0.46
- GGCC.CA: score=11.59 buy_ready=False sector_rank=7 price=0.41 support=0.39 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=51.85 liquidity=2619853.0 spike=0.35
- GIHD.CA: score=8.61 buy_ready=False sector_rank=7 price=40.72 support=35.15 resistance=44.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=49.48 liquidity=634284.56 spike=0.13
- GMCI.CA: score=4.41 buy_ready=False sector_rank=7 price=1.7 support=1.68 resistance=1.84 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=39.29 liquidity=355529.51 spike=1.04
- GRCA.CA: score=6.64 buy_ready=False sector_rank=7 price=54.11 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=36.73 liquidity=1672229.5 spike=0.19
- GSSC.CA: score=1.56 buy_ready=False sector_rank=7 price=248.63 support=228.1 resistance=272.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=12.69 liquidity=1592650.75 spike=0.25
- GTWL.CA: score=1.72 buy_ready=False sector_rank=7 price=46.99 support=45.47 resistance=59.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=25.6 liquidity=1748717.38 spike=0.25
- HDBK.CA: score=12.72 buy_ready=False sector_rank=10 price=141.0 support=138.0 resistance=146.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=37.06 liquidity=8052845.0 spike=0.56
- HELI.CA: score=21.48 buy_ready=False sector_rank=3 price=6.51 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=52.56 liquidity=55682560.0 spike=0.34
- HRHO.CA: score=12.2 buy_ready=False sector_rank=20 price=26.61 support=25.8 resistance=29.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=42.27 liquidity=75021552.0 spike=0.5
- ICID.CA: score=16.97 buy_ready=False sector_rank=7 price=6.9 support=4.5 resistance=6.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=87.25 liquidity=14098004.0 spike=0.9
- IDRE.CA: score=13.96 buy_ready=False sector_rank=7 price=42.47 support=41.01 resistance=49.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=44.29 liquidity=5983342.5 spike=0.18
- IFAP.CA: score=0.31 buy_ready=False sector_rank=14 price=19.15 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=32.23 liquidity=2221810.25 spike=0.23
- INFI.CA: score=6.09 buy_ready=False sector_rank=7 price=99.34 support=97.0 resistance=109.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=24.0 liquidity=4122494.5 spike=0.27
- IRON.CA: score=9.96 buy_ready=False sector_rank=19 price=32.56 support=31.3 resistance=35.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=50.36 liquidity=5375706.5 spike=0.68
- ISMA.CA: score=18.97 buy_ready=False sector_rank=7 price=30.49 support=22.7 resistance=30.96 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=90.06 liquidity=31501938.0 spike=0.77
- ISMQ.CA: score=23.9 buy_ready=False sector_rank=19 price=8.44 support=7.27 resistance=8.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=71.36 liquidity=163345952.0 spike=2.66
- ISPH.CA: score=4.83 buy_ready=False sector_rank=9 price=12.05 support=11.82 resistance=12.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=81615120.0 spike=0.62
- JUFO.CA: score=21.89 buy_ready=False sector_rank=8 price=30.01 support=26.51 resistance=30.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=64.57 liquidity=13608381.0 spike=0.3
- KABO.CA: score=17.29 buy_ready=False sector_rank=2 price=6.3 support=5.92 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=60.91 liquidity=4617450.5 spike=0.22
- KWIN.CA: score=13.7 buy_ready=False sector_rank=7 price=71.94 support=69.0 resistance=78.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=48.18 liquidity=3731480.5 spike=0.87
- KZPC.CA: score=13.59 buy_ready=False sector_rank=7 price=10.64 support=10.3 resistance=11.52 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=53.62 liquidity=3615490.25 spike=0.28
- LCSW.CA: score=10.08 buy_ready=False sector_rank=16 price=26.48 support=26.0 resistance=28.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=49.63 liquidity=3140556.0 spike=0.21
- LUTS.CA: score=9.97 buy_ready=False sector_rank=7 price=0.7 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=140801552.0 spike=6.9
- MAAL.CA: score=10.78 buy_ready=False sector_rank=7 price=5.79 support=4.44 resistance=6.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=78.07 liquidity=3807561.0 spike=0.29
- MASR.CA: score=17.97 buy_ready=False sector_rank=7 price=6.87 support=6.54 resistance=7.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=44.8 liquidity=37279620.0 spike=0.61
- MBSC.CA: score=11.94 buy_ready=False sector_rank=16 price=272.87 support=261.52 resistance=295.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=31.43 liquidity=31746278.0 spike=0.68
- MCQE.CA: score=8.94 buy_ready=False sector_rank=16 price=176.7 support=174.0 resistance=201.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=11.65 liquidity=12828515.0 spike=0.71
- MCRO.CA: score=13.97 buy_ready=False sector_rank=7 price=1.24 support=1.2 resistance=1.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=47.62 liquidity=19956522.0 spike=0.34
- MENA.CA: score=20.73 buy_ready=False sector_rank=3 price=6.61 support=5.83 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=9250585.0 spike=0.55
- MEPA.CA: score=15.97 buy_ready=False sector_rank=7 price=1.71 support=1.63 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=6000304.0 spike=0.32
- MFPC.CA: score=10.06 buy_ready=False sector_rank=19 price=38.45 support=39.47 resistance=46.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=24.69 liquidity=144560880.0 spike=1.74
- MFSC.CA: score=6.84 buy_ready=False sector_rank=7 price=46.04 support=43.0 resistance=65.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=19.86 liquidity=3867586.0 spike=0.24
- MHOT.CA: score=8.81 buy_ready=False sector_rank=12 price=29.69 support=26.3 resistance=34.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=44.87 liquidity=1418926.13 spike=0.07
- MICH.CA: score=20.34 buy_ready=False sector_rank=7 price=37.03 support=35.01 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=63.94 liquidity=8372666.5 spike=0.59
- MILS.CA: score=4.97 buy_ready=False sector_rank=7 price=149.13 support=143.0 resistance=149.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14243080.0 spike=0.75
- MIPH.CA: score=8.64 buy_ready=False sector_rank=9 price=658.2 support=640.0 resistance=717.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:22 PM market time freshness=DELAYED_CURRENT RSI=52.05 liquidity=813819.69 spike=0.28
- MOED.CA: score=1.94 buy_ready=False sector_rank=7 price=0.68 support=0.65 resistance=0.82 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=26.97 liquidity=2964054.75 spike=0.25
- MOIL.CA: score=8.34 buy_ready=False sector_rank=5 price=0.47 support=0.44 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=63.77 liquidity=64521.01 spike=0.33
- MOIN.CA: score=7.35 buy_ready=False sector_rank=7 price=25.01 support=24.02 resistance=26.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=382392.22 spike=0.21
- MOSC.CA: score=8.69 buy_ready=False sector_rank=7 price=298.21 support=254.15 resistance=298.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=26980356.0 spike=2.86
- MPCI.CA: score=19.97 buy_ready=False sector_rank=7 price=220.7 support=197.0 resistance=238.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=64.0 liquidity=32330672.0 spike=0.36
- MPCO.CA: score=21.09 buy_ready=False sector_rank=14 price=1.78 support=1.54 resistance=1.93 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=64.15 liquidity=46905396.0 spike=0.62
- MPRC.CA: score=14.99 buy_ready=False sector_rank=7 price=32.15 support=30.61 resistance=34.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:16 PM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=5018668.0 spike=0.24
- MTIE.CA: score=17.24 buy_ready=False sector_rank=1 price=8.92 support=8.65 resistance=9.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=5311236.5 spike=0.27
- NAHO.CA: score=3.98 buy_ready=False sector_rank=7 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=6412.78 spike=0.2
- NCCW.CA: score=16.97 buy_ready=False sector_rank=7 price=6.47 support=5.13 resistance=6.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=76.78 liquidity=17128260.0 spike=0.64
- NEDA.CA: score=8.68 buy_ready=False sector_rank=7 price=2.75 support=2.65 resistance=2.87 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=53.57 liquidity=503871.5 spike=1.1
- NHPS.CA: score=8.45 buy_ready=False sector_rank=7 price=68.12 support=65.03 resistance=72.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=42.32 liquidity=1482647.38 spike=0.25
- NINH.CA: score=4.72 buy_ready=False sector_rank=7 price=17.22 support=16.8 resistance=20.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:24 PM market time freshness=DELAYED_CURRENT RSI=24.12 liquidity=1752433.0 spike=0.21
- NIPH.CA: score=19.83 buy_ready=False sector_rank=9 price=164.2 support=155.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=52.42 liquidity=71915744.0 spike=0.7
- OBRI.CA: score=8.01 buy_ready=False sector_rank=7 price=36.0 support=34.99 resistance=37.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29818892.0 spike=2.52
- OCDI.CA: score=16.48 buy_ready=False sector_rank=3 price=20.54 support=20.0 resistance=23.67 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=46.58 liquidity=36116468.0 spike=0.95
- OCPH.CA: score=5.2 buy_ready=False sector_rank=7 price=346.32 support=337.0 resistance=404.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=28.14 liquidity=2232911.25 spike=0.28
- ODIN.CA: score=15.5 buy_ready=False sector_rank=7 price=2.07 support=1.89 resistance=2.19 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=62.96 liquidity=3532462.25 spike=0.33
- OFH.CA: score=16.71 buy_ready=False sector_rank=7 price=0.61 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:29 PM market time freshness=DELAYED_CURRENT RSI=45.54 liquidity=39925680.0 spike=1.87
- OIH.CA: score=10.36 buy_ready=False sector_rank=4 price=1.38 support=1.33 resistance=1.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=41810780.0 spike=0.41
- OLFI.CA: score=17.43 buy_ready=False sector_rank=8 price=22.49 support=21.0 resistance=22.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=75.88 liquidity=23477350.0 spike=1.27
- ORAS.CA: score=4.6 buy_ready=False sector_rank=11 price=768.17 support=756.01 resistance=779.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=191216048.0 spike=1.0
- ORHD.CA: score=6.96 buy_ready=False sector_rank=3 price=38.32 support=36.92 resistance=38.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=227800432.0 spike=1.24
- ORWE.CA: score=22.67 buy_ready=False sector_rank=2 price=23.3 support=21.6 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=64.63 liquidity=16493333.0 spike=0.37
- PHAR.CA: score=17.83 buy_ready=False sector_rank=9 price=84.32 support=83.02 resistance=92.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=48.57 liquidity=12850392.0 spike=0.4
- PHDC.CA: score=8.06 buy_ready=False sector_rank=3 price=15.69 support=15.01 resistance=16.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=654200896.0 spike=1.79
- PHTV.CA: score=4.57 buy_ready=False sector_rank=7 price=205.06 support=201.55 resistance=233.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=1595353.88 spike=0.11
- POUL.CA: score=17.89 buy_ready=False sector_rank=8 price=35.46 support=34.8 resistance=39.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=47.04 liquidity=16720600.0 spike=0.36
- PRCL.CA: score=18.94 buy_ready=False sector_rank=16 price=24.2 support=21.01 resistance=28.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=59.4 liquidity=15742573.0 spike=0.55
- PRDC.CA: score=18.48 buy_ready=False sector_rank=3 price=6.37 support=5.3 resistance=6.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=80.77 liquidity=19810870.0 spike=0.22
- PRMH.CA: score=22.67 buy_ready=False sector_rank=7 price=2.75 support=2.19 resistance=2.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=69.7 liquidity=34868672.0 spike=2.35
- RACC.CA: score=10.98 buy_ready=False sector_rank=7 price=9.81 support=9.38 resistance=10.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=53.57 liquidity=3008191.75 spike=0.22
- RAKT.CA: score=1.95 buy_ready=False sector_rank=7 price=22.9 support=22.1 resistance=25.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=34.13 liquidity=402842.19 spike=1.29
- RAYA.CA: score=17.01 buy_ready=False sector_rank=15 price=7.09 support=6.7 resistance=8.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=45.9 liquidity=58206112.0 spike=0.58
- RMDA.CA: score=19.83 buy_ready=False sector_rank=9 price=5.15 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=14013806.0 spike=0.14
- ROTO.CA: score=13.16 buy_ready=False sector_rank=7 price=33.73 support=32.66 resistance=36.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=52.08 liquidity=3183688.25 spike=0.24
- RREI.CA: score=13.21 buy_ready=False sector_rank=7 price=3.49 support=3.32 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=50.7 liquidity=5235037.0 spike=0.23
- RTVC.CA: score=10.2 buy_ready=False sector_rank=7 price=3.85 support=3.75 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=52.11 liquidity=3226871.0 spike=0.48
- RUBX.CA: score=9.5 buy_ready=False sector_rank=7 price=9.96 support=9.8 resistance=11.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=40.41 liquidity=5525054.0 spike=0.4
- SAUD.CA: score=9.03 buy_ready=False sector_rank=10 price=21.6 support=20.82 resistance=23.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=37.87 liquidity=4366893.5 spike=0.31
- SCEM.CA: score=5.82 buy_ready=False sector_rank=16 price=61.27 support=59.3 resistance=69.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=29.59 liquidity=6882537.5 spike=0.18
- SCFM.CA: score=7.85 buy_ready=False sector_rank=7 price=257.97 support=248.1 resistance=315.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=26.94 liquidity=4873167.5 spike=0.36
- SCTS.CA: score=4.67 buy_ready=False sector_rank=6 price=611.87 support=590.01 resistance=689.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:19 PM market time freshness=DELAYED_CURRENT RSI=25.78 liquidity=1605549.88 spike=0.16
- SDTI.CA: score=16.91 buy_ready=False sector_rank=7 price=47.35 support=43.4 resistance=47.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=62.56 liquidity=4942251.5 spike=0.26
- SEIG.CA: score=10.89 buy_ready=False sector_rank=7 price=183.47 support=173.35 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:25 PM market time freshness=DELAYED_CURRENT RSI=53.36 liquidity=916220.69 spike=0.17
- SIPC.CA: score=9.15 buy_ready=False sector_rank=7 price=3.43 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=40.82 liquidity=4180123.25 spike=0.29
- SKPC.CA: score=12.58 buy_ready=False sector_rank=19 price=16.42 support=16.29 resistance=18.24 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=37.6 liquidity=16413188.0 spike=0.26
- SMFR.CA: score=5.07 buy_ready=False sector_rank=7 price=202.62 support=192.0 resistance=222.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=28.85 liquidity=2096290.25 spike=0.36
- SNFC.CA: score=15.41 buy_ready=False sector_rank=7 price=12.33 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:30 PM market time freshness=DELAYED_CURRENT RSI=46.44 liquidity=5440788.0 spike=0.2
- SPIN.CA: score=8.69 buy_ready=False sector_rank=2 price=14.01 support=13.61 resistance=15.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:14 PM market time freshness=DELAYED_CURRENT RSI=41.94 liquidity=1015269.25 spike=0.21
- SPMD.CA: score=10.42 buy_ready=False sector_rank=7 price=0.41 support=0.38 resistance=0.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=56.19 liquidity=2452442.25 spike=0.1
- SUGR.CA: score=10.42 buy_ready=False sector_rank=8 price=48.96 support=48.0 resistance=52.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:28 PM market time freshness=DELAYED_CURRENT RSI=46.0 liquidity=2529718.75 spike=0.16
- SVCE.CA: score=12.97 buy_ready=False sector_rank=7 price=8.35 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=27.69 liquidity=12746537.0 spike=0.14
- SWDY.CA: score=14.97 buy_ready=False sector_rank=18 price=85.92 support=84.01 resistance=90.77 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=39.98 liquidity=8295141.0 spike=0.34
- TALM.CA: score=8.1 buy_ready=False sector_rank=6 price=16.03 support=15.12 resistance=16.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:20 PM market time freshness=DELAYED_CURRENT RSI=79.26 liquidity=1042080.25 spike=0.08
- TMGH.CA: score=14.48 buy_ready=False sector_rank=3 price=95.26 support=91.87 resistance=101.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=28.48 liquidity=272265216.0 spike=0.61
- TRTO.CA: score=10.98 buy_ready=False sector_rank=7 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-10T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=5988.11 spike=8.0
- UEFM.CA: score=-0.69 buy_ready=False sector_rank=7 price=469.72 support=455.6 resistance=500.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=26.76 liquidity=337685.16 spike=0.36
- UEGC.CA: score=19.48 buy_ready=False sector_rank=7 price=1.39 support=1.3 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:31 PM market time freshness=DELAYED_CURRENT RSI=56.67 liquidity=7508174.0 spike=0.28
- UNIP.CA: score=15.97 buy_ready=False sector_rank=7 price=0.32 support=0.28 resistance=0.34 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=80.39 liquidity=13680992.0 spike=0.7
- UNIT.CA: score=12.47 buy_ready=False sector_rank=3 price=13.92 support=12.07 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:26 PM market time freshness=DELAYED_CURRENT RSI=61.5 liquidity=989753.5 spike=0.09
- WCDF.CA: score=-4.14 buy_ready=False sector_rank=7 price=505.6 support=450.0 resistance=544.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=443045.63 spike=1.22
- WKOL.CA: score=8.73 buy_ready=False sector_rank=7 price=290.56 support=290.0 resistance=319.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=3753416.75 spike=0.94
- ZEOT.CA: score=17.94 buy_ready=False sector_rank=7 price=9.2 support=8.41 resistance=9.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:32 PM market time freshness=DELAYED_CURRENT RSI=63.78 liquidity=5965312.0 spike=0.95
- ZMID.CA: score=21.48 buy_ready=False sector_rank=3 price=6.25 support=5.77 resistance=6.57 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:27 PM market time freshness=DELAYED_CURRENT RSI=59.69 liquidity=129799416.0 spike=0.55

## Backtesting Lite
- GBCO.CA: 180d return=31.89%, max drawdown=-24.35%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- ISMQ.CA: 180d return=39.19%, max drawdown=-16.39%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- ANFI.CA: 180d return=235.87%, max drawdown=-19.31%, MA20>MA50 days last20=20, as_of=2026-06-10T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GBCO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=GB Corp summary=Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- ISMQ.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Iron and Steel for Mines and Quarries summary=Iron and Steel for Mines and Quarries stock stabilizes above key support after correction; Will Iron and Steel for Mines and Quarries stock hit new historical peaks?; Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25
  - Iron and Steel for Mines and Quarries stock stabilizes above key support after correction: https://english.mubasher.info/news/4578786/Iron-and-Steel-for-Mines-and-Quarries-stock-stabilizes-above-key-support-after-correction/
  - Will Iron and Steel for Mines and Quarries stock hit new historical peaks?: https://english.mubasher.info/news/4556956/Will-Iron-and-Steel-for-Mines-and-Quarries-stock-hit-new-historical-peaks-/
  - Iron and Steel for Mines and Quarries expects EGP 448m net profit in FY24/25: https://english.mubasher.info/news/4249734/Iron-and-Steel-for-Mines-and-Quarries-expects-EGP-448m-net-profit-in-FY24-25/
- ANFI.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Tycoon Holding Company For Financial Investments summary=Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- ADCI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=The Arab Drug Company summary=ADCO’s net profits after tax cross EGP 182.5m in 8M-25/26; Arab Drug unveils cash dividends for FY22/23; Arab Drug’s OGM approves FY21/22 dividends
  - ADCO’s net profits after tax cross EGP 182.5m in 8M-25/26: https://english.mubasher.info/news/4587961/ADCO-s-net-profits-after-tax-cross-EGP-182-5m-in-8M-25-26/
  - Arab Drug unveils cash dividends for FY22/23: https://english.mubasher.info/news/4193946/Arab-Drug-unveils-cash-dividends-for-FY22-23/
  - Arab Drug’s OGM approves FY21/22 dividends: https://english.mubasher.info/news/4022664/Arab-Drug-s-OGM-approves-FY21-22-dividends/
- ORWE.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=529 sources=3 expected=Oriental Weavers summary=Oriental Weavers to disburse EGP 1.5/shr dividends for 2025; Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025; Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25
  - Oriental Weavers to disburse EGP 1.5/shr dividends for 2025: https://english.mubasher.info/news/4590236/Oriental-Weavers-to-disburse-EGP-1-5-shr-dividends-for-2025/
  - Oriental Weavers’ consolidated profits cross EGP 2.2bn in 2025: https://english.mubasher.info/news/4562972/Oriental-Weavers-consolidated-profits-cross-EGP-2-2bn-in-2025/
  - Oriental Weavers generates EGP 12.5bn consolidated sales in H1-25: https://english.mubasher.info/news/4487417/Oriental-Weavers-generates-EGP-12-5bn-consolidated-sales-in-H1-25/
- PRMH.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Prime Holding S.A.E summary=Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- ASPI.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Aspire Capital Holding for Financial Investments summary=Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25; PREDCO, Aspire Holding consider establishing mortgage company; Pioneers Holding gets EGX&#39;s approval for capital cut, name change
  - Aspire Capital records higher consolidated net profits at over EGP 42m in 9M-25: https://english.mubasher.info/news/4541324/Aspire-Capital-records-higher-consolidated-net-profits-at-over-EGP-42m-in-9M-25/
  - PREDCO, Aspire Holding consider establishing mortgage company: https://english.mubasher.info/news/4185438/PREDCO-Aspire-Holding-consider-establishing-mortgage-company/
  - Pioneers Holding gets EGX&#39;s approval for capital cut, name change: https://english.mubasher.info/news/3861454/Pioneers-Holding-gets-EGX-s-approval-for-capital-cut-name-change/
- JUFO.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Juhayna Food Industries summary=Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.

## Warnings
- Evidence rejected for GBCO.CA: source text did not clearly match GBCO.CA / GB Corp.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for ISMQ.CA matches the company but no source/report date was detected.
- Mubasher stock-page evidence failed for ANFI.CA: 404 Client Error: Not Found for url: https://english.mubasher.info/markets/EGX/stocks/ANFI
- No Yahoo or Mubasher evidence found for ANFI.CA.
- Evidence rejected for ANFI.CA: source text did not clearly match ANFI.CA / Tycoon Holding Company For Financial Investments.
- Evidence for ADCI.CA matches the company but no source/report date was detected.
- Evidence for ORWE.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for PRMH.CA: source text did not clearly match PRMH.CA / Prime Holding S.A.E.
- Evidence for ASPI.CA matches the company but no source/report date was detected.
- Evidence rejected for JUFO.CA: source text did not clearly match JUFO.CA / Juhayna Food Industries.
