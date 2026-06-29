# Telegram-First EGX Scanner Report

Scan phase: Pre-market risk check
Generated UTC: 2026-06-29T10:15:44.669111+00:00
Generated Cairo: 2026-06-29 13:15
Run timing: target 08:45 Cairo | generated Cairo 2026-06-29 13:15 | cron 45 5 * * 0-4
Trigger: scheduled cron=45 5 * * 0-4 mapped to pre_market; Cairo now 2026-06-29 13:12

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 182/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Monday, June 29
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 25.0%
- EGX70 regime: BEARISH / above MA20 32.5% / above MA50 62.5%
- Sector breadth: 9.52%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- COMI.CA: liquidity=406995488.0 spike=0.72 score=13.91
- ORAS.CA: liquidity=171899776.0 spike=1.0 score=4.6
- CCAP.CA: liquidity=169147520.0 spike=0.25 score=8.64
- PHDC.CA: liquidity=115466816.0 spike=0.28 score=17.93
- TMGH.CA: liquidity=115260272.0 spike=0.29 score=14.93

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (≈9.5%). Liquidity is thin and most sectors are under pressure, so the risk mode is DEFENSIVE_NO_NEW_BUY. The top‑ranked tickets show mixed outlooks – a constructive case for RUBX.CA but an overheated RSI, and bullish‑watch signals for CSAG.CA, ZMID.CA, MTIE.CA, POUL.CA, MHOT.CA, LCSW.CA and CNFN.CA, yet none meet the buy‑ready criteria amid the current market stance.
- EGX30/EGX70 bearish, median 5‑day returns –3.5% and –3.7%; liquidity spikes low → defensive posture.
- Sector breadth only 9.5%; leading sectors (Tourism, Automotive, Transport) lack strong momentum.
- Top tickets have supportive liquidity and near‑term support levels, but RSI or sector weakness limits entry.
- Risk mode DEFENSIVE_NO_NEW_BUY means new longs are paused until market breadth improves.
- Uncertainty remains high; watch for any shift in EGX30/EGX70 breadth or liquidity spikes before reconsidering buys.

