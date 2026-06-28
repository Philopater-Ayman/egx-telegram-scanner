# Telegram-First EGX Scanner Report

Scan phase: Intraday liquidity update
Generated UTC: 2026-06-28T10:26:54.356967+00:00
Generated Cairo: 2026-06-28 13:26
Run timing: target 11:00 Cairo | generated Cairo 2026-06-28 13:26 | cron 0 8 * * 0-4
Trigger: scheduled cron=0 8 * * 0-4 mapped to intraday; Cairo now 2026-06-28 13:23

## Control Center
- Action tickets: 0 prioritized signal(s)
- BUY-ready candidates: 0
- Data quality issues: 0
- Tradeable price/liquidity tickers: 185/190
- Top sector: Tourism & Leisure

## Market Context
- Market trend: Bearish
- Source: Mubasher EGX market page (delayed public data)
- As of: Sunday, June 28
- Freshness: DELAYED
- EGX30 regime: BEARISH / above MA20 15.0% / above MA50 30.0%
- EGX70 regime: BEARISH / above MA20 37.5% / above MA50 62.5%
- Sector breadth: 23.81%
- Risk mode: DEFENSIVE_NO_NEW_BUY

## Top Liquidity
- ORAS.CA: liquidity=330712672.0 spike=1.0 score=4.6
- CCAP.CA: liquidity=218181776.0 spike=0.31 score=9.79
- ISMQ.CA: liquidity=181622336.0 spike=1.85 score=5.0
- PHDC.CA: liquidity=167061888.0 spike=0.41 score=18.08
- OCDI.CA: liquidity=153088896.0 spike=2.38 score=21.84

## AI Narrative
- Provider: OpenRouter OK
- Model: openai/gpt-oss-120b:free
- Summary: The local scanner stays on HOLD because both EGX30 and EGX70 are in a bearish regime with weak breadth (≈24%). Market risk mode is DEFENSIVE_NO_NEW_BUY, so new long entries are blocked despite a few stocks showing bullish watch signals.
- EGX30/EGX70 trends are bearish; 5‑day median returns negative and only 15‑38% of stocks sit above MA20.
- Sector breadth is low; only Tourism & Leisure, Technology & Distribution and Automotive & Distribution lead, but overall support is thin.
- Top‑ranked tickets (GGCC, LCSW, CSAG, ENGC, GTWL) show bullish outlooks and liquidity spikes, yet sector is not leading and risk mode disallows new buys.
- Liquidity spikes suggest short‑term accumulation, but high RSI on LCSW, GTWL and ETRS adds uncertainty.
- Expect continued defensive stance for the next 1‑3 days; any shift will require broader market breadth improvement.

## Top Liquidity Spikes
- CSAG.CA: spike=6.55 liquidity=78420160.0 outlook=BULLISH_WATCH score=95.01 buy_ready=False
- LCSW.CA: spike=5.66 liquidity=109588320.0 outlook=BULLISH_WATCH score=76.18 buy_ready=False
- RUBX.CA: spike=5.49 liquidity=50479384.0 outlook=WEAK_OR_RISKY score=0 buy_ready=False
- GGCC.CA: spike=4.19 liquidity=36998540.0 outlook=BULLISH_WATCH score=81.67 buy_ready=False
- GTWL.CA: spike=3.18 liquidity=49874748.0 outlook=CONSTRUCTIVE score=66.67 buy_ready=False

## Sector Leaderboard
- #1 Tourism & Leisure: score=15.74 5d=16.81% 20d=14.02% aboveMA50=100.0%
- #2 Technology & Distribution: score=8.71 5d=5.56% 20d=-1.07% aboveMA50=100.0%
- #3 Automotive & Distribution: score=8.69 5d=4.46% 20d=8.94% aboveMA50=100.0%
- #4 Transportation & Logistics: score=8.01 5d=-0.42% 20d=-1.81% aboveMA50=50.0%
- #5 Non-bank Financial Services: score=3.86 5d=1.74% 20d=1.56% aboveMA50=40.0%
- #6 Healthcare: score=3.43 5d=0.35% 20d=2.16% aboveMA50=50.0%
- #7 Education: score=3.18 5d=-1.97% 20d=2.38% aboveMA50=66.67%
- #8 Real Estate: score=2.7 5d=-3.67% 20d=2.51% aboveMA50=76.92%

## Today's Prioritized Action Tickets
- HOLD: Local scanner HOLD: EGX30/EGX70 regime and sector breadth are defensive, so no new BUY is allowed.

## Thndr Instruction
- Advisor-only signal mode is active. The scanner never executes trades.
- If action is BUY or SELL, verify current price, liquidity, and spread manually in Thndr.
- Choose position size yourself. This system no longer tracks account balances or holdings in the daily flow.

## Top 1-3 Day Outlook
- CSAG.CA: BULLISH_WATCH score=95.01 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=No major short-term scanner risk flags.
- RAYA.CA: BULLISH_WATCH score=94.71 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling
- GGCC.CA: BULLISH_WATCH score=81.67 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- CNFN.CA: BULLISH_WATCH score=79.86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ATLC.CA: BULLISH_WATCH score=79.86 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- CIRA.CA: BULLISH_WATCH score=79.18 liquidity=TRADEABLE sector=IMPROVING risk=liquidity is cooling
- ENGC.CA: BULLISH_WATCH score=78.67 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=sector is not leading
- EPPK.CA: BULLISH_WATCH score=78.67 liquidity=TRADEABLE sector=IMPROVING risk=momentum is extended; sector is not leading
- MTIE.CA: BULLISH_WATCH score=76.69 liquidity=TRADEABLE sector=LEADING risk=liquidity is cooling; below MA20
- LCSW.CA: BULLISH_WATCH score=76.18 liquidity=ACCUMULATION_SPIKE sector=IMPROVING risk=overheated RSI; sector is not leading

## BUY-Ready Candidates
- No BUY-ready candidates. Review block reasons and institution-flow status.

## Data Quality Issues
- No provider failures.