## Top Liquidity Spikes
- DTPP.CA: spike=8.46 liquidity=12278720.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GTWL.CA: spike=5.3 liquidity=98790112.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- RUBX.CA: spike=3.46 liquidity=52371984.0 outlook=CONSTRUCTIVE score=68.76 buy_ready=False
- ZEOT.CA: spike=2.98 liquidity=78660392.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- EPPK.CA: spike=2.96 liquidity=3133733.67 outlook=BULLISH_WATCH score=76.76 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=8.8 5d=2.1% 20d=8.17% aboveMA50=100.0%
- #2 Automotive & Distribution: score=8.34 5d=1.75% 20d=7.28% aboveMA50=100.0%
- #3 Transportation & Logistics: score=3.41 5d=-0.49% 20d=-1.76% aboveMA50=50.0%
- #4 Real Estate: score=2.33 5d=-4.04% 20d=1.47% aboveMA50=69.23%
- #5 Food, Beverages & Tobacco: score=2.0 5d=-3.6% 20d=0.24% aboveMA50=57.14%
- #6 Education: score=1.98 5d=-3.76% 20d=0.84% aboveMA50=66.67%
- #7 Energy & Petrochemicals: score=1.71 5d=-2.66% 20d=0.54% aboveMA50=75.0%
- #8 Industrial Goods & Construction: score=1.5 5d=0.0% 20d=0.0% aboveMA50=0.0%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- MHOT.CA: BULLISH_WATCH score=88.8 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- CSAG.CA: BULLISH_WATCH score=88.41 liquidity=TRADEABLE sector=LEADING risk=No major short-term scanner risk flags.
- MTIE.CA: BULLISH_WATCH score=81.34 liquidity=TRADEABLE sector=LEADING risk=below MA20
- ZMID.CA: BULLISH_WATCH score=78.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- MENA.CA: BULLISH_WATCH score=78.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- POUL.CA: BULLISH_WATCH score=78.0 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- EPPK.CA: BULLISH_WATCH score=76.76 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; close to resistance; sector is not leading
- LCSW.CA: BULLISH_WATCH score=76.22 liquidity=TRADEABLE sector=IMPROVING risk=sector is not leading
- ORHD.CA: BULLISH_WATCH score=72.33 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CNFN.CA: BULLISH_WATCH score=71.86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=16.44 buy_ready=False sector_rank=13 price=202.0 support=196.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=35.98 liquidity=11866910.0 spike=2.07
- ABUK.CA: score=8.0 buy_ready=False sector_rank=20 price=67.25 support=67.69 resistance=84.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=9.15 liquidity=44718564.0 spike=0.33
- ACAMD.CA: score=17.3 buy_ready=False sector_rank=13 price=2.19 support=2.14 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=41.18 liquidity=35975584.0 spike=0.29
- ACGC.CA: score=17.55 buy_ready=False sector_rank=9 price=9.2 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=38.76 liquidity=12169491.0 spike=0.29
- ADCI.CA: score=14.01 buy_ready=False sector_rank=13 price=239.95 support=211.0 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=84.03 liquidity=7705494.5 spike=0.84
- ADIB.CA: score=13.91 buy_ready=False sector_rank=16 price=44.89 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=20601612.0 spike=0.21
- ADPC.CA: score=11.73 buy_ready=False sector_rank=13 price=3.37 support=3.38 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=8428749.0 spike=0.37
- AFDI.CA: score=12.29 buy_ready=False sector_rank=13 price=42.77 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=46.07 liquidity=4987701.0 spike=0.33
- AFMC.CA: score=-0.16 buy_ready=False sector_rank=13 price=67.2 support=66.66 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=29.03 liquidity=532015.25 spike=0.21
- AJWA.CA: score=8.71 buy_ready=False sector_rank=13 price=176.19 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=83.3 liquidity=2408058.0 spike=0.09
- ALCN.CA: score=5.29 buy_ready=False sector_rank=3 price=27.88 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=32.2 liquidity=3926822.0 spike=0.32
- ALUM.CA: score=1.63 buy_ready=False sector_rank=13 price=20.87 support=20.55 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=16.11 liquidity=2323450.25 spike=0.24
- AMER.CA: score=9.93 buy_ready=False sector_rank=4 price=2.34 support=2.3 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=25.56 liquidity=19384520.0 spike=0.26
- AMES.CA: score=-0.23 buy_ready=False sector_rank=13 price=46.5 support=45.45 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=25.69 liquidity=1463786.63 spike=0.54
- AMIA.CA: score=9.63 buy_ready=False sector_rank=13 price=8.54 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:47 AM market time freshness=DELAYED_CURRENT RSI=38.81 liquidity=2327422.0 spike=0.17
- AMOC.CA: score=9.68 buy_ready=False sector_rank=7 price=7.51 support=7.42 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=10.0 liquidity=17051804.0 spike=0.35
- ANFI.CA: score=5.64 buy_ready=False sector_rank=13 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=STALE RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=-1.01 buy_ready=False sector_rank=13 price=8.29 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=12.5 liquidity=687710.31 spike=0.88
- ARAB.CA: score=14.93 buy_ready=False sector_rank=4 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=55.88 liquidity=51024324.0 spike=0.6
- ARCC.CA: score=8.84 buy_ready=False sector_rank=15 price=54.4 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=31.02 liquidity=9752336.0 spike=0.28
- AREH.CA: score=19.3 buy_ready=False sector_rank=13 price=1.55 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=54.39 liquidity=10804040.0 spike=0.32
- ARVA.CA: score=16.75 buy_ready=False sector_rank=13 price=11.03 support=8.2 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=46.55 liquidity=9445582.0 spike=0.3
- ASCM.CA: score=19.3 buy_ready=False sector_rank=13 price=58.52 support=47.5 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=53.76 liquidity=35200532.0 spike=0.38
- ASPI.CA: score=12.92 buy_ready=False sector_rank=13 price=0.31 support=0.27 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=36.92 liquidity=5616905.5 spike=0.08
- ATLC.CA: score=8.34 buy_ready=False sector_rank=12 price=5.0 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=49.44 liquidity=996937.94 spike=0.16
- ATQA.CA: score=11.91 buy_ready=False sector_rank=20 price=9.45 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=41.31 liquidity=9907439.0 spike=0.3
- AXPH.CA: score=3.11 buy_ready=False sector_rank=13 price=1084.76 support=1073.0 resistance=1174.0 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=31.18 liquidity=809230.97 spike=0.66
- BINV.CA: score=8.22 buy_ready=False sector_rank=19 price=45.64 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=50.05 liquidity=1574214.63 spike=0.15
- BIOC.CA: score=0.14 buy_ready=False sector_rank=13 price=67.89 support=66.75 resistance=75.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=31.39 liquidity=840297.31 spike=0.34
- BTFH.CA: score=13.34 buy_ready=False sector_rank=12 price=2.98 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=79319840.0 spike=0.42
- CAED.CA: score=4.84 buy_ready=False sector_rank=13 price=69.14 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=43.65 liquidity=537799.69 spike=0.11
- CANA.CA: score=1.52 buy_ready=False sector_rank=16 price=35.16 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=31.12 liquidity=3616026.25 spike=0.34
- CCAP.CA: score=8.64 buy_ready=False sector_rank=19 price=4.72 support=4.72 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=17.05 liquidity=169147520.0 spike=0.25
- CCRS.CA: score=17.3 buy_ready=False sector_rank=13 price=2.25 support=2.28 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=35.09 liquidity=12214165.0 spike=0.7
- CEFM.CA: score=-0.17 buy_ready=False sector_rank=13 price=96.24 support=98.0 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=20.82 liquidity=1521622.13 spike=0.89
- CERA.CA: score=10.85 buy_ready=False sector_rank=13 price=1.21 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=53.85 liquidity=4548384.0 spike=0.27
- CFGH.CA: score=-0.32 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=0.0 liquidity=11200.0 spike=1.68
- CICH.CA: score=7.45 buy_ready=False sector_rank=12 price=11.77 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=46.3 liquidity=1104926.13 spike=0.34
- CIEB.CA: score=9.05 buy_ready=False sector_rank=16 price=23.52 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=49.09 liquidity=5139152.0 spike=0.8
- CIRA.CA: score=14.64 buy_ready=False sector_rank=6 price=28.19 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=62.1 liquidity=4852552.5 spike=0.27
- CLHO.CA: score=21.21 buy_ready=False sector_rank=17 price=16.16 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=61.84 liquidity=41905180.0 spike=1.19
- CNFN.CA: score=21.34 buy_ready=False sector_rank=12 price=4.67 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=12592174.0 spike=0.31
- COMI.CA: score=13.91 buy_ready=False sector_rank=16 price=127.18 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=49.33 liquidity=406995488.0 spike=0.72
- COPR.CA: score=16.3 buy_ready=False sector_rank=13 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=10146213.0 spike=0.34
- COSG.CA: score=9.3 buy_ready=False sector_rank=13 price=1.5 support=1.48 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=29.73 liquidity=12327041.0 spike=0.23
- CPCI.CA: score=10.77 buy_ready=False sector_rank=13 price=374.31 support=347.11 resistance=378.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=56.92 liquidity=1468125.13 spike=0.78
- CSAG.CA: score=23.36 buy_ready=False sector_rank=3 price=32.33 support=30.08 resistance=33.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=60.25 liquidity=15255469.0 spike=0.96
- DAPH.CA: score=8.59 buy_ready=False sector_rank=13 price=80.18 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=44.51 liquidity=2282336.75 spike=0.22
- DEIN.CA: score=5.3 buy_ready=False sector_rank=13 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.92 buy_ready=False sector_rank=5 price=26.12 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=70.0 liquidity=2124799.25 spike=0.55
- DSCW.CA: score=13.3 buy_ready=False sector_rank=13 price=1.72 support=1.71 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=10138998.0 spike=0.26
- DTPP.CA: score=9.3 buy_ready=False sector_rank=13 price=138.38 support=120.0 resistance=138.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=12278720.0 spike=8.46
- EALR.CA: score=5.96 buy_ready=False sector_rank=13 price=342.87 support=332.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=38.22 liquidity=1658044.63 spike=0.52
- EASB.CA: score=20.78 buy_ready=False sector_rank=13 price=7.72 support=4.66 resistance=10.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=74.07 liquidity=20412512.0 spike=1.74
- EAST.CA: score=13.8 buy_ready=False sector_rank=5 price=37.26 support=37.0 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=14648958.0 spike=0.36
- EBSC.CA: score=4.79 buy_ready=False sector_rank=13 price=1.73 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=37.5 liquidity=481300.91 spike=0.18
- ECAP.CA: score=13.66 buy_ready=False sector_rank=13 price=32.01 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=55.96 liquidity=4353200.0 spike=0.5
- EDFM.CA: score=-0.42 buy_ready=False sector_rank=13 price=330.59 support=320.29 resistance=355.0 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=26.96 liquidity=272406.16 spike=0.51
- EEII.CA: score=7.16 buy_ready=False sector_rank=13 price=2.37 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=44.07 liquidity=2857293.5 spike=0.21
- EFIC.CA: score=-2.57 buy_ready=False sector_rank=20 price=190.77 support=192.0 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:34 AM market time freshness=DELAYED_CURRENT RSI=13.84 liquidity=428222.69 spike=0.22
- EFID.CA: score=9.8 buy_ready=False sector_rank=5 price=26.97 support=25.5 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=25.19 liquidity=71523368.0 spike=0.97
- EFIH.CA: score=11.28 buy_ready=False sector_rank=21 price=20.31 support=20.0 resistance=22.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=42.16 liquidity=8463783.0 spike=0.19
- EGAL.CA: score=8.0 buy_ready=False sector_rank=20 price=274.94 support=273.1 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=10.52 liquidity=15285175.0 spike=0.23
- EGAS.CA: score=9.56 buy_ready=False sector_rank=7 price=48.53 support=46.51 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=51.34 liquidity=1873261.25 spike=0.2
- EGBE.CA: score=10.93 buy_ready=False sector_rank=16 price=0.45 support=0.43 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=25950.38 spike=0.28
- EGCH.CA: score=8.0 buy_ready=False sector_rank=20 price=12.22 support=12.15 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=21.54 liquidity=15530373.0 spike=0.28
- EGSA.CA: score=7.14 buy_ready=False sector_rank=14 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=36.0 liquidity=1767.5 spike=0.19
- EGTS.CA: score=14.93 buy_ready=False sector_rank=4 price=16.42 support=16.11 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=41.49 liquidity=16402569.0 spike=0.18
- EHDR.CA: score=17.3 buy_ready=False sector_rank=13 price=2.41 support=2.27 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=16011764.0 spike=0.28
- EKHO.CA: score=9.68 buy_ready=False sector_rank=7 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=8.08 buy_ready=False sector_rank=18 price=2.09 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=40.74 liquidity=5264408.5 spike=0.27
- ELKA.CA: score=16.3 buy_ready=False sector_rank=13 price=1.21 support=1.16 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=12228563.0 spike=0.3
- ELNA.CA: score=-1.27 buy_ready=False sector_rank=13 price=36.03 support=35.55 resistance=41.51 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=33.43 liquidity=425190.02 spike=1.0
- ELSH.CA: score=12.3 buy_ready=False sector_rank=13 price=11.57 support=8.29 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=33948252.0 spike=0.18
- ELWA.CA: score=7.83 buy_ready=False sector_rank=13 price=1.98 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=36.36 liquidity=524889.5 spike=0.16
- EMFD.CA: score=17.93 buy_ready=False sector_rank=4 price=11.44 support=10.8 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=41.44 liquidity=25068348.0 spike=0.09
- ENGC.CA: score=16.73 buy_ready=False sector_rank=13 price=36.79 support=32.9 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=5422254.5 spike=0.38
- EOSB.CA: score=11.37 buy_ready=False sector_rank=13 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=65744.56 spike=0.49
- EPCO.CA: score=6.18 buy_ready=False sector_rank=13 price=8.69 support=8.69 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=38.82 liquidity=1877381.75 spike=0.21
- EPPK.CA: score=20.36 buy_ready=False sector_rank=13 price=13.04 support=11.67 resistance=13.3 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=62.62 liquidity=3133733.67 spike=2.96
- ETEL.CA: score=14.14 buy_ready=False sector_rank=14 price=90.0 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=39.04 liquidity=26409366.0 spike=0.36
- ETRS.CA: score=19.3 buy_ready=False sector_rank=13 price=10.51 support=8.01 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=65.32 liquidity=18461098.0 spike=0.25
- EXPA.CA: score=8.91 buy_ready=False sector_rank=16 price=18.2 support=18.03 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=24.55 liquidity=10870452.0 spike=0.34
- FAIT.CA: score=0.21 buy_ready=False sector_rank=16 price=35.69 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=33.38 liquidity=1304164.63 spike=0.43
- FAITA.CA: score=3.94 buy_ready=False sector_rank=16 price=0.98 support=0.98 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:27 AM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=34107.4 spike=0.86
- FERC.CA: score=-0.45 buy_ready=False sector_rank=20 price=73.47 support=74.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=16.06 liquidity=2553882.0 spike=0.69
- FWRY.CA: score=12.82 buy_ready=False sector_rank=21 price=18.33 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=49.05 liquidity=47977992.0 spike=0.19
- GBCO.CA: score=20.48 buy_ready=False sector_rank=2 price=31.71 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=85.94 liquidity=92703000.0 spike=1.04
- GDWA.CA: score=3.01 buy_ready=False sector_rank=13 price=0.77 support=0.76 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=29.32 liquidity=4702245.0 spike=0.34
- GGCC.CA: score=18.41 buy_ready=False sector_rank=13 price=0.46 support=0.4 resistance=0.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=66.67 liquidity=8107608.5 spike=0.75
- GIHD.CA: score=10.62 buy_ready=False sector_rank=13 price=41.01 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=49.38 liquidity=4315663.0 spike=0.54
- GMCI.CA: score=13.33 buy_ready=False sector_rank=13 price=1.77 support=1.66 resistance=1.84 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=48.39 liquidity=941578.04 spike=2.54
- GRCA.CA: score=5.53 buy_ready=False sector_rank=13 price=52.04 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=39.41 liquidity=1228415.63 spike=0.28
- GSSC.CA: score=-0.3 buy_ready=False sector_rank=13 price=241.0 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=27.12 liquidity=1391225.88 spike=0.44
- GTWL.CA: score=9.3 buy_ready=False sector_rank=13 price=73.5 support=60.3 resistance=73.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=98790112.0 spike=5.3
- HDBK.CA: score=20.91 buy_ready=False sector_rank=16 price=155.07 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=63.41 liquidity=21684978.0 spike=0.79
- HELI.CA: score=17.93 buy_ready=False sector_rank=4 price=6.44 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=50.61 liquidity=24185236.0 spike=0.2
- HRHO.CA: score=15.34 buy_ready=False sector_rank=12 price=26.49 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=53.83 liquidity=34768320.0 spike=0.25
- ICID.CA: score=10.02 buy_ready=False sector_rank=13 price=7.72 support=5.0 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=73.78 liquidity=714072.38 spike=0.04
- IDRE.CA: score=8.7 buy_ready=False sector_rank=13 price=41.97 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=41.92 liquidity=4393549.5 spike=0.28
- IFAP.CA: score=8.81 buy_ready=False sector_rank=11 price=18.99 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=49.12 liquidity=3469440.5 spike=0.53
- INFI.CA: score=-0.17 buy_ready=False sector_rank=13 price=89.42 support=89.0 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=14.52 liquidity=1523105.13 spike=0.2
- IRON.CA: score=1.06 buy_ready=False sector_rank=20 price=31.28 support=30.75 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=28.36 liquidity=4061158.75 spike=0.56
- ISMA.CA: score=11.86 buy_ready=False sector_rank=13 price=28.76 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=56.23 liquidity=4558899.0 spike=0.12
- ISMQ.CA: score=20.0 buy_ready=False sector_rank=20 price=9.25 support=7.39 resistance=9.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=70.06 liquidity=108244808.0 spike=1.0
- ISPH.CA: score=8.83 buy_ready=False sector_rank=17 price=11.37 support=11.2 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=34.51 liquidity=19838028.0 spike=0.17
- JUFO.CA: score=16.64 buy_ready=False sector_rank=5 price=29.46 support=28.1 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=47.21 liquidity=8843802.0 spike=0.25
- KABO.CA: score=17.55 buy_ready=False sector_rank=9 price=6.21 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=41.43 liquidity=10333818.0 spike=0.65
- KWIN.CA: score=14.82 buy_ready=False sector_rank=13 price=68.74 support=65.75 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=43.59 liquidity=13418494.0 spike=1.26
- KZPC.CA: score=-0.64 buy_ready=False sector_rank=13 price=8.41 support=8.35 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=14.05 liquidity=1059041.13 spike=0.17
- LCSW.CA: score=21.43 buy_ready=False sector_rank=15 price=27.42 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=31276280.0 spike=1.17
- LUTS.CA: score=19.3 buy_ready=False sector_rank=13 price=0.71 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=60.35 liquidity=10441289.0 spike=0.23
- MAAL.CA: score=18.3 buy_ready=False sector_rank=13 price=7.16 support=5.24 resistance=7.54 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=78.13 liquidity=10198893.0 spike=0.57
- MASR.CA: score=5.46 buy_ready=False sector_rank=13 price=7.16 support=6.82 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=84198224.0 spike=1.58
- MBSC.CA: score=9.09 buy_ready=False sector_rank=15 price=228.81 support=228.11 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=11.36 liquidity=16897062.0 spike=0.48
- MCQE.CA: score=3.25 buy_ready=False sector_rank=15 price=168.3 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=20.75 liquidity=4163506.25 spike=0.26
- MCRO.CA: score=8.3 buy_ready=False sector_rank=13 price=1.19 support=1.18 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=25.0 liquidity=20141190.0 spike=0.56
- MENA.CA: score=12.22 buy_ready=False sector_rank=4 price=6.85 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=2287124.75 spike=0.17
- MEPA.CA: score=1.97 buy_ready=False sector_rank=13 price=1.54 support=1.52 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=17.24 liquidity=3664841.25 spike=0.31
- MFPC.CA: score=8.0 buy_ready=False sector_rank=20 price=34.59 support=34.22 resistance=43.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=5.78 liquidity=41711960.0 spike=0.49
- MFSC.CA: score=13.13 buy_ready=False sector_rank=13 price=47.25 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=54.08 liquidity=3829922.0 spike=0.43
- MHOT.CA: score=21.47 buy_ready=False sector_rank=1 price=32.74 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=61.67 liquidity=5065052.5 spike=0.22
- MICH.CA: score=11.05 buy_ready=False sector_rank=13 price=36.28 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:54 AM market time freshness=DELAYED_CURRENT RSI=43.14 liquidity=3749413.0 spike=0.25
- MILS.CA: score=6.46 buy_ready=False sector_rank=13 price=127.52 support=128.06 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:46 AM market time freshness=DELAYED_CURRENT RSI=35.55 liquidity=2159626.75 spike=0.22
- MIPH.CA: score=4.28 buy_ready=False sector_rank=17 price=642.62 support=630.13 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=38.59 liquidity=450468.13 spike=0.23
- MOED.CA: score=6.42 buy_ready=False sector_rank=13 price=0.66 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=37.68 liquidity=1111195.38 spike=0.11
- MOIL.CA: score=7.77 buy_ready=False sector_rank=7 price=0.47 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=41.51 liquidity=83033.88 spike=0.43
- MOIN.CA: score=-1.51 buy_ready=False sector_rank=13 price=23.03 support=22.6 resistance=25.66 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=1.0 liquidity=187901.78 spike=0.29
- MOSC.CA: score=6.94 buy_ready=False sector_rank=13 price=280.87 support=250.55 resistance=298.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=19606326.0 spike=2.32
- MPCI.CA: score=19.3 buy_ready=False sector_rank=13 price=233.0 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=47.85 liquidity=52442600.0 spike=0.56
- MPCO.CA: score=16.34 buy_ready=False sector_rank=11 price=1.74 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=27413322.0 spike=0.26
- MPRC.CA: score=19.3 buy_ready=False sector_rank=13 price=38.3 support=31.15 resistance=40.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=74.69 liquidity=12762607.0 spike=0.3
- MTIE.CA: score=21.82 buy_ready=False sector_rank=2 price=9.04 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=46.15 liquidity=18695766.0 spike=1.21
- NAHO.CA: score=5.31 buy_ready=False sector_rank=13 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=9515.24 spike=0.44
- NCCW.CA: score=15.43 buy_ready=False sector_rank=13 price=5.98 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=42.78 liquidity=8124008.5 spike=0.25
- NEDA.CA: score=-0.4 buy_ready=False sector_rank=13 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=33.33 liquidity=298218.86 spike=0.79
- NHPS.CA: score=4.04 buy_ready=False sector_rank=13 price=62.06 support=61.62 resistance=68.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=40.84 liquidity=731560.88 spike=0.2
- NINH.CA: score=8.17 buy_ready=False sector_rank=13 price=17.72 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=48.35 liquidity=1865843.5 spike=0.45
- NIPH.CA: score=11.83 buy_ready=False sector_rank=17 price=159.0 support=157.05 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=30.86 liquidity=36950604.0 spike=0.54
- OBRI.CA: score=12.91 buy_ready=False sector_rank=13 price=32.59 support=31.5 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=8603988.0 spike=0.62
- OCDI.CA: score=19.93 buy_ready=False sector_rank=4 price=24.51 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=70.5 liquidity=49906896.0 spike=0.67
- OCPH.CA: score=13.3 buy_ready=False sector_rank=13 price=350.1 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=36.03 liquidity=3999864.5 spike=0.68
- ODIN.CA: score=9.24 buy_ready=False sector_rank=13 price=2.08 support=1.92 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=1934042.38 spike=0.18
- OFH.CA: score=2.31 buy_ready=False sector_rank=13 price=0.58 support=0.58 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=22.89 liquidity=4009719.75 spike=0.21
- OIH.CA: score=14.92 buy_ready=False sector_rank=19 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=9274859.0 spike=0.12
- OLFI.CA: score=17.8 buy_ready=False sector_rank=5 price=21.9 support=21.1 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=49.31 liquidity=15615269.0 spike=0.78
- ORAS.CA: score=4.6 buy_ready=False sector_rank=8 price=708.02 support=695.0 resistance=718.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=171899776.0 spike=1.0
- ORHD.CA: score=19.93 buy_ready=False sector_rank=4 price=37.97 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=58.12 liquidity=81434704.0 spike=0.45
- ORWE.CA: score=9.55 buy_ready=False sector_rank=9 price=22.18 support=22.07 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=26.23 liquidity=12095383.0 spike=0.33
- PHAR.CA: score=8.41 buy_ready=False sector_rank=17 price=84.88 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=2583726.75 spike=0.08
- PHDC.CA: score=17.93 buy_ready=False sector_rank=4 price=14.79 support=14.26 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=45.18 liquidity=115466816.0 spike=0.28
- PHTV.CA: score=13.17 buy_ready=False sector_rank=13 price=266.72 support=201.55 resistance=259.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=89.5 liquidity=4865734.5 spike=0.33
- POUL.CA: score=21.8 buy_ready=False sector_rank=5 price=37.98 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=55.23 liquidity=15355625.0 spike=0.41
- PRCL.CA: score=17.62 buy_ready=False sector_rank=15 price=30.58 support=22.11 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=65.11 liquidity=8530645.0 spike=0.21
- PRDC.CA: score=19.93 buy_ready=False sector_rank=4 price=7.25 support=5.74 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=64.47 liquidity=46028508.0 spike=0.4
- PRMH.CA: score=11.42 buy_ready=False sector_rank=13 price=2.43 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=31.53 liquidity=9112681.0 spike=0.3
- RACC.CA: score=6.89 buy_ready=False sector_rank=13 price=9.57 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=37.84 liquidity=2583176.25 spike=0.27
- RAKT.CA: score=1.6 buy_ready=False sector_rank=13 price=22.43 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=30.46 liquidity=371620.25 spike=1.46
- RAYA.CA: score=17.45 buy_ready=False sector_rank=10 price=7.2 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=42.18 liquidity=41665540.0 spike=0.5
- RMDA.CA: score=8.63 buy_ready=False sector_rank=17 price=4.91 support=4.85 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=31.0 liquidity=9801613.0 spike=0.13
- ROTO.CA: score=21.3 buy_ready=False sector_rank=13 price=39.91 support=32.91 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=64.72 liquidity=16113015.0 spike=0.57
- RREI.CA: score=7.88 buy_ready=False sector_rank=13 price=3.42 support=3.34 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=38.96 liquidity=3577598.75 spike=0.2
- RTVC.CA: score=0.7 buy_ready=False sector_rank=13 price=3.66 support=3.61 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=2392459.25 spike=0.47
- RUBX.CA: score=26.22 buy_ready=False sector_rank=13 price=11.38 support=9.8 resistance=12.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=74.26 liquidity=52371984.0 spike=3.46
- SAUD.CA: score=1.87 buy_ready=False sector_rank=16 price=20.35 support=19.99 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=19.03 liquidity=2964147.5 spike=0.34
- SCEM.CA: score=8.29 buy_ready=False sector_rank=15 price=61.53 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=40.78 liquidity=4198705.5 spike=0.24
- SCFM.CA: score=0.12 buy_ready=False sector_rank=13 price=232.2 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:39 AM market time freshness=DELAYED_CURRENT RSI=20.69 liquidity=819230.56 spike=0.17
- SCTS.CA: score=0.49 buy_ready=False sector_rank=6 price=547.04 support=540.0 resistance=630.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=20.92 liquidity=693422.44 spike=0.21
- SDTI.CA: score=10.0 buy_ready=False sector_rank=13 price=46.0 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=49.61 liquidity=2691546.75 spike=0.23
- SEIG.CA: score=9.14 buy_ready=False sector_rank=13 price=184.9 support=180.0 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:56 AM market time freshness=DELAYED_CURRENT RSI=40.65 liquidity=1838495.75 spike=0.45
- SIPC.CA: score=4.44 buy_ready=False sector_rank=13 price=3.29 support=3.35 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=26.67 liquidity=5132428.5 spike=0.44
- SKPC.CA: score=7.0 buy_ready=False sector_rank=20 price=15.77 support=15.64 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=20.87 liquidity=12076794.0 spike=0.33
- SMFR.CA: score=-0.72 buy_ready=False sector_rank=13 price=189.77 support=187.01 resistance=214.0 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=27.43 liquidity=979782.53 spike=0.52
- SNFC.CA: score=6.24 buy_ready=False sector_rank=13 price=11.89 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=48.46 liquidity=1934919.5 spike=0.11
- SPIN.CA: score=12.31 buy_ready=False sector_rank=9 price=14.2 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:50 AM market time freshness=DELAYED_CURRENT RSI=57.58 liquidity=3765829.5 spike=0.62
- SPMD.CA: score=11.62 buy_ready=False sector_rank=13 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=50.68 liquidity=4318716.5 spike=0.18
- SUGR.CA: score=3.65 buy_ready=False sector_rank=5 price=46.16 support=46.25 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:55 AM market time freshness=DELAYED_CURRENT RSI=23.45 liquidity=4848679.5 spike=0.63
- SVCE.CA: score=17.3 buy_ready=False sector_rank=13 price=8.93 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=53.11 liquidity=21059934.0 spike=0.31
- SWDY.CA: score=13.82 buy_ready=False sector_rank=18 price=85.0 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=41.75 liquidity=11876906.0 spike=0.69
- TALM.CA: score=8.99 buy_ready=False sector_rank=6 price=15.78 support=15.38 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:48 AM market time freshness=DELAYED_CURRENT RSI=36.56 liquidity=1193103.25 spike=0.15
- TMGH.CA: score=14.93 buy_ready=False sector_rank=4 price=92.8 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=38.74 liquidity=115260272.0 spike=0.29
- TRTO.CA: score=5.3 buy_ready=False sector_rank=13 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=340.0 spike=0.45
- UEFM.CA: score=6.28 buy_ready=False sector_rank=13 price=467.33 support=460.0 resistance=505.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:35 AM market time freshness=DELAYED_CURRENT RSI=44.83 liquidity=972691.44 spike=0.98
- UEGC.CA: score=3.48 buy_ready=False sector_rank=13 price=1.37 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=4177707.25 spike=0.18
- UNIP.CA: score=4.88 buy_ready=False sector_rank=13 price=0.33 support=0.3 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=29331444.0 spike=1.29
- UNIT.CA: score=4.06 buy_ready=False sector_rank=4 price=12.45 support=12.5 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:49 AM market time freshness=DELAYED_CURRENT RSI=16.0 liquidity=1127049.88 spike=0.17
- WCDF.CA: score=5.13 buy_ready=False sector_rank=13 price=514.97 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-27T21:00:00+00:00 freshness=FRESH RSI=35.83 liquidity=343999.94 spike=1.24
- WKOL.CA: score=1.05 buy_ready=False sector_rank=13 price=278.7 support=273.1 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:40 AM market time freshness=DELAYED_CURRENT RSI=27.71 liquidity=1742178.88 spike=0.63
- ZEOT.CA: score=8.26 buy_ready=False sector_rank=13 price=11.12 support=10.6 resistance=11.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=78660392.0 spike=2.98
- ZMID.CA: score=21.93 buy_ready=False sector_rank=4 price=6.28 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=51.03 liquidity=88898264.0 spike=0.43

## Backtesting Lite
- RUBX.CA: 180d return=12.72%, max drawdown=-21.39%, MA20>MA50 days last20=10, as_of=2026-06-27T21:00:00+00:00
- CSAG.CA: 180d return=13.87%, max drawdown=-28.0%, MA20>MA50 days last20=20, as_of=2026-06-27T21:00:00+00:00
- ZMID.CA: 180d return=30.5%, max drawdown=-19.84%, MA20>MA50 days last20=20, as_of=2026-06-27T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- RUBX.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Rubex International for Plastic and Acrylic Manufacturing summary=Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- ZMID.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=544 sources=3 expected=Zahraa Maadi Investment and Development summary=Zahraa Maadi unveils distribution date for 2025 cash dividends; Zahraa Maadi to disburse EGP 250m dividends for 2025; Zahraa Maadi’s stock faces key resistance at EGP 5.22
  - Zahraa Maadi unveils distribution date for 2025 cash dividends: https://english.mubasher.info/news/4594804/Zahraa-Maadi-unveils-distribution-date-for-2025-cash-dividends/
  - Zahraa Maadi to disburse EGP 250m dividends for 2025: https://english.mubasher.info/news/4583591/Zahraa-Maadi-to-disburse-EGP-250m-dividends-for-2025/
  - Zahraa Maadi’s stock faces key resistance at EGP 5.22: https://english.mubasher.info/news/4563531/Zahraa-Maadi-s-stock-faces-key-resistance-at-EGP-5-22/