## Ranked Scanner Results
- AALR.CA: score=9.19 buy_ready=False sector_rank=9 price=197.58 support=200.0 resistance=231.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=41.38 liquidity=4122590.25 spike=0.72
- ABUK.CA: score=8.3 buy_ready=False sector_rank=21 price=68.66 support=68.01 resistance=86.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=12.55 liquidity=34497132.0 spike=0.26
- ACAMD.CA: score=18.07 buy_ready=False sector_rank=9 price=2.22 support=2.17 resistance=2.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=36.21 liquidity=14774747.0 spike=0.12
- ACGC.CA: score=15.36 buy_ready=False sector_rank=16 price=9.33 support=9.11 resistance=10.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=37.16 liquidity=7579712.0 spike=0.14
- ADCI.CA: score=9.89 buy_ready=False sector_rank=9 price=235.01 support=211.0 resistance=244.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=85.03 liquidity=2820449.0 spike=0.31
- ADIB.CA: score=14.66 buy_ready=False sector_rank=17 price=44.64 support=44.01 resistance=48.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=39.2 liquidity=17771188.0 spike=0.18
- ADPC.CA: score=11.18 buy_ready=False sector_rank=9 price=3.46 support=3.43 resistance=3.94 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=38.89 liquidity=7113752.5 spike=0.31
- AFDI.CA: score=15.36 buy_ready=False sector_rank=9 price=44.02 support=40.15 resistance=48.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=50.15 liquidity=3296500.0 spike=0.22
- AFMC.CA: score=0.59 buy_ready=False sector_rank=9 price=68.25 support=67.0 resistance=74.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=33.54 liquidity=526913.56 spike=0.17
- AJWA.CA: score=10.26 buy_ready=False sector_rank=9 price=175.05 support=131.5 resistance=188.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=82.78 liquidity=3195664.75 spike=0.12
- ALCN.CA: score=11.4 buy_ready=False sector_rank=4 price=28.15 support=25.51 resistance=33.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=31.15 liquidity=10344965.0 spike=0.84
- ALUM.CA: score=3.07 buy_ready=False sector_rank=9 price=21.01 support=21.5 resistance=26.44 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=17.63 liquidity=3005897.75 spike=0.3
- AMER.CA: score=10.08 buy_ready=False sector_rank=8 price=2.34 support=2.35 resistance=3.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=33.33 liquidity=12365999.0 spike=0.16
- AMES.CA: score=0.42 buy_ready=False sector_rank=9 price=46.3 support=48.0 resistance=53.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=32.52 liquidity=1351167.63 spike=0.43
- AMIA.CA: score=11.09 buy_ready=False sector_rank=9 price=8.68 support=8.4 resistance=9.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=40.15 liquidity=3025943.25 spike=0.22
- AMOC.CA: score=9.9 buy_ready=False sector_rank=12 price=7.55 support=7.53 resistance=8.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=21.9 liquidity=12825359.0 spike=0.25
- ANFI.CA: score=15.4 buy_ready=False sector_rank=9 price=26.5 support=13.73 resistance=41.4 source=Yahoo Finance as_of=2026-06-22T21:00:00+00:00 freshness=FRESH RSI=64.45 liquidity=3331182.5 spike=0.04
- APSW.CA: score=-0.5 buy_ready=False sector_rank=9 price=8.46 support=8.24 resistance=9.21 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:53 AM market time freshness=DELAYED_CURRENT RSI=13.11 liquidity=433357.34 spike=0.54
- ARAB.CA: score=15.08 buy_ready=False sector_rank=8 price=0.21 support=0.2 resistance=0.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=47.06 liquidity=50075976.0 spike=0.59
- ARCC.CA: score=9.87 buy_ready=False sector_rank=13 price=55.18 support=53.0 resistance=60.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=31.64 liquidity=13966390.0 spike=0.41
- AREH.CA: score=22.07 buy_ready=False sector_rank=9 price=1.57 support=1.32 resistance=1.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=60.38 liquidity=15241874.0 spike=0.45
- ARVA.CA: score=15.69 buy_ready=False sector_rank=9 price=11.12 support=8.08 resistance=13.1 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=52.31 liquidity=5626942.0 spike=0.17
- ASCM.CA: score=22.07 buy_ready=False sector_rank=9 price=59.33 support=47.49 resistance=73.73 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=61.62 liquidity=30360194.0 spike=0.33
- ASPI.CA: score=13.07 buy_ready=False sector_rank=9 price=0.31 support=0.26 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=34.53 liquidity=14034854.0 spike=0.2
- ATLC.CA: score=14.38 buy_ready=False sector_rank=5 price=5.12 support=4.7 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=58.06 liquidity=1831917.13 spike=0.29
- ATQA.CA: score=14.66 buy_ready=False sector_rank=21 price=9.69 support=9.02 resistance=10.26 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=40.18 liquidity=37565204.0 spike=1.18
- AXPH.CA: score=8.46 buy_ready=False sector_rank=9 price=1096.07 support=1073.0 resistance=1174.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=40.71 liquidity=387695.38 spike=0.26
- BINV.CA: score=11.52 buy_ready=False sector_rank=15 price=47.11 support=42.97 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=60.78 liquidity=1734637.25 spike=0.17
- BIOC.CA: score=-2.48 buy_ready=False sector_rank=9 price=67.6 support=67.5 resistance=72.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=2408965.5 spike=1.02
- BTFH.CA: score=14.54 buy_ready=False sector_rank=5 price=2.99 support=2.96 resistance=3.23 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=47.83 liquidity=89590568.0 spike=0.45
- CAED.CA: score=9.41 buy_ready=False sector_rank=9 price=69.98 support=67.21 resistance=78.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=48.33 liquidity=1338250.88 spike=0.26
- CANA.CA: score=9.14 buy_ready=False sector_rank=17 price=35.01 support=34.5 resistance=39.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=41.16 liquidity=5478001.5 spike=0.52
- CCAP.CA: score=9.79 buy_ready=False sector_rank=15 price=4.88 support=4.85 resistance=5.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=17.46 liquidity=218181776.0 spike=0.31
- CCRS.CA: score=8.14 buy_ready=False sector_rank=9 price=2.33 support=2.32 resistance=2.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=31.75 liquidity=5069026.0 spike=0.28
- CEFM.CA: score=0.94 buy_ready=False sector_rank=9 price=99.9 support=100.0 resistance=109.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:08 AM market time freshness=DELAYED_CURRENT RSI=23.51 liquidity=873489.56 spike=0.42
- CERA.CA: score=20.1 buy_ready=False sector_rank=9 price=1.23 support=1.15 resistance=1.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=61.54 liquidity=9027936.0 spike=0.54
- CFGH.CA: score=0.1 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance history + Mubasher delayed current trading data as_of=10:26 AM market time freshness=DELAYED_CURRENT RSI=0.0 liquidity=10054.09 spike=1.51
- CICH.CA: score=9.98 buy_ready=False sector_rank=5 price=11.8 support=11.1 resistance=13.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=46.48 liquidity=2434682.0 spike=0.8
- CIEB.CA: score=9.15 buy_ready=False sector_rank=17 price=23.66 support=23.27 resistance=24.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=58.19 liquidity=2483857.0 spike=0.38
- CIRA.CA: score=22.27 buy_ready=False sector_rank=7 price=27.83 support=25.23 resistance=31.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=59.81 liquidity=13811793.0 spike=0.79
- CLHO.CA: score=18.69 buy_ready=False sector_rank=6 price=16.41 support=14.25 resistance=17.39 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=63.34 liquidity=6320892.5 spike=0.18
- CNFN.CA: score=22.54 buy_ready=False sector_rank=5 price=4.75 support=4.36 resistance=5.28 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=60.4 liquidity=11986714.0 spike=0.3
- COMI.CA: score=14.66 buy_ready=False sector_rank=17 price=130.64 support=129.8 resistance=137.07 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=50.27 liquidity=141107840.0 spike=0.24
- COPR.CA: score=13.68 buy_ready=False sector_rank=9 price=0.36 support=0.35 resistance=0.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=50.85 liquidity=6615314.5 spike=0.19
- COSG.CA: score=10.07 buy_ready=False sector_rank=9 price=1.5 support=1.52 resistance=1.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=32.35 liquidity=10829314.0 spike=0.2
- CPCI.CA: score=12.56 buy_ready=False sector_rank=9 price=372.09 support=347.11 resistance=378.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=72.05 liquidity=493604.41 spike=0.25
- CSAG.CA: score=26.4 buy_ready=False sector_rank=4 price=33.09 support=30.08 resistance=32.47 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=49.89 liquidity=78420160.0 spike=6.55
- DAPH.CA: score=17.12 buy_ready=False sector_rank=9 price=80.93 support=76.6 resistance=87.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=54.9 liquidity=6056835.0 spike=0.58
- DEIN.CA: score=6.07 buy_ready=False sector_rank=9 price=11.38 support=11.38 resistance=13.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=25 June 12:11 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=40.95 spike=0.01
- DOMT.CA: score=11.76 buy_ready=False sector_rank=10 price=26.79 support=23.7 resistance=27.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=73.9 liquidity=1757900.13 spike=0.46
- DSCW.CA: score=14.07 buy_ready=False sector_rank=9 price=1.74 support=1.74 resistance=1.88 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=17803212.0 spike=0.39
- DTPP.CA: score=1.06 buy_ready=False sector_rank=9 price=116.0 support=114.0 resistance=130.89 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=19.44 liquidity=990292.0 spike=0.87
- EALR.CA: score=7.28 buy_ready=False sector_rank=9 price=340.21 support=350.0 resistance=380.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=44.67 liquidity=2210166.5 spike=0.69
- EASB.CA: score=5.73 buy_ready=False sector_rank=9 price=7.67 support=7.5 resistance=8.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=14511653.0 spike=1.33
- EAST.CA: score=14.0 buy_ready=False sector_rank=10 price=37.38 support=37.01 resistance=40.59 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=47.42 liquidity=10690704.0 spike=0.24
- EBSC.CA: score=5.44 buy_ready=False sector_rank=9 price=1.77 support=1.66 resistance=2.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:45 AM market time freshness=DELAYED_CURRENT RSI=35.29 liquidity=372548.78 spike=0.14
- ECAP.CA: score=20.89 buy_ready=False sector_rank=9 price=32.99 support=29.8 resistance=34.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=69.97 liquidity=11610976.0 spike=1.41
- EDFM.CA: score=0.45 buy_ready=False sector_rank=9 price=330.59 support=322.11 resistance=355.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=26.96 liquidity=384806.76 spike=0.73
- EEII.CA: score=15.9 buy_ready=False sector_rank=9 price=2.41 support=2.3 resistance=2.55 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=53.45 liquidity=5830394.5 spike=0.42
- EFIC.CA: score=-1.74 buy_ready=False sector_rank=21 price=193.91 support=192.01 resistance=213.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=15.79 liquidity=954246.25 spike=0.5
- EFID.CA: score=10.0 buy_ready=False sector_rank=10 price=26.03 support=26.67 resistance=29.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=27.31 liquidity=36708676.0 spike=0.51
- EFIH.CA: score=9.52 buy_ready=False sector_rank=20 price=20.57 support=20.09 resistance=22.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=41.24 liquidity=6171747.5 spike=0.13
- EGAL.CA: score=8.3 buy_ready=False sector_rank=21 price=278.45 support=280.0 resistance=334.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=10.2 liquidity=17698532.0 spike=0.24
- EGAS.CA: score=11.58 buy_ready=False sector_rank=12 price=48.38 support=48.2 resistance=55.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=42.15 liquidity=3679013.75 spike=0.37
- EGBE.CA: score=9.72 buy_ready=False sector_rank=17 price=0.46 support=0.43 resistance=0.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=65.52 liquidity=56758.92 spike=0.64
- EGCH.CA: score=7.59 buy_ready=False sector_rank=21 price=12.67 support=12.69 resistance=15.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=28.76 liquidity=9283747.0 spike=0.16
- EGSA.CA: score=4.89 buy_ready=False sector_rank=11 price=8.75 support=8.55 resistance=9.1 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=31.03 liquidity=17500.0 spike=1.95
- EGTS.CA: score=15.08 buy_ready=False sector_rank=8 price=16.3 support=16.7 resistance=22.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=46.38 liquidity=36991020.0 spike=0.38
- EHDR.CA: score=18.07 buy_ready=False sector_rank=9 price=2.46 support=2.25 resistance=2.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=44.05 liquidity=16705810.0 spike=0.29
- EKHO.CA: score=9.9 buy_ready=False sector_rank=12 price=0.67 support=0.67 resistance=0.67 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=0.0 spike=0.0
- ELEC.CA: score=6.83 buy_ready=False sector_rank=19 price=2.09 support=2.06 resistance=2.2 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=36.67 liquidity=3690895.25 spike=0.18
- ELKA.CA: score=12.04 buy_ready=False sector_rank=9 price=1.23 support=1.15 resistance=1.37 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=4967791.5 spike=0.12
- ELNA.CA: score=0.84 buy_ready=False sector_rank=9 price=36.1 support=36.0 resistance=41.51 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=33.65 liquidity=636226.37 spike=1.57
- ELSH.CA: score=18.07 buy_ready=False sector_rank=9 price=11.3 support=8.28 resistance=14.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=52.69 liquidity=19978676.0 spike=0.11
- ELWA.CA: score=8.57 buy_ready=False sector_rank=9 price=2.03 support=2.0 resistance=2.22 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:51 AM market time freshness=DELAYED_CURRENT RSI=50.98 liquidity=504317.78 spike=0.15
- EMFD.CA: score=18.08 buy_ready=False sector_rank=8 price=11.49 support=10.5 resistance=12.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=43.95 liquidity=28884096.0 spike=0.1
- ENGC.CA: score=24.05 buy_ready=False sector_rank=9 price=37.18 support=32.81 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=59.63 liquidity=25736008.0 spike=1.99
- EOSB.CA: score=12.12 buy_ready=False sector_rank=9 price=1.48 support=1.35 resistance=1.55 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=50716.64 spike=0.39
- EPCO.CA: score=6.48 buy_ready=False sector_rank=9 price=8.81 support=8.89 resistance=9.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=40.24 liquidity=1410051.63 spike=0.15
- EPPK.CA: score=15.8 buy_ready=False sector_rank=9 price=13.28 support=11.67 resistance=13.12 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:57 AM market time freshness=DELAYED_CURRENT RSI=67.48 liquidity=1873255.38 spike=1.93
- ETEL.CA: score=16.98 buy_ready=False sector_rank=11 price=92.2 support=89.61 resistance=98.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=46.73 liquidity=20697156.0 spike=0.27
- ETRS.CA: score=22.99 buy_ready=False sector_rank=9 price=10.91 support=7.93 resistance=11.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=70.92 liquidity=99794656.0 spike=1.46
- EXPA.CA: score=9.66 buy_ready=False sector_rank=17 price=18.21 support=18.2 resistance=20.09 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=18.55 liquidity=15290780.0 spike=0.47
- FAIT.CA: score=5.67 buy_ready=False sector_rank=17 price=35.65 support=35.01 resistance=38.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=38.43 liquidity=1006385.56 spike=0.32
- FAITA.CA: score=7.7 buy_ready=False sector_rank=17 price=0.99 support=0.99 resistance=1.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=56.0 liquidity=32465.93 spike=0.91
- FERC.CA: score=1.02 buy_ready=False sector_rank=21 price=75.07 support=75.0 resistance=80.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=23.06 liquidity=1713204.13 spike=0.45
- FWRY.CA: score=15.34 buy_ready=False sector_rank=20 price=18.53 support=17.71 resistance=20.61 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=50.0 liquidity=44013792.0 spike=0.17
- GBCO.CA: score=21.4 buy_ready=False sector_rank=3 price=30.51 support=25.25 resistance=31.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=94.21 liquidity=42634404.0 spike=0.47
- GDWA.CA: score=2.0 buy_ready=False sector_rank=9 price=0.78 support=0.77 resistance=0.83 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=30.95 liquidity=2928651.0 spike=0.21
- GGCC.CA: score=28.07 buy_ready=False sector_rank=9 price=0.46 support=0.4 resistance=0.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=52.38 liquidity=36998540.0 spike=4.19
- GIHD.CA: score=17.2 buy_ready=False sector_rank=9 price=41.76 support=35.15 resistance=47.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=58.27 liquidity=5135728.0 spike=0.66
- GMCI.CA: score=12.37 buy_ready=False sector_rank=9 price=1.79 support=1.66 resistance=1.84 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=36.0 liquidity=700972.94 spike=1.8
- GRCA.CA: score=6.56 buy_ready=False sector_rank=9 price=52.04 support=50.2 resistance=60.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:01 PM market time freshness=DELAYED_CURRENT RSI=39.48 liquidity=1493351.63 spike=0.32
- GSSC.CA: score=5.75 buy_ready=False sector_rank=9 price=245.76 support=228.1 resistance=257.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=39.18 liquidity=677577.06 spike=0.21
- GTWL.CA: score=23.43 buy_ready=False sector_rank=9 price=60.5 support=45.47 resistance=68.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=86.73 liquidity=49874748.0 spike=3.18
- HDBK.CA: score=16.66 buy_ready=False sector_rank=17 price=158.8 support=138.0 resistance=172.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=80.29 liquidity=18822076.0 spike=0.72
- HELI.CA: score=18.08 buy_ready=False sector_rank=8 price=6.43 support=6.28 resistance=6.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=52.53 liquidity=26603830.0 spike=0.2
- HRHO.CA: score=16.54 buy_ready=False sector_rank=5 price=26.8 support=25.54 resistance=27.66 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=57.49 liquidity=36049408.0 spike=0.25
- ICID.CA: score=14.45 buy_ready=False sector_rank=9 price=7.73 support=5.0 resistance=8.05 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:00 PM market time freshness=DELAYED_CURRENT RSI=80.91 liquidity=5385346.0 spike=0.33
- IDRE.CA: score=11.72 buy_ready=False sector_rank=9 price=43.08 support=42.01 resistance=47.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=43.82 liquidity=3647087.25 spike=0.23
- IFAP.CA: score=6.95 buy_ready=False sector_rank=14 price=19.21 support=16.5 resistance=23.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=44.94 liquidity=3146199.5 spike=0.48
- INFI.CA: score=2.25 buy_ready=False sector_rank=9 price=90.22 support=92.5 resistance=105.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=18.57 liquidity=3181521.25 spike=0.41
- IRON.CA: score=5.23 buy_ready=False sector_rank=21 price=31.16 support=30.95 resistance=34.15 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=35.08 liquidity=2927465.25 spike=0.4
- ISMA.CA: score=20.07 buy_ready=False sector_rank=9 price=29.35 support=25.95 resistance=36.45 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=15246315.0 spike=0.4
- ISMQ.CA: score=5.0 buy_ready=False sector_rank=21 price=9.15 support=8.6 resistance=9.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=181622336.0 spike=1.85
- ISPH.CA: score=15.37 buy_ready=False sector_rank=6 price=11.46 support=11.3 resistance=12.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=39.94 liquidity=79327232.0 spike=0.7
- JUFO.CA: score=17.41 buy_ready=False sector_rank=10 price=30.02 support=28.09 resistance=32.17 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=58.37 liquidity=9405722.0 spike=0.27
- KABO.CA: score=18.06 buy_ready=False sector_rank=16 price=6.27 support=5.96 resistance=6.56 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=38.16 liquidity=19618538.0 spike=1.14
- KWIN.CA: score=17.03 buy_ready=False sector_rank=9 price=69.55 support=65.75 resistance=79.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=44.26 liquidity=19054918.0 spike=1.98
- KZPC.CA: score=-0.07 buy_ready=False sector_rank=9 price=8.56 support=8.6 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=14.44 liquidity=861507.69 spike=0.13
- LCSW.CA: score=26.87 buy_ready=False sector_rank=13 price=28.91 support=26.0 resistance=31.33 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=70.94 liquidity=109588320.0 spike=5.66
- LUTS.CA: score=22.07 buy_ready=False sector_rank=9 price=0.7 support=0.55 resistance=0.79 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=61.21 liquidity=14841016.0 spike=0.34
- MAAL.CA: score=20.87 buy_ready=False sector_rank=9 price=7.11 support=5.16 resistance=7.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=78.24 liquidity=31065544.0 spike=1.9
- MASR.CA: score=18.07 buy_ready=False sector_rank=9 price=6.87 support=6.54 resistance=7.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=56.89 liquidity=16010674.0 spike=0.29
- MBSC.CA: score=9.87 buy_ready=False sector_rank=13 price=232.0 support=242.0 resistance=258.91 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=34.9 liquidity=20461696.0 spike=0.56
- MCQE.CA: score=7.15 buy_ready=False sector_rank=13 price=170.48 support=166.66 resistance=200.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=17.86 liquidity=7279319.5 spike=0.45
- MCRO.CA: score=9.07 buy_ready=False sector_rank=9 price=1.19 support=1.2 resistance=1.31 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=28.57 liquidity=14407655.0 spike=0.38
- MENA.CA: score=8.66 buy_ready=False sector_rank=8 price=6.71 support=6.22 resistance=7.75 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:02 PM market time freshness=DELAYED_CURRENT RSI=49.28 liquidity=577676.25 spike=0.04
- MEPA.CA: score=4.47 buy_ready=False sector_rank=9 price=1.54 support=1.58 resistance=1.78 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=20.0 liquidity=5399313.0 spike=0.45
- MFPC.CA: score=8.3 buy_ready=False sector_rank=21 price=34.57 support=35.15 resistance=44.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=8.54 liquidity=47650624.0 spike=0.56
- MFSC.CA: score=19.25 buy_ready=False sector_rank=9 price=49.87 support=43.0 resistance=56.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=56.14 liquidity=7185558.5 spike=0.79
- MHOT.CA: score=18.28 buy_ready=False sector_rank=1 price=33.98 support=28.83 resistance=38.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=73.12 liquidity=3882385.5 spike=0.14
- MICH.CA: score=14.65 buy_ready=False sector_rank=9 price=36.92 support=35.4 resistance=40.4 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=54.58 liquidity=4578259.5 spike=0.3
- MILS.CA: score=7.16 buy_ready=False sector_rank=9 price=128.45 support=130.11 resistance=151.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=36.62 liquidity=2089098.88 spike=0.18
- MIPH.CA: score=6.13 buy_ready=False sector_rank=6 price=638.18 support=640.0 resistance=710.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=46.16 liquidity=754536.56 spike=0.35
- MOED.CA: score=8.5 buy_ready=False sector_rank=9 price=0.67 support=0.65 resistance=0.72 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=2435656.0 spike=0.24
- MOIL.CA: score=8.06 buy_ready=False sector_rank=12 price=0.48 support=0.46 resistance=0.49 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=60.87 liquidity=158958.14 spike=0.88
- MOIN.CA: score=-0.4 buy_ready=False sector_rank=9 price=23.03 support=22.61 resistance=25.66 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=0.97 liquidity=535194.19 spike=0.85
- MOSC.CA: score=7.61 buy_ready=False sector_rank=9 price=254.35 support=246.6 resistance=330.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=46.6 liquidity=2546938.0 spike=0.3
- MPCI.CA: score=22.07 buy_ready=False sector_rank=9 price=229.79 support=204.36 resistance=256.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=60.69 liquidity=42808136.0 spike=0.45
- MPCO.CA: score=17.81 buy_ready=False sector_rank=14 price=1.8 support=1.58 resistance=2.04 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=54.84 liquidity=18594416.0 spike=0.18
- MPRC.CA: score=21.01 buy_ready=False sector_rank=9 price=38.78 support=31.1 resistance=38.41 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=75.37 liquidity=74975504.0 spike=1.97
- MTIE.CA: score=16.03 buy_ready=False sector_rank=3 price=8.94 support=8.65 resistance=9.6 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=51.52 liquidity=5633114.5 spike=0.35
- NAHO.CA: score=6.37 buy_ready=False sector_rank=9 price=0.1 support=0.1 resistance=0.11 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=60.0 liquidity=24189.78 spike=1.14
- NCCW.CA: score=15.61 buy_ready=False sector_rank=9 price=6.12 support=5.29 resistance=6.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=7546197.5 spike=0.23
- NEDA.CA: score=0.19 buy_ready=False sector_rank=9 price=2.74 support=2.68 resistance=2.84 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=28.57 liquidity=117806.3 spike=0.32
- NHPS.CA: score=5.63 buy_ready=False sector_rank=9 price=63.03 support=61.62 resistance=68.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=45.83 liquidity=1558422.5 spike=0.39
- NINH.CA: score=15.89 buy_ready=False sector_rank=9 price=17.8 support=16.8 resistance=18.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=49.07 liquidity=5945268.5 spike=1.44
- NIPH.CA: score=13.37 buy_ready=False sector_rank=6 price=159.3 support=157.1 resistance=176.9 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=32.48 liquidity=20104160.0 spike=0.29
- OBRI.CA: score=9.03 buy_ready=False sector_rank=9 price=32.56 support=33.55 resistance=37.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:59 AM market time freshness=DELAYED_CURRENT RSI=45.44 liquidity=3961986.5 spike=0.29
- OCDI.CA: score=21.84 buy_ready=False sector_rank=8 price=24.6 support=20.0 resistance=25.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=76.51 liquidity=153088896.0 spike=2.38
- OCPH.CA: score=7.0 buy_ready=False sector_rank=9 price=341.85 support=337.0 resistance=377.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:52 AM market time freshness=DELAYED_CURRENT RSI=36.11 liquidity=1929826.5 spike=0.32
- ODIN.CA: score=12.4 buy_ready=False sector_rank=9 price=2.08 support=1.91 resistance=2.25 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=51.67 liquidity=4331174.5 spike=0.4
- OFH.CA: score=3.74 buy_ready=False sector_rank=9 price=0.59 support=0.59 resistance=0.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=24.36 liquidity=4672457.5 spike=0.24
- OIH.CA: score=16.79 buy_ready=False sector_rank=15 price=1.4 support=1.33 resistance=1.51 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=58.62 liquidity=15115397.0 spike=0.18
- OLFI.CA: score=11.35 buy_ready=False sector_rank=10 price=21.47 support=21.39 resistance=23.08 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=51.8 liquidity=6345707.5 spike=0.32
- ORAS.CA: score=4.6 buy_ready=False sector_rank=18 price=694.94 support=680.0 resistance=732.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=330712672.0 spike=1.0
- ORHD.CA: score=20.08 buy_ready=False sector_rank=8 price=38.54 support=35.01 resistance=39.68 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=60.63 liquidity=136296000.0 spike=0.77
- ORWE.CA: score=9.78 buy_ready=False sector_rank=16 price=22.33 support=22.61 resistance=24.3 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=31.25 liquidity=16099514.0 spike=0.43
- PHAR.CA: score=14.41 buy_ready=False sector_rank=6 price=87.0 support=83.02 resistance=89.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=59.17 liquidity=2040086.75 spike=0.06
- PHDC.CA: score=18.08 buy_ready=False sector_rank=8 price=14.7 support=14.43 resistance=16.43 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=54.93 liquidity=167061888.0 spike=0.41
- PHTV.CA: score=15.88 buy_ready=False sector_rank=9 price=257.0 support=201.55 resistance=256.89 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=85.23 liquidity=8810182.0 spike=0.44
- POUL.CA: score=22.0 buy_ready=False sector_rank=10 price=38.31 support=34.99 resistance=41.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=55.39 liquidity=15371538.0 spike=0.41
- PRCL.CA: score=19.87 buy_ready=False sector_rank=13 price=30.45 support=22.02 resistance=32.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=67.99 liquidity=22957360.0 spike=0.58
- PRDC.CA: score=20.08 buy_ready=False sector_rank=8 price=7.02 support=5.7 resistance=9.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=63.47 liquidity=31340170.0 spike=0.27
- PRMH.CA: score=18.07 buy_ready=False sector_rank=9 price=2.49 support=2.26 resistance=3.02 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=38.0 liquidity=11735188.0 spike=0.39
- RACC.CA: score=8.17 buy_ready=False sector_rank=9 price=9.76 support=9.38 resistance=10.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=43.75 liquidity=3105732.75 spike=0.32
- RAKT.CA: score=6.14 buy_ready=False sector_rank=9 price=23.11 support=22.0 resistance=24.1 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=37.86 liquidity=67226.99 spike=0.28
- RAYA.CA: score=23.4 buy_ready=False sector_rank=2 price=7.33 support=6.7 resistance=7.81 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=42.38 liquidity=41267168.0 spike=0.47
- RMDA.CA: score=15.37 buy_ready=False sector_rank=6 price=4.9 support=4.92 resistance=5.38 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=39.39 liquidity=14684845.0 spike=0.19
- ROTO.CA: score=19.49 buy_ready=False sector_rank=9 price=39.52 support=32.76 resistance=47.64 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=73.14 liquidity=9420960.0 spike=0.34
- RREI.CA: score=6.99 buy_ready=False sector_rank=9 price=3.42 support=3.35 resistance=3.85 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=40.54 liquidity=1920518.13 spike=0.1
- RTVC.CA: score=5.31 buy_ready=False sector_rank=9 price=3.64 support=3.63 resistance=4.14 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:03 PM market time freshness=DELAYED_CURRENT RSI=40.86 liquidity=1238424.5 spike=0.24
- RUBX.CA: score=10.07 buy_ready=False sector_rank=9 price=11.3 support=10.55 resistance=11.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT_UNALIGNED RSI=50.0 liquidity=50479384.0 spike=5.49
- SAUD.CA: score=2.46 buy_ready=False sector_rank=17 price=20.9 support=20.82 resistance=23.27 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=25.28 liquidity=2796061.0 spike=0.31
- SCEM.CA: score=10.76 buy_ready=False sector_rank=13 price=61.9 support=59.3 resistance=67.46 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:04 PM market time freshness=DELAYED_CURRENT RSI=42.29 liquidity=5887335.0 spike=0.31
- SCFM.CA: score=1.48 buy_ready=False sector_rank=9 price=234.94 support=226.5 resistance=276.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=20.9 liquidity=1408101.13 spike=0.23
- SCTS.CA: score=1.45 buy_ready=False sector_rank=7 price=553.64 support=552.8 resistance=630.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=29.99 liquidity=1176600.25 spike=0.33
- SDTI.CA: score=11.34 buy_ready=False sector_rank=9 price=46.71 support=44.03 resistance=49.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=59.39 liquidity=1271578.13 spike=0.11
- SEIG.CA: score=9.14 buy_ready=False sector_rank=9 price=183.8 support=179.43 resistance=205.7 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=42.41 liquidity=1072421.63 spike=0.26
- SIPC.CA: score=6.33 buy_ready=False sector_rank=9 price=3.39 support=3.4 resistance=3.74 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=29.09 liquidity=6264669.5 spike=0.54
- SKPC.CA: score=7.3 buy_ready=False sector_rank=21 price=15.86 support=15.9 resistance=17.5 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=31.8 liquidity=14813150.0 spike=0.39
- SMFR.CA: score=0.54 buy_ready=False sector_rank=9 price=195.1 support=192.0 resistance=214.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:05 PM market time freshness=DELAYED_CURRENT RSI=31.3 liquidity=471701.16 spike=0.2
- SNFC.CA: score=9.85 buy_ready=False sector_rank=9 price=12.0 support=11.68 resistance=12.99 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=68.84 liquidity=3786522.25 spike=0.19
- SPIN.CA: score=10.18 buy_ready=False sector_rank=16 price=14.03 support=13.3 resistance=14.65 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=45.63 liquidity=5398660.5 spike=0.95
- SPMD.CA: score=13.65 buy_ready=False sector_rank=9 price=0.42 support=0.4 resistance=0.48 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=49.01 liquidity=5580567.0 spike=0.23
- SUGR.CA: score=3.2 buy_ready=False sector_rank=10 price=46.64 support=47.03 resistance=51.29 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:09 PM market time freshness=DELAYED_CURRENT RSI=23.54 liquidity=4200194.0 spike=0.51
- SVCE.CA: score=20.07 buy_ready=False sector_rank=9 price=8.96 support=8.11 resistance=9.87 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=54.92 liquidity=20461542.0 spike=0.29
- SWDY.CA: score=14.14 buy_ready=False sector_rank=19 price=85.75 support=84.01 resistance=90.97 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=44.21 liquidity=11384502.0 spike=0.66
- TALM.CA: score=10.07 buy_ready=False sector_rank=7 price=15.92 support=15.5 resistance=16.53 source=Yahoo Finance history + Mubasher delayed current trading data as_of=11:58 AM market time freshness=DELAYED_CURRENT RSI=52.7 liquidity=1795729.25 spike=0.22
- TMGH.CA: score=18.08 buy_ready=False sector_rank=8 price=95.42 support=92.91 resistance=98.98 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:07 PM market time freshness=DELAYED_CURRENT RSI=54.96 liquidity=126894456.0 spike=0.29
- TRTO.CA: score=6.07 buy_ready=False sector_rank=9 price=0.03 support=0.03 resistance=0.04 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=50.0 liquidity=491.27 spike=0.67
- UEFM.CA: score=10.43 buy_ready=False sector_rank=9 price=486.78 support=465.01 resistance=505.0 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=62.58 liquidity=998385.78 spike=1.18
- UEGC.CA: score=5.68 buy_ready=False sector_rank=9 price=1.38 support=1.32 resistance=1.58 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=34.37 liquidity=5614381.5 spike=0.24
- UNIP.CA: score=12.49 buy_ready=False sector_rank=9 price=0.31 support=0.28 resistance=0.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:11 PM market time freshness=DELAYED_CURRENT RSI=40.0 liquidity=4421947.0 spike=0.19
- UNIT.CA: score=3.63 buy_ready=False sector_rank=8 price=12.74 support=12.91 resistance=15.8 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=33.47 liquidity=548255.56 spike=0.08
- WCDF.CA: score=5.25 buy_ready=False sector_rank=9 price=531.95 support=450.0 resistance=547.9 source=Yahoo Finance as_of=2026-06-24T21:00:00+00:00 freshness=FRESH RSI=43.92 liquidity=179267.15 spike=0.69
- WKOL.CA: score=0.99 buy_ready=False sector_rank=9 price=277.85 support=284.0 resistance=312.0 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:06 PM market time freshness=DELAYED_CURRENT RSI=34.43 liquidity=920742.25 spike=0.32
- ZEOT.CA: score=20.07 buy_ready=False sector_rank=9 price=10.76 support=8.41 resistance=12.35 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:10 PM market time freshness=DELAYED_CURRENT RSI=67.52 liquidity=21511014.0 spike=0.85
- ZMID.CA: score=22.08 buy_ready=False sector_rank=8 price=6.38 support=5.82 resistance=6.69 source=Yahoo Finance history + Mubasher delayed current trading data as_of=12:08 PM market time freshness=DELAYED_CURRENT RSI=62.07 liquidity=108663640.0 spike=0.52