- MTIE.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=MM Group For Industry and International Trade summary=Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- POUL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Cairo Poultry summary=Cairo Poultry stock approaching historic peak – Analysis; Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA; Cairo Poultry sees EGP 871m block-trading deal
  - Cairo Poultry stock approaching historic peak – Analysis: https://english.mubasher.info/news/4539104/Cairo-Poultry-stock-approaching-historic-peak-Analysis/
  - Cairo Poultry cancels commercial license in Dubai&#39;s JAFZA: https://english.mubasher.info/news/3962334/Cairo-Poultry-cancels-commercial-license-in-Dubai-s-JAFZA/
  - Cairo Poultry sees EGP 871m block-trading deal: https://english.mubasher.info/news/3862165/Cairo-Poultry-sees-EGP-871m-block-trading-deal/
- MHOT.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Misr Hotels summary=Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26; Shareholder buys EGP 3.39m worth of shares in Misr Hotels; Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits
  - Misr Hotels’ net profits cross EGP 1.1bn in 9M-25/26: https://english.mubasher.info/news/4602482/Misr-Hotels-net-profits-cross-EGP-1-1bn-in-9M-25-26/
  - Shareholder buys EGP 3.39m worth of shares in Misr Hotels: https://english.mubasher.info/news/4013808/Shareholder-buys-EGP-3-39m-worth-of-shares-in-Misr-Hotels/
  - Misr Hotels repays EGP 383m of NBE&#39;s loan, unveils estimated profits: https://english.mubasher.info/news/3975543/Misr-Hotels-repays-EGP-383m-of-NBE-s-loan-unveils-estimated-profits/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=544 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/

## Warnings
- Evidence rejected for RUBX.CA: source text did not clearly match RUBX.CA / Rubex International for Plastic and Acrylic Manufacturing.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Evidence for ZMID.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for MTIE.CA: source text did not clearly match MTIE.CA / MM Group For Industry and International Trade.
- Evidence for POUL.CA matches the company but no source/report date was detected.
- Evidence for MHOT.CA matches the company but no source/report date was detected.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