## Backtesting Lite
- GGCC.CA: 180d return=-16.12%, max drawdown=-45.58%, MA20>MA50 days last20=19, as_of=2026-06-24T21:00:00+00:00
- LCSW.CA: 180d return=14.22%, max drawdown=-15.87%, MA20>MA50 days last20=20, as_of=2026-06-24T21:00:00+00:00
- CSAG.CA: 180d return=18.29%, max drawdown=-28.0%, MA20>MA50 days last20=20, as_of=2026-06-24T21:00:00+00:00
- These checks are historical context only, not a prediction or guarantee.

## Evidence
- GGCC.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Giza General - Contracting and Real Estate Investment S.A.E summary=EGX approves listing EGP 144m capital increase for Giza Contracting; Giza Contracting tests key EGP 0.51 level; Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25
  - EGX approves listing EGP 144m capital increase for Giza Contracting: https://english.mubasher.info/news/4588793/EGX-approves-listing-EGP-144m-capital-increase-for-Giza-Contracting/
  - Giza Contracting tests key EGP 0.51 level: https://english.mubasher.info/news/4563778/Giza-Contracting-tests-key-EGP-0-51-level/
  - Giza Contracting’s consolidated net profits leap to EGP 140m in 9M-25: https://english.mubasher.info/news/4530408/Giza-Contracting-s-consolidated-net-profits-leap-to-EGP-140m-in-9M-25/
- LCSW.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Lecico Egypt summary=Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- CSAG.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Canal Shipping Agencies summary=Canal Shipping Agencies targets EGP 970m net profits in FY26/27; Canal Shipping Agencies’ stock rebounds; Canal Shipping Agencies mulls EGP 100m capital raise
  - Canal Shipping Agencies targets EGP 970m net profits in FY26/27: https://english.mubasher.info/news/4582423/Canal-Shipping-Agencies-targets-EGP-970m-net-profits-in-FY26-27/
  - Canal Shipping Agencies’ stock rebounds: https://english.mubasher.info/news/4564447/Canal-Shipping-Agencies-stock-rebounds/
  - Canal Shipping Agencies mulls EGP 100m capital raise: https://english.mubasher.info/news/4191441/Canal-Shipping-Agencies-mulls-EGP-100m-capital-raise/
- ENGC.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Industrial Engineering Company for Construction and Development (ICON) (S.A.E) summary=Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- GTWL.CA: status=ACCEPTED_UNDATED latest=n/a age_days=n/a sources=3 expected=Golden Textiles & Clothes Wool summary=Golden Textiles profits jump 214%; Golden Textiles OGM OKs 50 piasters/shr dividends; Golden Textiles consolidated profits down 18.5% in FY16
  - Golden Textiles profits jump 214%: https://english.mubasher.info/news/3108548/Golden-Textiles-profits-jump-214-/
  - Golden Textiles OGM OKs 50 piasters/shr dividends: https://english.mubasher.info/news/3103061/Golden-Textiles-OGM-OKs-50-piasters-shr-dividends/
  - Golden Textiles consolidated profits down 18.5% in FY16: https://english.mubasher.info/news/3092552/Golden-Textiles-consolidated-profits-down-18-5-in-FY16/
- RAYA.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=543 sources=3 expected=Raya Holding summary=Raya stock maintains bullish momentum above EGP 9; Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt; Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn
  - Raya stock maintains bullish momentum above EGP 9: https://english.mubasher.info/news/4601857/Raya-stock-maintains-bullish-momentum-above-EGP-9/
  - Aman Holding, MSMEDA partner to inject EGP 300m into SMEs across Egypt: https://english.mubasher.info/news/4577815/Aman-Holding-MSMEDA-partner-to-inject-EGP-300m-into-SMEs-across-Egypt/
  - Raya Holding’s consolidated profits surge in 2025; revenues hit EGP 63.8bn: https://english.mubasher.info/news/4564195/Raya-Holding-s-consolidated-profits-surge-in-2025-revenues-hit-EGP-63-8bn/
- ETRS.CA: status=REJECTED_TICKER_MISMATCH latest=n/a age_days=n/a sources=0 expected=Egyptian Transport and Commercial Services Company S.A.E. summary=Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- CNFN.CA: status=OLD_ACCEPTED latest=2025-01-01 age_days=543 sources=3 expected=Contact Financial Holding summary=Contact’s consolidated profits approach EGP 471m in 2025; Contact logs lower consolidated net profits at EGP 291m in 9M-25; Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem
  - Contact’s consolidated profits approach EGP 471m in 2025: https://english.mubasher.info/news/4582855/Contact-s-consolidated-profits-approach-EGP-471m-in-2025/
  - Contact logs lower consolidated net profits at EGP 291m in 9M-25: https://english.mubasher.info/news/4526894/Contact-logs-lower-consolidated-net-profits-at-EGP-291m-in-9M-25/
  - Contact, e&amp; money forge partnership to boost Egypt’s financial ecosystem: https://english.mubasher.info/news/4509412/Contact-e-money-forge-partnership-to-boost-Egypt-s-financial-ecosystem/

## Warnings
- Evidence for GGCC.CA matches the company but no source/report date was detected.
- Gemini grounding skipped because market regime is defensive; local fallback evidence used.
- Evidence rejected for LCSW.CA: source text did not clearly match LCSW.CA / Lecico Egypt.
- Evidence for CSAG.CA matches the company but no source/report date was detected.
- Evidence rejected for ENGC.CA: source text did not clearly match ENGC.CA / Industrial Engineering Company for Construction and Development (ICON) (S.A.E).
- Evidence for GTWL.CA matches the company but no source/report date was detected.
- Evidence for RAYA.CA matches the company but appears old; latest detected date is 2025-01-01.
- Evidence rejected for ETRS.CA: source text did not clearly match ETRS.CA / Egyptian Transport and Commercial Services Company S.A.E..
- Evidence for CNFN.CA matches the company but appears old; latest detected date is 2025-01-01.
